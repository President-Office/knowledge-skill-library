---
type: pattern-index
status: draft
created: 2026-07-02
updated: 2026-07-02
---

# 框架特点总览

这个目录用于快速理解当前知识库已收录框架的核心特点。每张卡片回答三个问题：

- 这个框架最突出的特点是什么？
- 适合学习什么能力？
- 不适合把它误解成什么？

## 后端 / 后台平台

| 框架 | 核心特点 | 适合学习 | 特点卡 |
| --- | --- | --- | --- |
| RuoYi/Yudao | 国内 [[Java]] 企业后台和业务中台样本 | [[RBAC]]、[[多租户]]、[[代码生成]]、业务模块化 | [[ruoyi-vue-pro]] |
| Yudao Cloud | Yudao 体系的 [[Spring Cloud]] 微服务版本 | [[Spring Cloud Gateway]]、[[Nacos]]、服务治理、分布式组件 | [[yudao-cloud]] |
| ERPNext | 基于 [[Frappe Framework]] 的完整 ERP 业务套件 | [[DocType]]、业务单据、账务和库存闭环 | [[erpnext]] |
| gin-vue-admin | [[Go]] + [[Vue]] 前后端分离后台脚手架 | [[Gin]]、[[GORM]]、[[Casbin]]、[[JWT]]、[[代码生成]] | [[gin-vue-admin]] |
| JeecgBoot | [[Java]] AI 低代码 / 零代码后台平台 | 在线表单、[[报表]]、[[工作流]]、[[代码生成]]、[[AI Skills]] | [[jeecgboot]] |
| Directus | 数据库优先 [[headless-cms]] / [[Admin Panel]] / [[API]] 平台 | [[Metadata]]、[[权限模型]]、[[Instant API]]、[[Admin App]] | [[directus]] |
| Payload | [[TypeScript]] / [[Next.js]] 全栈后台与 CMS 框架 | Collection 配置、[[Admin Panel]]、[[插件体系]]、[[数据库适配器]] | [[payload]] |

## 前端后台框架

| 框架 | 核心特点 | 适合学习 | 特点卡 |
| --- | --- | --- | --- |
| yudao-ui-admin-vue3 | Yudao 单应用 [[Vue 3]] 管理端 | 业务页面组织、权限路由、[[Element Plus]] 后台页面 | [[yudao-ui-admin-vue3]] |
| yudao-ui-admin-vben | 基于 [[Vben Admin]] 的平台化前端底座 | [[monorepo]]、多 UI app、共享 packages、偏好配置 | [[yudao-ui-admin-vben]] |

## 快速选择

| 目标 | 优先看 |
| --- | --- |
| 学国内 Java 常规企业后台 | [[ruoyi-vue-pro]] |
| 学 Java 微服务后台 | [[yudao-cloud]] |
| 学 Java 低代码平台 | [[jeecgboot]] |
| 学 Go 后台脚手架 | [[gin-vue-admin]] |
| 学完整 ERP 业务系统 | [[erpnext]] |
| 已有数据库要快速变后台/API | [[directus]] |
| [[TypeScript]] / [[Next.js]] 项目要内嵌后台和 CMS | [[payload]] |
| 快速二开 Yudao 管理端页面 | [[yudao-ui-admin-vue3]] |
| 评估长期后台前端平台底座 | [[yudao-ui-admin-vben]] |

## 底层概念入口

- [[architecture-as-wedge]]
- [[solid]]
- [[boundaries]]、[[abstractions]]
- [[database]]
- [[monorepo]]
- [[headless-cms]]
