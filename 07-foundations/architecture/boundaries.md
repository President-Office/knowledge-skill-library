---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [architecture, boundaries]
---

# 边界

## 核心问题

工程复杂度首先来自边界不清。边界不清时，权限逻辑会散落，数据模型会被页面牵着走，业务服务会直接绑定中间件，前端页面会复制后端规则。

边界要回答的是：**什么应该放在一起，什么应该隔离。**

## 常见边界

| 边界类型 | 典型问题 | 示例 |
| --- | --- | --- |
| 业务边界 | 哪些规则属于同一个业务域 | ERPNext 的 Accounting、Stock、Buying、Selling |
| 模块边界 | 哪些代码应该放在同一个模块 | RuoYi/Yudao 的 `system`、`infra`、`pay`、`mall` |
| 服务边界 | 哪些能力值得独立运行和部署 | Yudao Cloud 的 Gateway、业务服务 |
| 包边界 | 哪些能力应该复用、独立发布或独立测试 | Payload、Directus、Vben 的 packages |
| 数据边界 | 哪些表、字段、权限属于同一数据模型 | Directus 的 collections、fields、relations |

## 好边界的判断

- 变化集中：一个业务规则变化时，不需要跨很多模块同时修改。
- 依赖清楚：上层知道自己依赖什么，不直接穿透到基础设施细节。
- 所属明确：代码、表、接口、权限能看出属于哪个业务域或技术层。
- 可独立理解：读一个模块时，不必先读完整系统才能判断它的职责。

## 在项目中怎么观察

| 项目                             | 边界观察点         |                             |
| ------------------------------ | ------------- | --------------------------- |
| [[zhijiantianya--ruoyi-vue-pro]] | `yudao-framework` 与业务模块的边界  |
| [[zhijiantianya--yudao-cloud]] | Maven 模块边界和运行时服务边界是否一致      |
| [[frappe--erpnext]]     | DocType 和业务域模块是否表达真实业务边界    |
| [[directus--directus]]    | API、Admin、SDK、metadata 的包边界 |
| [[payloadcms--payload]]     | core、Next 集成、数据库适配器、插件的边界   |

## 和 SOLID 的关系

[[solid]] 是判断局部设计的工具，边界是系统尺度的判断工具。两者都在追问：变化发生时，系统需要改多少地方。

模块是否应该继续放在一起，还是拆成独立模块或服务，见：[[module-boundary-design-principles]]。

## 关联

- [[ai-era-engineering-design-scale]]
- [[module-boundary-design-principles]]
- [[abstractions]]
- [[solid]]
- [[monorepo]]
- [[database]]
- [[architecture-as-wedge]]
