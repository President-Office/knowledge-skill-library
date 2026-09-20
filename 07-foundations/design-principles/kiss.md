---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, kiss, simplicity]
---

# KISS 保持简单

## 核心定位

KISS 是 Keep It Simple。设计应采用能够满足已验证目标的最简单方案，让行为、边界和故障原因容易被人和 Agent 理解。

## 编程时怎么判断

- 这个抽象、依赖、异步链路或配置项是否解决了已经出现的问题？
- 新成员能否从入口追踪到核心行为？
- 是否可以先用更少的模块、更少的状态和更少的运行时组件完成目标？

简单不等于草率。安全、数据一致性、可观测性和测试边界不能为了少写代码而删除。

## 常见误区

- 把“代码少”误认为简单，忽略隐藏状态、隐式约定和难以验证的魔法行为。
- 把未来可能需要的扩展提前做成框架，增加当前用户和维护者的认知成本。

## 关联

- [[yagni]]
- [[module-boundary-design-principles]]
- [[separation-of-concerns]]
