# @liustack/modsearch

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `5.10.11` · **License / 许可证:** `MIT`

## 来源与署名

Author / 作者: Leon Liu

Upstream / 上游: [https://github.com/liustack/modsearch](https://github.com/liustack/modsearch)


保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 网页搜索与抓取：给没有原生联网能力的模型提供搜索与页面正文。
- 多引擎：Firecrawl、Keenable、You.com、Antigravity、Tavily、Exa 和本地抓取。
- X 搜索：配置并登录 Grok Build 后使用对应渠道。
- 回退与密钥轮换：渠道失败时切换；免费额度是上游声明，可能变化。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add @liustack/modsearch@5.10.11
dsh plugin --profile YOUR_PROFILE remove @liustack/modsearch
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

通过插件设置页配置；全部配置字段与默认值以固定版本的上游实现为准，不猜测缺失默认值。

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

要求 Agent 搜索网页或抓取指定页面；必要时通过上游 CLI 配置搜索引擎。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 5.10.11; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
