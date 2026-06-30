# Directus 源码阅读索引

项目主卡：[[01-projects/directus--directus|directus/directus]]

## 阅读顺序

| 顺序 | 主题 | 状态 | 笔记 |
| --- | --- | --- | --- |
| 1 | Monorepo 结构 | 待读 | `monorepo-structure.md` |
| 2 | 运行入口 | 待读 | `runtime-entrypoints.md` |
| 3 | 数据库优先模型 | 待读 | `database-first-model.md` |
| 4 | 元数据和权限 | 待读 | `metadata-and-permissions.md` |
| 5 | Admin App 架构 | 待读 | `admin-app-architecture.md` |
| 6 | SDK 和 API 契约 | 待读 | `sdk-and-api-contract.md` |
| 7 | 扩展系统 | 待读 | `extension-system.md` |

## 当前问题

- [ ] 本地确认 Node 22 和 pnpm 10。
- [ ] 跑通 Docker 或本地开发环境。
- [ ] 创建一个 collection 并观察数据库表、元数据和 Admin UI 的变化。
- [ ] 追踪 collection 列表接口从 Admin App 到 API 的调用链。
- [ ] 追踪权限配置如何影响 API 返回。
