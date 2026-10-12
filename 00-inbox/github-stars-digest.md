# GitHub Stars Digest

> 账号：`PeterKZhao`  
> 检查日期：2026-09-28  
> 本次状态：首次建立基线；历史报告不存在，无法做跨周增量比较。  
> 扫描窗口：2026-09-21 至 2026-09-28（活动信号）；starred_at 以 GitHub API 返回为准。

## 分类与关注优先级

### P0：优先跟进

- **Agent 工作台与执行基础设施**：`paperclipai/paperclip`、`microsoft/playwright-mcp`、`CopilotKit/OpenBot`、`LibreChat-AI/LibreChat`。
- **Jev / Agent 决策与技能生态**：`malevrigns/agent-jev`、`kerpopule/hermes-jev-skills`、`typesafe-ai/skills`、`Panniantong/Agent-Reach`。
- **量化研究与多 Agent 投研**：`TauricResearch/TradingAgents`、`simonlin1212/TradingAgents-astock`、`ccxt/ccxt`、`stefan-jansen/machine-learning-for-trading`。

### P1：持续观察

- `ClickHouse/ClickHouse`：分析型数据基础设施，近期版本和提交都很活跃。
- `shanraisshan/claude-code-best-practice`：Agent 工程实践资料，近期持续更新。
- `stefan-jansen/zipline-reloaded`、`mementum/backtrader`：回测基础库，前者仍有维护信号，后者长期低活跃。
- `paperclipai/paperclip`：近期修复工作区快照边界和路径安全，值得跟踪其远程执行模型。

### P2：资料池

- `wilsonfreitas/awesome-quant`、`wangzhe3224/awesome-systematic-trading`、`pallavi-shekhar/ai-engineering-interview-questions-company-wise`、`lukeTheNeuromancer/agentic-ai-system-design-primer-zh`。
- A 股应用与观察面板：`theBigGavin/marketingdashboard`、`simonlin1212/vibe-astock`、`jundizhou/easy-stock`、`TNT-Likely/PanWatch`、`liangdabiao/easy_investment_Agent_crewai`。

## 最近新增 starred

GitHub API 返回本周新增（按 `starred_at` 倒序）：

- 2026-09-27：`paperclipai/paperclip`、`theBigGavin/marketingdashboard`、`shanraisshan/claude-code-best-practice`
- 2026-09-26：`simonlin1212/vibe-astock`、`ccxt/ccxt`、`stefan-jansen/zipline-reloaded`、`mementum/backtrader`、`je-suis-tm/quant-trading`、`stefan-jansen/machine-learning-for-trading`、`wilsonfreitas/awesome-quant`、`wangzhe3224/awesome-systematic-trading`、`lukeTheNeuromancer/agentic-ai-system-design-primer-zh`、`ix-infrastructure/Ix`、`pallavi-shekhar/ai-engineering-interview-questions-company-wise`
- 2026-09-25：`microsoft/playwright-mcp`
- 2026-09-23：`liangdabiao/easy_investment_Agent_crewai`、`Yinsongxu/LLM2Jev`
- 2026-09-22：`TNT-Likely/PanWatch`、`CopilotKit/OpenBot`、`LibreChat-AI/LibreChat`、`TauricResearch/TradingAgents`、`typesafe-ai/skills`、`kerpopule/hermes-jev-skills`、`simonlin1212/TradingAgents-astock`、`jundizhou/easy-stock`、`malevrigns/agent-jev`、`heyjunpenn/awesome-jev`、`yibie/jev-engineering-zh`

## 重要版本、提交与 Issue/PR 活跃度

