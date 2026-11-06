# dsh-prompt-enhancer

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.2.2` · **License / 许可证:** `MIT`

## Source and attribution

Author / 作者: MCJF28

Upstream / 上游: [https://github.com/MCJF28/dsh-prompt-enhancer](https://github.com/MCJF28/dsh-prompt-enhancer)


This collection documents upstream work; third-party runtime source is not copied.

## Features

- Draft optimization: a composer button rewrites the draft before sending, with edit/undo opportunities.
- Instruction modes: concise, balanced (default), detailed and custom, with a short-chat over-expansion retry.
- Model routing: shared free channel, current model or fixed model; fallback may consume paid conversation quota.
- Diagnostics: settings test the channel and show the last actual route; settings are stored locally.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add dsh-prompt-enhancer@1.2.2
dsh plugin --profile YOUR_PROFILE remove dsh-prompt-enhancer
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `mode` | `balanced` | concise / balanced / detailed / custom |
| `DSH_FREE_CHANNEL_BASE_URL` | `upstream default` | Endpoint override / 覆盖端点 |
| `DSH_FREE_CHANNEL_API_KEY` | `unset` | Local environment only / 仅本地环境变量 |
| `DSH_FREE_CHANNEL_MODEL` | `upstream default` | Model override / 覆盖模型 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Type a draft, click Optimize, choose instruction/model modes in settings, then review before sending.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 1.2.2; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
