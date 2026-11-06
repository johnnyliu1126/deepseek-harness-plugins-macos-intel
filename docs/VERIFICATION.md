# macOS Intel — Verification scope / 验证范围

This edition targets `Darwin x64`. Its [Actions runs](https://github.com/johnnyliu1126/deepseek-harness-plugins-macos-intel/actions) are the authoritative status for this edition; previous collection-wide runs are historical evidence only.
本版验证目标如上，以本仓库 Actions 实际结果为准；原合集历史检查不能直接代表本版已在目标架构验证。

The workflow checks native Python/Node architecture, catalog/doc links and secret heuristics, installer safety/unit tests, local balance/host-route contracts, local package installation/packing, and full root dependency installation with lifecycle scripts disabled. Wrong-OS/CPU/Node combinations are tested as rejections. Runtime-source hashes remain checked against the original snapshot.
工作流检查原生架构、文档与敏感信息、安装器测试、余额和接口、本地包安装打包，以及禁用生命周期脚本的完整根依赖安装；同时测试拒绝错误系统/架构。原运行源码保持哈希验证。

Before publishing, the Intel development machine ran the platform guard tests for all editions. Native apply tests are skipped locally for other target architectures, then executed on the matching CI runner. No cross-architecture success is claimed from a skipped test.
发布前 Intel 开发机执行各版 guard 测试；不同目标平台的实际写入测试仅在本机跳过，随后由匹配 CI 执行。跳过不算跨架构通过。

Known upstream issues remain: four disabled Web UI children; mobile React ^19.3.0 versus original resolved 18.3.1; purge retired-row composition warnings; undeclared/conflicting licenses. The balance calendar is a local 2026 algorithm rather than a live official pricing feed.
四个 UI 子项禁用、手机 React peer 不匹配、purge 旧条目提示、许可证缺失/冲突等上游问题仍保留。余额日历不是官方实时价格源。

Not exercised: authenticated balance queries, live application restart, bot messaging, browser-cookie import, actual phone pairing, public tunnel exposure, notification delivery or every UI/backend combination. Installing the dependency graph does not mean these work.
未执行真实账号余额请求、桌面重启、机器人消息、Cookie 导入、手机配对、公开隧道、通知以及全部 UI/后端组合。依赖安装通过不代表这些功能已验证。

The edition does not modify the operator’s active DSH profiles or credentials.
此版本开发与验证未修改操作者正在使用的 DSH Profile 或凭据。
