/**
 * dsh-restart —— Host 半区
 *
 * 只做一件事：让「重启 DeepSeek Harness」变成一个可以被界面按钮、脚本、curl
 * 同时触发的动作，并且是**真的整棵树重启**（应用 + Host + 所有 helper），
 * 而不是只重载插件。
 *
 * 为什么重启要借外部脚本（bin/restart.sh）：
 *   重启的意思是「把我自己也杀掉」，宿主进程没法在自己身上完成这件事。
 *   所以这里只负责 spawn 一个 detached 的 shell，它先睡几百毫秒让 HTTP 响应回到
 *   浏览器，然后结束整棵应用进程树并重新 open 应用；宿主随应用一起退出。
 *
 * 路由：
 *   GET  /dsh-restart/state    当前运行环境（应用路径、主进程/Host pid、上次重启记录）
 *   POST /dsh-restart/restart  触发重启；body {trigger?, dryRun?}
 *   GET  /dsh-restart/log      重启脚本的日志尾巴
 *
 * 这些路由挂在宿主自己的 HTTP 服务器上，本机任何页面都能直连，所以重启接口只接受
 * 「没有跨站来源」的调用（见 callerAllowed）：外部网页的 POST 自带真实 Origin，直接被挡。
 */

import { spawn } from 'node:child_process'
import { appendFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'
import { fileURLToPath } from 'node:url'

export const name = 'dsh-restart'

/** 需要的服务：宿主 HTTP 服务器。 */
export const inject = ['webServer']

const DSH_HOME = process.env.DSH_HOME || join(homedir(), '.dsh')
const STATE_DIR = join(DSH_HOME, 'dsh-restart')
const STATE_FILE = join(STATE_DIR, 'state.json')
const LOG_FILE = join(STATE_DIR, 'restart.log')
const SCRIPT = fileURLToPath(new URL('./bin/restart.sh', import.meta.url))

/** 结束进程前的等待：留给「触发重启那次请求」的响应穿回界面。 */
const RESTART_DELAY_MS = 700
/** 两次点击之间的去抖窗口，避免连点拉起多个重启脚本。 */
const DEBOUNCE_MS = 10_000

const HOST_PID = process.pid
const APP_PID = process.ppid
const APP_BUNDLE = detectAppBundle(process.execPath)
const IS_DESKTOP = APP_BUNDLE !== undefined

let pendingRestart = null

function detectAppBundle(execPath) {
  if (typeof execPath !== 'string') return undefined
  // .../DeepSeek Harness.app/Contents/MacOS/DeepSeek Harness
  const matched = /^(.*?\.app)\/Contents\/MacOS\//u.exec(execPath)
  return matched === null ? undefined : matched[1]
}

function readState() {
  try {
    const parsed = JSON.parse(readFileSync(STATE_FILE, 'utf8'))
    return parsed !== null && typeof parsed === 'object' ? parsed : {}
  } catch {
    return {}
  }
}

function writeState(patch) {
  const next = { ...readState(), ...patch }
  try {
    mkdirSync(STATE_DIR, { recursive: true })
    writeFileSync(STATE_FILE, JSON.stringify(next, undefined, 2), 'utf8')
  } catch {
    /* 写不进去不影响重启本身 */
  }
  return next
}

function logLine(text) {
  try {
    mkdirSync(STATE_DIR, { recursive: true })
    appendFileSync(LOG_FILE, `${new Date().toISOString()} [host] ${text}\n`, 'utf8')
  } catch {
    /* 忽略 */
  }
}

function sendJson(res, status, payload) {
  res.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-store',
  })
  res.end(JSON.stringify(payload))
}

async function readBody(req) {
  const chunks = []
  for await (const chunk of req) chunks.push(chunk)
  return Buffer.concat(chunks).toString('utf8')
}

/**
 * 重启是能在本机杀掉一整个应用的副作用，所以只接受「没有跨站来源」的调用：
 *   - curl / 脚本 / 桌面渲染进程（file://）：没有 Origin，或 Origin 为 null；
 *   - 同一台机器上的 web 界面：Origin 是本机回环地址。
 * 任何外部网页发的 POST 都自带真实 Origin，会在这一步被挡住（不依赖预检）。
 */
function callerAllowed(req) {
  const origin = req.headers.origin
  if (origin === undefined) return true
  if (origin === 'null') return true
  return /^https?:\/\/(?:127\.0\.0\.1|localhost|\[::1\])(?::\d+)?$/iu.test(String(origin))
}

function envForScript(dryRun) {
  return {
    ...process.env,
    DSH_RESTART_APP_PATH: APP_BUNDLE ?? '',
    DSH_RESTART_APP_PID: String(APP_PID),
    DSH_RESTART_HOST_PID: String(HOST_PID),
    DSH_RESTART_LOG: LOG_FILE,
    DSH_RESTART_DELAY_MS: String(RESTART_DELAY_MS),
    DSH_RESTART_DRY_RUN: dryRun ? '1' : '0',
  }
}

