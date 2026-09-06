# Payload 源码阅读索引

项目主卡：[[payloadcms--payload]]
特点卡：[[payload]]

## 阅读主题网络

| 主题 | 关联源码入口 | 关键概念 |
| --- | --- | --- |
| [[02-reading-notes/payloadcms--payload/monorepo-structure]] | `packages`、`pnpm-workspace.yaml`、`turbo.json` | [[monorepo]]、[[Turborepo]] |
| [[02-reading-notes/payloadcms--payload/core-package-boundaries]] | `packages/payload`、`packages/next`、`packages/ui` | [[Monorepo Package]]、[[SDK]] |
| [[02-reading-notes/payloadcms--payload/collections-and-fields]] | `packages/payload`、`templates/blank` | [[TypeScript]]、[[Metadata]]、[[schema]] |
| [[02-reading-notes/payloadcms--payload/access-control-and-hooks]] | collection 配置、hooks、access control | [[权限模型]]、[[API]] |
| [[02-reading-notes/payloadcms--payload/nextjs-integration]] | `app/(payload)`、`packages/next` | [[Next.js]]、[[headless-cms]] |
| [[02-reading-notes/payloadcms--payload/admin-panel-architecture]] | `packages/ui`、`packages/payload` | [[Admin Panel]]、[[Admin App]] |
| [[02-reading-notes/payloadcms--payload/database-adapters]] | `packages/db-postgres`、`packages/db-mongodb`、`packages/db-sqlite` | [[数据库适配器]]、[[postgresql]]、[[mongodb]]、[[sqlite]] |
| [[02-reading-notes/payloadcms--payload/plugin-system]] | `packages/plugin-*` | [[插件体系]]、[[Form Builder]]、[[MCP]] |

## 当前问题

- [ ] 本地确认 Node、pnpm 和数据库版本。
- [ ] 跑通 `templates/blank` 或 `templates/with-postgres`。
- [ ] 创建一个 collection 并观察 Admin UI、[[REST]]、[[GraphQL]]、类型生成。
- [ ] 追踪 collection 配置如何影响数据库 [[schema]] 和 [[API]]。
- [ ] 追踪一个 access control hook 的执行链路。
