---
type: source-reading
status: initial
project: frappe/erpnext
topic: 库存流水与总账
created: 2026-07-02
updated: 2026-07-02
---

# ERPNext - 库存流水与总账

项目主卡：[[frappe--erpnext]]

## 核心关系

库存流水和总账分录是 ERPNext 中交易一致性的核心。一个业务单据可能同时影响 [[Stock]] 和 [[Accounting]]。

## 关联源码入口

- `erpnext/stock/doctype`
- `erpnext/accounts/doctype`
- `erpnext/controllers`

## 关联概念

- [[Stock]]
- [[Accounting]]
- [[database-transaction]]
- [[OLTP]]
