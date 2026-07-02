---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, table, data-modeling]
---

# 表

## 核心定位

表是关系型数据库中保存同一类业务事实的集合。

一句话理解：

**表回答“这一类东西如何被长期保存”。**

例如：

```text
school
major
admission_score
student_profile
volunteer_plan
```

这些表分别保存院校、专业、录取分数、学生画像、志愿方案等业务事实。

## 表包含什么

| 组成                    | 说明   |           |
| --------------------- | ---- | --------- |
| [[column]]  | 这类数据有哪些字段 |
| [[row]]  | 一条具体记录    |
| [[primary-key]] | 每行数据的唯一标识 |
| [[foreign-key]] | 和其他表的关系   |
| [[database-constraint]] | 数据合法性规则   |
| [[database-index]] | 查询加速结构    |

## 表设计要问什么

- 这张表表达的是一个真实业务概念，还是临时展示结果？
- 每一行代表什么？
- 哪些字段必须有？
- 哪些字段应该唯一？
- 是否需要租户字段、删除字段、审计字段？
- 是否需要保留历史记录或流水？

## 和类、对象的关系

表和 [[class]] 经常可以互相映射，但不能简单等同。

| 数据库 | 代码 |
| --- | --- |
| 表 | Entity / DO / Model |
| 行 | 一个对象或记录 |
| 列 | 字段 |

[[orm]] 可以做映射，但数据库表更关注长期存储和约束，类还可能承载行为和 [[encapsulation]]。

## 常见误区

- 表不是 Excel 工作表，它承担长期一致性和约束。
- 一张表不要同时表达多个变化原因，否则会影响 [[single-responsibility-principle]]。
- 为页面展示而临时拼出来的结果，不一定应该成为长期业务表。

## 关联

- [[database-basics]]
- [[orm]]
- [[schema]]
- [[column]]
- [[row]]
- [[primary-key]]
- [[foreign-key]]
- [[database]]
