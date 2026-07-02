---
type: open-source-project
status: active
source: gitee
repo: yudaocode/yudao-ui-admin-vue3
homepage: https://gitee.com/yudaocode/yudao-ui-admin-vue3
license:
language: TypeScript / Vue
created: 2026-07-01
updated: 2026-07-01
tags: [yudao, ruoyi, vue3, element-plus, admin, frontend]
---

# yudaocode/yudao-ui-admin-vue3

## 一句话定位

`yudao-ui-admin-vue3` 是芋道源码维护的 Vue3 管理后台前端，定位是承接 Yudao / RuoYi 体系的业务后台页面、权限菜单、表单列表和各业务模块前端。

## 为什么学它

- 它是当前芋道 Vue3 后台的直接业务开发入口，适合学习 Yudao 前端如何组织系统、基础设施、商城、ERP、CRM、BPM、支付等模块。
- 它采用单应用结构，业务页面集中在 `src/views/`，比 monorepo 更适合快速二开和落业务页面。
- 对新粮供应链金融、Future UI Admin Vue3 等业务后台项目，它更接近实际改造路径。

## 技术栈初判

| 层次 | 技术 |
| --- | --- |
| 前端框架 | [[Vue 3]] |
| 构建工具 | [[Vite]] |
| 语言 | [[TypeScript]] |
| UI 组件 | [[Element Plus]] |
| 状态管理 | [[Pinia]] |
| 路由 | [[Vue Router]] |
| 样式 / 原子类 | [[UnoCSS]] |
| 代码质量 | [[ESLint]]、[[Prettier]]、[[Stylelint]]、[[vue-tsc]] |

## 目录入口

```text
yudao-ui-admin-vue3/
├── build
├── public
├── src
│   ├── api
│   ├── assets
│   ├── components
│   ├── config
│   ├── directives
│   ├── hooks
│   ├── layout
│   ├── locales
│   ├── plugins
│   ├── router
│   ├── store
│   ├── styles
│   ├── utils
│   ├── views
│   ├── App.vue
│   ├── main.ts
│   └── permission.ts
├── types
├── package.json
├── vite.config.ts
└── uno.config.ts
```

## 业务模块入口

`src/views/` 下可见模块：

```text
system、infra、mall、erp、crm、bpm、pay、report、member、mp、im、iot、mes、wms、ai
```

## 快速结论

- 值得学的点：Yudao 前端模块组织、菜单权限、业务页面结构、Element Plus 后台交互模式。
- 不适合照搬的点：如果目标是集团统一前端平台底座，多 UI、多应用、多包治理能力不如 Vben 体系。
- 可复用到自己项目的点：业务模块目录组织、API / views 对应关系、权限入口、构建环境配置。

## 当前判断

`yudao-ui-admin-vue3` 更适合作为业务后台二开的起点。对需要快速完成列表、表单、审批、权限和业务模块页面的新粮类项目，优先级高于 `yudao-ui-admin-vben`。

## 相关笔记

- [[yudao-ui-admin-vue3-vs-vben]]
- [[zhijiantianya--ruoyi-vue-pro]]