| 项目 | 最新 Release | 最近提交 / 主题 | 近期活跃度信号 |
| --- | --- | --- | --- |
| `paperclipai/paperclip` | `v2026.916.1`（09-21） | 09-27：扩大未跟踪工作区快照上限，并加强显式文件选择、符号链接父目录和根目录替换校验 | 近期提交包含 134 项聚焦测试、类型检查和 CI 验证说明；适合跟踪远程 Agent 工作区安全边界 |
| `ccxt/ccxt` | `v4.5.84`（09-24） | 09-27：博客 canonical URL 修正 | 09-21 起 Issue 26、PR 142，维护活跃 |
| `stefan-jansen/machine-learning-for-trading` | `v3.1.0-artifacts`（09-20） | 09-24：重写案例 README，移除会随 registry 重建失效的结果数字和哈希 | 近期提交强调可复现性与结果来源分离，适合作为研究知识沉淀样本 |
| `microsoft/playwright-mcp` | `v0.0.82`（09-18） | 09-25：Docker 使用 `tini` 回收孤儿浏览器进程 | 修复运行时资源治理问题，适合纳入浏览器 Agent 部署检查 |
| `CopilotKit/OpenBot` | `v0.0.15`（09-22） | 09-27：为隐藏 coworker 增加可恢复列表 | 近期持续提交，体现 Agent UI 状态可逆性 |
| `LibreChat-AI/LibreChat` | 未读取到最新 Release | 09-27：将后台任务检查呈现为独立 Activity | 09-21 起 PR 484，活跃度很高；需后续关注版本发布与兼容性 |
| `TauricResearch/TradingAgents` | `v0.5.1`（09-24） | 09-24：发布 v0.5.1 | 09-21 起 Issue 64、PR 99；量化多 Agent 方向的主要观察对象 |
| `kerpopule/hermes-jev-skills` | `v0.20.0`（09-27） | 09-28：审计 Epic 状态迁移并补充 root-only installer refresh | 提交与 Release 同步活跃，直接关联当前 Agent skill/记忆工作流 |
| `malevrigns/agent-jev` | 未读取到 Release | 09-23：补充 Laya gap / race 的文档说明 | 仍在快速演进，建议先读模型边界和评测说明再复用 |
| `Panniantong/Agent-Reach` | `v1.5.0`（06-11） | 09-15：新增 Boss 直聘 channel，并强化 CDP 登录态、反爬挑战和 WebSocket 回归测试 | 09-21 起 Issue 2、PR 15；涉及浏览器凭据边界，禁止把本地会话信息写入知识库 |
| `ClickHouse/ClickHouse` | `v26.9.4.3-stable`（09-27） | 09-27：Pretty 格式显示 named Tuple 子列 | 09-21 起 Issue 586、PR 2529；基础设施级高活跃项目 |

## 项目活跃度信号

- Starred 总数：101 个。
- 本次新近 starred 明显集中于 Agent 工具链、Jev 生态、量化交易和 A 股研究应用，说明后续知识沉淀应优先围绕“Agent 执行边界 + 金融研究可复现性”组织。
- 高活跃仓库与低活跃仓库并存：`ClickHouse`、`LibreChat`、`ccxt`、`TradingAgents`、`Paperclip` 近期提交/Issue/PR 密度高；`backtrader` 最近提交停留在 2023 年，宜作为历史参考而非当前方案依据。
- Release 不是所有项目的可靠活跃度指标：部分项目无 Release，但提交和 PR 仍持续；后续应同时检查提交、Issue、PR 和 Release。

## 下周建议

1. 先建立 `paperclipai/paperclip`、`TauricResearch/TradingAgents`、`kerpopule/hermes-jev-skills`、`microsoft/playwright-mcp` 四张项目主卡，记录定位、核心模块、运行边界和可复用原则。
2. 对 `TradingAgents` 与 A 股衍生项目做一次“数据源、回测、Agent 决策、风险提示”横向比较，避免把演示型投研输出当成已验证投资结论。
3. 对 `Paperclip`、`OpenBot`、`LibreChat`、`Playwright MCP` 做 Agent 工作区、浏览器控制、任务状态和权限边界对比。
4. 下一次运行以本文件和 Git 历史为基线，只记录新增 starred、Release 变化、最近提交主题及显著 Issue/PR 活跃度变化。

## Sources checked

