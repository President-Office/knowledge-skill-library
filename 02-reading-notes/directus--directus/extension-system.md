---
type: source-reading
status: initial
project: directus/directus
topic: 扩展机制
created: 2026-07-02
updated: 2026-07-02
---

# Directus - 扩展机制

项目主卡：[[directus--directus]]

## 核心问题

Directus 的扩展机制决定它能否从通用数据后台变成可长期演进的平台。复杂业务不可能全部靠自动 CRUD 解决，扩展点就是把通用数据层和具体业务规则连接起来的地方。

## 知识关系

- [[插件体系]]：理解扩展如何注册、加载和隔离。
- [[Monorepo Package]]：理解扩展相关能力在 packages 中如何组织。
- [[API]]：服务端扩展可能改变接口、hook 或业务动作。
- [[Admin App]]：前端扩展可能改变 interface、layout、display 或操作体验。

## 阅读入口

- `packages`
- `api/src`
- `app/src`
- hooks、flows、interfaces、layouts、displays 等扩展相关模块。

## 阅读判断

扩展机制是 Directus 与“纯 CRUD 后台生成器”的分界点。只有当扩展点能承载真实业务变化，Directus 才能作为结构化数据层接入更复杂的软件系统。

## 关联

- [[02-reading-notes/directus--directus/metadata-and-permissions]]
- [[02-reading-notes/directus--directus/admin-app-architecture]]
- [[插件体系]]
- [[machine-readable-software-systems]]
