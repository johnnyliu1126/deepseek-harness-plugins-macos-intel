# @tt-a1i/archify-dsh

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.0.0` · **License / 许可证:** `MIT`

## 来源与署名

Author / 作者: tt-a1i (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)


保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 架构图技能：通过文件系统 skill provider 提供 Archify，按名称调用。
- 结构化产物：生成规范 JSON 与 HTML 图，用组件、主路径和信任边界解释仓库。
- 轻量适配：不添加模型工具或 Web UI；内置 Archify 3.0.1，与适配器版本分开。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add @tt-a1i/archify-dsh@1.0.0
dsh plugin --profile YOUR_PROFILE remove @tt-a1i/archify-dsh
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `archify-plugin` | `packaged skills root` | Filesystem provider; no custom settings / 文件系统技能提供器 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

在对话中要求“使用 archify skill 绘制当前仓库运行时架构”，并要求返回 JSON 与 HTML 路径。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

上游适配器声明测试目标是 DSH 0.1.2-rc.1 和 Node ^22.19.0 或 >=24；其他版本需复测。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 1.0.0; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
