---
type: source-reading
status: initial
project: directus/directus
topic: 运行入口
created: 2026-07-02
updated: 2026-07-02
---

# Directus - 运行入口

项目主卡：[[directus--directus]]

## 关注的问题

Directus 的运行入口要同时看 [[CLI]]、[[Node.js]] 包入口和 [[API]] 服务启动链路。它不是只读某个 Controller，而是要理解命令如何把配置、数据库连接、权限系统、API 路由和扩展加载起来。

## 关联源码入口

- `directus/package.json`
- `api/package.json`
- 根目录 `package.json`
- `pnpm-workspace.yaml`

## 知识关系

- [[CLI]]：理解用户输入的命令如何变成服务启动动作。
- [[API]]：理解 Directus 最终对外暴露的能力边界。
- [[Monorepo Package]]：理解 `directus`、`api`、`app`、`sdk` 等包之间的职责。
- [[Node.js]]：理解运行时、脚本和包入口。

## 阅读判断

运行入口的价值不在于记住启动命令，而在于确认 Directus 的核心对象何时被加载：数据库 schema、[[Metadata]]、[[权限模型]]、extensions 和 API routes。

## 关联

- [[02-reading-notes/directus--directus/monorepo-structure]]
- [[02-reading-notes/directus--directus/database-first-model]]
- [[02-reading-notes/directus--directus/extension-system]]
