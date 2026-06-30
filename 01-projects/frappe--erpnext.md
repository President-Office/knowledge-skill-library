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
updated: 2026-06-30
---

# frappe/erpnext

## 一句话定位

ERPNext 是基于 Frappe Framework 的开源 ERP 业务套件，覆盖会计、库存、采购、销售、制造、CRM、项目、支持、区域合规等业务域。它适合学习“元数据驱动的业务系统”如何组织 DocType、工作流、报表、权限、事件钩子和复杂业务交易。

## 为什么学它

- 它不是简单后台脚手架，而是完整 ERP 产品，适合学习真实业务系统的领域拆分和交易一致性。
- 它和 `ruoyi-vue-pro` 形成互补：RuoYi/Yudao 更适合学习 Java 中后台脚手架、模块化和代码生成；ERPNext 更适合学习可配置业务对象、DocType、账务/库存交易和 Frappe 应用生态。
- 之前做开源项目选型时，ERPNext/Frappe 曾被判断为更接近“可定制业务工作流平台”的底座，因为它已有合同、流程、会计、通知、自定义表单/应用等能力。
- 它适合作为后续研究低代码业务平台、ERP、财务系统、库存系统和多模块业务套件的基准样本。

## 当前快照

查询日期：2026-06-30

| 项 | 内容 |
| --- | --- |
| 仓库 | https://github.com/frappe/erpnext |
| 平台 | GitHub |
| 描述 | Free and Open Source Enterprise Resource Planning (ERP) |
| 默认分支 | `develop` |
| 当前 `HEAD` | `78a64cd79befb995213a734267922d04bd99355a` |
| 主要语言 | Python |
| License | GPL-3.0 |
| Stars | 36,361 |
| Forks | 11,924 |
| GitHub `open_issues_count` | 1,937 |
| 最近推送 | 2026-06-30T15:05:45Z |
| 最近更新 | 2026-06-30T15:06:08Z |

来源：GitHub API `repos/frappe/erpnext`、`git ls-remote --symref`、GitHub 仓库页。数字会随时间变化。

## 已验证关键分支

```text
develop              78a64cd79befb995213a734267922d04bd99355a
master               926150bccbf1d93bacebcf36dc33a3d116173138
version-15           25ee3695f09f04c96e771138e02f68b2d3c8b8c1
version-15-hotfix    1d24e1ef62b5b9d0f061e2f43e4033af9ebd884c
version-16           e9a9224ec4558622e646d1db9d4647790fd8ecdf
version-16-hotfix    169a4c82a472127423e9a25e71107d17ab571475
```

已验证标签：

```text
v15.0.0
v16.0.0
```

## 技术栈初判

| 层次 | 技术/概念 |
| --- | --- |
| 后端 | Python、Frappe Framework |
| 前端 | JavaScript、Frappe Desk、页面/表单脚本 |
| 数据模型 | DocType、字段元数据、控制器类、JSON 定义 |
| 业务域 | Accounting、Stock、Buying、Selling、Manufacturing、CRM、Projects、Support |
| 扩展机制 | `hooks.py`、DocType event、scheduler events、fixtures、patches |
| 运行工具 | bench、Frappe app/site 模型 |
| License 影响 | GPL-3.0，二次开发和分发时要认真评估开源义务 |

## 顶层目录入口

GitHub API 在 `develop` 分支看到的关键顶层结构：

```text
erpnext/
├── .github
├── banking
├── erpnext
├── semgrep
├── README.md
├── CODEOWNERS
├── license.txt
├── package.json
├── pyproject.toml
└── yarn.lock
```

`erpnext/` 应用目录下的关键模块：

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

目标：搞清楚 ERPNext 是如何作为 Frappe app 接入运行时的。

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

目标：理解 ERPNext 的核心不是传统 Java MVC 分层，而是 DocType + 元数据 + 控制器 + 事件钩子。

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

- [[02-reading-notes/frappe--erpnext/README|源码阅读索引]]
- [[05-practice-labs/frappe--erpnext/local-setup|本地运行实验]]
- [[04-comparisons/ruoyi-vue-pro-vs-erpnext|RuoYi/Yudao 与 ERPNext 对比]]
