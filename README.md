> **已迁移 / Superseded:** 本平台版本已合并到 [统一仓库](https://github.com/johnnyliu1126/deepseek-harness-plugin-collection)，请从同一个 [Release 页面](https://github.com/johnnyliu1126/deepseek-harness-plugin-collection/releases/tag/v0.2.0) 下载对应平台包。本仓库仅保留迁移前记录。 / Platform downloads now live in the single canonical repository; this repository is retained only as historical context.

# DeepSeek Harness — macOS Intel

[简体中文](README.zh-CN.md) | [English](README.md) | [平台差异 / Platform details](docs/PLATFORM.md)

This repository targets **macOS Intel / x64 runtimes**: 19 additional plugin entries, 12 top-level choices, 72 feature descriptions and 2 local source package(s). Built-in host code is excluded, with upstream ownership/links/licenses retained.

**Platform adaptation is not complete feature certification.** Before applying an install, the installer checks OS/Python architecture and, when fetching, Node architecture. Mismatches are refused before filesystem mutation. External accounts, browsers, phones and Desktop UI still require target-machine validation.

Use x64 Python and Node on Intel Macs. Existing local Intel checks do not certify all third-party online services.

## Install and launch

Install matching-architecture DeepSeek Harness, Node.js 24, Python 3.10+ and pnpm separately. Package pins come from a snapshot of host components 0.2.1-rc.4; check plugin compatibility on other host releases.

```sh
git clone https://github.com/johnnyliu1126/deepseek-harness-plugins-macos-intel.git
cd deepseek-harness-plugins-macos-intel
python3 scripts/platform_support.py --check-node

# Preview only / 只读预览
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection-macos-intel" --all

# Apply and fetch / 新建 Profile 并安装
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection-macos-intel" --all --apply --fetch
```

Existing targets are refused. The installer does not overwrite desktop, copy credentials or restart the app. For only local plugins:

```sh
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection-macos-intel-local" --plugins dsh-restart dsh-balance-monitor --apply --fetch
```

A new profile does not switch Desktop automatically. With a matching host CLI, inspect its configuration before explicitly launching:

```sh
dsh --profile collection-macos-intel --dump-config
dsh --profile collection-macos-intel --help
dsh --profile collection-macos-intel
```

Check ports before starting another instance. Configure the host CLI if dsh is absent; do not copy another OS’s application path. See the [install guide](docs/INSTALL.md).

## Plugins: purpose and first use

| Plugin | Version | Purpose | How to use |
|---|---|---|---|
| [dsh-purge-community](catalog/dsh-purge-community/README.md) | 1.6.60 | Diagnostics, rules and patch management | Open the plugin sidebar, inspect diagnostics/backups, then manage preset prompts/rules or revert changes. |
| [@neystan/dsh-web-ui-all](catalog/neystan--dsh-web-ui-all/README.md) | 0.1.16 | Web UI aggregate | Install the aggregate and use its board, Git graph and file-panel entries; four compatibility-limited children remain disabled. |
| [dsh-lark-channel](catalog/dsh-lark-channel/README.md) | 0.0.7 | Feishu / Lark bot | Provision a Feishu/Lark bot with local credentials, then send it tasks; use /status, /ws, /cd, /model and /sessions. |
| [@tt-a1i/archify-dsh](catalog/tt-a1i--archify-dsh/README.md) | 1.0.0 | Architecture diagrams | Ask: “Use the archify skill to analyze this repository, generate architecture JSON and HTML, and return their file paths.” |
| [dsh-prompt-enhancer](catalog/dsh-prompt-enhancer/README.md) | 1.2.2 | Prompt optimization | Write a draft, click Optimize, review it, then send; settings offer concise, balanced, detailed and custom modes. |
| [@liustack/modlens](catalog/liustack--modlens/README.md) | 3.27.2 | Vision and OCR | Configure a vision provider, then ask: “Read this image, transcribe all text and explain the chart.” Diagnose with modlens doctor. |
| [@liustack/modsearch](catalog/liustack--modsearch/README.md) | 5.10.11 | Web and X search | Ask for search/fetch, e.g. “Search this technical question and include source links.” X search additionally needs configured Grok Build. |
| [dsh-ego-browser](catalog/dsh-ego-browser/README.md) | 0.9.8 | Browser automation | Ask the agent to navigate/interact and watch the side panel; use the plugin login-import flow or sign in manually when needed. |
| [dsh-client-liang-intensity-skin](catalog/dsh-client-liang-intensity-skin/README.md) | 0.1.6 | Reasoning slider and skin | Enable the skin, select a model with multiple reasoning efforts, then drag and release the slider to commit a level. |
| [dsh-restart](catalog/dsh-restart/README.md) | 1.0.0 | One-click restart | Click Restart in the macOS Desktop sidebar footer; finish active work first because a real restart interrupts tasks. |
| [dsh-balance-monitor](catalog/dsh-balance-monitor/README.md) | 1.0.0 | Balance monitor | Sign in through the host DeepSeek account UI and open a session; view the balance below the composer and click it for polling/threshold settings. |
| [dsh-mobile](catalog/dsh-mobile/README.md) | 0.8.2 | Mobile access | Choose LAN or a remote transport in mobile-access settings and pair by QR; configure accounts, tunnels and notifications locally. |
| [@neystan/dsh-client-ui-task-board](catalog/neystan--dsh-client-ui-task-board/README.md) | 0.1.16 | Task board, cron and todos | On a compatible host, open the board, add tasks/todos and configure cron for scheduled runs. Disabled by the current template. |
| [@neystan/dsh-client-ui-aionui-panel](catalog/neystan--dsh-client-ui-aionui-panel/README.md) | 0.1.16 | File tree and multi-tab preview | Open the right panel to browse the workspace tree, search filenames, inspect Git changes and open preview tabs. |
| [@neystan/dsh-client-ui-git-graph](catalog/neystan--dsh-client-ui-git-graph/README.md) | 0.1.16 | Git graph and branches | Use the session-header Git graph to inspect/select/create/switch repository branches; operations affect the real repository. |
| [@neystan/dsh-pet](catalog/neystan--dsh-pet/README.md) | 0.1.16 | Companion interactions | On a compatible host, pet/feed the companion or import pet.json and spritesheet.webp separately. Disabled by the current template. |
| [@neystan/dsh-skins](catalog/neystan--dsh-skins/README.md) | 0.1.16 | Skin collection | Switch themes through the skin center or dsh-skin use; keep one skin active to avoid overlapping styles. |
| [@neystan/dsh-tool-describe-image](catalog/neystan--dsh-tool-describe-image/README.md) | 0.1.16 | Image-description tool | On a compatible host, configure baseURL/model and ask the agent to call describe_image on a path, URL or attachment. Disabled by the current template. |
| [@neystan/dsh-client-ui-skin-center](catalog/neystan--dsh-client-ui-skin-center/README.md) | 0.1.16 | Skin center | On a compatible host, open Skin Center in plugin settings, try on/apply themes and adjust colors, contrast/backgrounds. Disabled by the current template. |

The aggregate includes seven Web UI children. Avoid selecting both an aggregate and its child. Four compatibility guards stay disabled: task board, pet, image description and skin center. Mobile has a known React peer mismatch (^19.3.0 requested versus 18.3.1 in the original isolated graph), so mobile UI compatibility is not certified.

## Platform-specific differences

On macOS, upstream lists LAN, on-demand x64/arm64 cloudflared, FRP and own reverse proxy; this version has no managed macOS Funnel/cpolar/Caddy/iroh component. Restart only targets an actual macOS Desktop .app host, not an ordinary Node web profile.

## Feature details

### Diagnostics, rules and patch management — `dsh-purge-community`

- Status diagnostics: inspect patch and host evidence; a read failure is not an absent installation.
- Prompt and rule management: per-preset text, ordering, exclusions, and one-shot injection controls.
- Patch lifecycle: local backups, apply/revert and version management; host modification requires an explicit separate action.
- Lab workbench: packaged presets, skills, SQLite evidence store and /redteam/api bridge.
- Retry/continue: configurable retry limits and continuation text; success is not guaranteed.

**Use:** Open the plugin sidebar, inspect diagnostics/backups, then manage preset prompts/rules or revert changes.

[Configuration, provenance, permissions and limits](catalog/dsh-purge-community/README.md).

### Web UI aggregate — `@neystan/dsh-web-ui-all`

- Aggregate installation: task board, Git graph, side panel, pet, image description and skins.
- Composition: a bundle patch mounts child plugins; install individual packages for a subset.
- Compatibility: some settings require newer keyed slots; four child rows are disabled in the observed profile.

**Use:** Install the aggregate and use its board, Git graph and file-panel entries; four compatibility-limited children remain disabled.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-web-ui-all/README.md).

