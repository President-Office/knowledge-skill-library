---
type: source-reading
status: initial
project: directus/directus
topic: SDK 与 API 契约
created: 2026-07-02
updated: 2026-07-02
---

# Directus - SDK 与 API 契约

项目主卡：[[directus--directus]]

## 核心问题

Directus 的 [[SDK]] 把外部应用、脚本和 Agent 调用 [[API]] 的方式封装起来。这里要看的不是“有没有 SDK”，而是 SDK 如何表达认证、请求、资源、类型和错误。

## 知识关系

- [[SDK]]：降低外部系统接入成本。
- [[API]]：Directus 对外能力契约。
- [[REST]] / [[GraphQL]]：不同接口风格对调用方和 AI Agent 的影响不同。
- [[Instant API]]：契约来自数据模型、权限和元数据。

## 阅读入口

- `sdk/src`
- `api/src`
- API 认证、请求封装、类型定义相关模块。

## 阅读判断

SDK 是 Directus 从“后台系统”变成“数据平台”的关键出口。对 AI Agent 来说，稳定、可描述、可组合的 SDK/API 比手写 CRUD 更重要。

## 关联

- [[02-reading-notes/directus--directus/database-first-model]]
- [[02-reading-notes/directus--directus/metadata-and-permissions]]
- [[MCP]]
- [[machine-readable-software-systems]]
