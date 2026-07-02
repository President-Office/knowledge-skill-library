---
type: framework-characteristics
status: draft
project: directus/directus
created: 2026-07-02
updated: 2026-07-02
---

# Directus 特点

项目主卡：[[directus--directus]]

## 核心定位

数据库优先的 [[headless-cms]] / [[Admin App]] / [[API]] 平台。它的起点不是先写业务代码，而是把现有数据库通过 [[Metadata]]、[[权限模型]]、[[Admin App]] 和 [[Instant API]] 产品化。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| [[Database-first]] | 从现有数据库 [[schema]] 出发组织后台和 [[API]] | 学数据库如何变成产品化后台 |
| 元数据驱动 | collections、fields、relations、permissions 由 [[Metadata]] 表达 | 学运行时配置和动态 Admin |
| [[Instant API]] | [[REST]] / [[GraphQL]] / [[SDK]] 围绕数据模型生成 | 学 [[API]] 平台化 |
| [[Admin Panel]] | 管理端根据 [[Metadata]] 动态渲染 | 学后台页面运行时生成 |
| [[TypeScript]] monorepo | `api`、`app`、`sdk`、`packages` 分包 | 学 TS 后台平台包边界 |
| 许可证有约束 | MSCL-1.0-GPL 不是普通 MIT/Apache | 学自托管平台的许可证评估 |

## 最适合怎么读

1. 先读 monorepo：`api`、`app`、`directus`、`sdk`、`packages`。
2. 再读 [[schema]] / [[Metadata]] / [[权限模型]]。
3. 最后读 [[Admin App]]、[[SDK]]、extensions。

## 不要误解

- 不要把它当代码生成器，Directus 更像运行时元数据平台。
- 不要假设它适合所有复杂业务逻辑，重业务流程可能仍要写扩展或独立服务。
- 不要忽略 MSCL-1.0-GPL，对竞争性使用和产品化有约束。

## 关联

- [[database]]
- [[monorepo]]
- [[headless-cms]]
- [[payload]]
- [[database-first-admin-platforms]]
- [[pairwise-backend-comparisons]]
