# 主业 AI 平台规划

> 范围声明：本文只讨论主业 / 正式工作中的 AI 平台建设，不包含 project-time-management 中的副业、创业项目或个人产品线。

## 1. 平台定位

主业 AI 平台建议定位为：

> 企业内部 AI Enablement Platform / Agent Workbench，用统一的模型、知识库、Agent、工作流与审计能力，帮助研发、BA、QA、运维、合规和管理团队提升正式工作效率。

它不是对外 SaaS，也不是副业 Agent 集合，而是服务主业团队的内部 AI 能力底座。

核心目标：

- 让 AI 嵌入需求分析、方案设计、开发、测试、文档、合规和运营流程。
- 统一模型调用、知识库、Agent 配置、执行日志和权限审计。
- 把一次性 AI 对话沉淀为可复用的工作流、模板和组织知识。

## 2. 需要解决的问题

主业场景里常见痛点：

- 需求理解慢，澄清问题和影响范围依赖人工经验。
- 系统文档、业务规则、接口说明、测试案例分散。
- Solution Design、UAT Script、Release Note、周报等重复文档工作多。
- AI 工具各自使用，无法统一沉淀知识、流程和审计记录。
- 公司内部使用 AI 时需要考虑权限、敏感数据、日志和合规边界。

因此平台本质应是：

```text
统一 AI 底座
+ 企业知识库
+ Agent Runtime
+ Workflow Runner
+ Developer / BA / QA 工具箱
+ Governance & Audit
```

## 3. 核心模块

### 3.1 AI Gateway / 模型网关

负责统一所有模型调用。

能力：

- 多模型接入：OpenAI、DeepSeek、Claude、Gemini、Qwen、本地模型或公司私有模型。
- API Key 管理。
- 模型路由。
- 限流与失败重试。
- 成本统计。
- 调用日志。
- 敏感信息过滤。
- 按用户、团队、项目统计用量。

价值：所有内部 AI 调用统一入口，避免个人工具和脚本分散调用模型。

### 3.2 Enterprise Knowledge Base / 企业知识库

这是平台的资产层。

知识来源：

- BRD / FRD / Solution Design。
- 系统文档、接口文档、数据字典。
- 测试案例、UAT Script、缺陷记录。
- 业务规则、合规要求、SOP。
- 历史会议纪要、项目总结、生产问题记录。
- 代码仓库中的 README、架构说明和关键注释。

能力：

- 文档上传和解析。
- 自动切分、向量化和检索。
- 权限隔离。
- 版本管理。
- 来源引用。
- 资料过期提醒。
- 按业务域、系统、团队打标签。

原则：AI 回答必须尽量引用可信来源，而不是只给无来源结论。

### 3.3 Agent Builder / Agent 构建器

让正式工作中的不同场景可以配置自己的 Agent，而不是每次硬写一个新工具。

Agent 配置项：

- 名称和描述。
- 适用团队 / 场景。
- 模型。
- System Prompt。
- 可访问知识库。
- 可调用工具。
- 输入表单。
- 输出模板。
- 是否需要人工确认。
- 日志级别和权限范围。

示例 Agent：

| Agent | 用途 |
|---|---|
| AML Agentic AI | AML 文档、规则、流程、检查清单和标准化辅助。 |
| FE Skill Agent | 前端规范、组件使用、代码 Review、学习路径辅助。 |
| Requirement Analyst Agent | 需求拆解、澄清问题、User Story 和验收标准生成。 |
| Solution Design Agent | 根据需求和现有知识库生成 Solution Draft。 |
| Test Case Agent | 根据需求生成测试场景、边界条件和回归范围。 |
| Production Issue Agent | 结合日志、变更记录和知识库辅助定位问题。 |

### 3.4 Workflow / Agentic Process

很多主业任务不是一次问答，而是多步骤流程。

示例流程：

```text
需求文档上传
→ AI 提取业务目标
→ AI 识别影响系统
→ AI 生成澄清问题
→ BA 人工确认
→ AI 生成 Solution Draft
→ Tech Lead 审核
→ AI 生成测试建议
→ 输出最终文档
```

