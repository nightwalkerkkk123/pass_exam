#!/usr/bin/env python3
"""第 2 章 进程的描述与控制 — 40 题（100 分）"""
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
    out = render(TPL, title, qs, total, "../lessons/0010-process-sync.html")
    (BANK / name).write_text(out, encoding="utf-8")
    print(f"  {name}: {len(qs)} 题 / 自动批 {sum(q['points'] for q in qs if q['type'] in ('choice','tf','fill'))} 分 / {len([q for q in qs if q['type'] in ('short','calc','code')])} 参考题 / {(BANK/name).stat().st_size//1024}KB")

ch2 = [
    # ============ 选择 18 题 × 3 = 54 分 ============
    {"type":"choice","points":3,"question":"进程的三个基本状态是？",
     "options":["就绪、运行、阻塞","新建、就绪、终止","活动、静止、挂起","等待、就绪、运行"],
     "answer":0,"explanation":"三基本状态：就绪 Ready、运行 Running、阻塞 Blocked。","pitfall":"「挂起」是 Linux 加的扩展态，不是基本状态。"},
    {"type":"choice","points":3,"question":"进程从运行态到阻塞态的原因最可能是？",
     "options":["时间片用完","等待 IO 资源","进程被调度","优先级提高"],
     "answer":1,"explanation":"运行 → 阻塞 = 主动等待资源/IO/信号。","pitfall":"运行 → 就绪 = 被动（时间片到）；运行 → 阻塞 = 主动（等资源）。"},
    {"type":"choice","points":3,"question":"下列哪个转换是可能的？",
     "options":["就绪 → 阻塞","阻塞 → 运行","运行 → 就绪","就绪 → 新建"],
     "answer":2,"explanation":"运行 → 就绪：时间片用完或被高优先级抢占。","pitfall":"就绪不能直接阻塞，必须先运行；阻塞也不能直接运行，必须先就绪。"},
    {"type":"choice","points":3,"question":"PCB 是？",
     "options":["进程控制块，进程存在的唯一标志","一种磁盘块","一种信号量","CPU 寄存器"],
     "answer":0,"explanation":"PCB = Process Control Block，是 OS 描述进程的唯一数据结构。","pitfall":"没有 PCB 就没有进程。"},
    {"type":"choice","points":3,"question":"临界资源是指？",
     "options":["只能被一个进程使用的资源","CPU 时间","内存空间","磁盘文件"],
     "answer":0,"explanation":"临界资源 = 一次只允许一个进程访问的资源（如打印机）。","pitfall":"内存空间（分页后）不一定是临界资源。"},
    {"type":"choice","points":3,"question":"临界区是指？",
     "options":["访问临界资源的代码段","一种信号量","一个进程","一种调度算法"],
     "answer":0,"explanation":"临界区 = 进程中访问临界资源的代码段。","pitfall":"要分清「资源」和「访问资源的代码段」。"},
    {"type":"choice","points":3,"question":"记录型信号量 S.value = -3 表示？",
     "options":["有 3 个可用资源","有 3 个进程在等待该资源","出错","空闲资源数 -3 错误"],
     "answer":1,"explanation":"S.value < 0 时，|S.value| = 等待队列中的进程数。","pitfall":"-3 不是出错，是「缺 3 个，有 3 个在等」。"},
    {"type":"choice","points":3,"question":"P 操作的本质是？",
     "options":["申请资源（减 1）","释放资源（加 1）","调度进程","阻塞自己"],
     "answer":0,"explanation":"P = wait = proberen = 申请资源，S.value--；若 < 0 则阻塞。","pitfall":"P 申请不到时会阻塞自己，但本质是「申请资源」。"},
    {"type":"choice","points":3,"question":"V 操作的本质是？",
     "options":["申请资源","释放资源（加 1）","调度进程","唤醒一个等待者"],
     "answer":1,"explanation":"V = signal = verhogen = 释放资源，S.value++；若 ≤ 0 则唤醒一个等待者。","pitfall":"V 释放后可能唤醒等待者，但本质是「释放资源」。"},
    {"type":"choice","points":3,"question":"用信号量实现互斥时，mutex 的初值是？",
     "options":["0","1","-1","资源数"],
     "answer":1,"explanation":"互斥信号量初值 = 1（临界资源个数）。","pitfall":"同步信号量初值视情况而定（empty 初值=n, full=0）。"},
    {"type":"choice","points":3,"question":"生产者-消费者问题中，empty 和 full 的初值分别是？",
     "options":["n, 0","0, n","1, 1","n, n"],
     "answer":0,"explanation":"empty（空位数）= n；full（满位数）= 0。","pitfall":"empty 表示「空缓冲区数」，full 表示「已装数据缓冲区数」。"},
    {"type":"choice","points":3,"question":"生产者-消费者问题中，P(empty) 和 P(mutex) 的执行顺序可以颠倒吗？",
     "options":["可以","不可以，否则可能死锁","看情况","无所谓"],
     "answer":1,"explanation":"必须先 P(资源信号量) 再 P(mutex)，否则两个信号量交叉等待可能死锁。","pitfall":"V 顺序颠倒没影响（V 不会阻塞），P 颠倒可能死锁。"},
    {"type":"choice","points":3,"question":"哲学家进餐问题中，5 个哲学家同时拿左边筷子后会发生？",
     "options":["正常运行","死锁","饥饿","系统重启"],
     "answer":1,"explanation":"经典死锁场景：5 个哲学家各持一根筷子，互相等待对方的筷子。","pitfall":"解法：最多 4 人同时进餐、奇偶分拿、一次性拿两根。"},
    {"type":"choice","points":3,"question":"读者-写者问题中，「读者优先」可能导致？",
     "options":["写者饥饿","读者饥饿","系统崩溃","数据不一致"],
     "answer":0,"explanation":"读者不断来，写者永远抢不到锁。","pitfall":"「写者优先」则读者饥饿。"},
    {"type":"choice","points":3,"question":"下列哪种通信方式只能在父子/兄弟进程间使用？",
     "options":["共享存储器","消息传递","管道","信号量"],
     "answer":2,"explanation":"管道（pipe）半双工、FIFO、只能在有亲缘关系的进程间使用。","pitfall":"管道是特殊的「共享文件」。"},
    {"type":"choice","points":3,"question":"线程和进程最本质的区别是？",
     "options":["是否共享地址空间","线程比进程快","进程有 PCB 线程没有","线程不能调度"],
     "answer":0,"explanation":"同进程线程共享地址空间；不同进程不共享。","pitfall":"线程切换比进程快（不换内存），但本质区别是「共享」。"},
    {"type":"choice","points":3,"question":"内核支持线程 KLT 的优点是？",
     "options":["切换快","不需 OS 介入","可在多 CPU 上真正并行","线程库灵活"],
     "answer":2,"explanation":"KLT 由 OS 直接管理，线程阻塞不影响整个进程，可在多 CPU 上并行。","pitfall":"用户级线程 ULT 切换快但不能多核并行。"},
    {"type":"choice","points":3,"question":"AND 信号量（Swait）的特点是？",
     "options":["一次申请一个资源","一次申请多个资源，全部分到才执行","自动唤醒所有等待者","用于互斥"],
     "answer":1,"explanation":"Swait(S1,S2,...) 全部分到才继续，否则全释放并阻塞。","pitfall":"AND 信号量解决「申请资源时部分成功部分失败」的问题。"},
    # ============ 判断 8 题 × 2 = 16 分 ============
    {"type":"tf","points":2,"question":"进程是程序的一次执行，因此进程和程序一一对应。",
     "answer":False,"explanation":"1 个程序可对应多个进程（多开 QQ = 1 程序 2 进程）。","pitfall":"不是一一对应。"},
    {"type":"tf","points":2,"question":"就绪状态的进程已经获得了除 CPU 以外的所有资源。",
     "answer":True,"explanation":"就绪 = 资源齐了，只等 CPU。","pitfall":"阻塞 = 等资源。"},
    {"type":"tf","points":2,"question":"信号量 S.value 必须为非负整数。",
     "answer":False,"explanation":"记录型信号量 S.value 可为负，|负值| = 等待进程数。","pitfall":"整型信号量才要求非负（但有「忙等」问题）。"},
    {"type":"tf","points":2,"question":"用 P/V 操作可以实现进程的同步和互斥。",
     "answer":True,"explanation":"P/V 是通用同步互斥原语。","pitfall":"P/V 必须成对出现，遗漏会导致死锁或永久阻塞。"},
    {"type":"tf","points":2,"question":"V 操作的顺序颠倒对程序正确性没有影响。",
     "answer":True,"explanation":"V 不会阻塞，交换两个 V 顺序不影响结果。","pitfall":"P 操作顺序颠倒可能死锁。"},
    {"type":"tf","points":2,"question":"管程是一种高级同步机制，由编译器实现。",
     "answer":True,"explanation":"管程 = 一个数据 + 一组过程 + 互斥进入，编译器负责互斥。","pitfall":"管程比信号量更结构化，但实现更复杂。"},
    {"type":"tf","points":2,"question":"进程通信中的「直接通信」需要指明对方进程的标识符。",
     "answer":True,"explanation":"直接通信：send(P, msg)、receive(Q, msg)，必须指定收发双方。","pitfall":"间接通信通过「信箱」间接收发。"},
    {"type":"tf","points":2,"question":"线程是 CPU 调度的基本单位，进程是资源分配的基本单位。",
     "answer":True,"explanation":"这是经典定义。","pitfall":"「资源」和「调度」两层粒度。"},
    # ============ 填空 6 题 × 3 = 18 分 ============
    {"type":"fill","points":3,"question":"进程的 3 基本状态是就绪、运行和______。",
     "answer":["阻塞","等待","block"],"explanation":"阻塞 = 等待 IO/资源。","pitfall":"不要写「挂起」（那是扩展态）。"},
    {"type":"fill","points":3,"question":"记录型信号量 S.value = 0 表示资源刚好分完，______个进程在等待。",
     "answer":["0","零","没有"],"explanation":"S.value=0：资源分完但无人等待。","pitfall":"=0 是「临界」状态。"},
    {"type":"fill","points":3,"question":"用 P/V 操作解决 N 个进程互斥进入临界区时，mutex 初值 = ______。",
     "answer":["1"],"explanation":"互斥信号量初值 = 临界资源个数（1 个）。","pitfall":"N 个进程要互斥进入「1 个」临界区，mutex=1。"},
    {"type":"fill","points":3,"question":"哲学家进餐问题中「奇偶分拿」解法：奇数号哲学家先拿______筷子，偶数号先拿______筷子。",
     "answer":["左","右"],"explanation":"课件原文：奇数号先拿左、偶数号先拿右。","pitfall":"另一种是「奇先右偶先左」，关键是相邻哲学家不同时持同一根筷子。"},
    {"type":"fill","points":3,"question":"【老师课件·思考题 2】司机-售票员问题：司机 P(S1) 启动车辆，售票员 V(S1) 关门。S1 初值 = ______，S2 初值 = ______。",
     "answer":["0","0"],"explanation":"两个同步信号量初值都是 0：先做的人 V，唤醒后做的人。","pitfall":"S1 表示「车已停好可以启动」，S2 表示「门已关好可以开门」。"},
    {"type":"fill","points":3,"question":"进程通信的三种方式是：共享存储器、消息传递和______。",
     "answer":["管道","pipe"],"explanation":"管道 = 半双工 + FIFO + 亲缘进程。","pitfall":"不要和「信号量」混（信号量是同步原语，不是通信方式）。"},
    # ============ 计算/PV 大题 5 题 × 0 = 0 分（参考题） ============
    {"type":"calc","points":0,"question":"【老师课件·习题】P、Q、R 三个共行进程 + BufI/BufO 两个缓冲。P 读入到 BufI，Q 把 BufI 变换后送 BufO，R 从 BufO 输出。要求最大并行性。写出 P/V 操作填空。",
     "answer":"var S1, S2, mutex1, mutex2: SEMAPHORE := 0, 0, 1, 1; P: P(mutex1); Add to BufI; V(mutex1); V(S1); Q: P(S1); P(mutex1); Remove from BufI; V(mutex1); P(mutex2); Add to BufO; V(mutex2); V(S2); R: P(S2); P(mutex2); Remove from BufO; V(mutex2); Output.",
     "explanation":"S1 同步 P→Q（BufI 有数据），S2 同步 Q→R（BufO 有数据），mutex1/2 互斥访问 BufI/BufO。","pitfall":"不要忘了 4 个信号量全部要定义。"},
    {"type":"calc","points":0,"question":"【老师课件·思考题 1】6 个进程 P1...P6，按前趋图有依赖关系：P1→P2,P3,P4；P2→P6；P3→P5；P4→P5；P5→P6。用 7 个初值 = 0 的信号量 s12,s13,s14,s26,s35,s45,s56 写出同步代码。",
     "answer":"P1: V(s12);V(s13);V(s14); P2: P(s12);...;V(s26); P3: P(s13);...;V(s35); P4: P(s14);...;V(s45); P5: P(s35);P(s45);...;V(s56); P6: P(s26);P(s56);...",
     "explanation":"边的起点 P 在完成动作后 V，终点 P 在开始动作前 P。","pitfall":"s12 表示「P1→P2」这条边的信号量，P1 完 V，P2 开始 P。"},
    {"type":"calc","points":0,"question":"【老师课件·思考题 3】桌上 1 个空盘，爸爸放苹果/桔子，儿子吃桔子，女儿吃苹果。3 个信号量 S, So, Sa 初值 1,0,0。写出 3 个进程。",
     "answer":"Father: P(S); if(桔子)V(So); else V(Sa); Son: P(So);取桔子;V(S);吃; Daughter: P(Sa);取苹果;V(S);吃;",
     "explanation":"S 表示「盘子空可以放」，So 表示「盘里是桔子」，Sa 表示「盘里是苹果」。","pitfall":"S 初值=1 表示开始时盘子空可以放。"},
    {"type":"calc","points":0,"question":"哲学家进餐问题：用「奇偶分拿」解法写出 5 个哲学家进程的伪代码（筷子用 chopstick[5] 信号量，初值=1）。",
     "answer":"Pi: do { P(chopstick[i]); if(i%2==0){P(chopstick[(i+1)%5]);} else {P(chopstick[(i+4)%5]);} 吃; V(chopstick[i]); V(chopstick[(i+1)%5]); if(i%2==0){V(chopstick[(i+4)%5]);} else {V(chopstick[(i+1)%5]);} } while(1);",
     "explanation":"奇数号先左后右、偶数号先右后左。关键：相邻哲学家不同时持同一根。","pitfall":"注意 (i+1)%5 是右边、(i+4)%5 = (i-1)%5 是左边。"},
    {"type":"calc","points":0,"question":"读者-写者问题（读者优先）：用 rmutex、wmutex、readcount 三个信号量，写出完整伪代码。",
     "answer":"readcount=0; rmutex=1; wmutex=1; Reader: P(rmutex); if(readcount==0) P(wmutex); readcount++; V(rmutex); 读; P(rmutex); readcount--; if(readcount==0) V(wmutex); V(rmutex); Writer: P(wmutex); 写; V(wmutex);",
     "explanation":"第一个读者锁 wmutex（挡写者），最后一个读者解锁 wmutex。rmutex 保护 readcount。","pitfall":"「读者优先」= 写者饥饿；「写者优先」= 读者饥饿。"},
    # ============ 简答 3 题 × 0 分 ============
    {"type":"short","points":0,"question":"同步机制应遵循的 4 条准则是什么？",
     "answer":"① 空闲让进：临界区空闲时允许请求的进程进入；② 忙则等待：临界区有进程时其他等待；③ 有限等待：等待有限时间避免饥饿；④ 让权等待：进不去应释放 CPU，不能忙等。",
     "explanation":"口诀：「空闲让进、忙则等待、有限等待、让权等待」。","pitfall":"「让权等待」是考试最爱问的。"},
    {"type":"short","points":0,"question":"简述进程和程序的区别。",
     "answer":"程序是静态的代码文件（躺在磁盘上），进程是程序的一次执行（有生命周期、状态、占用资源）。最本质区别：动态性。",
     "explanation":"本质：动态性。程序 = 菜谱，进程 = 正在做的菜。","pitfall":"1 程序可对应 N 进程。"},
    {"type":"short","points":0,"question":"简述「让权等待」的含义，为什么需要它？",
     "answer":"含义：进程进不去临界区时，应主动释放 CPU（阻塞），而不是「忙等」(while 循环检查)。必要性：避免 CPU 时间浪费在无意义的循环上，提高系统效率。",
     "explanation":"整型信号量没做到让权等待，记录型信号量做到了。","pitfall":"记录型 vs 整型信号量的核心区别就是「让权等待」。"},
]

write("ch02-test.html", "第 2 章 进程的描述与控制 · 章节测试", ch2, 100)
print(f"  ch2 自动批 {sum(q['points'] for q in ch2 if q['type'] in ('choice','tf','fill'))} 分 / 5 参考题")
