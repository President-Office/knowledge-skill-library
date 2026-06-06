# 高考相关 Skill / Agent / MCP 项目调研

> 调研范围：GitHub 上与“高考 / Gaokao / 高考志愿 / 高考备考 / skill / agent / RAG / MCP”相关的公开项目。  
> 结论日期：2026-06-06。  
> 说明：这里的“Skill”既包括严格意义上的 Agent Skill / Claude Skill / OpenClaw Skill，也包括可作为高考 Agent 工具层或产品参考的 Agent、RAG、MCP 项目。

## 总体结论

高考相关项目比保险方向更集中，几乎全部都是**中国大陆高考语境**。主要分为四类：

1. **高考志愿填报 Skill / Agent**：围绕省份、分数、位次、选科、专业偏好、城市偏好、风险容忍度，输出“冲 / 稳 / 保 / 垫”等方案。
2. **专业路径测评 Skill**：不只判断“能不能上”，还评估专业路径是否适合学生长期发展。
3. **高考备考辅导 Agent**：面向学科辅导、试卷 RAG、学习规划、情绪疏导。
4. **MCP / 工具层**：提供专业信息查询、分数位次查询等能力，适合挂到志愿填报 Agent 后面。

最值得优先看的项目：

1. `harrylabsj/gaokao-application`：最适合严肃志愿填报。
2. `xiapuyang/gaokao-adi`：适合做专业路径测评。
3. `a18515373115-droid/ZhangXueFeng-skill`：适合研究用户体验和人格化表达。
4. `babyowen/gaokao-daily-skill`：适合做高考情报日报和招生动态监控。
5. `yja2576/mcp-server-gaokao` + `iefnaf/mcp-gaokao`：适合做数据工具层。
6. `chipfighter/gaokao_tutor`：适合研究高考备考多智能体和 RAG 架构。

---

## 一、重点 Skill / Agent 清单

