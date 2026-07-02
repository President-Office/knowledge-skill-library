---
type: foundation-index
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, database-index]
---

# 常用数据库

这个目录用于理解常见数据库的长期定位、适用场景和学习重点。这里不记录版本、热度和临时状态，只沉淀稳定概念。

## 分类索引

| 类型 | 数据库 | 适合理解什么 |
| --- | --- | --- |
| 关系型 | [[mysql]] | Web 后台、[[oltp]]、事务、索引、表结构、主从复制 |
| 关系型 | [[postgresql]] | [[oltp]]、强类型、复杂查询、扩展、JSONB、地理信息等能力 |
| 关系型 | [[sqlite]] | 嵌入式 OLTP、本地应用、轻量原型 |
| 关系型 | [[mariadb]] | MySQL 兼容生态、OLTP 和替代路线 |
| 商业关系型 | [[oracle-database]] | 大型企业 OLTP、强事务、复杂 SQL、商业数据库治理 |
| 商业关系型 | [[sql-server]] | Microsoft 生态企业 OLTP 和 BI 集成 |
| 分布式关系型 | [[tidb]] | 分布式 SQL、水平扩展、MySQL 协议兼容、HTAP |
| 国产关系型 | [[dm-database]] | 国产化、信创、Oracle/MySQL 迁移兼容、企业 OLTP |
| 文档型 | [[mongodb]] | 文档模型、灵活 schema、聚合查询 |
| 键值/缓存 | [[redis]] | 缓存、会话、分布式锁、排行榜、轻量队列 |
| 搜索 | [[elasticsearch]] | 搜索、倒排索引、日志检索、全文查询 |
| 分析型 | [[clickhouse]] | 列式存储、OLAP、聚合分析、报表查询 |

## 选择时先问的问题

- 数据模型是强关系、文档、键值、搜索还是分析？
- 读多还是写多？事务是否关键？
- 数据量增长靠单机增强、分库分表，还是分布式数据库？
- 查询是按主键、条件过滤、全文搜索，还是大规模聚合？
- 业务是否要求国产化、商业支持或特定云生态？

## 关联

- [[database]]
- [[database-basics]]
- [[schema]]
- [[database-index]]
- [[database-transaction]]
- [[oltp]]
- [[olap]]
- [[boundaries]]、[[abstractions]]
- [[headless-cms]]
