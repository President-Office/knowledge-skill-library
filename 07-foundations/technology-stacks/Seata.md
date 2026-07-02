---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, distributed-transaction]
---

# Seata

Seata 是分布式事务组件，用于微服务之间需要跨服务保持一致性的场景。

它不是默认应该使用的能力。优先判断业务能否通过本地事务、事件、补偿、幂等和最终一致性解决。

## 关联

- [[Spring Cloud Alibaba]]
- [[database-transaction]]
- [[oltp]]
