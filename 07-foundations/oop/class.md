---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, class]
---

# 类

## 核心定位

类是创建对象的蓝图。它描述对象有哪些状态、能执行哪些行为、如何被构造，以及应该满足哪些约束。

一句话理解：

**类把结构体里的数据，和围绕这些数据的行为放到同一个类型边界里。**

## 类通常包含什么

| 内容 | 作用 |
| --- | --- |
| 字段 | 描述对象状态 |
| 方法 | 描述对象行为 |
| 构造方法 | 控制对象如何产生 |
| 可见性 | 控制哪些细节能被外部访问 |
| 继承 / 实现关系 | 表达和其他类型的关系 |

例如：

```text
VolunteerPlan
  fields:
    studentId
    targetProvince
    items

  methods:
    addItem()
    confirm()
    calculateRisk()
```

## 类和结构体

[[struct]] 主要组织数据，类进一步组织行为和约束。

```text
struct StudentProfile:
  score
  rank

class StudentProfile:
  score
  rank
  updateScore()
  isEligibleFor()
```

类的价值不是“更高级”，而是让数据变化必须通过合法行为发生，从而支撑 [[encapsulation]]。

## 类和对象

[[class]] 是描述，[[object]] 是运行时实例。

```text
Student 是类
张三这个学生是对象
李四这个学生也是对象
```

同一个类可以产生很多对象，每个对象有自己的状态。

## 类和接口、抽象类

类、接口、抽象类都能表达类型边界，但侧重点不同：

- [[class]] 是具体实现，通常可以产生 [[object]]。
- [[interface]] 是能力契约，让调用方依赖稳定抽象。
- [[abstract-class]] 是共同骨架，复用部分实现并约束子类。

更完整的对比见：[[interface-class-abstract-class]]。

## 常见误区

- 类不是数据库表的简单复制。
- 类不是越多越好；没有行为和约束的数据类可能只是 DTO。
- 上帝类会破坏 [[single-responsibility-principle]]，所有行为都塞进一个类反而更难维护。

## 关联

- [[struct]]
- [[object]]
- [[interface]]
- [[abstract-class]]
- [[interface-class-abstract-class]]
- [[from-struct-to-class]]
- [[encapsulation]]
