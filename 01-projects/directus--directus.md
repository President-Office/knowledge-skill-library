---
type: open-source-project
status: active
source: github
repo: directus/directus
homepage: https://github.com/directus/directus
license: MSCL-1.0-GPL
language: TypeScript / Vue
tags: [typescript, headless-cms, admin-panel, database-first, api, auth, sdk, vue]
created: 2026-06-30
updated: 2026-06-30
---

# directus/directus

## 一句话定位

Directus 是数据库优先的后台平台：把现有数据库变成 Headless CMS、Admin Panel、即时 API、权限系统和可定制应用界面。它适合学习“围绕数据库元数据自动生成后台和 API”的产品化架构。

## 为什么学它

- 它和 RuoYi / JeecgBoot / gin-vue-admin 不同，不是从代码生成 CRUD 出发，而是从数据库和元数据出发生成管理后台与 API。
- 它适合学习 Headless CMS、数据模型反射、权限、字段/集合配置、Admin App、SDK、扩展包和 API 层的组合方式。
- 它是 TypeScript monorepo，能补上当前知识库里 TS 后台平台方向。
- 它适合和后续 `Strapi`、`Payload`、`Supabase` 做“后台/CMS/API 平台”横向对比。

## License 注意

Directus 的许可证是 `MSCL-1.0-GPL`，不是 MIT / Apache 这类宽松许可证。它适合学习源码和架构；如果要商用、托管成服务、分发或作为产品底座，必须单独评估许可证条款。

## 技术栈初判

| 层次 | 技术/概念 |
| --- | --- |
| 语言 | [[TypeScript]] |
| 管理端 | [[Vue]] / [[Vite]] |
| Monorepo | [[pnpm workspace]] |
| Node | [[Node.js]] |
| 包管理 | [[pnpm]] |
| 核心形态 | [[API]]、[[Admin App]]、[[CLI]]、[[SDK]]、[[Monorepo Package]] |
| 产品范式 | [[Database-first]]、[[headless-cms]]、[[Admin Panel]]、[[Instant API]] |

## 顶层目录入口

关键顶层结构：

```text
directus/
├── .changeset
├── .github
├── api
├── app
├── directus
├── packages
├── sdk
├── tests
├── Dockerfile
├── docker-compose.yml
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
├── readme.md
└── license
```

核心子目录：

```text
api/       # Directus API 服务包
app/       # 管理端应用
directus/  # CLI/主包入口
sdk/       # TypeScript SDK
packages/  # 共享包和扩展能力
tests/     # 测试
```

## 第一阶段阅读路线

### 1. 先读 monorepo 和运行入口

目标：搞清楚 Directus 的包边界、构建方式和服务启动入口。

优先阅读：

- `package.json`
- `pnpm-workspace.yaml`
- `directus/package.json`
- `api/package.json`
- `app/package.json`
- `sdk/package.json`

输出笔记：

- `02-reading-notes/directus--directus/monorepo-structure.md`
- `02-reading-notes/directus--directus/runtime-entrypoints.md`

### 2. 再读数据库优先模型

目标：理解 Directus 如何从数据库 [[schema]] / [[Metadata]] 组织 collections、fields、relations、[[权限模型]] 和 [[API]]。

优先阅读：

- `api/src`
- `packages`
- 数据模型、schema、权限、迁移相关模块。

输出笔记：

- `02-reading-notes/directus--directus/database-first-model.md`
- `02-reading-notes/directus--directus/metadata-and-permissions.md`

### 3. 读 [[Admin App]] 和 [[SDK]]

目标：理解管理端如何消费后端 [[API]]，[[SDK]] 如何把 [[API]] 封装给外部应用。

优先阅读：

- `app/src`
- `sdk/src`
- `api/src`

输出笔记：

- `02-reading-notes/directus--directus/admin-app-architecture.md`
- `02-reading-notes/directus--directus/sdk-and-api-contract.md`

### 4. 读扩展机制

目标：Directus 的学习价值不只在 CRUD，而在扩展包、hooks、flows、custom interfaces/layouts 等产品化扩展方式。

优先阅读：

- `packages`
- `api/src`
- `app/src`

输出笔记：

- `02-reading-notes/directus--directus/extension-system.md`

## 核心问题清单

- [ ] Directus 的 monorepo 包之间如何依赖？
- [ ] [[CLI]] 如何启动 [[API]] 服务？
- [ ] 它如何发现和表达数据库 collections、fields、relations？
- [ ] 元数据表和真实业务表如何分离？
- [ ] 权限系统如何控制 collection、field、item 和 operation？
- [ ] [[Admin App]] 如何根据元数据动态渲染列表、表单和关系？
- [ ] [[SDK]] 如何抽象认证、请求、类型和资源操作？
- [ ] 扩展系统如何接入 [[API]] 和 [[Admin App]]？
- [ ] 它和 JeecgBoot 的“低代码/代码生成”相比，数据库优先模式的优势和代价是什么？
- [ ] `MSCL-1.0-GPL` 对自建服务、SaaS、二次分发分别有什么限制？

## 可沉淀模式

后续优先沉淀到 `03-patterns/` 的方向：

- 数据库优先后台平台架构。
- 元数据驱动 [[Admin App]]。
- Headless CMS 权限模型。
- [[API]] + [[Admin App]] + [[SDK]] 三件套组织方式。
- TypeScript monorepo 的包边界。
- 自托管后台平台的许可证风险评估。

## 当前判断

Directus 应该作为“数据库优先后台平台”的代表项目学习。它和当前已收项目的关系是：

- `ruoyi-vue-pro`：Java 企业后台和业务中台。
- `JeecgBoot`：Java 低代码/零代码/AI 辅助后台平台。
- `gin-vue-admin`：Go + Vue 后台脚手架。
- `ERPNext`：完整 ERP 和 Frappe 元数据业务系统。
- `Directus`：数据库优先的 Headless CMS / Admin / API 平台。

后续不要按普通 MVC CRUD 项目读 Directus，而要按 [[schema]] introspection、[[Metadata]]、[[权限模型]]、[[Admin App]]、[[SDK]] 和 extensions 这条线读。

## 相关笔记

- [[02-reading-notes/directus--directus/README]]
- [[05-practice-labs/directus--directus/local-setup]]
- [[database-first-admin-platforms]]
