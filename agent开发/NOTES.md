# NOTES — Agent 开发教学工作区

## 学习者画像
- 后端工程师（字节跳动），服务端工程功底扎实：session 管理、缓存淘汰、RPC、CI 都是母语
- 正在向 AI 工程方向转型，有生产/准生产 Agent 项目可实操
- 中文授课，技术术语保留英文（API、context、eval、token 等）

## 教学基材：mino_server（用户的生产项目）

路径 `/Users/bytedance/code/mino-server/mino_server`，Go + Kitex 的多渠道 Agent 编排后端（Conductor 主 Agent + 40+ 工具 + memory 子系统）。**所有课程尽量落到这个项目的真实代码上讲**。已勘察的关键位置：

- context 组装：`biz/domain/dmservice/agents/conductorservice/agent.go` — `buildConductorMessages`(~L1418) / `buildContextPayload`(~L1492，内有 prefix cache 稳定性警告注释) / `streamCallLLM`(~L1545)
- 压缩：同目录 `summary.go`（触发线 `min(0.8*窗口, 200k)`，Nano 门控话题相关性）、`memory_flush.go`
- 工具：`tools.go` / `toolcall.go`（分组并行、分类超时、JSON 损坏回注修复）
- eval：`cmd/memory_eval`（Go 三维打分 contains+toolcall+LLM-judge；judge 跨厂商走 OpenRouter Gemini）+ Python `memory_eval_suite`
- 成本：`common.NewLLMMessageWithCache1Hour`、`switchModel`/`tryModelFallback`、`ptuquota/`

项目成熟度高：prefix cache 稳定性有专门测试（`cache_prefix_stability_test.go`）、分层压缩、廉价模型门控都已实现。教学重心应从"教模式"转向"解释项目里已有决策的为什么 + 找边界情况"（如 toolcall.go L335 附近有并发 context-too-long 的 FIXME）。

## 教学策略
- **借力服务端类比，但每次都标出类比的失效点**——失效点就是新知识所在。学习者自己提出的四段类比（eval≈CI、context≈缓存、工具≈RPC、token≈计费单位）质量很高，作为课程骨架沿用
- 以 context 管理为主轴：它同时决定质量（注意力分布）、成本（前缀缓存命中）、评估可复现性
- 每课一个窄主题，产出能直接用在生产项目上的判断或代码模式
- 用 AskUserQuestion 出题校验理解，答案选项等长、打乱位置
- 进入下一课前必须确认当前课已掌握（动机层 + 细节层）

## 理解清单（持续更新）

### 支柱一：评估
- [ ] 能说清 eval 与 CI 断言的本质差异：统计性 vs 确定性
- [ ] 知道三类判分器（精确匹配 / 代码判分 / LLM-as-judge）各自适用场景
- [ ] 理解"裁判可信度"问题：如何校准 LLM-as-judge
- [ ] 知道 pass@k、通过率漂移的含义与监控方式

### 支柱二：context 管理（主轴）
- [ ] 能解释 context 不是缓存：位置影响注意力（lost in the middle）
- [ ] 理解注意力预算概念：token 越多 ≠ 效果越好
- [ ] 掌握 compaction / 检索 / 结构化笔记三种 context 淘汰策略
- [ ] 能画出自己项目的 context 组装图，说明每段内容为何在那个位置

### 支柱三：工具调用
- [ ] 理解"工具描述即 API 文档，消费者是模型"
- [ ] 能按不可靠调用方假设设计：幂等、超时、重试、参数校验
- [ ] 理解错误信息会被模型读回，error message 是 prompt 的一部分
- [ ] 知道工具集设计的收敛原则：少而正交 > 多而重叠

### 支柱四：成本与延迟
- [ ] 理解 prompt cache 前缀匹配语义，及其对 context 排列的约束
- [ ] 能做 token 成本归因：输入/输出/缓存读写的价格差
- [ ] 知道模型路由的决策框架：什么任务降级到小模型
- [ ] 理解流式输出对感知延迟的作用

### 全局
- [ ] 能说出四支柱的耦合关系：context 组织如何同时影响质量、成本、评估
