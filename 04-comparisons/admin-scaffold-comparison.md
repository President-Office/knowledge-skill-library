---
type: comparison
status: draft
projects: [zhijiantianya/ruoyi-vue-pro, flipped-aurora/gin-vue-admin, jeecgboot/JeecgBoot]
created: 2026-06-30
updated: 2026-06-30
---

# 后台脚手架对比

## 结论

- 学国内 Java 企业后台：优先读 `zhijiantianya/ruoyi-vue-pro`。
- 学 Java 低代码/零代码/AI 辅助后台平台：重点读 `jeecgboot/JeecgBoot`。
- 学 Go + Vue3 后台管理系统：优先读 `flipped-aurora/gin-vue-admin`。
- 三者都适合学习后台权限、菜单、动态路由、代码生成和前后端分离，但技术栈、工程边界、低代码路线和 license 风险不同。

## 核心差异

| 维度 | RuoYi/Yudao | JeecgBoot | gin-vue-admin |
| --- | --- | --- | --- |
| 主要定位 | Java 企业后台 / SaaS / 业务中台 | Java 低代码 / 零代码 / AI 辅助后台平台 | Go + Vue3 后台管理基础平台 |
| 后端技术 | Spring Boot、MyBatis Plus、Maven 多模块 | Spring Boot、MyBatis Plus、Shiro、JimuReport | Gin、GORM、Viper、Zap |
| 前端技术 | Vue 管理端 | Vue3、Vite、Ant Design Vue | Vite、Vue3、Element Plus |
| 权限 | RBAC、菜单、数据权限、多租户 | Shiro、JWT、菜单、角色、组织 | JWT、Casbin、菜单、动态路由、资源权限 |
| 代码生成 | Java 后端 + 前端页面生成 | 低代码/零代码、在线表单、代码生成、报表 | Go 后端 + Vue 前端生成 |
| AI 辅助 | 当前项目卡未作为重点 | README 强调 AI Skills、知识库、流程编排、MCP 插件 | README 和目录中突出 MCP、skills、AI 辅助 |
| License | MIT | Apache-2.0 | Business Source License 1.1 |

## 后续阅读问题

- [ ] 二者的角色、菜单、API 权限模型有什么差异？
- [ ] RuoYi 的多租户、JeecgBoot 的低代码配置和 gin-vue-admin 的资源权限分别适合什么场景？
- [ ] 三者代码生成器输入模型和模板组织方式有什么差异？
- [ ] 如果做新后台项目，什么时候选 Java 企业后台、Java 低代码平台、Go 轻量后台？
- [ ] Business Source License 1.1 对 gin-vue-admin 的复用边界有什么影响？
