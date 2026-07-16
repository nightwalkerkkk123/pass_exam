# Agent 开发 Resources

## Knowledge

### context 管理（主轴）
- [Effective context engineering for AI agents — Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  官方一手资料，提出 context rot、注意力预算、compaction/检索/结构化笔记三种策略。Use for: 一切 context 组装与淘汰决策。

### 评估
- [Your AI Product Needs Evals — Hamel Husain](https://hamel.dev/blog/posts/evals/)
  业界公认最佳 eval 入门，核心主张"从错误分析开始，不是从基础设施开始"。Use for: 从零建 eval 流程。
- [LLM Evals FAQ — Hamel Husain](https://hamel.dev/blog/posts/evals-faq/)
  700+ 工程师课程沉淀的高频问答。Use for: 具体 eval 疑难（判分器选择、样本量、LLM-as-judge 校准）。

### 工具调用
- [Writing effective tools for agents — Anthropic Engineering](https://www.anthropic.com/engineering/writing-tools-for-agents)
  官方工具设计指南：namespacing、返回有意义的上下文、token 效率、工具描述即 prompt。Use for: 工具边界与描述设计。
- [Building Effective AI Agents — Anthropic Engineering](https://www.anthropic.com/engineering/building-effective-agents)
  Agent vs workflow 的经典分类文，"能用 workflow 就不要用 agent"。Use for: 架构选型与模式词汇表。

### 成本与延迟
- [Prompt caching — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
  官方文档：前缀匹配语义（tools → system → messages 顺序）、写入加价 25%、读取省 90%、5min/1h TTL。Use for: 一切缓存与成本归因计算。

## Wisdom (Communities)

- 暂未登记。学习者在字节内部有生产项目环境，内部 AI 工程社区是天然的实践场；外部社区（如 r/LocalLLaMA、Latent Space Discord）待学习者表达意愿后再补。

## Gaps

- 缺一份"模型路由"的高信任一手资料（多数是厂商营销文），待筛选。
- 缺延迟工程（streaming、TTFT 优化）的系统性资源，待搜集。
