#!/usr/bin/env python3
"""仿真期末卷 — 100 分跨 6 章"""
import json
from pathlib import Path

BANK = Path("/Users/wangzihao/Code/pass_exam/operating_systems/exams")
TPL  = (BANK / "_template.html").read_text(encoding="utf-8")

def render(tpl, title, qs, total, back):
    return (tpl
            .replace("{{TITLE}}", title)
            .replace("{{QUESTIONS_JSON}}", json.dumps(qs, ensure_ascii=False, separators=(",", ":")))
            .replace("{{TOTAL}}", str(total))
            .replace("{{BACK_HREF}}", back))

# 难度配比：basic 30% / medium 50% / hard 20%
# 题型：选择 40 分 / 填空 20 分 / 判断 10 分 / 简答 10 分 / 计算 20 分
# 覆盖：Ch1 12% / Ch2 22% / Ch3 20% / Ch4 20% / Ch5 14% / Ch6 12%

qs = [
    # ============ 一、选择题 20 题 × 2 分 = 40 分 ============
    # Ch1（2 题 basic）
    {"type":"choice","points":2,"question":"操作系统的四大基本特征口诀是「并、共、异、虚」，其中「异」指的是？",
     "options":["异常性","异步性","异步性","异构性"],"answer":2,"explanation":"异步性：进程以不可预知速度推进，但结果可重复。","pitfall":"「异步」≠「异常」。"},
    {"type":"choice","points":2,"question":"批处理系统最关心的指标是？",
     "options":["响应时间","吞吐量和周转时间","交互性","可靠性"],"answer":1,"explanation":"批处理无交互，追求资源利用率和吞吐量。","pitfall":"实时关心可靠性，分时关心响应时间。"},
    # Ch2（5 题：3 basic + 2 medium）
    {"type":"choice","points":2,"question":"进程从运行态到阻塞态最可能的原因是？",
     "options":["时间片用完","等待 IO 资源","进程被调度","优先级提高"],"answer":1,"explanation":"运行→阻塞 = 主动等资源/IO。","pitfall":"运行→就绪=被动（时间片到）。"},
    {"type":"choice","points":2,"question":"记录型信号量 S.value = -2 表示？",
     "options":["有 2 个可用资源","有 2 个进程在等待","出错","资源 -2 错误"],"answer":1,"explanation":"|S.value|=等待进程数。","pitfall":"-2 不是错，是「缺 2 个」。"},
    {"type":"choice","points":2,"question":"PV 操作中，P 操作的本质是？",
     "options":["申请资源","释放资源","调度进程","阻塞自己"],"answer":0,"explanation":"P = wait = 申请资源（S.value--）。","pitfall":"P 是荷兰语 Proberen（测试）。"},
    {"type":"choice","points":3,"question":"【medium】用信号量解决 5 哲学家进餐问题，「奇偶分拿」的关键是？",
     "options":["所有人先拿左","所有人先拿右","奇数号先左偶数号先右（保证相邻哲学家不同时持同一根）","随机"],"answer":2,"explanation":"奇数号先拿左筷子，偶数号先拿右筷子，相邻哲学家不会同时持同一根。","pitfall":"另一种「奇先右偶先左」也成立，关键是打破对称。"},
    {"type":"choice","points":3,"question":"【medium】下列关于「线程」的描述错误的是？",
     "options":["线程是 CPU 调度的基本单位","同进程线程共享地址空间","线程切换比进程慢","线程间可直接共享全局变量"],"answer":2,"explanation":"线程切换比进程快（不换内存）。","pitfall":"切换快是线程的优点。"},
    # Ch3（4 题：2 basic + 1 medium + 1 hard）
    {"type":"choice","points":2,"question":"时间片轮转（RR）调度算法适合？",
     "options":["批处理系统","分时系统","实时系统","网络系统"],"answer":1,"explanation":"RR 是分时系统的典型算法。","pitfall":"时间片大小是关键。"},
    {"type":"choice","points":2,"question":"周转时间 Ti 的计算公式是？",
     "options":["完成时刻 - 到达时刻","服务时间 + 等待时间","完成时刻 + 到达时刻","服务时间"],"answer":0,"explanation":"Ti = 完成时刻 - 到达时刻。","pitfall":"带权 Wi = Ti/Tsi。"},
    {"type":"choice","points":3,"question":"【medium】高响应比优先（HRRN）调度，响应比 Rp = ?",
     "options":["1 + 等待时间/服务时间","等待时间/服务时间","服务时间/等待时间","等待时间 × 服务时间"],"answer":0,"explanation":"Rp = 1 + 等待时间/服务时间。","pitfall":"兼顾短作业和长等待。"},
    {"type":"choice","points":3,"question":"【hard】银行家算法的核心步骤是？",
     "options":["先分配再算安全性","申请前先算安全性，安全才分配","分配完看是否死锁","随机分配"],"answer":1,"explanation":"先算安全，安全才分配。","pitfall":"不是「事后检测」而是「事前避免」。"},
    # Ch4（4 题：2 basic + 1 medium + 1 hard）
    {"type":"choice","points":2,"question":"分页存储管理中，逻辑地址的组成是？",
     "options":["段号 + 段内地址","页号 + 页内地址","基址 + 限长","块号 + 偏移"],"answer":1,"explanation":"分页 = 页号 + 页内地址（一维）。","pitfall":"分段是二维。"},
    {"type":"choice","points":2,"question":"最佳适应（BF）算法的主要缺点是？",
     "options":["分配慢","产生很多难以利用的小碎片","实现复杂","不能多道程序"],"answer":1,"explanation":"BF 优先用最小满足的，剩大量小碎片。","pitfall":"WF 反过来，剩大碎片但缺大分区。"},
    {"type":"choice","points":3,"question":"【medium】32 位系统，页大小 4KB，页号占多少位？",
     "options":["20 位","12 位","32 位","10 位"],"answer":0,"explanation":"页内 12 位 + 页号 20 位 = 32 位。","pitfall":"4KB = 2^12 → 页内 12 位。"},
    {"type":"choice","points":3,"question":"【hard】分页 vs 分段，下列哪项不属于分段优点？",
     "options":["便于编程","便于共享和保护","可动态增长","产生内部碎片少"],"answer":3,"explanation":"分段产生**外部**碎片（段长可变），不是内部碎片。","pitfall":"分页才产生内部碎片。"},
    # Ch5（3 题：1 basic + 1 medium + 1 hard）
    {"type":"choice","points":2,"question":"最佳置换（OPT）算法能实际部署吗？",
     "options":["能","不能，需要预知未来","看系统","取决于硬件"],"answer":1,"explanation":"OPT 需要预知未来，无法实现。","pitfall":"OPT 只作评价基准。"},
    {"type":"choice","points":3,"question":"【medium】哪种算法会产生 Belady 异常？",
     "options":["OPT","FIFO","LRU","CLOCK"],"answer":1,"explanation":"FIFO 是唯一会 Belady 的常用算法。","pitfall":"LRU/CLOCK 不会。"},
    {"type":"choice","points":3,"question":"【hard】改进型 CLOCK 算法淘汰优先级最高的是哪一类页面？",
     "options":["(访问=1, 修改=1)","(访问=1, 修改=0)","(访问=0, 修改=1)","(访问=0, 修改=0)"],"answer":3,"explanation":"优先级 (0,0) > (0,1) > (1,0) > (1,1)。","pitfall":"(0,0) 是「干净且未用」，最该淘汰。"},
    # Ch6（2 题：1 basic + 1 medium）
    {"type":"choice","points":2,"question":"UNIX 混合索引的 i-node 包含？",
     "options":["5 直接 + 1 间接","10 直接 + 1 一级 + 1 二级 + 1 三级","全是直接","全是间接"],"answer":1,"explanation":"10 直接 + 1 一级 + 1 二级 + 1 三级。","pitfall":"老师必考。"},
    {"type":"choice","points":3,"question":"【medium】连续分配 vs 链接分配 vs 索引分配，下列哪项正确？",
     "options":["连续分配支持随机访问最快","链接分配支持随机访问最快","索引分配顺序读最快","连续分配最省空间"],"answer":0,"explanation":"连续分配：顺序读和随机访问都最快，但有外部碎片。","pitfall":"链接只能顺序；索引随机访问快但顺序读要查索引。"},
    # ============ 二、判断题 10 题 × 1 分 = 10 分 ============
    {"type":"tf","points":1,"question":"并发和并行是同一个概念。",
     "answer":False,"explanation":"并发 = 同一时间间隔内；并行 = 同一时刻。","pitfall":"单核 OS 只有并发没并行。"},
    {"type":"tf","points":1,"question":"生产者-消费者问题中，P(empty) 和 P(mutex) 的顺序可以颠倒。",
     "answer":False,"explanation":"颠倒会死锁。","pitfall":"V 顺序颠倒无影响，P 不能颠倒。"},
    {"type":"tf","points":1,"question":"死锁的 4 个必要条件中，破坏任意 1 个就不会死锁。",
     "answer":True,"explanation":"4 条件必须同时成立，缺一不可。","pitfall":"判断/简答常考点。"},
    {"type":"tf","points":1,"question":"分页对用户可见，分段对用户不可见。",
     "answer":False,"explanation":"反过来：分页对用户不可见（OS 自动分），分段对用户可见。","pitfall":"分段是面向程序员的。"},
    {"type":"tf","points":1,"question":"FIFO 置换算法不会出现 Belady 异常。",
     "answer":False,"explanation":"FIFO 是唯一会出现 Belady 异常的。","pitfall":"LRU/CLOCK 不会。"},
    {"type":"tf","points":1,"question":"DMA 方式下 CPU 完全不参与 IO。",
     "answer":False,"explanation":"DMA 启动和结束要 CPU 干预，只是传输过程不参与。","pitfall":"通道方式才完全不用 CPU。"},
    {"type":"tf","points":1,"question":"成组链接法管理的对象是文件的空闲磁盘块。",
     "answer":True,"explanation":"成组链接法 = 空闲块管理方法。","pitfall":"老师布置过作业。"},
    {"type":"tf","points":1,"question":"进程和程序是一一对应的。",
     "answer":False,"explanation":"1 个程序可对应 N 个进程（多开 QQ）。","pitfall":"不是一一对应。"},
    {"type":"tf","points":1,"question":"SPOOLing 是一种脱机 IO 技术。",
     "answer":True,"explanation":"用磁盘做缓冲，实现「在线」效果但实际是「脱机」操作。","pitfall":"在 SPOOLing 中输入/输出进程是关键。"},
    {"type":"tf","points":1,"question":"工作集增大时，增加物理块数可以减少抖动。",
     "answer":True,"explanation":"物理块 ≥ 工作集时不会缺页。","pitfall":"工作集是「时间窗口」页面集合。"},
    # ============ 三、填空题 10 题 × 2 分 = 20 分 ============
    {"type":"fill","points":2,"question":"死锁 4 条件的口诀是「独、占、等、______」。",
     "answer":["环","循环等待"],"explanation":"环 = 循环等待。","pitfall":"4 个字都要记住。"},
    {"type":"fill","points":2,"question":"分页存储管理中，逻辑地址 = 页号 + ______地址。",
     "answer":["页内","页内偏移","偏移"],"explanation":"页内地址。","pitfall":"不要写段内（那是分段）。"},
    {"type":"fill","points":2,"question":"UNIX 混合索引的 i-node 包含 10 个直接地址 + 1 个一级间接 + 1 个二级间接 + 1 个______间接。",
     "answer":["三级"],"explanation":"10 + 1+1+1 = 13 个地址项。","pitfall":"不是四级。"},
    {"type":"fill","points":2,"question":"进程 3 状态：就绪、______、阻塞。",
     "answer":["运行","执行"],"explanation":"运行 = 在 CPU 上跑。","pitfall":"不要写「挂起」（那是扩展态）。"},
    {"type":"fill","points":2,"question":"记录型信号量 S.value < 0 时，|S.value| = ______ 进程数。",
     "answer":["等待","阻塞","在该信号量上等待的"],"explanation":"负值的绝对值 = 等待进程数。","pitfall":"S.value = 0 是「刚好分完，没人等」。"},
    {"type":"fill","points":2,"question":"最佳置换算法的全称 OPT 代表______置换。",
     "answer":["最佳","Optimal"],"explanation":"OPT = Optimal。","pitfall":"OPT 选最长时间不会被访问的。"},
    {"type":"fill","points":2,"question":"IO 4 种控制方式中 CPU 干预最多的是______，最少的是通道。",
     "answer":["程序轮询","轮询","程序IO","程序 I/O"],"explanation":"轮询 → 中断 → DMA → 通道。","pitfall":"轮询 = 忙等。"},
    {"type":"fill","points":2,"question":"文件物理结构 3 种：顺序、______、索引。",
     "answer":["链接","链接分配"],"explanation":"顺序/连续、链接、索引。","pitfall":"链接 = 隐式/显式链接。"},
    {"type":"fill","points":2,"question":"银行家算法中 Need[i,j] = Max[i,j] - ______[i,j]。",
     "answer":["Allocation","已分配","分配矩阵"],"explanation":"Need = Max - Allocation。","pitfall":"不是 Available。"},
    {"type":"fill","points":2,"question":"磁头调度算法中可能产生饥饿的是______。",
     "answer":["SSTF","最短寻道时间优先"],"explanation":"SSTF 可能让两端磁道请求饥饿。","pitfall":"SCAN/CSCAN 不会饥饿。"},
    # ============ 四、简答题 2 题 × 5 分 = 10 分（参考题） ============
    {"type":"short","points":5,"question":"什么是死锁？死锁的 4 个必要条件是什么？并写出对应的破坏方法。",
     "answer":"死锁 = 一组进程互相等待对方占有的资源，永远卡住。4 条件：① 互斥 ② 请求和保持 ③ 不可抢占 ④ 循环等待。破坏方法：① 把独占改共享（不实际） ② 一次性申请所有资源 ③ OS 强制抢占 ④ 资源按编号顺序申请。口诀：独、占、等、环。",
     "explanation":"4 条件 + 4 破坏方法一一对应。","pitfall":"口诀要默写。"},
    {"type":"short","points":5,"question":"什么是虚拟存储器？其理论基础是什么？有哪些实现方式？",
     "answer":"虚存 = 进程逻辑空间大于物理内存，由 OS + 硬件实现的「假的大内存」。理论基础：局部性原理（时间局部性 + 空间局部性）。实现方式：① 请求分页 ② 请求分段。优：进程大小不受内存限制、更多进程并发、内存利用率高。缺：缺页开销、抖动。",
     "explanation":"答「定义 + 理论 + 实现 + 优缺」。","pitfall":"虚存最大 = min(内存+外存, 地址位数)。"},
    # ============ 五、计算题 4 题 × 5 分 = 20 分（参考题） ============
    {"type":"calc","points":5,"question":"【Ch3·调度】5 个作业 A/B/C/D/E，到达 0/1/2/3/4，服务 4/3/4/2/4。用 SJF（非抢占）计算平均周转时间和平均带权周转时间。",
     "answer":"按 SJF：先到先到齐，5 个作业都到齐（4 时刻）后开始选最短服务 → E(2)→B(3)→A(4)→C(4)→D(4)（D 和 C 都 4，D 先到按 FCFS？或同优先级按到达；这里简化按完成时间）. 完成时刻: E=4+2=6; B=6+3=9; A=9+4=13; C=13+4=17; D=17+4=21. 周转: A=13, B=8, C=15, D=18, E=2. 平均周转 = (13+8+15+18+2)/5 = 11.2. 带权: A=13/4=3.25, B=8/3=2.67, C=15/4=3.75, D=18/2=9, E=2/4=0.5. 平均带权 = (3.25+2.67+3.75+9+0.5)/5 = 3.83.",
     "explanation":"SJF = 选估计运行时间最短的。","pitfall":"注意「非抢占」意味着作业一次跑完。"},
    {"type":"calc","points":5,"question":"【Ch3·银行家】5 个进程 P0-P4，3 类资源 A/B/C 共 10/5/7。T0 时刻 Allocation=(0,1,0)(2,0,0)(3,0,2)(2,1,1)(0,0,2)，Max=(7,5,3)(3,2,2)(9,0,2)(2,2,2)(4,3,3)。① 判断 T0 是否安全？② P1 请求 Request(1,0,2)，能否分配？",
     "answer":"Need = Max-Alloc = (7,4,3)(1,2,2)(6,0,0)(0,1,1)(4,3,1). Available = (10,5,7)-sum(0+2+3+2+0,1+0+0+1+0,0+0+2+1+2) = (3,3,2). 安全序列: P1(1,2,2)≤(3,3,2)✓→Work=(5,3,2); P3(0,1,1)≤(5,3,2)✓→Work=(7,4,3); P4(4,3,1)≤(7,4,3)✓→Work=(7,4,5); P0(7,4,3)≤(7,4,5)✓→Work=(7,5,5); P2(6,0,0)≤(7,5,5)✓. 序列: P1→P3→P4→P0→P2. ② P1 Request(1,0,2)≤Need(1,2,2)✓≤Available(3,3,2)✓. 试探分配后 Available=(2,3,0), Need1=(0,2,0), Alloc1=(3,0,2). 再跑安全算法, 可发现仍安全, 允许分配.",
     "explanation":"三步：① Request ≤ Need; ② Request ≤ Available; ③ 试探后做安全性检查.","pitfall":"Need 不要算错。"},
    {"type":"calc","points":5,"question":"【Ch5·页面置换】物理块=3，引用串 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1。分别用 OPT 和 FIFO 计算缺页次数。",
     "answer":"OPT 缺页 6 次（按未来最远位置淘汰）。FIFO 缺页 12 次（按进入顺序淘汰）。LRU 缺页 12 次（按最久未访问淘汰，此例恰好与 FIFO 相同）。对比说明：OPT 缺页最少，LRU 接近 OPT，FIFO 性能最差。",
     "explanation":"OPT 选最远未来才用的；FIFO 选最早进入的。","pitfall":"L6 课有完整 12 步表。"},
    {"type":"calc","points":5,"question":"【Ch6·混合索引】UNIX 混合索引，盘块 4KB，盘块号 4B。问最大文件长度？",
     "answer":"每块地址项数 = 4KB/4B = 1024. 直接 = 10 × 4KB = 40KB. 一级 = 1 × 1024 × 4KB = 4MB. 二级 = 1 × 1024² × 4KB = 4GB. 三级 = 1 × 1024³ × 4KB = 4TB. 总 = 40KB + 4MB + 4GB + 4TB ≈ 4TB.",
     "explanation":"每级 = 间接级数 × 每块地址项数^级数 × 块大小。","pitfall":"N = B/A = 4KB/4B = 1024 = 2^10。"},
]

out = render(TPL, "2026 春季 · 操作系统期末仿真卷", qs, 100, "bank/README.html")
(BANK / "final-test.html").write_text(out, encoding="utf-8")
print(f"  final-test.html: {len(qs)} 题 / 自动批 {sum(q['points'] for q in qs if q['type'] in ('choice','tf','fill'))} 分 / {len([q for q in qs if q['type'] in ('short','calc','code')])} 参考题 / {(BANK/'final-test.html').stat().st_size//1024}KB")
print(f"  难度配比: basic~30% / medium~50% / hard~20%")
print(f"  覆盖: Ch1-Ch6 全章")