### Feishu / Lark bot — `dsh-lark-channel`

- Chat-driven agents: Feishu/Lark messages launch host tasks with separate reasoning/tool/result views.
- Durable sessions: chat/thread/sender scopes, /new reset and /sessions continuation.
- Workspace/model controls: /ws, /cd, /model, /status and /stop.
- Interactive cards: questions, plan reviews and tool approvals subject to configured approvers.
- Multiple bots: separate credentials/sessions, botPeers allowlists and botHops loop bounds.
- File transfer: workspace inbox and per-send group approval, with a default 20 MiB per-file limit.

**Use:** Provision a Feishu/Lark bot with local credentials, then send it tasks; use /status, /ws, /cd, /model and /sessions.

[Configuration, provenance, permissions and limits](catalog/dsh-lark-channel/README.md).

### Architecture diagrams — `@tt-a1i/archify-dsh`

- Architecture skill: exposes Archify via a filesystem skill provider; invoke it by name.
- Structured artifacts: specification JSON and HTML diagrams with components, a main path and trust boundaries.
- Lightweight adapter: no extra native tools or Web UI; bundles Archify 3.0.1 independently of adapter version.

**Use:** Ask: “Use the archify skill to analyze this repository, generate architecture JSON and HTML, and return their file paths.”

[Configuration, provenance, permissions and limits](catalog/tt-a1i--archify-dsh/README.md).

