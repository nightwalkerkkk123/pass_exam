# 操作系统考前小题+问答题速记页 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `operating_systems/lessons/` 下新建一个独立的考前速记 HTML 页，包含小题速记、问答题速记、易错雷区三块，支持折叠卡片、高频过滤、全部展开/收起、打印优化，并更新课程总门户导航。

**Architecture:** 单文件内联版 HTML + CSS + JS。HTML 直接内联所有知识点卡片；CSS 沿用现有 lessons/ 设计系统；JS 用原生 DOM 操作实现折叠、过滤、展开/收起、打印样式切换。不引入外部框架或构建工具。

**Tech Stack:** HTML5、CSS3、原生 JavaScript（ES6）。

## Global Constraints

- 不改现有 `0013-exam-cheatsheet-map.html` 的内容和结构。
- 不引入外部框架（React/Vue/构建工具）。
- 不添加后端或数据持久化。
- 不覆盖 Ch7–Ch12（项目已确认跳过）。
- 老师口径优先：成组链接法、位示图 0/1 含义、混合索引 D 值等敏感点必须按老师课件/范例写。
- 避免 408 化：不引入超出学校自命题范围的考点。
- 保持零基础友好：每张卡片答案先给结论再补关键词。
- 所有路径以 `E:/CODE/pass_exam` 为根。

---

## File Structure

| 文件 | 动作 | 职责 |
|---|---|---|
| `operating_systems/lessons/0088-exam-cram-cards.html` | 创建 | 主要交付物：小题速记 + 问答题速记 + 易错雷区 |
| `operating_systems/lessons/index.html` | 修改 | 在冲刺区新增一条指向 0088 的链接 |
| `operating_systems/learning-records/0088-exam-cram-cards.md` | 可选创建 | 简短使用记录 |

---

## Task 1: 创建 HTML 骨架与 CSS 设计系统

**Files:**
- Create: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Produces: 一个能正常打开、无样式错误的空白页面，包含 `<head>`、`<body>`、`<style>`、`<script>` 四个基本区域。

- [ ] **Step 1: 写入基础 HTML 骨架**

在文件开头写入：

```html
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="data:,">
<title>操作系统期末 · 小题 + 问答题速记</title>
<style>
  /* CSS 将在 Task 1 Step 2 填充 */
</style>
</head>
<body>
<div class="wrap">
  <!-- 内容将在后续 Task 填充 -->
</div>
<script>
  /* JS 将在 Task 8 填充 */
</script>
</body>
</html>
```

- [ ] **Step 2: 写入 CSS 设计系统**

在 `<style>` 中写入：

