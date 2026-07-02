---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [solid, design-principles, oop]
---

# SOLID

## 核心定位

SOLID 不是背诵用的五个缩写，而是一组判断代码是否容易变化、测试和组合的工具。它适合在读开源项目时追问：这个模块为什么这样分？这个接口为什么这样抽？这个依赖方向是否合理？

## 五个原则

| 原则 | 中文理解 | 阅读源码时看什么 |
| --- | --- | --- |
| [[single-responsibility-principle]] | 一个模块应该只有一个主要变化原因 | Controller 是否只处理输入输出，Service 是否混入太多职责 |
| [[open-closed-principle]] | 对扩展开放，对修改关闭 | 新增支付渠道、存储适配、插件时是否少改旧代码 |
| [[liskov-substitution-principle]] | 子类型能替换父类型而不破坏行为 | 多数据库适配、多存储适配是否遵守共同契约 |
| [[interface-segregation-principle]] | 接口不应该强迫调用方依赖不用的方法 | API、Service、SDK 是否拆出更小能力面 |
| [[dependency-inversion-principle]] | 高层策略不依赖低层细节，依赖抽象 | 业务逻辑是否直接绑定具体数据库、消息队列、第三方 SDK |

## 和架构的关系

架构层面的很多问题，其实是 SOLID 在更大尺度上的表现：

- 单一职责：一个服务、一个模块、一个 package 是否有清晰职责。
- 开闭原则：插件、适配器、代码生成模板能否扩展。
- 依赖倒置：业务模块是否依赖基础设施细节。
- 接口隔离：SDK、API、模块间契约是否过大。

## 在当前项目中怎么观察

| 项目 | 观察点 |
| --- | --- |
| [[zhijiantianya--ruoyi-vue-pro]] | Controller / Service / Mapper / VO 分层是否清楚，框架层和业务层是否分离 |
| [[zhijiantianya--yudao-cloud]] | 服务拆分是否只是技术拆分，还是对应稳定业务边界 |
| [[flipped-aurora--gin-vue-admin]] | Gin 路由、Service、Model、Middleware 的职责是否清楚 |
| [[payloadcms--payload]] | 数据库适配器和插件是否通过抽象契约扩展 |
| [[directus--directus]] | API、Admin、SDK、metadata 是否各自承担稳定职责 |

## 常见误区

- SOLID 不是要求把所有东西拆碎。
- 抽象不是越多越好，只有当变化方向清楚时抽象才有价值。
- 依赖倒置不是为了“看起来高级”，而是为了让核心业务不被基础设施绑死。

## 关联

- [[boundaries]]
- [[abstractions]]
- [[single-responsibility-principle]]
- [[open-closed-principle]]
- [[liskov-substitution-principle]]
- [[interface-segregation-principle]]
- [[dependency-inversion-principle]]
- [[lsp-vs-dip]]
- [[architecture-as-wedge]]
- [[03-patterns/framework-characteristics/README]]
