---
type: foundation
status: draft
created: 2026-09-20
updated: 2026-09-20
tags: [design-principles, fail-fast, validation]
---

# Fail Fast 尽早失败

## 核心定位

Fail Fast 要求在系统仍然知道问题原因和上下文时，尽早验证前置条件并暴露错误，避免无效状态继续传播。

## 编程时怎么判断

- 输入、配置、权限和依赖是否在边界处验证？
- 错误是否保留了足够上下文，能被日志、测试和调用方识别？
- 是否把错误吞掉、转换成空值，或拖到更深层才崩溃？

安全场景通常还要遵守 fail closed：无法确认权限时拒绝访问，而不是放行。对于可恢复的外部故障，Fail Fast 仍应和超时、重试、熔断及降级策略一起设计。

## 常见误区

- 用异常替代业务分支，把正常的用户输入错误当成系统崩溃。
- 只在日志里报错，却不给调用方稳定的错误契约。

## 关联

- [[least-privilege]]
- [[measure-first]]
- [[separation-of-concerns]]
