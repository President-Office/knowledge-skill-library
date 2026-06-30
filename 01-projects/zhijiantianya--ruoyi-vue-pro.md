---
type: open-source-project
status: active
source: gitee
repo: zhijiantianya/ruoyi-vue-pro
homepage: https://gitee.com/zhijiantianya/ruoyi-vue-pro
license: MIT
language: Java / TypeScript / Vue
tags: [ruoyi, yudao, spring-boot, mybatis-plus, vue, admin, saas, workflow]
created: 2026-06-30
updated: 2026-06-30
---

# zhijiantianya/ruoyi-vue-pro

## 一句话定位

`ruoyi-vue-pro` 是芋道源码维护的企业级后台管理系统与业务中台脚手架，核心价值是把 Spring Boot、MyBatis Plus、Vue 管理端、权限体系、多租户、工作流、支付、商城、CRM、ERP、MES、IM、IoT、AI 等模块放在一个可二次开发的工程体系里。

## 为什么学它

- 它是国内 Java 后台管理系统生态中非常典型的工程样本，适合学习企业后台的模块拆分、权限模型、代码生成、租户隔离、业务模块扩展方式。
- 它比普通脚手架更接近真实业务系统：不仅有系统管理，还有支付、商城、会员、CRM、ERP、流程、报表等模块。
- 它适合作为以后阅读国内 Java SaaS / 中后台 / 低代码 / 业务平台项目的基准参照。
- 当前知识库后续可以围绕它沉淀一批可复用模式：RBAC、数据权限、多租户、代码生成、模块化 Maven、后台前端组织、业务插件边界。

## 当前快照

查询日期：2026-06-30

| 项 | 内容 |
| --- | --- |
| 仓库 | https://gitee.com/zhijiantianya/ruoyi-vue-pro |
| 平台 | Gitee |
| 所属 | 芋道源码 |
| 分类 | Web Development / Backend Management |
| License | MIT |
| 默认分支 | `master` |
| 分支 | 远程验证 9 个分支：`develop`、`feat/iot-2026`、`feature/dev-yunai`、`feature/im-dev`、`master`、`master-dm8-jdk17`、`master-jdk17`、`master-jdk17-bpm-bug-fix`、`master-jdk25` |
| 标签 | Gitee 仓库页显示 64 个标签，远程引用可见 `v2026.06(jdk8/11)`、`v2026.06(jdk17/21)`、`v2026.06(jdk25)` |
| 规模 | Gitee 页面显示约 111.2K Star、19.9K Fork、11,604 commits |
| 当前主干提交 | `81c976551fceada9153027e87013bdabc7cb7095` |
| Issues / PR | Gitee 页面显示 Issues 0、Pull Requests 6 |

注意：这些数字是 Gitee 页面在 2026-06-30 的展示快照，后续会变化。

## 技术栈初判

| 层次 | 技术 |
| --- | --- |
| 后端 | Spring Boot、MyBatis Plus、Maven 多模块 |
| 前端 | Vue、Element 系列后台管理界面 |
| 权限 | RBAC、数据权限 |
| 平台能力 | SaaS 多租户、三方登录、支付、工作流、报表 |
| 业务模块 | Mall、Member、CRM、ERP、MES、WMS、MP、IM、IoT、AI |

## 仓库目录入口

从 Gitee 页面可见的顶层目录：

```text
ruoyi-vue-pro/
├── .gitee
├── .github
├── .image
├── script
├── sql
├── yudao-dependencies
├── yudao-framework
├── yudao-module-ai
├── yudao-module-bpm
├── yudao-module-crm
├── yudao-module-erp
├── yudao-module-im
├── yudao-module-infra
├── yudao-module-iot
├── yudao-module-mall
├── yudao-module-member
├── yudao-module-mes
├── yudao-module-mp
├── yudao-module-pay
├── yudao-module-report
├── yudao-module-system
├── yudao-module-wms
├── yudao-server
├── yudao-ui
├── LICENSE
├── README.md
├── lombok.config
└── pom.xml
```

## 第一阶段阅读路线

### 1. 先读工程边界

目标：搞清楚 Maven 多模块如何组织，哪些是框架层，哪些是业务模块，启动入口在哪里。

优先阅读：

- 根目录 `pom.xml`
- `yudao-dependencies`
- `yudao-framework`
- `yudao-server`
- `yudao-ui`

输出笔记：

- `02-reading-notes/zhijiantianya--ruoyi-vue-pro/maven-module-structure.md`
- `02-reading-notes/zhijiantianya--ruoyi-vue-pro/startup-flow.md`

### 2. 再读系统基础能力

目标：把后台管理系统最核心的权限、租户、菜单、用户、部门、岗位、字典、操作日志等基础能力读清楚。

优先阅读：

- `yudao-module-system`
- `yudao-module-infra`
- `yudao-framework`

输出笔记：

- `02-reading-notes/zhijiantianya--ruoyi-vue-pro/rbac-and-menu.md`
- `02-reading-notes/zhijiantianya--ruoyi-vue-pro/tenant-model.md`
- `02-reading-notes/zhijiantianya--ruoyi-vue-pro/codegen-flow.md`

### 3. 选择一个业务模块深读

建议先从 `pay` 或 `mall` 选一个，因为它们比纯系统模块更接近真实业务流程。

候选：

- `yudao-module-pay`：支付渠道、支付订单、回调、退款、通知。
- `yudao-module-mall`：商品、订单、会员、营销。
- `yudao-module-bpm`：Flowable 工作流接入。
- `yudao-module-crm`：业务对象、跟进、客户关系。

输出笔记：

- 业务模块主流程调用链。
- 数据模型和表关系。
- API 到 Service 到 Mapper 的路径。
- 可复用到自己项目的工程模式。

## 核心问题清单

- [ ] 根 `pom.xml` 如何组织模块依赖？
- [ ] `yudao-framework` 和各业务模块之间的边界是什么？
- [ ] 后端启动入口和自动配置链路是什么？
- [ ] RBAC 的用户、角色、菜单、权限标识如何关联？
- [ ] 数据权限是通过 AOP、SQL 拼接、Mapper 拦截还是业务手写实现？
- [ ] 多租户字段如何注入、过滤和绕过？
- [ ] 代码生成器如何从表结构生成 Controller、Service、Mapper、VO、前端页面？
- [ ] 前端菜单、路由、权限按钮如何和后端权限体系对齐？
- [ ] 支付模块的订单、渠道、回调、退款如何建模？
- [ ] 哪些模块适合直接复用，哪些只适合作为参考？

## 可沉淀模式

后续优先沉淀到 `03-patterns/` 的方向：

- Java 后台 Maven 多模块边界设计。
- RuoYi/Yudao 风格的 Controller / Service / Mapper / VO 分层。
- RBAC 与菜单权限模型。
- 数据权限与多租户隔离。
- 代码生成器的输入输出模型。
- 支付模块的渠道适配器设计。
- 后台管理前端的动态路由和按钮权限。

## 当前判断

这个项目适合长期作为“国内 Java 企业后台系统样本库”来读，不适合一次性从头读到尾。更好的学习方式是：

1. 先建立工程地图。
2. 读透系统基础模块。
3. 选择一个业务模块深挖。
4. 把每个模块的模式抽到 `03-patterns/`。
5. 和 ERPNext、Directus、Baserow、Supabase 等项目做横向比较，形成后台系统/业务平台选型判断。

## 相关笔记

- [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/README|源码阅读索引]]
- [[05-practice-labs/zhijiantianya--ruoyi-vue-pro/local-setup|本地运行实验]]
