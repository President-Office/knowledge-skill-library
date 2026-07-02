---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [cms, content-management, enterprise-software]
---

# CMS

## 核心定位

CMS 是 Content Management System，内容管理系统。

一句话理解：

**CMS 负责让内容被建模、编辑、审核、发布和复用。**

这里的内容可以是文章、页面、产品介绍、媒体资源、帮助文档、活动页、知识库条目，也可以是更泛化的数据内容。

## CMS 管什么

| 对象 | 说明 |
| --- | --- |
| 内容模型 | 文章、页面、栏目、媒体、标签、作者等结构 |
| 编辑流程 | 草稿、审核、发布、下线、版本 |
| 权限 | 谁能编辑、审核、发布、管理栏目 |
| 展示渠道 | 网站、小程序、App、API、静态站点 |
| 媒体资源 | 图片、文件、视频、附件 |

## CMS 和 Headless CMS

传统 CMS 往往同时负责内容管理和页面展示。

[[headless-cms]] 把内容管理和前端展示解耦，重点提供 Admin、API、权限、SDK，让多个前端消费内容。

```text
传统 CMS：内容管理 + 页面渲染
Headless CMS：内容管理 + API，前端独立渲染
```

## 和后台管理系统的区别

有 Admin 界面不等于 CMS。

CMS 的核心是内容生命周期：

- 内容怎么建模。
- 内容怎么编辑。
- 内容怎么审核。
- 内容怎么发布。
- 内容怎么被多个渠道复用。

普通后台 CRUD 只解决“数据管理”，不一定解决内容生产和发布流程。

## 在项目中怎么观察

| 项目 | 观察点 |
| --- | --- |
| [[directus--directus]] | 如何把数据库 schema 转成 collections、fields、permissions 和 API |
| [[payloadcms--payload]] | 如何用 TypeScript 配置 collections、fields、hooks 和 Admin |

## 常见误区

- CMS 不只是文章系统，核心是内容模型和发布流程。
- Headless CMS 不等于没有后端，它只是把展示层拆出去。
- CMS 可以管理内容，但复杂交易流程通常不应该塞进 CMS。

## 关联

- [[enterprise-software-systems]]
- [[headless-cms]]
- [[database]]
- [[schema]]
- [[directus]]
- [[payload]]
