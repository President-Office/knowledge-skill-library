---
type: framework-characteristics
status: draft
project: payloadcms/payload
created: 2026-07-02
updated: 2026-07-02
---

# Payload 特点

项目主卡：[[payloadcms--payload]]

## 核心定位

[[TypeScript]] / [[Next.js]] 全栈后台与 CMS 框架。它通过代码配置 collections、fields、hooks、access control，生成 [[Admin Panel]]、[[API]]、[[GraphQL]]、[[SDK]]，并和 [[Next.js]] 应用融合。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| 代码配置优先 | 通过 [[TypeScript]] 配置 collection、field、access、hook | 学类型安全后台建模 |
| [[Next.js]] 融合 | 后台、CMS、业务应用可在 Next 工程内协同 | 学全栈后台工程形态 |
| 内置 [[Admin Panel]] | 根据配置生成管理界面 | 学配置驱动后台 UI |
| 多数据库适配 | MongoDB、Postgres、SQLite 等适配包 | 学数据库适配器设计 |
| [[插件体系]] 丰富 | [[多租户]]、[[Search]]、[[SEO]]、[[Stripe]]、[[MCP]]、[[Form Builder]] 等插件 | 学后台平台扩展机制 |
| MIT 许可证 | 相对适合学习和二开参考 | 可作为 TS 后台框架样本 |

## 最适合怎么读

1. 先读 `packages/payload`、`packages/next`、`packages/ui` 的包边界。
2. 再读 blank / postgres 模板里的配置入口。
3. 深读 collections、fields、hooks、access control、database adapters 和 plugins。

## 不要误解

- 不要把它当数据库优先平台，它更偏代码配置优先。
- 不要把它只当 CMS，它也可以作为 TS/Next 后台和 [[API]] 框架。
- 不要忽略 [[Next.js]] 集成，它是 Payload 当前架构理解的关键。

## 关联

- [[solid]]
- [[monorepo]]
- [[headless-cms]]
- [[directus]]
- [[database-first-admin-platforms]]
- [[pairwise-backend-comparisons]]
