---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, column, data-modeling]
---

# 列

## 核心定位

列是表中某个字段的定义，包括字段名、类型、是否允许为空、默认值和约束。

一句话理解：

**列回答“一条记录有哪些属性，以及这些属性必须满足什么规则”。**

## 列包含的设计信息

| 信息 | 例子 | 关注点 |
| --- | --- | --- |
| 字段名 | `school_name` | 是否表达业务含义 |
| 类型 | `varchar`、`int`、`decimal`、`datetime` | 是否能准确保存数据 |
| 是否为空 | `not null` | 业务上是否必填 |
| 默认值 | `0`、`CURRENT_TIMESTAMP` | 是否有合理初始状态 |
| 约束 | unique、check、foreign key | 是否阻止非法数据 |

## 类型为什么重要

字段类型不是技术细节，它会影响业务含义：

- 分数应该用整数还是小数？
- 金额是否要避免浮点误差？
- 时间是本地时间还是 UTC？
- 状态应该用字符串、数字枚举，还是单独字典表？
- JSON 字段是合理弹性，还是逃避建模？

## 和代码字段的关系

数据库列通常会映射到代码里的字段：

```text
column: school_name
field: schoolName
```

但代码字段可以更灵活，数据库列更强调长期稳定、可迁移和可查询。

## 常见误区

- 不要所有字段都用字符串，类型会丢失业务约束。
- 不要随意允许 `null`，否则业务语义会变复杂。
- 不要把所有不确定结构都塞进 JSON，除非明确知道查询和演进代价。

## 关联

- [[database-basics]]
- [[table]]
- [[row]]
- [[database-constraint]]
- [[schema]]
