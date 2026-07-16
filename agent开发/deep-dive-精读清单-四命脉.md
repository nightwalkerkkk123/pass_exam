# 深挖清单 · agent 的四条命脉（LLM抽象 / DB落地 / MCP / Slides）

> 目标：把 mino_server 里这四块从"名字"变成"读透并能复述"。逐块推进，每块确认再往下。
> 纪律：每条结论落到 `文件:符号`；避免绝对量词除非 grep 证实；数值真查。
> 顺序按依赖/教学法：LLM抽象（怎么说话）→ DB落地（怎么记住）→ MCP（工具怎么动态长进来）→ Slides（把前三串起来的复杂工具）。

## 第 0 块 · 热身：先激活你的后端直觉（进行中）
- [ ] 用你自己的话：如果让你设计"业务代码 ↔ N 个模型供应商"之间那一层，你会放什么、要解决哪些问题？

## 第 1 块 · LLM 抽象（infrastructure/llms）（待侦察回归）
- [ ] 核心接口 + 方法签名 + 谁实现（file:symbol）
- [ ] 支持哪些供应商、如何路由到具体模型
- [ ] 流式怎么做（streamCallLLM 或等价）
- [ ] 工具带外传参：model.WithTools 在这层怎么被消费成 API 参数
- [ ] token 计数在哪
- [ ] 模型降级 tryModelFallback：触发条件 + 回退目标（核实是否 slides 专属）
- [ ] 错误分类：ErrLLMPromptTooLong / 429 如何被识别
- [ ] eino 在这层的角色
- [ ] 连接点：主循环怎么调这层

## 第 2 块 · DB 落地（infrastructure/persistence + dmrepo）（待侦察回归）
- [ ] 存储选型实证（MySQL/Redis/字节内部存储？附证据）
- [ ] Repository 模式：接口 + 核心方法 + 实现
- [ ] 会话/消息核心实体字段（entity）
- [ ] 写路径：一轮结束后状态在哪、怎么写回（"查 DB 真落了没"）
- [ ] 读路径：下一轮怎么把历史重建成 messages
- [ ] 事务/幂等/并发控制（version/weaklock）
- [ ] 大消息（工具结果/大文本）怎么处理

## 第 3 块 · MCP（mcpservice / mcptoolservice / mcpsecurity）（待侦察回归）
- [ ] MCPSessions 从哪来、结构、生命周期
- [ ] MCP tool → eino ToolInfo 的转换点（适配器）
- [ ] mcpservice vs mcptoolservice 分工
- [ ] 调用一个 MCP 工具的执行路径
- [ ] 安全：mcpsecurity 防什么、怎么防
- [ ] **钉死连接点**：静态 54 + 动态 MCP（agent.go ~755-758）→ getCurrentToolInfos → WithTools

## 第 4 块 · Slides（slidesservice / htmlslidesservice）（待侦察回归）
- [ ] 端到端管线（大纲→内容→HTML→渲染？几次 LLM 调用）
- [ ] 它是"工具"还是"子 agent"：判定依据
- [ ] 为什么复杂到单独立服务
- [ ] 可靠性特殊待遇的真相（tryModelFallback / 429 是否 slides 专属，逐条证实/证伪）
- [ ] 产物怎么落地/返回（artifact / 对象存储）
