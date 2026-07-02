---
type: open-source-project
status: active
source: gitee
repo: yudaocode/yudao-ui-admin-vben
homepage: https://gitee.com/yudaocode/yudao-ui-admin-vben
license: MIT
language: TypeScript / Vue
created: 2026-07-01
updated: 2026-07-01
tags: [yudao, vben, vue3, monorepo, turbo, admin, frontend]
---

# yudaocode/yudao-ui-admin-vben

## 一句话定位

`yudao-ui-admin-vben` 是芋道源码基于 Vben Admin 5 改造的后台前端工程，定位更接近“平台化后台前端底座”，通过 monorepo 组织多 UI 应用和共享 packages。

## 为什么学它

- 它可以用来学习 Vben Admin 5 的工程组织方式：`apps/` 承载不同 UI 应用，`packages/` 承载共享能力。
- 它同时提供 Element Plus、Ant Design Vue、Naive UI、TDesign 等不同 UI 入口，适合评估长期后台前端平台化路线。
- 它有更强的工程治理和抽象能力，但对团队学习、迁移、调试和 CI/CD 的要求也更高。

## 技术栈初判

| 层次 | 技术 |
| --- | --- |
| 前端框架 | [[Vue 3]] |
| 工程底座 | [[Vben Admin]] 5 |
| 构建工具 | [[Vite]]、[[Turborepo]] |
| 语言 | [[TypeScript]] |
| 包管理 / 工作区 | [[pnpm workspace]] |
| UI 应用 | [[Element Plus]]、[[Ant Design Vue]]、[[Naive UI]]、[[TDesign]] 等 |
| 代码质量 | [[ESLint]]、[[Oxlint]]、[[Stylelint]]、[[Vitest]]、[[cspell]]、[[lefthook]] |

## 目录入口

```text
yudao-ui-admin-vben/
├── apps
│   ├── web-antd
│   ├── web-antdv-next
│   ├── web-ele
│   ├── web-naive
│   └── web-tdesign
├── docs
├── internal
├── packages
│   ├── @core
│   ├── constants
│   ├── effects
│   ├── icons
│   ├── locales
│   ├── preferences
│   ├── stores
│   ├── styles
│   ├── types
│   └── utils
├── package.json
├── pnpm-workspace.yaml
└── turbo.json
```

## Element Plus 应用入口

如果要和 `yudao-ui-admin-vue3` 做近似对比，优先看 `apps/web-ele/`：

```text
apps/web-ele/
├── public
├── src
│   ├── adapter
│   ├── api
│   ├── assets
│   ├── components
│   ├── layouts
│   ├── locales
│   ├── plugins
│   ├── router
│   ├── store
│   ├── types
│   ├── utils
│   ├── views
│   ├── app.vue
│   ├── bootstrap.ts
│   ├── main.ts
│   └── preferences.ts
├── package.json
└── vite.config.ts
```

`apps/web-ele/src/views/` 下可见模块：

```text
system、infra、mall、erp、crm、bpm、pay、report、member、mp、im、iot、mes、wms、ai
```

## 快速结论

- 值得学的点：Vben Admin 5 的 monorepo 组织、多 UI 应用、共享 packages、偏好配置、布局和请求抽象。
- 不适合照搬的点：如果团队当前主要目标是快速交付业务后台页面，直接切换到 Vben 会增加学习、迁移、调试和部署成本。
- 可复用到自己项目的点：后台前端平台化分层、多 UI app 组织、共享工具包治理、偏好配置体系。

## 当前判断

`yudao-ui-admin-vben` 适合做平台底座评估，不适合作为所有业务后台的默认起点。更稳妥的方式是单独开 spike，迁移一个列表页、一个表单页、一个权限菜单入口，再决定是否作为长期路线。

## 相关笔记

- [[yudao-ui-admin-vue3-vs-vben]]
- [[yudaocode--yudao-ui-admin-vue3]]
