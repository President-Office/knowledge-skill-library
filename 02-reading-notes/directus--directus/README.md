# Directus 源码阅读索引

项目主卡：[[directus--directus]]
特点卡：[[directus]]

## 阅读主题网络

| 主题 | 关联源码入口 | 关键概念 |
| --- | --- | --- |
| [[02-reading-notes/directus--directus/monorepo-structure]] | `api`、`app`、`sdk`、`packages`、`pnpm-workspace.yaml` | [[monorepo]]、[[Monorepo Package]]、[[pnpm workspace]] |
| [[02-reading-notes/directus--directus/runtime-entrypoints]] | `directus`、`api`、`package.json` | [[CLI]]、[[Node.js]]、[[API]] |
| [[02-reading-notes/directus--directus/database-first-model]] | `api/src`、`packages` | [[Database-first]]、[[schema]]、[[database]] |
| [[02-reading-notes/directus--directus/metadata-and-permissions]] | metadata、collections、fields、permissions 相关模块 | [[Metadata]]、[[权限模型]]、[[Admin Panel]] |
| [[02-reading-notes/directus--directus/admin-app-architecture]] | `app/src` | [[Admin App]]、[[Vue]]、[[Vite]] |
| [[02-reading-notes/directus--directus/sdk-and-api-contract]] | `sdk/src`、`api/src` | [[SDK]]、[[API]]、[[REST]]、[[GraphQL]] |
| [[02-reading-notes/directus--directus/extension-system]] | `packages`、`api/src`、`app/src` | [[插件体系]]、[[Monorepo Package]]、[[machine-readable-software-systems]] |

## 当前问题

- [ ] 本地确认 Node 22 和 pnpm 10。
- [ ] 跑通 Docker 或本地开发环境。
- [ ] 创建一个 collection 并观察数据库表、元数据和 Admin UI 的变化。
- [ ] 追踪 collection 列表接口从 [[Admin App]] 到 [[API]] 的调用链。
- [ ] 追踪[[权限模型]]配置如何影响 [[API]] 返回。
