# dsh-prompt-enhancer

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.2.2` · **License / 许可证:** `MIT`

## 来源与署名

Author / 作者: MCJF28

Upstream / 上游: [https://github.com/MCJF28/dsh-prompt-enhancer](https://github.com/MCJF28/dsh-prompt-enhancer)


保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 草稿优化：输入框按钮替换草稿，保留发送前编辑和撤销的机会。
- 四档指令：精简、均衡（默认）、详细和自定义；短闲聊有防过度扩写重试。
- 模型路由：免费通道、当前模型或固定模型；免费通道失败可能回退到付费对话模型。
- 连通性与记录：设置页测试通道并显示上次实际调用；本机 settings.json 保存设置。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add dsh-prompt-enhancer@1.2.2
dsh plugin --profile YOUR_PROFILE remove dsh-prompt-enhancer
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `mode` | `balanced` | concise / balanced / detailed / custom |
| `DSH_FREE_CHANNEL_BASE_URL` | `upstream default` | Endpoint override / 覆盖端点 |
| `DSH_FREE_CHANNEL_API_KEY` | `unset` | Local environment only / 仅本地环境变量 |
| `DSH_FREE_CHANNEL_MODEL` | `upstream default` | Model override / 覆盖模型 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

输入草稿，点击“优化”；设置 → 优化选择力度和模型，然后检查草稿再发送。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 1.2.2; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