```css
:root{
  --ink:#1a2230; --muted:#667; --line:#e3e6ec; --bg:#f7f8fb;
  --blue:#2b6cb0; --blue2:#3182ce; --green:#2f855a; --amber:#b7791f;
  --red:#c53030; --purple:#6b46c1; --soft:#eef4fb;
  --hi:#c53030; --hi-bg:#fdecec; --hi-bd:#f3c4c4;
  --mid:#b7791f; --mid-bg:#fdf6e9; --mid-bd:#ecd9ad;
  --low:#5a6270; --low-bg:#eef1f5; --low-bd:#d6dbe3;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  color:var(--ink); background:var(--bg); line-height:1.7; font-size:16px}
.wrap{max-width:900px; margin:0 auto; padding:28px 20px 90px}
a{color:var(--blue); text-decoration:none} a:hover{text-decoration:underline}
code{font-family:"SF Mono",Menlo,Consolas,monospace; font-size:13px; background:#eef1f6; padding:1px 5px; border-radius:3px}

header.hero{border-bottom:2px solid var(--ink); padding-bottom:18px; margin-bottom:10px}
.eyebrow{color:var(--blue); font-weight:800; letter-spacing:.12em; font-size:12px}
h1{font-size:28px; margin:6px 0 6px}
.lede{color:var(--muted); font-size:14px; margin:0; max-width:70ch}

.scorebar{display:flex; height:44px; border-radius:8px; overflow:hidden; border:1px solid var(--line); margin:16px 0 8px; font-size:12px; font-weight:700}
.seg{display:flex; flex-direction:column; align-items:center; justify-content:center; color:#fff; padding:2px; text-align:center; line-height:1.15}
.seg small{font-weight:600; opacity:.9; font-size:10px}
.seg.sel{background:var(--blue)} .seg.fill{background:var(--blue2)} .seg.judge{background:#4a90c9}
.seg.short{background:var(--amber)} .seg.calc{background:var(--red)}

.topbar{position:sticky; top:0; z-index:20; background:rgba(247,248,251,.95); backdrop-filter:blur(6px);
  border-bottom:1px solid var(--line); margin:14px -20px 22px; padding:10px 20px;
  display:flex; align-items:center; gap:10px; flex-wrap:wrap}
.btn{font:inherit; font-size:12.5px; font-weight:700; border:1px solid var(--line); background:#fff;
  padding:5px 12px; border-radius:16px; cursor:pointer; transition:.15s}
.btn:hover{background:var(--soft)}
.btn.primary{border-color:var(--red); color:var(--red)}
.btn.primary.on{background:var(--red); color:#fff}
.nav{display:flex; gap:5px; flex-wrap:wrap; margin-left:auto}
.nav a{font-size:12px; padding:4px 10px; border-radius:14px; color:var(--blue); border:1px solid transparent}
.nav a:hover{background:var(--soft); text-decoration:none}

h2.zone{font-size:20px; margin:36px 0 6px; border-left:5px solid var(--blue); padding-left:11px; scroll-margin-top:60px}
h3.chap{font-size:16px; margin:22px 0 10px; color:var(--ink); padding-bottom:5px; border-bottom:1px dashed var(--line)}

.card{background:#fff; border:1px solid var(--line); border-radius:10px; margin:10px 0; overflow:hidden;
  box-shadow:0 1px 3px rgba(20,30,60,.04)}
.card .q{display:flex; align-items:flex-start; gap:10px; padding:12px 14px; cursor:pointer; user-select:none}
.card .q:hover{background:#fafbfc}
.card .freq{width:5px; align-self:stretch; flex-shrink:0}
.card.hi .freq{background:var(--hi)} .card.mid .freq{background:var(--mid)} .card.low .freq{background:var(--low)}
.card .badge{font-size:10px; font-weight:800; padding:1px 6px; border-radius:4px; flex-shrink:0}
.card.hi .badge{background:var(--hi-bg); color:var(--hi); border:1px solid var(--hi-bd)}
.card.mid .badge{background:var(--mid-bg); color:var(--mid); border:1px solid var(--mid-bd)}
.card.low .badge{background:var(--low-bg); color:var(--low); border:1px solid var(--low-bd)}
.card .title{flex:1; font-weight:700; font-size:14.5px}
.card .arrow{color:var(--muted); font-size:12px; transition:.15s}
.card.open .arrow{transform:rotate(90deg)}
.card .a{display:none; padding:0 14px 14px 29px; font-size:13.7px; color:var(--ink); border-top:1px dashed var(--line)}
.card.open .a{display:block}
.card .a p{margin:6px 0}
.card .a ul{margin:6px 0; padding-left:20px}
.card .a li{margin:4px 0}
.card .a b{color:var(--red)}

.mines{background:#fff; border:1px solid var(--hi-bd); border-radius:10px; padding:14px 16px; margin:14px 0}
.mine{padding:8px 0; border-bottom:1px dashed var(--line)}
.mine:last-child{border-bottom:none}
.mine .q{font-weight:800; color:var(--hi); font-size:13.5px; margin-bottom:3px}
.mine .a{font-size:13px}
.mine .a b{color:var(--hi)}

.note{background:#ecfdf5; border:1px solid #b7e4c7; border-left:4px solid var(--green); border-radius:8px; padding:12px 14px; margin:16px 0; font-size:13.5px}
.note b{color:var(--green)}

footer{margin-top:50px; padding-top:14px; border-top:1px solid var(--line); color:var(--muted); font-size:12.5px}

body.only-hi .card.mid, body.only-hi .card.low{display:none}
body.only-hi h3.chap:has(+ .card){display:block}

@media (prefers-reduced-motion: reduce){ html{scroll-behavior:auto} .btn,.nav a{transition:none} }
@media (max-width:520px){ h1{font-size:24px} .wrap{padding:20px 15px 80px} .topbar{margin-left:-15px; margin-right:-15px; padding-left:15px; padding-right:15px} }

@media print{
  body{background:#fff}
  .topbar,.btn{display:none !important}
  .card .a{display:block !important}
  .card .arrow{display:none}
  .card{box-shadow:none; break-inside:avoid}
  h2.zone{break-after:avoid}
  a{color:var(--ink)}
}
```

- [ ] **Step 3: 验证文件可打开且无报错**

Run: `ls -la operating_systems/lessons/0088-exam-cram-cards.html`
Expected: 文件存在且大小 > 0。

用浏览器打开 `operating_systems/lessons/0088-exam-cram-cards.html`。
Expected: 页面背景为浅灰、字体正常、无内容但无控制台报错。

---

## Task 2: 实现 Hero 区与 Sticky 控制条

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Consumes: Task 1 创建的 HTML 骨架和 CSS。
- Produces: 页面顶部 Hero 区可见，包含标题、分值条、控制按钮和导航。

- [ ] **Step 1: 在 `<body><div class="wrap">` 内写入 Hero 和 topbar**

```html
<header class="hero">
  <p class="eyebrow">操作系统 · 学校自命题期末 · 考前速记</p>
  <h1>小题 + 问答题速记</h1>
  <p class="lede">考前 30 分钟专用：先想答案，再点开核对。红色标签 = 高频必看，橙色 = 中频，灰色 = 低频。</p>
  <div class="scorebar" role="img" aria-label="选择40分 填空20分 判断10分 简答10分 计算20分">
    <div class="seg sel" style="flex:40">选择 40<small>20×2</small></div>
    <div class="seg fill" style="flex:20">填空 20<small>10×2</small></div>
    <div class="seg judge" style="flex:10">判断 10<small>10×1</small></div>
    <div class="seg short" style="flex:10">简答 10<small>2×5</small></div>
    <div class="seg calc" style="flex:20">计算 20<small>4×5</small></div>
  </div>
</header>

<div class="topbar">
  <button class="btn primary" id="filterBtn" aria-pressed="false">只看高频</button>
  <button class="btn" id="expandBtn">全部展开</button>
  <button class="btn" id="collapseBtn">全部收起</button>
  <nav class="nav" aria-label="页内导航">
    <a href="#small">小题</a>
    <a href="#qa">问答</a>
    <a href="#traps">雷区</a>
  </nav>
</div>
```

