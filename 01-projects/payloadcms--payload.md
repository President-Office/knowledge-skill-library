---
type: open-source-project
status: active
source: github
repo: payloadcms/payload
homepage: https://github.com/payloadcms/payload
license: MIT
language: TypeScript / Next.js
tags: [typescript, nextjs, headless-cms, admin-panel, fullstack, monorepo, payload, cms]
created: 2026-06-30
updated: 2026-06-30
---

# payloadcms/payload

## 一句话定位

Payload 是一个开源的 TypeScript / Next.js 全栈后台框架，可以快速得到类型安全的后端、Admin Panel、Headless CMS 能力，并支持用集合配置、数据库适配器、插件、GraphQL/REST、SDK 和 Next.js 集成构建业务应用。

## 为什么学它

- 它补上当前知识库里的现代 TypeScript 全栈后台范式，和 Java/Go 后台脚手架、Frappe ERP、Directus 数据库优先平台都不同。
- 它是 MIT 许可证，比 Directus 当前的 `MSCL-1.0-GPL` 更适合作为二开参考。
- 它的 monorepo 结构覆盖核心框架、Next.js 集成、多数据库适配、GraphQL、SDK、UI、插件、存储、模板，适合学习成熟 TS 后台平台如何拆包。
- 它适合和 Directus 对比：Payload 更偏代码配置和全栈框架，Directus 更偏现有数据库和运行时元数据。

## 当前快照

查询日期：2026-06-30

| 项 | 内容 |
| --- | --- |
| 仓库 | https://github.com/payloadcms/payload |
| 平台 | GitHub |
| 描述 | Open-source, fullstack Next.js framework with TypeScript backend and admin panel |
| 默认分支 | `main` |
| 当前 `HEAD` | `e3f00c98ef4642786c1a2f7c4360ea918f1571b2` |
| 当前根版本 | `4.0.0-beta.0` |
| 主要语言 | TypeScript |
| License | MIT |
| Stars | 43,315 |
| Forks | 3,858 |
| GitHub `open_issues_count` | 840 |
| 最近推送 | 2026-06-30T14:39:16Z |
| 最近更新 | 2026-06-30T15:32:50Z |

来源：GitHub API `repos/payloadcms/payload`、`git ls-remote --symref`、根 `package.json`。数字会随时间变化。

## 技术栈初判

| 层次 | 技术/概念 |
| --- | --- |
| 语言 | TypeScript |
| Web 框架 | Next.js |
| Monorepo | pnpm workspace、Turborepo |
| 核心包 | `packages/payload` |
| Next 集成 | `packages/next` |
| 数据库适配 | MongoDB、Postgres、SQLite、D1、Vercel Postgres 等 |
| API | REST、GraphQL、SDK |
| Admin UI | `packages/ui`、内置 Admin Panel |
| 插件 | form-builder、import-export、multi-tenant、search、seo、stripe、mcp 等 |
| 存储 | S3、Azure、GCS、R2、Vercel Blob、UploadThing 等 |

## 顶层目录入口

GitHub API 在 `main` 分支看到的关键顶层结构：

```text
payload/
├── .github
├── .codex
├── .claude
├── app
├── docs
├── examples
├── packages
├── public
├── scripts
├── templates
├── test
├── tools
├── LICENSE.md
├── README.md
├── next.config.mjs
├── package.json
├── pnpm-workspace.yaml
├── turbo.json
└── vitest.config.ts
```

关键 `packages/`：

```text
packages/
├── payload
├── next
├── ui
├── sdk
├── graphql
├── db-mongodb
├── db-postgres
├── db-sqlite
├── plugin-form-builder
├── plugin-import-export
├── plugin-mcp
├── plugin-multi-tenant
├── plugin-search
├── plugin-seo
├── plugin-stripe
├── storage-s3
├── storage-azure
├── storage-gcs
└── ...
```

模板入口：

```text
templates/
├── blank
├── ecommerce
├── plugin
├── website
├── with-postgres
├── with-vercel-mongodb
├── with-vercel-postgres
└── with-cloudflare-d1
```

