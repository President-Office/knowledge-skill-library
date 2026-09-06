---
type: source-reading
status: initial
project: zhijiantianya/yudao-cloud
topic: 网关路由
created: 2026-07-02
updated: 2026-07-02
---

# Yudao Cloud - 网关路由

项目主卡：[[zhijiantianya--yudao-cloud]]

## 核心关系

微服务版的请求入口先经过 [[Spring Cloud Gateway]]，再进入具体业务服务。网关是认证、路由、跨域、限流和服务边界的第一观察点。

## 关联源码入口

- `yudao-gateway`
- 网关配置
- Nacos 路由配置

## 关联概念

- [[Spring Cloud Gateway]]
- [[Nacos]]
- [[权限模型]]
- [[API]]
