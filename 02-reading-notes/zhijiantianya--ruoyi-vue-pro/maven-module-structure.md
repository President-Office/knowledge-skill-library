---
type: source-reading
status: initial
project: zhijiantianya/ruoyi-vue-pro
topic: Maven 多模块结构
created: 2026-07-02
updated: 2026-07-02
---

# ruoyi-vue-pro - Maven 多模块结构

项目主卡：[[zhijiantianya--ruoyi-vue-pro]]
特点卡：[[ruoyi-vue-pro]]

## 阅读目标

先建立工程地图，弄清楚哪些模块是框架层、哪些是启动层、哪些是业务模块。后续读权限、租户、代码生成和支付模块时，才不会在目录里迷路。

## 已确认结构

根据项目主卡中记录的仓库顶层目录，`ruoyi-vue-pro` 的核心结构可以先分成四层：

| 层次 | 目录 | 初步职责 |
| --- | --- | --- |
| 依赖管理 | `yudao-dependencies` | 统一管理 Spring Boot、MyBatis Plus、三方组件版本 |
| 框架能力 | `yudao-framework` | 通用配置、Web、安全、数据权限、租户、Redis、工具封装 |
| 启动聚合 | `yudao-server` | 后端启动入口，聚合系统和业务模块 |
| 业务模块 | `yudao-module-*` | system、infra、member、pay、mall、bpm、crm、erp 等业务域 |
| 前端入口 | `yudao-ui` | 管理后台前端工程 |

## 初步判断

`ruoyi-vue-pro` 不是把所有代码放进一个 `src/main/java` 的普通单体应用，而是“单体运行 + Maven 多模块组织”。这意味着：

- 运行时可以是一个后端服务。
- 开发时按模块分层，业务边界比普通单体清楚。
- 框架层能力会被多个业务模块复用。
- 读源码时要从根 `pom.xml` 和模块依赖关系开始，而不是直接进入某个 Controller。

## 读源码时要验证的问题

- 根 `pom.xml` 的 `<modules>` 顺序是否反映依赖方向？
- `yudao-framework` 是否被所有业务模块依赖？
- `yudao-server` 是如何引入 `yudao-module-system`、`yudao-module-infra` 和业务模块的？
- `system` 与 `infra` 的边界是什么：哪些是业务后台基础能力，哪些是平台基础设施？
- 业务模块之间是否直接互相依赖，还是通过 API / Service 抽象隔离？

## Obsidian 关联

- 底层概念：[[solid]]、[[database]]、[[boundaries]]、[[abstractions]]
- 对比 Cloud 版：[[microservice-module-map]]
- 框架特点：[[ruoyi-vue-pro]]
- 单体 vs Cloud：[[yudao-monolith-vs-cloud]]