- [ ] **Step 2: 验证 Hero 和 topbar 渲染正确**

刷新浏览器。
Expected: 顶部显示标题、分值条、三个按钮、导航链接；Sticky topbar 在滚动时吸顶。

---

## Task 3: 填充小题速记区（Ch1–Ch3）

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Consumes: Task 1 的 CSS 中 `.card`、`.hi/.mid/.low`、`.q`、`.a` 样式。
- Produces: 小题速记区 Ch1–Ch3 的折叠卡片内容。

- [ ] **Step 1: 在 topbar 后插入小题区标题和 Ch1–Ch3 卡片**

```html
<h2 class="zone" id="small">一、小题速记 · 选择 / 填空 / 判断</h2>

<h3 class="chap">Ch1 · 操作系统引论</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">OS 的四大特征是什么？哪个是核心？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>并发、共享、虚拟、异步。</b>并发是核心。</p>
    <ul>
      <li>并发：宏观同时，微观交替（单 CPU 也能实现）。</li>
      <li>共享：互斥共享（临界资源）+ 同时访问。</li>
      <li>虚拟：时分/空分复用，把物理一个变逻辑多个。</li>
      <li>异步：进程走走停停，但 OS 能控制。</li>
    </ul>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">并发和并行的区别？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>并发</b>＝同一<b>时间间隔</b>内交替执行；<b>并行</b>＝同一<b>时刻</b>真正同时执行（需多核）。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">OS 五大功能 + 三类接口</span><span class="arrow">▶</span></div>
  <div class="a">
    <p>五大功能：<b>处理机、存储器、设备、文件管理 + 用户接口</b>。</p>
    <p>三类接口：命令接口、程序接口（系统调用）、图形接口。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">系统调用 vs 库函数？用户态 vs 核心态？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>系统调用</b>是用户程序取得 OS 服务的<b>唯一途径</b>。库函数可能封装了系统调用，也可能没有。</p>
    <p><b>特权指令</b>（启动 I/O、置 PSW、开关中断）只能在<b>核心态</b>执行；用户程序通过<b>访管指令/trap</b>陷入核心态。</p>
  </div>
</div>

<h3 class="chap">Ch2 · 进程管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">进程 vs 程序？PCB 是什么？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>程序</b>是静态的指令集合，<b>进程</b>是程序的一次执行过程。</p>
    <p><b>PCB（进程控制块）</b>是进程存在的<b>唯一标志</b>，创建进程就是创建 PCB。</p>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">进程三态 / 五态？哪两条转换不可能？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p>三态：<b>就绪、运行、阻塞</b>。</p>
    <p>不可能转换：<b>阻塞 → 运行</b>、<b>就绪 → 阻塞</b>。</p>
    <ul>
      <li>就绪：除 CPU 外资源齐，等调度。</li>
      <li>运行：占用 CPU。</li>
      <li>阻塞：等某事件，给 CPU 也不能跑。</li>
    </ul>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">进程 vs 线程？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>进程</b>是资源分配的独立单位；<b>线程</b>是 CPU 调度的基本单位，共享进程资源，切换开销小。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">临界资源、临界区、同步四准则</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>临界资源</b>：一次只允许一个进程使用的资源。</p>
    <p><b>临界区</b>：访问临界资源的那段代码。</p>
    <p>同步四准则：<b>空闲让进、忙则等待、有限等待、让权等待</b>。</p>
  </div>
</div>

<h3 class="chap">Ch3 · 处理机调度与死锁</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">死锁四必要条件？破坏任一即可预防</span><span class="arrow">▶</span></div>
  <div class="a">
    <ol>
      <li><b>互斥</b>：资源一次只能给一个进程。</li>
      <li><b>请求与保持</b>：拿着资源还要新的。</li>
      <li><b>不可剥夺</b>：已占资源不能被抢。</li>
      <li><b>循环等待</b>：进程形成环。</li>
    </ol>
    <p>注意：<b>四条件是必要但不充分</b>：都成立未必死锁，死锁一定都成立。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">三级调度分别调度什么？</span><span class="arrow">▶</span></div>
  <div class="a">
    <ul>
      <li><b>高级调度（作业调度）</b>：从外存后备队列选作业进内存，频率最低。</li>
      <li><b>中级调度（内存调度）</b>：挂起/对换，调节内存负载。</li>
      <li><b>低级调度（进程调度）</b>：从就绪队列选进程上 CPU，频率最高。</li>
    </ul>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">死锁处理四策略</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>预防</b>（破坏四条件）、<b>避免</b>（银行家算法）、<b>检测与解除</b>、<b>鸵鸟策略</b>（不管）。</p>
  </div>
</div>
```

