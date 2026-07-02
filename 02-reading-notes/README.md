# Reading Notes

这里保存源码阅读笔记。笔记应该围绕具体模块、调用链、功能点、Issue、PR 或技术问题，不要变成泛泛摘要。

## 当前阅读入口

| 项目 | 已有入口 | 第一篇实质笔记 |
| --- | --- | --- |
| RuoYi/Yudao | [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/README]] | [[02-reading-notes/zhijiantianya--ruoyi-vue-pro/maven-module-structure]] |
| Yudao Cloud | [[02-reading-notes/zhijiantianya--yudao-cloud/README]] | [[microservice-module-map]] |
| ERPNext | [[02-reading-notes/frappe--erpnext/README]] | [[frappe-app-structure]] |
| gin-vue-admin | [[02-reading-notes/flipped-aurora--gin-vue-admin/README]] | [[go-project-structure]] |
| JeecgBoot | [[02-reading-notes/jeecgboot--JeecgBoot/README]] | [[02-reading-notes/jeecgboot--JeecgBoot/maven-module-structure]] |
| Directus | [[02-reading-notes/directus--directus/README]] | [[02-reading-notes/directus--directus/monorepo-structure]] |
| Payload | [[02-reading-notes/payloadcms--payload/README]] | [[02-reading-notes/payloadcms--payload/monorepo-structure]] |
| yudao-ui-admin-vue3 | [[02-reading-notes/yudaocode--yudao-ui-admin-vue3/README]] | [[frontend-module-map]] |
| yudao-ui-admin-vben | [[02-reading-notes/yudaocode--yudao-ui-admin-vben/README]] | [[monorepo-frontend-map]] |

## 推荐目录

```text
02-reading-notes/
└── <owner>--<repo>/
    ├── startup-flow.md
    ├── auth-module.md
    ├── data-model.md
    └── plugin-system.md
```

## 记录要求

- 写清楚阅读目标：为什么读这一段。
- 写清楚证据：源码路径、函数名、配置文件、运行结果。
- 写清楚结论：这段代码如何工作，有什么优缺点。
- 最后沉淀复用点：能否进入 `03-patterns/`。

## 写作约束

- 已创建的笔记必须有实质内容，不能只放标题。
- README 里只有已经存在的笔记使用 Obsidian wikilink。
- 计划中的后续主题可以列出，但不伪装成已存在文件。
- 每篇源码阅读笔记尽量链接一个底层概念，例如 [[solid]]、[[database]]、[[monorepo]]、[[headless-cms]]。
