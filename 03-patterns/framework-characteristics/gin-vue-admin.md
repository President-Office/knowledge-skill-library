---
type: framework-characteristics
status: draft
project: flipped-aurora/gin-vue-admin
created: 2026-07-02
updated: 2026-07-02
---

# gin-vue-admin 特点

项目主卡：[[flipped-aurora--gin-vue-admin]]

## 核心定位

[[Go]] + [[Vue 3]] 的前后端分离后台脚手架。它适合学习 Go 生态如何组织后台管理系统：[[Gin]] 路由、[[GORM]] 数据访问、[[Casbin]] 权限、[[JWT]] 登录、[[Vue]] 管理端和 [[代码生成]]。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| Go 后台工程分层 | `server/api`、`router`、`service`、`model`、`middleware` 等目录清楚 | 学 Go 后台项目结构 |
| [[Gin]] + [[GORM]] | 轻量 Web 框架和 [[orm]] 组合 | 学 [[Go]] Web 常见技术栈 |
| [[Casbin]] + [[JWT]] 权限 | API 权限、角色权限、动态路由协同 | 学 [[Go]] 后台权限模型 |
| 前后端分离 | `server` 和 `web` 分离明显 | 适合和 Java 后台脚手架对照 |
| [[代码生成]] / 表单生成 | 提供后台开发提效能力 | 学 Go 体系里的 CRUD 生成方案 |
| AI/[[MCP]] 辅助痕迹 | 仓库包含 [[MCP]]、[[AI Skills]]、AI 文档等辅助能力 | 观察传统后台脚手架如何接入 AI 开发资产 |

## 最适合怎么读

1. 从 `server/main.go` 追启动链路。
2. 读 `initialize`、`core`、`router`、`middleware` 建立后端地图。
3. 读 [[JWT]]、[[Casbin]]、动态路由和前端 `permission.js`。
4. 再读代码生成和表单生成。

## 不要误解

- 不要把它当 ERP 或低代码平台，它主要是 Go 后台脚手架。
- 不要忽略 Business Source License 1.1，商用或二次分发要评估。
- 不要只读前端页面，Go 后端启动和权限链路才是它的核心学习点。

## 关联

- [[solid]]
- [[boundaries]]、[[abstractions]]
- [[admin-scaffold-comparison]]
- [[pairwise-backend-comparisons]]
