---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, redis, cache, key-value]
---

# Redis

## 核心定位

Redis 是内存键值数据库，常用于缓存、会话、分布式锁、限流、排行榜、轻量队列和临时状态存储。它经常和关系型数据库配合，而不是替代关系型数据库。

## 适合场景

- 热点数据缓存。
- 登录 token、验证码、会话状态。
- 分布式锁、限流计数、排行榜。
- 轻量消息队列或延迟任务辅助。

## 学习重点

| 主题 | 为什么重要 |
| --- | --- |
| 数据结构 | String、Hash、List、Set、ZSet 决定建模方式 |
| 过期策略 | 缓存和临时状态必须理解 TTL |
| 缓存一致性 | 数据库和缓存之间会出现一致性问题 |
| 分布式锁 | 要理解锁超时、误删、续期和幂等 |
| 持久化 | Redis 是内存优先，但仍有持久化和恢复问题 |

## 在当前项目中观察

- [[zhijiantianya--ruoyi-vue-pro]]：token、权限、缓存、多租户辅助能力。
- [[zhijiantianya--yudao-cloud]]：微服务环境中的认证状态和缓存共享。
- [[jeecgboot--JeecgBoot]]：Shiro / JWT / Redis 会话或权限缓存。

## 不要误解

- Redis 快不代表可以随便放业务事实，核心业务事实仍应落在持久化数据库。
- 分布式锁不是解决并发问题的万能工具，业务幂等和事务边界仍然重要。

## 关联

- [[database]]
- [[mysql]]
- [[boundaries]]、[[abstractions]]

