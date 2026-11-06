# @liustack/modsearch

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `5.10.11` · **License / 许可证:** `MIT`

## Source and attribution

Author / 作者: Leon Liu

Upstream / 上游: [https://github.com/liustack/modsearch](https://github.com/liustack/modsearch)


This collection documents upstream work; third-party runtime source is not copied.

## Features

- Web search/fetch: search and page text for models without native web access.
- Engines: Firecrawl, Keenable, You.com, Antigravity, Tavily, Exa and local fetch.
- X search: available through a configured, authenticated Grok Build installation.
- Fallback/key rotation: switch failed channels; advertised free quotas are upstream claims and may change.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add @liustack/modsearch@5.10.11
dsh plugin --profile YOUR_PROFILE remove @liustack/modsearch
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

Configure through the plugin settings UI. The pinned upstream implementation is authoritative for complete fields/defaults; missing defaults are not guessed.

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Ask the agent to search the web or fetch a page; configure engines through the upstream CLI when needed.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 5.10.11; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
