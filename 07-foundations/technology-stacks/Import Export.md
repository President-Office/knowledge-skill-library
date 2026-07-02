---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [technology-stack, data, import-export]
---

# Import Export

Import Export 是后台系统中导入和导出数据的能力，常用于 Excel、CSV、报表、批量维护和系统迁移。

它看起来像工具功能，但实际涉及字段映射、校验、权限、幂等、错误回滚和审计。

## 学习重点

- 导入模板如何生成，字段和校验规则来自哪里。
- 大批量导入如何处理事务、失败行和重试。
- 导出是否遵守数据权限和脱敏规则。

## 关联

- [[数据权限]]
- [[报表]]
- [[schema]]
- [[database-transaction]]
