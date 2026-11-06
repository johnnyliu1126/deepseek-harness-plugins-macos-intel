# dsh-ego-browser

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.9.8` · **License / 许可证:** `MIT`

## 来源与署名

Author / 作者: Fisfzy (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/Fisfzy/dsh-ego-browser](https://github.com/Fisfzy/dsh-ego-browser)


保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 浏览器工具：ego_* 工具驱动内置 ego-lite，执行页面访问和交互。
- 实时面板：SSE 画面、直接鼠标操作、标签页、下载捕获及人工验证提示。
- 登录导入：Chrome/Edge 扩展桥或非破坏性配置副本，登录资料不进入仓库。
- 不同宿主：Web 右侧栏、可选 TUI 文本面板，headless 仅工具模式。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add dsh-ego-browser@0.9.8
dsh plugin --profile YOUR_PROFILE remove dsh-ego-browser
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `chromePath` | `auto-detect` | Set only to an existing local browser / 本地浏览器路径 |
| `defaultSpace` | `empty` | Runtime space / 运行时空间 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

在会话中要求访问网页，观察右侧浏览器面板；需要登录时使用上游导入流程。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 0.9.8; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。

[Tool-by-tool reference / 逐工具说明](../../docs/BROWSER-TOOLS.md)