### Prompt optimization — `dsh-prompt-enhancer`

- Draft optimization: a composer button rewrites the draft before sending, with edit/undo opportunities.
- Instruction modes: concise, balanced (default), detailed and custom, with a short-chat over-expansion retry.
- Model routing: shared free channel, current model or fixed model; fallback may consume paid conversation quota.
- Diagnostics: settings test the channel and show the last actual route; settings are stored locally.

**Use:** Write a draft, click Optimize, review it, then send; settings offer concise, balanced, detailed and custom modes.

[Configuration, provenance, permissions and limits](catalog/dsh-prompt-enhancer/README.md).

### Vision and OCR — `@liustack/modlens`

- Image understanding: OCR, reading order, regions, entities and relationships for text-only models.
- Providers: Gemini, OpenAI-compatible, Anthropic, Antigravity, Claude and Kimi CLI backends.
- Failover/key rotation: authorization, rate-limit and quota failures can rotate keys or switch providers.
- CLI reuse: doctor discovers installed tools; explicitly configured reuse may consume their subscription quota.

**Use:** Configure a vision provider, then ask: “Read this image, transcribe all text and explain the chart.” Diagnose with modlens doctor.

[Configuration, provenance, permissions and limits](catalog/liustack--modlens/README.md).

### Web and X search — `@liustack/modsearch`

- Web search/fetch: search and page text for models without native web access.
- Engines: Firecrawl, Keenable, You.com, Antigravity, Tavily, Exa and local fetch.
- X search: available through a configured, authenticated Grok Build installation.
- Fallback/key rotation: switch failed channels; advertised free quotas are upstream claims and may change.

**Use:** Ask for search/fetch, e.g. “Search this technical question and include source links.” X search additionally needs configured Grok Build.

[Configuration, provenance, permissions and limits](catalog/liustack--modsearch/README.md).

