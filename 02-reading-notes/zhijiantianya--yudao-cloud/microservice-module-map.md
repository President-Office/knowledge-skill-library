---
type: source-reading
status: initial
project: zhijiantianya/yudao-cloud
topic: 微服务模块地图
created: 2026-07-02
updated: 2026-07-02
---

# yudao-cloud - 微服务模块地图

项目主卡：[[zhijiantianya--yudao-cloud]]
特点卡：[[yudao-cloud]]

## 阅读目标

建立 Cloud 版的第一张工程地图，明确它和 [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/maven-module-structure]] 的差异。

## 已确认结构

根 `pom.xml` 中可见的核心模块：

| 层次 | 模块 | 初步职责 |
| --- | --- | --- |
| 依赖管理 | `yudao-dependencies` | 统一依赖版本 |
| 网关入口 | `yudao-gateway` | 统一请求入口、路由、可能承载鉴权前置 |
| 框架能力 | `yudao-framework` | 通用框架封装 |
| 服务聚合 / 管理端 | `yudao-server` | 管理端和 App 服务入口，需要继续确认运行职责 |
| 基础服务 | `yudao-module-system`、`yudao-module-infra` | 权限、菜单、用户、配置、代码生成等基础能力 |
| 业务服务 | `member`、`pay`、`mall`、`bpm`、`crm`、`erp`、`iot`、`mes`、`wms`、`im` | 业务域服务 |
| 可选能力 | `yudao-module-ai` | 在 `master` POM 中为注释状态，需结合 JDK 17 线确认 |

## 与单体版的关键差异

| 维度 | ruoyi-vue-pro | yudao-cloud |
| --- | --- | --- |
| 请求入口 | 后端服务直接承接 | 先经过 `yudao-gateway` |
| 配置方式 | 应用本地配置为主 | Nacos 配置中心是关键依赖 |
| 服务边界 | Maven 模块边界 | 模块边界进一步影响运行时服务边界 |
| 分布式组件 | 不是主线学习点 | Sentinel、Seata、XXL-Job、MQ 是主线学习点 |

## 初步判断

Cloud 版的阅读重点不应该是“业务模块有哪些”，因为这些模块和单体版高度相似。真正要读的是：

- Gateway 如何找到后端服务。
- Nacos 如何组织配置。
- Token、租户、权限如何跨服务传播。
- 哪些业务流程真的使用 Seata、MQ、XXL-Job。

## 读源码时要验证的问题

- `yudao-gateway` 的路由配置来自本地配置还是 Nacos？
- 登录请求从前端到 Gateway 再到系统服务的完整链路是什么？
- `system`、`infra` 是否独立成服务，还是仍由 `yudao-server` 聚合？
- Seata 是否只在少数业务模块启用？
- MQ 事件是框架层封装，还是各模块直接使用？

## Obsidian 关联

- 底层概念：[[boundaries]]、[[abstractions]]、[[solid]]
- 单体版模块地图：[[02-reading-notes/zhijiantianya--ruoyi-vue-pro/maven-module-structure]]
- 框架特点：[[yudao-cloud]]
- 对比文档：[[yudao-monolith-vs-cloud]]