- [ ] **Step 2: 验证 Ch1–Ch3 小题卡片渲染**

刷新浏览器。
Expected: 能看到「一、小题速记」标题、Ch1/Ch2/Ch3 分节、卡片带红/橙/灰标签，点击标题可展开/收起答案。

---

## Task 4: 填充小题速记区（Ch4–Ch6）

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Consumes: Task 1 CSS，Task 3 的小题区结构。
- Produces: 小题速记区 Ch4–Ch6 的折叠卡片内容。

- [ ] **Step 1: 在 Ch3 后插入 Ch4–Ch6 小题卡片**

```html
<h3 class="chap">Ch4 · 存储器管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">分页 vs 分段的核心区别？</span><span class="arrow">▶</span></div>
  <div class="a">
    <table style="width:100%;border-collapse:collapse;font-size:13px;margin:8px 0">
      <tr style="background:#eef2f8"><th></th><th>分页</th><th>分段</th></tr>
      <tr><td>单位</td><td>物理单位、定长</td><td>逻辑单位、变长</td></tr>
      <tr><td>维度</td><td>一维</td><td>二维（段号，段内偏移）</td></tr>
      <tr><td>用户可见</td><td>透明</td><td>可见</td></tr>
      <tr><td>碎片</td><td>内碎片</td><td>外碎片</td></tr>
      <tr><td>共享保护</td><td>不方便</td><td>方便</td></tr>
    </table>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">分页地址变换公式？快表 EAT？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><code>页号 = 逻辑地址 ÷ 页大小</code>；<code>偏移 = 逻辑地址 % 页大小</code>。</p>
    <p><code>物理地址 = 物理块号 × 页大小 + 偏移</code>。</p>
    <p>若页大小是 2 的幂，可直接按位截取：高位页号、低位偏移。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">静态重定位 vs 动态重定位</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>静态</b>：装入时改地址，程序装入后不能移动。</p>
    <p><b>动态</b>：运行时由<b>重定位寄存器</b>转换，可移动、可换出。<b>虚存必须用动态重定位</b>。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">内碎片 vs 外碎片？哪些分配方式有？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>内碎片</b>：分配单位内部零头 → 分页、固定分区有。</p>
    <p><b>外碎片</b>：分散小块凑不出大块 → 连续分配、分段有，可用<b>紧凑</b>消除。</p>
  </div>
</div>

<h3 class="chap">Ch5 · 虚拟内存 / 设备管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">缺页中断是什么中断？处理完做什么？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p>缺页中断属于<b>内部中断（异常）</b>。</p>
    <p>处理完缺页后，<b>重新执行原指令</b>（不是下一条）；一条指令可能触发多次缺页。</p>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">Belady 异常出现在哪种算法？为什么？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>只有 FIFO</b> 会出现 Belady 异常：分配给进程的物理块数增加，缺页次数反而增加。</p>
    <p>LRU 和 OPT 是堆栈类算法，不会出现 Belady 异常。</p>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">I/O 四级控制方式，CPU 干预度递减？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>程序直接控制（轮询）</b> → <b>中断驱动</b> → <b>DMA</b> → <b>通道</b>。</p>
    <p>单位：中断以<b>字</b>为单位，DMA 以<b>块</b>为单位，通道以<b>一组块/通道程序</b>为单位。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">SPOOLing 的作用？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>假脱机技术</b>：用磁盘输入井/输出井，把<b>独占设备虚拟成共享设备</b>。典型例子：打印机排队。</p>
  </div>
</div>

<h3 class="chap">Ch6 · 文件管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">三种文件物理结构对比？</span><span class="arrow">▶</span></div>
  <div class="a">
    <ul>
      <li><b>连续分配</b>：随机访问快，有外碎片，难增长。</li>
      <li><b>隐式链接</b>：易增长，只能顺序访问，断一处全丢。</li>
      <li><b>索引分配</b>：随机访问一步到，无外碎片；小文件浪费索引块。</li>
    </ul>
    <p><b>FAT 是显式链接，不是索引。</b></p>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">inode 里含文件名吗？硬链接 vs 软链接？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>inode 不含文件名</b>，文件名只在目录项里；一个 inode 可被多个目录项指向（硬链接）。</p>
    <ul>
      <li><b>硬链接</b>：共享 inode，count=0 才真正删除，不能跨文件系统。</li>
      <li><b>软链接</b>：存路径，可跨文件系统；原文件删了则悬空失效。</li>
    </ul>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">位示图 0/1 含义？块号 ↔ 字号位号？</span><span class="arrow">▶</span></div>
  <div class="a">
    <p>本课老师口径：<b>0 = 空闲，1 = 已分配</b>（有的教材相反，以老师为准）。</p>
    <p><code>块号 n = i × 8 + j</code>；回收时 <code>i = n ÷ 8</code>，<code>j = n mod 8</code>。</p>
  </div>
</div>
```

- [ ] **Step 2: 验证 Ch4–Ch6 小题卡片渲染**

