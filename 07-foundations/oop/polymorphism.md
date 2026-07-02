---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, polymorphism, abstraction]
---

# 多态

## 核心定位

多态是同一个抽象调用点，可以在不同场景下使用不同实现。

一句话理解：

**多态让调用方依赖稳定契约，而不是依赖具体类。**

## 和抽象的关系

[[abstractions]] 定义稳定契约，多态让这个契约可以被多个实现替换。

例如业务代码只依赖 `PaymentClient`：

```text
OrderService -> PaymentClient
                -> WeChatPayClient
                -> AliPayClient
                -> MockPaymentClient
```

`OrderService` 不需要知道具体支付渠道，只需要调用 `pay()`。

## 多态带来什么

| 价值 | 含义 |
| --- | --- |
| 可替换 | 同一个接口可以接不同实现 |
| 可扩展 | 新增实现时尽量不改调用方 |
| 可测试 | 测试时可以替换成 fake 或 mock |
| 低耦合 | 高层业务流程不直接依赖底层细节 |

## 后台项目里的例子

| 场景 | 抽象 | 多态实现 |
| --- | --- | --- |
| 支付 | `PaymentClient` | 微信、支付宝、Stripe |
| 文件存储 | `FileStorage` | 本地磁盘、OSS、S3 |
| 消息发送 | `MessageSender` | 短信、邮件、站内信 |
| 权限判断 | `PermissionService` | 不同项目的权限策略 |

## 常见误区

- 多态不只是“父类引用指向子类对象”的语法，它真正服务于依赖抽象。
- 没有真实变化点时强行做多态，只会增加认知成本。
- 多态依赖清晰契约；如果接口含糊，多个实现只会让系统更难理解。

## 关联

- [[object-oriented-abstraction]]
- [[abstractions]]
- [[encapsulation]]
- [[inheritance]]
- [[solid]]
