---
type: open-source-project
status: active
source: gitee
repo: zhijiantianya/yudao-cloud
homepage: https://gitee.com/zhijiantianya/yudao-cloud
license: MIT
language: Java / TypeScript / Vue
tags: [yudao, ruoyi, spring-cloud, spring-cloud-alibaba, nacos, gateway, microservices, java, vue]
created: 2026-07-01
updated: 2026-07-01
---

# zhijiantianya/yudao-cloud

## 一句话定位

`yudao-cloud` 是芋道源码的 Spring Cloud 微服务版本，和 `ruoyi-vue-pro` 同源，但重点从“单体多模块企业后台”转向“Spring Cloud Alibaba 微服务架构”：网关、注册配置中心、服务治理、分布式事务、定时任务、消息队列和按业务域拆分服务。

## 为什么学它

- 它适合在已经理解 `ruoyi-vue-pro` 单体版后，继续学习国内 Java 微服务后台系统如何拆分。
- 它覆盖 Spring Cloud Alibaba 常见组件：Nacos、Gateway、Sentinel、Seata、XXL-Job、MQ、Redis、Redisson。
- 它保留了 Yudao/RuoYi 的后台业务模块：系统、基础设施、会员、支付、商城、ERP、CRM、BPM、报表、IoT、MES、WMS、IM 等，便于和单体版逐项对照。
- 它适合作为“Java 后台从单体到微服务”的源码阅读样本，而不是单独从零读起。

## 技术栈初判

| 层次 | 技术 |
| --- | --- |
| 微服务基础 | [[Spring Cloud Alibaba]]、[[Nacos]]、[[Spring Cloud Gateway]] |
| 服务治理 | [[Sentinel]]、[[Seata]]、[[XXL-Job]] |
| 后端基础 | [[Spring Boot]]、[[MyBatis Plus]]、[[redis]]、[[Redisson]] |
| 消息 | [[Event]]、[[redis]]、[[RabbitMQ]]、[[Kafka]]、[[RocketMQ]]、[[MQ]] |
| 权限 | [[Spring Security]]、[[Token]]、[[redis]]、[[多端认证]]、[[SSO]] |
| 数据库 | [[mysql]]、[[oracle-database]]、[[postgresql]]、[[sql-server]]、[[mariadb]]、[[dm-database]]、[[tidb]] |
| 业务能力 | [[SaaS]] [[多租户]]、[[BPM]]、[[支付]]、[[Mall]]、[[erp]]、[[crm]]、[[报表]]、[[IoT]]、[[mes]]、[[WMS]]、[[IM]] |
| 前端 | [[Vue]] 管理端生态，和 Yudao 前端项目配合使用 |

## 仓库模块入口

根 `pom.xml` 可见的核心模块：

```text
yudao-cloud/
├── yudao-dependencies
├── yudao-gateway
├── yudao-framework
├── yudao-server
├── yudao-module-system
├── yudao-module-infra
├── yudao-module-member
├── yudao-module-bpm
├── yudao-module-pay
├── yudao-module-report
├── yudao-module-mp
├── yudao-module-mall
├── yudao-module-erp
├── yudao-module-crm
├── yudao-module-iot
├── yudao-module-mes
├── yudao-module-wms
├── yudao-module-im
└── yudao-module-ai
```

`yudao-module-ai` 在 `master` 的 POM 中是注释状态，说明 AI / Spring AI / 大模型支持需要结合 JDK 17 路线单独确认。

## 第一阶段阅读路线

### 1. 先读微服务工程边界

目标：搞清楚它和 `ruoyi-vue-pro` 的差异，不先陷入业务模块细节。

优先阅读：

- 根目录 `pom.xml`
- `yudao-dependencies`
- `yudao-gateway`
- `yudao-server`
- `yudao-framework`

输出笔记：

- `02-reading-notes/zhijiantianya--yudao-cloud/microservice-module-map.md`
- `02-reading-notes/zhijiantianya--yudao-cloud/gateway-routing.md`

### 2. 再读注册、配置、认证链路

目标：把一个后台请求从 Gateway 到业务服务、鉴权、租户、权限校验的路径读清楚。

优先阅读：

- Gateway 路由配置。
- Nacos 配置与服务发现。
- Security / Token / Redis 认证相关框架代码。
- `system` 模块中的用户、角色、菜单、权限接口。

输出笔记：

- `02-reading-notes/zhijiantianya--yudao-cloud/auth-through-gateway.md`
- `02-reading-notes/zhijiantianya--yudao-cloud/nacos-config-map.md`

### 3. 选择一个跨服务业务流程

建议优先读支付、商城或会员，因为它们更容易暴露分布式边界。

候选：

- `yudao-module-pay`：支付订单、回调、退款、通知。
- `yudao-module-mall`：商品、订单、会员、营销。
- `yudao-module-bpm`：流程服务和业务表单之间的调用边界。
- `yudao-module-system` + `yudao-module-infra`：后台基础能力和通用平台能力。

## 核心问题清单

- [ ] `yudao-cloud` 和 `ruoyi-vue-pro` 的模块边界有哪些一一对应关系？
- [ ] Gateway 如何路由到各业务服务？
- [ ] Nacos 中哪些配置是运行必需，哪些只是环境差异？
- [ ] Token、Redis、Spring Security 如何跨网关和服务协同？
- [ ] 多租户、数据权限在微服务拆分后如何传播？
- [ ] Seata 在哪些业务流程中真正介入？
- [ ] MQ、XXL-Job、Sentinel 分别解决什么问题？
- [ ] 单体版业务模块迁移到 Cloud 版时，代码层面改动集中在哪里？

## 可沉淀模式

后续优先沉淀到 `03-patterns/` 的方向：

- Spring Cloud Alibaba 微服务后台工程地图。
- Gateway + Security + Token 的后台认证链路。
- Nacos 配置分层和多环境管理。
- 单体多模块到微服务拆分的边界判断。
- Seata / MQ / XXL-Job 在企业后台中的使用边界。

## 当前判断

`yudao-cloud` 不应该替代 `ruoyi-vue-pro` 作为第一个 Yudao 项目来读。更合理的顺序是：

1. 先用 `ruoyi-vue-pro` 理解 Yudao 的业务模块、RBAC、多租户、代码生成和后台工程风格。
2. 再读 `yudao-cloud`，重点看网关、服务拆分、Nacos、Sentinel、Seata、XXL-Job、MQ。
3. 把同一个业务模块在单体版和 Cloud 版中的差异整理成对比笔记。

## 相关笔记

- [[02-reading-notes/zhijiantianya--yudao-cloud/README]]
- [[05-practice-labs/zhijiantianya--yudao-cloud/local-setup]]
- [[yudao-monolith-vs-cloud]]
- [[zhijiantianya--ruoyi-vue-pro]]
