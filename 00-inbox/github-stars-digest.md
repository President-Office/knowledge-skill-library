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

- Starred 项目：101（公开 101，私有 0）
- 最近 7 天新增公开项目：28
- 最近 7 天新增私有项目：0（私有仓库名称不写入公开仓库）
- 最近 7 天有活动的公开项目：40
- 最近 7 天有活动的私有项目：0（仅统计数量）

### 最近新增公开 starred

- [paperclipai/paperclip](https://github.com/paperclipai/paperclip)
- [theBigGavin/marketingdashboard](https://github.com/theBigGavin/marketingdashboard)
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
- [simonlin1212/vibe-astock](https://github.com/simonlin1212/vibe-astock)
- [ccxt/ccxt](https://github.com/ccxt/ccxt)
- [stefan-jansen/zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded)
- [mementum/backtrader](https://github.com/mementum/backtrader)
- [je-suis-tm/quant-trading](https://github.com/je-suis-tm/quant-trading)
- [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading)
- [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant)
- [wangzhe3224/awesome-systematic-trading](https://github.com/wangzhe3224/awesome-systematic-trading)
- [lukeTheNeuromancer/agentic-ai-system-design-primer-zh](https://github.com/lukeTheNeuromancer/agentic-ai-system-design-primer-zh)
- [ix-infrastructure/Ix](https://github.com/ix-infrastructure/Ix)
- [pallavi-shekhar/ai-engineering-interview-questions-company-wise](https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise)
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- [liangdabiao/easy_investment_Agent_crewai](https://github.com/liangdabiao/easy_investment_Agent_crewai)
- [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev)
- [TNT-Likely/PanWatch](https://github.com/TNT-Likely/PanWatch)
- [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)
- [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills)
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)
- [simonlin1212/TradingAgents-astock](https://github.com/simonlin1212/TradingAgents-astock)
- [jundizhou/easy-stock](https://github.com/jundizhou/easy-stock)
- [malevrigns/agent-jev](https://github.com/malevrigns/agent-jev)
- [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev)
- [yibie/jev-engineering-zh](https://github.com/yibie/jev-engineering-zh)

### 最近活动公开项目

| 项目 | 最近提交 | 最新 Release | 近 7 天 Issue/PR |
| --- | --- | --- | --- |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 2026-09-28 `403794ea` | `v1.3.7` 2026-09-13 | 5 / 38 |
| [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | 2026-09-28 `ac699e16` | `v26.9.4.3-stable` 2026-09-27 | 31 / 69 |
| [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) | 2026-09-28 `c8c5478c` | 无 | 16 / 84 |
| [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) | 2026-09-28 `2cf62bae` | `v0.20.0` 2026-09-27 | 9 / 16 |
| [ix-infrastructure/Ix](https://github.com/ix-infrastructure/Ix) | 2026-09-27 `7ef7f89d` | `v0.11.0` 2026-09-26 | 3 / 48 |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 2026-09-27 `95ba6ae7` | 无 | 6 / 49 |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 2026-09-27 `738c8472` | 无 | 21 / 79 |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 2026-09-27 `7598f906` | 无 | 0 / 100 |
| [mutonby/openshorts](https://github.com/mutonby/openshorts) | 2026-09-27 `89f03093` | 无 | 6 / 2 |
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | 2026-09-27 `deb97caa` | `v4.5.84` 2026-09-24 | 13 / 87 |
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 2026-09-27 `2d0285ab` | `career-ops-v1.34.0` 2026-09-24 | 37 / 63 |
| [Lingtai-AI/lingtai](https://github.com/Lingtai-AI/lingtai) | 2026-09-27 `f3a459ac` | `v1.0.10` 2026-09-27 | 1 / 6 |
| [TNT-Likely/PanWatch](https://github.com/TNT-Likely/PanWatch) | 2026-09-27 `5ebd90ad` | `0.15.0` 2026-09-25 | 2 / 20 |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 2026-09-27 `08a1592e` | `v0.5.6` 2026-09-23 | 37 / 63 |
| [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 2026-09-27 `24e3d67e` | `epub-latest` 2026-09-18 | 17 / 1 |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 2026-09-27 `d3fee51a` | `v3.32.0` 2026-09-06 | 11 / 21 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 2026-09-27 `fd914595` | `v1.24.0` 2026-09-25 | 36 / 64 |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 2026-09-27 `0f14d261` | `v2026.916.1` 2026-09-21 | 28 / 72 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 2026-09-27 `09170eec` | `v2.15.0` 2026-08-13 | 3 / 6 |
| [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 2026-09-27 `2ac9084a` | 无 | 0 / 28 |
| [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | 2026-09-27 `2265a013` | `v0.2.23` 2026-09-24 | 3 / 95 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 2026-09-27 `59dc4f04` | 无 | 1 / 7 |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 2026-09-27 `ca8d51c3` | `v0.0.15` 2026-09-22 | 5 / 50 |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 2026-09-27 `c3352738` | 无 | 9 / 20 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 2026-09-27 `3c301956` | 无 | 0 / 100 |
| [gaogaotiantian/viztracer](https://github.com/gaogaotiantian/viztracer) | 2026-09-26 `75a662d6` | `1.1.1` 2025-11-10 | 2 / 3 |
| [jundizhou/easy-stock](https://github.com/jundizhou/easy-stock) | 2026-09-26 `bd47fc3d` | `v1.2.2` 2026-09-22 | 0 / 1 |
| [ollama/ollama](https://github.com/ollama/ollama) | 2026-09-26 `16b4376a` | `v0.34.4` 2026-09-23 | 32 / 68 |
| [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | 2026-09-26 `a4aafa85` | 无 | 1 / 1 |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 2026-09-26 `e40a45ec` | `v0.16.2` 2026-09-08 | 2 / 3 |
| [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | 2026-09-26 `557497b3` | `v0.2.16` 2026-09-26 | 11 / 30 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | 2026-09-26 `4f570385` | `v2.1.160` 2026-06-02 | 1 / 2 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 2026-09-26 `dc676965` | 无 | 5 / 18 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 2026-09-26 `2686b620` | `0.6.11` 2026-09-26 | 11 / 37 |
| [bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book) | 2026-09-26 `56ecb425` | `build-20260923-204840` 2026-09-23 | 0 / 11 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 2026-09-25 `e87bb897` | `v0.0.82` 2026-09-18 | 9 / 3 |
| [github/spec-kit](https://github.com/github/spec-kit) | 2026-09-25 `c00dc055` | `v1.0.12` 2026-09-25 | 39 / 61 |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 2026-09-25 `e0d4d756` | `v0.4.15` 2026-08-23 | 3 / 9 |
| [lukeTheNeuromancer/agentic-ai-system-design-primer-zh](https://github.com/lukeTheNeuromancer/agentic-ai-system-design-primer-zh) | 2026-09-25 `43e4937a` | 无 | 0 / 0 |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 2026-09-25 `68253fc2` | `4.0` 2023-01-05 | 5 / 28 |

### Sources checked

- GitHub REST API `user/starred`（含私有项目；私有名称和详情不写入此公开报告）。
- 公开 starred 项目的仓库元数据、最近提交、最新 Release 和近 7 天 Issue/PR。
- 私有项目只保留数量统计，避免把私有信息发布到公开仓库。

### Validation

- GitHub Actions workflow 执行 `git diff --check`。
- 只有快照发生实质变化时才提交，避免无变化噪声提交。
- 推送后通过 GitHub Contents API 回读远端文件 SHA。
<!-- END GITHUB_STARS_ACTIONS -->
