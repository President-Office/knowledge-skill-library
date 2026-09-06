---
type: source-reading
status: initial
project: directus/directus
topic: Admin App 架构
created: 2026-07-02
updated: 2026-07-02
---

# Directus - Admin App 架构

项目主卡：[[directus--directus]]

## 核心问题

Directus 的 [[Admin App]] 不是普通业务前端，而是一个根据 [[Metadata]]、[[权限模型]] 和 [[API]] 动态工作的后台应用。

## 知识关系

- [[Vue]] / [[Vite]]：Admin App 的前端工程基础。
- [[Admin Panel]]：面向管理人员的数据操作界面。
- [[Metadata]]：决定列表、表单、关系字段和展示方式。
- [[权限模型]]：决定界面上哪些集合、字段、操作可见可用。

## 阅读入口

- `app/src`
- 与 collections、fields、relations、layout、interfaces 相关的前端模块。

## 阅读判断

读 Admin App 时不要只看页面组件，要看它如何把“元数据”变成“用户可以操作的界面”。这和 RuoYi/Yudao 的手写页面或代码生成页面不同。

## 关联

- [[02-reading-notes/directus--directus/metadata-and-permissions]]
- [[02-reading-notes/directus--directus/sdk-and-api-contract]]
- [[Admin App]]
