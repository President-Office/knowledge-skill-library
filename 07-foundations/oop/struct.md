---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, struct, data-modeling]
---

# 结构体

## 核心定位

结构体是把一组相关字段组织在一起的数据结构。

一句话理解：

**结构体先解决“这些数据属于同一个东西”的问题。**

例如一个学生可以先被表达成一组字段：

```text
Student
  id
  name
  province
  score
  rank
```

这时重点还不是行为，而是数据聚合。

## 结构体解决什么

没有结构体时，代码里可能到处传散落字段：

```text
name, province, score, rank
```

有结构体后，可以把它们作为一个整体传递：

```text
StudentProfile
```

它带来的价值是：

- 字段归属更清楚。
- 函数参数更少。
- 数据模型更容易复用。
- 后续可以继续演化出行为和约束。

## 和类的关系

[[class]] 可以看作结构体的进一步演化：不只把字段放在一起，还把操作这些字段的行为、约束和构造方式也放在一起。

```text
结构体：数据放在一起
类：数据 + 行为 + 约束 放在一起
```

所以理解面向对象时，可以先从结构体开始：先看数据怎么聚合，再看行为如何靠近数据。

## 和对象的关系

结构体本身通常是类型描述或内存布局。程序运行时，按这个结构创建出来的具体数据，就是一个具体值或 [[object]]。

例如：

```text
StudentProfile 是结构
张三的 StudentProfile 是一个具体对象/值
```

## 在后台项目中怎么观察

| 场景 | 类似结构体的表现 |
| --- | --- |
| DO / Entity | 数据库表的一行数据 |
| DTO | 接口入参或出参的数据结构 |
| VO | 页面展示需要的数据结构 |
| Record / Value Object | 一组不可变或有业务含义的字段 |

## 关联

- [[from-struct-to-class]]
- [[class]]
- [[object]]
- [[encapsulation]]
- [[database]]
