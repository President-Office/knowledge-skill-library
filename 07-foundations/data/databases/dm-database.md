---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, relational, dm, domestic-database]
---

# 达梦 DM

## 核心定位

达梦 DM 是国产化和信创场景中常见的关系型数据库。学习它时，重点不是把它当普通 MySQL 变体，而是理解国产数据库在企业 [[oltp]] 中的适配、Oracle 兼容、SQL 方言差异和政企环境迁移要求。

## 适合场景

- 政企、信创、国产化替代场景。
- 需要从 Oracle、MySQL 等数据库迁移到国产数据库的系统。
- 对数据库选型有合规或采购要求的项目。

## 学习重点

| 主题 | 为什么重要 |
| --- | --- |
| SQL 方言 | 迁移和兼容首先会遇到 SQL、类型、函数差异 |
| 驱动适配 | Java 后台要关注 JDBC、连接池、ORM 方言 |
| 迁移脚本 | 初始化 SQL、索引、序列、分页都需要验证 |
| 国产化环境 | 数据库只是信创链路的一部分，还涉及 OS、中间件、CPU 架构 |

## 在当前项目中观察

- [[zhijiantianya--ruoyi-vue-pro]] 这类国内 Java 后台经常需要面向国产数据库做适配。
- 对比 [[oracle-database]] 能理解很多国产数据库的兼容目标。

## 不要误解

- 支持达梦不只是换连接字符串，SQL、字段类型、分页、主键策略、迁移脚本都要验证。
- 国产化适配是系统工程，不是单点数据库替换。

## 关联

- [[database]]
- [[oltp]]
- [[oracle-database]]
- [[mysql]]
