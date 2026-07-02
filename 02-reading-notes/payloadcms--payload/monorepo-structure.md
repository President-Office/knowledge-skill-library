---
type: source-reading
status: initial
project: payloadcms/payload
topic: Monorepo 结构
created: 2026-07-02
updated: 2026-07-02
---

# Payload - Monorepo 结构

项目主卡：[[payloadcms--payload]]
特点卡：[[payload]]

## 阅读目标

理解 Payload 如何把 [[TypeScript]] / [[Next.js]] 后台框架拆成核心包、Next 集成、Admin UI、数据库适配器、插件和模板。

## 已确认结构

| 目录 / 包 | 初步职责 |
| --- | --- |
| `packages/payload` | 核心框架 |
| `packages/next` | [[Next.js]] 集成 |
| `packages/ui` | [[Admin App]] 和共享界面能力 |
| `packages/sdk` | [[SDK]] |
| `packages/graphql` | [[GraphQL]] 支持 |
| `packages/db-*` | MongoDB、Postgres、SQLite 等数据库适配 |
| `packages/plugin-*` | [[Form Builder]]、[[多租户]]、[[Search]]、[[SEO]]、[[Stripe]]、[[MCP]] 等插件 |
| `templates` | blank、website、ecommerce、with-postgres 等模板 |
| `examples` | 示例项目 |

## 初步判断

Payload 的核心不是“已有数据库变后台”，而是“用 TypeScript 配置定义后台”。这和 [[02-reading-notes/directus--directus/monorepo-structure]] 形成清晰对照：

- Directus：数据库优先，适合接管已有 [[schema]]。
- Payload：代码配置优先，适合在 [[Next.js]]/[[TypeScript]] 项目里内嵌后台、CMS 和 [[API]]。

## 读源码时要验证的问题

- `packages/payload` 暴露的核心配置入口是什么。
- `packages/next` 如何接入 [[Next.js]] App Router。
- Admin UI 是如何从 collection 配置生成的。
- 数据库适配器如何复用同一套 collection 配置。
- 插件如何修改 collection、admin、[[API]] 或运行时行为。

## Obsidian 关联

- 底层概念：[[solid]]、[[monorepo]]、[[headless-cms]]
- 框架特点：[[payload]]
- Directus 对照：[[02-reading-notes/directus--directus/monorepo-structure]]
- 平台对比：[[database-first-admin-platforms]]
