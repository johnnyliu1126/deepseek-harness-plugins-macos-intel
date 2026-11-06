# Architecture / 架构

`platform.json`: target OS and process architecture.
`scripts/platform_support.py`: native Python/Node checks and Windows .cmd invocation.
`scripts/collection.py`: read-only plan, then checked staging and integrity-verified installation into a new profile.
`catalog.lock.json`: 19 versioned extra plugin entries and upstream integrity/attribution.
`plugins/`: 2 imported local source package(s); unchanged runtime implementations.
`catalog/`, `docs/`, `licenses/`: bilingual functionality, platform limits and original licensing evidence.

The active Desktop profile is never overwritten. Built-in DSH source and private state are excluded. See [platform contract](PLATFORM.md) and [verification scope](VERIFICATION.md).
不覆盖现有配置，不上传自带源码与私人状态，平台边界和验证范围见链接。
