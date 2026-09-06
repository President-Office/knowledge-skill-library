---
type: source-reading
status: initial
project: frappe/erpnext
topic: Hooks 与事件
created: 2026-07-02
updated: 2026-07-02
---

# ERPNext - Hooks 与事件

项目主卡：[[frappe--erpnext]]

## 核心关系

ERPNext 通过 Frappe 的 hooks、[[DocType Event]]、[[Scheduler Event]]、fixtures 和 patches 接入运行时。它的扩展点比传统 Controller 更靠近业务对象生命周期。

## 关联源码入口

- `erpnext/hooks.py`
- `erpnext/patches.txt`
- `erpnext/patches`

## 关联概念

- [[Frappe App]]
- [[DocType Event]]
- [[Scheduler Event]]
- [[fixtures]]
- [[patches]]
