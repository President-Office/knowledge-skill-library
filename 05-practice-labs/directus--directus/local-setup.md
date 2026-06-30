---
type: practice-lab
project: directus/directus
status: todo
created: 2026-06-30
updated: 2026-06-30
---

# Directus - 本地运行实验

## 目标

- clone `directus/directus`。
- 安装 Node 22 和 pnpm 10。
- 跑通 Directus API 和 Admin App。
- 创建一个 collection。
- 观察数据库表、Directus 元数据和 Admin UI 的关系。

## 待确认环境

| 项 | 内容 |
| --- | --- |
| OS | Windows |
| Node | 根 `package.json` 要求 Node 22 |
| pnpm | 根 `package.json` 要求 pnpm 10.x |
| Database | 待确认 |
| 分支 | `main` |

## 初始入口

```bash
pnpm install
pnpm build
```

以上命令待实际执行后修正。也可以优先尝试仓库自带 `docker-compose.yml`。

## 验证标准

- [ ] 依赖安装成功。
- [ ] API 服务启动成功。
- [ ] Admin App 可访问。
- [ ] 能创建 collection。
- [ ] 能通过 API 读取 collection。
- [ ] 能说明真实业务表和 Directus 元数据表的关系。

## 问题记录

| 问题 | 原因 | 解决 |
| --- | --- | --- |
|  |  |  |
