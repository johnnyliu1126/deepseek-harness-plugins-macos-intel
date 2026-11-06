# dsh-purge-community

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.6.60` · **License / 许可证:** `MIT`

## 来源与署名

Author / 作者: kingcharleslzy-ai

Upstream / 上游: [https://github.com/kingcharleslzy-ai/dsh-purge](https://github.com/kingcharleslzy-ai/dsh-purge)

- Contributor / 贡献者: 小杨 / YuJunZhiXue (original dsh-purge author)
- Contributor / 贡献者: luowang-ui
- Contributor / 贡献者: heigit
- Contributor / 贡献者: OGHong
- Contributor / 贡献者: loLollipop
- Contributor / 贡献者: youki258
- Contributor / 贡献者: SimonQvQ

Original project / 原项目: [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge). Community fork maintained by kingcharleslzy-ai.

保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 状态自检与宿主证据：面板检查补丁和运行状态，失败读取不等于未安装。
- 提示词与规则：按预设管理文本、追加顺序、排除预设和一次性注入选项。
- 补丁生命周期：本机备份、应用、回滚与版本管理；可能改写宿主，需单独操作。
- 演练台：附带预设、技能、SQLite 事实库和 /redteam/api 桥接。
- 重试与继续：配置自动重试、次数上限和继续文本；不保证任务一定成功。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add https://github.com/kingcharleslzy-ai/dsh-purge/releases/download/v1.6.60/dsh-purge-community-1.6.60.tgz
dsh plugin --profile YOUR_PROFILE remove dsh-purge-community
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `autoApplyOnStart / autoUpdateOnStart` | `false` | Explicit lifecycle controls / 显式生命周期控制 |
| `autoRetry / retryMax` | `true / 3` | Retry controls / 重试 |
| `autoContinue / continueMax` | `false / 3` | Continuation controls / 继续 |
| `postPrompt` | `empty` | Local prompt text / 本地提示词 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

打开插件侧栏状态页；先查看证据与备份，再显式操作应用或回滚。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 1.6.60; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
