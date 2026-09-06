---
type: source-reading
status: initial
project: frappe/erpnext
topic: 采购到付款
created: 2026-07-02
updated: 2026-07-02
---

# ERPNext - 采购到付款

项目主卡：[[frappe--erpnext]]

## 核心关系

采购到付款链路连接 [[Buying]]、[[Stock]] 和 [[Accounting]]：采购订单、收货、采购发票和付款共同影响库存与账务。

## 关联源码入口

- `erpnext/buying/doctype`
- `erpnext/stock/doctype`
- `erpnext/accounts/doctype`

## 关联概念

- [[Buying]]
- [[Stock]]
- [[Accounting]]
- [[database-transaction]]
