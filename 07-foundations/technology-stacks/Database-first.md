---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, database, architecture]
---

# Database-first

Database-first 是从已有数据库结构出发构建后台、API 和管理端的路线。

它和 code-first 的区别在于：系统先尊重数据库中的表、字段、关系和约束，再通过元数据补充权限、展示、校验和交互配置。

## 学习重点

- 数据库 schema 如何被读取、缓存和转换成应用模型。
- 元数据如何补足数据库本身不表达的业务语义。
- 复杂业务规则如何避免散落在动态配置之外。

## 关联

- [[database]]
- [[schema]]
- [[Metadata]]
- [[Instant API]]
- [[database-first-admin-platforms]]