刷新浏览器。
Expected: 小题区完整显示 Ch1–Ch6，所有卡片可折叠。

---

## Task 5: 填充问答题速记区（Ch1–Ch3）

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Consumes: Task 1 CSS，Task 3/4 的卡片结构。
- Produces: 问答题速记区 Ch1–Ch3 的折叠卡片内容。

- [ ] **Step 1: 在小题区后插入问答区 Ch1–Ch3**

```html
<h2 class="zone" id="qa">二、问答题速记 · 简答 / 论述</h2>

<h3 class="chap">Ch1 · 操作系统引论</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述操作系统的四大特征及其关系</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ol>
      <li><b>并发</b>：两个或多个事件在同一时间间隔内发生，是 OS 的核心特征。</li>
      <li><b>共享</b>：系统中的资源可供多个并发执行的进程共同使用；分互斥共享和同时访问。</li>
      <li><b>虚拟</b>：通过某种技术把一个物理实体变为若干逻辑上的对应物。</li>
      <li><b>异步</b>：进程的执行是走走停停、不可预知的，但 OS 能保证运行结果正确。</li>
    </ol>
    <p><b>关系</b>：并发和共享互为存在条件；虚拟以并发和共享为前提；异步是并发执行的必然结果。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">简述 OS 的五大功能</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b>处理机管理、存储器管理、设备管理、文件管理、提供用户接口。</p>
    <p>可一句话补：处理机管理负责进程调度；存储器管理负责内存分配与回收；设备管理负责 I/O 控制；文件管理负责文件的存取/共享/保护；用户接口让计算机方便使用。</p>
  </div>
</div>

<h3 class="chap">Ch2 · 进程管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述进程的基本状态及转换，说明哪两种转换不可能</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ol>
      <li><b>就绪态</b>：已获除 CPU 外所需资源，等待调度。</li>
      <li><b>运行态</b>：正占用 CPU 执行。</li>
      <li><b>阻塞态</b>：因等待某事件而暂停，即使给 CPU 也不能执行。</li>
    </ol>
    <p>转换：</p>
    <ul>
      <li>就绪 → 运行：进程被调度程序选中。</li>
      <li>运行 → 就绪：时间片到或被更高优先级进程抢占。</li>
      <li>运行 → 阻塞：进程请求某事件（如 I/O）。</li>
      <li>阻塞 → 就绪：等待的事件发生。</li>
    </ul>
    <p><b>不可能转换</b>：阻塞 → 运行、就绪 → 阻塞。</p>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述进程与线程的区别</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ul>
      <li>进程是资源分配的独立单位，线程是 CPU 调度的基本单位。</li>
      <li>线程共享所属进程的资源（地址空间、打开文件等），本身几乎不拥有资源。</li>
      <li>线程切换开销小，因为不需要切换地址空间；进程切换开销大。</li>
      <li>同一进程内的线程间通信更简单，可直接读写共享变量。</li>
    </ul>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">简述临界区同步应遵循的准则</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b>空闲让进、忙则等待、有限等待、让权等待。</p>
    <p>解释：临界区空闲时，应允许一个请求进入；已有进程进入时，其他进程必须等待；请求进入的进程应在有限时间内进入；等待时应释放 CPU，避免忙等。</p>
  </div>
</div>

<h3 class="chap">Ch3 · 处理机调度与死锁</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述死锁产生的四个必要条件</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ol>
      <li><b>互斥条件</b>：资源一次只能被一个进程占用。</li>
      <li><b>请求与保持条件</b>：进程已占资源，又提出新资源请求。</li>
      <li><b>不可剥夺条件</b>：已分配的资源在未使用完前不能被强行夺走。</li>
      <li><b>循环等待条件</b>：存在进程—资源的循环链。</li>
    </ol>
    <p><b>注意</b>：四条件是死锁的必要条件，同时满足未必一定死锁，但死锁一定同时满足四条件。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">简述死锁预防、避免、检测的区别</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ul>
      <li><b>预防</b>：事先破坏死锁四条件中的一个或多个，简单但限制强。</li>
      <li><b>避免</b>：不破坏条件，每次分配前用银行家算法判断是否会进入不安全状态。</li>
      <li><b>检测</b>：允许死锁发生，定期用资源分配图化简法检测，再解除。</li>
    </ul>
  </div>
</div>
```

- [ ] **Step 2: 验证 Ch1–Ch3 问答卡片渲染**

刷新浏览器。
Expected: 能看到「二、问答题速记」标题、Ch1/Ch2/Ch3 分节、卡片可折叠。

---

## Task 6: 填充问答题速记区（Ch4–Ch6）

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Consumes: Task 1 CSS，Task 5 的问答区结构。
- Produces: 问答题速记区 Ch4–Ch6 的折叠卡片内容。

- [ ] **Step 1: 在 Ch3 问答后插入 Ch4–Ch6 问答卡片**

