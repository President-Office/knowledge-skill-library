---
type: comparison
status: draft
projects:
  - zhijiantianya/ruoyi-vue-pro
  - jeecgboot/JeecgBoot
  - flipped-aurora/gin-vue-admin
  - frappe/erpnext
  - directus/directus
  - payloadcms/payload
created: 2026-07-01
updated: 2026-07-01
---

# 后端项目一对一对比

这份文档用于逐对比较当前知识库已收录的后台/后端/后台平台项目。

## 项目速记

| 简称 | 项目 | 核心定位 | 技术栈 | License |
| --- | --- | --- | --- | --- |
| RuoYi/Yudao | [[01-projects/zhijiantianya--ruoyi-vue-pro|zhijiantianya/ruoyi-vue-pro]] | Java 企业后台 / SaaS / 业务中台 | Spring Boot、MyBatis Plus、Vue | MIT |
| JeecgBoot | [[01-projects/jeecgboot--JeecgBoot|jeecgboot/JeecgBoot]] | Java 低代码 / 零代码 / AI 辅助后台平台 | Spring Boot、MyBatis Plus、Shiro、Vue3 | Apache-2.0 |
| gin-vue-admin | [[01-projects/flipped-aurora--gin-vue-admin|flipped-aurora/gin-vue-admin]] | Go + Vue 后台脚手架 | Gin、GORM、Casbin、JWT、Vue3 | Business Source License 1.1 |
| ERPNext | [[01-projects/frappe--erpnext|frappe/erpnext]] | ERP 业务套件 | Python、Frappe、DocType | GPL-3.0 |
| Directus | [[01-projects/directus--directus|directus/directus]] | 数据库优先 Headless CMS / Admin / API | TypeScript、Vue、Node | MSCL-1.0-GPL |
| Payload | [[01-projects/payloadcms--payload|payloadcms/payload]] | TypeScript / Next.js 全栈后台和 CMS | TypeScript、Next.js | MIT |

## 总体结论

- 如果目标是国内 Java 企业后台：先看 RuoYi/Yudao。
- 如果目标是 Java 低代码、在线表单、报表、AI 生成系统：先看 JeecgBoot。
- 如果目标是 Go 技术栈的后台脚手架：先看 gin-vue-admin。
- 如果目标是完整 ERP、财务、库存、业务单据：先看 ERPNext。
- 如果目标是已有数据库快速变后台和 API：先看 Directus。
- 如果目标是 TypeScript / Next.js 全栈后台和 CMS：先看 Payload。

## RuoYi/Yudao vs JeecgBoot

| 维度 | RuoYi/Yudao | JeecgBoot |
| --- | --- | --- |
| 核心范式 | 企业后台和业务中台脚手架 | 低代码/零代码后台平台 |
| 技术路线 | Spring Boot + MyBatis Plus + 多模块 | Spring Boot + MyBatis Plus + Shiro + 低代码组件 |
| 强项 | 权限、租户、模块化、业务模块丰富 | 在线表单、报表、代码生成、AI Skills、流程编排 |
| 学习重点 | 后台模块边界、RBAC、多租户、业务模块组织 | 低代码平台如何把配置、表单、报表、AI 拼成系统 |
| 取舍 | 更适合学习常规 Java 业务后台 | 更适合学习低代码平台化能力 |

选 RuoYi/Yudao：你要做可控的 Java 后台、SaaS、业务中台，且希望代码层面清晰掌控。

选 JeecgBoot：你更关心低代码、在线配置、报表、表单、AI 生成系统，以及减少重复开发。

## RuoYi/Yudao vs gin-vue-admin

| 维度 | RuoYi/Yudao | gin-vue-admin |
| --- | --- | --- |
| 后端语言 | Java | Go |
| 后端框架 | Spring Boot | Gin |
| 数据访问 | MyBatis Plus | GORM |
| 权限重点 | RBAC、菜单、数据权限、多租户 | JWT、Casbin、动态路由、资源权限 |
| License | MIT | Business Source License 1.1 |

选 RuoYi/Yudao：你在 Java 生态，重视企业后台、复杂业务模块、租户和数据权限。

选 gin-vue-admin：你要学习 Go 后台管理系统，关注 Gin/GORM/Casbin 的工程组织。

## RuoYi/Yudao vs ERPNext

| 维度 | RuoYi/Yudao | ERPNext |
| --- | --- | --- |
| 核心定位 | 后台开发底座 | 完整 ERP 产品 |
| 建模方式 | Java DO/VO/Service/Mapper + SQL | Frappe DocType + Python Controller + JS |
| 业务完整度 | 模块丰富，但偏开发平台 | 财务、库存、采购、销售、制造等闭环成熟 |
| 前后端关系 | 更接近前后端分离 | Frappe 全栈应用，不是典型前后端分离 |
| License | MIT | GPL-3.0 |

