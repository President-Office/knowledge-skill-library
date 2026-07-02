---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, relational, oracle]
---

# Oracle Database

## 核心定位

Oracle Database 是大型企业系统中常见的商业关系型数据库。它适合理解传统企业级 [[oltp]]、复杂 [[SQL]]、强事务、存储过程、权限治理、备份恢复和商业数据库生态。

## 适合场景

- 金融、电信、政企等大型核心业务系统。
- 历史系统、复杂报表、复杂事务和高可靠要求场景。
- 企业已有 Oracle 运维和授权体系的环境。

## 学习重点

| 主题         | 为什么重要                               |
| ---------- | ----------------------------------- |
| [[SQL]] 方言 | Oracle SQL 和 MySQL/PostgreSQL 有明显差异 |
| 存储过程       | 很多传统企业系统把部分业务逻辑放在数据库侧               |
| 权限和 Schema | 企业数据库治理绕不开权限、用户、Schema              |
| 迁移成本       | 从 Oracle 迁移到其他数据库通常涉及 SQL、类型和函数差异   |

## 在当前项目中观察

- [[zhijiantianya--ruoyi-vue-pro]]、[[jeecgboot--JeecgBoot]] 这类国内 Java 后台在企业项目中经常需要兼容 Oracle 或类 Oracle 数据库。
- [[dm-database]] 等国产数据库也常常涉及 Oracle 兼容迁移。

## 不要误解

- Oracle 不只是一个“更贵的 MySQL”，它带有完整企业数据库生态和历史包袱。
- 兼容 Oracle 往往意味着 SQL、分页、函数、序列、类型都要单独考虑。

## 关联

- [[database]]
- [[oltp]]
- [[sql-server]]
- [[dm-database]]
