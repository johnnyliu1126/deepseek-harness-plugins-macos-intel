# dsh-purge-community

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.6.60` · **License / 许可证:** `MIT`

## Source and attribution

Author / 作者: kingcharleslzy-ai

Upstream / 上游: [https://github.com/kingcharleslzy-ai/dsh-purge](https://github.com/kingcharleslzy-ai/dsh-purge)

- Contributor / 贡献者: 小杨 / YuJunZhiXue (original dsh-purge author)
- Contributor / 贡献者: luowang-ui
- Contributor / 贡献者: heigit
- Contributor / 贡献者: OGHong
- Contributor / 贡献者: loLollipop
- Contributor / 贡献者: youki258
- Contributor / 贡献者: SimonQvQ

Original project / 原项目: [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge). Community fork maintained by kingcharleslzy-ai.

This collection documents upstream work; third-party runtime source is not copied.

## Features

- Status diagnostics: inspect patch and host evidence; a read failure is not an absent installation.
- Prompt and rule management: per-preset text, ordering, exclusions, and one-shot injection controls.
- Patch lifecycle: local backups, apply/revert and version management; host modification requires an explicit separate action.
- Lab workbench: packaged presets, skills, SQLite evidence store and /redteam/api bridge.
- Retry/continue: configurable retry limits and continuation text; success is not guaranteed.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add https://github.com/kingcharleslzy-ai/dsh-purge/releases/download/v1.6.60/dsh-purge-community-1.6.60.tgz
dsh plugin --profile YOUR_PROFILE remove dsh-purge-community
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `autoApplyOnStart / autoUpdateOnStart` | `false` | Explicit lifecycle controls / 显式生命周期控制 |
| `autoRetry / retryMax` | `true / 3` | Retry controls / 重试 |
| `autoContinue / continueMax` | `false / 3` | Continuation controls / 继续 |
| `postPrompt` | `empty` | Local prompt text / 本地提示词 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Open the plugin sidebar status page; inspect evidence/backups before explicitly applying or reverting patches.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 1.6.60; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
