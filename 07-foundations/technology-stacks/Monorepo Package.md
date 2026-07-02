---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, monorepo, package]
---

# Monorepo Package

Monorepo Package 是 monorepo 中可独立声明依赖、构建、测试和发布的子包。

在 Directus、Payload、Vben Admin 这类项目中，package 是理解边界的关键：核心框架、UI、SDK、插件、数据库适配器和工具包通常被拆成不同 package。

## 学习重点

- package 是否有独立 `package.json`、构建脚本和依赖边界。
- package 之间是源码依赖、构建产物依赖，还是发布后的版本依赖。
- 公共包是否承载稳定抽象，还是变成了无边界工具集合。

## 关联

- [[monorepo]]
- [[pnpm workspace]]
- [[Turborepo]]
- [[SDK]]
