# dsh-lark-channel

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.0.7` · **License / 许可证:** `BSD-3-Clause`

## 来源与署名

Author / 作者: omdsh-dev (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/omdsh-dev/dsh-lark](https://github.com/omdsh-dev/dsh-lark)


保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 聊天驱动 Agent：飞书/Lark 文本触发真实宿主任务，推理、工具和结果分开展示。
- 持久会话：按聊天、话题或发送者隔离，/new 新建，/sessions 续接。
- 工作区和模型：/ws、/cd、/model 切换，/status 查看状态，/stop 停止。
- 交互卡片：回答模型问题、评审计划和批准工具；权限调整仍遵守批准者配置。
- 多机器人：独立凭据与会话，botPeers 限制对话对象，botHops 限制循环。
- 文件传输：接收文件到工作区；群聊发送需要逐次批准，默认单文件 20 MiB。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add dsh-lark-channel@0.0.7
dsh plugin --profile YOUR_PROFILE remove dsh-lark-channel
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `sessionScope` | `see upstream schema` | chat / chat-thread / chat-sender |
| `botHops` | `6` | Maximum bot-to-bot hops / 机器人连续对话上限 |
| `attachImages` | `false` | Enable only for vision models / 仅视觉模型启用 |
| `receiveFiles / sendFiles` | `true` | Group sends require approval / 群聊发送仍需批准 |
| `maxReceiveFileBytes / maxSendFileBytes` | `20 MiB` | Per-direction size limits / 双向单文件大小限制 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

先用上游配置流程创建飞书应用并设置本地凭据，再在机器人聊天中输入 /status 或 /help。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 0.0.7; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
