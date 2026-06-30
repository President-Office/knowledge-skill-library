---
type: practice-lab
project: payloadcms/payload
status: todo
created: 2026-06-30
updated: 2026-06-30
---

# Payload - 本地运行实验

## 目标

- clone `payloadcms/payload`。
- 安装 Node 和 pnpm。
- 跑通一个官方模板。
- 创建 collection。
- 验证 Admin Panel、REST/GraphQL、类型生成和数据库映射。

## 待确认环境

| 项 | 内容 |
| --- | --- |
| OS | Windows |
| Node | 待确认 |
| pnpm | 待确认 |
| Database | MongoDB / Postgres / SQLite 待选 |
| 分支 | `main` |
| 当前根版本 | `4.0.0-beta.0` |

## 初始入口

```bash
pnpm install
pnpm build
```

更适合从模板启动：

```bash
cd templates/blank
pnpm install
pnpm dev
```

以上命令待实际执行后修正。

## 验证标准

- [ ] 依赖安装成功。
- [ ] 模板项目启动成功。
- [ ] Admin Panel 可访问。
- [ ] 能创建或修改 collection 配置。
- [ ] REST 或 GraphQL 能访问 collection。
- [ ] 类型生成可用。

## 问题记录

| 问题 | 原因 | 解决 |
| --- | --- | --- |
|  |  |  |