```html
<h3 class="chap">Ch4 · 存储器管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述分页与分段的主要区别</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <table style="width:100%;border-collapse:collapse;font-size:13px;margin:8px 0">
      <tr style="background:#eef2f8"><th>比较项</th><th>分页</th><th>分段</th></tr>
      <tr><td>单位</td><td>物理单位，页大小固定</td><td>逻辑单位，段长可变</td></tr>
      <tr><td>地址空间</td><td>一维</td><td>二维（段号，段内偏移）</td></tr>
      <tr><td>用户可见性</td><td>对用户透明</td><td>用户可见</td></tr>
      <tr><td>碎片</td><td>内碎片</td><td>外碎片</td></tr>
      <tr><td>共享与保护</td><td>不方便</td><td>方便</td></tr>
    </table>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述请求分页页表的主要字段</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b>页号、物理块号、<b>状态位 P</b>、<b>访问字段 A</b>、<b>修改位 M（脏位）</b>、外存地址。</p>
    <p>说明：P=0 表示该页不在内存，A 供置换算法参考，M=1 表示该页被修改过、换出时需写回磁盘。</p>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">简述虚拟存储器的理论基础</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b>虚拟存储器基于<b>局部性原理</b>。</p>
    <ul>
      <li><b>时间局部性</b>：刚被访问的指令或数据很可能再次被访问。</li>
      <li><b>空间局部性</b>：一旦访问某个单元，其邻近单元也很可能被访问。</li>
    </ul>
    <p>因此不必把整个程序装入内存，只需装入当前需要的部分，其余放在外存，按需调入。</p>
  </div>
</div>

<h3 class="chap">Ch5 · 虚拟内存 / 设备管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述页面抖动（Thrashing）及其产生原因、预防措施</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ul>
      <li><b>定义</b>：页面在内存与外存之间频繁换入换出，导致 CPU 利用率急剧下降。</li>
      <li><b>原因</b>：系统中并发进程太多，每个进程分到的物理块太少，不能容纳其工作集。</li>
      <li><b>预防</b>：用<b>工作集</b>模型控制并发度，保证每个进程有足够物理块；或采用缺页率反馈调节。</li>
    </ul>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">简述 SPOOLing 系统的组成与作用</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ul>
      <li><b>组成</b>：输入井/输出井（磁盘）、输入缓冲/输出缓冲、输入进程/输出进程、井管理程序。</li>
      <li><b>作用</b>：将一台独占设备改造为可供多个用户共享的虚拟设备，提高设备利用率。</li>
      <li><b>典型应用</b>：打印机虚拟共享，用户提交打印任务后无需等待打印完成。</li>
    </ul>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">简述 DMA 与中断驱动 I/O 的主要区别</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ul>
      <li>中断驱动以<b>字</b>为单位传送，每传送一个字都要中断 CPU。</li>
      <li>DMA 以<b>块</b>为单位传送，整块传完才中断 CPU 一次。</li>
      <li>DMA 进一步减少 CPU 干预，适合高速设备批量数据传输。</li>
    </ul>
  </div>
</div>

<h3 class="chap">Ch6 · 文件管理</h3>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述文件的三种物理分配方式及其优缺点</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ul>
      <li><b>连续分配</b>：文件占连续盘块。优点是可随机访问、速度快；缺点是有外碎片、文件难增长。</li>
      <li><b>链接分配</b>：文件块用指针链起。优点是无外碎片、易增长；缺点是只能顺序访问、可靠性差（断链全丢）。</li>
      <li><b>索引分配</b>：每个文件有一个索引块集中存放块号。优点是可随机访问、无外碎片；缺点是小文件浪费索引块。</li>
    </ul>
  </div>
</div>

<div class="card hi">
  <div class="q"><div class="freq"></div><span class="badge">高</span><span class="title">简述文件系统中目录、FCB、inode 的作用</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b></p>
    <ul>
      <li><b>目录</b>：实现按名存取，是 FCB 的有序集合。</li>
      <li><b>FCB（文件控制块）</b>：存放文件属性（名、大小、物理位置、权限等），是文件存在的标志。</li>
      <li><b>inode</b>：UNIX 系统中存放文件属性和地址索引的数据结构；<b>inode 不含文件名</b>，文件名只在目录项中。</li>
    </ul>
  </div>
</div>

<div class="card mid">
  <div class="q"><div class="freq"></div><span class="badge">中</span><span class="title">简述成组链接法的基本思想</span><span class="arrow">▶</span></div>
  <div class="a">
    <p><b>考试写法：</b>成组链接法是 UNIX 采用的空闲盘块管理方法，结合了空闲表和空闲链的优点。</p>
    <ul>
      <li>把空闲盘块分成若干组，每组用一个栈保存块号。</li>
      <li>分配时从栈顶弹出；栈顶只剩最后一块时，先读出它指向的下一组信息，再分配该块。</li>
      <li>回收时压栈；栈满时把当前整组写入被回收块，该块成为新组首块。</li>
    </ul>
    <p><b>注意</b>：栈中第一个数是「块数」不是块号；具体数字以老师范例为准。</p>
  </div>
</div>
```

- [ ] **Step 2: 验证 Ch4–Ch6 问答卡片渲染**

刷新浏览器。
Expected: 问答区完整显示 Ch1–Ch6，所有卡片可折叠。

---

