# JeecgBoot 源码阅读索引

项目主卡：[[jeecgboot--JeecgBoot]]
特点卡：[[jeecgboot]]

## 阅读主题网络

| 主题 | 关联源码入口 | 关键概念 |
| --- | --- | --- |
| [[02-reading-notes/jeecgboot--JeecgBoot/maven-module-structure]] | `jeecg-boot/pom.xml`、`jeecg-boot-base-core`、`jeecg-module-system` | [[Maven]]、[[Spring Boot]]、[[module-boundary-design-principles]] |
| [[02-reading-notes/jeecgboot--JeecgBoot/backend-startup-flow]] | `jeecg-boot`、`jeecg-module-system` | [[Spring Boot]]、[[MyBatis Plus]] |
| [[02-reading-notes/jeecgboot--JeecgBoot/auth-shiro-jwt]] | `jeecg-module-system`、`jeecg-boot-base-core` | [[Shiro]]、[[JWT]]、[[RBAC]] |
| [[02-reading-notes/jeecgboot--JeecgBoot/menu-and-router]] | `jeecgboot-vue3/src`、系统菜单模块 | [[Vue Router]]、[[权限模型]] |
| [[02-reading-notes/jeecgboot--JeecgBoot/codegen-flow]] | 代码生成模块、前端页面生成入口 | [[jeecg codegenerate]]、[[代码生成]] |
| [[02-reading-notes/jeecgboot--JeecgBoot/online-form-and-report]] | 在线表单、JimuReport/JimuBI 集成 | [[Form Builder]]、[[JimuReport]]、[[JimuBI]] |
| [[02-reading-notes/jeecgboot--JeecgBoot/ai-skills-and-mcp]] | `README-AI.md`、AI/MCP 相关模块 | [[AI Skills]]、[[MCP]]、[[AI Flow]] |

## 当前问题

- [ ] 本地确认 JDK、Maven、Node、pnpm、数据库版本。
- [ ] 跑通后端 `jeecg-boot`。
- [ ] 跑通前端 `jeecgboot-vue3`。
- [ ] 定位默认登录、菜单加载和权限校验链路。
- [ ] 跑一遍代码生成或在线表单流程。
