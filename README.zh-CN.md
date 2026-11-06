> **已迁移 / Superseded:** 本平台版本已合并到 [统一仓库](https://github.com/johnnyliu1126/deepseek-harness-plugin-collection)，请从同一个 [Release 页面](https://github.com/johnnyliu1126/deepseek-harness-plugin-collection/releases/tag/v0.2.0) 下载对应平台包。本仓库仅保留迁移前记录。 / Platform downloads now live in the single canonical repository; this repository is retained only as historical context.

# DeepSeek Harness — macOS Intel

[简体中文](README.zh-CN.md) | [English](README.md) | [平台差异 / Platform details](docs/PLATFORM.md)

本仓库专供 **macOS Intel / x64 运行时**，包括 19 个额外插件条目、12 个顶层安装项、72 条功能说明。提供 2 个本地插件源码包。宿主自带插件不上传，第三方作者、上游链接和许可证保留。

**平台适配不等于全部功能认证。** 安装器会检查操作系统、Python 架构和 Node 架构；实际执行安装时不匹配就拒绝写入。第三方账号、浏览器、手机和桌面 UI 仍需要在目标机器验证。

Intel 版使用 x64 Python 与 Node。本机已有 Intel 环境检查记录，但仍不把第三方在线服务标为全部测试通过。

## 安装与启动

先单独安装对应架构的 DeepSeek Harness、Node.js 24、Python 3.10+ 和 pnpm。本仓库依赖清单来自宿主组件 0.2.1-rc.4 的盘点快照，其他宿主版本请核对插件兼容说明。

```sh
git clone https://github.com/johnnyliu1126/deepseek-harness-plugins-macos-intel.git
cd deepseek-harness-plugins-macos-intel
python3 scripts/platform_support.py --check-node

# Preview only / 只读预览
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection-macos-intel" --all

# Apply and fetch / 新建 Profile 并安装
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection-macos-intel" --all --apply --fetch
```

已有目标目录会被拒绝，不覆盖当前 desktop，不复制凭据，也不自动重启应用。只需要本地插件时可使用：

```sh
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection-macos-intel-local" --plugins dsh-restart dsh-balance-monitor --apply --fetch
```

新 Profile 不会自动切换 Desktop 当前配置。若安装了匹配宿主的 CLI，可先检查配置，再显式启动：

```sh
dsh --profile collection-macos-intel --dump-config
dsh --profile collection-macos-intel --help
dsh --profile collection-macos-intel
```

启动前检查端口，避免与正在运行的实例冲突。没有 dsh 命令时先配置宿主 CLI，勿照抄其他操作系统的应用路径。详细流程见 [安装指南](docs/INSTALL.zh-CN.md)。

## 插件清单：功能与如何使用

| 插件 | 版本 | 功能 | 使用入口 |
|---|---|---|---|
| [dsh-purge-community](catalog/dsh-purge-community/README.zh-CN.md) | 1.6.60 | 状态、规则与补丁管理 | 打开插件侧栏，先看状态自检和备份，再按需管理预设提示词、规则或执行回滚。 |
| [@neystan/dsh-web-ui-all](catalog/neystan--dsh-web-ui-all/README.zh-CN.md) | 0.1.16 | Web UI 全家桶 | 安装聚合包后使用对应看板、Git 图、右侧文件面板等入口；四个兼容性受限子项默认禁用。 |
| [dsh-lark-channel](catalog/dsh-lark-channel/README.zh-CN.md) | 0.0.7 | 飞书 / Lark 机器人 | 先配置飞书/Lark 机器人和本地凭据，再向机器人发任务；用 /status、/ws、/cd、/model、/sessions 管理会话。 |
| [@tt-a1i/archify-dsh](catalog/tt-a1i--archify-dsh/README.zh-CN.md) | 1.0.0 | 架构图 | 在对话里说：“使用 archify skill 分析当前仓库，生成架构 JSON 和 HTML，并告诉我文件路径。” |
| [dsh-prompt-enhancer](catalog/dsh-prompt-enhancer/README.zh-CN.md) | 1.2.2 | 提示词优化 | 在输入框写草稿，点击“优化”，检查改写内容后再发送；设置中可选精简、均衡、详细或自定义。 |
| [@liustack/modlens](catalog/liustack--modlens/README.zh-CN.md) | 3.27.2 | 图像理解与 OCR | 先配置视觉提供商，再说：“读取这张图片，提取全部文字并解释图表。”遇到问题运行 modlens doctor。 |
| [@liustack/modsearch](catalog/liustack--modsearch/README.zh-CN.md) | 5.10.11 | 网页与 X 搜索 | 在对话中要求搜索或抓取，例如：“搜索这个技术问题，并附上来源链接。”X 搜索还需要已配置的 Grok Build。 |
| [dsh-ego-browser](catalog/dsh-ego-browser/README.zh-CN.md) | 0.9.8 | 浏览器自动化 | 让 Agent 打开网页并执行交互，在右侧面板观察过程；需要登录时按插件流程导入或手工登录。 |
| [dsh-client-liang-intensity-skin](catalog/dsh-client-liang-intensity-skin/README.zh-CN.md) | 0.1.6 | 推理滑块与皮肤 | 在外观设置启用皮肤，选择支持多个 reasoning effort 的模型，拖动并松开滑块提交档位。 |
| [dsh-restart](catalog/dsh-restart/README.zh-CN.md) | 1.0.0 | 一键重启 | 在 macOS Desktop 侧栏页脚点击“重启”；先保存工作，真实重启会中断正在执行的任务。 |
| [dsh-balance-monitor](catalog/dsh-balance-monitor/README.zh-CN.md) | 1.0.0 | 余额监控 | 先登录宿主 DeepSeek 账号并打开一个会话；在输入框下方查看余额，点击余额展开刷新间隔和阈值。 |
| [dsh-mobile](catalog/dsh-mobile/README.zh-CN.md) | 0.8.2 | 手机访问 | 在手机访问设置选择 LAN 或远程方式，手机扫码配对；账号、隧道和通知权限在本机单独配置。 |
| [@neystan/dsh-client-ui-task-board](catalog/neystan--dsh-client-ui-task-board/README.zh-CN.md) | 0.1.16 | 任务看板、定时任务与待办 | 兼容宿主上打开任务看板，添加任务或待办，为需要自动执行的任务设置 cron。当前模板默认禁用。 |
| [@neystan/dsh-client-ui-aionui-panel](catalog/neystan--dsh-client-ui-aionui-panel/README.zh-CN.md) | 0.1.16 | 文件树与多标签预览 | 打开右侧文件面板，浏览工作区文件树、搜索文件名、查看 Git 改动并打开预览标签。 |
| [@neystan/dsh-client-ui-git-graph](catalog/neystan--dsh-client-ui-git-graph/README.zh-CN.md) | 0.1.16 | Git 图与分支管理 | 在会话顶部查看 Git 图，选择、创建或切换工作区仓库的分支；操作会影响真实 Git 状态。 |
| [@neystan/dsh-pet](catalog/neystan--dsh-pet/README.zh-CN.md) | 0.1.16 | 宠物互动 | 兼容宿主上显示宠物后可抚摸、喂食，或分别导入 pet.json 和 spritesheet.webp。当前模板默认禁用。 |
| [@neystan/dsh-skins](catalog/neystan--dsh-skins/README.zh-CN.md) | 0.1.16 | 皮肤合集 | 通过皮肤中心或 dsh-skin use 切换主题；同一时间只启用一个皮肤，避免外观叠加。 |
| [@neystan/dsh-tool-describe-image](catalog/neystan--dsh-tool-describe-image/README.zh-CN.md) | 0.1.16 | 图像描述工具 | 兼容宿主上填写 baseURL 和视觉模型，再让 Agent 调用 describe_image 读取路径、URL 或附件。当前模板默认禁用。 |
| [@neystan/dsh-client-ui-skin-center](catalog/neystan--dsh-client-ui-skin-center/README.zh-CN.md) | 0.1.16 | 皮肤中心 | 兼容宿主上打开插件配置中的皮肤中心，试穿后再应用，可调整颜色、对比度和背景。当前模板默认禁用。 |

聚合包包含 7 个 Web UI 子包，不要同时安装聚合包与相同子插件。四个子项在兼容性模板中保持禁用：任务看板、宠物、图像描述、皮肤中心。手机插件已有 React peer 警告，`^19.3.0` 与原隔离依赖图 `18.3.1` 不匹配，不能据此声明手机 UI 可用。

## 本平台的实际差异

手机插件在 macOS 可选择 LAN、cloudflared（x64/arm64 按需下载）、FRP 和自建反向代理；上游此版本没有托管的 macOS Funnel、cpolar、Caddy 或 iroh 组件。restart 仅能重启真实 macOS Desktop .app 宿主，普通 Node Web Profile 不能借此变成桌面进程。

## 逐项功能

### 状态、规则与补丁管理 — `dsh-purge-community`

- 状态自检与宿主证据：面板检查补丁和运行状态，失败读取不等于未安装。
- 提示词与规则：按预设管理文本、追加顺序、排除预设和一次性注入选项。
- 补丁生命周期：本机备份、应用、回滚与版本管理；可能改写宿主，需单独操作。
- 演练台：附带预设、技能、SQLite 事实库和 /redteam/api 桥接。
- 重试与继续：配置自动重试、次数上限和继续文本；不保证任务一定成功。

**使用：** 打开插件侧栏，先看状态自检和备份，再按需管理预设提示词、规则或执行回滚。

[详细配置、来源、权限与限制](catalog/dsh-purge-community/README.zh-CN.md)。

### Web UI 全家桶 — `@neystan/dsh-web-ui-all`

- 聚合安装：一次安装任务看板、Git 图、右侧面板、宠物、图像描述和皮肤包。
- 组合层：通过 bundle patch 注册子插件，单独安装子包可选取部分功能。
- 兼容性：部分设置使用较新 keyed slot，本机已禁用四个不兼容子项。

**使用：** 安装聚合包后使用对应看板、Git 图、右侧文件面板等入口；四个兼容性受限子项默认禁用。

[详细配置、来源、权限与限制](catalog/neystan--dsh-web-ui-all/README.zh-CN.md)。

### 飞书 / Lark 机器人 — `dsh-lark-channel`

- 聊天驱动 Agent：飞书/Lark 文本触发真实宿主任务，推理、工具和结果分开展示。
- 持久会话：按聊天、话题或发送者隔离，/new 新建，/sessions 续接。
- 工作区和模型：/ws、/cd、/model 切换，/status 查看状态，/stop 停止。
- 交互卡片：回答模型问题、评审计划和批准工具；权限调整仍遵守批准者配置。
- 多机器人：独立凭据与会话，botPeers 限制对话对象，botHops 限制循环。
- 文件传输：接收文件到工作区；群聊发送需要逐次批准，默认单文件 20 MiB。

**使用：** 先配置飞书/Lark 机器人和本地凭据，再向机器人发任务；用 /status、/ws、/cd、/model、/sessions 管理会话。

[详细配置、来源、权限与限制](catalog/dsh-lark-channel/README.zh-CN.md)。

### 架构图 — `@tt-a1i/archify-dsh`

- 架构图技能：通过文件系统 skill provider 提供 Archify，按名称调用。
- 结构化产物：生成规范 JSON 与 HTML 图，用组件、主路径和信任边界解释仓库。
- 轻量适配：不添加模型工具或 Web UI；内置 Archify 3.0.1，与适配器版本分开。

**使用：** 在对话里说：“使用 archify skill 分析当前仓库，生成架构 JSON 和 HTML，并告诉我文件路径。”

[详细配置、来源、权限与限制](catalog/tt-a1i--archify-dsh/README.zh-CN.md)。

### 提示词优化 — `dsh-prompt-enhancer`

- 草稿优化：输入框按钮替换草稿，保留发送前编辑和撤销的机会。
- 四档指令：精简、均衡（默认）、详细和自定义；短闲聊有防过度扩写重试。
- 模型路由：免费通道、当前模型或固定模型；免费通道失败可能回退到付费对话模型。
- 连通性与记录：设置页测试通道并显示上次实际调用；本机 settings.json 保存设置。

**使用：** 在输入框写草稿，点击“优化”，检查改写内容后再发送；设置中可选精简、均衡、详细或自定义。

[详细配置、来源、权限与限制](catalog/dsh-prompt-enhancer/README.zh-CN.md)。

### 图像理解与 OCR — `@liustack/modlens`

- 图像理解：为文本模型补充 OCR、阅读顺序、区域、实体和关系描述。
- 多提供商：Gemini、OpenAI 兼容、Anthropic、Antigravity、Claude 和 Kimi CLI。
- 故障转移与轮换：授权、限流和额度错误可触发同提供商密钥轮换及链路回退。
- 复用现有 CLI：doctor 检测已装工具，按授权配置复用；可能消耗对应订阅额度。

**使用：** 先配置视觉提供商，再说：“读取这张图片，提取全部文字并解释图表。”遇到问题运行 modlens doctor。

[详细配置、来源、权限与限制](catalog/liustack--modlens/README.zh-CN.md)。

### 网页与 X 搜索 — `@liustack/modsearch`

- 网页搜索与抓取：给没有原生联网能力的模型提供搜索与页面正文。
- 多引擎：Firecrawl、Keenable、You.com、Antigravity、Tavily、Exa 和本地抓取。
- X 搜索：配置并登录 Grok Build 后使用对应渠道。
- 回退与密钥轮换：渠道失败时切换；免费额度是上游声明，可能变化。

**使用：** 在对话中要求搜索或抓取，例如：“搜索这个技术问题，并附上来源链接。”X 搜索还需要已配置的 Grok Build。

[详细配置、来源、权限与限制](catalog/liustack--modsearch/README.zh-CN.md)。

### 浏览器自动化 — `dsh-ego-browser`

- 浏览器工具：ego_* 工具驱动内置 ego-lite，执行页面访问和交互。
- 实时面板：SSE 画面、直接鼠标操作、标签页、下载捕获及人工验证提示。
- 登录导入：Chrome/Edge 扩展桥或非破坏性配置副本，登录资料不进入仓库。
- 不同宿主：Web 右侧栏、可选 TUI 文本面板，headless 仅工具模式。

**使用：** 让 Agent 打开网页并执行交互，在右侧面板观察过程；需要登录时按插件流程导入或手工登录。

[详细配置、来源、权限与限制](catalog/dsh-ego-browser/README.zh-CN.md)。

### 推理滑块与皮肤 — `dsh-client-liang-intensity-skin`

- 推理滑块：读取模型实际 reasoning.efforts，均匀映射到 0–30。
- 提交规则：拖动仅预览，松开、键盘完成或失焦后吸附并提交原始 effort ID。
- 可见性：不支持推理、单档位或 addressed subagent 时隐藏。
- 外观切换：皮肤模式显示人物、背景和配色；原生模式恢复宿主界面。

**使用：** 在外观设置启用皮肤，选择支持多个 reasoning effort 的模型，拖动并松开滑块提交档位。

[详细配置、来源、权限与限制](catalog/dsh-client-liang-intensity-skin/README.zh-CN.md)。

### 一键重启 — `dsh-restart`

- 常驻入口：侧边栏页脚文字按钮，窄栏降级为图标。
- 重启过程：POST 路由调用 detached shell，延迟退出整棵应用进程并重新打开。
- 状态与日志：state 和 log 接口，dryRun 预演和 10 秒重复请求去抖。
- 重连：浏览器轮询宿主返回后刷新；实际重启会打断进行中的任务。

**使用：** 在 macOS Desktop 侧栏页脚点击“重启”；先保存工作，真实重启会中断正在执行的任务。

[详细配置、来源、权限与限制](catalog/dsh-restart/README.zh-CN.md)。

### 余额监控 — `dsh-balance-monitor`

- 余额：通过宿主 deepseekAccount 查询，按币种展示充值、赠金和合计。
- 刷新：默认 60 秒，可选 30/60/120/300 秒，手动刷新、请求合并和 3 秒节流。
- 提醒：低余额阈值默认 10，金额着色，设置保存在 localStorage。
- 时段：北京时间工作日时段与切换倒计时，硬编码 2026 假日。不是官方实时价格源。
- 错误状态：区分未登录、接口不可用和查询失败；失败不显示零余额。

**使用：** 先登录宿主 DeepSeek 账号并打开一个会话；在输入框下方查看余额，点击余额展开刷新间隔和阈值。

[详细配置、来源、权限与限制](catalog/dsh-balance-monitor/README.zh-CN.md)。

### 手机访问 — `dsh-mobile`

- 手机会话：与桌面共享 Workspace、消息和工具，适配触屏输入框、抽屉和问答卡片。
- 客户端：Android App 与手机浏览器/PWA；界面与设备列表可定制。
- 配对：二维码、链接或密钥，多设备可达性检查、切换、重新配对和移除记录。
- 网络：LAN、Tailscale、cpolar、Cloudflare、FRP、自建代理、Caddy；iroh 是平台受限实验项。
- 通知：iOS 主屏幕 Web Push 和 Android 原生通知，需用户显式开启。
- 诊断与安全：脱敏连接报告、设备凭据、Origin 绑定和第三方 WebSocket 逐路径批准。

**使用：** 在手机访问设置选择 LAN 或远程方式，手机扫码配对；账号、隧道和通知权限在本机单独配置。

[详细配置、来源、权限与限制](catalog/dsh-mobile/README.zh-CN.md)。

### 任务看板、定时任务与待办 — `@neystan/dsh-client-ui-task-board`

- 任务看板：多列卡片、宿主持久化和真实 Agent 会话执行。
- 定时任务：宿主 cron，创建、列表、暂停、恢复、运行和删除。
- 待办：添加、查询、完成和删除，数据持久保存。

**使用：** 兼容宿主上打开任务看板，添加任务或待办，为需要自动执行的任务设置 cron。当前模板默认禁用。

[详细配置、来源、权限与限制](catalog/neystan--dsh-client-ui-task-board/README.zh-CN.md)。

### 文件树与多标签预览 — `@neystan/dsh-client-ui-aionui-panel`

- 文件管理：Workspace 文件树、文件名搜索与 Git 改动。
- 预览：多标签查看十余种文件格式，通过宿主 fs/git 服务获取数据。

**使用：** 打开右侧文件面板，浏览工作区文件树、搜索文件名、查看 Git 改动并打开预览标签。

[详细配置、来源、权限与限制](catalog/neystan--dsh-client-ui-aionui-panel/README.zh-CN.md)。

### Git 图与分支管理 — `@neystan/dsh-client-ui-git-graph`

- 分支与图：会话顶部的分支选择器和提交关系图。
- 真实 Git 操作：通过宿主创建或切换分支，并执行操作前检查。

**使用：** 在会话顶部查看 Git 图，选择、创建或切换工作区仓库的分支；操作会影响真实 Git 状态。

[详细配置、来源、权限与限制](catalog/neystan--dsh-client-ui-git-graph/README.zh-CN.md)。

### 宠物互动 — `@neystan/dsh-pet`

- 活动动画：会话与工具事件驱动九种动画状态。
- 互动：抚摸、喂食、亲密度和鱼干库存，宿主统一保存。
- 自定义：分别导入 pet.json 与 spritesheet.webp，验证、预览、切换一个自定义槽。

**使用：** 兼容宿主上显示宠物后可抚摸、喂食，或分别导入 pet.json 和 spritesheet.webp。当前模板默认禁用。

[详细配置、来源、权限与限制](catalog/neystan--dsh-pet/README.zh-CN.md)。

### 皮肤合集 — `@neystan/dsh-skins`

- 聚合皮肤：内置十种皮肤资产与一个独立自定义主题槽。
- 互斥切换：dsh-skin use 管理激活，避免多个皮肤叠加。
- 外观控制：强调色、背景、前景、对比度与可复用 WebP 背景。

**使用：** 通过皮肤中心或 dsh-skin use 切换主题；同一时间只启用一个皮肤，避免外观叠加。

[详细配置、来源、权限与限制](catalog/neystan--dsh-skins/README.zh-CN.md)。

### 图像描述工具 — `@neystan/dsh-tool-describe-image`

- 图像输入：本地绝对路径、HTTP(S) URL 或附件引用，一次一张。
- 模型工具：describe_image 接受指定 OCR、图表、翻译等 prompt，只把返回文字写入会话。
- 协议：OpenAI 兼容 Chat Completions 或 Responses，设置修改即时生效。
- 边界：默认 10 MiB、1024 输出 tokens、60 秒；拒绝重定向并检查文件魔数。

**使用：** 兼容宿主上填写 baseURL 和视觉模型，再让 Agent 调用 describe_image 读取路径、URL 或附件。当前模板默认禁用。

[详细配置、来源、权限与限制](catalog/neystan--dsh-tool-describe-image/README.zh-CN.md)。

### 皮肤中心 — `@neystan/dsh-client-ui-skin-center`

- 浏览与试穿：默认主题、内置皮肤、自定义主题，即时试穿和退出恢复。
- 应用：宿主写入 managed patch，配置 watcher 热加载并刷新页面。
- 自定义与背景：三色加对比度，Follow skin/Custom/None 背景模式；图片压缩为 WebP。

**使用：** 兼容宿主上打开插件配置中的皮肤中心，试穿后再应用，可调整颜色、对比度和背景。当前模板默认禁用。

[详细配置、来源、权限与限制](catalog/neystan--dsh-client-ui-skin-center/README.zh-CN.md)。

## 卸载、恢复与隐私

使用 `dsh plugin --profile YOUR_PROFILE remove PACKAGE` 移除单个插件。换机时克隆相应平台仓库并创建新 Profile，然后重新配置账号。回退时继续使用原 Profile，安装器没有覆盖它。

账号、API Key、机器人 Token、手机配对、浏览器 Cookie、隧道状态、私钥与聊天不进入仓库。图片、草稿和搜索请求可能发往你配置的第三方服务。

## 来源与许可证

Platform adaptation of [https://github.com/johnnyliu1126/deepseek-harness-plugin-collection](https://github.com/johnnyliu1126/deepseek-harness-plugin-collection) at `c10c4436740e8d462215f361d3a8e18b3801d326`. 第三方作者和 fork 链条保留；见 [署名清单](THIRD_PARTY_NOTICES.md)、[许可证说明](LICENSE) 和各插件文档。未声明或冲突的许可证不会被虚构补全。

## 验证与维护

CI targets `macos-15-intel` / `x64`: [Actions](https://github.com/johnnyliu1126/deepseek-harness-plugins-macos-intel/actions). 实际运行状态以链接为准。CI 检查平台、安装器、源码、下载完整性、本地插件包和全部根依赖安装；不连接真实账号，不执行桌面重启。已运行与未运行项目见 [平台验证说明](docs/VERIFICATION.md)。

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
node --test plugins/dsh-balance-monitor/core.test.js tests/routes.test.mjs
```

更多说明：[平台差异](docs/PLATFORM.md) · [浏览器工具](docs/BROWSER-TOOLS.md) · [MCP 与本地技能](docs/INTEGRATIONS.md)。
