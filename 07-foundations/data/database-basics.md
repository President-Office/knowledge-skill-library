---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, schema, data-modeling]
---

# 数据库基础概念

## 核心问题

学习后台系统时，数据库不是只要知道 MySQL、PostgreSQL 这些产品名就够了。真正影响系统理解的是更基础的概念：SQL、ORM、schema、表、列、行、主键、外键、约束、索引、事务。

一句话理解：

**数据库基础概念决定业务事实如何被长期保存、约束、查询和演进。**

## 基础概念地图

| 概念 | 解决的问题 |
| --- | --- |
| [[sql]] | 如何定义结构、查询数据、修改数据和控制事务 |
| [[orm]] | 程序对象如何映射到数据库表、列、行和 SQL |
| [[schema]] | 数据库对象如何被组织和命名 |
| [[table]] | 同一类业务事实如何被集合化保存 |
| [[column]] | 一个业务事实有哪些字段和类型 |
| [[row]] | 一条具体业务事实如何落库 |
| [[primary-key]] | 一行数据如何被唯一识别 |
| [[foreign-key]] | 表和表之间的引用关系如何表达 |
| [[database-constraint]] | 数据库如何阻止非法数据进入 |
| [[database-index]] | index 如何用额外结构更快定位数据 |
| [[database-transaction]] | 多个读写操作如何保持一致 |

## 从业务到数据库

以高考志愿系统为例：

```text
业务概念：院校、专业、录取分数、学生、志愿方案
数据库表达：school 表、major 表、admission_score 表、student_profile 表、volunteer_plan 表
```

数据库设计要回答：

- 哪些概念应该成为表？
- 哪些属性应该成为列？
- 哪个字段能唯一标识一行？
- 表之间是一对一、一对多，还是多对多？
- 哪些数据必须唯一、不能为空、必须合法？
- 哪些查询高频，需要索引？
- 哪些操作必须放在一个事务里？

## 和后台代码的关系

| 数据库概念 | 后台代码里常见对应 |
| --- | --- |
| 表 | Entity / DO / Model |
| 行 | 一个对象实例或一条记录 |
| 列 | 字段、属性 |
| 主键 | `id`、业务唯一编号 |
| 外键 | 关联 ID、关系字段 |
| 约束 | 校验、唯一性、状态合法性 |
| 索引 | 查询条件、排序条件、唯一查询 |
| 事务 | Service 层的原子业务流程 |

## 学习顺序

建议先按这个顺序理解：

```text
sql -> schema -> table -> column / row -> primary key -> foreign key -> constraint -> index -> transaction -> orm
```

这个顺序不是数据库产品手册的顺序，而是后台业务建模时最容易建立直觉的顺序。

## 关联

- [[database]]
- [[sql]]
- [[orm]]
- [[schema]]
- [[table]]
- [[primary-key]]
- [[foreign-key]]
- [[database-index]]
- [[database-transaction]]
- [[oltp]]
