# @tt-a1i/archify-dsh

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.0.0` · **License / 许可证:** `MIT`

## Source and attribution

Author / 作者: tt-a1i (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)


This collection documents upstream work; third-party runtime source is not copied.

## Features

- Architecture skill: exposes Archify via a filesystem skill provider; invoke it by name.
- Structured artifacts: specification JSON and HTML diagrams with components, a main path and trust boundaries.
- Lightweight adapter: no extra native tools or Web UI; bundles Archify 3.0.1 independently of adapter version.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add @tt-a1i/archify-dsh@1.0.0
dsh plugin --profile YOUR_PROFILE remove @tt-a1i/archify-dsh
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `archify-plugin` | `packaged skills root` | Filesystem provider; no custom settings / 文件系统技能提供器 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Ask: “Use the archify skill to map this repository’s runtime architecture; return the JSON and HTML paths.”

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Upstream adapter acceptance targets DSH 0.1.2-rc.1 and Node ^22.19.0 or >=24; retest other hosts.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 1.0.0; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
