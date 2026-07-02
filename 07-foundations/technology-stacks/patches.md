---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, migration, frappe]
---

# patches

patches 是版本升级时执行的数据或结构迁移脚本。

它们解决“代码已经变了，历史数据也要跟着调整”的问题，是成熟业务系统长期演进时不可缺少的机制。

## 学习重点

- patch 是否可重复执行，失败后如何恢复。
- patch 修改 schema、配置、历史数据还是权限。
- patch 和数据库迁移工具、业务版本发布流程如何配合。

## 关联

- [[database-transaction]]
- [[schema]]
- [[Frappe App]]
- [[fixtures]]
