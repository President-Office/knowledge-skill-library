---
type: source-reading
status: initial
project: payloadcms/payload
topic: 数据库适配器
created: 2026-07-02
updated: 2026-07-02
---

# Payload - 数据库适配器

项目主卡：[[payloadcms--payload]]

## 核心关系

数据库适配器把同一套 collection 配置映射到不同数据库实现。真正的难点是类型、事务、索引、查询能力和迁移差异。

## 关联源码入口

- `packages/db-postgres`
- `packages/db-mongodb`
- `packages/db-sqlite`

## 关联概念

- [[数据库适配器]]
- [[postgresql]]
- [[mongodb]]
- [[sqlite]]
- [[schema]]
