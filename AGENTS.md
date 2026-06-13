# AGENTS.md

本文件定义 AI 代理在本项目中的工作方式。项目根目录下所有文件默认遵守本规则；若子目录出现更具体的 `AGENTS.md`，以子目录规则为准。

## 项目定位

这是一个《操作系统》期末冲刺学习工作区，不是传统软件工程仓库。AI 的主要职责是帮助学习者在短时间内理解第 1–8 章核心概念、掌握常考题型，并维护可持续复习的资料结构。

## 必读上下文

开始任何实质工作前，至少阅读：

1. `README.md`
2. `operating_systems/teach/MISSION.md`
3. `operating_systems/teach/NOTES.md`
4. 最新的 `operating_systems/learning-records/*.md`
5. 当前任务相关的 `operating_systems/textbook/` 章节、术语表或算法速查表

如果任务涉及生成题目、课程或复盘，必须参考 `operating_systems/LEARNING-RECORD-FORMAT.md`、`MISSION-FORMAT.md` 等格式文件。

## 教学原则

- 默认学习者是深零基础，不要假设她已经理解术语。
- 每次只讲一个核心概念，避免一次塞入过多知识。
- 使用"类比 → 小表 → 例题 → 复述/选择题验证"的节奏。
- 解释要面向学校期末，而不是面向研究、408 拔高或系统实现细节。
- 对计算题必须给出步骤，不只给答案。
- 对概念题要给"考试写法"，而不是只给口语解释。
- 若用户答错，先定位错因，再补最小必要概念。

## 内容优先级

优先级从高到低：

1. 老师已讲章节与作业题
2. `operating_systems/teach/MISSION.md` 中确认的考试目标
3. `operating_systems/` 中已有整理和作业
4. 汤小丹教材知识库
5. 408/王道等外部高频考点
6. `reference/egos-2000/` 的实现细节

注意：本项目是学校自命题期末复习，408 材料只能作为参考，不得反客为主。

## 文件维护规则

### 可以新增或更新

- `README.md`
- `AGENTS.md`
- `workflow/*.md`
- `operating_systems/learning-records/*.md`
- `operating_systems/lessons/*.html`
- `operating_systems/reference/*`
- 与教材整理相关的 markdown 文件

### 谨慎修改

- `operating_systems/textbook/` 下的原始教材和课件：通常只读，不修改。
- `reference/egos-2000/`：第三方参考代码，除非用户明确要求，不修改。
- `.agent`、`.claude`：旧式 AI 提示，可参考但不要随意重写。
- `skills/ExamPass-Assistant/`、`skills/book-to-skill/`：独立工具技能，除非任务要求维护这些工具，否则不改。

## 新增课程规范

新增 HTML 课程时：

- 放在 `operating_systems/lessons/`。
- 命名为 `NNNN-dash-case-topic.html`，编号递增。
- 一节课只讲一个窄主题。
- 必须包含：直觉类比、关键定义、小表格、至少 1 道自测题、答案解释。
- 内容应能独立打开阅读，不依赖当前对话。
- 课程结尾建议给下一步复习建议。

## 新增学习记录规范

新增学习记录时：

- 放在 `operating_systems/learning-records/`。
- 命名为 `NNNN-dash-case-topic.md`，编号递增。
- 记录用户反馈、错因、下一步教学策略，而不是流水账。
- 若改变学习路线或任务目标，必须同步考虑更新 `operating_systems/teach/MISSION.md`。

## 语言和风格

- 默认用中文。
- 语气要直接、清楚、鼓励，但不要哄骗式夸奖。
- 能用表格就不用长段落。
- 能用一道题验证就不要空讲。
- 重要术语第一次出现时要解释。
- 保留教材标准名词，例如：进程同步、临界资源、信号量、请求分页、缺页中断、成组链接法。

## 校验清单

完成任务前检查：

- 是否服务 `MISSION.md` 的期末目标？
- 是否考虑了学习者零基础状态？
- 是否避免了 408/实现细节过度展开？
- 是否更新了必要的学习记录或索引？
- 是否没有误改原始教材、第三方代码或旧提示文件？