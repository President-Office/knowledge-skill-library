---
type: framework-characteristics
status: draft
project: yudaocode/yudao-ui-admin-vue3
created: 2026-07-02
updated: 2026-07-02
---

# yudao-ui-admin-vue3 特点

项目主卡：[[yudaocode--yudao-ui-admin-vue3]]

## 核心定位

Yudao/RuoYi 体系的单应用 [[Vue 3]] 管理后台前端。它更适合快速二开业务页面：列表、表单、审批、支付、商城、CRM、ERP、BPM 等模块都集中在一个前端工程里。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| 单应用结构 | `src/api`、`src/views`、`src/router`、`src/store` 集中 | 学业务后台前端二开路径 |
| [[Vue 3]] + [[Vite]] + [[TypeScript]] | 现代 [[Vue]] 工程基础 | 适合快速理解 Yudao 前端 |
| [[Element Plus]] | 国内后台常见 UI 组件体系 | 学表格、表单、弹窗、查询页组织 |
| 业务模块直接 | `system`、`infra`、`mall`、`erp`、`crm` 等视图集中 | 易于定位后端模块对应前端页面 |
| 权限入口明确 | `permission.ts`、路由、菜单和按钮权限 | 学后台前端权限控制 |
| 二开成本低 | 比 [[monorepo]] 平台底座更直接 | 适合实际业务交付 |

## 最适合怎么读

1. 先读 `src/main.ts`、`src/permission.ts`、`src/router`。
2. 再读 `src/api` 与 `src/views` 的模块对应关系。
3. 选择一个业务页面，看它如何调用后端 API、渲染表格和表单。

## 不要误解

- 不要把它当平台化前端底座，它更偏业务交付型单应用。
- 不要忽略和后端权限、菜单、API 的配合。
- 如果目标是多 UI、多 app、共享包治理，应对比 Vben 版本。

## 关联

- [[boundaries]]、[[abstractions]]
- [[yudao-ui-admin-vben]]
- [[yudao-ui-admin-vue3-vs-vben]]
- [[zhijiantianya--ruoyi-vue-pro]]
