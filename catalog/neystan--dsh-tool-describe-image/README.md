# @neystan/dsh-tool-describe-image

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.1.16` · **License / 许可证:** `Apache-2.0`

## Source and attribution

Author / 作者: neystan

Upstream / 上游: [https://github.com/neystan/dsh-web-ui](https://github.com/neystan/dsh-web-ui)

- Contributor / 贡献者: zhu1090093659 (Original author)

Original project / 原项目: [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui), original npm scope `@linxin666/*`; fork maintained by neystan.

Additional lineage / 补充来源: DeepSeek Harness `packages/vision/tool-describe-image`, mirrored by [whitelonng](https://github.com/whitelonng/dsh-plugin-describe-image).

This collection documents upstream work; third-party runtime source is not copied.

## Features

- Inputs: one local absolute path, HTTP(S) URL or attachment reference per call.
- Tool: describe_image accepts OCR/chart/translation instructions and adds only returned text to the conversation.
- Protocols: OpenAI-compatible Chat Completions or Responses with live configuration.
- Bounds: defaults of 10 MiB, 1024 output tokens and 60 seconds; redirects refused and magic bytes checked.

## Installation and removal

```sh
dsh plugin --profile YOUR_PROFILE add @neystan/dsh-tool-describe-image@0.1.16
dsh plugin --profile YOUR_PROFILE remove @neystan/dsh-tool-describe-image
```

The collection installer can create a fresh profile; it defaults to a dry plan and refuses existing targets. Avoid selecting an aggregate and its child together. Built-in host plugins are not copied. Local plugins can also be removed with dsh plugin remove.

## Configuration

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `baseURL / model` | `required` | Endpoint and vision model / 端点与视觉模型 |
| `apiStyle` | `chat-completions` | or responses |
| `apiKeyEnv` | `VISION_API_KEY` | Credential reference / 凭据引用 |
| `maxBytes` | `10485760` | Image size cap / 图像上限 |
| `maxOutputTokens` | `1024` | Output cap / 输出上限 |
| `timeoutMs` | `60000` | Request timeout / 请求超时 |

Package-relative entry hashes and the bundle configuration snapshot are in evidence.json; personal absolute paths are omitted.

## Usage

Open the corresponding plugin UI and use the features above; see upstream documentation for the complete workflow.

## Permissions and data

Images, web queries, chat or workspace data may reach configured upstream services; browsers/mobile clients may hold credentials. Configure only needed access. Credentials and private runtime state are excluded.

## Compatibility, validation and troubleshooting

Observed host component version: 0.2.1-rc.4. This is not a compatibility guarantee or proof of successful execution. Third-party features have not all been exercised online for this release.

**Disabled by the observed compatibility patch.** Do not remove the guard to conceal a missing host API; upgrade and retest separately.

Check bundle registration, dependency resolution and required settings before reading host logs. Review pnpm build approvals individually instead of disabling protections globally.

## Changelog

2026-11-06: documented installed version 0.1.16; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