- GitHub REST API：`PeterKZhao` 用户信息与全部 101 个 starred（含 `starred_at`）。
- 每个 starred 项目的仓库元数据：描述、语言、stars、forks、默认分支、归档状态、更新时间、最近 push 时间、开放 Issue 数。
- 重点项目的最新 Release、最近提交，以及 2026-09-21 起 Issue/PR 搜索结果。
- 本地 `knowledge-skill-library` 当前 `main`、工作区状态和 git 历史；本文件此前不存在。
- 组织上下文：`President-Office/.github/BOOTSTRAP.md`、`President-Office/policies` 的 README/AGENTS/相关制度文档、`President-Office/ai-project-operating-system` 的 README/AGENTS/开发与测试规则。

## Validation

- 本地工作区同步：`git pull --ff-only origin main` 成功，原工作区无未提交变更。
- 敏感信息检查：报告未写入 token、密码、cookie、会话文件或本地凭据。
- 事实边界：首次运行没有上一版报告，因此未声称任何跨周增量；无法读取 Release 的项目已明确标注。

<!-- BEGIN GITHUB_STARS_ACTIONS -->
## GitHub Actions 自动检查快照

> 本区块由 GitHub Actions 维护；上方分类、判断和手工笔记不会被自动覆盖。

- Starred 项目：181（公开 181，私有 0）
- 最近 7 天新增公开项目：28
- 最近 7 天新增私有项目：0（私有仓库名称不写入公开仓库）
- 最近 7 天有活动的公开项目：40
- 最近 7 天有活动的私有项目：0（仅统计数量）

### 最近新增公开 starred