需要支持：

- 多步骤流程。
- 条件分支。
- 人工确认节点。
- 文件输入输出。
- 审批和复核记录。
- 结果版本管理。
- 执行日志追溯。

### 3.5 Developer / BA / QA 工具箱

#### BA 工具

- 需求摘要。
- 澄清问题生成。
- User Story 生成。
- Acceptance Criteria 生成。
- Gap Analysis。
- Impact Analysis。
- 流程图草稿。

#### Developer 工具

- 代码解释。
- 改动影响分析。
- API 对照。
- SQL / 数据结构解释。
- 代码 Review。
- Migration 辅助。
- Release Note 生成。

#### QA 工具

- 测试用例生成。
- 边界条件生成。
- 回归范围建议。
- 测试数据建议。
- Defect Summary。
- UAT Script Draft。

#### 管理工具

- 周报生成。
- 项目状态摘要。
- 风险识别。
- 会议纪要。
- Action Item 提取。

### 3.6 Governance / 权限审计

主业平台必须具备治理能力，否则难以在公司内部推广。

能力：

- SSO / 公司账号。
- 用户、团队、项目权限。
- 知识库访问控制。
- 敏感数据脱敏。
- Prompt 和模型调用日志。
- 文件上传、下载、分享审计。
- 人工确认记录。
- 审计导出。
- 外部模型调用边界控制。
- 高风险回答提示和免责声明。

原则：让管理层放心、让团队敢用、让结果可追溯。

## 4. 主业场景优先级

### P0：AML Agentic AI

优先级最高。

原因：

- 已经是主业中的明确 AI 方向。
- 适合文档、规则、流程、检查类 Agentic AI。
- 容易体现平台价值。
- 适合作为第一个标杆 Agent。

可做能力：

- AML 文档知识库。
- AML 规则解释。
- Case / Alert 辅助分析。
- 文档标准化。
- 检查清单生成。
- Solution / Requirement 辅助。

### P0：FE Skill Agent

原因：

- 风险较低。
- 容易落地。
- 能快速让开发团队感受到价值。

可做能力：

- 前端规范问答。
- 组件使用指南。
- 代码 Review Checklist。
- 示例代码生成。
- 技术学习路径。
- 常见错误解释。

### P1：Requirement / Solution Design Agent

这是最通用的主业 Agent。

能力：

```text
输入需求
→ 自动提取业务目标
→ 识别系统影响
→ 生成澄清问题
→ 生成 Solution Draft
→ 生成测试建议
```

### P1：Testing / UAT Agent

适合 BA 和 QA。

能力：

```text
需求文档
→ 测试场景
→ 边界条件
→ 回归范围
→ UAT Script
→ Defect Summary
```

### P2：Production Support Agent

后续再做。

能力：

```text
日志
+ 变更记录
+ 知识库
+ 历史 Incident
→ 初步定位建议
```

## 5. MVP 范围

第一版目标：

> 让 2-3 个主业 Agent 在统一平台中运行，并具备基础知识库、日志、权限和输出保存能力。

### 第一版页面

1. Dashboard / 首页
   - 我的 Agent。
   - 最近使用。
   - 最近文档。
   - 用量。
   - 常用工具。
   - 风险提醒。

2. Agent Center
   - AML Agentic AI。
   - FE Skill Agent。
   - Requirement Analyst Agent。
   - Test Case Agent。

3. Knowledge Center
   - 文档上传。
   - 文档分类。
   - 权限。
   - 标签。
   - 向量化状态。
   - 来源引用。

4. Workflow Runner
   - 选择流程模板。
   - 上传输入。
   - 执行。
   - 人工确认。
   - 输出报告。

5. Admin / Audit
   - 用户。
   - 权限。
   - 调用日志。
   - 模型用量。
   - 成本统计。
   - 敏感数据记录。

### 第一版 Agent

建议先做：

