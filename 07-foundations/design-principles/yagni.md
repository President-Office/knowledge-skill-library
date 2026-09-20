---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, yagni, scope]
---

# YAGNI 不构建尚未需要的东西

## 核心定位

YAGNI 是 You Aren't Gonna Need It。只为明确需求、已确认的约束和真实出现的变化实现能力，不为想象中的未来预先支付复杂度。

## 编程时怎么判断

- 需求、Issue、验收标准或真实使用是否证明这个能力现在需要？
- 这层抽象是否已经有第二个真实实现或调用方？
- 省下的未来重构成本，是否确实大于现在引入的复杂度、测试和部署成本？

## 常见误区

- 用“以后可能复用”证明提前建框架、插件系统或微服务。
- 把 AI 生成文件和目录的低成本误认为系统复杂度也变低。

YAGNI 不禁止设计，只要求设计强度和已知问题的规模匹配。

## 关联

- [[kiss]]
- [[open-closed-principle]]
- [[module-boundary-design-principles]]
- [[ai-era-engineering-design-scale]]
