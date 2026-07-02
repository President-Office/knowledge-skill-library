---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [architecture, ai, metadata, data-layer, agents]
---

# 机器可理解的软件系统

## 核心判断

AI 时代真正有价值的，不只是某一个框架，而是一个系统能否被机器理解。

一句话理解：

**实现会越来越便宜，机器可读的结构、元数据、权限、关系和业务上下文会越来越贵。**

这意味着很多工具的价值会重新排序。纯 CRUD 后台生成器的价值可能下降，因为 AI 写 CRUD 很快；但结构化数据管理层、数据平台、工作流平台的价值会放大，因为它们能把业务系统变成 AI Agent 可以理解和调用的对象。

## 价值变化判断

| 产品类型 | AI 时代价值变化 | 原因 |
| --- | --- | --- |
| 纯 CRUD 后台生成器 | 下降 | CRUD 实现会被 AI 快速生成 |
| 低代码页面搭建 | 下降 | 页面和表单样板的生成成本下降 |
| Headless CMS | 基本持平 | 内容管理、API、权限仍有价值，但不一定天然成为数据中枢 |
| Database First 平台 | 上升 | 数据库 schema、metadata、permission、API 更容易被机器理解 |
| 数据平台 | 大幅上升 | AI 需要统一、可信、可发现的数据入口 |
| Workflow 平台 | 大幅上升 | Agent 需要可调用、可审计、可编排的业务动作 |

这里的重点不是某个具体产品，而是价值从“帮人少写代码”转向“帮机器理解系统”。

## CRUD 为什么贬值

过去开发后台时，典型链路是：

```text
database
  -> Java / Go / Python backend
  -> Vue / React admin
```

新增、删除、修改、查询都由人写。低代码、代码生成、后台脚手架的主要价值之一，是节省 CRUD 实现。

AI 出现后，Claude Code、Codex、Cursor、Gemini CLI 这类工具可以快速生成 Controller、Service、Mapper、DTO、页面和测试样板。于是 CRUD 本身开始贬值。

但这不代表数据管理平台会贬值。因为 AI 真正缺的不是写代码能力，而是对数据和业务上下文的可靠理解。

## AI 真正需要什么

AI 最怕的不是不会写代码，而是不知道数据是什么。

它需要回答：

- `customer` 有哪些字段？
- `phone` 是否允许为空？
- `status` 有哪些枚举？
- 外键关系是谁？
- 哪些字段可读、可写、可搜索？
- 哪些角色有权限修改？
- 哪些数据是主数据，哪些只是派生数据？
- 哪些字段代表业务不变量？

如果系统没有统一的数据入口，AI 只能从 SQL、ORM 类、接口文档、前端页面和历史代码中猜。

这就是结构化数据管理层的价值。

## 机器可读元数据

机器可读元数据是 AI 时代数据层的关键资产。

```text
schema
  -> metadata
  -> relationship
  -> permission
  -> API
  -> assets / files
```

如果一个平台能把这些内容稳定暴露出来，AI Agent 就能更可靠地理解：

- 有哪些数据对象。
- 对象之间如何关联。
- 字段含义和类型是什么。
- 哪些操作被允许。
- 通过什么 API 读取或修改。
- 哪些文件、图片、附件属于业务对象。

例如客户表 `customer`。AI 想做客户分析、营销邮件、画像生成或报表，它首先需要知道有没有 `birthday`、`city`、`gender`、`orders`、`tags` 等字段。

如果只有 `CREATE TABLE`，AI 要自己解析。  
如果平台提供机器可读字段接口，AI 可以直接获取字段、类型、关系和权限。

这比 CRUD 更值钱。

## Data Layer 的价值

结构化数据管理层不是简单数据库，也不是简单后台页面。

它通常承担：

- 统一数据对象入口。
- 字段和关系元数据。
- 权限和角色规则。
- REST / GraphQL / SDK。
- 文件和资产管理。
- 审计、版本、工作流或扩展点。

从 AI Agent 角度看，它就是可发现、可调用、可约束的数据接口。

```text
Agent
  -> REST / GraphQL / Tool
  -> Data Layer
  -> Database
```

Agent 不应该直接猜数据库，也不应该到处学习每个系统的私有 API。越统一的数据层，越适合 Agent 使用。

## GraphQL 为什么适合 AI

AI 写复杂 SQL 容易出错，尤其涉及多表关联、权限、过滤和聚合时。

传统方式：

