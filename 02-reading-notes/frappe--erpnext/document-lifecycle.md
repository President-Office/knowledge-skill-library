---
type: source-reading
status: initial
project: frappe/erpnext
topic: 单据生命周期
created: 2026-07-02
updated: 2026-07-02
---

# ERPNext - 单据生命周期

项目主卡：[[frappe--erpnext]]

## 核心关系

ERPNext 的业务单据通常围绕 draft、submit、cancel、amend 等状态变化运行。理解生命周期，是理解账务、库存和业务一致性的前提。

## 关联源码入口

- `erpnext/accounts/doctype`
- `erpnext/stock/doctype`
- `erpnext/controllers`

## 关联概念

- [[DocType]]
- [[DocType Event]]
- [[database-transaction]]
- [[Accounting]]
- [[Stock]]
