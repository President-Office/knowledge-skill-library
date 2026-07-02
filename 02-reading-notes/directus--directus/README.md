# Directus 源码阅读索引

项目主卡：[[directus--directus]]
特点卡：[[directus]]

## 已有笔记

| 顺序 | 主题 | 状态 | 笔记 |
| --- | --- | --- | --- |
| 1 | Monorepo 结构 | 初稿 | [[02-reading-notes/directus--directus/monorepo-structure]] |

## 后续主题

- 运行入口
- 数据库优先模型
- 元数据和权限
- [[Admin App]] 架构
- [[SDK]] 和 [[API]] 契约
- 扩展系统

## 当前问题

- [ ] 本地确认 Node 22 和 pnpm 10。
- [ ] 跑通 Docker 或本地开发环境。
- [ ] 创建一个 collection 并观察数据库表、元数据和 Admin UI 的变化。
- [ ] 追踪 collection 列表接口从 [[Admin App]] 到 [[API]] 的调用链。
- [ ] 追踪[[权限模型]]配置如何影响 [[API]] 返回。