1. AML Agentic AI。
2. FE Skill Agent。
3. Requirement Analyst Agent。

### 第一版不要做

暂时不做：

- 对外客户。
- 副业 Agent。
- Marketplace。
- 复杂计费。
- 大而全项目管理。
- 过重的流程编排。
- 多租户商业 SaaS。

第一版核心是证明：

> 主业正式工作可以被统一 AI 平台提效。

## 6. 推荐技术架构

```text
Agent Workbench
├── Web Console
│   ├── Agent Center
│   ├── Knowledge Center
│   ├── Workflow Center
│   └── Admin / Audit
│
├── Platform API
│   ├── User / Team / Project
│   ├── Agent Config
│   ├── Knowledge Metadata
│   ├── Workflow State
│   └── Audit Log
│
├── AI Gateway
│   ├── Model Routing
│   ├── Key Management
│   ├── Cost Tracking
│   └── Safety Filter
│
├── Agent Runtime
│   ├── Prompt Assembly
│   ├── Tool Calling
│   ├── Memory
│   ├── Human Approval
│   └── Output Parser
│
├── Knowledge Service
│   ├── Document Parse
│   ├── Chunking
│   ├── Embedding
│   ├── Vector Search
│   └── Citation
│
└── Tool Services
    ├── Jira / Confluence
    ├── Git / Repo
    ├── Document Generator
    ├── Test Case Generator
    └── Internal APIs
```

## 7. 核心数据对象

```text
User
Team
Project
Agent
Skill
KnowledgeBase
Document
Workflow
WorkflowRun
Message
ToolCall
AuditLog
ModelUsage
OutputArtifact
```

### Agent

```text
Agent
├── name
├── description
├── model
├── system_prompt
├── enabled_skills
├── knowledge_base_ids
├── tools
├── input_schema
├── output_schema
├── approval_required
└── owner_team
```

### Workflow

```text
Workflow
├── name
├── trigger
├── steps
├── human_review_steps
├── output_template
└── permissions
```

### KnowledgeBase

```text
KnowledgeBase
├── name
├── domain
├── owner_team
├── documents
├── permission_policy
├── version
└── freshness_status
```

## 8. 推荐路线图

### 阶段 1：统一入口

交付：

- 登录。
- Dashboard。
- Agent Center。
- AML Agent 页面。
- FE Skill Agent 页面。
- Requirement Agent 页面。

### 阶段 2：知识库

交付：

- 文档上传。
- 文档分类。
- 向量化。
- 引用来源。
- 权限隔离。
- 知识库问答。

### 阶段 3：Agent Runtime

交付：

- Agent 配置。
- Prompt 模板。
- Skill 选择。
- 工具调用。
- 日志。
- 输出模板。

### 阶段 4：工作流

交付：

- 需求分析流程。
- Solution Draft 流程。
- Test Case 生成流程。
- 人工确认节点。
- 输出报告。

### 阶段 5：治理和推广

交付：

- 权限。
- 审计。
- 成本统计。
- 敏感信息检测。
- 使用报表。
- 团队模板。

## 9. 产品原则

1. 只服务主业正式工作场景，不混副业和创业项目。
2. AI 输出必须可追溯，有引用、有日志、有来源。
3. Agent 必须可配置，不为每个场景硬写代码。
4. 知识和流程要沉淀，不停留在一次性聊天。
5. 高风险动作必须人工确认，AI 辅助而不直接替代审批。

## 10. 总结

主业 AI 平台建议先做成：

> Agent Workbench：以模型网关、企业知识库、Agent Runtime、Workflow 和审计治理为底座，先落地 AML Agentic AI、FE Skill Agent、Requirement Analyst Agent 三个主业场景，证明 AI 能在正式工作中降低需求、开发、测试、文档和流程成本。

优先级：

```text
1. Agent Workbench 首页
2. AML Agentic AI
3. FE Skill Agent
4. Requirement Analyst Agent
5. Knowledge Center
6. Workflow Runner
7. Audit / Usage / Governance
```