## Task 7: 实现易错雷区与页脚

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Consumes: Task 1 CSS 中 `.mines`、`.mine`、`.note`、footer 样式。
- Produces: 底部易错雷区直接展开，页脚提供来源说明。

- [ ] **Step 1: 在问答区后插入易错雷区和页脚**

```html
<h2 class="zone" id="traps">三、易错雷区 · 考前再扫一遍</h2>
<p class="lede">这些点在选择/判断里最容易挖坑，看到就慢一拍。</p>

<div class="mines">
  <div class="mine">
    <div class="q">死锁四条件是必要但不充分</div>
    <div class="a">四条件都成立<b>未必</b>死锁；死锁一定四条件都成立。</div>
  </div>
  <div class="mine">
    <div class="q">FIFO vs LRU / Belady</div>
    <div class="a">FIFO 按<b>进入先后</b>淘汰、可能 Belady；LRU 按<b>最久未用</b>淘汰、绝无 Belady。</div>
  </div>
  <div class="mine">
    <div class="q">进程状态两条不可能转换</div>
    <div class="a"><b>阻塞→运行</b>、<b>就绪→阻塞</b>不存在。</div>
  </div>
  <div class="mine">
    <div class="q">分页 vs 分段</div>
    <div class="a">分页=定长/一维/透明/只内碎片；分段=变长/<b>二维</b>/可见/只外碎片、利于共享。</div>
  </div>
  <div class="mine">
    <div class="q">请求分页页表字段</div>
    <div class="a">状态位 P、访问字段 A、<b>修改位 M</b>、外存地址——填空常漏 M。</div>
  </div>
  <div class="mine">
    <div class="q">inode 不含文件名</div>
    <div class="a">文件名只在<b>目录项</b>；inode 只存属性+地址。</div>
  </div>
  <div class="mine">
    <div class="q">中断 / DMA / 通道 的单位</div>
    <div class="a">中断=<b>字</b>，DMA=<b>块</b>，通道=<b>一组块</b>。</div>
  </div>
  <div class="mine">
    <div class="q">位示图 0/1 含义</div>
    <div class="a">本课老师口径 <b>0=空闲、1=已分配</b>。</div>
  </div>
  <div class="mine">
    <div class="q">硬链接 vs 软链接</div>
    <div class="a">硬链接 count=0 才删、不跨系统；软链接存路径、<b>原文件删则失效</b>。</div>
  </div>
  <div class="mine">
    <div class="q">两个 P 不能颠倒</div>
    <div class="a">先 P(资源) 后 P(mutex)；颠倒会<b>死锁</b>。</div>
  </div>
  <div class="mine">
    <div class="q">SSTF 会饥饿 / SCAN 折返</div>
    <div class="a">SSTF 两端易饿死；SCAN 到端才折返、C-SCAN 到端跳回不反向服务。</div>
  </div>
  <div class="mine">
    <div class="q">系统调用 / 特权指令</div>
    <div class="a">系统调用是取得 OS 服务<b>唯一途径</b>；特权指令<b>只能核心态</b>执行。</div>
  </div>
</div>

<div class="note">
  <b>使用建议：</b>先全部收起，逐张卡片自己想答案，再点开核对；考前最后一晚点「只看高频」扫一遍红色标签卡片，最后把「易错雷区」通读一次。
</div>

<footer>
  《操作系统》期末小题 + 问答题速记 · 覆盖 Ch1–Ch6 · 学校自命题 · 与 <a href="./0013-exam-cheatsheet-map.html">0013 速查地图</a> 互补 · 配套 <a href="../exams/final-test.html">仿真期末卷</a>
</footer>
```

- [ ] **Step 2: 验证雷区和页脚渲染**

刷新浏览器。
Expected: 页面底部显示「易错雷区」12 条（全部展开）、使用建议、页脚链接。

---

## Task 8: 实现 JavaScript 交互

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`

**Interfaces:**
- Consumes: DOM 元素 `#filterBtn`、`#expandBtn`、`#collapseBtn`、`.card`、`.q`。
- Produces: 折叠/展开、只看高频、全部展开/收起功能可用。

- [ ] **Step 1: 在 `<script>` 标签内写入 JS**

```javascript
(function(){
  var cards = document.querySelectorAll('.card');
  var filterBtn = document.getElementById('filterBtn');
  var expandBtn = document.getElementById('expandBtn');
  var collapseBtn = document.getElementById('collapseBtn');

  // 点击卡片标题切换展开/收起
  cards.forEach(function(card){
    var q = card.querySelector('.q');
    if (!q) return;
    q.addEventListener('click', function(){
      card.classList.toggle('open');
    });
  });

  // 只看高频
  if (filterBtn) {
    filterBtn.addEventListener('click', function(){
      var on = document.body.classList.toggle('only-hi');
      filterBtn.classList.toggle('on', on);
      filterBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
      filterBtn.textContent = on ? '显示全部' : '只看高频';
    });
  }

  // 全部展开
  if (expandBtn) {
    expandBtn.addEventListener('click', function(){
      cards.forEach(function(card){ card.classList.add('open'); });
    });
  }

  // 全部收起
  if (collapseBtn) {
    collapseBtn.addEventListener('click', function(){
      cards.forEach(function(card){ card.classList.remove('open'); });
    });
  }
})();
```

