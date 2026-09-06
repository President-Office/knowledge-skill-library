# yudao-cloud 源码阅读索引

项目主卡：[[zhijiantianya--yudao-cloud]]
特点卡：[[yudao-cloud]]

## 阅读主题网络

| 主题 | 关联源码入口 | 关键概念 |
| --- | --- | --- |
| [[microservice-module-map]] | 各 `yudao-*` 服务 | [[Spring Cloud]]、[[module-boundary-design-principles]] |
| [[02-reading-notes/zhijiantianya--yudao-cloud/gateway-routing]] | `yudao-gateway`、网关配置 | [[Spring Cloud Gateway]]、[[Nacos]]、[[API]] |
| [[02-reading-notes/zhijiantianya--yudao-cloud/auth-through-gateway]] | Gateway、system 服务、token 配置 | [[Spring Security]]、[[Token]]、[[权限模型]] |
| [[02-reading-notes/zhijiantianya--yudao-cloud/nacos-config-map]] | Nacos 配置、服务注册配置 | [[Nacos]]、[[Spring Cloud Alibaba]]、[[Sentinel]]、[[Seata]] |

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
