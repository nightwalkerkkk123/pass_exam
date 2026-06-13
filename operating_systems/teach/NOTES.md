# NOTES

## Workspace setup
- 教学 workspace 根: `/Users/wangzihao/Code/pass_exam/operating_systems/teach/`
- 父目录 `/Users/wangzihao/Code/pass_exam/operating_systems/` 是学习上下文：
  - `textbook/`: 主教材结构化整理 + 课件文本
  - `1_操作系统引论/ ~ 6_文件管理/`：各章节内容
  - `reference/egos-2000/`: 教学用小型 OS（清华）
  - `operating_systems_tangxiaodan/`: **教材内容技能**
    - `SKILL.md`: 12 章结构化索引
    - `textbook/术语表.md`: 教材标准术语
    - `textbook/算法速查表.md`: 调度/页面/磁盘/银行家/混合索引公式
    - `textbook/考研高频考点汇总.md`: 408 视角的高频考点
    - `textbook/《汤小丹操作系统第四版》全文结构化整理.md`: 教材全文结构化
    - `textbook/ch0X_*.md`: 8 个章节文件（ch01-08 + ch09-12）

## 双技能教学法（2026-06-10 起）
**teach（方法）+ operating_systems_tangxiaodan（内容）**:
- teach: Socratic 节奏、1 概念/节、ELI5 + 小表 + 单选验证、复述通过
- operating_systems_tangxiaodan: 每节课从术语表/算法速查表/章节文件拉**权威定义**和**考试原文**
- 优势：定义和老师口径一致、不靠记忆推断；公式和算法名以教材为准
- 工作流：每节课开始 → grep 相关章节 + 速查表 → 锁定术语和公式 → 用 teach 方法讲

## Learner profile
- 称呼：她（来自父目录 `.agent` / `.claude` 的人设文件）
- 学习方法偏好：Socratic 教学，维护 checklist，要复述理解，ELI5/14/II 分层，AskUserQuestion 出题并打乱答案顺序
- **真实起点**：用户自评零基础 + Lesson 1 自检 5 题全空 → 零基础是**深的零**，不是听过课但不牢。**每节课只能装 1 个概念**，且必须以她能用自己的话复述作为通过条件。
- 时间约束：1-2 周内考试，每节 lesson 必须直接出题，不能纯讲历史。

## 题库（2026-06-10）
- 位置：`../exams/`
- 7 个 HTML：6 套章节测试（190 题 / 600 分）+ 1 套仿真期末卷（46 题 / 100 分）
- 模板：可交互批改（选择/判断/填空自动判，简答/计算/代码给参考答案）
- 题目来源标注：老师在 PPT 里的作业题/思考题/范例 100% 收录
- 12 节课页脚已挂对应章节测试链接
- 题库使用顺序：lesson → 章节测试 → 错题回 lesson → 仿真期末卷

## Java 编程题精讲（2026-06-10，独立加餐）
- 用户零基础 Java，需讲解 `/Users/wangzihao/Desktop/tmp/` 两道作业题（Stream + RaceTime + 骰子 + myFormat）
- 课时：`../lessons/0013-java-two-exercises-zero-to-hero.html`（零基础逐行讲解 + 自测 5 题）
- 与 OS mission 无关，属跨主题加餐；代码在 Desktop/tmp

## 源码精讲专题（2026-06-13，老师必讲算成绩）
- 位置：`../linux/`（6 节课，1 周专题）
- 主题：Linux 0.11 fork() 源码精讲 + 质疑 + 现代视角
- 关键资源：git clone https://github.com/zhaojiewen/Linux-0.11
- 3 个必读文件：sched.h（task_struct）/ fork.c（copy_process）/ system_call.s（sys_fork 入口）
- 使用顺序：Day 1-6 按序学完 → Day 7 找老师讲
- 关键文档：Day 6 讲稿（lesson 0019）含 8 分钟逐字稿 + 6 张 PPT 大纲 + 5 个老师可能问的问题