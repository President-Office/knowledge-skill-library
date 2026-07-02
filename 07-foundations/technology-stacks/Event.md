---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, event, architecture]
---

# Event

Event 是系统中已经发生的事实，例如订单已支付、库存已扣减、用户已注册。

事件可以在单体内用于模块解耦，也可以通过 MQ 在微服务之间传播。

## 学习重点

- 事件表达的是事实，还是伪装成事件的命令。
- 事件是否有明确 schema、版本和幂等键。
- 事件发布和数据库事务如何保持一致。

## 关联

- [[MQ]]
- [[RabbitMQ]]
- [[Kafka]]
- [[RocketMQ]]
- [[module-boundary-design-principles]]
