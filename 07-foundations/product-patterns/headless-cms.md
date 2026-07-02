---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [headless-cms, cms, api, admin]
---

# Headless CMS

## 核心定位

Headless CMS 是把内容管理能力和前端展示层解耦的系统。它通常提供数据模型、权限、Admin 界面、API、SDK，让不同前端或业务系统通过 API 消费内容和数据。

它是 [[cms]] 的一种架构形态：保留内容建模和管理能力，把页面展示交给独立前端。

## 为什么重要

传统 CMS 往往绑定页面渲染方式。Headless CMS 更关注：

- 内容或数据如何建模。
- 管理后台如何编辑数据。
- API 如何暴露给多个前端。
- 权限如何控制字段、集合、操作。
- 扩展机制如何承接业务逻辑。

在 AI 时代，Headless CMS 和 Database First 平台的价值不只来自“少写 CRUD”，还来自它们能否把内容、数据、字段、关系和权限变成机器可读结构。更完整的判断见：[[machine-readable-software-systems]]。

## Headless CMS 不等于什么

| 误解 | 更准确的理解 |
| --- | --- |
| Headless CMS 只是内容系统 | 它也可能承担后台 Admin、API 平台、数据管理能力 |
| Headless CMS 不需要后端 | 它只是把后端能力产品化，仍然有数据、权限、扩展和运行时 |
| 有 Admin Panel 就是 CMS | CMS 还需要内容模型、权限、API、工作流等能力 |
| 可以替代所有业务系统 | 复杂业务交易、强一致流程、ERP 规则通常需要专门业务服务 |

## Directus 和 Payload 的差异

| 维度    | Directus       | Payload                          |
| ----- | -------------- | -------------------------------- |
| 起点    | 现有数据库          | TypeScript 配置                    |
| 核心范式  | Database-first | Code-config-first                |
| Admin | 元数据驱动          | 配置驱动                             |
| 适合场景  | 已有数据库快速变后台/API | Next.js / TypeScript 项目内嵌后台和 CMS |

## 在项目中怎么观察

| 项目 | 观察点 |
| --- | --- |
| [[directus--directus]] | 数据库 schema、metadata、permissions、Admin、API 如何协同 |
| [[payloadcms--payload]] | collections、fields、hooks、access、Admin Panel 如何从代码配置生成 |

## 关联

- [[cms]]
- [[enterprise-software-systems]]
- [[database]]
- [[machine-readable-software-systems]]
- [[monorepo]]
- [[directus]]
- [[payload]]
- [[database-first-admin-platforms]]
