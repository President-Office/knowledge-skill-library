---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, olap, analytics]
---

# OLAP

## 核心定位

OLAP 是 Online Analytical Processing，中文常译为“联机分析处理”。它关注的是从大量历史数据中快速做分析、统计、报表和指标看板。

一句话理解：

**[[oltp]] 负责记录业务事实，OLAP 负责从业务事实中提炼洞察。**

## 典型问题

OLAP 适合回答这类问题：

- 今年每个月销售额是多少？
- 不同地区、渠道、产品线的利润对比如何？
- 最近 30 天用户留存趋势怎样？
- 某个业务指标按天、按省份、按客户类型聚合后是什么结果？
- 哪些商品、客户、渠道贡献了主要收入？

## 和 OLTP 的关系

[[oltp]] 负责记录业务事实，OLAP 负责从业务事实中提炼洞察。两者的完整对比放在独立卡片：[[oltp-vs-olap]]。

## 为什么 OLAP 通常和业务库分开

交易系统和分析系统的访问模式不同，所以常见做法是：

```text
业务系统 -> OLTP 数据库 -> 同步/ETL -> OLAP 数据库 -> 报表/BI/看板
```

## 在项目中怎么观察

| 项目 | 观察点 |
| --- | --- |
| [[jeecgboot--JeecgBoot]] | 报表 / BI 能力如何从业务数据中提取指标 |
| [[zhijiantianya--ruoyi-vue-pro]] | `report` 模块如何处理报表需求，业务库和分析需求是否分离 |
| [[clickhouse]] | 为什么列式存储适合聚合分析，不适合作为普通交易主库 |

## 不要误解

- OLAP 不是“复杂 SQL”的同义词，它代表一种面向分析的系统目标。
- OLAP 数据库通常不是业务事实的唯一来源，业务事实仍然先由 OLTP 系统记录。
- 报表慢不一定只靠换数据库解决，还要看数据模型、同步链路、分区、预聚合和指标定义。

## 关联

- [[database]]
- [[oltp]]
- [[oltp-vs-olap]]
- [[clickhouse]]
- [[07-foundations/data/databases/README]]
- [[boundaries]]、[[abstractions]]