```sql
select ...
from customer
left join orders ...
left join products ...
```

GraphQL 这类结构化查询更接近对象关系：

```graphql
customer {
  orders {
    products {
      name
    }
  }
}
```

这不意味着 GraphQL 总是更好。复杂统计、批量处理、OLAP 仍然需要合适的数据模型和查询引擎。  
但对 Agent 来说，GraphQL 的 schema、类型和关系天然更容易被理解和生成。

## MCP 和工具协议

AI Agent 越来越需要的不是“读一段文档后猜接口”，而是通过工具协议发现能力：

```text
Tool
  -> Schema
  -> Capability
  -> Permission
  -> Result
```

例如：

- 读取客户。
- 新增订单。
- 上传文件。
- 审批合同。
- 触发通知。

如果数据平台或工作流平台能把这些能力以机器可读工具形式暴露，Agent 就不需要重新学习每个系统的私有 API。

这也是为什么数据平台和 Workflow 平台在 AI 时代会变得更重要。

## Directus 只是一个例子

Directus 的价值不应该只理解成“不用写 CRUD”。

更重要的是，它代表一种 Database First 平台思路：

```text
database
  -> schema introspection
  -> metadata
  -> relationship
  -> permission
  -> REST / GraphQL API
  -> Admin
```

从这个角度看，它更像 AI 喜欢的数据接口，而不是普通低代码后台生成器。

但这个判断不是只针对 Directus。ERPNext 的 DocType、Payload 的 collection 配置、JeecgBoot 的在线表单和元数据能力，本质上也都在不同程度上把业务对象变成机器可读结构。

区别在于：谁的元数据更完整、更稳定、更容易被 API、权限、工作流和 Agent 共同使用。

## Implementation 和 Metadata

AI 可以很快生成实现：

```text
Controller
Service
Mapper
CRUD Page
DTO
```

这些属于 implementation。

但 AI 很难凭空知道：

```text
业务对象是什么
字段含义是什么
关系如何成立
权限如何约束
状态如何流转
哪些规则不可违反
历史决策为什么这样设计
```

这些属于 metadata、spec、ADR、业务规则和知识层。

未来 implementation 会越来越便宜，metadata 会越来越贵。

## 分层架构判断

一个更适合 AI 时代的软件系统，可能需要形成这样的层次：

```text
GitHub / Docs / ADR / Spec
  -> knowledge layer

Data Layer / Metadata / Permission / API
  -> machine readable data layer

Spring Boot / Java / Domain Service
  -> business rule layer

UniApp / Web / Admin
  -> interaction layer
```

各层职责不同：

| 层次 | 解决的问题 |
| --- | --- |
| GitHub / Docs / ADR / Spec | 让 AI 理解为什么这样设计 |
| Data Layer / Metadata | 让 AI 理解有哪些数据、字段、关系和权限 |
| Spring Boot / Domain Service | 实现复杂业务规则、事务和领域逻辑 |
| UniApp / Web / Admin | 承接用户交互和操作体验 |

在这个体系里，结构化数据层不是替代业务后端，而是连接数据库、AI Agent 和业务系统的中枢。

## 对技术路线的启发

如果目标是长期演进的平台，而不是一次性后台，那么更重要的是形成机器可理解的软件系统：

- 用 GitHub、文档、ADR、需求卡沉淀设计理由。
- 用结构化数据层暴露 schema、metadata、relationship、permission。
- 用 Java / Spring Boot 承接复杂业务规则、事务和领域服务。
- 用前端承接交互，而不是让前端持有核心业务规则。
- 用测试、审计和模型版本保护 AI 生成或 Agent 执行的结果。

所以 Database First 平台的价值，不是替代 Java 后台，而是成为 AI 可理解的数据平台。

## 什么时候价值会下降

如果未来数据库自身完整提供：

- schema introspection
- metadata management
- GraphQL / REST
- auth / permission
- workflow
- file / asset management
- tool protocol integration

那么单独的数据管理平台价值会下降。

但在大多数现实系统里，数据库、权限、API、后台、工作流和知识层仍然是分散的。能把它们结构化整合起来的平台，仍然有明显价值。

## 关联

- [[ai-era-engineering-design-scale]]
- [[database]]
- [[schema]]
- [[orm]]
- [[headless-cms]]
- [[cms]]
- [[abstractions]]
- [[boundaries]]
- [[architecture-as-wedge]]
- [[directus--directus]]
- [[payloadcms--payload]]
- [[frappe--erpnext]]
