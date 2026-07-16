# 全套课程已建成：12 节课 + 速查表，全部落在 mino_server 真实代码

四支柱课程（0001 总纲 + 0002-0012）已生成完毕，母版是用户生产项目 `/Users/bytedance/code/mino-server/mino_server`（MinoServer，Go + Kitex Conductor Agent）。每节课句句落到真实符号（文件名 + 行号 + 常量值），并经"精读→起草→对抗式核验"三段流水线核验：约 300 条代码断言逐条回查，仅 1 条 medium（已修）+ 若干 low（学员可见项已修）。

**Evidence**: workflow `build-agent-dev-course` 完成 33 个 agent 零报错；核验报告确认 0003/0006/0009/0011/0012 全 clear，其余仅低危教学简化。

**Implications**:
- 未来会话的默认动作是**用这些课交互式授课**（按教学人设循序推进、AskUserQuestion 出题校验），而不是重建课程。授课顺序见 [[MISSION.md]] 与 `index.html`。
- context 管理是主轴（0002-0004），其余三支柱都经 context 组织耦合进来——这是全课的中心论点，也是校验用户是否真懂的关键点（见 0012）。
- 代码坐标会随 mino_server 演进漂移：讲解时认文件与符号名，不认死行号；0003 本身就把"行号漂移"做成了一个教学点（cache_prefix_stability_test.go:405 的注释已引用过期行号）。
- 项目成熟度高（全 conductorservice/ + llms/ 仅 2 处 FIXME），教学重心是"解释已有决策的为什么 + 找边界"，而非"教缺失的模式"。
