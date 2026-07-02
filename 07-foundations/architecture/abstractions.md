---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [architecture, abstraction]
---

# 抽象

## 核心问题

抽象的目的不是把代码写得更复杂，而是让变化被限制在合理范围内。

抽象要回答的是：**调用方应该依赖什么稳定概念，而不是依赖哪些易变细节。**

## 什么是好的抽象

好的抽象通常满足三个条件：

- 隐藏细节：调用方不需要知道底层数据库、对象存储、支付渠道的具体实现。
- 表达稳定概念：抽象的是长期存在的业务或技术角色，而不是临时需求。
- 限制变化：新增实现时少改旧代码。

## 常见抽象

| 抽象类型                 | 隐藏什么         | 典型例子                          |
| -------------------- | ------------ | ----------------------------- |
| Repository / Mapper  | 数据库访问细节      | MyBatis Mapper、ORM Repository |
| Service              | 业务流程和业务规则    | 订单创建、支付发起、库存扣减                |
| Adapter              | 外部系统差异       | 支付渠道、短信服务、对象存储                |
| Interface / Contract | 依赖方和实现方的约定   | Java interface、OpenAPI、SDK    |
| Plugin               | 可扩展点和宿主系统的边界 | Payload 插件、Directus extension |

## 和面向对象的关系

[[struct]]、[[class]]、[[object]]、[[interface]]、[[abstract-class]] 是理解面向对象的基础构件。

[[encapsulation]]、[[inheritance]]、[[polymorphism]] 是面向对象里表达抽象的常见机制，但它们不是抽象本身。

更完整的关系见：[[object-oriented-abstraction]]。

## 坏抽象的信号

- 只为了“看起来高级”而引入接口，但系统只有一个实现且没有变化点。
- 抽象名称没有业务含义，只是把原方法包装了一层。
- 抽象泄漏细节，调用方仍然需要知道底层数据库、缓存、第三方 API 的特殊规则。
- 抽象层太早固定，导致真实需求出现时反而更难修改。

## 在项目中怎么观察

| 项目                              | 抽象观察点           |                                              |
| ------------------------------- | --------------- | -------------------------------------------- |
| [[zhijiantianya--ruoyi-vue-pro]]   | 框架层如何把 Redis、消息、权限、租户等能力封装给业务模块              |
| [[flipped-aurora--gin-vue-admin]] | Go 项目中 service、repository、middleware 的职责是否清楚 |
| [[payloadcms--payload]]       | collection、plugin、adapter 如何形成扩展点            |
| [[directus--directus]]      | metadata、service、extension 如何隐藏数据库和 API 细节   |
| [[frappe--erpnext]]       | DocType 是否既是数据模型，也是业务操作的抽象入口                 |

## 和边界的关系

[[boundaries]] 决定什么应该隔离，抽象决定隔离之后如何交互。

没有边界的抽象容易变成空壳；没有抽象的边界容易变成硬隔离，复用和演进成本都会变高。

## 关联

- [[ai-era-engineering-design-scale]]
- [[boundaries]]
- [[object-oriented-abstraction]]
- [[from-struct-to-class]]
- [[solid]]
- [[monorepo]]
- [[database]]
- [[orm]]
- [[mathematical-modeling]]
- [[architecture-as-wedge]]
