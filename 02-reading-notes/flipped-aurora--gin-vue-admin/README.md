# gin-vue-admin 源码阅读索引

项目主卡：[[flipped-aurora--gin-vue-admin]]
特点卡：[[gin-vue-admin]]

## 阅读主题网络

| 主题 | 关联源码入口 | 关键概念 |
| --- | --- | --- |
| [[go-project-structure]] | `server`、`web` | [[Go]]、[[Gin]]、[[GORM]] |
| [[02-reading-notes/flipped-aurora--gin-vue-admin/server-startup-flow]] | `server/main.go`、`server/core`、`server/initialize` | [[Gin]]、[[Viper]]、[[Zap]]、[[GORM]] |
| [[02-reading-notes/flipped-aurora--gin-vue-admin/auth-rbac-casbin]] | `server/middleware`、`server/model/system`、`server/service/system` | [[JWT]]、[[Casbin]]、[[RBAC]]、[[权限模型]] |
| [[02-reading-notes/flipped-aurora--gin-vue-admin/dynamic-router-permission]] | `web/src/router`、`web/src/permission.js` | [[Vue Router]]、[[RBAC]]、[[权限模型]] |
| [[02-reading-notes/flipped-aurora--gin-vue-admin/codegen-flow]] | `server/service/system`、`web/src/view`、`web/src/api` | [[代码生成]]、[[schema]]、[[API]] |
| [[02-reading-notes/flipped-aurora--gin-vue-admin/form-generator]] | `web/src/components`、`web/src/view` | [[Form Builder]]、[[Element Plus]] |
| [[02-reading-notes/flipped-aurora--gin-vue-admin/ai-assisted-development]] | `AGENT.MD`、`aiDoc`、`server/mcp` | [[AI]]、[[MCP]]、[[AI Skills]] |

## 当前问题

- [ ] 本地 clone 后确认 Go、Node、数据库版本。
- [ ] 跑通 `server`。
- [ ] 跑通 `web`。
- [ ] 确认默认账号、初始化数据和配置方式。
- [ ] 追踪一个登录请求从前端到后端的完整链路。
- [ ] 追踪一个菜单/按钮权限从后端到前端的完整链路。
