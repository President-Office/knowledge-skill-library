---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, orm, persistence, data-access]
aliases: [Object Relational Mapping, 对象关系映射]
---

# ORM

## 核心定位

ORM 是 Object Relational Mapping，对象关系映射。它把程序里的对象、类、字段和数据库里的表、列、行之间建立映射关系。

一句话理解：

**ORM 让业务代码用对象操作数据，但最终仍然要落到 SQL、表结构和事务上。**

例如：

```text
class StudentProfile
  id
  score
  rank

student_profile 表
  id
  score
  rank
```

ORM 负责在两者之间转换。

## ORM 解决什么

| 问题 | ORM 提供的帮助 |
| --- | --- |
| 对象和表如何对应 | 类映射表，字段映射列 |
| 查询如何组织 | 方法、查询构造器、注解、XML 或 DSL |
| 数据如何保存 | 把对象变化转换成 `insert`、`update`、`delete` |
| 关系如何加载 | 一对一、一对多、多对多关联映射 |
| 跨数据库差异如何隔离 | 方言、分页、类型映射、生成 SQL |

ORM 的价值是减少重复数据访问代码，让开发者更专注业务对象和数据访问意图。

## ORM 不是什么

ORM 不是数据库设计的替代品。

它不能替你决定：

- 哪些业务事实应该成为 [[table]]。
- 哪些字段应该成为 [[column]]。
- 哪些字段必须唯一、非空或受 [[database-constraint]] 保护。
- 哪些查询需要 [[database-index]]。
- 哪些操作必须放在 [[database-transaction]] 里。

ORM 只是映射层。底层的 [[schema]]、[[sql]]、索引、事务和数据库方言仍然存在。

## 常见 ORM / Mapper 风格

| 风格 | 典型技术 | 特点 |
| --- | --- | --- |
| Active Record | Rails ActiveRecord、部分 Django Model | 对象自己负责保存和查询 |
| Data Mapper | Hibernate、JPA、MyBatis、SQLAlchemy | 对象和持久化逻辑相对分离 |
| SQL Mapper | MyBatis | SQL 可见，映射结果到对象 |
| Query Builder | Prisma、TypeORM、Knex、部分 GORM 用法 | 用代码构造查询 |
| Metadata-driven | Frappe DocType、Directus metadata | 元数据同时驱动表、表单、API 或权限 |

不同框架的抽象强度不同。MyBatis 更接近 SQL Mapper，JPA/Hibernate 更强调对象关系映射，GORM/Prisma 更偏向模型和查询构造。

## ORM 和 SQL 的关系

ORM 可能隐藏 SQL，但不会消灭 SQL。

```text
业务代码 -> ORM / Mapper -> SQL -> 数据库
```

所以读后台项目时要同时看：

- Entity / Model / DO 如何定义。
- Mapper / Repository 如何查询。
- 生成或手写的 SQL 是什么。
- 查询条件是否匹配索引。
- 事务边界在哪里。

如果只看 ORM 类，不看 SQL 和 schema，容易误判系统真实的数据边界。

## 常见风险

| 风险 | 说明 |
| --- | --- |
| N+1 查询 | 查列表后逐条加载关联对象，导致查询次数暴涨 |
| 隐式 SQL | 代码看起来简单，实际生成复杂 SQL |
| 过度关联加载 | 一次加载太多对象，造成性能和内存问题 |
| 方言差异 | 多数据库支持时，分页、函数、类型、锁语义可能不同 |
| 贫血模型 | ORM 对象只剩字段，业务规则散落到 Service 或 Controller |
| 数据库约束缺失 | 只靠代码校验，绕过应用后数据可能损坏 |

ORM 最危险的地方不是“慢”，而是让人误以为自己不需要理解数据库。

## 在开源项目中怎么观察

| 项目 | 观察点 |
| --- | --- |
| [[zhijiantianya--ruoyi-vue-pro]] | MyBatis Plus 的 DO、Mapper、Service 和代码生成边界 |
| [[zhijiantianya--yudao-cloud]] | 多模块 Mapper、跨服务数据边界和数据库方言适配 |
| [[flipped-aurora--gin-vue-admin]] | GORM model、service、repository 的组织方式 |
| [[frappe--erpnext]] | DocType 如何同时表达数据模型、表单和业务入口 |
| [[payloadcms--payload]] | collection 配置如何映射到 PostgreSQL、MongoDB 等适配器 |
| [[directus--directus]] | 数据库 schema 和 metadata 如何驱动 API 与 Admin |

## 使用原则

- 先理解 [[database]] 和 [[schema]]，再理解 ORM。
- ORM 生成的 SQL 也要能解释。
- 重要业务查询要看执行计划，而不是只看方法名。
- 事务边界应该落在业务流程上，而不是随意落在单个 Mapper 调用上。
- 数据合法性不能只依赖 ORM 校验，关键约束应该进入数据库。
- 对外部接口、支付、权限、报表等高风险场景，要保留输入输出和 SQL 证据。

## 关联

- [[database]]
- [[sql]]
- [[schema]]
- [[table]]
- [[column]]
- [[row]]
- [[database-index]]
- [[database-transaction]]
- [[object]]
- [[class]]
- [[abstractions]]
- [[mathematical-modeling]]
