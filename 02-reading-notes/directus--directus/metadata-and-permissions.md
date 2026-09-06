---
type: source-reading
status: initial
project: directus/directus
topic: 元数据与权限
created: 2026-07-02
updated: 2026-07-02
---

# Directus - 元数据与权限

项目主卡：[[directus--directus]]

## 核心问题

Directus 的 [[Metadata]] 不只是 UI 配置，而是连接 [[database]]、[[Admin App]]、[[API]] 和 [[权限模型]] 的中间层。

## 知识关系

- [[Metadata]]：描述 collections、fields、relations、display、layout 等信息。
- [[权限模型]]：决定谁能对哪些 collection、field、item、operation 执行动作。
- [[Admin Panel]]：根据元数据和权限动态呈现管理界面。
- [[Instant API]]：根据数据模型和权限暴露接口能力。

## 阅读入口

- `api/src`
- `packages`
- collections、fields、relations、permissions 相关模块。

## 阅读判断

Directus 对 AI 友好的价值就在这里：它把字段、关系、权限和接口能力组织成机器可读结构。未来如果 Agent 要读写数据，它需要的不是一堆 Controller，而是可发现的数据模型和权限边界。

## 关联

- [[machine-readable-software-systems]]
- [[02-reading-notes/directus--directus/database-first-model]]
- [[02-reading-notes/directus--directus/admin-app-architecture]]
- [[02-reading-notes/directus--directus/sdk-and-api-contract]]
