# PPT 课件文本提取结果

本目录保存 `book/` 下旧版 PowerPoint `.ppt` 课件的文本提取结果。PDF 暂未处理。

## 来源文件

- `第1章.md` ← `../第1章.ppt`
- `第2章.md` ← `../第2章.ppt`
- `第3章.md` ← `../第3章.ppt`
- `第4章.md` ← `../第4章.ppt`
- `第5章.md` ← `../第5章.ppt`
- `第6章_new.md` ← `../第6章_new.ppt`

## 用途

- 给 AI 快速读取老师课件口径。
- 对照 `lessons/` 校准已有课程。
- 后续可作为 `ExamPass-Assistant` 生成知识清单和章节测试的输入。

## 注意

- 这些 `.ppt` 是旧版二进制 PowerPoint 文件，不是 `.pptx`。
- 提取器使用 `olefile` 读取 PowerPoint 文本记录，只抽取文本，不抽取图片。
- 原始课件没有被修改。

## 对应 ExamPass 提取工作区

PPT-only 的 `.epa_work` 已生成在：

`../ppt_only/.epa_work/`

核心 bundle：

`../ppt_only/.epa_work/chapters/ppt_only/_extraction_bundle.json`
