---
type: source-reading
status: initial
project: flipped-aurora/gin-vue-admin
topic: 动态路由与权限
created: 2026-07-02
updated: 2026-07-02
---

# gin-vue-admin - 动态路由与权限

项目主卡：[[flipped-aurora--gin-vue-admin]]

## 核心关系

前端动态路由要和后端菜单、角色、API 权限对齐。它不是单纯的 Vue Router 配置，而是后台 [[权限模型]] 在 [[Vue]] 管理端的投影。

## 关联源码入口

- `web/src/router`
- `web/src/permission.js`
- `server/service/system`

## 关联概念

- [[Vue Router]]
- [[RBAC]]
- [[权限模型]]
- [[API]]
