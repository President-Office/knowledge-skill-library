---
type: framework-characteristics
status: draft
project: yudaocode/yudao-ui-admin-vben
created: 2026-07-02
updated: 2026-07-02
---

# yudao-ui-admin-vben 特点

项目主卡：[[yudaocode--yudao-ui-admin-vben]]

## 核心定位

基于 [[Vben Admin]] 5 的平台化后台前端底座。它不是简单业务页面工程，而是用 [[monorepo]] 管理多 UI app 和共享 packages，适合评估长期后台前端平台化路线。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| Turbo [[monorepo]] | `apps` + `packages` 组织方式 | 学前端平台工程治理 |
| 多 UI 应用 | [[Element Plus]]、[[Ant Design Vue]]、[[Naive UI]]、[[TDesign]] 等入口 | 学多 UI 体系如何共用底座 |
| 共享 packages | stores、utils、styles、types、icons、preferences 等抽象 | 学大型前端共享能力拆分 |
| Vben Admin 5 | 工程抽象、布局、偏好配置更强 | 学成熟后台前端底座 |
| 迁移成本较高 | 学习、调试、CI/CD 和团队规范要求更高 | 适合做平台评估，不适合盲目替换 |
| [[Element Plus]] 应用可对照 | `apps/web-ele` 可和 [[Vue 3]] 单应用版本对比 | 适合小范围 spike |

## 最适合怎么读

1. 先读根 `package.json`、`pnpm-workspace.yaml`、`turbo.json`。
2. 再读 `apps/web-ele`，和 `yudao-ui-admin-vue3` 做同模块对比。
3. 最后读 `packages` 下的共享能力：stores、utils、preferences、styles。

## 不要误解

- 不要把它当快速业务二开的默认选择，平台化能力会带来复杂度。
- 不要只看 UI，真正学习点是 [[monorepo]]、共享包和多 app 组织。
- 不要在没有 spike 的情况下直接迁移业务后台。

## 关联

- [[monorepo]]
- [[boundaries]]、[[abstractions]]
- [[yudao-ui-admin-vue3]]
- [[yudao-ui-admin-vue3-vs-vben]]
