---
type: source-reading
status: initial
project: yudaocode/yudao-ui-admin-vue3
topic: 前端业务模块地图
created: 2026-07-02
updated: 2026-07-02
---

# yudao-ui-admin-vue3 - 前端业务模块地图

项目主卡：[[yudaocode--yudao-ui-admin-vue3]]
特点卡：[[yudao-ui-admin-vue3]]

## 阅读目标

建立 Yudao Vue3 管理端的第一张前端地图，明确业务页面、API、路由、权限和状态管理分别在哪里。

## 已确认结构

| 目录 / 文件 | 初步职责 |
| --- | --- |
| `src/main.ts` | 应用入口 |
| `src/permission.ts` | 权限、路由守卫相关入口 |
| `src/router` | 路由定义和动态路由 |
| `src/store` | Pinia 状态管理 |
| `src/api` | 后端接口封装 |
| `src/views` | 业务页面 |
| `src/components` | 通用组件 |
| `src/layout` | 后台布局 |
| `src/utils` | 工具函数 |

`src/views` 下的业务模块包括 `system`、`infra`、`mall`、`erp`、`crm`、`bpm`、`pay`、`report`、`member`、`mp`、`im`、`iot`、`mes`、`wms`、`ai`。

## 初步判断

这个项目适合做业务后台二开，因为模块路径直接：

- 后端模块通常能在 `src/api/<module>` 和 `src/views/<module>` 找到对应入口。
- 权限和菜单通常要结合 `src/permission.ts`、路由和后端菜单接口一起读。
- 和 [[yudao-ui-admin-vben]] 相比，它的平台抽象少，但业务落地更直接。

## 读源码时要验证的问题

- 登录后动态路由如何生成。
- 菜单权限和按钮权限在哪里判断。
- `src/api` 的接口命名是否和后端 Controller 路径一致。
- 一个典型列表页如何组织查询条件、表格、弹窗和表单。

## Obsidian 关联

- 底层概念：[[boundaries]]、[[abstractions]]
- Vben 对照：[[monorepo-frontend-map]]
- 前端对比：[[yudao-ui-admin-vue3-vs-vben]]
- 后端项目：[[zhijiantianya--ruoyi-vue-pro]]
