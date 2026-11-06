# dsh-client-liang-intensity-skin

[English](README.md) | [简体中文](README.zh-CN.md)

**Version / 版本:** `0.1.6` · **License / 许可证:** `UNDECLARED`

## 来源与署名

Author / 作者: kingOfSoySauce (upstream repository owner; package author undeclared)

Upstream / 上游: [https://github.com/kingOfSoySauce/dsh-liang-skin](https://github.com/kingOfSoySauce/dsh-liang-skin)


保留上游权利；本合集负责整理文档，第三方源码未复制。

## 功能

- 推理滑块：读取模型实际 reasoning.efforts，均匀映射到 0–30。
- 提交规则：拖动仅预览，松开、键盘完成或失焦后吸附并提交原始 effort ID。
- 可见性：不支持推理、单档位或 addressed subagent 时隐藏。
- 外观切换：皮肤模式显示人物、背景和配色；原生模式恢复宿主界面。

## 安装与卸载

```sh
dsh plugin --profile YOUR_PROFILE add dsh-client-liang-intensity-skin@0.1.6
dsh plugin --profile YOUR_PROFILE remove dsh-client-liang-intensity-skin
```

也可用仓库恢复脚本创建新 Profile；默认只预览，现有目录会被拒绝。不要同时安装聚合包和同一子插件。宿主自带插件无需复制。卸载本地插件可使用同样的 dsh plugin remove 命令。

## 配置

| Key / 参数 | Default / 默认 | Meaning / 含义 |
|---|---|---|
| `appearance` | `user-selected` | Themed/native; effort values come from model / 皮肤与原生；档位由模型决定 |

原始 patch 的默认配置和入口哈希记录于本目录 evidence.json；源文件路径相对插件包，未包含本机绝对路径。

## 使用

在外观设置启用皮肤；用支持多推理档位的模型拖动滑块并松开提交。

## 权限与数据

图片、网页请求、聊天或工作区数据可能发送到你配置的上游服务；浏览器与移动端可能持有登录凭据。按需配置，凭据与私人状态不在本仓库。

## 兼容性、验证与排错

盘点到宿主组件 0.2.1-rc.4；这不代表所有插件均兼容或已运行成功。第三方功能未在此发布过程中逐项在线测试。

先确认 bundle 已声明、依赖可解析、相关设置已配置，再查看宿主日志。pnpm 构建授权错误要逐项审查，勿全局关闭保护。

## 更新记录

2026-11-06: documented installed version 0.1.6; runtime implementation not changed by this collection. / 记录固定版本，未修改第三方运行实现。
