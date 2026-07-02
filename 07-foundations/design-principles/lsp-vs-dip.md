---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [solid, lsp, dip, design-principles]
---

# LSP 和 DIP 的区别与联系

## 核心结论

[[liskov-substitution-principle]] 和 [[dependency-inversion-principle]] 不矛盾，它们关注的是同一件事的两个层面。

- DIP 关注依赖方向：高层业务应该依赖抽象，而不是依赖具体细节。
- LSP 关注行为契约：具体实现必须真的能替换抽象，而不破坏调用方预期。

一句话理解：

**DIP 要求“依赖抽象”，LSP 要求“抽象必须真实”。**

## 区别

| 原则 | 关注点 | 追问 |
| --- | --- | --- |
| [[dependency-inversion-principle]] | 依赖结构是否合理 | 高层业务是否直接依赖数据库、支付 SDK、消息队列等细节 |
| [[liskov-substitution-principle]] | 实现是否可靠替换抽象 | 换一个实现后，调用方依赖的行为是否仍然成立 |

例如支付场景：

```text
DIP：OrderService 应该依赖 PaymentClient，而不是 WeChatPaySdk
LSP：所有 PaymentClient 实现都必须像一个真正的 PaymentClient
```

DIP 更像“依赖结构原则”，LSP 更像“行为契约原则”。

## 联系

DIP 让高层业务依赖抽象，LSP 保证这些抽象的实现是可靠可替换的。

```text
OrderService -> PaymentClient
                -> WeChatPayClient
                -> AliPayClient
                -> MockPaymentClient
```

如果 `OrderService` 只依赖 `PaymentClient`，这是 DIP 的方向。

如果 `WeChatPayClient`、`AliPayClient`、`MockPaymentClient` 都遵守 `PaymentClient` 的成功、失败、回调、退款语义，这是 LSP 的要求。

## 为什么有人认为它们矛盾

常见原因是：为了 DIP 强行抽接口，但接口设计得太宽、太假，导致实现类无法满足同一契约，于是违反 LSP。

典型例子：

```text
FileStorage
  upload()
  download()
  delete()
```

如果本地存储和 OSS 都支持删除，但某个归档存储不支持删除，只能在 `delete()` 里抛 `UnsupportedOperationException`，那么它虽然表面上依赖了抽象，但违反了 LSP。

调用方以为所有 `FileStorage` 都能删除，实际不是。

这不是 LSP 和 DIP 矛盾，而是抽象设计错了。

## 如何修正

更好的做法是让抽象表达真实能力。

一种拆法：

```text
ReadableStorage
WritableStorage
DeletableStorage
```

另一种拆法：

```text
FileStorage
ArchiveStorage
```

如果删除能力不是所有存储都具备，就不要把 `delete()` 强塞进所有实现必须遵守的共同接口。

这里需要同时看 [[interface-segregation-principle]]：接口过宽时，调用方和实现方都会被迫依赖自己不需要或不具备的能力。

## 和 ISP 的关系

三者应该一起看：

| 原则 | 作用 |
| --- | --- |
| [[dependency-inversion-principle]] | 让业务不直接依赖细节 |
| [[liskov-substitution-principle]] | 保证细节实现不破坏抽象承诺 |
| [[interface-segregation-principle]] | 把过大的抽象拆小，让接口表达真实能力 |

当 DIP 和 LSP 看起来冲突时，通常要检查 ISP：接口是不是太大、太假、太贪心。

## 判断清单

- 高层业务是否依赖稳定抽象，而不是具体 SDK 或基础设施？
- 每个实现是否都能满足抽象承诺的行为？
- 是否存在“不支持该方法”的实现？
- 是否为了复用一个接口，把不相关能力塞进同一个抽象？
- 是否需要用 ISP 把接口拆成更小的能力面？

## 关联

- [[solid]]
- [[liskov-substitution-principle]]
- [[dependency-inversion-principle]]
- [[interface-segregation-principle]]
- [[abstractions]]
- [[polymorphism]]
