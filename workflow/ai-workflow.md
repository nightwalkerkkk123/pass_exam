# AI 工作流说明

本文档说明 AI 代理如何在本项目中接手、产出和交接工作。

## 1. 接手项目

每次开始前执行以下阅读顺序：

1. `README.md`：确认项目结构和目标。
2. `AGENTS.md`：确认行为规范。
3. `operating_systems/MISSION.md`：确认考试目标和边界。
4. `operating_systems/NOTES.md`：确认用户偏好和教学法。
5. `operating_systems/learning-records/`：阅读最新 2–3 条学习记录。
6. 按任务读取 `operating_systems/` 中的相关章节、术语表、算法速查表。

## 2. 判断任务类型

### A. 用户要“继续学”

处理流程：

1. 从学习记录判断最近学到哪里。
2. 选择一个最小可学概念。
3. 用类比和小表讲清楚。
4. 出一道选择题或小计算题。
5. 根据用户回答决定是否进入下一概念。
6. 必要时新增学习记录。

### B. 用户要“补资料/课程”

处理流程：

1. 查 `MISSION.md` 确认是否属于考试范围。
2. 查教材知识库和原始资料，锁定标准定义。
3. 生成 `operating_systems/lessons/NNNN-topic.html` 或 `operating_systems/reference/*`。
4. 新增学习记录说明为什么补这节、它解决什么问题。

### C. 用户要“刷题/出卷”

处理流程：

1. 先确认章节范围、题型和难度。
2. 题目必须贴近期末题型，不默认拔高到 408。
3. 答案要包含解题步骤和易错点。
4. 如果是整卷，可参考 `skills/ExamPass-Assistant/` 的流程。

### D. 用户要“整理项目基础设施”

处理流程：

1. 先盘点现有 README、AGENTS、旧提示文件和 docs。
2. 保持根目录文档简洁，详细流程放入 `docs/`。
3. 不移动原始资料、不重命名课程文件，除非用户明确要求。
4. 更新文档后检查链接和路径。

## 3. 教学输出模板

推荐使用以下节奏：

```text
今天只学一个东西：<概念>

1. 先用一句话说：...
2. 类比：...
3. 考试定义：...
4. 小表：...
5. 例题：...
6. 你来判断/复述：...
```

如果用户明显不会，不要继续推进，改用更低阶解释。

## 4. 学习记录模板

新记录建议包含：

```markdown
# <主题>

## 用户表现
- ...

## 关键错因/洞察
- ...

## 本次处理
- ...

## 下一步
- ...
```

具体格式优先参考 `operating_systems/LEARNING-RECORD-FORMAT.md`。

## 5. 常见误区

- 不要把 `参考代码/egos-2000/` 当作主项目开发。
- 不要直接讲完整教材章节，要压成可考试的最小知识块。
- 不要只讲概念不做题。
- 不要因为有 `考研高频考点汇总.md` 就默认按 408 难度教学。
- 不要随意覆盖 `materials/`、`notes/`、第三方技能目录。

## 6. 推荐命令

列出课程：

```bash
find operating_systems/lessons -maxdepth 1 -type f | sort
```

查看最新学习记录：

```bash
ls -1 operating_systems/learning-records | sort | tail
```

搜索某个考点：

```bash
rg "页面置换|FIFO|LRU|缺页" operating_systems/
```

打开某节课：

```bash
open operating_systems/0006-page-replacement.html
```
