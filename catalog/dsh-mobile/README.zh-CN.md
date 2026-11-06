# dsh-mobile

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.8.2` · **License / 许可证:** `Apache-2.0`

## 来源与署名

Author / 作者: saya-ch (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/saya-ch/dsh-mobile](https://github.com/saya-ch/dsh-mobile)


保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 手机会话：与桌面共享 Workspace、消息和工具，适配触屏输入框、抽屉和问答卡片。
- 客户端：Android App 与手机浏览器/PWA；界面与设备列表可定制。
- 配对：二维码、链接或密钥，多设备可达性检查、切换、重新配对和移除记录。
- 网络：LAN、Tailscale、cpolar、Cloudflare、FRP、自建代理、Caddy；iroh 是平台受限实验项。
- 通知：iOS 主屏幕 Web Push 和 Android 原生通知，需用户显式开启。
- 诊断与安全：脱敏连接报告、设备凭据、Origin 绑定和第三方 WebSocket 逐路径批准。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add dsh-mobile@0.8.2
dsh plugin --profile YOUR_PROFILE remove dsh-mobile
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `pairing / network` | `configure in plugin UI` | Local credentials are never exported / 配对凭据不导出 |
| `notifications` | `explicit opt-in` | Platform requirements apply / 受平台限制 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

打开插件手机访问配置，选择 LAN 或远程方案，在手机端扫描配对码；凭据留在本机。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 0.8.2; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。

**Observed peer warning / 实测依赖警告:** `dsh-mobile@0.8.2` requests React `^19.3.0`; the isolated dependency graph selected `18.3.1`. Installation succeeded, but mobile UI compatibility is not certified. / 安装成功，但手机 UI 兼容性未认证；未强行替换宿主 React。
