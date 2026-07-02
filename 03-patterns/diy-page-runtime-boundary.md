---
type: engineering-pattern
status: draft
sources:
  - zhijiantianya/ruoyi-vue-pro
  - yudao-mall-uniapp
tags: [mall, diy, low-code, uni-app, page-runtime, tabbar]
created: 2026-07-01
updated: 2026-07-01
---

# DIY 页面运行时边界

## 解决什么问题

判断一个“装修 / 低代码 / DIY 页面”能力，是否真的可以替代业务页面运行时。

常见误判是：只要后台能配置页面 JSON，并且前端有 CSS，就认为所有 tabbar 甚至所有页面都可以通过 DIY 配置加载。这个判断不成立。CSS 只解决展示，不解决路由注册、数据加载、权限、业务校验、状态管理和页面生命周期。

## 典型场景

- 商城首页、个人中心、活动页等内容展示页面需要灵活配置。
- 产品希望把 tabbar 条目、图标、颜色和跳转地址交给后台配置。
- 团队需要判断“装修系统”能否覆盖分类、购物车、订单、支付、售后等复杂业务页。
- 二次开发时需要决定：新增配置组件，还是新增真实 Vue / uni-app 页面。

## 来自哪些项目

| 项目 | 证据 | 备注 |
| --- | --- | --- |
| `zhijiantianya/ruoyi-vue-pro` | Mall promotion 模块提供 `promotion_diy_template`、`promotion_diy_page`，App 端接口返回已使用模板、首页、我的页和单个 DIY 页属性 | 后端存储的是模板属性和页面属性，不是完整动态应用引擎 |
| `yudao-mall-uniapp` | `s-tabbar` 读取 `app.template.basic.tabbar`，点击后走 `sheep.$router.go(item.url)`；`pages/index/index`、`pages/index/user`、`pages/index/page` 通过组件列表渲染 | tabbar 可配置，但目标路由必须已在前端存在 |

## 核心做法

```text
DIY 模板接口 -> app store -> tabbar / home / user
DIY 页面接口 -> pages/index/page?id=... -> s-block-item 组件映射
业务页面路由 -> pages.json -> Vue 页面代码 -> API / store / permission / lifecycle
```

把“可配置装修内容”和“业务页面运行时”分开：

- tabbar 配置负责展示条目、图标、颜色和跳转地址。
- 首页、我的页、自定义页可以通过组件列表渲染。
- 分类、购物车、订单、商品详情、支付、售后等业务页仍然是前端注册过的真实页面。
- 如果 tabbar 指向一个 DIY 内容页，推荐统一指向 `/pages/index/page?id=...` 这样的容器页。
- 如果 tabbar 指向一个业务工作流，仍然指向现有业务页面。

## 优点

- 装修能力边界清晰，不会把简单内容配置误当成完整低代码平台。
- 首页、用户中心、活动页等高频改版页面可以快速调整。
- 复杂业务页保留显式代码，便于维护权限、状态、接口和异常处理。
- tabbar 可运营配置，但不会破坏 uni-app 对页面注册和 `switchTab` 的约束。

## 代价

- 所有可跳转页面仍要在 `pages.json` 中注册。
- DIY 组件能力受 `s-block-item` 组件映射限制。
- 新业务能力如果没有组件化，不能只靠 JSON 和 CSS 配出来。
- tabbar 配置可以隐藏或暴露入口，但不能自动生成对应页面能力。

## 适合复用到哪里

- 商城装修系统。
- CMS / 低代码页面搭建器。
- App 首页运营配置。
- 多租户 SaaS 的可配置门户。
- 任何需要判断“配置驱动页面”与“业务页面代码”边界的项目。

## 不适合的情况

- 购物车、支付、订单、售后这类强状态、强校验页面，除非已经把完整业务能力抽成稳定组件和动作模型。
- 需要动态创建原生页面路由的场景，除非平台本身提供了动态路由容器和统一页面 schema。
- 需要复杂权限、数据绑定、表单校验、流程编排的页面，不能只依赖样式和静态组件。

## 判断准则

如果一个页面只需要“展示内容 + 简单跳转”，可以优先 DIY。

如果一个页面需要“业务状态 + API 写操作 + 权限判断 + 表单校验 + 生命周期处理”，应优先保留真实页面代码，最多把局部区域组件化给 DIY 使用。

如果产品要求“所有页面都完全 DIY”，那已经不是普通装修能力，而是低代码运行时平台需求，需要补齐：

- 动态页面路由策略。
- 页面 schema。
- 组件注册表。
- API / 数据源绑定。
- action / event 模型。
- 权限和登录拦截模型。
- 表单校验和错误态。
- 预览、发布、回滚和兼容策略。

## 相关项目卡

- [[zhijiantianya--ruoyi-vue-pro]]
