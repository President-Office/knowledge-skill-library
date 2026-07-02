---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [monorepo, engineering-organization]
---

# Monorepo

## 核心定位

Monorepo 是一种工程组织方式：多个应用、包、工具或模块放在同一个仓库中管理。它不是为了“目录更大”，而是为了让共享代码、依赖关系、构建流程、版本协作在一个边界内被治理。

## 为什么重要

很多现代后台平台都不是一个简单应用：

- API 服务和 Admin App 要共享类型、权限、请求契约。
- 多个 UI 应用要共享布局、状态、工具和样式。
- 核心框架、数据库适配器、插件、模板需要共同演进。

这些场景会自然推向 monorepo。

## 典型结构

| 目录 | 常见职责 |
| --- | --- |
| `apps/` | 可运行应用，例如管理端、文档站、不同 UI 入口 |
| `packages/` | 可复用包，例如 core、sdk、ui、utils、db adapters |
| `examples/` | 示例项目 |
| `templates/` | 项目模板 |
| `tools/` / `internal/` | 构建、代码生成、内部工具 |

## 好处和代价

| 方面 | 好处 | 代价 |
| --- | --- | --- |
| 共享代码 | 类型、工具、UI、SDK 可以统一复用 | 包边界不清会互相污染 |
| 构建协作 | 可以统一 lint、test、build | 构建缓存和依赖编排更复杂 |
| 版本演进 | 多包可以同步修改 | 发布策略和变更影响面更大 |
| 团队认知 | 系统全貌集中 | 新人上手成本更高 |

## 在项目中怎么观察

| 项目 | 观察点 |
| --- | --- |
| [[directus--directus]] | `api`、`app`、`sdk`、`packages` 如何组成数据库优先平台 |
| [[payloadcms--payload]] | core、Next 集成、UI、数据库适配器、插件、模板如何拆包 |
| [[yudaocode--yudao-ui-admin-vben]] | 多 UI app 和共享 packages 如何支撑平台化前端 |

## 不要误解

- Monorepo 不自动带来工程治理，治理来自清晰包边界和构建规则。
- 小团队快速业务交付时，单应用结构可能更合适。
- Monorepo 的价值在复用和协作，不在“看起来高级”。

## 关联

- [[boundaries]]、[[abstractions]]
- [[yudao-ui-admin-vben]]
- [[payload]]
- [[directus]]