## 第一阶段阅读路线

### 1. 先读 monorepo 和核心包边界

目标：搞清楚 Payload 如何把核心框架、Next 集成、数据库适配、Admin UI、插件和模板拆成包。

优先阅读：

- `package.json`
- `pnpm-workspace.yaml`
- `turbo.json`
- `packages/payload`
- `packages/next`
- `packages/ui`

输出笔记：

- `02-reading-notes/payloadcms--payload/monorepo-structure.md`
- `02-reading-notes/payloadcms--payload/core-package-boundaries.md`

### 2. 再读集合配置和运行时模型

目标：理解 Payload 的核心抽象：collection、global、field、access control、hooks、uploads、auth。

优先阅读：

- `packages/payload`
- `templates/blank`
- `templates/with-postgres`
- `examples`

输出笔记：

- `02-reading-notes/payloadcms--payload/collections-and-fields.md`
- `02-reading-notes/payloadcms--payload/access-control-and-hooks.md`

### 3. 读 Next.js 集成和 Admin Panel

目标：理解 Payload 如何嵌入 Next.js，并提供 Admin UI 和业务应用同仓开发能力。

优先阅读：

- `app/(payload)`
- `packages/next`
- `packages/ui`
- `templates/website`

输出笔记：

- `02-reading-notes/payloadcms--payload/nextjs-integration.md`
- `02-reading-notes/payloadcms--payload/admin-panel-architecture.md`

### 4. 读数据库和插件体系

目标：理解数据库适配器和插件如何扩展 Payload 平台能力。

优先阅读：

- `packages/db-postgres`
- `packages/db-mongodb`
- `packages/db-sqlite`
- `packages/plugin-multi-tenant`
- `packages/plugin-form-builder`
- `packages/plugin-mcp`

输出笔记：

- `02-reading-notes/payloadcms--payload/database-adapters.md`
- `02-reading-notes/payloadcms--payload/plugin-system.md`

## 核心问题清单

- [ ] Payload 的核心配置入口是什么？
- [ ] collection / global / field / hook / access control 如何组合？
- [ ] Admin Panel 是如何根据配置生成的？
- [ ] Payload 如何与 Next.js App Router 集成？
- [ ] REST、GraphQL、SDK 的契约如何从配置生成？
- [ ] 数据库适配器如何把同一套配置映射到 MongoDB、Postgres、SQLite？
- [ ] 插件如何扩展 collection、admin、API 和运行时行为？
- [ ] Payload 的多租户插件和 JeecgBoot/RuoYi 的租户模型有什么差异？
- [ ] Payload 的代码配置路线和 Directus 的数据库优先路线如何取舍？

## 可沉淀模式

后续优先沉淀到 `03-patterns/` 的方向：

- TypeScript 全栈后台框架包边界。
- 配置驱动 Admin Panel。
- Collection/Field/Hook/Access 的业务建模方式。
- Next.js 与后台管理系统融合架构。
- 数据库适配器设计。
- 插件扩展后台平台能力。
- MIT 许可后台框架的二开参考价值。

## 当前判断

Payload 适合作为“现代 TypeScript 全栈后台 / CMS 框架”代表项目学习。它和当前已收项目的关系是：

- `Directus`：数据库优先，适合已有数据库和运行时元数据管理。
- `Payload`：代码配置优先，适合 TypeScript/Next.js 项目中嵌入后台、CMS 和业务 API。
- `JeecgBoot`：Java 低代码和在线配置。
- `ERPNext`：ERP 业务套件和 Frappe DocType。

后续读 Payload 时，重点放在 collection 配置、Admin UI 生成、Next 集成、数据库适配和插件体系。

## 相关笔记

- [[02-reading-notes/payloadcms--payload/README|源码阅读索引]]
- [[05-practice-labs/payloadcms--payload/local-setup|本地运行实验]]
- [[04-comparisons/database-first-admin-platforms|后台/CMS/API 平台对比]]
