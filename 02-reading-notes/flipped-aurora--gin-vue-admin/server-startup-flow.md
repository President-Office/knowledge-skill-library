---
type: source-reading
status: initial
project: flipped-aurora/gin-vue-admin
topic: 后端启动链路
created: 2026-07-02
updated: 2026-07-02
---

# gin-vue-admin - 后端启动链路

项目主卡：[[flipped-aurora--gin-vue-admin]]

## 核心关系

`server/main.go` 是理解 gin-vue-admin 的第一入口。启动链路把 [[Viper]] 配置、[[Zap]] 日志、[[GORM]] 数据库、定时任务、路由和中间件串到 [[Gin]] 服务中。

## 关联源码入口

- `server/main.go`
- `server/core`
- `server/initialize`
- `server/router`
- `server/middleware`

## 关联概念

- [[Gin]]
- [[Viper]]
- [[Zap]]
- [[GORM]]
- [[database-transaction]]
