# AGENTS.md

> 本文件供 AI coding agent 阅读。当前目录 `/Users/wangzihao/template` 是一个**多项目工作区**，每个子目录都是独立的 Git 仓库，分别对应简历、面试、求职、系统架构等不同的开源项目或 AI Skill 包。
>
> **重要前提**：工作区根目录没有任何统一的构建配置（无根级 `package.json`、`pyproject.toml`、`Cargo.toml` 等），**请勿把整个工作区当作单一 monorepo 处理**。绝大多数操作都应进入具体子目录后再执行。

---

## 1. 项目概览

### 1.1 工作区性质

- **根目录无统一构建入口**：每个子项目自带依赖管理、脚本和部署方式。
- **子目录均为独立 Git 仓库**：各自保留 `.git`、LICENSE、README、贡献指南等。
- **文档语言混合**：约半数以上项目以中文 README/文档为主（`ai-interview-platform`、`awesome-architecture`、`backend-agent-resume-scout`、`resume-jd-optimizer-cn`、`shushu-internship-tool`、`shushu-internship-resume-optimizer`、`TechSpar`、`ResumeToJob`、`LapisCV` 中文说明较多），其余以英文为主（`coding-interview-university`、`interview-guide`、`Resume-Matcher`、`resume-tailoring-skill`、`ResumeSkills`）。
- **项目类型多样**：包括完整 Web 应用、Python CLI 工具、AI Agent Skill（Markdown 规则包）、VitePress 文档站、静态简历主题、个人笔记等。

### 1.2 子项目一览

| 路径 | 项目类型 | 主要文档语言 | 技术栈 | 包管理/构建 | 关键入口 |
|---|---|---|---|---|---|
| `ai-interview-platform/` | 全栈 Web 应用（AI 面试平台） | 中文 | Next.js 14 + TypeScript + tRPC + React 18 + Tailwind + Radix UI + Supabase（PostgreSQL）+ 独立 Node.js Voice Relay | `pnpm`（`pnpm-lock.yaml`） | `package.json`：`dev`、`build`、`docker:full`、`test:web`、`test:functional` |
| `awesome-architecture/` | VitePress 文档站（架构知识库） | 中文 | VitePress 1.6、Markdown | `pnpm`（`pnpm-lock.yaml`） | `package.json`：`docs:dev`、`docs:build`、`docs:preview` |
| `backend-agent-resume-scout/` | Codex/Claude Skill（后端/Agent 项目筛选） | 中文 | Markdown 规则 + Python 辅助脚本（GitHub 搜索、仓库拉取、Markdown 转 PDF） | 无（Skill 包，复制到 `~/.codex/skills`） | `backend-agent-project-selector/SKILL.md` |
| `coding-interview-university/` | Markdown 学习计划 | 英文 | 纯 Markdown，无构建 | 无 | `README.md` |
| `interview-guide/` | VitePress 文档站 + 博客 | 英文 | VitePress 1 alpha、Vue 3、Hexo/VitePress 博客 | `yarn`（`yarn.lock`） | `package.json`：`docs:dev`、`docs:build`；`Makefile`：`build` |
| `LapisCV/` | Markdown 简历主题模板 | 中英 | CSS + Markdown + 字体 | `make`（`Makefile`） | `make` / `make all` 生成 `build/` |
| `personal/` | 个人笔记与简历草稿 | 中文 | 纯 Markdown | 无 | 敏感个人资料，勿对外公开 |
| `resume-jd-optimizer-cn/` | AI Skill（中文简历优化） | 中文 | Markdown 规则 + Prompt + Rubric + 模板 + 测试 | 无（Skill 包） | `SKILL.md` |
| `Resume-Matcher/` | 全栈 Web 应用（简历匹配） | 英文 | 后端 FastAPI + Python 3.13；前端 Next.js 16 + React 19 + TypeScript + Tailwind 4 | 后端 `uv`/`pip`（`pyproject.toml`、`requirements.txt`）；前端 `npm`（`package-lock.json`） | 后端：`uv run app`；前端：`npm run dev`；根目录有 `docker-compose.yml`、`Dockerfile` |
| `resume-tailoring-skill/` | Claude Code Skill（简历定制） | 英文 | Markdown 规则 | 无（Skill 包） | `SKILL.md`、`multi-job-workflow.md` |
| `ResumeSkills/` | 多 Agent Skill 集合 | 英文 | 20+ 个 Markdown Skill（`SKILL.md`） | 无（Skill 包） | `skills/<skill-name>/SKILL.md` |
| `ResumeToJob/` | 前端 Web 应用（在线简历制作） | 中英 | Next.js 14 + React 18 + TypeScript + Tailwind + Lexical + Redux + next-intl | `pnpm`（`pnpm-lock.yaml`） | `package.json`：`dev`、`build`、`lint`、`format:src` |
| `shushu-internship-resume-optimizer/` | Python CLI 工具包（实习简历优化） | 中文 | Python ≥3.10，setuptools | `pip`（`pyproject.toml`） | `python -m shushu_internship_tool.achievement_audit` 等 |
| `shushu-internship-tool/` | Python CLI 工具包（实习项目准备） | 中文 | Python ≥3.10，setuptools | `pip`（`pyproject.toml`） | `python -m shushu_internship_tool.repo_audit` 等 |
| `TechSpar/` | 全栈 Web 应用（技术面试训练闭环） | 中文 | FastAPI + LangChain/LangGraph + SQLite；React 19 + Vite + Tailwind 4 | 后端 `pip`（`requirements.txt`）；前端 `npm` | 后端：`uvicorn backend.main:app`；前端：`npm run dev`；`docker compose up --build` |

