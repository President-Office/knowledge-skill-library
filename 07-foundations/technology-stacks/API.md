---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, api, integration]
---

# API

API 是系统对外暴露能力的契约。它把内部实现隐藏起来，只让调用方看到可用的资源、操作、参数、返回值和错误语义。

在后台框架中，API 不只是 Controller 路由，而是前端、第三方系统、SDK、AI Agent 和自动化工具理解系统能力的入口。

## 学习重点

- API 是否来自手写代码、代码生成、配置、元数据，还是数据库 schema。
- API 契约是否稳定，是否能被 SDK、OpenAPI、GraphQL schema 或 MCP 工具描述。
- API 层和权限、租户、审计、事务、限流之间如何组合。

## 关联

- [[REST]]
- [[GraphQL]]
- [[SDK]]
- [[MCP]]
- [[machine-readable-software-systems]]
