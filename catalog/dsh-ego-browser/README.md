# dsh-ego-browser

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.9.8` · **License / 许可证:** `MIT`

## Source and attribution

Author / 作者: Fisfzy (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/Fisfzy/dsh-ego-browser](https://github.com/Fisfzy/dsh-ego-browser)


This collection documents upstream work; third-party runtime source is not copied.

## Features

- Browser tools: ego_* tools drive the bundled ego-lite runtime for navigation and interaction.
- Live panel: SSE screencast, direct mouse control, tabs, download capture and human-verification notices.
- Login import: Chrome/Edge bridge or non-destructive profile copies; login data is excluded here.
- Host variants: Web side panel, optional TUI text UI and tools-only headless use.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add dsh-ego-browser@0.9.8
dsh plugin --profile YOUR_PROFILE remove dsh-ego-browser
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `chromePath` | `auto-detect` | Set only to an existing local browser / 本地浏览器路径 |
| `defaultSpace` | `empty` | Runtime space / 运行时空间 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Request browser navigation in a session and watch the side panel; use upstream login-import setup if needed.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 0.9.8; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。

[Tool-by-tool reference / 逐工具说明](../../docs/BROWSER-TOOLS.md)