---

## 2. 构建与运行命令

> **通用原则**：先 `cd` 到目标子目录，再使用对应包管理器执行命令。不要在根目录运行 `npm install`、`pnpm build`、`pytest` 等。

### 2.1 Node.js / Next.js / VitePress 项目

| 项目 | 包管理器 | 开发 | 构建 | 测试/其他 |
|---|---|---|---|---|
| `ai-interview-platform` | `pnpm` | `pnpm install && pnpm dev` | `pnpm build` | `pnpm test:web`、`pnpm test:functional`、`pnpm run docker:full` |
| `awesome-architecture` | `pnpm` | `pnpm install && pnpm docs:dev` | `pnpm docs:build` | `pnpm docs:preview` |
| `interview-guide` | `yarn` | `yarn install && yarn docs:dev` | `yarn docs:build` 或 `make build` | `make build` 会同时构建 docs 和 blog |
| `Resume-Matcher/apps/frontend` | `npm` | `npm install && npm run dev` | `npm run build` | `npm run test`（vitest）、`npm run lint`、`npm run format` |
| `ResumeToJob` | `pnpm` | `pnpm install && pnpm dev` | `pnpm build` | `pnpm lint`、`pnpm format:src` |
| `TechSpar/frontend` | `npm` | `npm install && npm run dev` | `npm run build` | `npm run lint`、`npm run preview` |

### 2.2 Python 项目

| 项目 | Python 版本 | 安装 | 运行示例 | 测试 |
|---|---|---|---|---|
| `Resume-Matcher/apps/backend` | ≥3.13 | `uv sync` 或 `pip install -r requirements.txt` | `uv run app` | `pytest`（按 `pyproject.toml` 配置，默认排除 `eval` 标记） |
| `shushu-internship-tool` | ≥3.10 | `python -m venv .venv && source .venv/bin/activate && python -m pip install -e ".[dev]"` | `python -m shushu_internship_tool.repo_audit --repo ...` | `pytest` |
| `shushu-internship-resume-optimizer` | ≥3.10 | 同上 | `python -m shushu_internship_tool.achievement_audit ...` | `pytest` |
| `TechSpar` | 未显式限定，依赖要求 Python 3.10+ | `pip install -r requirements.txt`（本地 embedding 额外安装 `requirements.local-embedding.txt`） | `uvicorn backend.main:app --reload --port 8000` | 未提供统一测试命令 |

