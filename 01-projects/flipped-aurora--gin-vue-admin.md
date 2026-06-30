---
type: open-source-project
status: active
source: github
repo: flipped-aurora/gin-vue-admin
homepage: https://github.com/flipped-aurora/gin-vue-admin
license: Business Source License 1.1
language: Go / Vue / JavaScript
tags: [go, gin, vue3, vite, admin, gorm, casbin, jwt, codegen, ai-assisted]
created: 2026-06-30
updated: 2026-06-30
---

# flipped-aurora/gin-vue-admin

## 一句话定位

`gin-vue-admin` 是一个 Go + Vue3 的后台管理基础平台，后端基于 Gin/GORM/Casbin/JWT，前端基于 Vite/Vue3/Element Plus，内置权限管理、动态路由、资源权限、上传下载、代码生成器、表单生成器、导入导出和 AI/MCP 辅助能力。

## 为什么学它

- 它是 Go 生态里非常典型的前后端分离后台脚手架，适合和 Java 生态的 `ruoyi-vue-pro` 对照学习。
- 它的目录结构清晰分为 `server` 和 `web`，适合快速建立 Go 后台项目的工程地图。
- 它覆盖后台系统常见能力：JWT 登录、Casbin 权限、动态菜单/路由、GORM 数据访问、Swagger、代码生成、文件上传、任务调度、多数据库/多存储适配。
- 它近期开头就强调 AI 辅助开发、MCP、skills 管理，适合作为“传统后台脚手架如何接入 AI 开发能力”的观察样本。

## 当前快照

查询日期：2026-06-30

| 项 | 内容 |
| --- | --- |
| 仓库 | https://github.com/flipped-aurora/gin-vue-admin |
| 平台 | GitHub |
| 描述 | Vite + Vue3 + Gin 的基础开发平台，集成 AI 辅助、MCP、skills 管理、JWT、权限、动态路由、代码生成器等 |
| 默认分支 | `main` |
| 当前 `HEAD` | `4445d0e583ece83bd35c2c104ad7f058f7c03f66` |
| 主要语言 | Go |
| GitHub API license | `NOASSERTION` |
| 实际 LICENSE | Business Source License 1.1 |
| Stars | 24,818 |
| Forks | 7,091 |
| GitHub `open_issues_count` | 40 |
| 最近推送 | 2026-06-30T09:34:10Z |
| 最近更新 | 2026-06-30T11:24:50Z |

来源：GitHub API `repos/flipped-aurora/gin-vue-admin`、`git ls-remote --symref`、仓库 `LICENSE`、`server/go.mod`、`web/package.json`。数字会随时间变化。

## License 注意

仓库 `LICENSE` 开头是 Business Source License 1.1。它适合学习源码和架构，但不是 MIT/Apache 这类宽松许可证。商用、公司内部使用、二次分发或基于它做产品前，必须单独评估许可证条款和商业授权要求。

## 技术栈初判

| 层次 | 技术/概念 |
| --- | --- |
| 后端语言 | Go |
| 后端框架 | Gin |
| ORM | GORM |
| 权限 | Casbin、JWT |
| 配置/日志 | Viper、Zap |
| 数据库/缓存 | MySQL、PostgreSQL、SQL Server、SQLite、MongoDB、Redis 等依赖入口 |
| 文件存储 | 阿里云 OSS、AWS S3、华为 OBS、七牛、腾讯云 COS、MinIO 等 |
| API 文档 | Swagger / swaggo |
| 前端 | Vite、Vue 3、Element Plus、Pinia、Vue Router、Axios |
| AI/Agent | MCP、skills、`.codex`、`.claude`、`.cursor`、`.trae` 等辅助目录 |

## 顶层目录入口

GitHub API 在 `main` 分支看到的关键顶层结构：

```text
gin-vue-admin/
├── .aone_copilot
├── .claude
├── .codex
├── .cursor
├── .github
├── .trae
├── aiDoc
├── deploy
├── server
├── web
├── AGENT.MD
├── LICENSE
├── Makefile
├── README.md
└── README-en.md
```

后端 `server/`：

```text
server/
├── api
├── cmd
├── config
├── core
├── global
├── initialize
├── mcp
├── middleware
├── model
├── plugin
├── resource
├── router
├── service
├── source
├── task
├── utils
├── main.go
├── config.yaml
└── go.mod
```

前端 `web/`：

```text
web/
├── public
├── src
├── vitePlugin
├── package.json
├── vite.config.js
└── index.html
```

前端 `web/src/`：

```text
src/
├── api
├── assets
├── components
├── core
├── directive
├── hooks
├── permission.js
├── pinia
├── plugin
├── router
├── style
├── utils
└── view
```

## 启动入口初读

