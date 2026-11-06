# dsh-client-liang-intensity-skin

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.1.6` · **License / 许可证:** `UNDECLARED`

## Source and attribution

Author / 作者: kingOfSoySauce (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/kingOfSoySauce/dsh-liang-skin](https://github.com/kingOfSoySauce/dsh-liang-skin)


This collection documents upstream work; third-party runtime source is not copied.

## Features

- Reasoning slider: maps the model’s actual reasoning.efforts evenly to 0–30.
- Commit behavior: drag previews; release, keyboard completion or blur snaps and commits the original effort ID.
- Visibility: hidden for unsupported/single-effort models and addressed subagents.
- Appearance: themed mode adds characters/background/colors; native mode restores the host UI.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add dsh-client-liang-intensity-skin@0.1.6
dsh plugin --profile YOUR_PROFILE remove dsh-client-liang-intensity-skin
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `appearance` | `user-selected` | Themed/native; effort values come from model / 皮肤与原生；档位由模型决定 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Enable the skin in appearance settings; select a model with multiple reasoning efforts, drag and release the slider.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 0.1.6; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
