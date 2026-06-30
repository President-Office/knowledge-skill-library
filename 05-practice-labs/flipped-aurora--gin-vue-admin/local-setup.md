---
type: practice-lab
project: flipped-aurora/gin-vue-admin
status: todo
created: 2026-06-30
updated: 2026-06-30
---

# gin-vue-admin - 本地运行实验

## 目标

- clone `flipped-aurora/gin-vue-admin`。
- 跑通 Go 后端 `server`。
- 跑通 Vue 前端 `web`。
- 初始化数据库。
- 登录管理端。
- 记录一个接口从前端请求到后端处理的完整路径。

## 待确认环境

| 项 | 内容 |
| --- | --- |
| OS | Windows |
| Go | `server/go.mod` 显示 go 1.24.0，toolchain go1.24.2 |
| Node | 待确认 |
| Package manager | npm / pnpm / yarn 待确认 |
| Database | 待确认 |
| Redis | 待确认 |
| 分支 | `main` |

## 初始入口

后端：

```bash
cd server
go mod tidy
go run main.go
```

前端：

```bash
cd web
npm install
npm run dev
```

以上命令待实际执行后修正。

## 验证标准

- [ ] 后端启动成功。
- [ ] 前端登录页可访问。
- [ ] 数据库连接成功。
- [ ] 管理端能正常登录。
- [ ] Swagger 或 API 文档可访问。
- [ ] 能定位一个菜单对应的前端页面、API、后端 router、api、service、model。

## 问题记录

| 问题 | 原因 | 解决 |
| --- | --- | --- |
|  |  |  |
