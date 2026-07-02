---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, row, record]
---

# 行

## 核心定位

行是表中的一条具体记录。

一句话理解：

**行回答“某一个具体业务事实是什么”。**

例如 `school` 表中一行可以代表一所具体院校，`admission_score` 表中一行可以代表某年某省某院校某专业的一条录取数据。

## 行和对象的关系

后台系统里，一行数据经常会被映射成一个 [[object]]：

```text
数据库行 -> DO / Entity -> Java 对象
```

但二者不完全等同：

- 行是持久化记录。
- 对象是运行时实例。
- 对象可能包含行为，行通常只保存状态。

## 一行应该代表什么

设计表时要明确每一行的业务含义：

| 表 | 一行代表什么 |
| --- | --- |
| `school` | 一所院校 |
| `major` | 一个专业 |
| `admission_score` | 一条录取分数记录 |
| `volunteer_plan` | 一个志愿方案 |
| `volunteer_plan_item` | 志愿方案中的一个志愿项 |

如果说不清“一行代表什么”，这张表通常还没有建模清楚。

## 常见误区

- 一行不要混合多个业务事实。
- 不要把可重复明细硬塞进一行的多个字段里，例如 `major1`、`major2`、`major3`。
- 不要只为了页面展示方便设计行结构，长期业务事实更重要。

## 关联

- [[database-basics]]
- [[table]]
- [[column]]
- [[primary-key]]
- [[object]]
