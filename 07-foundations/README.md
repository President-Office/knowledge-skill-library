---
type: foundation-index
status: draft
created: 2026-07-02
updated: 2026-07-02
---

# Foundations

这一层不是项目索引，也不是术语表。它用来沉淀更底层、可迁移的工程思想和基础概念。

架构是楔子，不是目的。我们通过架构进入问题，但最后要理解的是：为什么要分层、为什么要抽象、为什么要隔离变化、为什么要把数据建模清楚、为什么工程组织会影响认知成本。

## 学习路线

| 层次 | 关注问题 | 笔记 |
| --- | --- | --- |
| 工程思想 | 如何判断代码和模块是否容易变化、扩展、测试 | [[solid]] |
| 单一职责 | 一个模块应该只有一个主要变化原因 | [[single-responsibility-principle]] |
| 模块边界设计 | 什么时候放在一个模块里，什么时候拆成模块、服务或仓库 | [[module-boundary-design-principles]] |
| 开闭原则 | 如何让新增能力尽量通过扩展完成 | [[open-closed-principle]] |
| 里氏替换 | 子类型如何可靠替换父类型 | [[liskov-substitution-principle]] |
| 接口隔离 | 如何避免接口强迫调用方依赖不用的方法 | [[interface-segregation-principle]] |
| 依赖倒置 | 如何让核心业务依赖抽象而不是基础设施细节 | [[dependency-inversion-principle]] |
| LSP 与 DIP | 为什么依赖抽象和可靠替换不矛盾 | [[lsp-vs-dip]] |
| AI 时代的设计尺度 | AI 降低实现成本后，如何在设计质量和不过度设计之间取舍 | [[ai-era-engineering-design-scale]] |
| 机器可理解的软件系统 | 为什么实现会变便宜，而机器可读元数据、数据层和工作流会变贵 | [[machine-readable-software-systems]] |
| 架构观 | 为什么架构只是理解系统的入口，不是学习终点 | [[architecture-as-wedge]] |
| 边界 | 什么应该放在一起，什么应该隔离 | [[boundaries]] |
| 抽象 | 调用方应该依赖什么稳定概念，而不是依赖哪些易变细节 | [[abstractions]] |
| 面向对象抽象 | 封装、继承、多态和抽象之间是什么关系 | [[object-oriented-abstraction]] |
| 面向对象起点 | 从结构体、类到运行时对象如何演化 | [[from-struct-to-class]] |
| 结构体 | 如何把相关字段组织在一起 | [[struct]] |
| 对象 | 运行时具体实例如何承载状态和行为 | [[object]] |
| 类 | 如何描述对象的状态、行为和构造方式 | [[class]] |
| 接口 | 如何表达稳定能力契约 | [[interface]] |
| 抽象类 | 如何表达共同骨架和部分通用实现 | [[abstract-class]] |
| 接口、类和抽象类 | 三者的职责边界、选择标准和关系 | [[interface-class-abstract-class]] |
| 封装 | 如何隐藏状态、细节和非法操作 | [[encapsulation]] |
| 继承 | 什么时候应该表达“是一种”的类型关系 | [[inheritance]] |
| 多态 | 如何让同一抽象在不同场景下替换实现 | [[polymorphism]] |
| 数据基础 | 数据库为什么是很多后台系统的中心 | [[database]] |
| 数据库基础概念 | schema、表、列、行、键、索引、事务如何组成数据模型 | [[database-basics]] |
| SQL | 如何定义结构、查询数据、修改数据和控制事务 | [[sql]] |
| ORM | 程序对象如何映射到数据库表、列、行和 SQL | [[orm]] |
| Schema | 数据库对象如何组织，结构定义如何演进 | [[schema]] |
| 表 | 同一类业务事实如何被集合化保存 | [[table]] |
| 列和行 | 字段定义和具体记录如何共同表达业务事实 | [[column]]、[[row]] |
| 键和关系 | 主键如何识别记录，外键如何表达关系 | [[primary-key]]、[[foreign-key]] |
| 约束 | 数据库如何阻止非法数据进入 | [[database-constraint]] |
| Index / 索引 | 如何用额外结构更快定位数据 | [[database-index]] |
| 事务 | 多个读写操作如何保持一致 | [[database-transaction]] |
| 数据库类型 | 常见数据库的定位、适用场景和学习重点 | [[07-foundations/data/databases/README]] |
| 交易处理 | 业务系统如何记录交易、状态变化和一致性约束 | [[oltp]] |
| 数据分析 | OLTP 和 OLAP 的边界，业务事实如何变成指标洞察 | [[olap]] |
| 交易与分析对比 | OLTP 和 OLAP 的职责、访问模式和数据链路有什么不同 | [[oltp-vs-olap]] |
| 技术栈 | 开源框架依赖哪些语言、框架、构建、权限、数据和平台能力 | [[技术栈]] |
| 工程组织 | monorepo 为什么影响协作、依赖和构建 | [[monorepo]] |
| 数学建模 | 如何把业务问题表达成变量、约束、目标、公式和可验证模型 | [[mathematical-modeling]] |
| 企业软件系统 | CMS、ERP、MES、CRM 等企业系统分别管理什么 | [[enterprise-software-systems]] |
| CMS | 内容如何建模、编辑、审核、发布和复用 | [[cms]] |
| ERP | 企业资源和交易流程如何保持一致 | [[erp]] |
| MES | 生产计划如何落到车间执行和追溯 | [[mes]] |
| CRM | 客户关系和销售过程如何管理 | [[crm]] |
| 产品范式 | Headless CMS 解决什么问题，不解决什么问题 | [[headless-cms]] |

