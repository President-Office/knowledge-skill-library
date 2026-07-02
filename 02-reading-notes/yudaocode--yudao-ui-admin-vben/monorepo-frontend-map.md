---
type: source-reading
status: initial
project: yudaocode/yudao-ui-admin-vben
topic: Monorepo 前端地图
created: 2026-07-02
updated: 2026-07-02
---

# yudao-ui-admin-vben - Monorepo 前端地图

项目主卡：[[yudaocode--yudao-ui-admin-vben]]
特点卡：[[yudao-ui-admin-vben]]

## 阅读目标

建立 Vben 版本的前端工程地图，理解它和 [[frontend-module-map]] 的差异。

## 已确认结构

| 目录 | 初步职责 |
| --- | --- |
| `apps/web-ele` | Element Plus 版本应用，最适合和 Vue3 单应用版对照 |
| `apps/web-antd` / `web-naive` / `web-tdesign` | 不同 UI 版本应用 |
| `packages/@core` | 核心能力 |
| `packages/stores` | 共享状态管理 |
| `packages/utils` | 共享工具 |
| `packages/styles` | 共享样式 |
| `packages/preferences` | 偏好配置 |
| `pnpm-workspace.yaml` | workspace 入口 |
| `turbo.json` | Turbo 构建编排 |

## 初步判断

Vben 版本的学习重点不是某一个业务页面，而是前端平台化：

- 多个 UI app 共享底层 packages。
- 业务迁移成本比单应用高。
- 长期收益在工程治理、共享能力和多 UI 适配。

如果只是快速交付 Yudao 业务后台，[[frontend-module-map]] 更直接；如果要建设长期后台前端底座，Vben 版本更值得研究。

## 读源码时要验证的问题

- `apps/web-ele` 如何引用 `packages` 下的共享能力。
- 路由、权限、请求封装是在 app 内还是 core package 内。
- 不同 UI app 之间能复用多少业务页面。
- 偏好配置如何影响布局、菜单和主题。

## Obsidian 关联

- 底层概念：[[monorepo]]、[[boundaries]]、[[abstractions]]
- Vue3 单应用对照：[[frontend-module-map]]
- 前端对比：[[yudao-ui-admin-vue3-vs-vben]]
