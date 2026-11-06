# @neystan/dsh-tool-describe-image

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.1.16` · **License / 许可证:** `Apache-2.0`

## 来源与署名

Author / 作者: neystan

Upstream / 上游: [https://github.com/neystan/dsh-web-ui](https://github.com/neystan/dsh-web-ui)

- Contributor / 贡献者: zhu1090093659 (Original author)

Original project / 原项目: [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui), original npm scope `@linxin666/*`; fork maintained by neystan.

Additional lineage / 补充来源: DeepSeek Harness `packages/vision/tool-describe-image`, mirrored by [whitelonng](https://github.com/whitelonng/dsh-plugin-describe-image).

保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 图像输入：本地绝对路径、HTTP(S) URL 或附件引用，一次一张。
- 模型工具：describe_image 接受指定 OCR、图表、翻译等 prompt，只把返回文字写入会话。
- 协议：OpenAI 兼容 Chat Completions 或 Responses，设置修改即时生效。
- 边界：默认 10 MiB、1024 输出 tokens、60 秒；拒绝重定向并检查文件魔数。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add @neystan/dsh-tool-describe-image@0.1.16
dsh plugin --profile YOUR_PROFILE remove @neystan/dsh-tool-describe-image
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `baseURL / model` | `required` | Endpoint and vision model / 端点与视觉模型 |
| `apiStyle` | `chat-completions` | or responses |
| `apiKeyEnv` | `VISION_API_KEY` | Credential reference / 凭据引用 |
| `maxBytes` | `10485760` | Image size cap / 图像上限 |
| `maxOutputTokens` | `1024` | Output cap / 输出上限 |
| `timeoutMs` | `60000` | Request timeout / 请求超时 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

打开对应插件 UI；按上面功能条目操作，详细流程见上游文档。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

**本机兼容性 patch 禁用了这个子插件。** 不要删除禁用项来掩盖缺失 API；升级并单独验证。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 0.1.16; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