### 2.3 无需构建的项目

- `coding-interview-university/`：纯 Markdown 学习清单，无需构建。
- `resume-jd-optimizer-cn/`、`resume-tailoring-skill/`、`ResumeSkills/`、`backend-agent-resume-scout/`：AI Skill 包，由对应 Agent 加载 Markdown 规则；无需安装依赖。
- `personal/`：个人笔记，无构建入口。

### 2.4 静态资源/主题项目

- `LapisCV/`：使用 `make` 构建，输出到 `build/obsidian`、`build/typora`、`build/vscode`。
  ```bash
  cd LapisCV
  make          # 构建全部目标
  make clean    # 清理 build/
  ```

---

## 3. 代码组织与模块划分

### 3.1 全栈 Web 应用

- **`ai-interview-platform`**（聆悟 / Aural）
  - `src/app/`：Next.js App Router 路由（仪表盘、候选人面试页 `/i`、API 路由）。
  - `src/components/`：UI 与业务组件。
  - `src/server/`：tRPC 路由与服务端逻辑。
  - `src/lib/`：工具、Supabase 封装、AI 调用、品牌配置。
  - `server/`：独立语音中继服务（`voice-relay.ts`、`openai-voice-relay.ts`）。
  - `supabase/migrations/`：数据库迁移、RLS、函数。
  - `scripts/`：种子数据与开发辅助脚本。
  - `deploy/`：生产部署脚本与 Nginx 模板。

- **`Resume-Matcher`**
  - `apps/backend/app/`：FastAPI 后端主包（`main.py` 入口）。
  - `apps/backend/tests/`：pytest 测试。
  - `apps/backend/e2e_monitor/`：端到端监控与 fixture。
  - `apps/frontend/`：Next.js 16 前端，使用 Tailwind 4、Tiptap、DND Kit。
  - `docker/`：Docker 相关文件。

- **`ResumeToJob`**
  - `src/`：Next.js 页面与组件。
  - `public/`：静态资源。
  - `messages/`：next-intl 多语言 JSON。

- **`TechSpar`**
  - `backend/`：FastAPI 入口与核心 LangGraph 工作流。
    - `backend/graphs/`：简历面试、专项训练、JD 备面、录音复盘、Copilot 预处理等核心流程。
    - `backend/copilot/`：实时辅助策略树、语音流处理。
    - `backend/storage/`：会话与 Copilot 持久化。
  - `frontend/src/pages/`：训练、画像、图谱、题库、Copilot、设置、复盘等页面。
  - `data/users/{user_id}/`：用户隔离的数据目录（画像、简历、知识库、题库、设置、密钥）。
  - `scripts/`：数据导出/导入迁移脚本。

### 3.2 Python CLI 工具包

- **`shushu-internship-tool`** 与 **`shushu-internship-resume-optimizer`**
  - Python 包名均为 `shushu_internship_tool`（历史命名保持兼容）。
  - 代码位于 `skills/shushu-internship-tool/scripts/shushu_internship_tool/`。
  - 模块：`achievement_audit`、`resume_rank`、`interview_pack`、`doc_knowledge`、`repo_audit`、`candidate_score` 等。
  - 入口：既可通过 `python -m shushu_internship_tool.<module>` 调用，也通过 `pyproject.toml` 的 `project.scripts` 注册为控制台命令（如 `shushu-repo-audit`）。

### 3.3 AI Skill / 文档站

