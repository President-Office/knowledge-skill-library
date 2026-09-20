---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, measure-first, observability]
---

# Measure First 先度量再优化

## 核心定位

Measure First 要求先定义目标、建立基线和收集证据，再决定是否优化、重构或引入复杂基础设施。

## 编程时怎么判断

- 优化解决的是已观测的瓶颈，还是想象中的问题？
- 是否有可重复的指标、样本、测试或基准来比较改动前后？
- 是否同时观察正确性、延迟、吞吐、成本、资源、错误率和安全影响？

度量不是为了给每一行代码加监控，而是让重要决策有证据。没有基线时，先补最小可用的观测和验证。

## 常见误区

- 先引入缓存、并发、分布式组件，再寻找它们是否真的必要。
- 只看平均值，忽略尾延迟、失败率、资源成本和用户体验。

## 关联

- [[fail-fast]]
- [[yagni]]
- [[ai-era-engineering-design-scale]]
