---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, least-privilege, security]
---

# Least Privilege 最小权限

## 核心定位

Least Privilege 要求用户、Agent、服务、Token、数据库账号和部署流程只获得完成当前任务所必需的最小权限，并且默认拒绝未明确授权的动作。

## 编程时怎么判断

- 这个调用是否真的需要写权限、全库权限或管理员权限？
- 权限是否按资源、动作、租户、环境和生命周期进行约束？
- 凭据是否短期、可轮换、可审计，且不会进入日志、代码或构建产物？
- 失败时是否 fail closed，而不是因为权限判断失败而放行？

最小权限既是安全原则，也是降低错误半径的工程原则。它适用于人、AI Agent、CI、服务账号和第三方集成。

## 常见误区

- 为了省事给开发工具、CI 或 Agent 一个长期全能 Token。
- 只限制前端按钮，不在后端、数据层和部署边界重复验证。

## 关联

- [[fail-fast]]
- [[dependency-inversion-principle]]
- [[machine-readable-software-systems]]
