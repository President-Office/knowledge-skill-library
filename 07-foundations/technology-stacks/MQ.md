---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, messaging, mq]
---

# MQ

MQ 是消息队列，用于在系统之间异步传递消息，解耦请求方和处理方。

在企业后台和微服务中，MQ 常用于订单、支付、通知、库存、日志、数据同步和任务削峰。

## 学习重点

- 消息是否需要顺序、事务、延迟、广播或重试。
- 消费者是否幂等，失败消息如何处理。
- MQ 和数据库事务如何协调。

## 关联

- [[RabbitMQ]]
- [[Kafka]]
- [[RocketMQ]]
- [[database-transaction]]
- [[Seata]]
