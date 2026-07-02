---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, database, datasource]
---

# dynamic-datasource

dynamic-datasource 是 Java 后台中常见的多数据源切换组件，用于读写分离、多租户、分库或访问多个业务库。

重点要看切换边界、事务边界和默认数据源，避免在业务代码里隐式穿透数据边界。

## 关联

- [[Spring Boot]]
- [[database]]
- [[database-transaction]]
