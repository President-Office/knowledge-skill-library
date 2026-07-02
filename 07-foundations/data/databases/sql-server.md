---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, relational, sql-server]
---

# SQL Server

## 核心定位

SQL Server 是 Microsoft 生态中的企业级关系型数据库。它常见于 Windows Server、.NET、企业 [[oltp]]、报表、BI 和传统政企系统。

## 适合场景

- Microsoft 技术栈为主的企业系统。
- 需要和 Windows、Active Directory、Power BI、SSIS/SSRS 等生态协同的系统。
- 传统企业数据仓库、报表和业务系统。

## 学习重点

| 主题 | 为什么重要 |
| --- | --- |
| T-SQL | SQL Server 有自己的 SQL 方言和过程语言 |
| 企业集成 | Microsoft 生态协同是它的重要价值 |
| 权限治理 | 企业环境常需要细粒度权限和审计 |
| 迁移差异 | 和 MySQL/PostgreSQL 在类型、分页、函数、过程上都有差异 |

## 在当前项目中观察

- Java 后台平台如果声明支持 SQL Server，需要关注 MyBatis / ORM 方言、分页 SQL、字段类型和迁移脚本差异。
- [[zhijiantianya--ruoyi-vue-pro]] 和 [[zhijiantianya--yudao-cloud]] 的多数据库支持可以作为观察入口。

## 不要误解

- SQL Server 的价值不只在数据库本身，也在 Microsoft 企业生态。
- 跨数据库兼容时，不要只改连接驱动，还要检查 SQL 方言和迁移脚本。

## 关联

- [[database]]
- [[oltp]]
- [[oracle-database]]
- [[mysql]]
