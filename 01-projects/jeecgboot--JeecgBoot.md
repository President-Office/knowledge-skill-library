---
type: open-source-project
status: active
source: github
repo: jeecgboot/JeecgBoot
homepage: https://github.com/jeecgboot/JeecgBoot
license: Apache-2.0
language: Java / Vue / TypeScript
tags: [java, spring-boot, vue3, low-code, codegen, ai-skills, shiro, mybatis-plus, admin]
created: 2026-06-30
updated: 2026-06-30
---

# jeecgboot/JeecgBoot

## 一句话定位

JeecgBoot 是 Java 生态的 AI 低代码/零代码后台平台，核心是用 Spring Boot + Vue3 构建企业后台，并通过代码生成、在线配置、流程/表单设计、报表、AI Skills 和 MCP 插件减少重复开发。

## 为什么学它

- 它和 `ruoyi-vue-pro` 同属国内 Java 后台/低代码赛道，适合横向比较代码生成、权限、菜单、模块化和业务扩展方式。
- 它比普通 CRUD 脚手架更强调低代码、零代码、在线表单、流程、报表和 AI 生成系统。
- 它采用 Apache-2.0，比一些非标准商业许可证项目更适合作为学习和参考对象。
- 它适合研究“Java 后台平台如何从代码生成走向 AI 辅助业务系统生成”。

## 当前快照

查询日期：2026-06-30

| 项 | 内容 |
| --- | --- |
| 仓库 | https://github.com/jeecgboot/JeecgBoot |
| 平台 | GitHub |
| 描述 | AI 低代码平台，支持低代码/零代码、AI Skills、知识库、流程编排、MCP 插件、代码生成 |
| 默认分支 | `main` |
| 当前 `HEAD` | `faca0d058e4d7a93a8e6d2ab33e53cda0ec35552` |
| 主要语言 | Java |
| License | Apache-2.0 |
| Stars | 46,919 |
| Forks | 16,077 |
| GitHub `open_issues_count` | 31 |
| 最近推送 | 2026-06-29T02:06:09Z |
| 最近更新 | 2026-06-30T14:56:57Z |

来源：GitHub API `repos/jeecgboot/JeecgBoot`、`git ls-remote --symref`、`jeecg-boot/pom.xml`、`jeecgboot-vue3/package.json`。数字会随时间变化。

## 技术栈初判

| 层次 | 技术/概念 |
| --- | --- |
| 后端 | Spring Boot 3.5.5、Java 17 默认，POM 注释显示支持 JDK 17、21、24、25 |
| 持久层 | MyBatis Plus、dynamic-datasource、Druid |
| 权限 | Shiro、JWT、shiro-redis |
| 微服务 | Spring Cloud 2025.0.0、Spring Cloud Alibaba、Nacos |
| 报表/BI | JimuReport、JimuBI |
| 代码生成 | jeecg codegenerate |
| 前端 | Vue 3.5、Vite、Ant Design Vue、Pinia、Vue Router |
| AI/流程 | README 描述包含 AI聊天、知识库、流程编排、MCP插件、AI Skills；前端依赖含 `@jeecg/aiflow` |

## 顶层目录入口

GitHub API 在 `main` 分支看到的关键顶层结构：

```text
JeecgBoot/
├── .github
├── jeecg-boot
├── jeecgboot-vue3
├── README.md
├── README-AI.md
├── LICENSE
├── docker-compose.yml
├── docker-compose-cloud.yml
├── check_jeecgenv.py
└── start-docker-compose*.sh / .bat
```

后端 `jeecg-boot/`：

```text
jeecg-boot/
├── db
├── jeecg-boot-base-core
├── jeecg-boot-module
├── jeecg-module-system
├── jeecg-server-cloud
├── pom.xml
├── docker-compose.yml
└── README.md
```

前端 `jeecgboot-vue3/`：

```text
jeecgboot-vue3/
├── build
├── electron
├── mock
├── public
├── src
├── tests
├── types
├── package.json
├── vite.config.ts
└── pnpm-lock.yaml
```

## 第一阶段阅读路线

