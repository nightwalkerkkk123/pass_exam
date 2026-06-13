# 学习操作系统

这是一个面向《操作系统》期末复习的个人学习工作区。它不是传统软件项目，而是把教材、课件、AI 教学技能、学习记录和少量参考代码组织在一起，用来支持短周期、高针对性的操作系统应试复习。

## 当前目标

- **考试类型**：学校自命题期末，不是 408 统考。
- **复习范围**：已讲第 1–8 章；第 9–12 章默认低优先级或跳过。
- **学习起点**：接近零基础，需要从直觉和类比开始。
- **成功标准**：能复述核心概念，并能做出选择、填空、简答和计算题。
- **重点题型**：PV 操作、页面置换、磁盘调度、文件分配、成组链接法。

详细任务定义见 `operating_systems/teach/MISSION.md`。

## 目录结构

```text
.
├── README.md                          # 项目说明
├── AGENTS.md                          # AI 代理工作规范
├── workflow/
│   └── ai-workflow.md                # AI 工作流与交接规则
├── operating_systems/                # 操作系统课程主目录
│   ├── 1_操作系统引论/ ~ 6_文件管理/  # 各章节内容（教材+ppt+测试）
│   ├── textbook/                     # 教材原文+汇总资料
│   ├── lessons/                      # AI 生成课程
│   ├── linux/                        # Linux 0.11 源码分析系列
│   ├── build/                        # 构建脚本
│   ├── exams/                        # 综合测试卷
│   ├── reference/                    # 模板
│   ├── teach/                        # 主教学工作区
│   ├── operating_systems_tangxiaodan/ # 汤小丹教材知识库
│   ├── learning-records/             # 学习记录
│   ├── bank/                         # 题库
│   └── MISSION.md/NOTES.md/           # 教学配置
├── advanced_oop/                      # 面向对象高级编程（另一门课程）
├── reference/                        # 参考代码（xv6, egos-2000）
├── skills/                          # 通用技能
│   ├── ExamPass-Assistant/           # 资料转知识清单/测试的辅助技能
│   ├── book-to-skill/                # 资料转 skill 的工具技能
│   ├── caveman/                      # 简化表达/粗暴类比风格技能
│   └── grill-me/                     # 追问式校验理解技能
├── .agent                            # 旧式 AI 教学人设提示
└── .claude                           # 旧式 Claude 教学人设提示
```

## 核心工作区

### `operating_systems/teach/`

主教学状态都在这里：

- `MISSION.md`：为什么学、考试范围、成功标准、教学策略。
- `NOTES.md`：教学偏好、工作区说明、双技能教学法。
- `RESOURCES.md`：教材、课件、外部资源。
- `../learning-records/`：学习记录和复盘，用来判断下一步该教什么。
- `../lessons/`：已经生成的 HTML 微课程。
- `../reference/`：可复用速查资料，若不存在可按需创建。

### `operating_systems/operating_systems_tangxiaodan/`

教材内容知识库：

- `SKILL.md`：12 章结构化索引。
- `textbook/ch*.md`：按章拆分的教材整理。
- `textbook/术语表.md`：标准术语。
- `textbook/算法速查表.md`：调度、页面置换、磁盘调度、银行家算法等。
- `textbook/考研高频考点汇总.md`：参考高频考点，注意本项目以学校自命题为主。

### `operating_systems/textbook/`

- 保存主教材结构和课件，适合查原始定义和老师口径。
- `0_总框架.md` 保存已有人工整理材料，优先用于快速定位老师讲过的内容和作业题。

## 已生成课程

`operating_systems/lessons/` 中已有多节 HTML 课程，覆盖：

1. 总览与题型地图
2. 调度算法
3. 银行家算法
4. 成组链接法
5. 分页基本原理
6. 页面置换
7. 磁盘调度
8. IO 系统
9. 混合索引
10. 进程同步
11. 经典同步问题
12. 进程、线程与死锁

打开课程示例：

```bash
open operating_systems/lessons/0006-page-replacement.html
```

## 推荐复习方式

1. 先读 `operating_systems/teach/MISSION.md`，确认当前考试目标。
2. 再读最新的 `operating_systems/learning-records/*.md`，确认学习状态。
3. 按 `lessons/` 顺序复习，遇到不会的点回查教材知识库。
4. 每章最后必须做题，不能只看概念。
5. 新增课程或复盘后，及时更新 `learning-records/`。

## 给 AI 代理的快速入口

如果你是 AI 代理，请先读：

1. `AGENTS.md`
2. `operating_systems/teach/MISSION.md`
3. `operating_systems/teach/NOTES.md`
4. 最新 2–3 条 `operating_systems/learning-records/*.md`
5. 与当前任务相关的教材章节或算法速查表

更详细的协作流程见 `workflow/ai-workflow.md`。

## 不要误判项目性质

- 当前目标不是开发一个操作系统。
- `reference/egos-2000/` 是参考材料，不是主任务。
- 当前目标不是做 408 难题集，而是服务学校期末。
- 不要把内容一次性讲满；每节课只解决一个关键概念或一类题。