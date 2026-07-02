# Knowledge Skill Library

这个知识库用于系统学习 GitHub 上的开源项目，并把阅读源码、运行实践、架构判断和可复用经验沉淀下来。

它不是聊天记录归档，也不是某个项目的临时进度看板。这里保存的是经过整理后能长期复用的知识：一个项目为什么值得学、源码怎么读、架构如何拆、和同类项目相比差异是什么、以后遇到类似问题可以复用什么方法。

## 快速入口

- [[Home]]
- [[00-inbox/README]]：临时收集入口，先放链接、想法和待整理资料。
- [[01-projects/README]]：每个开源项目一张主卡，记录定位、学习目标、仓库结构、关键模块和结论。
- [[02-reading-notes/README]]：源码阅读笔记，按模块、调用链、PR、Issue 或功能点拆分。
- [[03-patterns/README]]：从项目中抽出的通用工程模式、架构模式、代码组织方式。
- [[04-comparisons/README]]：同类项目横向对比，用于技术选型和判断优先级。
- [[05-practice-labs/README]]：本地运行、改造实验、最小复现和二次开发记录。
- [[06-glossary/README]]：术语、概念、缩写、项目内黑话。
- [[github-project-intake]]
- [[weekly-open-source-learning]]

## 学习一个开源项目的流程

1. 在 [[00-inbox/README]] 放入 GitHub 链接和初步动机。
2. 用 `01-projects/_template-open-source-project.md` 建立项目主卡。
3. 先读 `README`、官方文档、目录结构、启动方式和核心配置。
4. 在 [[02-reading-notes/README]] 记录关键模块的源码阅读过程。
5. 在 [[05-practice-labs/README]] 记录本地运行、调试、改造和验证结果。
6. 把可迁移的做法提炼到 [[03-patterns/README]]。
7. 如果涉及选型，把项目放进 [[04-comparisons/README]] 和同类项目比较。
8. 更新相关 README 索引，保证以后能快速找回。

## Obsidian 约定

1. 内部链接统一使用 Obsidian wikilink，格式为“目录/文件名 + 显示名”。
2. 不使用 `../../` 形式的相对路径。
3. 索引页优先链接到 `README`，项目页优先链接到主卡。
4. 新项目、阅读笔记、对比文档都要同步更新索引。

## 写入原则

1. 结论优先：不要只摘抄资料，要写出自己的判断。
2. 证据清楚：重要结论标明来源，是源码、文档、Issue、运行结果还是推断。
3. 项目事实回项目卡：具体项目的结构、命令、模块放在 `01-projects/` 或 `02-reading-notes/`。
4. 可复用经验进模式库：跨项目有用的架构、代码和流程经验放进 `03-patterns/`。
5. 对比单独沉淀：选型、竞品、技术路线比较放进 `04-comparisons/`。
6. 敏感信息不入库：不保存 token、密码、客户隐私、服务器凭据和未授权资料。

## 推荐命名

项目主卡：

```text
01-projects/<owner>--<repo>.md
```

源码阅读笔记：

```text
02-reading-notes/<owner>--<repo>/<module-or-topic>.md
```

模式总结：

```text
03-patterns/<domain>/<pattern-name>.md
```

对比文档：

```text
04-comparisons/<topic>-comparison.md
```

实践记录：

```text
05-practice-labs/<owner>--<repo>/<experiment>.md
```

## 当前任务

- 先把这个库建设成开源项目学习的稳定容器。
- 每次选择一个 GitHub 项目，按模板建立项目卡。
- 学完一个模块后，至少沉淀一条源码阅读笔记或模式总结。
