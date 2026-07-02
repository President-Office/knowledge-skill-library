---
type: framework-characteristics
status: draft
project: jeecgboot/JeecgBoot
created: 2026-07-02
updated: 2026-07-02
---

# JeecgBoot 特点

项目主卡：[[jeecgboot--JeecgBoot]]

## 核心定位

[[Java]] AI 低代码 / 零代码后台平台。它的特点不是单纯写 CRUD，而是把 [[代码生成]]、在线表单、[[报表]]、[[工作流]]、[[AI Skills]]、[[MCP]] 插件和企业后台基础能力结合起来。

## 主要特点

| 特点 | 说明 | 学习价值 |
| --- | --- | --- |
| 低代码 / 零代码能力 | 在线表单、流程、报表、代码生成是核心卖点 | 学后台平台如何减少重复开发 |
| [[Spring Boot]] + [[Vue 3]] | 国内 [[Java]] 后台常见技术组合 | 适合 [[Java]] 团队学习和二开 |
| [[Shiro]] + [[JWT]] 权限 | 权限体系不同于 [[Spring Security]] 路线 | 可和 RuoYi/Yudao 对比 |
| [[JimuReport]] / [[JimuBI]] | [[报表]] 和 BI 能力嵌入后台平台 | 学企业后台报表平台化 |
| [[AI Skills]] / [[MCP]] | README 描述包含 AI 生成、知识库、流程编排、[[插件体系]] 能力 | 学传统低代码平台向 AI 平台演进 |
| Apache-2.0 | 许可证相对宽松 | 更适合作为二开参考样本 |

## 最适合怎么读

1. 先读 `jeecg-boot/pom.xml` 和模块边界。
2. 再读 `jeecg-module-system`、权限、菜单、租户和组织模型。
3. 重点深读 [[代码生成]]、在线表单、[[JimuReport]]、[[AI Skills]]。

## 不要误解

- 不要只把它当普通 Java 后台，低代码和在线配置才是主要差异。
- 不要只比较技术栈，要比较它如何把表单、报表、流程和代码生成组合成平台。
- 不要把 AI Skills 直接等同于业务智能，需要在源码里确认运行边界。

## 关联

- [[solid]]
- [[database]]
- [[boundaries]]、[[abstractions]]
- [[admin-scaffold-comparison]]
- [[pairwise-backend-comparisons]]
