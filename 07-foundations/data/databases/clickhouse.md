---
type: database
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, olap, clickhouse]
---

# ClickHouse

## 核心定位

ClickHouse 是面向 [[olap]] 的列式分析数据库。它适合大规模聚合查询、报表分析、日志分析和指标查询，不适合作为普通 [[oltp]] 交易系统的主库。

## 适合场景

- 报表、BI、指标看板。
- 大量追加写入、少量更新删除的数据。
- 按时间、维度、指标进行聚合分析。

## 学习重点

| 主题     | 为什么重要               |
| ------ | ------------------- |
| 列式存储   | 解释为什么分析查询快，事务写入不是强项 |
| 分区和排序键 | 决定查询扫描范围和性能         |
| 聚合模型   | 报表系统通常围绕维度和指标设计     |
| 数据同步   | 分析库通常从业务库同步或汇总数据    |

## 在当前项目中观察

- [[jeecgboot--JeecgBoot]] 的报表 / BI 方向可以作为理解分析型数据库需求的入口。
- [[zhijiantianya--ruoyi-vue-pro]] 的 report 模块也可以用来思考业务库和分析库的边界。

## 不要误解

- ClickHouse 不适合替代 MySQL/PostgreSQL 做常规订单、支付、权限等交易系统主库。
- 报表快不只靠数据库，还依赖数据模型、分区、预聚合和同步链路。

## 关联

- [[database]]
- [[oltp]]
- [[olap]]
- [[elasticsearch]]
- [[boundaries]]、[[abstractions]]
