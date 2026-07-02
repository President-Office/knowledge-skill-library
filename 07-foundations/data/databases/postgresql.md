---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, relational, postgresql]
---

# PostgreSQL

## 核心定位

PostgreSQL 是功能完整、类型系统强、扩展能力强的关系型数据库。它适合学习 [[oltp]]、更严谨的数据建模、复杂 SQL、事务一致性、JSONB、全文搜索、地理信息和扩展机制。

## 适合场景

- 需要复杂查询和强一致事务的业务系统。
- 既有关系数据，又需要部分半结构化字段的系统。
- 需要使用数据库扩展能力的产品，例如 GIS、全文检索、复杂索引。

## 学习重点

| 主题 | 为什么重要 |
| --- | --- |
| 类型系统 | 更严谨的数据表达能减少业务层歧义 |
| JSONB | 在关系模型中承载半结构化数据 |
| 索引类型 | B-tree、GIN、GiST 等索引适配不同查询模式 |
| 事务和锁 | 复杂业务系统必须理解并发写入行为 |
| 扩展机制 | PostgreSQL 的生态价值很大一部分来自扩展 |

## 在当前项目中观察

- [[directus--directus]]：数据库优先平台通常需要理解 PostgreSQL 这类强关系数据库的 schema 能力。
- [[payloadcms--payload]]：数据库适配器如何把 collection 配置映射到 PostgreSQL。
- [[headless-cms]]：内容模型和 API 平台常常受数据库能力影响。

## 不要误解

- PostgreSQL 不是“更高级的 MySQL”这么简单，它的类型、扩展和查询能力会影响建模方式。
- JSONB 不是让数据库随意无结构化，核心业务字段仍然要认真建模。

## 关联

- [[database]]
- [[oltp]]
- [[mysql]]
- [[sqlite]]
