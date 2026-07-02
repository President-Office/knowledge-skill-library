---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [architecture, learning-method]
---

# 架构是楔子，不是目的

## 核心判断

架构图、目录结构、模块拆分只是进入系统的楔子。真正值得沉淀的是背后的工程判断：变化在哪里发生，边界如何划分，依赖如何流动，数据如何建模，复杂度如何被隔离。

## 为什么要这样看

如果只学“某个项目用了什么架构”，知识会很快失效。框架会变，版本会变，项目热度会变，但下面这些问题长期有效：

- 为什么这里要拆模块？
- 为什么这里要用网关？
- 为什么这里把 Admin、API、SDK 分开？
- 为什么这个系统从数据库出发，而不是从代码生成出发？
- 为什么这个业务系统用 DocType，而不是普通 Controller / Service / Mapper？
- 为什么某些业务需要先做数学建模，而不是直接写 if/else？

## 架构作为入口

| 架构现象         | 不要停在这里         | 继续追问                   |
| ------------ | -------------- | ---------------------- |
| [[Monorepo]] | “它用了 monorepo” | 依赖、构建、发布、共享包边界如何被管理    |
| 微服务          | “它是微服务”        | 服务边界是否对应业务边界，分布式成本是否值得 |
| Headless CMS | “它有 CMS”       | 内容、数据、权限、前端呈现如何解耦      |
| 代码生成         | “它能生成 CRUD”    | 生成物和手写业务代码的边界在哪里       |
| 低代码          | “它能拖拽表单”       | 配置表达能力到哪里会失效           |
| Database First | “它不用写后台” | schema、metadata、permission 是否形成机器可读数据层 |

## 在本库中的使用方式

1. 从 [[01-projects/README]] 进入一个真实项目。
2. 用 [[02-reading-notes/README]] 记录结构和证据。
3. 把项目中出现的底层问题链接到 [[07-foundations/README]]。
4. 把多个项目重复出现的工程做法沉淀到 [[03-patterns/README]]。
5. 用 [[04-comparisons/README]] 做选型判断，但不把选型当作学习终点。

## 相关概念

- [[ai-era-engineering-design-scale]]
- [[solid]]
- [[machine-readable-software-systems]]
- [[boundaries]]、[[abstractions]]
- [[database]]
- [[mathematical-modeling]]
- [[monorepo]]
- [[headless-cms]]
