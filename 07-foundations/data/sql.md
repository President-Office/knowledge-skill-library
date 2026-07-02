---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, sql, query, data-modeling]
---

# SQL

## 核心定位

SQL 是 Structured Query Language，结构化查询语言。它是关系型数据库中定义结构、读写数据、表达关系和控制事务的主要语言。

一句话理解：

**SQL 是业务代码和关系型数据库之间最重要的表达层。**

学习后台系统时，不能只看 Java、Go、Python 代码，还要看 SQL。因为很多真实业务边界最终会落在表结构、查询条件、索引、事务和数据迁移脚本里。

## SQL 解决什么

SQL 主要解决四类问题：

| 问题 | SQL 负责什么 |
| --- | --- |
| 结构如何定义 | 建库、建表、建索引、修改字段 |
| 数据如何读写 | 新增、查询、更新、删除记录 |
| 关系如何表达 | join、外键、聚合、子查询 |
| 一致性如何保证 | 事务、锁、约束、隔离级别 |

所以 SQL 不是“查数据的命令”这么简单。它同时连接 [[schema]]、[[table]]、[[column]]、[[row]]、[[database-index]] 和 [[database-transaction]]。

## 常见 SQL 类型

| 类型 | 关注点 | 常见语句 |
| --- | --- | --- |
| DDL | 定义数据库结构 | `create table`、`alter table`、`drop table`、`create index` |
| DML | 修改数据 | `insert`、`update`、`delete` |
| DQL | 查询数据 | `select`、`where`、`join`、`group by`、`order by` |
| DCL | 控制权限 | `grant`、`revoke` |
| TCL | 控制事务 | `begin`、`commit`、`rollback` |

在日常后台开发里，最常遇到的是 DDL、DML、DQL 和事务控制。

## 查询的基本思路

一个查询通常要回答：

- 从哪些表取数据？
- 用什么条件过滤？
- 表之间如何关联？
- 是否需要聚合统计？
- 结果如何排序和分页？
- 哪些条件需要索引支持？

典型结构：

```sql
select columns
from table_name
join other_table on relation_condition
where filter_condition
group by group_columns
having aggregate_condition
order by sort_columns
limit offset, size;
```

读 SQL 时，不要只看 `select` 后面取了哪些字段，更要看 `where`、`join`、`group by`、`order by`。这些部分决定了业务含义和性能风险。

## 和后台代码的关系

| 后台动作 | SQL 层面常见表达 |
| --- | --- |
| 创建业务对象 | `insert into ...` |
| 修改状态 | `update ... set status = ... where id = ...` |
| 查询详情 | `select ... where id = ...` |
| 查询列表 | `select ... where ... order by ... limit ...` |
| 删除数据 | `delete ...` 或逻辑删除字段更新 |
| 统计报表 | `select ... group by ...` |
| 保证原子性 | 事务包住多条 SQL |

在 MyBatis、JPA、Prisma、SQLAlchemy 等工具里，SQL 可能被 XML、注解、方法名、查询构造器或 [[orm]] 自动生成隐藏起来。但它没有消失，只是换了表达位置。

## SQL 和 Schema

[[schema]] 关注数据库结构本身，SQL 是操作这些结构和数据的语言。

```text
schema: 有哪些表、字段、约束、索引、关系
SQL: 如何创建它们、查询它们、修改它们
```

例如：

```sql
create table school (
  id bigint primary key,
  name varchar(128) not null,
  province varchar(32) not null
);

select id, name
from school
where province = '陕西'
order by name;
```

前一段 SQL 定义结构，后一段 SQL 查询业务事实。

## SQL 方言

不同数据库都支持 SQL，但不会完全一致。

| 数据库               | 需要关注的差异                |                              |
| ----------------- | ---------------------- | ---------------------------- |
| [[mysql]]         | 分页、字符集、索引、事务隔离、函数      |                              |
| [[postgresql]]    | 类型系统、JSONB、数组、窗口函数、扩展  |                              |
| [[oracle-database]] | 序列、分页、函数、存储过程、类型 |
| [[sql-server]] | T-SQL、分页、函数、权限和 Microsoft 生态 |
| [[sqlite]]        | 嵌入式场景、类型亲和性、并发边界       |                              |
| [[tidb]]          | MySQL 协议兼容下的分布式执行和事务差异 |                              |

所以“支持多数据库”不是只换连接字符串。SQL 方言、字段类型、分页语法、函数、索引和迁移脚本都要检查。

## 在开源项目里怎么观察

| 项目                             | 观察 SQL 的入口    |                               |
| ------------------------------ | ------------- | ----------------------------- |
| [[zhijiantianya--ruoyi-vue-pro]] | `mapper.xml`、初始化 SQL、代码生成表结构 |
| [[zhijiantianya--yudao-cloud]] | 多模块 SQL、分库/微服务边界、跨数据库适配 |
| [[jeecgboot--JeecgBoot]] | 在线表单、报表、代码生成背后的查询和表结构 |
| [[frappe--erpnext]] | DocType 对表结构的映射、Ledger 类流水查询 |
| [[directus--directus]] | 数据库 schema 如何驱动 API、权限和 Admin |

## 常见误区

- 以为用了 [[orm]] 就不用学 SQL：ORM 只是生成或组织 SQL，性能和一致性仍然落在数据库。
- 只看 `select` 字段，不看 `where` 和 `join`：容易误判业务边界和性能风险。
- 把 SQL 当成字符串拼接：这会带来 SQL 注入、维护困难和方言兼容问题。
- 忽略事务：多条 SQL 共同完成一个业务动作时，要判断是否必须原子提交。
- 忽略执行计划：慢查询往往不是语句长，而是索引、过滤条件、排序、分页或数据分布有问题。

## 关联

- [[database]]
- [[orm]]
- [[database-basics]]
- [[schema]]
- [[table]]
- [[column]]
- [[row]]
- [[primary-key]]
- [[foreign-key]]
- [[database-index]]
- [[database-transaction]]
- [[oltp]]
- [[olap]]