选 RuoYi/Yudao：你要学习如何开发后台系统。

选 ERPNext：你要学习真实 ERP 业务、单据生命周期、会计分录、库存流水和 Frappe 元数据模型。

## RuoYi/Yudao vs Directus

| 维度 | RuoYi/Yudao | Directus |
| --- | --- | --- |
| 起点 | 业务代码和模块 | 现有数据库 |
| 产物 | 后端代码、前端页面、业务服务 | Admin、API、权限、SDK |
| 定制方式 | 写 Java/Vue 代码 | 运行时元数据和扩展 |
| 适合场景 | 复杂业务逻辑、企业后台 | 数据管理、内容管理、快速 API |
| License | MIT | MSCL-1.0-GPL |

选 RuoYi/Yudao：业务逻辑重，需要深度定制。

选 Directus：已有数据库，想快速生成后台、API、权限和管理界面。

## RuoYi/Yudao vs Payload

| 维度 | RuoYi/Yudao | Payload |
| --- | --- | --- |
| 技术栈 | Java + Vue | TypeScript + Next.js |
| 建模方式 | Java 分层 + SQL 表 | Collection / Field / Hook / Access 配置 |
| Admin 生成 | 代码生成和前端工程 | 配置驱动 Admin Panel |
| 类型体验 | Java 类型体系 | TypeScript 端到端类型 |
| License | MIT | MIT |

选 RuoYi/Yudao：你要学习国内 Java 后台工程化。

选 Payload：你要学习 TypeScript / Next.js 里如何内嵌后台、CMS、API 和 Admin Panel。

## JeecgBoot vs gin-vue-admin

| 维度 | JeecgBoot | gin-vue-admin |
| --- | --- | --- |
| 核心方向 | Java 低代码平台 | Go 后台脚手架 |
| 强项 | 表单、报表、流程、AI Skills、代码生成 | Go 服务端、Casbin 权限、Gin/GORM 工程结构 |
| 前端 | Vue3 + Ant Design Vue | Vue3 + Element Plus |
| 适合学习 | 低代码平台能力 | Go 后台系统分层 |
| License | Apache-2.0 | Business Source License 1.1 |

选 JeecgBoot：你关注低代码平台、企业后台配置化、报表和 AI 生成。

选 gin-vue-admin：你关注 Go 技术栈和后台脚手架本身。

## JeecgBoot vs ERPNext

| 维度 | JeecgBoot | ERPNext |
| --- | --- | --- |
| 核心定位 | 低代码后台平台 | ERP 业务套件 |
| 建模方式 | 表单/代码生成/在线配置 | DocType 元数据和业务单据 |
| 业务深度 | 适合生成业务系统骨架 | 财务、库存、制造等业务内核成熟 |
| 扩展方式 | Java 模块、在线配置、AI Skills | Frappe app、hooks、patches、DocType |
| License | Apache-2.0 | GPL-3.0 |

选 JeecgBoot：你要研究如何快速生成和配置业务系统。

选 ERPNext：你要研究 ERP 业务规则、单据流转、账务和库存一致性。

## JeecgBoot vs Directus

| 维度 | JeecgBoot | Directus |
| --- | --- | --- |
| 起点 | Java 低代码平台和代码生成 | 现有数据库 |
| 输出 | Java 后端、Vue 前端、在线表单、报表 | Admin、API、权限、SDK |
| 业务逻辑 | 更适合写复杂 Java 业务 | 更适合通用数据管理和 API |
| 使用方式 | 生成/配置后进入代码体系 | 运行时元数据驱动 |
| License | Apache-2.0 | MSCL-1.0-GPL |

选 JeecgBoot：需要复杂业务逻辑、流程报表和 Java 后台二开。

选 Directus：已有数据库，目标是快速获得数据后台和 API。

## JeecgBoot vs Payload

| 维度 | JeecgBoot | Payload |
| --- | --- | --- |
| 技术栈 | Java + Vue3 | TypeScript + Next.js |
| 平台方向 | 低代码/零代码后台平台 | 代码配置型 CMS / 全栈后台框架 |
| 建模方式 | 表单、报表、流程、代码生成 | Collections、Fields、Hooks、Access |
| 适合团队 | Java 企业开发团队 | TypeScript / Next.js 团队 |
| License | Apache-2.0 | MIT |

选 JeecgBoot：你要在 Java 体系内建设低代码后台。

选 Payload：你要在 TS/Next.js 体系内做类型安全后台和 CMS。

## gin-vue-admin vs ERPNext

| 维度 | gin-vue-admin | ERPNext |
| --- | --- | --- |
| 核心定位 | Go 后台脚手架 | ERP 产品 |
| 业务深度 | 通用后台能力 | 财务、库存、销售、采购、制造 |
| 建模方式 | Go model/service/router | Frappe DocType + Document 生命周期 |
| 学习重点 | Gin/GORM/Casbin/JWT | DocType、GL Entry、Stock Ledger、hooks |
| License | Business Source License 1.1 | GPL-3.0 |

