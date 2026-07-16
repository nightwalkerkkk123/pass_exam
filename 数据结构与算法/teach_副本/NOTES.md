# NOTES

## Workspace setup
- 教学 workspace 根：`/Users/bytedance/pass_exam/数据结构与算法/teach_副本/`
- 父目录 `/Users/bytedance/pass_exam/数据结构与算法/` 是学习上下文：
  - `原始资料/`：两本书的原始 PDF + 提取的纯文本/元数据（`算法图解-提取文本.txt`、`啊哈算法-提取文本.txt` 等），只在需要核对原文措辞时查阅
  - `skill/bhargava-algorithms/`：**内容技能** —《算法图解》11 章结构化知识库（SKILL.md + glossary.md + patterns.md + cheatsheet.md + chapters/）
  - `skill/aha-algorithms/`：**内容技能** —《啊哈！算法》9 章结构化知识库，与上面互补，专攻图论进阶

## 双技能教学法（沿用 operating_systems 的成功模式）
**teach（方法）+ skill/bhargava-algorithms + skill/aha-algorithms（内容）**：
- teach：Socratic 节奏、一节课一个核心概念、先复习激活旧知再叠加新写法、AskUserQuestion 出题验证理解
- skill/*：每节课从对应 `chapters/*.md` 拉取权威的核心思想/关键概念/常见陷阱/参考表格，不凭空造术语
- 工作流：每节课开始 → 读对应 skill 的 chapter 文件锁定概念和陷阱 → 决定 C 语言实现细节 → 按 teach 方法讲 → 自测题验证 → 视情况写 learning record

## Learner profile
- 称呼：她
- **真实起点**（2026-07-16 诊断）：C 语言语法 + 数组/链表/栈/队列**已经学过，但不熟练**——不是零基础。这意味着：
  - 不需要重讲"什么是指针/循环"
  - 但也不能默认她记得具体算法的代码写法（比如选择排序的双重循环边界），每个算法仍需完整过一遍代码，只是节奏可以比零基础快
  - 复习类语言优先于"从头教"类语言（"回忆一下……"比"这是……"更合适开场）
- 学习方法偏好（继承自本仓库全局教学人设）：每阶段结束前必须让她复述理解；用 AskUserQuestion 出选择题验证，打乱正确选项顺序，提交前不公布答案；可按需要用 ELI5/ELI14/ELI 实习生分层解释
- 两本书整合方式：**不交叉，按书本顺序独立开课**——先学完《算法图解》(Lesson 1-10)，再学《啊哈！算法》(Lesson 11-19)，见 MISSION.md 的完整课程目录
- 代码语言：**统一 C**（含《算法图解》原本是 Python 的章节，讲解时改写为 C）

## Lesson 页面约定
- 本工作区其余课程（operating_systems 等）的 lesson 都是**单文件内联 `<style>`**，没有共享 `assets/` 目录——延续这个约定，保持独立可打开、不依赖外部文件
- 每节课结构：直觉类比 → 关键定义（与对应 skill 的 chapter 对齐）→ 小结表格 → 代码实现（C）→ ≥1 道自测题 + 答案解析 → 关联章节/下一课预告
- 每节课末尾提醒："有不清楚的地方随时问我"（呼应 teach SKILL.md 对 agent-as-teacher 的要求）

## 进度记录
- 2026-07-16：Workspace 初始化，MISSION/NOTES/GLOSSARY/RESOURCES 建立，Lesson 0001（大O表示法与二分查找）产出。
- 2026-07-16：应用户要求继续搭建，通过 subagent 并行分三批产出 Lesson 0002-0019，19 课全部完成并逐个独立核实（HTML结构、quiz-反馈对应、内容是否严格对齐 skill/ 知识库、OCR 诚实标注是否保留）。GLOSSARY.md 和 learning-records/ **仍未填充**——这些只在用户真正走完某一课的"通关条件"、demonstrate 出理解之后才应该写入，不能因为课件已生成就提前当作"已学会"记录。下一步：陪用户从 Lesson 1 开始实际走一遍，而不是默认她已经消化了这19课的内容。