- [ ] **Step 2: 验证交互功能**

刷新浏览器，执行以下检查：

1. 点击任意卡片标题 → 答案展开，箭头旋转。
2. 再次点击同一标题 → 答案收起。
3. 点击「全部展开」 → 所有卡片展开。
4. 点击「全部收起」 → 所有卡片收起。
5. 点击「只看高频」 → 中频/低频卡片隐藏，按钮变红/显示「显示全部」。
6. 再次点击 → 恢复全部显示。
7. 打开浏览器开发者工具 Console → 无 JS 报错。

Expected: 以上 7 项全部通过。

---

## Task 9: 更新课程总门户导航

**Files:**
- Modify: `operating_systems/lessons/index.html`

**Interfaces:**
- Consumes: 现有 `index.html` 的冲刺区/新增课程链接结构。
- Produces: 在 `index.html` 顶部新增课程提示或 Ch1 卡片中新增一条指向 0088 的链接。

- [ ] **Step 1: 在 `index.html` header 的 sub 段落中新增 0088 链接**

找到 `<p class="sub">` 开头、包含多个新增课程链接的段落（约第 90 行）。

在段落末尾（`</p>` 之前）插入：

```html
 + <a href="./0088-exam-cram-cards.html">0088 小题+问答题速记</a>
```

- [ ] **Step 2: 在 Ch1 卡片中新增 0088 条目（可选但推荐）**

找到 `operating_systems/lessons/index.html` 中 Ch1 卡片的 `<ul>` 列表末尾（约第 139 行附近，在 `</ul>` 之前）。

插入：

```html
      <li><a href="./0088-exam-cram-cards.html"><span class="num">0088</span><span class="ttl">小题+问答题速记</span></a><span class="badge b-cram">冲刺</span><span class="desc">考前 30 分钟：折叠卡片自测小题和问答要点。</span></li>
```

- [ ] **Step 3: 验证导航链接**

刷新 `operating_systems/lessons/index.html`。
Expected: 顶部 sub 段落出现「0088 小题+问答题速记」链接；Ch1 卡片列表出现 0088 条目；点击链接可打开 0088 页面。

---

## Task 10: 打印优化与最终验证

**Files:**
- Modify: `operating_systems/lessons/0088-exam-cram-cards.html`（CSS 已在 Task 1 写好，本 Task 只验证）

**Interfaces:**
- Consumes: `@media print` 样式。
- Produces: 打印预览时按钮隐藏、所有卡片展开、布局适配 A4。

- [ ] **Step 1: 验证打印样式**

在浏览器中打开 0088 页面，按 `Ctrl+P`（或右键 → 打印）。
Expected:
- 顶部 topbar、按钮全部隐藏。
- 所有卡片答案展开。
- 背景为白色。
- 没有大面积截断（卡片 `break-inside:avoid`）。

- [ ] **Step 2: 最终检查清单**

- [ ] 文件路径正确：`operating_systems/lessons/0088-exam-cram-cards.html`
- [ ] 页面标题正确：「操作系统期末 · 小题 + 问答题速记」
- [ ] 小题区覆盖 Ch1–Ch6
- [ ] 问答区覆盖 Ch1–Ch6
- [ ] 易错雷区 12 条全部展开
- [ ] 折叠/展开、只看高频、全部展开/收起交互正常
- [ ] 打印预览按钮隐藏且卡片展开
- [ ] `index.html` 已更新导航
- [ ] Console 无报错

---

## Self-Review

### Spec Coverage

| 设计文档要求 | 对应 Task |
|---|---|
| 单文件内联 HTML | Task 1 |
| Hero 区 + 分值条 | Task 2 |
| 小题速记 Ch1–Ch6 | Task 3 + Task 4 |
| 问答题速记 Ch1–Ch6 | Task 5 + Task 6 |
| 易错雷区 | Task 7 |
| 折叠卡片交互 | Task 8 |
| 只看高频 / 全部展开 / 收起 | Task 8 |
| 打印优化 | Task 1 CSS + Task 10 验证 |
| 更新 index.html 导航 | Task 9 |
| 老师口径优先 / 零基础友好 | 贯穿内容 Task 3–7 |

### Placeholder Scan

- 无 TBD、TODO、implement later。
- 每个 Task 都给出具体 HTML/JS 代码片段。
- 每个 Task 都有明确验证命令/预期结果。

### Type Consistency

- CSS 类名一致：`.card`、`.q`、`.a`、`.hi/.mid/.low`、`.freq`。
- JS 选择器与 HTML ID 一致：`filterBtn`、`expandBtn`、`collapseBtn`。
- 打印样式使用与常规样式相同的类名。

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-07-14-os-exam-cram-cards.md`.

Two execution options:

1. **Subagent-Driven (recommended)** - Dispatch a fresh subagent per task, review between tasks, fast iteration.
2. **Inline Execution** - Execute tasks in this session using `executing-plans`, batch execution with checkpoints.

Which approach?
