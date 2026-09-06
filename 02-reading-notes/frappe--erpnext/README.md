# ERPNext 源码阅读索引

项目主卡：[[frappe--erpnext]]
特点卡：[[erpnext]]

## 阅读主题网络

| 主题 | 关联源码入口 | 关键概念 |
| --- | --- | --- |
| [[frappe-app-structure]] | `pyproject.toml`、`erpnext/hooks.py`、`erpnext/modules.txt` | [[Frappe App]]、[[Frappe Site]]、[[bench]] |
| [[02-reading-notes/frappe--erpnext/hooks-and-events]] | `erpnext/hooks.py`、`erpnext/patches` | [[DocType Event]]、[[Scheduler Event]]、[[patches]] |
| [[02-reading-notes/frappe--erpnext/doctype-model]] | `erpnext/*/doctype` | [[DocType]]、[[Metadata]]、[[JSON]] |
| [[02-reading-notes/frappe--erpnext/document-lifecycle]] | `erpnext/controllers`、核心 doctype 控制器 | [[DocType Event]]、[[database-transaction]] |
| [[02-reading-notes/frappe--erpnext/sales-to-cash]] | `selling`、`stock`、`accounts` | [[Selling]]、[[Stock]]、[[Accounting]] |
| [[02-reading-notes/frappe--erpnext/procure-to-pay]] | `buying`、`stock`、`accounts` | [[Buying]]、[[Stock]]、[[Accounting]] |
| [[02-reading-notes/frappe--erpnext/stock-ledger-and-gl]] | `stock`、`accounts` | [[Stock]]、[[Accounting]]、[[OLTP]] |

## 当前问题

- [ ] 本地安装 bench。
- [ ] 确认 ERPNext 与 Frappe 的分支版本配套关系。
- [ ] 跑通一个本地 site。
- [ ] 确认 DocType 文件结构：`.json`、`.py`、`.js`、测试文件。
- [ ] 选定第一个业务闭环：销售到收款或采购到付款。
