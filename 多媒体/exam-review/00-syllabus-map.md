# 课程结构地图 - 多媒体系统导论 (方山城，2026 春)

> 输入材料：完整课件第二讲到第十二讲（11 个讲次）
> 用途：为后续 5 个并行 agent 提供结构化输入
> 范围：图像 / 视频 / 音频基础 → 压缩算法 → 压缩标准 → 检索 → 深度学习

---

## 1. 总览表 — 11 讲一览（讲次 / 中英标题 / 关键词）

| 讲次 | 中文标题 | 英文标题 | 核心主题关键词 |
|------|----------|----------|---------------|
| L02 | 图形和图像的数据表现 | Image Data Representation | 像素/位图/位平面/灰度图/24-bit 彩色/直方图/颜色查找表/抖动 |
| L03 | 图像和视频中的颜色 | Color in Image and Video | 光谱/CIE XYZ/HIS/HSV/Lab/YCbCr/Gamma/CMYK/伽马校正 |
| L04 | 视频中的基本概念 | Basic Concepts in Video | 逐行/隔行扫描/NTSC/PAL/色度二次采样/HDTV/UHDTV/VGA/HDMI/3D 显示 |
| L05 | 数字音频基础 | Basics of Digital Audio | 声音三要素/采样/奈奎斯特/SNR/SQNR/PCM/DPCM |
| L06 | 无损压缩算法 | Lossless Compression | 信息熵/RLC/Shannon-Fano/Huffman/LZW/算术编码 |
| L07 | 有损压缩算法 | Lossy Compression | 失真度量/MSE/PSNR/率失真/量化/DCT/IDCT |
| L08 | 图像压缩标准 | Image Compression Standards (JPEG) | YCbCr 采样/DCT/Zigzag/DPCM/RLC/熵编码/JPEG 比特流 |
| L09 | 视频压缩技术 I | Video Compression I | 时间冗余/运动补偿/MAD/宏块/MV/搜索算法 |
| L10 | 视频压缩技术 II | Video Compression II | H.261/I 帧/P 帧/B 帧/MPEG-1/2/4/VOP/Mesh/5G+VVC |
| L11 | 基于内容的多媒体检索 | Content-based Multimedia Retrieval (CBIR) | 语义鸿沟/全局特征/角点检测/SIFT/SURF/距离度量/索引 |
| L12 | 深度学习与卷积神经网络 | Deep Learning & CNN | 卷积层/池化/全连接/AlexNet/VGG/GoogleNet/ResNet/损失函数 |

> 注：课件从"第二讲"开始（L01 应为绪论，未提供）；共 11 讲。

---

## 2. 知识图谱 — 讲与讲之间的依赖 / 递进关系

### 主干链路（必修前置链）
- **L02 → L03**：L02 学 RGB 通道基础，L03 拓展到颜色科学（CIE XYZ/HSV/Lab/CMYK/伽马）。
- **L02 → L08**：L02 的 24-bit 彩色图与 8x8 像素块 → L08 JPEG 中 YCbCr 采样与 8×8 DCT 块。
- **L03 → L04**：L03 的 YCbCr/YUV → L04 的视频色度二次采样 4:2:0 / 4:2:2。
- **L05 → L06**：L05 的 PCM/DPCM 差分思想 → L06 的 DPCM/熵编码概念。
- **L06 → L07**：L06 的无损 + 信息熵 → L07 的有损 + 失真度量（PSNR/率失真）；共享编码思想。
- **L07 → L08**：L07 的 DCT + 量化 → L08 JPEG 完整流水线（= L07 理论的工程实例）。
- **L08 → L09 → L10**：L08 JPEG（图像）→ L09 视频帧间冗余 / 运动补偿 → L10 H.261/MPEG（视频标准）。
- **L02/L08 → L11**：L02 像素 + L08 DCT 压缩 + 颜色模型 → L11 全局特征（颜色直方图）/局部特征（DoG/SIFT）。
- **L11 → L12**：L11 的 SIFT/Harris 等手工特征 → L12 CNN 自动学习特征。

