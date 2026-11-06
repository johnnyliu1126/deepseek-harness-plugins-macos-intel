# dsh-balance-monitor

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `1.0.0` · **License / 许可证:** `UNDECLARED`

## 来源与署名

Author / 作者: Undeclared in original manifest / 原清单未声明


Local source included with provenance; no missing license or author is fabricated. / 本地源码附来源说明，不虚构缺失许可证或作者。

## 功能

- 余额：通过宿主 deepseekAccount 查询，按币种展示充值、赠金和合计。
- 刷新：默认 60 秒，可选 30/60/120/300 秒，手动刷新、请求合并和 3 秒节流。
- 提醒：低余额阈值默认 10，金额着色，设置保存在 localStorage。
- 时段：北京时间工作日时段与切换倒计时，硬编码 2026 假日。不是官方实时价格源。
- 错误状态：区分未登录、接口不可用和查询失败；失败不显示零余额。

## 安装与卸载

```sh
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-balance-monitor
python3 scripts/collection.py --target "$HOME/.dsh/profiles/collection" --plugins dsh-balance-monitor --apply --fetch
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `刷新间隔 / interval` | `60 s` | 30, 60, 120, 300; localStorage dshbm-interval |
| `低余额阈值 / threshold` | `10` | localStorage dshbm-threshold |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

登录宿主 DeepSeek 账号并打开会话；点击输入框下方余额展开设置。

## 权限与数据

本地余额依赖宿主账号服务；不保存账号凭据。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

检查宿主登录和 account 服务；2026 以外节假日日历未知。尚无 API Key、消费历史或会话估算。测试：`node --test plugins/dsh-balance-monitor/core.test.js`。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 1.0.0; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