- **`resume-jd-optimizer-cn`**：以 `SKILL.md` 为核心，配合 `prompts/`、`templates/`、`rubrics/`、`docs/`、`examples/`、`tests/` 构成完整工作流。
- **`backend-agent-resume-scout`**：`backend-agent-project-selector/SKILL.md` 为入口，`references/` 存放规则、输入模板、搜索/拉取/PDF 生成脚本。
- **`resume-tailoring-skill`**：`SKILL.md`、`multi-job-workflow.md`、`research-prompts.md`、`matching-strategies.md`、`branching-questions.md` 为核心。
- **`ResumeSkills`**：`skills/<skill-name>/SKILL.md`，每个 Skill 独立。
- **`awesome-architecture`**：`tutorial/`（教程）、`templates/`（架构地图）、`cases/`（完整案例）、`.vitepress/`（站点配置）。
- **`interview-guide`**：`docs/`（VitePress 文档）、`blog/`（博客）、`leetcode/`、`behavioral/`。

---

## 4. 代码风格与开发约定

### 4.1 通用原则

- **遵循子项目已有配置**：每个项目自带 `.eslintrc.json`、`.prettierrc`、`pyproject.toml`、`.markdownlint-cli2.jsonc` 等，修改代码时应遵守对应规则。
- **不要跨项目引入依赖**：各项目依赖相互独立，根目录没有 workspace 链接。
- **保持 README/文档语言一致**：中文项目优先使用中文提交说明、注释和文档；英文项目使用英文。
- **Skill 类项目以 Markdown 为主**：修改 `SKILL.md`、`prompts/`、`templates/`、`rubrics/` 时保持原有 frontmatter 和分阶段结构，避免破坏 Agent 解析。

### 4.2 JavaScript/TypeScript 项目

- `ai-interview-platform`：使用 Next.js 14 App Router、tRPC v10、Zod v4、Tailwind CSS 3、Radix UI。
- `Resume-Matcher` 前端：Next.js 16、React 19、Tailwind CSS 4、ESLint 9、Prettier 3、Vitest。
- `ResumeToJob`：Next.js 14、React 18、Tailwind 3.3.2、Lexical 编辑器、Redux Toolkit、next-intl。
- `TechSpar` 前端：React 19、Vite、React Router v7、Tailwind CSS 4。

### 4.3 Python 项目

- `shushu-*` 工具包：`pyproject.toml` 使用 setuptools，测试路径在 `tests/`，pytest 配置在 `pyproject.toml`。
- `Resume-Matcher` 后端：`pyproject.toml` 使用 hatchling，测试使用 pytest 标记（`unit`、`service`、`integration`、`eval`）。
- `TechSpar`：依赖 `requirements.txt`，使用 Pydantic v2、FastAPI、LangChain/LangGraph。

---

## 5. 测试说明

| 项目 | 测试框架 | 运行方式 | 备注 |
|---|---|---|---|
| `ai-interview-platform` | Node 内置 test runner + tsx | `pnpm test:web`、`pnpm test:functional` | 功能测试 `--test-concurrency=1` |
| `Resume-Matcher/apps/backend` | pytest | `pytest` | 默认排除 `eval` 标记（LLM-as-judge 评测） |
| `Resume-Matcher/apps/frontend` | vitest | `npm run test` | — |
| `shushu-internship-tool` | pytest | `pytest` | `addopts = -q` |
| `shushu-internship-resume-optimizer` | pytest | `pytest` | `addopts = -q` |
| 其余项目 | 无统一自动化测试 | — | Skill/文档站/笔记类项目靠人工审阅 |

- 新增代码应尽量补充对应测试；Python 项目修改后运行 `pytest`。
- `Resume-Matcher` 后端的 `eval` 标记测试可能调用真实 LLM，仅在配置了 API Key 时按需运行（`pytest -m eval`）。

---

## 6. 安全与隐私注意事项

- **环境变量与密钥**：
  - `ai-interview-platform` 使用 `.env.local`（基于 `.env.example`），包含 Supabase、LLM、豆包语音等密钥。
  - `TechSpar` 使用 `.env`（基于 `.env.example`），仅配置管理员账号和 `JWT_SECRET`；所有模型/服务密钥由用户在 UI 设置中单独填写，**不应写入 `.env`**。
  - `Resume-Matcher` 后端通过 `.env` 配置 AI 提供商。
  - **切勿将 `.env.local`、`.env`、密钥文件提交到 Git**。