选 gin-vue-admin：你要学习 Go 后台系统如何搭。

选 ERPNext：你要学习业务系统如何处理 ERP 级复杂交易。

## gin-vue-admin vs Directus

| 维度 | gin-vue-admin | Directus |
| --- | --- | --- |
| 核心范式 | Go 后台脚手架 | 数据库优先后台平台 |
| 定制方式 | 写 Go/Vue 代码 | 元数据配置和扩展 |
| API | 手写业务 API | 自动生成 REST/GraphQL/API 能力 |
| 适合场景 | 自研后台、Go 服务 | 快速数据后台、内容管理、已有数据库 |
| License | Business Source License 1.1 | MSCL-1.0-GPL |

选 gin-vue-admin：你要掌控 Go 代码和服务结构。

选 Directus：你要快速把数据库包装成后台和 API。

## gin-vue-admin vs Payload

| 维度 | gin-vue-admin | Payload |
| --- | --- | --- |
| 技术栈 | Go + Vue3 | TypeScript + Next.js |
| 后端形态 | 独立 Go API 服务 | Next.js 全栈后台框架 |
| Admin | Vue 管理端 | 内置 Admin Panel |
| 建模 | Go model/service + 前端页面 | Collections/Fields/Hooks |
| License | Business Source License 1.1 | MIT |

选 gin-vue-admin：你要 Go 服务端和前后端分离后台。

选 Payload：你要 TS 全栈、CMS、Admin Panel 和类型安全。

## ERPNext vs Directus

| 维度 | ERPNext | Directus |
| --- | --- | --- |
| 核心定位 | ERP 业务套件 | 数据库优先后台/API |
| 业务模型 | 会计、库存、采购、销售等强业务 | Collections、fields、permissions |
| 数据库关系 | 由 Frappe/ERPNext 业务模型驱动 | 适合接管已有数据库 |
| 学习重点 | 单据生命周期和业务一致性 | 元数据、权限、Admin、API |
| License | GPL-3.0 | MSCL-1.0-GPL |

选 ERPNext：你要学习 ERP 领域业务内核。

选 Directus：你要学习数据库如何产品化为后台和 API。

## ERPNext vs Payload

| 维度 | ERPNext | Payload |
| --- | --- | --- |
| 核心定位 | ERP 产品 | CMS / 全栈后台框架 |
| 技术栈 | Python + Frappe | TypeScript + Next.js |
| 建模方式 | DocType + Controller + hooks | Collection + Fields + Hooks + Access |
| 业务内置 | 强，ERP 模块完整 | 弱，偏框架和 CMS，需要自己建模 |
| License | GPL-3.0 | MIT |

选 ERPNext：你要完整 ERP 业务流程。

选 Payload：你要在 TS/Next.js 中构建自己的后台和 CMS。

## Directus vs Payload

| 维度 | Directus | Payload |
| --- | --- | --- |
| 核心范式 | 数据库优先 | 代码配置优先 |
| 起点 | 已有数据库 schema | TypeScript collections 配置 |
| Admin | 根据元数据和数据库动态生成 | 根据代码配置生成 |
| API | 数据库/权限驱动的即时 API | 配置驱动 REST/GraphQL/SDK |
| License | MSCL-1.0-GPL | MIT |

选 Directus：数据库已经存在，目标是快速变成后台、API、权限和 SDK。

选 Payload：你从应用代码出发，希望 TS 类型、Next.js、Admin、CMS 在一个工程里协同。

## 学习顺序建议

如果按“后台系统能力”学习：

1. [[01-projects/zhijiantianya--ruoyi-vue-pro|RuoYi/Yudao]]
2. [[01-projects/jeecgboot--JeecgBoot|JeecgBoot]]
3. [[01-projects/flipped-aurora--gin-vue-admin|gin-vue-admin]]

如果按“业务平台和元数据”学习：

1. [[01-projects/frappe--erpnext|ERPNext]]
2. [[01-projects/directus--directus|Directus]]
3. [[01-projects/payloadcms--payload|Payload]]

如果按“选型对照”学习：

1. Java 常规后台：[[01-projects/zhijiantianya--ruoyi-vue-pro|RuoYi/Yudao]]
2. Java 低代码：[[01-projects/jeecgboot--JeecgBoot|JeecgBoot]]
3. Go 后台：[[01-projects/flipped-aurora--gin-vue-admin|gin-vue-admin]]
4. ERP 业务套件：[[01-projects/frappe--erpnext|ERPNext]]
5. 数据库优先后台：[[01-projects/directus--directus|Directus]]
6. TS/Next 后台：[[01-projects/payloadcms--payload|Payload]]
