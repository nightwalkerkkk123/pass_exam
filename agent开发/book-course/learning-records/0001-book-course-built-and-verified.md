# 书精读课（book-course）建成并全量核验

`book-course/` 作为 agent开发工作区的**第三条 track** 已建成：57 节 HTML 微课（0001–0057）+ 门户 index + MISSION/NOTES/GLOSSARY(86 词)/RESOURCES/SKILL + 专属样式 `assets/book.css`。真实源是李博杰《深入理解 AI Agent》10 章原文，按核心公式 `Agent=LLM+上下文+工具` 组织。

**这改变未来会话的什么**：教「书里的原理」走这门课，不要重建；它与前两门（`from-zero/`、`lessons/`）互补——那两门落到 `mino_server` 代码行号，这门落到书里的概念/图号/实验/开源项目目录（`chapterN/`），两种 grounding 别混。授课按仓库教学人设交互式推进（复述→补缺→AskUserQuestion 出题）。

**建法（可复用于"为一本书生成一套课"）**：① 11 个 subagent 并行精读全书 → 结构化 course-map（候选微课/术语/图/配套项目，纯从原文抽取、防幻觉）；② 手写并浏览器验收 1 节金标准，锁定视觉与结构契约；③ 56 个 subagent 各据其 spec + 章节原文**克隆金标准骨架**产出其余各课（写文件的 agent 不加 schema，否则会跳过落盘——见 [[workflow-schema-side-effect-skip]]）。

**Evidence（核验结论）**：57/57 结构齐全（≥2 图/自测/误区/关键定义/结论/导航）；50 处图号 + 64 处项目目录引用**零编造**（逐条比对原文/仓库）；prev/next 链路 0001↔0057 全对；0001/0012/0054/index 四页 headless 渲染确认多种信息图（cacheline/分层 SVG/树形 SVG/trio/表）在深色安全下正常。fan-out 唯一系统性瑕疵是金标准 `.good` 框无 `<p>` 包裹、克隆时多带一个 `</p>`（18 处），已批量修掉——**给 drafter 的骨架里那种"无包裹标签"最易被克隆成不配对标签**，下次金标准就把每个块都写成规整配对。

相关：[[absolute-wording-hallucination-fingerprint]]
