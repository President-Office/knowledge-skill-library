---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, relational, mariadb]
---

# MariaDB

## 核心定位

MariaDB 是 [[MySQL]] 生态兼容路线中的关系型数据库。学习它时，重点不在于把它和 [[MySQL]] 背成两个完全不同的体系，而是理解 [[oltp]] 场景下的兼容、替代、差异和迁移成本。

## 适合场景

- 需要 [[MySQL]] 生态兼容的业务系统。
- 团队已有 [[MySQL]] 使用经验，但部署或许可证策略选择 MariaDB。
- 一些 Linux 发行版或平台默认提供 MariaDB 的环境。

## 学习重点

| 主题 | 为什么重要 |
| --- | --- |
| MySQL 兼容性 | 决定现有应用迁移成本 |
| SQL 方言差异 | 兼容不等于完全一致 |
| 存储引擎 | 影响事务、索引和性能表现 |
| 运维策略 | 备份、复制、监控和 MySQL 接近但需确认差异 |

## 在当前项目中观察

- [[zhijiantianya--ruoyi-vue-pro]] 和 [[zhijiantianya--yudao-cloud]] 这类 Java 后台通常会声明支持多种关系型数据库，MariaDB 常作为 [[MySQL]] 兼容选项出现。

## 不要误解

- MariaDB 兼容 [[MySQL]]，但不要默认所有 SQL、驱动、函数和运维行为完全一致。
- 迁移前要确认驱动、SQL 方言、索引、字符集和事务行为。

## 关联

- [[database]]
- [[oltp]]
- [[mysql]]
