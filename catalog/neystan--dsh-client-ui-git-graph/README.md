# @neystan/dsh-client-ui-git-graph

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.1.16` · **License / 许可证:** `Apache-2.0`

## Source and attribution

Author / 作者: neystan

Upstream / 上游: [https://github.com/neystan/dsh-web-ui](https://github.com/neystan/dsh-web-ui)

- Contributor / 贡献者: zhu1090093659 (Original author)

Original project / 原项目: [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui), original npm scope `@linxin666/*`; fork maintained by neystan.

This collection documents upstream work; third-party runtime source is not copied.

## Features

- Branches/graph: a branch selector and commit graph in the session header.
- Git operations: host-side branch creation/switching with guards.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add @neystan/dsh-client-ui-git-graph@0.1.16
dsh plugin --profile YOUR_PROFILE remove @neystan/dsh-client-ui-git-graph
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

Configure through the plugin settings UI. The pinned upstream implementation is authoritative for complete fields/defaults; missing defaults are not guessed.

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Open the corresponding plugin UI and use the features above; see upstream documentation for the complete workflow.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 0.1.16; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
