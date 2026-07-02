# Payload 源码阅读索引

项目主卡：[[payloadcms--payload]]
特点卡：[[payload]]

## 已有笔记

| 顺序 | 主题 | 状态 | 笔记 |
| --- | --- | --- | --- |
| 1 | Monorepo 结构 | 初稿 | [[02-reading-notes/payloadcms--payload/monorepo-structure]] |

## 后续主题

- 核心包边界
- Collections 和 Fields
- Access Control 和 Hooks
- [[Next.js]] 集成
- Admin Panel 架构
- 数据库适配器
- 插件系统

## 当前问题

- [ ] 本地确认 Node、pnpm 和数据库版本。
- [ ] 跑通 `templates/blank` 或 `templates/with-postgres`。
- [ ] 创建一个 collection 并观察 Admin UI、[[REST]]、[[GraphQL]]、类型生成。
- [ ] 追踪 collection 配置如何影响数据库 [[schema]] 和 [[API]]。
- [ ] 追踪一个 access control hook 的执行链路。
