---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, frappe, event]
---

# DocType Event

DocType Event 是 Frappe 中围绕文档生命周期触发的事件扩展点。

它让业务逻辑可以在保存、提交、取消、删除、校验等阶段接入，但也要求开发者清楚事件顺序和事务边界。

## 学习重点

- 哪些事件属于校验、保存、提交、取消或删除阶段。
- 事件处理函数是否会修改当前文档、关联单据或账务/库存流水。
- 事件逻辑和控制器类方法如何分工。

## 关联

- [[DocType]]
- [[Frappe Framework]]
- [[Frappe App]]
- [[database-transaction]]
