---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, interface, abstraction]
---

# 接口

## 核心定位

接口表达一组稳定能力契约，告诉调用方“你可以依赖什么”，而不是告诉调用方“具体怎么做”。

一句话理解：

**接口是能力承诺，不是实现细节。**

例如：

```text
PaymentClient
  pay()
  refund()
  query()
```

调用方依赖 `PaymentClient`，具体实现可以是微信支付、支付宝、Stripe 或测试替身。

## 接口解决什么

接口主要解决依赖方向和替换问题：

- 高层业务可以依赖接口，而不是依赖具体 SDK。
- 多个实现可以遵守同一契约。
- 测试时可以替换成 mock / fake。
- 新增实现时尽量少改调用方。

这和 [[dependency-inversion-principle]]、[[polymorphism]] 关系很近。

## 接口不应该是什么

接口不应该只是为了“看起来解耦”而存在。

坏信号：

- 系统永远只有一个实现，也没有测试替换价值。
- 接口方法太多，调用方被迫依赖不用的能力。
- 实现类经常抛“不支持该操作”。
- 接口名称只是实现类名称前面加一个 `I`。

这时需要检查 [[interface-segregation-principle]] 和 [[liskov-substitution-principle]]。

## 接口和类、抽象类

接口、类和抽象类不是同一条“高级程度”阶梯，而是三种不同建模工具。

- [[interface]] 关注能力契约。
- [[class]] 关注具体状态、行为和构造规则。
- [[abstract-class]] 关注共同流程骨架和部分通用实现。

更完整的对比见：[[interface-class-abstract-class]]。

## 后台项目里的例子

| 场景 | 接口 |
| --- | --- |
| 支付 | `PaymentClient` |
| 文件存储 | `FileStorage` |
| 消息发送 | `MessageSender` |
| 权限判断 | `PermissionService` |
| 数据访问 | Repository / Mapper contract |

## 关联

- [[abstractions]]
- [[class]]
- [[abstract-class]]
- [[interface-class-abstract-class]]
- [[polymorphism]]
- [[dependency-inversion-principle]]
- [[interface-segregation-principle]]
- [[lsp-vs-dip]]
