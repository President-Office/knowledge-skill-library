---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, composition, modularity]
---

# Composition 组合优于继承

## 核心定位

Composition 通过组合小而明确的能力构建更大的行为。它通常比深层继承树更容易替换、测试和演进。

## 编程时怎么判断

- 能否把变化点拆成独立策略、适配器、端口、组件或函数，再通过组合完成流程？
- 新能力是否必须修改一条脆弱的继承链？
- 组合后的依赖方向和生命周期是否仍然清晰？

组合不是把系统拆成无数小对象。每个组件仍应有清楚的职责、契约和验证方式。

## 常见误区

- 为了“组合”把简单逻辑包装成过多对象和接口。
- 只改变目录结构，没有真正隔离状态、数据和变化原因。

## 关联

- [[solid]]
- [[dependency-inversion-principle]]
- [[open-closed-principle]]
- [[module-boundary-design-principles]]