### 横向支撑链
- **颜色模型**主线：L02 RGB → L03 YCbCr/HSV/Lab → L04 YUV/YIQ → L08 JPEG-YCbCr 采样。
- **采样/量化**主线：L05 音频采样 → L07 标量/向量量化 → L08 JPEG 量化表。
- **DCT 变换**主线：L07 1D/2D DCT 推导 → L08 JPEG 8×8 DCT 编码 → L10 H.261/MPEG DCT。
- **熵与编码**主线：L05 差分编码 → L06 Huffman → L08 JPEG 熵编码 + DPCM + RLC。

### 应用层（L11-L12）相对独立
- L11 检索是图像底层视觉特征的应用层；L12 CNN 是特征提取的现代替代方案；二者形成"传统 vs 深度"对比。

---

## 3. 考频预判（高频 / 中频 / 低频）

| 讲次 | 预估考频 | 理由 |
|------|----------|------|
| L02 图像数据表现 | **高频** | 计算题集中（图像存储量、灰度转换公式、24-bit→8-bit）；位平面/抖动概念常考 |
| L03 颜色模型 | **高频** | RGB/YCbCr/HSV/Lab 转换、色域、Gamma 校正是选择题/简答题热门 |
| L04 视频基础 | **中频** | 色度二次采样 4:2:0/4:2:2/4:4:4 计算 + HDTV/UHDTV 参数 + 接口对比表 |
| L05 数字音频 | **高频** | 奈奎斯特计算、SNR/SQNR 计算、声音三要素、音频量化位数对应音质 |
| L06 无损压缩 | **高频** | Huffman 编码计算（高频计算题）、熵的计算、Shannon-Fano 步骤、算术编码区间 |
| L07 有损压缩 | **高频** | PSNR 计算公式、量化原理、DCT 推导（数学计算）、率失真概念 |
| L08 JPEG 标准 | **高频** | JPEG 完整流水线为综合大题常考点；DCT→量化→Zigzag→DPCM→RLC→熵编码顺序 |
| L09 视频压缩 I | **中频** | 运动补偿概念、MAD 计算、搜索算法复杂度对比；公式题为主 |
| L10 视频压缩 II | **中频** | H.261 p×64、MPEG I/P/B 帧差异、显示顺序 vs 编码顺序、MPEG-4 VOP 概念 |
| L11 CBIR 检索 | **中频** | SIFT 步骤、Harris 角点响应函数 R、特征描述子对比、距离度量性质 |
| L12 CNN 深度学习 | **高频** | 卷积输出尺寸公式、参数共享、ReLU/Dropout 原理、典型网络结构对比（AlexNet/ResNet） |

**预估频次最高 TOP 5**：L02、L03、L06、L08、L12（计算题密集 + 概念对比密集）。

---

## 4. 跨讲横向主题

| 横向主题 | 涉及讲次 | 核心内容串联 |
|----------|----------|--------------|
| **压缩技术（核心主线）** | L06、L07、L08、L09、L10 | 无损（熵/Huffman/LZW）→ 有损（量化/DCT）→ 图像标准（JPEG）→ 视频压缩（运动补偿/MPEG） |
| **颜色模型** | L02、L03、L04、L08、L11 | RGB（显示）→ YCbCr/HSV/Lab（图像处理）→ YUV（视频）→ 颜色直方图（检索） |
| **采样与量化** | L04、L05、L07、L08 | 视频色度采样 4:2:0 → 音频采样（奈奎斯特）→ 标量/向量量化 → JPEG 量化表 |
| **DCT 变换** | L07、L08、L10 | 1D/2D DCT 数学 → JPEG 8×8 DCT → H.261/MPEG 视频 DCT |
| **冗余类型** | L06、L08、L09 | 空间冗余（DCT/RLC）→ 时间冗余（运动补偿）→ 统计冗余（熵编码）→ 视觉冗余（量化） |
| **帧 / 块结构** | L08、L09、L10 | JPEG 8×8 块 → H.261 16×16 宏块（含 4 个 8×8 亮度 + 2 个 8×8 色度）→ MPEG I/P/B 帧 |
| **特征提取** | L11、L12 | 手工特征（Harris/SIFT/SURF）→ 深度特征（CNN 卷积层） |
| **数据格式 / 标准** | L02、L04、L08、L10 | BMP/GIF/JPEG 文件格式 → HDMI/DP 接口 → JPEG → H.261/MPEG-1/2/4 |
| **信息度量** | L05、L06、L07 | SNR/SQNR（音频）→ 熵/平均码长（无损）→ PSNR/率失真（有损） |
| **差分编码** | L05、L08、L10 | DPCM（音频预测）→ JPEG DC 系数 DPCM → MPEG 帧间差分 |

