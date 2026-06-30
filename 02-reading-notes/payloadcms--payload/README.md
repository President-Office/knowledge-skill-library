# Payload 源码阅读索引

项目主卡：[[01-projects/payloadcms--payload|payloadcms/payload]]

## 阅读顺序

| 顺序 | 主题 | 状态 | 笔记 |
| --- | --- | --- | --- |
| 1 | Monorepo 结构 | 待读 | `monorepo-structure.md` |
| 2 | 核心包边界 | 待读 | `core-package-boundaries.md` |
| 3 | Collections 和 Fields | 待读 | `collections-and-fields.md` |
| 4 | Access Control 和 Hooks | 待读 | `access-control-and-hooks.md` |
| 5 | Next.js 集成 | 待读 | `nextjs-integration.md` |
| 6 | Admin Panel 架构 | 待读 | `admin-panel-architecture.md` |
| 7 | 数据库适配器 | 待读 | `database-adapters.md` |
| 8 | 插件系统 | 待读 | `plugin-system.md` |

## 当前问题

- [ ] 本地确认 Node、pnpm 和数据库版本。
- [ ] 跑通 `templates/blank` 或 `templates/with-postgres`。
- [ ] 创建一个 collection 并观察 Admin UI、REST、GraphQL、类型生成。
- [ ] 追踪 collection 配置如何影响数据库 schema 和 API。
- [ ] 追踪一个 access control hook 的执行链路。