### 1. 先读后端 Maven 和模块边界

目标：搞清楚 JeecgBoot 的后端工程如何拆分核心能力、系统模块、业务模块和云服务模块。

优先阅读：

- `jeecg-boot/pom.xml`
- `jeecg-boot/jeecg-boot-base-core`
- `jeecg-boot/jeecg-module-system`
- `jeecg-boot/jeecg-boot-module`
- `jeecg-boot/jeecg-server-cloud`

输出笔记：

- `02-reading-notes/jeecgboot--JeecgBoot/maven-module-structure.md`
- `02-reading-notes/jeecgboot--JeecgBoot/backend-startup-flow.md`

### 2. 再读权限、菜单和租户/组织模型

目标：理解 Shiro、JWT、角色、菜单、部门、用户和权限标识如何组织。

优先阅读：

- `jeecg-boot/jeecg-module-system`
- `jeecg-boot/jeecg-boot-base-core`
- `jeecgboot-vue3/src`

输出笔记：

- `02-reading-notes/jeecgboot--JeecgBoot/auth-shiro-jwt.md`
- `02-reading-notes/jeecgboot--JeecgBoot/menu-and-router.md`

### 3. 深读代码生成和低代码能力

目标：把 JeecgBoot 最核心的学习价值读出来：从数据库/配置到后端代码、前端页面、在线表单、报表和流程。

优先阅读：

- 代码生成相关模块
- 在线表单/低代码配置模块
- JimuReport / JimuBI 相关集成
- `README-AI.md`
- `jeecgboot-vue3/src`

输出笔记：

- `02-reading-notes/jeecgboot--JeecgBoot/codegen-flow.md`
- `02-reading-notes/jeecgboot--JeecgBoot/online-form-and-report.md`
- `02-reading-notes/jeecgboot--JeecgBoot/ai-skills-and-mcp.md`

## 核心问题清单

- [ ] `jeecg-boot/pom.xml` 的父子模块和依赖管理如何组织？
- [ ] `jeecg-boot-base-core` 和 `jeecg-module-system` 的边界是什么？
- [ ] Shiro + JWT 的认证、鉴权和 Redis 会话如何串起来？
- [ ] 菜单、按钮权限、路由和前端动态页面如何对齐？
- [ ] 代码生成器的输入模型是什么：表结构、在线配置还是模板？
- [ ] 在线表单、流程和报表如何与普通业务表关联？
- [ ] JimuReport / JimuBI 是怎样嵌入后台平台的？
- [ ] AI Skills、MCP 插件、AI Flow 是运行时能力还是开发辅助能力？
- [ ] 它和 RuoYi/Yudao 的代码生成、模块边界、权限模型有什么本质差异？

## 可沉淀模式

后续优先沉淀到 `03-patterns/` 的方向：

- Java 低代码平台的模块边界。
- Shiro + JWT + Redis 的后台认证模型。
- 代码生成和在线配置结合的开发模式。
- 表单、流程、报表一体化后台平台设计。
- AI Skills / MCP 接入传统后台开发平台的方式。
- JeecgBoot 与 RuoYi/Yudao 的低代码路线差异。

## 当前判断

JeecgBoot 适合作为“Java 低代码后台平台”重点学习对象。它和当前已收项目的关系是：

- `ruoyi-vue-pro`：Java 企业后台和业务中台样本。
- `JeecgBoot`：Java 低代码/零代码/AI 辅助后台平台样本。
- `gin-vue-admin`：Go + Vue 后台脚手架样本。
- `ERPNext`：Python/Frappe 元数据驱动 ERP 套件样本。

后续读 JeecgBoot 时，重点不只是 CRUD，而是它如何把代码生成、在线配置、报表、流程和 AI 辅助拼成一个平台。

## 相关笔记

- [[02-reading-notes/jeecgboot--JeecgBoot/README|源码阅读索引]]
- [[05-practice-labs/jeecgboot--JeecgBoot/local-setup|本地运行实验]]
- [[04-comparisons/admin-scaffold-comparison|后台脚手架对比]]
