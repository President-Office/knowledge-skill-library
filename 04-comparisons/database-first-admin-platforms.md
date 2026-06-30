---
type: comparison
status: draft
projects: [directus/directus, payloadcms/payload]
created: 2026-06-30
updated: 2026-06-30
---

# 后台/CMS/API 平台对比

## 结论

- `directus/directus` 代表数据库优先路线：从现有数据库出发生成 Headless CMS、Admin、API、权限和 SDK。
- `payloadcms/payload` 代表 TypeScript/Next.js 代码配置路线：从 collection 配置出发生成后台、API、类型和 Admin Panel。
- 二者都不同于 RuoYi/JeecgBoot 的代码生成路线：它们更强调平台运行时、配置模型和产品化后台能力。
- 后续建议继续补 `Strapi`、`Supabase`，形成 CMS / Backend Platform / Admin Platform 对比。

## 当前项目

| 项目 | 定位 | 技术栈 | License | 学习重点 |
| --- | --- | --- | --- | --- |
| Directus | Database-first Headless CMS / Admin / API | TypeScript、Vue、Node、pnpm monorepo | MSCL-1.0-GPL | Schema introspection、metadata、permissions、Admin App、SDK、extensions |
| Payload | TypeScript / Next.js 全栈后台和 CMS 框架 | TypeScript、Next.js、pnpm、Turborepo | MIT | Collections、fields、hooks、access control、Admin Panel、database adapters、plugins |

## 与后台脚手架的差异

| 维度 | 代码生成后台脚手架 | Directus | Payload |
| --- | --- | --- | --- |
| 起点 | 表结构或模型生成代码 | 现有数据库和元数据 | TypeScript collection 配置 |
| 主要产物 | 后端代码、前端页面、接口 | 运行时 Admin、API、权限、SDK | Admin Panel、API、类型、数据库映射 |
| 修改方式 | 生成后人工维护代码 | 在线配置和元数据驱动 | 代码配置 + 插件扩展 |
| 适合场景 | 业务逻辑重、需要深度定制 | 数据管理、内容管理、快速 API、通用后台 | Next.js 全栈应用、CMS、类型安全后台 |
| 风险 | 生成代码后容易分叉 | 平台约束强，license 要评估 | 要接受 Payload 的框架模型和 Next 集成方式 |

## 后续阅读问题

- [ ] Directus 如何映射现有数据库 schema？
- [ ] Directus 元数据表和业务表如何共存？
- [ ] Field / collection / relation / permission 的核心模型是什么？
- [ ] Payload 的 collection 配置如何生成 Admin、API、类型和数据库映射？
- [ ] Directus 和 Payload 在建模方式上有什么差异？
- [ ] 数据库优先路线和 JeecgBoot 在线表单路线哪个更适合内部系统？
