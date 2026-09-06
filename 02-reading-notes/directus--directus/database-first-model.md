---
type: source-reading
status: initial
project: directus/directus
topic: 数据库优先模型
created: 2026-07-02
updated: 2026-07-02
---

# Directus - 数据库优先模型

项目主卡：[[directus--directus]]

## 核心问题

Directus 的关键不是“生成 CRUD”，而是把已有 [[database]] 的 [[schema]] 转换成可管理、可授权、可通过 [[API]] 暴露的数据模型。

## 知识关系

- [[Database-first]]：Directus 的产品起点。
- [[schema]]：Directus 需要识别表、字段、关系和约束。
- [[Metadata]]：数据库不能表达的展示、权限和业务语义需要元数据补充。
- [[Instant API]]：API 不是逐个手写，而是围绕数据模型自动暴露。

## 阅读入口

- `api/src`
- `packages`
- schema、collections、fields、relations、migrations 相关模块。

## 阅读判断

这里要重点区分两层数据：

- 业务数据：用户自己的表和记录。
- Directus 元数据：描述 collection、field、relation、permission、display、layout 的系统数据。

理解这两层的分离，才能理解 Directus 为什么更像 [[machine-readable-software-systems]] 的数据层，而不是普通代码生成器。

## 关联

- [[02-reading-notes/directus--directus/metadata-and-permissions]]
- [[database-first-admin-platforms]]
- [[Metadata]]
