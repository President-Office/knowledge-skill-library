---
type: framework-characteristics
status: draft
project: zhijiantianya/yudao-cloud
created: 2026-07-02
updated: 2026-07-02
---

# Yudao Cloud 特点

项目主卡：[[zhijiantianya--yudao-cloud]]

## 核心定位

Yudao/RuoYi 体系的 [[Spring Cloud]] 微服务版本。它保留单体版的后台业务模块，但把学习重点转向 Gateway、Nacos、服务拆分、服务治理、分布式事务、任务调度和 [[MQ]]。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| [[Spring Cloud Alibaba]] 体系 | [[Nacos]]、[[Spring Cloud Gateway]]、[[Sentinel]]、[[Seata]] 等组件成体系出现 | 学国内 [[Java]] 微服务后台常见技术栈 |
| [[Spring Cloud Gateway]] 统一入口 | 请求先经过网关再进入业务服务 | 学路由、鉴权前置、跨服务调用入口 |
| [[Nacos]] 注册配置 | 服务发现和配置管理是运行基础 | 学多服务环境配置和本地调试依赖 |
| 分布式组件齐全 | [[Seata]]、[[XXL-Job]]、[[MQ]]、[[Sentinel]] | 学分布式事务、定时任务、异步消息、限流熔断的边界 |
| 与单体版同源 | 业务模块和 `ruoyi-vue-pro` 有可比性 | 很适合做“单体到微服务”的一对一对照 |
| 多 JDK 主线 | `master`、`master-jdk17`、`master-jdk25` 对应不同技术基线 | 学版本路线和升级策略 |

## 最适合怎么读

1. 先读 `yudao-gateway`、根 `pom.xml`、`yudao-server`。
2. 再读 [[Nacos]] 配置、认证链路、服务注册和路由规则。
3. 选择一个业务模块，和 `ruoyi-vue-pro` 单体版做同模块对比。

## 不要误解

- 不适合作为 Yudao 的第一个项目直接读，环境和链路复杂度更高。
- 不要只看业务代码，Cloud 版的学习重点在运行时边界和分布式基础设施。
- 不要默认所有分布式组件都必须在自己的项目中引入，应先确认业务是否真的需要。

## 关联

- [[boundaries]]、[[abstractions]]
- [[solid]]
- [[ruoyi-vue-pro]]
- [[yudao-monolith-vs-cloud]]
- [[pairwise-backend-comparisons]]
