# macOS Intel — Installation and restoration

[English](INSTALL.md) | [简体中文](INSTALL.zh-CN.md)

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

Check ports before starting another instance. Configure the host CLI if dsh is absent; do not copy another OS’s application path. See the [install guide](INSTALL.md).

Before adding a single package to an existing profile, back it up locally and use the plugin’s dsh plugin add command. Lifecycle scripts stay disabled; review necessary builds separately. catalog.lock.json pins roots; the generated pnpm-lock.yaml records transitive resolution. Local plugins use file: references, so retain the checkout path or create a fresh profile after moving it.

Failed staging data is retained for inspection. Do not delete the DSH data root to fix installation issues. Restore does not include account, pairing, bot or browser credentials.
