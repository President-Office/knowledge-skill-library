---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, document, mongodb]
---

# MongoDB

## 核心定位

MongoDB 是面向文档的 NoSQL 数据库。它用文档模型表达数据，适合 schema 变化较快、对象嵌套明显、读写围绕文档聚合的场景。

它也可以承载 operational workload，但不是典型关系型 [[oltp]] 样本。读 MongoDB 时更应该关注文档模型、聚合查询、索引和应用层约束。

## 适合场景

- 内容、配置、事件、日志、用户画像等文档结构明显的数据。
- 字段变化频繁、不适合一开始就严格关系建模的业务。
- 应用层以完整对象读写为主，而不是复杂跨表 join。

## 学习重点

| 主题 | 为什么重要 |
| --- | --- |
| 文档模型 | 决定数据嵌套、冗余和查询方式 |
| 聚合管道 | MongoDB 的复杂查询主要通过 aggregation 表达 |
| 索引 | 文档数据库同样需要认真设计索引 |
| Schema 边界 | 灵活 schema 不等于没有数据约束 |

## 在当前项目中观察

- [[payloadcms--payload]]：数据库适配器支持文档数据库和关系型数据库，适合观察同一套 collection 配置如何映射不同存储。

## 不要误解

- MongoDB 不是“没有 schema”，而是 schema 更多由应用和约定管理。
- 文档数据库不适合所有强关系、强事务、复杂 join 的业务。

## 关联

- [[database]]
- [[oltp]]
- [[postgresql]]
- [[payload]]
