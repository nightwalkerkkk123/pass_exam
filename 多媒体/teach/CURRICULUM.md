# 课程计划 · 多媒体系统导论（专题精编版）

> 目标见 [MISSION.md](./MISSION.md)。教学法见 [NOTES.md](./NOTES.md)。
> 21 节专题微课，**一节一窄主题**，输出到 `lessons/NNNN-dash-case.html`。
> 图例：⭐真题直接命中 · 🔴重点 · 🟡中频 · ⚪选择/了解。进度：☐ 待建 / ☑ 已建。

## 生成状态

| # | 文件名 | 主题 | 讲次 | 权重 | 状态 |
|---|---|---|---|---|---|
| 0001 | `0001-what-is-multimedia-exam-map.html` | 什么是多媒体·考试结构与复习地图 | L01 | ⚪ | ☑ |
| 0002 | `0002-pixel-bitmap-image-size.html` | 像素·位图·位平面·图像数据量计算 | L02 | ⭐🔴 | ☑ |
| 0003 | `0003-grayscale-histogram-dithering.html` | 灰度图·24bit→8bit·直方图·抖动 | L02 | ⭐🔴 | ☑ |
| 0004 | `0004-color-science-rgb-cie-hsv-lab.html` | 颜色科学:RGB/CIE-XYZ/HSV/Lab | L03 | 🔴 | ☑ |
| 0005 | `0005-ycbcr-gamma-correction.html` | YCbCr 与 Gamma 校正(为什么·怎么转) | L03 | 🔴 | ☑ |
| 0006 | `0006-video-chroma-subsampling-420.html` | 视频制式·色度二次采样 4:2:0 计算 | L04 | ⭐🔴 | ☑ |
| 0007 | `0007-digital-audio-nyquist-pcm-sqnr.html` | 数字音频·奈奎斯特·PCM/DPCM·SQNR 计算 | L05 | ⭐🔴 | ☑ |
| 0008 | `0008-entropy-rlc.html` | 信息熵与游程编码 RLC | L06 | ⭐🔴 | ☑ |
| 0009 | `0009-shannon-fano-huffman.html` | Shannon-Fano 与 Huffman 编码计算 | L06 | ⭐🔴 | ☑ |
| 0010 | `0010-adaptive-huffman.html` | 自适应 Huffman | L06 | 🟡 | ☑ |
| 0011 | `0011-lzw-dictionary-coding.html` | LZW 字典编码(压缩+解压) | L06 | ⭐🔴 | ☑ |
| 0012 | `0012-arithmetic-coding.html` | 算术编码(编码+解码) | L06 | ⭐🔴 | ☑ |
| 0013 | `0013-distortion-psnr-rate-distortion.html` | 失真度量 MSE/PSNR·率失真理论 | L07 | ⭐🔴 | ☑ |
| 0014 | `0014-quantization-uniform-vector.html` | 量化:均匀vs非均匀·标量vs向量 | L07 | ⭐🔴 | ☑ |
| 0015 | `0015-dct-transform-coding.html` | DCT 变换编码(为什么变换后再编码) | L07 | ⭐🔴 | ☑ |
| 0016 | `0016-jpeg-pipeline.html` | JPEG 完整流水线(zigzag/DPCM/RLC/Huffman) | L08 | ⭐🔴 | ☑ |
| 0017 | `0017-motion-compensation-mv-mad.html` | 运动补偿·MV·MAD·2D 对数搜索 | L09 | ⭐🔴 | ☑ |
| 0018 | `0018-h261-mpeg-ipb-frames.html` | H.261 与 MPEG:I/P/B 帧 | L10 | 🔴 | ☑ |
| 0019 | `0019-cbir-sift-features.html` | CBIR:语义鸿沟·全局vs局部·SIFT | L11 | 🟡 | ☑ |
| 0020 | `0020-retrieval-metrics-recall-precision-map.html` | 图像检索指标 Recall/Precision/AP/mAP | L12 | ⭐🔴 | ☑ |
| 0021 | `0021-cnn-conv-pooling-output-size.html` | CNN 基础:卷积/池化/输出尺寸计算 | L12 | 🔴 | ☑ |

## 每节结构（统一模板）
1. **直觉类比** — 一句话把概念钩到日常经验
2. **关键定义** — 2-4 个核心术语（进 GLOSSARY.md）
3. **小表格** — 对比/参数/步骤
4. **核心内容** — 讲清「是什么·为什么·怎么做」
5. **例题分步**（计算类必备）— 一道按步骤做完的样例
6. **自测题** — ≥1 道，含答案与解释（可折叠）
7. **下一步** — 指向相关节次或 exam-review 复习页

## 优先级（时间紧时的生成顺序）
计算重心先行：**0016 JPEG → 0017 运动补偿 → 0012 算术编码 → 0020 检索指标 → 0009 Huffman → 0006 色度采样 → 0007 音频**，其余随后。
