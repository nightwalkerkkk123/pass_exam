# 精读理解清单 · conductorservice/tools.go

> 目标：真正理解这 154 行如何把"工具"接进 agent。逐层推进，每层确认再往下。
> 文件：`biz/domain/dmservice/agents/conductorservice/tools.go`（3 个函数）

## Stage 1 · 大图景（已完成 ✓）
- [x] 这个文件在 agent 里扮演什么角色：**工具服务的总登记表 + 一条只读的 eval 导出路径**
- [x] 三件套心智模型：**登记（这里）→ 每轮注入（agent.go）→ 执行（toolcall.go）** 是三个不同环节，别混
- [x] "工具是带外（out-of-band）传给模型的 API 参数，不写进 messages" 这句话的含义
- [x] 文件三块：`GetAllToolServices`（登记表）/ `initializeLabEvalFeatures` / `GetToolDefaults`（eval 导出）

## Stage 2 · 登记表 GetAllToolServices（已完成 ✓）
- [x] 返回类型 `map[AgentToolType]ConductorToolService`：键=类型安全枚举，**值=服务(工厂)而非成品工具**
- [x] 精确数：54 个在用 + 1 个被注释（BrowserSubAgent，改用 browser_activate 模式切换）
- [x] 工具按用途归类；`Claw*` 前缀=AnyClaw(IM 渠道)专属变体，多渠道体现在命名上
- [ ] Go map 是无序的——那"稳定顺序利于缓存"是在哪保证的？（埋点：agent.go 的排序，Stage 5 揭晓）

## Stage 3 · 一个 service 如何变成模型能看见的工具（进行中）
- [x] `AsTools(ctx) []*ToolInfo`：一个服务 → **0..N** 个工具（sandbox=5 个；memory 按开关 0 或多个）
- [x] 为什么登记单位是"服务(工厂)"而非"工具"：现场按 AgentFeatures 生产/裁剪
- [x] 两道过滤：`hooks.GetToolServices`(粗，筛服务) + `AsTools` 内部(细，裁工具)
- [ ] `ToolInfo` 到底含哪些字段（Name/Desc/Extra/ParamsOneOf）
- [ ] 参数 schema：`ParamsOneOf.ToOpenAPIV3()` → 模型看到的"工具说明书"

## Stage 4 · GetToolDefaults 这条路（未开始）
- [ ] 为什么说它是 **Lab eval 的导出路径**，不是活请求路径
- [ ] 它顺带揭示的组装：`hooks.GetToolServices`（第一道过滤）→ `AsTools`（第二道裁剪）→ schema
- [ ] 工具默认描述 + system prompt 一起导出，是给谁用的

## Stage 5 · 连回 agent loop（未开始）
- [ ] 活请求里工具从哪注入：agent.go `getCurrentToolInfos`（按名排序）→ `model.WithTools`
- [ ] "工具定义每轮原样重发 = 固定 context 税"（接第 06 课）
