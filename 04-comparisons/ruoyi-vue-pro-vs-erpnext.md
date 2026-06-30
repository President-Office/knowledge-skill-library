---
type: comparison
status: draft
projects: [zhijiantianya/ruoyi-vue-pro, frappe/erpnext]
created: 2026-06-30
updated: 2026-06-30
---

# RuoYi/Yudao 与 ERPNext 对比

## 结论

- 学 Java 企业后台、权限、代码生成、模块化脚手架：优先读 `zhijiantianya/ruoyi-vue-pro`。
- 学完整 ERP 业务套件、DocType 元数据、会计/库存交易：优先读 `frappe/erpnext`。
- 如果目标是快速做国内中后台项目，RuoYi/Yudao 更贴近技术栈和交付方式。
- 如果目标是做高度可配置的业务系统、工作流平台或 ERP 类产品，ERPNext/Frappe 更值得深读。

## 核心差异

| 维度 | RuoYi/Yudao | ERPNext |
| --- | --- | --- |
| 主要定位 | Java 中后台 / SaaS / 业务中台脚手架 | 完整 ERP 业务套件 |
| 技术栈 | Spring Boot、MyBatis Plus、Vue、Maven 多模块 | Python、Frappe Framework、DocType、bench |
| 建模方式 | Java DO/VO/Service/Mapper + SQL 表 | DocType JSON + Python Controller + JS Form |
| 扩展方式 | 新增模块、代码生成、Spring Bean、接口适配 | 自定义 DocType、hooks、patches、Frappe app |
| 学习重点 | 权限、租户、代码生成、模块边界、后台前端 | 会计、库存、单据生命周期、元数据、事件钩子 |
| 业务完整度 | 覆盖很多业务模块，但更偏开发底座 | ERP 业务闭环更成熟 |
| License | MIT | GPL-3.0 |

## 后续阅读问题

- [ ] 二者权限模型如何不同？
- [ ] RuoYi 的代码生成和 Frappe 的 DocType 元数据分别适合什么场景？
- [ ] ERPNext 的账务/库存不可变流水能否抽象成通用业务模式？
- [ ] 如果做国内 SaaS 中后台，应从二者分别借鉴哪些部分？
