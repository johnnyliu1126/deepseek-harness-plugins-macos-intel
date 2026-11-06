# macOS Intel — 安装与恢复

[English](INSTALL.md) | [简体中文](INSTALL.zh-CN.md)

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

启动前检查端口，避免与正在运行的实例冲突。没有 dsh 命令时先配置宿主 CLI，勿照抄其他操作系统的应用路径。详细流程见 [安装指南](INSTALL.zh-CN.md)。

现有 Profile 添加单项前先本地备份，再使用该插件详情中的 dsh plugin add 命令。第三方的生命周期脚本默认不执行，必要构建步骤要单独审查。根版本固定于 catalog.lock.json；传递依赖由新 Profile 中生成的 pnpm-lock.yaml 记录。仓库通过 file: 依赖提供本地插件，因此保留 checkout 位置；移动后创建新 Profile。

失败暂存目录保留供检查。不要删除整个 DSH 数据目录来处理安装错误。重新安装不包含账号、手机配对、机器人或浏览器登录资料。
