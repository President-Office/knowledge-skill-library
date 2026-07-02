---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, schema, data-modeling]
---

# Schema

## 核心定位

Schema 是数据库对象的组织方式，也可以指一组表、视图、索引、约束等对象的结构定义。

一句话理解：

**Schema 描述数据库里有什么，以及这些东西如何被组织。**

## 两种常见含义

| 含义 | 说明 |
| --- | --- |
| 结构定义 | 表有哪些列、类型、约束、索引、关系 |
| 命名空间 | 一组数据库对象所在的逻辑空间 |

不同数据库产品里 schema 的具体含义不完全一样：

- MySQL 里，schema 常常和 database 基本等同。
- PostgreSQL 里，一个 database 下面可以有多个 schema，例如 `public`。
- SQL Server 里，schema 常作为对象命名空间，例如 `dbo`。

所以看到 schema 时，要先问：这里说的是“结构定义”，还是“命名空间”。

## 为什么重要

Schema 决定：

- 业务对象如何落表。
- 字段类型和约束如何表达业务规则。
- 表之间如何关联。
- 迁移脚本如何演进。
- 后台代码生成和 [[orm]] 如何映射数据库。

在 Directus 这类 database-first 平台里，schema 甚至直接驱动 Admin、API 和权限配置。

## 和表、列、约束的关系

```text
schema
  table
    column
    primary key
    foreign key
    constraint
    index
```

Schema 是整体结构，[[table]]、[[column]]、[[database-constraint]]、[[database-index]] 是其中的组成部分。

## 常见误区

- Schema 不只是“建表 SQL”，它表达了业务事实和长期约束。
- Schema 变化不是小事，生产数据迁移成本通常很高。
- 只看 [[orm]] 类而不看 schema，容易误判系统真实数据边界。

## 关联

- [[database-basics]]
- [[database]]
- [[orm]]
- [[table]]
- [[column]]
- [[database-constraint]]
- [[database-index]]
- [[headless-cms]]
