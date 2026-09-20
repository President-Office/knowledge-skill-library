---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, separation-of-concerns, boundaries]
---

# Separation of Concerns 关注点分离

## 核心定位

关注点分离要求把不同变化原因、不同运行边界、不同权限边界和不同数据责任分开表达，让每个部分可以独立理解、测试和演进。

## 编程时怎么判断

- Controller、Service、Repository、UI、权限和基础设施是否混在同一段逻辑里？
- 安全规则、业务规则、展示格式和持久化细节是否互相泄漏？
- 一个变化是否会因为共享隐式状态而波及不相关模块？

分离不等于机械套分层模板。边界应该由变化原因、数据 ownership、部署方式和测试需求驱动。

## 常见误区

- 只拆目录，不拆依赖、状态和责任。
- 为了形式上的层数引入空壳 Facade、Service 或 Manager。

## 关联

- [[single-responsibility-principle]]
- [[module-boundary-design-principles]]
- [[boundaries]]
- [[abstractions]]