- **个人敏感信息**：
  - `personal/` 目录包含用户个人简历、AI 助手对其个人经历的完整了解等敏感中文 Markdown 文件。
  - **不要读取、修改、复制或向外部输出 `personal/` 中的内容**，除非用户明确要求并授权。

- **求职/简历类工具的反造假原则**：
  - `resume-jd-optimizer-cn`、`shushu-internship-tool`、`shushu-internship-resume-optimizer`、`backend-agent-resume-scout` 均强调**真实性优先**。
  - 不得编造项目、数据、职责；未经验证的内容不能写进最终简历或面试材料。
  - 使用这些工具处理实习/业务材料时，应优先脱敏，不要上传公司内部文档、真实用户数据、密钥或访问凭证。

- **安全策略文件**：
  - `ai-interview-platform/SECURITY.md`、`resume-jd-optimizer-cn/SECURITY.md` 对漏洞报告和隐私有专门说明，重大安全修改前请先阅读。

---

## 7. 部署与发布

- **`ai-interview-platform`**：
  - 本地开发：`pnpm run dev:stack`（同时启动 Web 3000 + 语音中继 8766），或分别运行 `pnpm dev` 与 `pnpm dev:voice`。
  - Docker 全量部署：`pnpm run docker:full`（基于 `.env.local` 与 `docker-compose.yaml`），暴露 Web 4010 与语音中继 4011。
  - 生产部署参考 `deploy/README.md`。

- **`TechSpar`**：
  - 本地：`pip install -r requirements.txt` + `uvicorn backend.main:app`，前端 `cd frontend && npm install && npm run dev`。
  - Docker：`docker compose up --build`，默认暴露后端 8000 和前端 80。

- **`Resume-Matcher`**：
  - 本地：分别启动 `apps/backend`（`uv run app`）和 `apps/frontend`（`npm run dev`）。
  - Docker：`docker-compose.yml` 构建一体化镜像，默认端口 3000。
  - 官方镜像发布在 `ghcr.io/srbhr/resume-matcher`。

- **`awesome-architecture`** / **`interview-guide`**：
  - 构建为静态站点，产物在 `docs/.vitepress/dist` 或 `blog/dist`。
  - `interview-guide` 使用 `make build` 串联 docs 与 blog 构建并合并资源。

- **`LapisCV`**：
  - `make` 生成 Obsidian/Typora/VSCode 三种主题包，产物在 `build/`。

- **Skill 类项目**：
  - 不通过 CI/CD 部署，而是复制到对应 Agent 的 skills 目录（如 `~/.codex/skills`、`~/.claude/skills`、`~/.cursor/skills`）后由 Agent 加载。

---

## 8. 给 AI Agent 的实操建议

1. **先定位子项目**：接到任务时先确认应操作哪个子目录，不要默认在根目录执行命令。
2. **先读对应 README**：每个子项目 README 都包含安装、运行、工作流和项目结构说明，优先作为信息来源。
3. **注意 lockfile**：Node 项目分别使用 `pnpm-lock.yaml`、`yarn.lock`、`package-lock.json`，请使用对应包管理器安装依赖，避免 lockfile 冲突。
4. **Python 工具使用虚拟环境**：`shushu-*`、`Resume-Matcher`、`TechSpar` 都建议创建 `.venv`，并通过 `-e ".[dev]"` 或 `requirements.txt` 安装。
5. **尊重 Skill 项目的规则结构**：修改 prompt、rubric、template 时，保持原有的阶段划分和 frontmatter，不要破坏 Agent 调用入口。
6. **涉及 `personal/` 时保持只读且保密**：除非任务明确要求修改个人文件，否则不主动读取或改动该目录。

---

## 9. 变更记录

- **2026-06-28**：首次创建根目录 `AGENTS.md`。此前根目录不存在该文件，各子项目也均未发现独立的 `AGENTS.md`。