| 项目 | 类型 | 使用范围 | 国家/地区 | 评价 |
|---|---|---|---|---|
| [`a18515373115-droid/ZhangXueFeng-skill`](https://github.com/a18515373115-droid/ZhangXueFeng-skill) | 高考志愿填报 Skill | 张雪峰风格志愿咨询、专业/院校选择、数据来源标注、省份规则适配 | 中国 | 当前 star 较高。更像“人格化 + 数据校验”的高考 Agent Skill，适合研究用户体验和志愿填报话术；但要注意张雪峰风格可能带来表达偏见。 |
| [`harrylabsj/gaokao-application`](https://github.com/harrylabsj/gaokao-application) | AgentSkills-style Skill | 高考志愿填报：省份、分数、位次、选科、偏好、风险容忍度，输出冲/小冲/稳/保/垫方案 | 中国大陆 | 最像严肃志愿填报 skill。强调位次优先、官方源核验、避免“保证录取”。适合做可靠填报助手。 |
| [`xiapuyang/gaokao-adi`](https://github.com/xiapuyang/gaokao-adi) | 高考专业路径 Skill | 按成绩推荐专业 + ADI 专业路径测评 | 中国 | 很有特色。不是单纯按分数排学校，而是评估“这条专业路径走不走得通”。适合和志愿填报系统结合。 |
| [`babyowen/gaokao-daily-skill`](https://github.com/babyowen/gaokao-daily-skill) | OpenClaw agent skill | 高考每日情报、招生新闻、关注高校、中外合办、专业动态、天气和录取数据追踪 | 中国，特别是江苏 2026 考生 | 适合做定时日报/情报系统。不是直接填志愿，而是信息监测。 |
| [`codepa1o/skill-agent-lab`](https://github.com/codepa1o/skill-agent-lab) | Skill 测评系统 | 输入 GitHub Skill URL，拉取 `SKILL.md`，做多轮对话、RAG、Judge 评分 | 中国/通用 | 它不是高考业务 skill，而是用来评测高考/职业规划 skill 的实验台。适合后续评测多个 skill。 |
| [`X-RayLuan/Openclaw-Study-Coach`](https://github.com/X-RayLuan/Openclaw-Study-Coach) | K-12 学习辅导 Skill | 小学/初中/高中全科辅导，语数英、物化生、史地政，含家长 Playbook | 多语言，中国 K-12 语境明显 | 范围比高考更大，适合备考辅导，不专门做志愿填报。 |
| [`chipfighter/gaokao_tutor`](https://github.com/chipfighter/gaokao_tutor) | 高考辅导 Agent | LangGraph 多智能体，情感识别、RAG 试卷检索、个性化学习规划 | 中国 | 技术架构较完整。适合学习多 Agent + RAG + 学习规划，不是标准 Skill 包。 |
| [`yja2576/mcp-server-gaokao`](https://github.com/yja2576/mcp-server-gaokao) | MCP Server | 查询中国高考专业信息，支持 stdio / SSE / streamable-http | 中国 | 适合作为高考 Agent 的工具层。当前工具较少，README 里主要是 `query_major_info`。 |
| [`iefnaf/mcp-gaokao`](https://github.com/iefnaf/mcp-gaokao) | MCP Server | 查询高考分数在对应省份、年份、类别下的排名位次 | 中国 | 很实用的工具型 MCP，适合填报系统调用，但数据覆盖和更新要单独核验。 |
| [`l-encre/essay-coach`](https://github.com/l-encre/essay-coach) | AI 写作教练 | 高考议论文专项训练、范文检索、记忆卡片 | 中国 | 适合语文作文训练，不涉及志愿填报。 |

---

## 二、志愿填报类产品 / Demo

这些项目更像完整应用或 demo，不一定是标准 skill，但可以作为产品形态参考。

| 项目 | 使用范围 | 评价 |
|---|---|---|
| [`05TCLJH/zhangxuefeng-agent`](https://github.com/05TCLJH/zhangxuefeng-agent) | 张雪峰风格升学规划智能体，FastAPI + 前端 + 通义千问 | 小型完整应用，适合参考产品实现；数据可靠性需要核验。 |
| [`Caser-86/gaokao-tianzhiyuan.agent`](https://github.com/Caser-86/gaokao-tianzhiyuan.agent) | 高考填志愿 Agent MVP，FastAPI + Next.js + 管理后台 + chat 技能网关 | 产品结构比较完整，适合参考“志愿填报平台”形态。 |
| [`mear9713/gaokao`](https://github.com/mear9713/gaokao) | AI Agent + RAG 知识库志愿规划系统，院校专业匹配、保研评估、横向对比 | 偏产品原型，适合参考前端和信息架构。 |
| [`wuli2025/gaokaozhiyuan`](https://github.com/wuli2025/gaokaozhiyuan) | 高考志愿 AI 系统，本地优先 AI 工作台/知识库/技能系统 | README 更像通用 AI 工作台 Polaris，高考只是描述里的一个方向，需谨慎评估。 |
| `shuolsure/admission-agent`、`CMS0514/GaoKao-AgentSystem3.0` 等 | 高考志愿 Agent | 多数 star 很少，需要逐个看数据源、维护状态和是否真的有可用数据。 |

---

## 三、推荐排序

### 1. `harrylabsj/gaokao-application`

**定位**：严肃志愿填报 Skill。  
**为什么推荐**：

- 强调省份、年份、分数、位次、选科、批次、偏好等必要上下文；
- 使用省排名 / 位次作为主要匹配信号；
- 支持上传 CSV 录取数据；
- 输出风险分层：`冲 / 小冲 / 稳 / 保 / 垫`；
- 强制官方源验证；
- 明确避免“保证录取”等不安全承诺。

**适合场景**：

- 高考志愿填报咨询；
- 家长/学生初筛方案；
- 和省考试院录取数据、招生计划数据结合；
- 作为后台系统中的 AI 志愿助手。

---

### 2. `xiapuyang/gaokao-adi`

**定位**：专业路径测评 Skill。  
**为什么推荐**：

- 不只回答“能报什么专业”，还评估“这条路是否走得通”；
- ADI 从 `paths / reach / correct / recover` 四个维度打分；
- 适合补足传统志愿填报只看分数和学校的不足；
- 运行时零第三方依赖，便于集成。

**适合场景**：

- 专业推荐；
- 专业横向比较；
- 学生长期路径规划；
- 志愿填报前的专业筛选。

---

### 3. `a18515373115-droid/ZhangXueFeng-skill`

**定位**：张雪峰风格志愿咨询 Skill。  
**为什么推荐**：

- 用户体验强；
- 话术、节奏、情绪价值设计完整；
- v2.0 强调数据来源标注、省份规则适配和情绪危机处理。

**风险点**：

- 人格化表达可能带来刻板判断或表达偏见；
- “张雪峰风格”适合提升可读性，但不应替代官方数据；
- 需要把情绪价值和数据准确性分离评估。

**适合场景**：

- 研究用户体验；
- 志愿咨询话术；
- 家长/学生低门槛解释；
- 作为严肃数据系统外层的表达层参考。

---

### 4. `babyowen/gaokao-daily-skill`

**定位**：高考每日情报 Skill。  
**为什么推荐**：

- 面向每日新闻、招生动态、关注高校、专业组变化、录取数据追踪；
- 支持搜索关键词自优化；
- 强调官方源优先和多源交叉验证。

**适合场景**：

- 定时日报；
- 招生政策监控；
- 目标院校动态追踪；
- 高考倒计时期间的信息提醒。

---

### 5. `yja2576/mcp-server-gaokao` + `iefnaf/mcp-gaokao`

**定位**：高考 Agent 工具层。  
**为什么推荐**：

- MCP 形式便于被 Claude、VS Code、OpenClaw、其他 Agent Host 调用；
- 一个偏专业信息查询，一个偏分数/位次查询；
- 适合挂在志愿填报 Agent 后面，补足结构化查询能力。

**风险点**：

- 数据覆盖和更新频率必须核验；
- 高考填报对数据时效性要求极高，不能只依赖本地历史库；
- 最终仍需回到省考试院、阳光高考、目标院校招生章程。

---

### 6. `chipfighter/gaokao_tutor`

**定位**：高考备考多智能体系统。  
**为什么推荐**：

- 基于 LangGraph；
- 包含学科辅导、学习规划、情绪疏导；
- 集成 RAG 试卷检索和个性化学习规划；
- 技术架构比单一 prompt skill 更完整。

**适合场景**：

- 高考备考辅导；
- 多智能体教育产品；
- 试卷 RAG；
- 学习规划和情绪支持。

---

## 四、国家/地区与省份差异

这些项目几乎全部是**中国大陆高考语境**，不像保险项目那样有美国/国际差异。真正需要注意的是**省份和年份差异**。

高考志愿填报不能只按“全国统一规则”处理，至少要区分：

- 新高考 `3+1+2`、`3+3`、老高考文理分科；
- 各省批次设置不同；
- 院校专业组 / 专业 + 院校 / 平行志愿规则不同；
- 选科要求每年变化；
- 招生计划每年变化；
- 位次比分数更重要；
- 同一分数在不同年份、不同省份含义完全不同；
- 中外合作、地方专项、国家专项、提前批、强基、综评等特殊路径需要单独处理；
- 最终必须以省考试院、阳光高考、目标院校招生章程为准。

---

## 五、对后续建设的建议

如果要在现有项目或后台系统中加入“高考 AI 能力”，建议拆成三层：

```text
1. 数据工具层
   - 省考试院数据
   - 阳光高考
   - 目标院校招生章程
   - 历年录取分/位次
   - 招生计划
   - 专业选科要求
   - MCP 工具：位次查询、专业查询、院校查询

2. 决策 Skill 层
   - gaokao-application：志愿风险分层
   - gaokao-adi：专业路径测评
   - gaokao-daily：招生情报监控

3. 表达与交互层
   - 张雪峰风格可作为解释层参考
   - 但数据判断必须回到官方源和结构化规则
   - 对“保证录取”“一定能上”等话术设安全边界
```

推荐组合：

```text
harrylabsj/gaokao-application
  + xiapuyang/gaokao-adi
  + yja2576/mcp-server-gaokao / iefnaf/mcp-gaokao
  + 官方数据 RAG
  + 可选：ZhangXueFeng-skill 风格表达层
```

---

## 六、一句话总结

高考 skill 里，`gaokao-application` 最适合做可靠志愿填报，`gaokao-adi` 适合做专业路径测评，`ZhangXueFeng-skill` 适合研究用户体验，MCP 项目适合做数据工具层；所有结论都必须按省份、年份、位次和官方招生规则核验。