- [SourceWeft/SourceWeft](https://github.com/SourceWeft/SourceWeft)
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- [cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox)
- [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads)
- [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber)
- [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI)
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)
- [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge)
- [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)
- [rtk-ai/rtk](https://github.com/rtk-ai/rtk)
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)
- [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)
- [obra/superpowers](https://github.com/obra/superpowers)
- [alswl/guides](https://github.com/alswl/guides)
- [alswl/skm](https://github.com/alswl/skm)
- [alswl/mind-forge](https://github.com/alswl/mind-forge)
- [zilliztech/deep-searcher](https://github.com/zilliztech/deep-searcher)
- [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
- [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)
- [dongzhuoyao/academic-figure-generator](https://github.com/dongzhuoyao/academic-figure-generator)
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
- [HytidelLegend/ai-aug-edu](https://github.com/HytidelLegend/ai-aug-edu)

### 最近活动公开项目

| 项目 | 最近提交 | 最新 Release | 近 7 天 Issue/PR |
| --- | --- | --- | --- |
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | 2026-10-12 `cf950ca4` | `v4.5.85` 2026-10-01 | 15 / 66 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 2026-10-12 `8311f78d` | `v0.2.22` 2026-10-08 | 4 / 9 |
| [docling-project/docling](https://github.com/docling-project/docling) | 2026-10-12 `070a6d39` | `v2.138.0` 2026-10-12 | 39 / 61 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 2026-10-12 `9620ccab` | `v1.0.0-rc1` 2026-09-29 | 10 / 90 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 2026-10-12 `63281e52` | 无 | 1 / 55 |
| [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) | 2026-10-12 `5d5b86dd` | `v0.5.1` 2026-10-12 | 35 / 65 |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 2026-10-12 `e0946f94` | `open-design-v0.24.1` 2026-09-24 | 29 / 71 |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 2026-10-12 `a5ad4e48` | 无 | 13 / 87 |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 2026-10-12 `1b4c8038` | `v2026.1005.0` 2026-10-06 | 27 / 73 |
| [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | 2026-10-12 `371b23a4` | `v26.9.16.11-stable` 2026-10-11 | 31 / 69 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 2026-10-12 `0f1b6f62` | `v1.26.0` 2026-10-08 | 24 / 76 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 2026-10-12 `026b6e17` | `v2.15.0` 2026-08-13 | 4 / 14 |
| [ollama/ollama](https://github.com/ollama/ollama) | 2026-10-12 `c1c53629` | `v0.40.3` 2026-10-11 | 29 / 71 |
| [Lingtai-AI/lingtai](https://github.com/Lingtai-AI/lingtai) | 2026-10-12 `d17bfc15` | `v1.0.12` 2026-10-12 | 3 / 12 |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 2026-10-12 `2905162d` | `v0.8.149` 2026-10-11 | 21 / 79 |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 2026-10-12 `bd6939b6` | `v1.3.8` 2026-10-03 | 7 / 76 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | 2026-10-12 `0b41ef47` | `v1.6.0` 2026-07-20 | 1 / 30 |
| [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 2026-10-12 `48754739` | `epub-latest` 2026-09-18 | 30 / 10 |
| [pallavi-shekhar/ai-engineering-interview-questions-company-wise](https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise) | 2026-10-12 `42e4e135` | 无 | 0 / 0 |
| [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | 2026-10-12 `6b287c49` | `v3.9.5` 2026-08-27 | 21 / 9 |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 2026-10-12 `4c9a2759` | 无 | 4 / 19 |
| [TNT-Likely/PanWatch](https://github.com/TNT-Likely/PanWatch) | 2026-10-12 `f1d76d17` | `0.18.1` 2026-10-12 | 7 / 18 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 2026-10-12 `4d0afc1b` | `v1.5.7` 2026-09-02 | 13 / 27 |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 2026-10-12 `7703ca66` | `v0.5.6` 2026-09-23 | 35 / 65 |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 2026-10-12 `7b1c20a6` | `v0.1.2` 2026-10-07 | 7 / 38 |
| [SourceWeft/SourceWeft](https://github.com/SourceWeft/SourceWeft) | 2026-10-12 `5586920f` | `v0.3.0-rc.8` 2026-10-11 | 29 / 40 |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 2026-10-11 `106f9874` | 无 | 10 / 43 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | 2026-10-11 `7afe0e16` | 无 | 1 / 18 |
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 2026-10-11 `f4840b7d` | `career-ops-v1.36.0` 2026-10-10 | 24 / 76 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 2026-10-11 `aac16fbd` | `v3.56.7` 2026-10-11 | 13 / 87 |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 2026-10-11 `9f198716` | `v6.12.2` 2026-10-11 | 64 / 34 |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 2026-10-11 `3a416d89` | 无 | 1 / 99 |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 2026-10-11 `d3c76819` | `v0.1.16` 2026-09-29 | 26 / 74 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 2026-10-11 `27a659f5` | `v0.51.0` 2026-10-02 | 33 / 67 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 2026-10-11 `d1e51716` | `v3.23.0` 2026-10-03 | 10 / 6 |
| [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | 2026-10-11 `f2bdad64` | `v0.1.0` 2026-10-11 | 0 / 3 |
| [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 2026-10-11 `7535907a` | 无 | 0 / 27 |
| [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | 2026-10-11 `988cf971` | `v3.1.0-artifacts` 2026-09-20 | 5 / 13 |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 2026-10-11 `2d228630` | 无 | 4 / 0 |
| [simonlin1212/TradingAgents-astock](https://github.com/simonlin1212/TradingAgents-astock) | 2026-10-11 `e3981af1` | `v0.5.21` 2026-10-11 | 1 / 6 |

### Sources checked

- GitHub REST API `user/starred`（含私有项目；私有名称和详情不写入此公开报告）。
- 公开 starred 项目的仓库元数据、最近提交、最新 Release 和近 7 天 Issue/PR。
- 私有项目只保留数量统计，避免把私有信息发布到公开仓库。

### Validation

- GitHub Actions workflow 执行 `git diff --check`。
- 只有快照发生实质变化时才提交，避免无变化噪声提交。
- 推送后通过 GitHub Contents API 回读远端文件 SHA。
<!-- END GITHUB_STARS_ACTIONS -->