---

## 5. 关键术语清单 — TOP 30（按主题聚类）

### 5.1 图像基础（L02）
1. **Pixel / 像素** — L02
2. **Bitmap / Bitplane（位图 / 位平面）** — L02
3. **Histogram（直方图）** — L02、L11
4. **Color Lookup Table（颜色查找表）** — L02
5. **Dithering / Halftone（抖动 / 网板打印）** — L02

### 5.2 颜色模型（L03、L04、L08）
6. **RGB / CMY(K)** — L02、L03
7. **CIE XYZ / CIELAB** — L03
8. **HSV / HSL** — L03
9. **YCbCr / YUV / YIQ** — L03、L04、L08
10. **Gamma Correction（伽马校正）** — L03

### 5.3 视频基础（L04）
11. **Interlaced / Progressive Scanning（隔行 / 逐行扫描）** — L04
12. **NTSC / PAL** — L04
13. **Chroma Subsampling 4:2:0（色度二次采样）** — L04、L08、L10
14. **HDTV / UHDTV（4K / 8K）** — L04

### 5.4 音频基础（L05）
15. **Nyquist Theorem（奈奎斯特定理）** — L05
16. **SNR / SQNR（信噪比）** — L05、L07
17. **PCM / DPCM / ADPCM** — L05、L08

### 5.5 无损压缩（L06）
18. **Entropy（信息熵）** — L06
19. **Huffman Coding（哈夫曼编码）** — L06、L08
20. **Shannon-Fano Coding** — L06
21. **LZW（字典编码）** — L06
22. **Arithmetic Coding（算术编码）** — L06
23. **Run-Length Coding（游程编码）** — L06、L08

### 5.6 有损压缩（L07-L08）
24. **MSE / PSNR（均方差 / 峰值信噪比）** — L07
25. **Scalar Quantization / Vector Quantization（标量 / 向量量化）** — L07、L08
26. **DCT / IDCT（离散余弦变换）** — L07、L08、L10

### 5.7 视频压缩（L09-L10）
27. **Motion Compensation / Motion Vector（运动补偿 / 运动矢量）** — L09、L10
28. **Macroblock（宏块）** — L09、L10
29. **I-frame / P-frame / B-frame** — L10
30. **H.261 / MPEG-1 / MPEG-4 / VOP** — L10

### 5.8 检索与深度学习（L11-L12，附补充）
- 补充关键术语：**Harris Corner**（L11）、**SIFT / SURF / MSER**（L11）、**Semantic Gap**（L11）、**Stride / Padding / Receptive Field**（L12）、**ReLU / Dropout**（L12）、**ResNet Residual**（L12）

> 说明：以上 30 项为计算题与概念题最高频考点；其余术语（VGA/HDMI/DisplayPort、CNN 池化层、KNN/RANSAC、TF/PyTorch 等）为次级考点，可在专项复习中补齐。

---

**备注**：本地图仅为结构化导航，每个讲次的详细考题类型与计算题模板由后续 5 个并行 agent 分别深入。