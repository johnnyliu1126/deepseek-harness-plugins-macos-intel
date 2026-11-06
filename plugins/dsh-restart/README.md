# dsh-restart

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.0.0` · **License / 许可证:** `MIT`

## Source and attribution

Author / 作者: Undeclared in original manifest / 原清单未声明


Local source included with provenance; no missing license or author is fabricated. / 本地源码附来源说明，不虚构缺失许可证或作者。

## Features

- Persistent entry: sidebar footer button with an icon in collapsed mode.
- Restart flow: POST route launches a detached shell that terminates and relaunches the application.
- Diagnostics: state/log routes, dryRun preview and a 10-second duplicate-request debounce.
- Reconnect: browser polling reloads after host recovery; a real restart interrupts active tasks.

## Installation and removal

```sh
python3 ../../scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-restart
python3 ../../scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-restart --apply --fetch
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `DSH_RESTART_APP_PATH` | `/Applications/DeepSeek Harness.app` | Application bundle / 应用路径 |
| `DSH_RESTART_DELAY_MS` | `700` | Delay before termination / 退出延迟 |
| `DSH_RESTART_DRY_RUN` | `0` | 1 prints the plan / 1 仅预演 |
| `debounce` | `10000 ms` | Host duplicate suppression / 宿主去抖 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Finish active tasks, inspect state/dryRun, then click Restart in the sidebar.

## Permissions and data

Can terminate local application processes and read restart logs.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Restart targets a macOS Desktop .app process; non-desktop requests return 409. Release verification does not actually restart the app.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 1.0.0; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。

Standalone archive installation / 独立压缩包安装：

```sh
dsh plugin --profile YOUR_PROFILE add /absolute/path/to/dsh-restart-1.0.0.tgz
```
