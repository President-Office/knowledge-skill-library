---
type: open-source-project
status: active
source: github
repo: frappe/erpnext
homepage: https://github.com/frappe/erpnext
license: GPL-3.0
language: Python / JavaScript
tags: [erp, frappe, python, accounting, inventory, manufacturing, crm, business-suite]
created: 2026-06-30
updated: 2026-07-02
---

# frappe/erpnext

## 一句话定位

ERPNext 是基于 [[Frappe Framework]] 的开源 [[erp]] 业务套件，覆盖会计、库存、采购、销售、制造、CRM、项目、支持、区域合规等业务域。它适合学习“元数据驱动的业务系统”如何组织 [[DocType]]、工作流、报表、权限、事件钩子和复杂业务交易。

## 为什么学它

- 它不是简单后台脚手架，而是完整 ERP 产品，适合学习真实业务系统的领域拆分和交易一致性。
- 它和 `ruoyi-vue-pro` 形成互补：RuoYi/Yudao 更适合学习 [[Java]] 中后台脚手架、模块化和代码生成；ERPNext 更适合学习可配置业务对象、[[DocType]]、账务/库存交易和 Frappe 应用生态。
- 它适合作为研究低代码业务平台、ERP、财务系统、库存系统和多模块业务套件的基准样本。
- 它能帮助理解 [[machine-readable-software-systems]] 中的元数据、权限、业务对象和工作流如何结合。

## 技术栈初判

| 层次 | 技术/概念 |
| --- | --- |
| 后端 | [[Python]]、[[Frappe Framework]] |
| 前端 | [[JavaScript]]、[[Frappe Desk]]、页面/表单脚本 |
| 数据模型 | [[DocType]]、字段 [[Metadata]]、控制器 [[class]]、[[JSON]] 定义 |
| 业务域 | [[Accounting]]、[[Stock]]、[[Buying]]、[[Selling]]、[[Manufacturing]]、[[crm]]、[[Projects]]、[[Support]] |
| 扩展机制 | `hooks.py`、[[DocType Event]]、[[Scheduler Event]]、[[fixtures]]、[[patches]] |
| 运行工具 | [[bench]]、[[Frappe App]] / [[Frappe Site]] 模型 |
| License 影响 | GPL-3.0，二次开发和分发时要认真评估开源义务 |

## 顶层目录入口

ERPNext 的关键结构不是普通 Controller / Service / Mapper，而是 Frappe app 结构和业务模块目录。

```text
erpnext/
├── accounts
├── assets
├── buying
├── controllers
├── crm
├── domains
├── erpnext_integrations
├── manufacturing
├── patches
├── projects
├── regional
├── selling
├── setup
├── shopping_cart
├── stock
├── support
├── utilities
├── hooks.py
├── modules.txt
└── patches.txt
```

## 第一阶段阅读路线

### 1. 先读 Frappe 应用结构

目标：搞清楚 ERPNext 是如何作为 [[Frappe App]] 接入运行时的。

优先阅读：

- `pyproject.toml`
- `erpnext/hooks.py`
- `erpnext/modules.txt`
- `erpnext/patches.txt`
- `erpnext/config`
- `erpnext/setup`

输出笔记：

- `02-reading-notes/frappe--erpnext/frappe-app-structure.md`
- `02-reading-notes/frappe--erpnext/hooks-and-events.md`

### 2. 再读 DocType 模型

目标：理解 ERPNext 的核心不是传统 Java MVC 分层，而是 [[DocType]] + [[Metadata]] + 控制器 + 事件钩子。

优先阅读：

- `erpnext/accounts/doctype`
- `erpnext/stock/doctype`
- `erpnext/selling/doctype`
- `erpnext/buying/doctype`
- 每个 DocType 下的 `.json`、`.py`、`.js`、测试文件。

输出笔记：

- `02-reading-notes/frappe--erpnext/doctype-model.md`
- `02-reading-notes/frappe--erpnext/document-lifecycle.md`

### 3. 选择一个业务闭环深读

建议优先读“销售到收款”或“采购到付款”，因为它们能同时覆盖主数据、单据流转、库存、账务和状态更新。

候选闭环：

- Sales Order -> Delivery Note -> Sales Invoice -> Payment Entry -> GL Entry
- Purchase Order -> Purchase Receipt -> Purchase Invoice -> Payment Entry
- Stock Entry -> Stock Ledger Entry -> GL Entry
- BOM -> Work Order -> Job Card -> Stock Entry

输出笔记：

- `02-reading-notes/frappe--erpnext/sales-to-cash.md`
- `02-reading-notes/frappe--erpnext/procure-to-pay.md`
- `02-reading-notes/frappe--erpnext/stock-ledger-and-gl.md`

## 核心问题清单

- [ ] Frappe app 的生命周期如何加载 `hooks.py`？
- [ ] ERPNext 的 DocType JSON、Python 控制器、JS 表单脚本如何配合？
- [ ] 一个业务单据从 draft、submit、cancel 到 amend 的状态机如何实现？
- [ ] 会计分录 `GL Entry` 由哪些业务单据触发？
- [ ] 库存流水 `Stock Ledger Entry` 和账务分录如何保持一致？
- [ ] `accounts`、`stock`、`selling`、`buying` 四个模块之间如何互相依赖？
- [ ] patches 如何迁移历史数据和修复版本升级问题？
- [ ] 区域合规逻辑放在 `regional` 下如何接入主流程？
- [ ] ERPNext 自定义业务对象和自定义字段的边界在哪里？
- [ ] GPL-3.0 对二次开发和商业使用有什么影响？

## 可沉淀模式

后续优先沉淀到 `03-patterns/` 的方向：

- Frappe DocType 元数据驱动模型。
- 业务单据生命周期：draft / submit / cancel / amend。
- ERP 交易流水和不可变账务分录设计。
- 库存流水与会计分录联动。
- hooks 事件扩展机制。
- patch 驱动的数据迁移体系。
- 区域合规插件化组织方式。
- 完整业务套件与后台脚手架的架构差异。

## 当前判断

ERPNext 值得长期学习，但不适合从代码目录从头扫到尾。更高效的路径是：

1. 先理解 Frappe app/site/DocType 运行模型。
2. 选择 Accounting 或 Stock 作为第一业务域。
3. 按一个完整业务闭环追调用链。
4. 把 DocType、事件钩子、账务流水、库存流水分别沉淀为模式。
5. 和 `ruoyi-vue-pro` 做横向比较：一个是 Java 中后台开发底座，一个是 Python/Frappe 元数据驱动 ERP 套件。

## 相关笔记

- [[02-reading-notes/frappe--erpnext/README]]
- [[05-practice-labs/frappe--erpnext/local-setup]]
- [[04-comparisons/ruoyi-vue-pro-vs-erpnext]]
