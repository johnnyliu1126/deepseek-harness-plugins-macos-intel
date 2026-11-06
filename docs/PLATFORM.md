# macOS Intel — Platform contract / 平台约定

Target / 目标: `Darwin` / `x64`. Node.js 24 native architecture required by CI.

`platform.json` identifies the edition. `scripts/platform_support.py` validates Python/Node architecture. `scripts/collection.py --apply` refuses an OS/architecture mismatch before creating the target parent or staging directory. Dry plans can be viewed from another platform. A process-architecture check is not a physical-device attestation; on Apple Silicon use the native arm64 edition instead of mixing Rosetta runtimes.
平台清单标识版本，安装前检查 Python/Node 进程架构；不匹配时在写入前拒绝。其他平台仍可查看只读计划。检查的是运行时，不是物理硬件认证；M 系列应使用原生 arm64 版本。

Included / 收录: 19 packages, 12 roots, 2 local source packages. Excluded / 排除: No additional package exclusions / 无额外排除.

Built-in DSH components are prerequisites, never copied. No architecture-specific binary is copied from the source computer: upstream packages fetch their own components for the target platform, subject to upstream availability and setup. The absence of os/cpu restrictions in package metadata is not evidence that every native backend works.
不复制官方宿主组件或来源机器上的架构二进制；第三方组件按其上游机制获取。包未声明 os/cpu 限制不代表所有原生后端均兼容。

Mobile / 手机访问: macOS: LAN/cloudflared/FRP/own proxy; no managed Funnel/cpolar/Caddy/iroh in this pinned version. / 此固定版本不提供托管的 macOS Funnel、cpolar、Caddy、iroh。

CI runner: `macos-15-intel`. Labels verified against [GitHub runner documentation](https://docs.github.com/en/actions/reference/runners/github-hosted-runners). Runner OS images differ from real users’ Desktop environments; CI does not certify UI, accounts, phone notifications or live tunnel connectivity.
Runner 标签已按官方文档核对；CI 环境与用户桌面环境不同，不能认证 UI、账号、手机通知或隧道连通性。

Source / 来源: https://github.com/johnnyliu1126/deepseek-harness-plugin-collection at `c10c4436740e8d462215f361d3a8e18b3801d326`. Platform edits change installation/packaging/docs/tests, not the imported balance/restart runtime source. Windows deliberately omits restart rather than offering an untested Windows implementation.
平台改动仅涉及安装、打包、文档和测试，未改写原运行源码；Windows 直接排除 restart，不冒充已实现 Windows 重启。
