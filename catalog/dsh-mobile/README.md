# dsh-mobile

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.8.2` · **License / 许可证:** `Apache-2.0`

## Source and attribution

Author / 作者: saya-ch (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/saya-ch/dsh-mobile](https://github.com/saya-ch/dsh-mobile)


This collection documents upstream work; third-party runtime source is not copied.

## Features

- Mobile sessions: shared workspaces/messages/tools with touch-oriented composer, drawer and question cards.
- Clients: Android application and mobile browser/PWA, with customizable UI and device lists.
- Pairing: QR/link/key setup, multi-device reachability, switching, re-pairing and local-record removal.
- Networking: LAN, Tailscale, cpolar, Cloudflare, FRP, own proxy and Caddy; iroh is experimental and platform-limited.
- Notifications: iOS Home Screen Web Push and Android native alerts require explicit opt-in.
- Diagnostics/security: redacted connection reports, device credentials, Origin binding and per-path third-party WebSocket approvals.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add dsh-mobile@0.8.2
dsh plugin --profile YOUR_PROFILE remove dsh-mobile
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `pairing / network` | `configure in plugin UI` | Local credentials are never exported / 配对凭据不导出 |
| `notifications` | `explicit opt-in` | Platform requirements apply / 受平台限制 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Open mobile-access settings, choose LAN or a remote transport and scan the pairing code; keep credentials local.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 0.8.2; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。

**Observed peer warning / 实测依赖警告:** `dsh-mobile@0.8.2` requests React `^19.3.0`; the isolated dependency graph selected `18.3.1`. Installation succeeded, but mobile UI compatibility is not certified. / 安装成功，但手机 UI 兼容性未认证；未强行替换宿主 React。
