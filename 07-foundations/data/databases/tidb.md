---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, distributed-sql, tidb]
---

# TiDB

## 核心定位

TiDB 是兼容 MySQL 协议的分布式 SQL 数据库。它适合理解关系型数据库在 [[oltp]] 水平扩展、分布式事务、HTAP 和大规模数据场景中的取舍。

## 适合场景

- 单机 MySQL 容量或写入压力成为瓶颈的业务。
- 希望保留 SQL 和 MySQL 协议兼容，又需要水平扩展。
- 需要同时支持在线业务查询和一定分析能力的场景。

## 学习重点

| 主题 | 为什么重要 |
| --- | --- |
| 分布式 SQL | 关系模型和分布式存储结合后的复杂度 |
| MySQL 兼容 | 降低迁移成本，但不等于完全无差异 |
| 分布式事务 | 需要理解一致性、延迟和冲突 |
| 扩展成本 | 分布式数据库解决容量问题，也引入运维和查询规划复杂度 |

## 在当前项目中观察

- [[zhijiantianya--ruoyi-vue-pro]] 等后台系统如果支持 TiDB，重点观察 SQL 方言、事务、分页、索引和运维假设是否兼容。

## 不要误解

- TiDB 不是默认替代 MySQL 的选项，只有在容量、扩展或架构要求明确时才值得引入。
- 分布式数据库不会消除数据建模问题，只会把错误建模放大。

## 关联

- [[database]]
- [[oltp]]
- [[olap]]
- [[mysql]]
- [[boundaries]]、[[abstractions]]
