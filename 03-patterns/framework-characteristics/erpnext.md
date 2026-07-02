---
type: framework-characteristics
status: draft
project: frappe/erpnext
created: 2026-07-02
updated: 2026-07-02
---

# ERPNext 特点

项目主卡：[[frappe--erpnext]]

## 核心定位

基于 [[Frappe Framework]] 的完整 ERP 业务套件。它不是后台脚手架，而是围绕会计、库存、采购、销售、制造、CRM 等业务域构建的元数据驱动业务系统。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| [[DocType]] 元数据模型 | 业务对象由 [[DocType]] JSON、[[Python]] 控制器、JS 表单脚本共同表达 | 学元数据驱动业务系统 |
| 完整 ERP 业务闭环 | Accounting、Stock、Buying、Selling、Manufacturing 等模块成熟 | 学真实业务单据流和交易一致性 |
| Document 生命周期 | draft、submit、cancel、amend 等状态机制贯穿业务 | 学业务单据状态机 |
| 账务与库存流水 | GL Entry、Stock Ledger Entry 等流水是核心 | 学 ERP 级不可变交易记录 |
| hooks / patches 扩展 | 通过事件钩子、fixtures、patches 接入扩展和升级 | 学业务平台扩展与迁移 |
| GPL-3.0 许可证 | 二开和分发要评估开源义务 | 学项目选型时的许可证风险 |

## 最适合怎么读

1. 先理解 Frappe app、site、[[DocType]]、hooks 的运行模型。
2. 选择 Accounting 或 Stock 作为第一个业务域。
3. 按业务闭环读：例如 Sales Order -> Delivery Note -> Sales Invoice -> Payment Entry -> GL Entry。

## 不要误解

- 不要把 ERPNext 当普通前后端分离后台，它是 Frappe 全栈应用。
- 不要从目录从头扫到尾，应该按业务单据闭环追踪。
- 不要忽略 GPL-3.0，学习可以，商用和分发要单独评估。

## 关联

- [[database]]
- [[boundaries]]、[[abstractions]]
- [[ruoyi-vue-pro-vs-erpnext]]
- [[pairwise-backend-comparisons]]
