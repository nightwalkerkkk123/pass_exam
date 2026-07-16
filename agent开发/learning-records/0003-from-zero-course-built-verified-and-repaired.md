# 从零入门课（13 节）建成 → 全量对抗核验 → 修复，全部落到真实代码

用户要求「基于 mino_server 怎么搭建起 agent 能力，从零面向小白生成一套课程」。这与已有的《四支柱》进阶课互补：进阶课是**解剖学**（成熟系统按关注点横切，装置=「⚠ 类比在这里漏水」），这门是**发育学**（从无状态大脑一层层长成生产 agent，装置=**问题链** `.chain.in`/`.chain.out`：每节承接上一课的痛、引出下一课的新痛）。

产物：`from-zero/` 独立门户（hero=能力叠加塔）+ 13 节课（01 什么是 agent → 02 循环 → 03 messages → 04 system prompt → 05/06 工具 → 07 编排 → 08 可靠性 → 09 压缩 → 10 记忆 → 11 评估 → 12 成本 → 13 收口），主门户加双轨互链横幅。

**过程与三次踩坑（这是本记录的重点）**：
1. 第一轮流水线（精读→起草→核验）：4 份精读质量极高全部成功；但 **11/12/13 三节起草 agent 在 schema 约束下只产出 JSON、跳过了 Write**，文件没落盘；且该流水线还**卡死**（有 agent 占并发槽），01-10 核验没跑完。
2. 恢复流水线：**加固起草**（动作里把 Write 列为「缺一即失败」+ 写完 Read 回读自检 + 回报 writeConfirmed/byteCount）补齐 11/12/13；并对全 13 节补做对抗核验。16 agent 全绿。
3. 修复流水线：核验挖出 5 处 high（01/02/05「streamCallLLM 全仓库唯一」绝对化误导、08 重试逻辑讲反两处、09 把 thresholdToken=120000 错绑成错误恢复阈值）+ 多处 med/low（55≠54 工具、ToolInfo 字段数、08 的 `fill="#fff"` 深色不可读、weaklock「等 10s」误解 TTL 等）。逐条给精确改法并行修复。

**Evidence**：独立 grep 磁盘复核——绝对措辞清零（仅剩 01 里的显式否定句）、55→54、08 无 `fill="#fff"` 且 RetryIf/ELI5/流程图三处一致、09 把无条件 `summarizeForce` 与 `IsBigContext` 判定线解绑；13 个文件首 `<!DOCTYPE html>`、尾 `</html>`、2 条样式链接、每节 2-4 幅图。

**Implications（给未来会话）**：
- 默认动作：用这两门课**交互式授课**，不要重建。入门从 `from-zero/index.html` 的 01 起，进阶见 [[0002-course-scaffolded-from-mino-server]]。
- 两条方法论已沉淀为记忆：`workflow-schema-side-effect-skip`（schema 会让 agent 跳过写文件等副作用）与 `absolute-wording-hallucination-fingerprint`（「唯一/全部」是幻觉指纹）。
- 代码坐标会漂移：认文件+符号名，不认死行号；数值常量（54 工具、5.5min/30min/10min 超时、0.6 阈值、读 0.1×/写 5m 1.25× / 写 1h 2×）已逐条回仓库核对。
- 核验哲学：不信 agent 自我报告（「16 个全绿」是流程绿不是内容对），一切代码断言回仓库独立 grep。
