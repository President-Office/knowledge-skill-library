---
type: comparison
status: draft
projects:
  - zhijiantianya/ruoyi-vue-pro
  - zhijiantianya/yudao-cloud
created: 2026-07-01
updated: 2026-07-01
---

# Yudao 单体版与 Cloud 版对比

## 结论

先读 [[zhijiantianya--ruoyi-vue-pro]]，再读 [[zhijiantianya--yudao-cloud]]。

`ruoyi-vue-pro` 更适合作为 Yudao/RuoYi 的第一份源码样本，因为它部署简单、模块边界集中、业务代码路径更短。`yudao-cloud` 更适合作为第二阶段，用来学习同一套后台业务能力如何放进 Spring Cloud Alibaba 微服务体系。

## 一对一差异

| 维度 | ruoyi-vue-pro | yudao-cloud |
| --- | --- | --- |
| 架构形态 | 单体多模块后台 | Spring Cloud 微服务后台 |
| 学习重点 | Maven 多模块、RBAC、多租户、代码生成、业务模块 | Gateway、Nacos、服务拆分、Sentinel、Seata、XXL-Job、MQ |
| 启动复杂度 | 较低，核心是后端服务、前端、数据库、Redis | 较高，需要网关、注册配置中心和多个服务 |
| 调用链长度 | Controller -> Service -> Mapper 为主 | Gateway -> 服务 -> 安全认证 -> 业务服务，可能有远程调用 |
| 服务边界 | 模块边界主要在代码和 Maven 依赖中 | 模块边界进一步变成服务边界和运行时边界 |
| 运维关注 | 单应用配置、数据库、Redis、前端部署 | 注册发现、配置中心、网关路由、服务治理、链路排查 |
| 适合阶段 | 第一阶段建立 Yudao 业务地图 | 第二阶段学习微服务化落地 |

## 共同点

- 都来自芋道源码 / Yudao / RuoYi 生态。
- 都围绕企业后台、SaaS、多租户、权限、支付、商城、CRM、ERP、BPM、报表等业务模块组织。
- 都适合学习国内 Java 中后台项目的模块命名、Controller / Service / Mapper 分层、VO/DO 使用习惯和业务扩展方式。

## Cloud 版新增学习点

| 新增点 | 为什么重要 |
| --- | --- |
| `yudao-gateway` | 统一入口、路由、鉴权前置、跨服务访问的第一站 |
| Nacos | 服务注册发现和配置中心，是本地运行 Cloud 版的关键依赖 |
| Sentinel | 学习限流、熔断、服务保护在后台系统中的接入方式 |
| Seata | 学习分布式事务是否真的适合复杂业务流程 |
| XXL-Job | 学习后台系统定时任务从单体到平台化调度的变化 |
| MQ | 学习异步事件、解耦和最终一致性在业务模块里的实际使用点 |

## 选择建议

选 `ruoyi-vue-pro`：

- 你要快速跑起来并开始读源码。
- 你主要关心 Java 企业后台、权限、租户、代码生成和业务模块。
- 你暂时不想把精力消耗在微服务环境依赖上。

选 `yudao-cloud`：

- 你已经知道 Yudao 单体版的大致业务地图。
- 你要学习 Spring Cloud Alibaba 微服务工程组织。
- 你要研究网关、注册配置中心、分布式事务、任务调度、消息队列和服务治理。

## 后续笔记方向

- 同一登录请求在两个版本中的调用链对比。
- 同一支付模块在两个版本中的服务边界对比。
- 单体版 `yudao-server` 与 Cloud 版 `yudao-gateway` / `yudao-server` 的职责差异。
- Nacos 配置如何影响本地运行和多环境部署。

