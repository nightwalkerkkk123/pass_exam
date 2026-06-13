#!/usr/bin/env python3
"""第 3 章 处理机调度与死锁 — 30 题（100 分）"""
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

def write(name, title, qs, total):
    out = render(TPL, title, qs, total, "../lessons/0002-scheduling-algorithms.html")
    (BANK / name).write_text(out, encoding="utf-8")
    auto = sum(q['points'] for q in qs if q['type'] in ('choice','tf','fill'))
    ref  = len([q for q in qs if q['type'] in ('short','calc','code')])
    print(f"  {name}: {len(qs)} 题 / 自动批 {auto} 分 / {ref} 参考题 / {(BANK/name).stat().st_size//1024}KB")

ch3 = [
    # ============ 选择 14 题 × 3 = 42 分 ============
    {"type":"choice","points":3,"question":"高级调度又称为什么？",
     "options":["作业调度","进程调度","中级调度","微观调度"],
     "answer":0,"explanation":"高级调度 = 作业调度，决定哪些作业从后备状态进入内存。","pitfall":"中级调度 = 对换/挂起；低级调度 = 进程调度。"},
    {"type":"choice","points":3,"question":"周转时间的计算公式是？",
     "options":["完成时刻 - 到达时刻","服务时间 + 等待时间","完成时刻 + 到达时刻","服务时间 - 等待时间"],
     "answer":0,"explanation":"周转时间 Ti = 完成时刻 - 到达时刻（含等待+运行）。","pitfall":"带权周转时间 = 周转时间 / 服务时间。"},
    {"type":"choice","points":3,"question":"带权周转时间的公式是？",
     "options":["Ti","Ti / Tsi","Tsi / Ti","(Ti-Tsi)/Tsi"],
     "answer":1,"explanation":"Wi = Ti / Tsi，含义：「实际花了多少倍的自己要求时间」。","pitfall":"Wi ≥ 1（因为 Ti ≥ Tsi）。"},
    {"type":"choice","points":3,"question":"FCFS 调度算法对哪种作业最有利？",
     "options":["短作业","CPU 繁忙型长作业","IO 繁忙型作业","紧迫作业"],
     "answer":1,"explanation":"FCFS 不区分作业长短，长作业先到先跑，对 CPU 繁忙型有利。","pitfall":"对短作业不利（要等长作业）。"},
    {"type":"choice","points":3,"question":"短作业优先（SJF）调度算法的主要缺点是？",
     "options":["实现复杂","长作业可能饥饿","不能抢占","不区分作业长度"],
     "answer":1,"explanation":"SJF 一心照顾短作业，长作业可能永远轮不到。","pitfall":"需要估计运行时间，估计不准就失效。"},
    {"type":"choice","points":3,"question":"时间片轮转（RR）调度的核心思想是？",
     "options":["按优先级调度","按时间片轮流执行就绪队列","先来先服务","最短剩余时间优先"],
     "answer":1,"explanation":"RR 把 CPU 时间分成小片，每个进程轮一个时间片。","pitfall":"时间片太小切换开销大，太大退化为 FCFS。"},
    {"type":"choice","points":3,"question":"高响应比优先（HRRN）调度的响应比公式是？",
     "options":["等待时间 / 服务时间","1 + 等待时间/服务时间","服务时间 / 等待时间","等待时间 × 服务时间"],
     "answer":1,"explanation":"Rp = 1 + 等待时间/服务时间，兼顾短作业和长等待作业。","pitfall":"等待时间越长 Rp 越大；服务时间越短 Rp 越大。"},
    {"type":"choice","points":3,"question":"多级反馈队列（MFQ）的特点是？",
     "options":["按时间片轮转","不同队列时间片不同，长作业用完时间片降级","所有队列用相同时间片","只能有一个队列"],
     "answer":1,"explanation":"MFQ 是通用调度算法：多个队列，进程降级，长作业自动降入低优先级队列。","pitfall":"MFQ 兼顾长短作业、交互性好。"},
    {"type":"choice","points":3,"question":"死锁的 4 个必要条件是？",
     "options":["并发、共享、虚拟、异步","互斥、请求和保持、不可抢占、循环等待","竞争、饥饿、活锁、阻塞","同步、互斥、通信、调度"],
     "answer":1,"explanation":"死锁 4 条件：互斥、请求和保持、不可抢占、循环等待。口诀：独、占、等、环。","pitfall":"缺一不可。"},
    {"type":"choice","points":3,"question":"资源按编号顺序申请，破坏的是死锁 4 条件中的？",
     "options":["互斥","请求和保持","不可抢占","循环等待"],
     "answer":3,"explanation":"按编号申请 → 不会出现「A 等 B, B 等 A」的环。","pitfall":"其他 3 个条件没破坏。"},
    {"type":"choice","points":3,"question":"银行家算法属于哪种死锁处理方法？",
     "options":["预防","避免","检测","解除"],
     "answer":1,"explanation":"避免 = 在分配前计算安全性，安全才分配。银行家算法是代表。","pitfall":"预防 = 破坏 4 条件；检测 = 出事后化简资源分配图。"},
    {"type":"choice","points":3,"question":"安全状态一定不会出现死锁吗？",
     "options":["是","否","不一定","看资源数"],
     "answer":0,"explanation":"安全 = 存在安全序列，按序列分配可让所有进程完成。","pitfall":"不安全不一定死锁，但可能死锁。"},
    {"type":"choice","points":3,"question":"解除死锁的常用方法是？",
     "options":["重启电脑","剥夺资源或撤销进程","增加资源","减少进程"],
     "answer":1,"explanation":"剥夺资源（从某进程抢走）、撤销进程（杀掉某进程）是常用方法。","pitfall":"重启代价大，不作为「方法」。"},
    {"type":"choice","points":3,"question":"实时调度算法 EDF 是？",
     "options":["最早截止时间优先","最低松弛度优先","最短剩余时间优先","优先级调度"],
     "answer":0,"explanation":"EDF = Earliest Deadline First，截止时间越早越优先。","pitfall":"LLF = Lowest Laxity First，松弛度 = 截止-剩余-当前。"},
    # ============ 判断 6 题 × 2 = 12 分 ============
    {"type":"tf","points":2,"question":"FCFS 算法是非抢占式的。",
     "answer":True,"explanation":"FCFS 严格按到达顺序，不抢占。","pitfall":"SJF 才有「最短剩余时间优先」的抢占版本。"},
    {"type":"tf","points":2,"question":"RR 调度算法时间片越小，系统效率越高。",
     "answer":False,"explanation":"时间片太小 → 频繁切换 → 开销增大 → 效率反而低。","pitfall":"时间片太大退化为 FCFS。"},
    {"type":"tf","points":2,"question":"带权周转时间一定 ≥ 1。",
     "answer":True,"explanation":"Wi = Ti/Tsi，Ti ≥ Tsi，所以 Wi ≥ 1。等于 1 表示「刚好不被等」。","pitfall":"数值越大说明等得越久。"},
    {"type":"tf","points":2,"question":"死锁的 4 个必要条件中，破坏任意一个就不会死锁。",
     "answer":True,"explanation":"4 条件必须同时成立，缺一不可。","pitfall":"这是判断「是否死锁」的关键。"},
    {"type":"tf","points":2,"question":"系统进入不安全状态一定会死锁。",
     "answer":False,"explanation":"不安全是「可能死锁」，不是「一定死锁」。","pitfall":"安全 → 一定不死锁；不安全 → 可能死锁。"},
    {"type":"tf","points":2,"question":"死锁的「循环等待」一定指「所有进程都参与环」。",
     "answer":False,"explanation":"部分进程形成环也是循环等待。","pitfall":"环可以只涉及部分进程。"},
    # ============ 填空 5 题 × 3 = 15 分 ============
    {"type":"fill","points":3,"question":"周转时间 Ti = ______ - 到达时刻。",
     "answer":["完成时刻","完成时间"],"explanation":"Ti = 完成时刻 - 到达时刻。","pitfall":"不要写「运行时间」（那是服务时间）。"},
    {"type":"fill","points":3,"question":"带权周转时间 Wi = Ti / ______。",
     "answer":["Tsi","服务时间","要求服务时间"],"explanation":"Tsi 是进程要求的服务时间。","pitfall":"不要和 Ti 混。"},
    {"type":"fill","points":3,"question":"死锁 4 条件的口诀是「独、占、______、环」。",
     "answer":["等","不可抢占"],"explanation":"独 = 互斥，占 = 请求和保持，等 = 不可抢占，环 = 循环等待。","pitfall":"4 个字都对。"},
    {"type":"fill","points":3,"question":"银行家算法中的 Need 矩阵定义：Need[i,j] = ______ - Allocation[i,j]。",
     "answer":["Max","最大需求","最大需求矩阵"],"explanation":"Need = Max - Allocation，表示还需要的资源数。","pitfall":"Need 也可写成 Max - Allocation。"},
    {"type":"fill","points":3,"question":"安全序列是按某种顺序为每个进程分配其所需资源，直至所有进程完成的 ______ 序列。",
     "answer":["进程","进程推进"],"explanation":"安全序列是进程推进顺序。","pitfall":"不是资源顺序。"},
    # ============ 计算大题 3 题 × 0 分 ============
    {"type":"calc","points":0,"question":"【计算】5 个作业 A/B/C/D/E，到达时间 0/1/2/3/4，服务时间 4/3/4/2/4。分别用 FCFS、SJF、RR（时间片=2）调度，计算平均周转时间和平均带权周转时间。",
     "answer":"FCFS: 完成 4/7/11/13/17, 周转 4/6/9/10/13, 平均 = 8.4; 带权 = 1.0/2.0/2.25/5.0/3.25, 平均 = 2.7. SJF (非抢占): 完成 4/3/7/13/17, 周转 4/2/5/10/13, 平均 = 6.8; 带权 = 1.0/0.67/1.25/5.0/3.25, 平均 = 2.23. RR(q=2): 调度序列 A0 B1 A2 C3 B4 D5 A6 C7 D8 E9 C10 E11 A12 ... 计算复杂, 略. 经验: RR 适合分时系统，平均周转比 FCFS 差。",
     "explanation":"FCFS 简单；SJF 周转最小但有饥饿；RR 公平。",
     "pitfall":"注意 RR 每次跑完一个时间片就放回队尾。"},
    {"type":"calc","points":0,"question":"【老师课件·银行家算法例】5 个进程 P0-P4，3 类资源 A/B/C 共 10/5/7。T0 时刻: Allocation: P0(0,1,0) P1(2,0,0) P2(3,0,2) P3(2,1,1) P4(0,0,2); Max: P0(7,5,3) P1(3,2,2) P2(9,0,2) P3(2,2,2) P4(4,3,3). Need=Max-Alloc. Available=(10,5,7)-sum(0+2+3+2+0, 1+0+0+1+0, 0+0+2+1+2)=(10-7, 5-2, 7-5)=(3,3,2). ① 判断 T0 是否安全？② P1 请求 Request(1,0,2)，能否分配？",
     "answer":"Need: P0(7,4,3) P1(1,2,2) P2(6,0,0) P3(0,1,1) P4(4,3,1). Available=(3,3,2). 安全序列: P1(1,2,2)≤(3,3,2)✓ Work=(3+2,3+0,2+0)=(5,3,2); P3(0,1,1)≤(5,3,2)✓ Work=(5+2,3+1,2+1)=(7,4,3); P4(4,3,1)≤(7,4,3)✓ Work=(7+0,4+0,3+2)=(7,4,5); P0(7,4,3)≤(7,4,5)✓ Work=(7+0,4+1,5+0)=(7,5,5); P2(6,0,0)≤(7,5,5)✓ 安全. 序列: P1→P3→P4→P0→P2. ② P1 Request(1,0,2)≤Need(1,2,2)✓ ≤Available(3,3,2)✓ 试探分配后 Available=(2,3,0), Need1=(0,2,0), Alloc1=(3,0,2). 重做安全: P1(0,2,0)≤(2,3,0)✓ Work=(5,3,2); P3(0,1,1)≤(5,3,2)✓ Work=(7,4,3); P4(4,3,1)≤(7,4,3)✓ Work=(7,4,5); P0(7,4,3)≤(7,4,5)✓ Work=(7,5,5); P2(6,0,0)≤(7,5,5)✓ 仍安全, 可分配.",
     "explanation":"三步：① Request ≤ Need; ② Request ≤ Available; ③ 试探分配后做安全性检查。",
     "pitfall":"Need 不要算错，安全性检查要把 5 个进程都跑一遍。"},
    {"type":"calc","points":0,"question":"【简答】死锁的 4 种处理策略各举 1 例。",
     "answer":"① 预防：破坏 4 条件之一（如资源按编号顺序申请破坏循环等待）；② 避免：银行家算法（动态检查安全状态）；③ 检测：资源分配图化简（定期跑算法看是否死锁）；④ 解除：剥夺资源或撤销进程（杀掉某个进程释放其资源）。",
     "explanation":"预防 vs 避免 = 静态约束 vs 动态检查。检测 vs 解除 = 发现了 vs 解决。",
     "pitfall":"检测+解除是「先放着不管，出事了再救」。"},
    # ============ 简答 2 题 × 0 分 ============
    {"type":"short","points":0,"question":"简述银行家算法的核心思想。",
     "answer":"银行家 = 把 OS 当银行家，进程 = 公司。申请资源前先算：分配后系统是否处于「安全状态」（能找到安全序列让所有进程完成）。安全才分配；不安全就拒绝。",
     "explanation":"口诀：先算安全性，安全再分配。",
     "pitfall":"银行家算法不做死锁检测，只在分配前避免。"},
    {"type":"short","points":0,"question":"简述死锁、饥饿、死循环的区别。",
     "answer":"死锁：多个进程互相等对方资源，全卡住；饥饿：一个进程长期得不到资源（如 SJF 长作业）；死循环：程序 bug，CPU 一直跑（不是 OS 调度问题）。",
     "explanation":"三者的施动者不同：死锁=互相等；饥饿=OS 没分到；死循环=自己写错。",
     "pitfall":"饥饿可能是「合法但不公平」的调度导致。"},
]

write("ch03-test.html", "第 3 章 处理机调度与死锁 · 章节测试", ch3, 100)
print(f"  ch3 自动批 {sum(q['points'] for q in ch3 if q['type'] in ('choice','tf','fill'))} 分")
