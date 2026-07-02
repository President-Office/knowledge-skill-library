---
type: source-reading
status: initial
project: jeecgboot/JeecgBoot
topic: Maven 多模块结构
created: 2026-07-02
updated: 2026-07-02
---

# JeecgBoot - Maven 多模块结构

项目主卡：[[jeecgboot--JeecgBoot]]
特点卡：[[jeecgboot]]

## 阅读目标

建立 JeecgBoot 后端工程地图，区分基础核心、系统模块、业务模块和云服务模块，后续再读低代码、在线表单、报表和 AI Skills。

## 已确认结构

后端主目录是 `jeecg-boot/`：

| 目录 | 初步职责 |
| --- | --- |
| `jeecg-boot-base-core` | 基础核心能力，预计包含通用配置、工具、权限基础封装 |
| `jeecg-module-system` | 系统管理模块，用户、角色、菜单、组织等基础后台能力 |
| `jeecg-boot-module` | 业务或扩展模块聚合 |
| `jeecg-server-cloud` | 微服务 / 云服务相关入口 |
| `db` | 数据库脚本 |
| `pom.xml` | Maven 聚合和依赖管理入口 |

## 初步判断

JeecgBoot 和 [[ruoyi-vue-pro]] 都是国内 Java 后台平台，但学习重点不同：

- RuoYi/Yudao 更适合作为企业后台和业务中台样本。
- JeecgBoot 更适合研究低代码、在线表单、报表、流程、AI Skills 如何拼成平台。

因此 JeecgBoot 的 Maven 结构不能只按“普通后台模块”读，还要特别关注低代码相关模块在哪里落地。

## 读源码时要验证的问题

- `jeecg-boot-base-core` 和 `jeecg-module-system` 的依赖方向。
- Shiro + JWT 的核心配置在哪个模块。
- 代码生成器是否属于 core、system，还是独立模块。
- JimuReport / JimuBI 如何接入后端。
- `jeecg-server-cloud` 与单体启动方式的区别。

## Obsidian 关联

- 底层概念：[[solid]]、[[database]]、[[boundaries]]、[[abstractions]]
- 框架特点：[[jeecgboot]]
- 后台脚手架对比：[[admin-scaffold-comparison]]
- 一对一对比：[[pairwise-backend-comparisons]]
