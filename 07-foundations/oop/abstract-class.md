---
type: foundation
status: draft
created: 2026-07-02
updated: 2026-07-02
tags: [oop, abstract-class, inheritance, abstraction]
---

# 抽象类

## 核心定位

抽象类介于普通类和接口之间：它可以提供部分通用实现，也可以留下必须由子类完成的抽象行为。

一句话理解：

**抽象类适合表达“这些类型有共同骨架，但某些步骤需要子类决定”。**

## 抽象类解决什么

抽象类常用于复用一套稳定流程，同时允许子类定制某些步骤。

例如：

```text
AbstractImportJob
  run()
    validate()
    read()
    transform()
    save()

  abstract read()
  abstract transform()
```

`run()` 是共同流程，`read()` 和 `transform()` 由具体导入任务实现。

## 和接口的区别

如果只需要表达“能做什么”，优先考虑 [[interface]]。  
如果确实存在共同流程骨架和可复用实现，再考虑抽象类。  
如果要表达完整的状态、行为和构造规则，通常使用 [[class]]。

更完整的对比见：[[interface-class-abstract-class]]。

## 和继承的关系

抽象类通常依赖 [[inheritance]]。因此它也会继承继承的风险：

- 父类变化会影响所有子类。
- 子类可能被迫接受不需要的行为。
- 继承层级过深会让行为来源变得难追踪。

使用抽象类时，尤其要关注 [[liskov-substitution-principle]]：子类能否可靠替代抽象父类。

## 常见误区

- 抽象类不是“更高级的接口”。
- 不要为了复用几行代码就建立抽象父类。
- 如果未来变化点不清楚，抽象类会比普通组合更难改。
- 在 Java 单继承限制下，抽象类会占用继承位置，使用前要更谨慎。

## 关联

- [[interface]]
- [[class]]
- [[interface-class-abstract-class]]
- [[inheritance]]
- [[abstractions]]
- [[liskov-substitution-principle]]
- 模板方法模式
