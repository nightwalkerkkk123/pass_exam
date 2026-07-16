# 《深入理解 AI Agent》精读课 · Resources

高信任一手来源。本课知识以「书」为主源，下列为书内所引、值得回到原文核对的关键外部来源（按三支柱归类，URL 取自原文/配套项目 README；作者未附 URL 者仅记名）。

## Knowledge

### 主源
- [书] **《深入理解 AI Agent：设计原理与工程实践》— 李博杰**（开源）。正文：`原始资料/ai-agent-book/book/introduction.md`、`chapter1.md`–`chapter10.md`、`afterword.md`。Use for: 一切概念、图、实验编号的权威口径。
- [仓库] **配套开源代码 — github.com/bojieli/ai-agent-book**。项目按章组织在 `chapterN/`，与书中「实验 X-Y」一一对应。Use for: 动手把实验跑一遍，把直觉从"读懂"升级到"做过"。
- [补充读物] **《图解大模型》（图灵出版）**。Transformer / 预训练 / 微调的图解入门，与本书 Agent 工程视角互补。Use for: 补第 2、7 章的大模型底层基础。

### 基础与上下文（第 1–3 章）
- [Anthropic] [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — 保持简单/透明/ACI 三原则、workflow vs 自主 Agent 分类、护栏实践（第 1 章直接引用）。
- [Blog] [Shunyu Yao — The Second Half](https://ysymyth.github.io/The-Second-Half/) 与 [ReAct 论文](https://arxiv.org/abs/2210.03629) — 实验 1.1 / ReAct 循环的思想源。
- [Anthropic] [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) — 第 3 章上下文感知检索的出处；配套 LoCoMo (arXiv:2402.17753)、Mem0 (arXiv:2504.19413)。
- [研究] Li & Shi, *Distill, Don't Retrieve: Inference-Time Context Distillation* (2026), https://01.me/research/context-distillation — 第 2 章状态栏/上下文蒸馏的量化依据（作者本人研究）。

### 工具与 Coding Agent（第 4–5 章）
- **MCP（Model Context Protocol）标准 — Anthropic**；**Simon Willison「致命三要素」(lethal trifecta)** — 第 4–5 章工具互操作与执行安全的框架。
- [研究] Li & Shi, *Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents* (arXiv:2606.30383) — 第 5 章可信边界。

### 评估与后训练（第 6–7 章）
- **Scale AI, "Rubrics as Rewards"** — 第 6 章 Rubric 四准则出处；**LMSYS "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"** + [Chatbot Arena](https://chat.lmsys.org/) + Bradley-Terry 模型。
- [论文] Chu 等 (2025), *SFT Memorizes, RL Generalizes*, [arXiv:2501.17161](https://arxiv.org/abs/2501.17161) — 第 7 章 GeneralPoints / V-IRL 对照实验的原始出处。

### 进阶（第 8–10 章）
- [论文] *Alita: Generalist Agent … Maximal Self-Evolution* ([arXiv:2505.20286](https://arxiv.org/abs/2505.20286)) — 第 8 章"最小预定义、最大自我进化"；配 Reflexion / GEPA / MCP-Zero / Voyager。
- [OpenAI] [Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/) — 第 9 章级联/轮次式/全双工三分法出处。
- [论文] Tran & Kiela (2026), *Single-Agent LLMs Outperform Multi-Agent Systems … Under Equal Thinking Token Budgets* ([arXiv:2604.02460](https://arxiv.org/abs/2604.02460)) — 第 10 章"新信息判据"的核心外部依据。

## Wisdom (Communities)
- **开源仓库的 Issues / PR — github.com/bojieli/ai-agent-book**：把实验跑出问题、或对某条原则有异议，去提 issue / PR，是与作者及读者直接切磋的地方。
- 学习者在字节内部有生产 Agent 项目环境，**内部 AI 工程社区**是天然实践场；外部社区（r/LocalLLaMA、Latent Space 等）待表达意愿后再补。

## Gaps
- 第 7 章多数前沿方法（RLVP / On-Policy Distillation / AdaptThink 等）依赖作者团队待发表论文，公开一手 URL 不全；以书正文 + 配套项目 README 为准。
- 部分来源书正文未附 URL（仅记名），核对时以配套项目 `chapterN/README.md` 的引用为二级线索。