## 和项目的关系

| 基础概念             | 观察项目                                        |
| ---------------- | ------------------------------------------- |
| [[solid]]        | RuoYi/Yudao、JeecgBoot、gin-vue-admin、Payload |
| [[database]] | Directus、ERPNext、RuoYi/Yudao、JeecgBoot      |
| [[oltp]]         | RuoYi/Yudao、ERPNext、JeecgBoot、Yudao Cloud   |
| [[olap]]         | JeecgBoot、RuoYi/Yudao Report、ClickHouse     |
| [[monorepo]]     | Directus、Payload、yudao-ui-admin-vben        |
| [[headless-cms]] | Directus、Payload             |
| [[erp]] | ERPNext |
| [[crm]] | RuoYi/Yudao、JeecgBoot |
| [[boundaries]] | Yudao Cloud、ERPNext、gin-vue-admin           |
| [[abstractions]] | RuoYi/Yudao、Directus、Payload、gin-vue-admin  |

## 目录结构

| 目录 | 内容 |
| --- | --- |
| `architecture/` | 架构观、AI 时代的设计尺度、机器可理解的软件系统、边界、抽象 |
| `design-principles/` | SOLID、SRP/OCP/LSP/ISP/DIP、LSP vs DIP、模块边界设计 |
| `oop/` | 结构体、对象、类、接口、抽象类、封装、继承、多态 |
| `data/` | 数据库基础、SQL、ORM、schema、表、列、行、键、约束、索引、事务、OLTP/OLAP |
| `data/databases/` | MySQL、PostgreSQL、Redis、ClickHouse 等具体数据库 |
| `technology-stacks/` | Java、Spring、Go、Vue、TypeScript、Directus/Payload/Frappe 相关技术栈 |
| `engineering/` | Monorepo、数学建模等工程组织和建模概念 |
| `product-patterns/` | CMS、ERP、MES、CRM、Headless CMS 等产品/平台范式 |

## 写作原则

- 概念卡必须解释“为什么重要”，不只给定义。
- 概念要连接到项目源码阅读笔记，不能孤立成百科。
- 不追逐临时版本和热度信息，优先沉淀长期有效的判断框架。
- 一张概念卡只解决一个核心问题，复杂主题拆成多张卡。
