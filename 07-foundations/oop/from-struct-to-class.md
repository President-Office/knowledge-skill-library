---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, struct, class, object]
---

# 从结构体到类再到对象

## 核心问题

理解面向对象时，可以先从一个更朴素的问题出发：

**程序为什么需要先把数据组织成结构，再把行为放进类型，最后在运行时创建对象？**

这条路径可以帮助理解 [[struct]]、[[class]]、[[object]]、[[interface]]、[[abstract-class]] 之间的关系。

## 第一步：散落字段

最开始，程序可能只是处理一堆散落字段：

```text
name
province
score
rank
preferredMajors
```

问题是字段一多，函数签名会变长，字段归属也会变模糊。

## 第二步：结构体聚合数据

于是把相关字段聚合起来：

```text
StudentProfile
  name
  province
  score
  rank
  preferredMajors
```

这就是 [[struct]] 的思路：先承认这些字段属于同一个概念。

这一步解决的是数据组织问题。

## 第三步：函数围绕结构体工作

接下来会出现很多函数围绕这个结构体工作：

```text
calculateRank(StudentProfile)
matchMajor(StudentProfile, Major)
generatePlan(StudentProfile, SchoolList)
```

这时数据和行为已经有了稳定关系，但行为还在结构体外部。

问题是：合法状态、业务约束、状态变化规则可能散落在各个函数里。

## 第四步：类把数据和行为放到一起

[[class]] 出现后，可以把状态和行为放在同一个类型边界里：

```text
StudentProfile
  fields:
    name
    province
    score
    rank

  methods:
    updateScore()
    canApplyTo()
    buildPreferenceSnapshot()
```

这一步不是为了“看起来像面向对象”，而是为了让状态变化通过合法入口发生。

这就是 [[encapsulation]] 的基础。

## 第五步：运行时创建对象

类仍然只是描述。程序运行时，需要根据类或结构体创建具体对象：

```text
StudentProfile zhangSan = new StudentProfile(...)
StudentProfile liSi = new StudentProfile(...)
```

`StudentProfile` 是类，`zhangSan` 和 `liSi` 是两个 [[object]]。

对象通常通过这些方式产生：

| 方式 | 说明 |
| --- | --- |
| 构造函数 | 直接 new 一个对象 |
| 工厂方法 | 根据条件选择创建哪种对象 |
| [[orm]] / Mapper | 从数据库记录映射成内存对象 |
| 反序列化 | 从 JSON、消息、缓存恢复对象 |
| 依赖注入容器 | 框架启动时创建并管理对象 |

## 第六步：接口表达能力，抽象类表达骨架

当调用方不应该依赖具体类时，就需要 [[interface]]：

```text
PaymentClient
  pay()
```

当多个类有共同流程，但部分步骤不同，可以考虑 [[abstract-class]]：

```text
AbstractImportJob
  run()
  read()
  transform()
```

所以路径可以理解为：

```text
散落字段 -> 结构体 -> 围绕结构体的函数 -> 类 -> 对象 -> 接口/抽象类
```

这不是所有语言的真实历史顺序，但它是一条很好用的理解路径。

## 在 Java 后台中怎么映射

| 概念 | Java / 后台常见表现 |
| --- | --- |
| 结构体 | DTO、VO、DO、Record、只有字段的数据类 |
| 类 | Service、Entity、Domain Object、Client、Adapter |
| 对象 | 运行时的某个 DTO、Service 实例、Entity 实例 |
| 接口 | `PaymentClient`、`FileStorage`、Repository contract |
| 抽象类 | `AbstractJob`、`AbstractHandler`、模板方法父类 |

## 学习判断

- 如果一个类型只有字段，没有行为，它更像结构体或数据载体。
- 如果一个类型保护状态变化，它开始接近真正的对象。
- 如果调用方只关心能力，不关心实现，考虑接口。
- 如果多个实现共享稳定流程骨架，才考虑抽象类。
- 如果只是为了复用几行代码，不要急着继承。

## 关联

- [[struct]]
- [[class]]
- [[object]]
- [[interface]]
- [[abstract-class]]
- [[encapsulation]]
- [[abstractions]]
