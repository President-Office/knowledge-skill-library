---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, frappe, configuration]
---

# fixtures

fixtures 是随代码分发的配置或种子数据，用来让应用在安装、迁移或测试时具备必要的基础配置。

在 Frappe 生态中，fixtures 常用于把自定义字段、权限、工作流、报表等配置从一个环境带到另一个环境。

## 学习重点

- 哪些配置应该成为 fixtures，哪些应该留在环境内。
- fixtures 是否会覆盖线上手工配置。
- fixtures 和 patches、迁移脚本如何配合。

## 关联

- [[Frappe App]]
- [[Metadata]]
- [[patches]]
- [[schema]]
