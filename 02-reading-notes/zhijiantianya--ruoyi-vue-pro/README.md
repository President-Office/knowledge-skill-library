# ruoyi-vue-pro 源码阅读索引

项目主卡：[[zhijiantianya--ruoyi-vue-pro]]
特点卡：[[ruoyi-vue-pro]]

## 阅读主题网络

| 主题 | 关联源码入口 | 关键概念 |
| --- | --- | --- |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/maven-module-structure]] | 根 `pom.xml`、`yudao-framework`、`yudao-module-*` | [[Maven]]、[[module-boundary-design-principles]] |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/startup-flow]] | `yudao-server`、`yudao-framework` | [[Spring Boot]]、[[MyBatis Plus]] |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/rbac-and-menu]] | `yudao-module-system`、`yudao-ui` | [[RBAC]]、[[权限模型]]、[[Vue Router]] |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/tenant-model]] | 租户相关拦截器、配置和表结构 | [[多租户]]、[[SaaS]]、[[数据权限]] |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/codegen-flow]] | `yudao-module-infra`、代码生成入口 | [[代码生成]]、[[schema]] |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/business-module-flow]] | `pay`、`mall`、`bpm`、`crm` 模块 | [[支付]]、[[Mall]]、[[工作流]]、[[crm]] |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/data-model-and-table-relations]] | `sql`、各模块 DO/Mapper | [[database]]、[[schema]]、[[orm]] |
| [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/api-service-mapper-path]] | Controller、Service、Mapper | [[API]]、[[boundaries]]、[[abstractions]] |

## 当前问题

- [ ] 本地 clone 后确认分支选择：`master`、`master-jdk17` 还是 `master-jdk25`。
- [ ] 确认当前推荐 JDK、Node、数据库版本。
- [ ] 运行后端服务和前端管理端。
- [ ] 建立第一张调用链笔记。
