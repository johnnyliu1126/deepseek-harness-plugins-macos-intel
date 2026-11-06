# dsh-restart

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.0.0` · **License / 许可证:** `MIT`

## 来源与署名

Author / 作者: Undeclared in original manifest / 原清单未声明


Local source included with provenance; no missing license or author is fabricated. / 本地源码附来源说明，不虚构缺失许可证或作者。

## 功能

- 常驻入口：侧边栏页脚文字按钮，窄栏降级为图标。
- 重启过程：POST 路由调用 detached shell，延迟退出整棵应用进程并重新打开。
- 状态与日志：state 和 log 接口，dryRun 预演和 10 秒重复请求去抖。
- 重连：浏览器轮询宿主返回后刷新；实际重启会打断进行中的任务。

## 安装与卸载

```sh
python3 ../../scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-restart
python3 ../../scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-restart --apply --fetch
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `DSH_RESTART_APP_PATH` | `/Applications/DeepSeek Harness.app` | Application bundle / 应用路径 |
| `DSH_RESTART_DELAY_MS` | `700` | Delay before termination / 退出延迟 |
| `DSH_RESTART_DRY_RUN` | `0` | 1 prints the plan / 1 仅预演 |
| `debounce` | `10000 ms` | Host duplicate suppression / 宿主去抖 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

先完成正在进行的任务；查看状态或 dryRun，再点击侧栏“重启”。

## 权限与数据

可终止本机应用进程并读取重启日志。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

仅 macOS Desktop 的 .app 进程可重启；非桌面请求返回 409。此次验证不会真的重启应用。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 1.0.0; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。

Standalone archive installation / 独立压缩包安装：

```sh
dsh plugin --profile YOUR_PROFILE add /absolute/path/to/dsh-restart-1.0.0.tgz
```
