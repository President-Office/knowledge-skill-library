---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [database, data-modeling, backend]
---

# 数据库

## 核心定位

数据库不是后台项目的附属品。对大多数后台、[[ERP]]、[[CMS]]、低代码平台来说，数据库是业务事实的长期载体。代码会重构，前端会替换，框架会升级，但数据模型一旦进入生产，迁移成本最高。

## 为什么重要

读后台开源项目时，如果只看 Controller 和页面，很容易错过真正的系统核心。应该追问：

- 业务对象如何落表？
- 表之间的关系如何表达？
- 权限是按用户、角色、字段、行还是租户隔离？
- 历史记录和业务流水是否可追溯？
- Schema 变化如何迁移？

## 常见数据库视角

| 视角 | 关注点 | 典型项目 |
| --- | --- | --- |
| 业务建模 | 表、字段、关系是否表达业务事实 | RuoYi/Yudao、JeecgBoot |
| 元数据驱动 | 数据库结构如何变成后台和 API | Directus |
| 机器可读数据层 | schema、metadata、relationship、permission 如何被 AI 和 Agent 使用 | Directus、Payload、ERPNext |
| 交易流水 | 业务变化如何记录为不可变流水 | ERPNext |
| OLTP 交易 | 业务系统如何记录日常交易和状态变化 | RuoYi/Yudao、ERPNext、JeecgBoot |
| OLAP 分析 | 从历史业务数据中提炼报表、指标和趋势 | JeecgBoot、RuoYi/Yudao Report |
| 多租户 | 租户字段、数据隔离、绕过规则 | RuoYi/Yudao、JeecgBoot、Payload |
| 适配器 | 同一业务模型如何支持多种数据库 | Payload |

## 基础概念索引

| 概念 | 学习重点 |
| --- | --- |
| [[database-basics]] | 从 schema、表、列、行、键、索引、事务建立整体地图 |
| [[sql]] | 如何定义结构、查询数据、修改数据和控制事务 |
| [[orm]] | 对象、类、字段如何映射到表、列、行和 SQL |
| [[schema]] | 数据库对象如何组织，结构定义如何演进 |
| [[table]] | 同一类业务事实如何被集合化保存 |
| [[column]] | 字段名、类型、非空、默认值和约束如何表达业务含义 |
| [[row]] | 一条具体业务事实如何落库 |
| [[primary-key]] | 一行数据如何被唯一识别 |
| [[foreign-key]] | 表之间的关系如何表达 |
| [[database-constraint]] | 数据库如何保护数据合法性 |
| [[database-index]] | index 如何用额外结构更快定位数据 |
| [[database-transaction]] | 多个读写操作如何保持一致 |

## 常用数据库索引

| 类型     | 数据库             | 核心定位                    | 笔记                  |
| ------ | --------------- | ----------------------- | ------------------- |
| 关系型    | MySQL           | Web 后台最常见的通用关系型数据库      | [[mysql]]           |
| 关系型    | PostgreSQL      | 功能完整、类型系统强、扩展能力强的关系型数据库 | [[postgresql]]      |
| 关系型    | SQLite          | 嵌入式、单文件、轻量数据库           | [[sqlite]]          |
| 关系型    | MariaDB         | MySQL 生态兼容路线的关系型数据库     | [[mariadb]]         |
| 商业关系型  | Oracle Database | 企业级商业关系型数据库             | [[oracle-database]] |
| 商业关系型  | SQL Server      | Microsoft 生态的企业级关系型数据库  | [[sql-server]]      |
| 分布式关系型 | TiDB            | MySQL 协议兼容的分布式 SQL 数据库  | [[tidb]]            |
| 国产关系型  | 达梦 DM           | 国产化和信创场景常见关系型数据库        | [[dm-database]]     |
| 文档型    | MongoDB         | 面向文档的 NoSQL 数据库         | [[mongodb]]         |
| 键值/缓存  | Redis           | 内存键值数据库，常用于缓存、会话、锁和队列辅助 | [[redis]]           |
| 搜索     | Elasticsearch   | 面向搜索和日志检索的分布式搜索引擎       | [[elasticsearch]]   |
| 分析型    | ClickHouse      | 面向 [[olap]] 的列式分析数据库    | [[clickhouse]]      |

更完整的数据库卡片索引：[[07-foundations/data/databases/README]]

## 在项目中怎么观察

| 项目 | 数据库学习点 |
| --- | --- |
| [[directus--directus]] | 现有数据库 schema 如何变成 collections、fields、relations 和权限 |
| [[frappe--erpnext]] | GL Entry、Stock Ledger Entry 等流水如何保证业务一致性 |
| [[zhijiantianya--ruoyi-vue-pro]] | RBAC、多租户、代码生成如何依赖表结构 |
| [[jeecgboot--JeecgBoot]] | 在线表单、报表、代码生成如何绑定业务表 |
| [[payloadcms--payload]] | collection 配置如何映射到不同数据库适配器 |

## 不要误解

- 数据库不是“只要能存就行”，它表达了业务边界和长期约束。
- [[orm]] 不是数据库设计的替代品。
- 数据库优先不等于没有业务逻辑，代码优先也不等于可以忽略数据模型。

## 关联

- [[07-foundations/data/databases/README]]
- [[database-basics]]
- [[sql]]
- [[orm]]
- [[machine-readable-software-systems]]
- [[schema]]
- [[table]]
- [[primary-key]]
- [[database-index]]
- [[database-transaction]]
- [[oltp]]
- [[olap]]
- [[headless-cms]]
- [[boundaries]]、[[abstractions]]
- [[directus]]
- [[erpnext]]