### Browser automation — `dsh-ego-browser`

- Browser tools: ego_* tools drive the bundled ego-lite runtime for navigation and interaction.
- Live panel: SSE screencast, direct mouse control, tabs, download capture and human-verification notices.
- Login import: Chrome/Edge bridge or non-destructive profile copies; login data is excluded here.
- Host variants: Web side panel, optional TUI text UI and tools-only headless use.

**Use:** Ask the agent to navigate/interact and watch the side panel; use the plugin login-import flow or sign in manually when needed.

[Configuration, provenance, permissions and limits](catalog/dsh-ego-browser/README.md).

### Reasoning slider and skin — `dsh-client-liang-intensity-skin`

- Reasoning slider: maps the model’s actual reasoning.efforts evenly to 0–30.
- Commit behavior: drag previews; release, keyboard completion or blur snaps and commits the original effort ID.
- Visibility: hidden for unsupported/single-effort models and addressed subagents.
- Appearance: themed mode adds characters/background/colors; native mode restores the host UI.

**Use:** Enable the skin, select a model with multiple reasoning efforts, then drag and release the slider to commit a level.

[Configuration, provenance, permissions and limits](catalog/dsh-client-liang-intensity-skin/README.md).

### One-click restart — `dsh-restart`

- Persistent entry: sidebar footer button with an icon in collapsed mode.
- Restart flow: POST route launches a detached shell that terminates and relaunches the application.
- Diagnostics: state/log routes, dryRun preview and a 10-second duplicate-request debounce.
- Reconnect: browser polling reloads after host recovery; a real restart interrupts active tasks.

**Use:** Click Restart in the macOS Desktop sidebar footer; finish active work first because a real restart interrupts tasks.

[Configuration, provenance, permissions and limits](catalog/dsh-restart/README.md).

### Balance monitor — `dsh-balance-monitor`

- Balances: query host deepseekAccount; show recharge, bonus and total per currency.
- Refresh: 60-second default, 30/60/120/300 options, manual refresh, request merging and a 3-second throttle.
- Alert: default threshold 10 highlights low balances; settings persist in localStorage.
- Timing: Beijing-time workday windows/countdown with hardcoded 2026 holidays; not an official live pricing feed.
- Failure states: signed out, unsupported and failed are distinct; failures do not display zero balances.

**Use:** Sign in through the host DeepSeek account UI and open a session; view the balance below the composer and click it for polling/threshold settings.

[Configuration, provenance, permissions and limits](catalog/dsh-balance-monitor/README.md).

### Mobile access — `dsh-mobile`

- Mobile sessions: shared workspaces/messages/tools with touch-oriented composer, drawer and question cards.
- Clients: Android application and mobile browser/PWA, with customizable UI and device lists.
- Pairing: QR/link/key setup, multi-device reachability, switching, re-pairing and local-record removal.
- Networking: LAN, Tailscale, cpolar, Cloudflare, FRP, own proxy and Caddy; iroh is experimental and platform-limited.
- Notifications: iOS Home Screen Web Push and Android native alerts require explicit opt-in.
- Diagnostics/security: redacted connection reports, device credentials, Origin binding and per-path third-party WebSocket approvals.

**Use:** Choose LAN or a remote transport in mobile-access settings and pair by QR; configure accounts, tunnels and notifications locally.

[Configuration, provenance, permissions and limits](catalog/dsh-mobile/README.md).

### Task board, cron and todos — `@neystan/dsh-client-ui-task-board`

- Task board: multi-column cards, host persistence and execution through real agent sessions.
- Scheduling: host cron with create/list/pause/resume/run/delete actions.
- Todos: add/list/complete/delete with durable storage.

**Use:** On a compatible host, open the board, add tasks/todos and configure cron for scheduled runs. Disabled by the current template.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-client-ui-task-board/README.md).

### File tree and multi-tab preview — `@neystan/dsh-client-ui-aionui-panel`

- Explorer: workspace file tree, filename search and Git changes.
- Preview: multi-tab viewing for over ten formats using host fs/git services.

