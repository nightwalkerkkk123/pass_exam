# Agent 开发 Glossary

本术语表是这门课的标准语言。它把 Agent 工程的通用概念，与 `mino_server` 里的**真实实现载体**绑定——每个术语都尽量指向代码中的具体符号，这样"抽象概念"和"你项目里那段代码"在你脑中是同一个东西。

## 主轴：context 管理

**context engineering（上下文工程）**：
在每次 LLM 调用时，策划并维护"最优 token 集合"的一整套策略——回答"什么样的 context 配置最可能产生期望行为"。
_载体_：`conductorservice/agent.go` 的 `buildConductorMessages` → `buildContextPayload` → `streamCallLLM` 管线。
_Avoid_: prompt 工程、拼 prompt。

**context 组装管线（context assembly pipeline）**：
把系统指令、工具定义、参考文档、历史、用户请求按固定顺序拼成一次调用输入的过程。
_载体_：`buildConductorMessages`（顺序：System Prompt → developer messages → hooks 注入文档 → chatMessages）。

**context_info**：
`mino_server` 里对"当轮上下文信息块"的称呼，含空间信息、用户身份、时间、Memory、个性化、AnyGen.md、当前 plan。
_载体_：`buildContextPayload` 返回的 `ConductorContextPayload`。

**context rot（上下文腐烂）**：
context 长度增长时，模型检索与利用其中信息的精度连续退化的现象；容量的**软失效**模式，与"缓存装满报错"的离散失效相反。

**注意力预算（attention budget）**：
把模型注意力视为随 token 数摊薄的有限资源；每加一个 token 都在花这个预算。目标是"最小的高信号 token 集"。

**compaction / 压缩（summarize）**：
当历史逼近上下文窗口时，用模型把旧历史总结成摘要以回收 token 的策略。
_载体_：`conductorservice/summary.go`，触发线 `min(0.8×模型窗口, 200_000)`；`summaryReuseStepThreshold` 防止短期重复总结。

**memory flush**：
压缩发生前，先把对话中的记忆异步落盘（session.jsonl 去重打标），避免压缩丢信息。
_载体_：`conductorservice/memory_flush.go`。

**廉价模型门控（cheap-model gating）**：
用一个便宜小模型先做一个判断（是否该压缩、话题是否相关），再决定要不要动用贵的主模型。
_载体_：`preCompactSummarize` 用 GPT-5.4-Nano 判断话题相关性。

## 成本与延迟

**prefix cache / prompt caching（前缀缓存）**：
厂商按"字节级严格前缀匹配"缓存已处理的 prompt 前段，顺序为 tools → system → messages；命中部分按约 10% 计价，写入加价约 25%，未命中即从**分歧点**起全额重算。
_载体_：`common.NewLLMMessageWithCache1Hour` 打标，`claude/convert.go:convertCacheControl` 映射到 Anthropic ephemeral cache。

**分歧点（divergence point）**：
一次请求的 prompt 与已缓存前缀第一个字节不同的位置；其后所有 token 的缓存全部失效。稳定内容放前、易变内容放后，就是为了把分歧点尽量往后推。
_载体_：`buildContextPayload` 中关于 `<current_plan>` 打破缓存的警告注释。

**cache write / cache read**：
首次写入缓存（比基础输入价贵约 25%）与后续命中读取（约为基础输入价的 10%）。usage 里以 `cache_creation_input_tokens` / `cache_read_input_tokens` 区分。

**模型路由（model routing）**：
按任务/mode 选择不同模型（贵主模型 vs 廉价辅助模型），并在失败时降级兜底。
_载体_：`agent.go:switchModel` / `tryModelFallback`；模型枚举事实源 `llms/common/model.go`。

**PTU 配额 / 准入（PTU quota / admission）**：
对 Provisioned Throughput 的配额管理与请求排队准入控制。
_载体_：`llms/ptuquota/`（`admission.go` / `waitlist.go` / `bucket.go`）。

**流式（streaming）**：
边生成边返回 token，降低**感知延迟**（首 token 时间 TTFT），而非降低总延迟。
_载体_：`llms/stream.go`、`StreamingMessageProcessor`。

## 工具调用

**工具（tool / function）**：
提供给模型调用外部能力的接口定义，其 schema 与描述本身就是**面向模型的 API 文档**，占用 context 预算。
_载体_：`conductorservice/tools.go:GetAllToolServices`，通过 `model.WithTools` 传入。

**不可靠调用方假设（unreliable-caller assumption）**：
把模型当成一个会传错参数、会超时、会重复调的调用方来设计工具边界：幂等、超时、重试、参数校验、可读错误。

**分层超时（tiered timeout）**：
不同工具按预期耗时设不同超时（普通工具 5.5min、subAgent 30min、slides 10min 等）。
_载体_：`conductorservice/toolcall.go` 的超时常量表。

**错误回注（error feedback into context）**：
工具执行失败时，把可读的错误信息作为消息回注给模型让它自我修复（如 JSON 参数损坏时回注修复提示）——error message 是 prompt 的一部分。
_载体_：`toolcall.go` 参数损坏不执行 + 回注修复提示。

## 评估

**eval（评估集）**：
一组固定输入 + 判分逻辑，用来持续观测模型输出质量。与单元测试的差异：判分是**统计性**的，不是确定性 assert。

**判分器（scorer）**：
把模型输出映射成分数的逻辑。三类：精确/包含匹配、代码判分（如工具调用是否正确）、LLM-as-judge。
_载体_：`cmd/memory_eval/eval/scorer.go`（`containsScore` + `toolCallScore` + `llmJudge`）。

**LLM-as-judge（模型裁判）**：
用一个 LLM 给另一个 LLM 的输出打分。核心风险是裁判可信度与自评偏差。
_载体_：`eval/config.go`，judge 默认 `google/gemini-2.5-flash` 走 OpenRouter——**跨厂商**以避免自家模型自评偏袒。

**通过率漂移（pass-rate drift）**：
同一 eval 集的通过率随模型/prompt/代码变化而移动，是 Agent 系统的"回归信号"。

**对抗样本（adversarial case）**：
故意构造"正确行为是拒绝/不回答"的用例，判据为"无高分即通过"。
_载体_：Python 侧 `scorer.py`。
