# dsh-lark-channel

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.0.7` · **License / 许可证:** `BSD-3-Clause`

## Source and attribution

Author / 作者: omdsh-dev (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/omdsh-dev/dsh-lark](https://github.com/omdsh-dev/dsh-lark)


This collection documents upstream work; third-party runtime source is not copied.

## Features

- Chat-driven agents: Feishu/Lark messages launch host tasks with separate reasoning/tool/result views.
- Durable sessions: chat/thread/sender scopes, /new reset and /sessions continuation.
- Workspace/model controls: /ws, /cd, /model, /status and /stop.
- Interactive cards: questions, plan reviews and tool approvals subject to configured approvers.
- Multiple bots: separate credentials/sessions, botPeers allowlists and botHops loop bounds.
- File transfer: workspace inbox and per-send group approval, with a default 20 MiB per-file limit.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add dsh-lark-channel@0.0.7
dsh plugin --profile YOUR_PROFILE remove dsh-lark-channel
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `sessionScope` | `see upstream schema` | chat / chat-thread / chat-sender |
| `botHops` | `6` | Maximum bot-to-bot hops / 机器人连续对话上限 |
| `attachImages` | `false` | Enable only for vision models / 仅视觉模型启用 |
| `receiveFiles / sendFiles` | `true` | Group sends require approval / 群聊发送仍需批准 |
| `maxReceiveFileBytes / maxSendFileBytes` | `20 MiB` | Per-direction size limits / 双向单文件大小限制 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Provision a Feishu/Lark application with local credentials using the upstream guide; send /status or /help in its chat.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 0.0.7; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
