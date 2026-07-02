---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [design-principles, boundaries, srp, modularity]
---

# 模块边界设计原则

## 核心问题

模块边界设计要回答：一个业务应该先放在一个模块里，还是拆成多个模块、服务或仓库？

一句话理解：

**不要因为名字不同就拆模块，要因为变化原因、数据规模、部署方式、团队 ownership 或复用边界不同才拆。**

这和 [[single-responsibility-principle]]、[[boundaries]]、[[abstractions]] 密切相关。SRP 不是“一个功能一个模块”，而是“一个模块应该有清楚、主要的变化原因”。

## 起步原则

对于一个业务域，保守做法通常是：

```text
先放在一个 coherent business module 里
再在模块内部按子领域拆 controller / service / dal / algorithm
最后等真实信号出现，再拆成独立模块或服务
```

这种方式避免两个极端：

- 所有能力塞进一个大服务，形成上帝模块。
- 一开始按名词拆成很多模块，导致调用链、事务、数据和部署复杂度过早上升。

## 内部边界怎么拆

一个业务模块内部仍然要有清晰子领域。

例如：

```text
module
  controller/admin/<sub-domain>
  service/<sub-domain>
  dal/dataobject/<sub-domain>
  algorithm/<sub-domain>
```

拆分依据不是目录好看，而是不同子领域有不同变化原因。

| 位置 | 好信号 | 坏信号 |
| --- | --- | --- |
| Controller | 按用例或业务区域组织入口 | 所有接口塞进一个大 Controller |
| Service | 一个服务围绕一个主要业务职责 | 一个 Service 同时查询、生成、支付、导出、同步 |
| DAL / Repository | 数据访问边界跟业务数据归属一致 | 随手跨表跨域拼查询 |
| Algorithm / Model | 计算、推荐、规则有独立输入输出和测试 | 算法散落在 Controller、SQL、前端里 |

## 依赖方向

模块内部可以有编排层和基础能力层，但依赖方向要清楚。

```text
orchestration / workflow
  -> domain service
  -> repository / mapper
  -> database
```

数据查询能力通常不应该反向依赖业务编排能力。

例如推荐/生成类能力可以依赖基础数据查询服务；但学校、专业、历史分数等基础数据服务，不应该依赖推荐生成服务。

## 什么时候不要拆太早

不要因为这些理由过早拆模块：

- 名词不同。
- 目录看起来更整齐。
- 未来可能会独立部署。
- 觉得微服务更高级。
- AI 生成多个模块很容易。

过早拆分会带来确定成本：跨模块调用、事务边界、权限同步、测试装配、部署顺序、日志排查和数据一致性。

## 什么时候应该拆

当出现真实工程信号时，再考虑拆成独立模块、服务或仓库。

| 信号 | 说明 |
| --- | --- |
| 部署不同 | 某个能力需要独立发布、伸缩或隔离故障 |
| 数据规模不同 | 某类数据需要独立数据库、搜索引擎、OLAP 或归档策略 |
| 计算特征不同 | 某个流程需要异步、队列、批处理或专门算力 |
| ownership 不同 | 不同团队负责不同生命周期和质量目标 |
| 权限模型不同 | 访问规则、审计要求、数据隔离明显不同 |
| 复用边界明确 | 该能力被多个业务域稳定复用 |
| 外部 API 稳定 | 外部客户或其他系统需要独立依赖它 |

拆分应该由这些信号驱动，而不是由命名偏好驱动。

## 和 AI 时代设计尺度的关系

AI 降低了创建文件、目录、接口和样板代码的成本，但没有降低错误边界的长期成本。

在 [[ai-era-engineering-design-scale]] 下，模块边界要更重视：

- 确定复杂性要建立边界。
- 想象中的变化不要提前付复杂度。
- 先让重构变容易，再追求一步到位。
- AI 生成的代码要接受边界、依赖方向和测试的审查。

## 常见误区

- 把 SRP 理解成“一个功能一个 Maven module”。
- 把所有接口放进一个 `XxxService`，导致职责持续膨胀。
- 只拆代码目录，不拆数据边界和权限边界。
- 服务拆开了，但数据库表和事务仍然高度耦合。
- 用“以后可能复用”证明提前抽象，但没有真实复用方。

## 关联

- [[single-responsibility-principle]]
- [[boundaries]]
- [[abstractions]]
- [[ai-era-engineering-design-scale]]
- [[monorepo]]
- [[database]]
- [[mathematical-modeling]]
