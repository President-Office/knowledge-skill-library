---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [solid, dip, design-principles]
---

# DIP 依赖倒置原则

## 核心定位

DIP 是 Dependency Inversion Principle，通常译为“依赖倒置原则”。

一句话理解：

**高层策略不应该依赖低层细节，二者都应该依赖抽象。**

这里的高层策略通常是业务规则、业务流程、领域服务；低层细节通常是数据库、缓存、消息队列、第三方 SDK、文件系统、HTTP 客户端。

## 它解决什么问题

如果业务逻辑直接依赖基础设施细节，会出现这些问题：

- 换数据库、支付渠道、短信服务时要改业务流程。
- 单元测试必须启动真实数据库、缓存或第三方服务。
- 基础设施异常语义渗透到核心业务。
- 业务代码越来越像 glue code，真正规则被淹没。

DIP 追问的是：核心业务依赖的是稳定能力，还是某个具体实现？

## 后台项目里的判断

| 场景 | 更符合 DIP 的做法 |
| --- | --- |
| 支付 | 订单服务依赖 `PaymentClient`，不直接依赖微信支付 SDK |
| 存储 | 业务服务依赖 `FileStorage`，不直接依赖 OSS 客户端 |
| 消息 | 业务服务依赖消息发送抽象，不直接绑定 RabbitMQ、Kafka 或 Redis Stream |
| 数据访问 | 业务流程通过 Repository / Mapper 边界访问数据 |
| 第三方接口 | 通过 Adapter 隔离签名、重试、异常和返回结构 |

## 和抽象、多态的关系

[[abstractions]] 定义稳定契约，[[polymorphism]] 让不同实现可以替换，DIP 则规定依赖方向：高层业务依赖抽象，不依赖具体细节。

这也是 [[open-closed-principle]] 能成立的重要基础。

## 和 LSP 的关系

[[dependency-inversion-principle]] 让高层业务依赖抽象，[[liskov-substitution-principle]] 保证这些抽象的具体实现真的可以替换。

更完整的对比见：[[lsp-vs-dip]]。

## 常见误区

- DIP 不是每个类都要配一个 interface。
- 依赖倒置不是为了形式高级，而是为了保护核心业务。
- 如果抽象只包装了一个不变实现，而且没有测试或替换价值，可能只是多了一层噪音。
- 依赖注入是实现 DIP 的常见方式，但 DIP 不等于依赖注入框架。

## 关联

- [[solid]]
- [[lsp-vs-dip]]
- [[abstractions]]
- [[polymorphism]]
- [[open-closed-principle]]
- [[interface-segregation-principle]]
