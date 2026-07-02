---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, scheduler, frappe]
---

# Scheduler Event

Scheduler Event 是定时触发的任务事件，用来处理周期性任务、异步补偿、数据同步、提醒和统计。

在后台框架中，定时任务需要重点关注幂等性、失败重试、并发控制和业务数据一致性。

## 学习重点

- 定时任务由框架调度、操作系统调度，还是独立任务平台调度。
- 任务是否幂等，失败后能否重跑。
- 任务执行是否影响权限、租户和审计。

## 关联

- [[XXL-Job]]
- [[Frappe Framework]]
- [[database-transaction]]
- [[工作流]]
