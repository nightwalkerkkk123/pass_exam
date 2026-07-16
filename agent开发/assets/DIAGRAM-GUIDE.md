# 图示规范（drafter 必读）

每节 lesson 必须**图文并茂**：至少 2 幅图，其中至少 1 幅是"结构图/流程图/时间线/成本条"这类信息图（不是纯装饰）。全部用 `assets/diagram.css` + `assets/style.css` 里的组件，**纯 CSS/HTML 或内联 SVG，禁止外链任何库**（lesson 是本地 `open` 打开的，外链会挂）。

`<head>` 固定两行：
```html
<link rel="stylesheet" href="../assets/style.css">
<link rel="stylesheet" href="../assets/diagram.css">
```

## 组件速查

### 1. 管线图 `.pipeline` —— 讲 context 组装顺序、阶段流转
```html
<figure class="diagram">
<div class="pipeline">
  <div class="node stable"><span class="n-title">System Prompt</span><span class="n-sub">带 1h 缓存</span></div>
  <span class="arrow">→</span>
  <div class="node stable"><span class="n-title">工具定义</span><span class="n-sub">tools.go</span></div>
  <span class="arrow">→</span>
  <div class="node volatile"><span class="n-title">chatMessages</span><span class="n-sub">历史+请求</span></div>
</div>
<figcaption>绿=稳定(缓存命中区)，红=易变(每轮变)。对应 <code>buildConductorMessages</code>。</figcaption>
</figure>
```
`.node.stable`（绿）表示稳定/可缓存段，`.node.volatile`（红）表示易变段。

### 2. 分歧点图 `.cacheline` —— 讲 prefix cache 失效
```html
<figure class="diagram">
<div class="cacheline">
  <div class="seg hit">命中前缀<br>tools + system</div>
  <div class="seg diverge">分歧点<br>&lt;current_plan&gt; 变了</div>
  <div class="seg recompute">其后全部重算<br>历史 + 本轮</div>
</div>
<figcaption>一个字节不同，分歧点之后全部按全价重算。</figcaption>
</figure>
```

### 3. 时间线/阈值轴 `.axis` —— 讲压缩触发线、窗口占用
```html
<figure class="diagram">
<div class="axis">
  <span class="mark" style="left:80%">80% 窗口 → 触发压缩</span>
  <span class="fill-label" style="left:2%">0</span>
  <span class="fill-label" style="right:2%">满窗口</span>
</div>
<figcaption>summary.go：min(0.8×窗口, 200k) 就压缩，不等填满。</figcaption>
</figure>
```

### 4. 决策树/纵向流程 `.flow` —— 讲模型路由、工具执行分支
```html
<div class="flow">
  <div class="step decision">tokens 超过 min(0.8×窗口,200k)?</div>
  <div class="down">│</div>
  <div class="branches">
    <div class="branch"><div class="label">否</div><div class="step action">直接调用主模型</div></div>
    <div class="branch"><div class="label">是</div><div class="step action">Nano 判断话题相关性 → 压缩</div></div>
  </div>
</div>
```

### 5. 成本条 `.bars` —— 讲计价对比
```html
<div class="bars">
  <div class="row"><span class="lbl">基础输入</span><div class="track"><div class="val base" style="width:40%">1×</div></div></div>
  <div class="row"><span class="lbl">缓存写入</span><div class="track"><div class="val write" style="width:50%">1.25×</div></div></div>
  <div class="row"><span class="lbl">缓存读取</span><div class="track"><div class="val read" style="width:4%">0.1×</div></div></div>
</div>
```

### 6. 内联 SVG —— 需要自定义拓扑（如三层架构、耦合关系）时
用 `.svg-wrap` 包裹，`viewBox` 自适应，文字用 `font-family="PingFang SC, sans-serif"`，颜色用 `currentColor` 或深浅都可读的中性色（避免纯黑/纯白，深色模式会看不见）。宽度用相对，`svg` 设 `width="100%"`。保持简洁：矩形节点 + 箭头 + 标签即可，不要追求复杂渲染。

## 硬约束
- 每幅信息图必须落到**真实符号**（函数名/文件名/行号/常量值），图注里用 `<code>` 标注。
- 图不许编造数字。计价倍数用课程既定值（写入 1.25×、读取 0.1×）。触发线用 `min(0.8×窗口, 200k)` 等真实值。
- 深色模式必须可读：只用 diagram.css/style.css 里的 CSS 变量配色，不要写死颜色。
