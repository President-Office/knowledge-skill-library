---
type: practice-lab
project: jeecgboot/JeecgBoot
status: todo
created: 2026-06-30
updated: 2026-06-30
---

# JeecgBoot - 本地运行实验

## 目标

- clone `jeecgboot/JeecgBoot`。
- 跑通后端 `jeecg-boot`。
- 跑通前端 `jeecgboot-vue3`。
- 初始化数据库和 Redis。
- 登录后台。
- 运行一次代码生成或在线表单流程。

## 待确认环境

| 项 | 内容 |
| --- | --- |
| OS | Windows |
| JDK | `pom.xml` 默认 Java 17，注释显示支持 17、21、24、25 |
| Spring Boot | 3.5.5 |
| Maven | 待确认 |
| Node | 待确认 |
| pnpm | 待确认 |
| Database | 待确认 |
| Redis | 待确认 |
| 分支 | `main` |

## 初始入口

后端：

```bash
cd jeecg-boot
mvn clean install
```

前端：

```bash
cd jeecgboot-vue3
pnpm install
pnpm dev
```

以上命令待实际执行后修正。

## 验证标准

- [ ] 后端启动成功。
- [ ] 前端登录页可访问。
- [ ] 数据库初始化成功。
- [ ] Redis 连接成功。
- [ ] 管理端能正常登录。
- [ ] 能定位一个菜单对应的前端页面、后端接口、权限标识和数据库表。
- [ ] 能跑通一次代码生成或在线表单配置。

## 问题记录

| 问题 | 原因 | 解决 |
| --- | --- | --- |
|  |  |  |
