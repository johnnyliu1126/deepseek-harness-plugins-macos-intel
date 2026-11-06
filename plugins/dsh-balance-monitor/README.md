# dsh-balance-monitor

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.0.0` · **License / 许可证:** `UNDECLARED`

## Source and attribution

Author / 作者: Undeclared in original manifest / 原清单未声明


Local source included with provenance; no missing license or author is fabricated. / 本地源码附来源说明，不虚构缺失许可证或作者。

## Features

- Balances: query host deepseekAccount; show recharge, bonus and total per currency.
- Refresh: 60-second default, 30/60/120/300 options, manual refresh, request merging and a 3-second throttle.
- Alert: default threshold 10 highlights low balances; settings persist in localStorage.
- Timing: Beijing-time workday windows/countdown with hardcoded 2026 holidays; not an official live pricing feed.
- Failure states: signed out, unsupported and failed are distinct; failures do not display zero balances.

## Installation and removal

```sh
python3 ../../scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-balance-monitor
python3 ../../scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-balance-monitor --apply --fetch
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `刷新间隔 / interval` | `60 s` | 30, 60, 120, 300; localStorage dshbm-interval |
| `低余额阈值 / threshold` | `10` | localStorage dshbm-threshold |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Sign in through the host account UI and open a session; click the balance below the composer to expand settings.

## Permissions and data

Uses the host account service without storing account credentials.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check host sign-in/account service. Holiday dates outside 2026 are unknown. No API-key mode, spending history or session estimates. Test: `node --test core.test.js`.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 1.0.0; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。

Standalone archive installation / 独立压缩包安装：

```sh
dsh plugin --profile YOUR_PROFILE add /absolute/path/to/dsh-balance-monitor-1.0.0.tgz
```
