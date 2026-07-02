---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, security, rbac]
---

# RBAC

RBAC 是基于角色的访问控制。它通常把用户分配给角色，再把权限分配给角色，从而减少直接给用户分配权限的复杂度。

在企业后台中，RBAC 经常和菜单权限、按钮权限、部门、岗位、租户、数据权限组合出现。

## 学习重点

- 用户、角色、权限、菜单、部门之间的关系表如何设计。
- 后端 API 权限和前端菜单/按钮权限是否来自同一套权限标识。
- 数据权限是否属于 RBAC，还是作为独立模型叠加。

## 关联

- [[权限模型]]
- [[数据权限]]
- [[Casbin]]
- [[Spring Security]]
- [[Shiro]]
