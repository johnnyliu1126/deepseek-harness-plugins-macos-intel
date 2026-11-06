# Additional integrations / 额外集成

These are recorded separately from plugin packages. Built-in DSH MCP clients and hook bridges are host prerequisites and are not uploaded. Raw personal configuration, executables and credential files are excluded.
这些集成不算重复插件包。DSH 自带 MCP client 和 hook 桥不上传；原始个人配置、可执行文件和凭据不复制。

| Integration | Observed version / source | 功能 | Function | Restore / 恢复 |
|---|---|---|---|---|
| Playwright MCP | @playwright/mcp 0.0.83; microsoft/playwright-mcp | 浏览器交互、截图、PDF、devtools；本机配置采用 Edge isolated | Browser interaction, screenshots, PDF and devtools; observed Edge isolated setup | Install the pinned server separately and point a local DSH MCP row at its CLI / 单独安装并配置本地启动路径 |
| Context7 MCP | @upstash/context7-mcp 4.4.4; upstash/context7 | 查询库与开发文档 | Library/documentation lookup | Install server and configure stdio locally / 配置 stdio |
| GitHub MCP | github/github-mcp-server; binary version not queried | 仓库、Issue、PR 等，权限以本地 Token 为准 | Repository, issue and PR access subject to token scopes | Obtain upstream binary; set credentials locally, never commit them / 使用上游二进制，本地配置凭据 |
| REA MCP | local REA checkout/CLI; version not verified | 逆向分析工具服务 | Reverse-engineering analysis server | Build/install the original REA project and configure `rea mcp` / 单独构建或安装原项目 |

Upstream references: [Playwright](https://github.com/microsoft/playwright-mcp), [Context7](https://github.com/upstash/context7), [GitHub MCP](https://github.com/github/github-mcp-server). These are references to observed integrations, not claims of successful remote authentication. No MCP binary is redistributed.
上述链接指向上游，不表示本次已验证远程登录。未分发 MCP 二进制。

## Local skills / 本地技能

Six loose skill folders were observed outside plugin bundles. Their author/license metadata was not established, so only their workflow purpose is recorded; source is not reattributed or redistributed. Plugin-provided skills, such as Archify and the purge workbench, remain part of their upstream packages.
发现六个独立技能目录，作者和许可证未确认，只记录用途；不将其标为本仓库原创。Archify 与 purge 附带技能由各自上游包提供。

| Skill | 中文用途 | English purpose |
|---|---|---|
| commit | 检查 diff、提交信息与敏感文件 | Review diffs, commit messages and sensitive-file exclusions |
| verify | 执行验证并基于实际输出报告结果 | Run checks and report evidence from actual outputs |
| webapp-test | 使用 Playwright 检查网页交互 | Exercise web interactions through Playwright |
| code-review | 按严重程度与源码位置审查改动 | Review changes with severity and source locations |
| refactor | 在行为不变与测试基线下渐进重构 | Refactor incrementally against a behavioral baseline |
| debug | 复现、隔离、根因、修复与回归 | Reproduce, isolate, diagnose, fix and regress |

## Excluded private state / 排除的私人状态

Account credentials, API keys, bot tokens, mobile pairing records, CA/server private keys, session history, attachments, logs, backups, browser cookies, tunnel state, local prompt text and model downloads are not part of the collection. Recreate only the needed integration on the destination machine.
账号凭据、API Key、机器人 Token、手机配对、CA/服务器私钥、聊天、附件、日志、备份、浏览器 Cookie、隧道状态、个人提示词和模型下载都不进入合集；在目标机器按需重新配置。
