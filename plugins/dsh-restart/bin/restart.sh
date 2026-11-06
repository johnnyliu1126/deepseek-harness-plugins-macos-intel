#!/bin/bash
#
# dsh-restart —— 重启 DeepSeek Harness 桌面应用
#
# 两种用法：
#   1. 由 dsh-restart 插件的 Host 半区以 detached 方式拉起（推荐，界面里点一下就走到这里）；
#   2. 直接在终端执行：bash bin/restart.sh
#
# 流程：
#   等一小会儿（让界面上那次 HTTP 请求拿到响应）→ 结束整棵应用进程树 →
#   轮到没有任何应用进程后再 open 应用 → 等新主进程出现并记日志。
#
# 可覆盖的环境变量：
#   DSH_RESTART_APP_PATH   应用路径（默认 /Applications/DeepSeek Harness.app）
#   DSH_RESTART_APP_PID    主进程 pid（默认按命令行精确匹配自动探测）
#   DSH_RESTART_LOG        日志路径（默认 ~/.dsh/dsh-restart/restart.log）
#   DSH_RESTART_DELAY_MS   结束进程前的等待毫秒数（默认 700，留给 HTTP 响应）
#   DSH_RESTART_DRY_RUN    1 = 只把计划写进日志，不动任何进程

set -u

APP_PATH="${DSH_RESTART_APP_PATH:-/Applications/DeepSeek Harness.app}"
LOG="${DSH_RESTART_LOG:-$HOME/.dsh/dsh-restart/restart.log}"
DELAY_MS="${DSH_RESTART_DELAY_MS:-700}"
DRY_RUN="${DSH_RESTART_DRY_RUN:-0}"

mkdir -p "$(dirname "$LOG")" 2>/dev/null || true

log() {
  printf '%s [%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$$" "$*" >>"$LOG" 2>/dev/null || true
}

# 真实路径：/tmp、/var 这类路径在 macOS 上是符号链接，进程命令行里出现的是展开后的
# /private/... 形式，不解析就对不上进程。
APP_REAL="$(cd "$APP_PATH" 2>/dev/null && pwd -P)"
[ -n "${APP_REAL:-}" ] || APP_REAL="$APP_PATH"

# 应用包里的可执行文件名 = 去掉 .app 后的包名（DeepSeek Harness.app → DeepSeek Harness）。
APP_NAME="$(basename "$APP_PATH" .app)"
MAIN_BINARY="$APP_REAL/Contents/MacOS/$APP_NAME"
# 同一路径的另一种写法（未展开符号链接时）：两个都认，免得把已经在跑的实例当成"没跑"。
MAIN_BINARY_ALT="$APP_PATH/Contents/MacOS/$APP_NAME"

if [ ! -x "$MAIN_BINARY" ]; then
  log "abort: $MAIN_BINARY 不存在或不可执行"
  exit 1
fi

# 主进程的命令行恰好只有二进制路径；宿主进程的命令行后面还挂着一串参数，
# 所以用「整行相等」而不是子串匹配，避免认错进程。
find_main_pid() {
  ps -axo pid=,command= | while read -r pid cmd; do
    if [ "$cmd" = "$MAIN_BINARY" ] || [ "$cmd" = "$MAIN_BINARY_ALT" ]; then
      printf '%s' "$pid"
      break
    fi
  done
}

# 同一应用包里的全部进程。用 ps 而不是 pgrep：Electron 的宿主子进程（
# `... --expose-internals ...`）在 macOS 上 pgrep -f 匹配不到，但 ps 看得到。
# 只认「命令行以应用包路径开头」的进程，避免误伤只是顺带提到这个路径的进程。
list_app_pids() {
  ps -axo pid=,command= | APP_REAL="$APP_REAL" APP_ALT="$APP_PATH" awk '{
    cmd = $0
    sub(/^[ \t]*[0-9]+[ \t]+/, "", cmd)
    if (index(cmd, ENVIRON["APP_REAL"]) == 1 || index(cmd, ENVIRON["APP_ALT"]) == 1) print $1
  }'
}

APP_PID="${DSH_RESTART_APP_PID:-$(find_main_pid)}"

if [ "$DRY_RUN" = "1" ]; then
  log "dry-run: app=$APP_REAL main=${APP_PID:-<none>} delay=${DELAY_MS}ms app_pids=[$(list_app_pids | tr '\n' ' ')]"
  exit 0
fi

log "restart requested: app=$APP_REAL main=${APP_PID:-<none>}"

if [ -z "$APP_PID" ] && [ -z "$(list_app_pids)" ]; then
  log "应用未运行，直接启动"
  open -a "$APP_PATH" </dev/null >>"$LOG" 2>&1 && log "launched"
  exit 0
fi

# 让触发重启的那次 HTTP 响应先回到界面。
sleep "$(printf '%d.%03d' $((DELAY_MS / 1000)) $((DELAY_MS % 1000)))"

if [ -n "$APP_PID" ] && kill -0 "$APP_PID" 2>/dev/null; then
  log "SIGTERM -> $APP_PID"
  kill -TERM "$APP_PID" 2>/dev/null || true
  i=0
  while kill -0 "$APP_PID" 2>/dev/null && [ "$i" -lt 50 ]; do
    sleep 0.2
    i=$((i + 1))
  done
  if kill -0 "$APP_PID" 2>/dev/null; then
    log "主进程未在 10s 内退出，SIGKILL"
    kill -KILL "$APP_PID" 2>/dev/null || true
  fi
fi

# 收掉同一应用包里的其余进程：Host、helper、ego-cast-worker 之类。
# 不清干净的话下一次启动会撞端口（Another DSH instance is running）。
for pass in 1 2 3 4 5 6; do
  list_app_pids | while read -r pid; do
    [ "$pid" = "$$" ] && continue
    kill -TERM "$pid" 2>/dev/null || true
  done
  sleep 0.3
  [ -z "$(list_app_pids)" ] && break
done

list_app_pids | while read -r pid; do
  [ "$pid" = "$$" ] && continue
  log "SIGKILL leftover $pid"
  kill -KILL "$pid" 2>/dev/null || true
done

# 等进程真的从进程表消失，否则 open 只会把正在退出的那个实例激活回来。
i=0
while [ -n "$(list_app_pids)" ] && [ "$i" -lt 50 ]; do
  sleep 0.2
  i=$((i + 1))
done

# 关键一步：宿主进程带着 ELECTRON_RUN_AS_NODE=1 / DSH_DESKTOP_* 这类只该出现在
# 子进程里的变量，原样传给 open 会把新实例也变成无界面进程。清掉再启动。
for var in $(env | awk -F= '/^(ELECTRON_|DSH_|NODE_OPTIONS=)/{print $1}'); do
  unset "$var"
done

sleep 0.4
launched=0
for attempt in 1 2 3; do
  if open -a "$APP_PATH" </dev/null >>"$LOG" 2>&1; then
    log "open -a ok（第 $attempt 次）"
    launched=1
    break
  fi
  log "open -a 失败（第 $attempt 次），稍后重试"
  sleep 0.8
done

if [ "$launched" = "0" ]; then
  log "abort: 三次 open 都失败，请手动启动"
  exit 1
fi

i=0
NEW_PID=""
while [ "$i" -lt 40 ]; do
  NEW_PID="$(find_main_pid)"
  [ -n "$NEW_PID" ] && break
  sleep 0.25
  i=$((i + 1))
done

log "relaunched: main=${NEW_PID:-unknown}"