`server/main.go` 的主路径很清楚：

```text
main()
-> initializeSystem()
   -> core.Viper()
   -> initialize.OtherInit()
   -> core.Zap()
   -> initialize.Gorm()
   -> initialize.Timer()
   -> initialize.DBList()
   -> initialize.SetupHandlers()
   -> initialize.RegisterTables()
-> core.RunServer()
```

第一阶段读源码时，可以从这个路径向下追配置、日志、数据库、定时任务、路由注册和 HTTP 服务启动。

## 第一阶段阅读路线

### 1. 先读后端启动和工程分层

目标：搞清楚 Gin 项目如何初始化配置、日志、数据库、路由、中间件和服务。

优先阅读：

- `server/main.go`
- `server/core`
- `server/initialize`
- `server/global`
- `server/config`
- `server/router`
- `server/middleware`

输出笔记：

- `02-reading-notes/flipped-aurora--gin-vue-admin/server-startup-flow.md`
- `02-reading-notes/flipped-aurora--gin-vue-admin/go-project-structure.md`

### 2. 再读权限和登录体系

目标：理解 JWT、Casbin、菜单、角色、API 权限、资源权限如何协同。

优先阅读：

- `server/middleware`
- `server/model/system`
- `server/service/system`
- `server/router/system`
- `web/src/router`
- `web/src/permission.js`

输出笔记：

- `02-reading-notes/flipped-aurora--gin-vue-admin/auth-rbac-casbin.md`
- `02-reading-notes/flipped-aurora--gin-vue-admin/dynamic-router-permission.md`

### 3. 读代码生成和表单生成

目标：理解它如何把数据库/配置转换成 Go 后端、Vue 页面和表单。

优先阅读：

- `server/service/system`
- `server/model/system`
- `web/src/view`
- `web/src/components`
- `web/src/api`

输出笔记：

- `02-reading-notes/flipped-aurora--gin-vue-admin/codegen-flow.md`
- `02-reading-notes/flipped-aurora--gin-vue-admin/form-generator.md`

### 4. 读 AI/MCP 接入

目标：看传统后台脚手架如何把 AI 辅助开发能力作为工程资产放进仓库。

优先阅读：

- `AGENT.MD`
- `aiDoc`
- `server/mcp`
- `.codex`
- `.claude`
- `.cursor`

输出笔记：

- `02-reading-notes/flipped-aurora--gin-vue-admin/ai-assisted-development.md`

## 核心问题清单

- [ ] `server/main.go` 到 `core.RunServer()` 的完整启动链路是什么？
- [ ] `initialize` 目录里每个初始化步骤的职责边界是什么？
- [ ] Gin 路由如何按模块注册？
- [ ] JWT token 的签发、刷新、拦截和多点登录控制如何实现？
- [ ] Casbin 策略如何与角色、菜单、API 权限关联？
- [ ] 前端动态路由如何从后端菜单/权限生成？
- [ ] 代码生成器的输入模型、模板和输出文件如何组织？
- [ ] 表单生成器与普通 CRUD 生成之间是什么关系？
- [ ] 多数据库和多对象存储适配是如何抽象的？
- [ ] MCP/skills/AI 辅助能力在项目里是文档资产、运行能力还是开发辅助工具？
- [ ] Business Source License 1.1 对学习、公司内部使用和二次分发分别有什么限制？

## 可沉淀模式

后续优先沉淀到 `03-patterns/` 的方向：

- Go + Gin 后台管理系统分层结构。
- Viper/Zap/GORM/Gin 的启动初始化链路。
- Casbin + JWT 的后台权限模型。
- Go 后端与 Vue 动态路由的权限协同。
- 后台代码生成器的模板组织方式。
- 多对象存储适配器设计。
- 后台脚手架接入 MCP/skills/AI 辅助开发的方式。

## 当前判断

`gin-vue-admin` 适合放在“后台脚手架”方向深读。它和 `ruoyi-vue-pro` 的对比价值很高：

- `ruoyi-vue-pro`：Java / Spring / MyBatis Plus / Maven 多模块，适合国内 Java 中后台项目。
- `gin-vue-admin`：Go / Gin / GORM / Vue3，适合学习 Go 后台管理工程结构和轻量化服务端。
- `erpnext`：Python / Frappe / DocType，适合学习完整 ERP 和元数据驱动业务系统。

后续不要把它当 ERP 学，而应该从启动链路、权限模型、代码生成和前后端契约开始。

## 相关笔记

- [[02-reading-notes/flipped-aurora--gin-vue-admin/README|源码阅读索引]]
- [[05-practice-labs/flipped-aurora--gin-vue-admin/local-setup|本地运行实验]]
- [[04-comparisons/admin-scaffold-comparison|后台脚手架对比]]
