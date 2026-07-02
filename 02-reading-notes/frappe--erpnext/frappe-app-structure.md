---
type: source-reading
status: initial
project: frappe/erpnext
topic: Frappe app 结构
created: 2026-07-02
updated: 2026-07-02
---

# ERPNext - Frappe app 结构

项目主卡：[[frappe--erpnext]]
特点卡：[[erpnext]]

## 阅读目标

先理解 ERPNext 不是传统前后端分离后台，而是一个 Frappe app。读懂 app 结构后，再进入 DocType、单据生命周期、账务和库存流水。

## 已确认结构

ERPNext 的关键入口集中在 `erpnext/` 应用目录：

| 目录 / 文件 | 初步职责 |
| --- | --- |
| `erpnext/hooks.py` | Frappe app 接入运行时的核心配置入口 |
| `erpnext/modules.txt` | 模块声明 |
| `erpnext/patches.txt` | 版本升级和数据迁移补丁列表 |
| `erpnext/accounts` | 会计域 |
| `erpnext/stock` | 库存域 |
| `erpnext/selling` | 销售域 |
| `erpnext/buying` | 采购域 |
| `erpnext/manufacturing` | 制造域 |
| `erpnext/controllers` | 跨模块控制器和通用业务逻辑 |

## 初步判断

ERPNext 的核心不是 Controller / Service / Mapper，而是 Frappe 的 DocType 体系：

- DocType JSON 描述字段、权限、表单结构。
- Python 控制器承载业务校验和生命周期逻辑。
- JavaScript 表单脚本承载前端交互。
- hooks 和 patches 负责扩展、事件接入和升级。

这和 [[ruoyi-vue-pro]]、[[jeecgboot]] 的 Java 分层模型完全不同。

## 读源码时要验证的问题

- `hooks.py` 里注册了哪些 document events、scheduler events、fixtures？
- 一个 DocType 目录中 `.json`、`.py`、`.js`、测试文件如何配合？
- `accounts` 和 `stock` 之间通过哪些公共控制器或服务交互？
- `patches.txt` 如何保证历史版本数据迁移？

## Obsidian 关联

- 底层概念：[[database]]、[[boundaries]]、[[abstractions]]
- 框架特点：[[erpnext]]
- 与 RuoYi 对比：[[ruoyi-vue-pro-vs-erpnext]]
- 一对一对比：[[pairwise-backend-comparisons]]
