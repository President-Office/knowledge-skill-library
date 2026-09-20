---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, dry, reuse]
---

# DRY 不重复原则

## 核心定位

DRY 是 Don't Repeat Yourself。它要求同一条知识、业务规则或约束只保留一个权威表达，避免多个副本逐渐产生分歧。

## 编程时怎么判断

- 同一业务规则是否在多个服务、SQL、前端校验和脚本中分别实现？
- 修改一个规则时，是否必须手工同步多个位置？
- 重复的是稳定知识，还是只是暂时相似的代码形状？

## 常见误区

- 看到两段相似代码就立即抽象。只有变化原因和语义都稳定一致时，抽象才真的减少重复。
- 为了复用而让不相关模块共享一个巨大的工具类，结果把耦合集中起来。

DRY 要消除的是重复知识，不是所有重复字符。过早抽象会和 [[kiss]]、[[yagni]] 冲突。

## 关联

- [[solid]]
- [[single-responsibility-principle]]
- [[kiss]]
- [[yagni]]
