---
type: framework-characteristics
status: draft
project: zhijiantianya/ruoyi-vue-pro
created: 2026-07-02
updated: 2026-07-02
---

# RuoYi/Yudao 特点

项目主卡：[[zhijiantianya--ruoyi-vue-pro]]

## 核心定位

国内 Java 企业后台 / [[SaaS]] / 业务中台样本。它的价值不只是 CRUD 脚手架，而是把 [[权限模型]]、[[多租户]]、[[代码生成]]、[[工作流]]、支付、商城、[[crm]]、[[erp]] 等能力放进一个 [[Spring Boot]] + [[MyBatis Plus]] 的多模块工程里。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| Maven 多模块边界 | `yudao-framework`、`yudao-server`、多个 `yudao-module-*` 分层明显 | 学 Java 后台如何拆框架层、启动层和业务模块 |
| [[RBAC]] + 菜单权限 | 用户、角色、菜单、按钮权限是后台系统基础能力 | 可作为企业后台权限模型样本 |
| [[多租户]]和[[数据权限]] | [[SaaS]] 后台常见隔离能力 | 学租户字段、权限过滤、绕过机制 |
| 代码生成器 | 从表结构生成后端、前端和基础 CRUD | 学低代码/[[代码生成]]的工程入口 |
| 业务模块丰富 | 支付、商城、CRM、ERP、BPM、报表、会员等 | 比纯脚手架更接近真实业务系统 |
| 国内生态贴近度高 | 命名、技术栈、业务模块符合国内中后台项目习惯 | 适合作为国内 Java 项目阅读基准 |

## 最适合怎么读

1. 先读根 `pom.xml`、`yudao-framework`、`yudao-server`。
2. 再读 `system` 和 `infra`，建立权限、菜单、租户、代码生成的基础地图。
3. 选择一个业务模块深读，优先 `pay`、`mall`、`bpm` 或 `crm`。

## 不要误解

- 不要把它只当普通 RuoYi CRUD 脚手架，它更像业务中台样本库。
- 不要一上来读所有模块，模块太多，应该按“基础能力 -> 一个业务闭环”的顺序读。
- 不要直接假设所有模块都适合复制到自己的项目，很多模块更适合参考模式。

## 关联

- [[solid]]
- [[database]]
- [[boundaries]]、[[abstractions]]
- [[yudao-cloud]]
- [[yudao-monolith-vs-cloud]]
- [[admin-scaffold-comparison]]
