---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, abstraction, encapsulation, inheritance, polymorphism]
---

# 封装、继承、多态和抽象

## 核心关系

抽象是目标，封装、继承、多态是面向对象里常见的实现手段。

一句话理解：

**抽象决定“外部应该依赖什么稳定概念”，封装隐藏细节，继承表达类型关系，多态让同一个抽象可以有多个实现。**

## 四个概念分别解决什么

| 概念 | 解决的问题 | 和抽象的关系 |
| --- | --- | --- |
| 抽象 | 从具体实现中提炼稳定概念 | 定义调用方应该依赖的角色、能力或契约 |
| [[encapsulation]] | 隐藏内部状态和实现细节 | 让抽象背后的变化不影响调用方 |
| [[inheritance]] | 表达“是一种”的类型关系，复用或扩展行为 | 可以承载抽象层级，但不是抽象的必要条件 |
| [[polymorphism]] | 同一个调用点可以使用不同实现 | 让调用方依赖抽象，而不是依赖具体类 |

## 基本构件

在理解封装、继承、多态之前，可以先理解面向对象的几个基本构件：

| 概念 | 解决的问题 |
| --- | --- |
| [[struct]] | 把相关字段组织在一起 |
| [[class]] | 把数据、行为和约束放进同一个类型边界 |
| [[object]] | 运行时真正产生的具体实例 |
| [[interface]] | 表达稳定能力契约 |
| [[abstract-class]] | 表达共同骨架和部分通用实现 |

更完整的理解路径见：[[from-struct-to-class]]。  
接口、类和抽象类的职责边界见：[[interface-class-abstract-class]]。

## 封装和抽象

详见：[[encapsulation]]。

封装强调把内部细节藏起来，只暴露稳定入口。

例如支付能力可以暴露一个 `pay()` 方法，调用方不需要知道底层是微信支付、支付宝、Stripe，还是银行转账。

封装对抽象的价值是：

- 隐藏内部状态，避免调用方直接修改不该修改的数据。
- 隐藏实现细节，让底层存储、第三方接口、缓存策略可以变化。
- 保护业务不变量，例如订单金额、库存数量、账户余额不能被随意改坏。

封装不是简单地把字段改成 `private`。真正有价值的封装，是把“哪些操作合法”表达出来。

## 继承和抽象

详见：[[inheritance]]。

继承可以用来表达抽象层级，例如：

```text
PaymentClient
  -> WeChatPayClient
  -> AliPayClient
```

但继承不是抽象的同义词。很多好的抽象并不依赖继承，而是依赖接口、组合、函数参数、模块边界或协议。

继承适合表达稳定的“是一种”关系；如果只是为了复用几行代码，继承往往会制造耦合。

判断继承是否合理，可以问三个问题：

- 子类是否真的可以替代父类？
- 父类变化时，子类是否会被意外影响？
- 调用方关心的是父类的稳定契约，还是某个子类的特殊细节？

这里和 [[solid]] 的 [[liskov-substitution-principle]]、[[open-closed-principle]]、[[dependency-inversion-principle]] 都有关：子类要能替代父类，扩展不应该频繁修改旧代码，高层策略应该依赖抽象。

## 多态和抽象

详见：[[polymorphism]]。

多态是抽象在运行时发挥作用的关键。

如果业务代码只依赖 `PaymentClient`，那么同一个 `pay()` 调用可以在不同环境下使用不同实现：

```text
OrderService -> PaymentClient
                -> WeChatPayClient
                -> AliPayClient
                -> MockPaymentClient
```

这意味着：

- 业务流程不需要知道具体支付渠道。
- 新增支付渠道时，尽量新增实现，而不是改订单流程。
- 测试时可以替换成 fake 或 mock 实现。

多态的重点不是“用了父类引用指向子类对象”这个语法，而是让调用方只依赖稳定契约。

## 在后台项目中怎么理解

| 场景 | 抽象 | 封装 | 多态 |
| --- | --- | --- | --- |
| 支付 | `PaymentClient` | 隐藏签名、回调、渠道参数 | 微信、支付宝、Stripe 不同实现 |
| 文件存储 | `FileStorage` | 隐藏本地磁盘、OSS、S3 细节 | 不同存储服务可替换 |
| 消息发送 | `MessageSender` | 隐藏短信、邮件、站内信渠道差异 | 不同渠道实现同一发送契约 |
| 权限判断 | `PermissionService` | 隐藏角色、菜单、租户、数据权限规则 | 不同项目可替换权限策略 |

继承在这些场景里不一定出现。很多时候，用接口加组合，比用父类继承更清楚。

## 常见误区

- 把抽象等同于继承：继承只是手段，抽象也可以由接口、协议、模块边界表达。
- 把封装等同于 getter/setter：如果所有字段都能直接读写，封装没有保护业务规则。
- 为了多态强行抽接口：没有真实变化点时，接口只会增加认知成本。
- 过早设计继承树：业务模型还不稳定时，继承层级越深，修改越困难。

## 关联

- [[abstractions]]
- [[from-struct-to-class]]
- [[struct]]
- [[class]]
- [[object]]
- [[interface]]
- [[abstract-class]]
- [[interface-class-abstract-class]]
- [[encapsulation]]
- [[inheritance]]
- [[polymorphism]]
- [[boundaries]]
- [[solid]]
- [[architecture-as-wedge]]
