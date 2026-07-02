---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, interface, class, abstract-class, abstraction]
---

# 接口、类和抽象类

## 核心问题

接口、类和抽象类都在表达“类型”，但它们解决的问题不同：

- [[class]] 解决“对象有什么状态、行为和构造规则”。
- [[interface]] 解决“调用方可以依赖什么能力契约”。
- [[abstract-class]] 解决“多个子类共享什么流程骨架和通用实现”。

一句话理解：

**类负责生成对象，接口负责稳定依赖，抽象类负责复用共同骨架。**

## 三者关系

| 概念 | 核心定位 | 是否能直接创建对象 | 主要表达什么 | 典型用途 |
| --- | --- | --- | --- | --- |
| [[class]] | 完整类型实现 | 通常可以 | 状态、行为、构造规则、不变量 | 具体业务对象、服务实现、DTO |
| [[interface]] | 能力契约 | 不可以 | 调用方可依赖的方法集合 | 支付、存储、消息、权限等可替换能力 |
| [[abstract-class]] | 契约 + 部分实现 | 不可以完整实例化 | 共同流程、共享状态、可复用步骤 | 导入任务、模板流程、框架扩展点 |

接口和抽象类都可以参与 [[polymorphism]]，但它们的重心不同：

- 接口让调用方只关心“能做什么”。
- 抽象类让子类继承“共同怎么做的一部分”。
- 类最终提供可运行的具体实现和运行时对象。

## 如何选择

优先问三个问题：

| 问题 | 更可能选择 |
| --- | --- |
| 我需要创建一个承载状态和行为的具体业务类型吗？ | [[class]] |
| 我需要让业务依赖稳定能力，并允许多个实现替换吗？ | [[interface]] |
| 我已经确认多个实现有稳定共同流程或共享状态吗？ | [[abstract-class]] |

一个保守顺序是：

1. 先用普通类把业务行为表达清楚。
2. 当调用方需要替换实现、测试替身或跨基础设施适配时，抽出接口。
3. 当多个实现真的共享稳定流程骨架时，再考虑抽象类。

## 后台项目例子

| 场景 | 更适合的表达 |
| --- | --- |
| 志愿方案 `VolunteerPlan`，包含院校专业组、风险计算、确认状态 | [[class]] |
| 支付客户端 `PaymentClient`，支持微信、支付宝、Stripe 多实现 | [[interface]] |
| 数据导入任务 `AbstractImportJob`，统一校验、读取、转换、保存流程 | [[abstract-class]] |
| 文件存储 `FileStorage`，本地、OSS、S3 可替换 | [[interface]] |
| 批处理任务有固定 `run()` 流程，但每个任务实现不同步骤 | [[abstract-class]] |

## 和 SOLID 的关系

- [[single-responsibility-principle]] 关注一个类型或模块是否只有一个主要变化原因。
- [[interface-segregation-principle]] 约束接口不要过大，不要强迫调用方依赖不用的方法。
- [[liskov-substitution-principle]] 要求子类或实现类能够可靠替代抽象类型。
- [[dependency-inversion-principle]] 鼓励高层业务依赖接口等稳定抽象，而不是依赖具体实现。

接口、类、抽象类不是“越抽象越好”的递进关系，而是不同建模工具。真正的判断标准是变化点在哪里、调用方应该依赖什么、共同逻辑是否已经稳定。

## 常见误区

- 把接口当成所有类的必备配套：没有替换价值时，接口会增加认知成本。
- 把抽象类当成更高级的接口：抽象类绑定继承关系，也继承继承的风险。
- 把类当成数据库表复制品：类应该表达行为和约束，不只是字段集合。
- 为了复用几行代码建立抽象父类：组合或私有 helper 往往更简单。
- 在接口里塞太多方法：这会破坏 [[interface-segregation-principle]]，也会让实现类难以满足 [[liskov-substitution-principle]]。

## 关联

- [[object-oriented-abstraction]]
- [[from-struct-to-class]]
- [[class]]
- [[interface]]
- [[abstract-class]]
- [[encapsulation]]
- [[inheritance]]
- [[polymorphism]]
- [[solid]]