**Use:** Open the right panel to browse the workspace tree, search filenames, inspect Git changes and open preview tabs.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-client-ui-aionui-panel/README.md).

### Git graph and branches — `@neystan/dsh-client-ui-git-graph`

- Branches/graph: a branch selector and commit graph in the session header.
- Git operations: host-side branch creation/switching with guards.

**Use:** Use the session-header Git graph to inspect/select/create/switch repository branches; operations affect the real repository.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-client-ui-git-graph/README.md).

### Companion interactions — `@neystan/dsh-pet`

- Activity animation: nine states driven by session/tool events.
- Interaction: petting, feeding, affinity and treat stock persisted by the host.
- Customization: validate/preview/import pet.json and spritesheet.webp into one custom slot.

**Use:** On a compatible host, pet/feed the companion or import pet.json and spritesheet.webp separately. Disabled by the current template.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-pet/README.md).

### Skin collection — `@neystan/dsh-skins`

- Skin collection: ten bundled skins and an independent custom-theme slot.
- Exclusive activation: dsh-skin use manages one active skin at a time.
- Appearance controls: accent/background/foreground/contrast and reusable WebP backgrounds.

**Use:** Switch themes through the skin center or dsh-skin use; keep one skin active to avoid overlapping styles.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-skins/README.md).

### Image-description tool — `@neystan/dsh-tool-describe-image`

- Inputs: one local absolute path, HTTP(S) URL or attachment reference per call.
- Tool: describe_image accepts OCR/chart/translation instructions and adds only returned text to the conversation.
- Protocols: OpenAI-compatible Chat Completions or Responses with live configuration.
- Bounds: defaults of 10 MiB, 1024 output tokens and 60 seconds; redirects refused and magic bytes checked.

**Use:** On a compatible host, configure baseURL/model and ask the agent to call describe_image on a path, URL or attachment. Disabled by the current template.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-tool-describe-image/README.md).

### Skin center — `@neystan/dsh-client-ui-skin-center`

- Browse/try-on: stock, bundled and custom themes with live preview and restoration on exit.
- Apply: host updates the managed patch; config watching reloads it and refreshes the page.
- Customization/backgrounds: three colors plus contrast; Follow skin/Custom/None modes and WebP normalization.

**Use:** On a compatible host, open Skin Center in plugin settings, try on/apply themes and adjust colors, contrast/backgrounds. Disabled by the current template.

[Configuration, provenance, permissions and limits](catalog/neystan--dsh-client-ui-skin-center/README.md).

## Uninstall, restore and privacy

Remove individual packages with `dsh plugin --profile YOUR_PROFILE remove PACKAGE`. On another machine, clone its platform repository, create a fresh profile and reconfigure accounts locally. Rollback can return to the untouched original profile.

Credentials, API keys, bot tokens, pairing records, cookies, tunnel state, private keys and chats are excluded. Images/drafts/search queries may reach configured external services.

## Attribution and licenses

Platform adaptation of [https://github.com/johnnyliu1126/deepseek-harness-plugin-collection](https://github.com/johnnyliu1126/deepseek-harness-plugin-collection) at `c10c4436740e8d462215f361d3a8e18b3801d326`. Upstream authors/fork lineage are retained; see [credits](THIRD_PARTY_NOTICES.md), [license scope](LICENSE) and plugin pages. Missing/conflicting license facts are not fabricated.

## Verification and maintenance

CI targets `macos-15-intel` / `x64`: [Actions](https://github.com/johnnyliu1126/deepseek-harness-plugins-macos-intel/actions). Use the linked run status as evidence. CI checks the platform, installer, sources, integrity, local packages and full root dependency installation; it does not use real accounts or restart Desktop. See [verification scope](docs/VERIFICATION.md).

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
node --test plugins/dsh-balance-monitor/core.test.js tests/routes.test.mjs
```

More: [platform details](docs/PLATFORM.md) · [browser tools](docs/BROWSER-TOOLS.md) · [MCP/local skills](docs/INTEGRATIONS.md).