/**
 * 拉起重启脚本。
 * detached + stdio:'ignore' 是关键：宿主随时会被这个脚本杀掉，脚本必须是独立进程组的孤儿。
 */
function spawnRestart(dryRun) {
  const child = spawn('/bin/bash', [SCRIPT], {
    cwd: DSH_HOME,
    env: envForScript(dryRun),
    detached: true,
    stdio: 'ignore',
  })
  child.unref()
  return child.pid
}

export function apply(ctx) {
  ctx.webServer.register({
    kind: 'exact',
    path: '/dsh-restart/state',
    handler: async (_req, res) => {
      const state = readState()
      sendJson(res, 200, {
        ok: true,
        desktop: IS_DESKTOP,
        appPath: APP_BUNDLE ?? null,
        appPid: APP_PID,
        hostPid: HOST_PID,
        platform: process.platform,
        version: process.env.DSH_CLIENT_VERSION ?? null,
        profile: process.env.DSH_PROFILE ?? null,
        uptimeMs: Math.round(process.uptime() * 1000),
        script: SCRIPT,
        logPath: LOG_FILE,
        lastRestart: state.lastRestart ?? null,
        pending: pendingRestart !== null && Date.now() - pendingRestart < DEBOUNCE_MS,
      })
    },
  })

  ctx.webServer.register({
    kind: 'exact',
    path: '/dsh-restart/restart',
    handler: async (req, res) => {
      if (req.method !== 'POST') {
        res.writeHead(405, { Allow: 'POST', 'Content-Type': 'application/json; charset=utf-8' })
        res.end(JSON.stringify({ ok: false, error: '只支持 POST' }))
        return
      }
      if (!callerAllowed(req)) {
        sendJson(res, 403, { ok: false, error: '拒绝：请求来自非本机界面' })
        return
      }

      let body = {}
      try {
        const text = (await readBody(req)).trim()
        if (text.length > 0) body = JSON.parse(text)
      } catch {
        sendJson(res, 400, { ok: false, error: 'body 不是合法 JSON' })
        return
      }

      const dryRun = body?.dryRun === true
      const trigger = typeof body?.trigger === 'string' ? body.trigger : 'unknown'

      if (!IS_DESKTOP) {
        sendJson(res, 409, {
          ok: false,
          error: `当前不是桌面应用（execPath: ${process.execPath}），没有可重启的 .app 包`,
        })
        return
      }
      if (!existsSync(SCRIPT)) {
        sendJson(res, 500, { ok: false, error: `重启脚本缺失：${SCRIPT}` })
        return
      }
      if (!dryRun && pendingRestart !== null && Date.now() - pendingRestart < DEBOUNCE_MS) {
        sendJson(res, 200, { ok: true, duplicate: true, appPath: APP_BUNDLE, appPid: APP_PID })
        return
      }

      let pid = null
      try {
        pid = spawnRestart(dryRun)
      } catch (error) {
        sendJson(res, 500, { ok: false, error: `拉起重启脚本失败：${String(error?.message ?? error)}` })
        return
      }

      if (dryRun) {
        logLine(`dry-run requested by ${trigger}`)
        sendJson(res, 200, {
          ok: true,
          dryRun: true,
          appPath: APP_BUNDLE,
          appPid: APP_PID,
          hostPid: HOST_PID,
          script: SCRIPT,
          delayMs: RESTART_DELAY_MS,
        })
        return
      }

      pendingRestart = Date.now()
      logLine(`restart requested by ${trigger} (script pid ${pid ?? 'unknown'})`)
      writeState({
        lastRestart: {
          at: new Date().toISOString(),
          trigger,
          appPid: APP_PID,
          hostPid: HOST_PID,
          appPath: APP_BUNDLE,
        },
      })

      sendJson(res, 200, {
        ok: true,
        appPath: APP_BUNDLE,
        appPid: APP_PID,
        hostPid: HOST_PID,
        delayMs: RESTART_DELAY_MS,
        logPath: LOG_FILE,
      })
    },
  })

  ctx.webServer.register({
    kind: 'exact',
    path: '/dsh-restart/log',
    handler: async (req, res) => {
      const url = new URL(req.url ?? '/', 'http://dsh.local')
      const wanted = Number.parseInt(url.searchParams.get('lines') ?? '80', 10)
      const limit = Number.isFinite(wanted) ? Math.min(Math.max(wanted, 1), 1000) : 80
      let lines = []
      try {
        lines = readFileSync(LOG_FILE, 'utf8').trimEnd().split('\n').slice(-limit)
      } catch {
        /* 还没有日志 */
      }
      sendJson(res, 200, { ok: true, path: LOG_FILE, lines })
    },
  })

  logLine(`loaded: desktop=${IS_DESKTOP} app=${APP_BUNDLE ?? '-'} appPid=${APP_PID} hostPid=${HOST_PID}`)
}
