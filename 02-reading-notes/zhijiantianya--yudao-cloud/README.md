# yudao-cloud 源码阅读索引

项目主卡：[[zhijiantianya--yudao-cloud]]
特点卡：[[yudao-cloud]]

## 已有笔记

| 顺序 | 主题 | 状态 | 笔记 |
| --- | --- | --- | --- |
| 1 | 微服务模块地图 | 初稿 | [[microservice-module-map]] |

## 后续主题

- Gateway 路由与入口
- Nacos 配置与服务发现
- Gateway 到业务服务的认证链路
- 系统服务、基础设施服务边界
- Seata / MQ / XXL-Job 使用点
- 单体版模块到 Cloud 版模块映射

## 当前问题

- [ ] 本地 clone 后确认使用 `master`、`master-jdk17` 还是 `master-jdk25`。
- [ ] 确认当前推荐 JDK、Maven、Node、Nacos、Redis、数据库版本。
- [ ] 跑通 Nacos、Gateway、后端服务和管理端前端。
- [ ] 建立第一条请求链路：前端请求 -> Gateway -> 服务 -> Security -> Service -> Mapper。
- [ ] 和 [[zhijiantianya--ruoyi-vue-pro]] 做同模块对照。

## 证据记录规范

- 每篇笔记写清楚分支和提交号。
- 涉及 Nacos、Seata、Sentinel、XXL-Job、MQ 时，必须记录配置文件路径。
- 涉及调用链时，至少记录 Controller、Service、Mapper 或远程调用接口。
- 不复制大段源码，只记录路径、类名、方法名和结论。
