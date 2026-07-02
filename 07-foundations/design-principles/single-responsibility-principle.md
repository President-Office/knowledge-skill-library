---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [solid, srp, design-principles]
---

# SRP 单一职责原则

## 核心定位

SRP 是 Single Responsibility Principle，通常译为“单一职责原则”。

一句话理解：

**一个模块应该只有一个主要变化原因。**

这里的“模块”可以是类、函数、包、服务、页面组件，也可以是数据库表或后台菜单模块。重点不是“只能做一件小事”，而是不要把不同变化方向强行绑在一起。

## 它解决什么问题

当一个模块同时承担太多职责时，任何变化都会牵连它：

- 改接口入参，会影响业务逻辑。
- 改数据库字段，会影响前端展示。
- 改权限规则，会影响报表统计。
- 改导出格式，会影响核心交易流程。

SRP 让我们追问：这些代码是否因为同一个原因而变化？

## 后台项目里的判断

| 位置 | 好信号 | 坏信号 |
| --- | --- | --- |
| Controller | 只处理参数、鉴权入口、返回值转换 | 写复杂业务规则、拼 SQL、直接调用第三方 SDK |
| Service | 表达业务流程和业务规则 | 同时处理 HTTP、缓存、导出、定时任务、权限细节 |
| Mapper / Repository | 负责数据访问 | 混入业务判断和接口组装 |
| DTO / VO | 表达接口输入输出 | 被拿去当领域对象或数据库实体 |
| 前端组件 | 负责一个明确交互或展示单元 | 同时处理接口、权限、状态机、复杂业务规则 |

## 和抽象、边界的关系

SRP 是判断 [[boundaries]] 的一个入口。职责不清，边界通常也不清。

SRP 也会影响 [[abstractions]]：如果一个接口承担太多职责，调用方就很难只依赖自己需要的稳定能力。

在模块尺度上，SRP 不等于“一个功能一个模块”。更完整的拆分判断见：[[module-boundary-design-principles]]。

## 常见误区

- 单一职责不是把每个方法拆到极小，而是让变化原因清楚。
- 一个类有多个方法不一定违反 SRP，关键看这些方法是否服务于同一个职责。
- 过度拆分也会伤害理解成本，职责边界要能被业务语义解释。

## 关联

- [[solid]]
- [[open-closed-principle]]
- [[interface-segregation-principle]]
- [[module-boundary-design-principles]]
- [[boundaries]]
- [[abstractions]]
