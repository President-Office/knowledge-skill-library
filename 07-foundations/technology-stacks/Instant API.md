---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, api, metadata]
---

# Instant API

Instant API 指系统根据数据库、配置或元数据自动暴露的 API。开发者不必为每张表手写基础 CRUD 接口。

它的价值不是“省几行 Controller”，而是让数据模型、权限、关系和 API 契约在同一个元数据体系下被机器读取。

## 学习重点

- API 是根据 [[schema]]、配置文件还是 [[Metadata]] 生成。
- 权限、字段可见性、关系加载和审计是否纳入生成逻辑。
- 复杂业务规则是放在扩展点里，还是独立业务服务里。

## 关联

- [[API]]
- [[REST]]
- [[GraphQL]]
- [[Metadata]]
- [[database-first-admin-platforms]]
