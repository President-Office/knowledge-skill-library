---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, frappe, runtime]
---

# Frappe Site

Frappe Site 是 Frappe 的运行实例，通常对应一套站点配置、数据库、已安装 app 和运行环境。

理解 site 模型很重要，因为 ERPNext 不是单纯启动一个 Python 包，而是在 Frappe site 中加载 app、DocType、权限和配置。

## 学习重点

- site 如何绑定数据库、配置和已安装 app。
- bench 如何创建、迁移、启动和管理 site。
- 多站点部署时 app 代码和站点数据如何分离。

## 关联

- [[Frappe Framework]]
- [[Frappe App]]
- [[bench]]
- [[DocType]]
