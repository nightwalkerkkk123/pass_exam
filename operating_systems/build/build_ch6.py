#!/usr/bin/env python3
"""第 6 章 文件管理（ch6_new.ppt = IO + 文件） — 30 题（100 分）"""
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
    out = render(TPL, title, qs, total, "../lessons/0004-group-linking.html")
    (BANK / name).write_text(out, encoding="utf-8")
    auto = sum(q['points'] for q in qs if q['type'] in ('choice','tf','fill'))
    ref  = len([q for q in qs if q['type'] in ('short','calc','code')])
    print(f"  {name}: {len(qs)} 题 / 自动批 {auto} 分 / {ref} 参考题 / {(BANK/name).stat().st_size//1024}KB")

ch6 = [
    # ============ 选择 14 题 × 3 = 42 分 ============
    {"type":"choice","points":3,"question":"IO 系统的 4 种控制方式是？",
     "options":["轮询、中断、DMA、通道","串行、并行、USB、网络","读、写、打开、关闭","缓存、缓冲、置换、对换"],
     "answer":0,"explanation":"4 种控制方式：程序轮询（程序IO）、中断驱动、DMA、通道。","pitfall":"CPU 干预越来越少：轮询→中断→DMA→通道。"},
    {"type":"choice","points":3,"question":"程序轮询（程序IO）方式的主要缺点是？",
     "options":["实现复杂","CPU 大量时间在忙等（CPU 利用率低）","不能用于键盘","需要硬件支持"],
     "answer":1,"explanation":"轮询 = CPU 不断查设备状态，大部分时间在「等」（忙等）。","pitfall":"CPU 99.9% 都在等，只 0.1% 在传输。"},
    {"type":"choice","points":3,"question":"中断驱动 IO 的核心改进是？",
     "options":["CPU 不再等设备","设备不需要中断","CPU 和设备并行工作","内存加快"],
     "answer":2,"explanation":"中断驱动：CPU 启动 IO 后做别的，设备完成时发中断，CPU 处理。","pitfall":"CPU 利用率提高约 1000 倍。"},
    {"type":"choice","points":3,"question":"DMA 方式适用于？",
     "options":["单字节 IO","批量数据传送（块设备）","键盘","显示器"],
     "answer":1,"explanation":"DMA 适合一次传一个数据块（如磁盘），无需 CPU 干预每个字节。","pitfall":"DMA 在设备和内存之间直接传送数据。"},
    {"type":"choice","points":3,"question":"通道（Channel）方式是？",
     "options":["DMA 的简化","DMA 的进一步发展，可执行通道程序","一种 CPU","一种内存"],
     "answer":1,"explanation":"通道 = 专门处理 IO 的处理器，能执行通道程序。","pitfall":"通道可控制多台设备，CPU 干预最少。"},
    {"type":"choice","points":3,"question":"SPOOLing 技术的核心思想是？",
     "options":["脱机输入输出 + 预输入 + 缓输出","多道程序设计","分时处理","实时处理"],
     "answer":0,"explanation":"SPOOLing = Simultaneous Peripheral Operations On-Line，用磁盘做缓冲。","pitfall":"SPOOLing 实现了「在线」的效果但实际是「脱机」操作。"},
    {"type":"choice","points":3,"question":"SPOOLing 系统的 3 大组成部分是？",
     "options":["输入井、输出井、输入输出进程","磁盘、内存、CPU","键盘、显示器、打印机","用户、内核、硬件"],
     "answer":0,"explanation":"SPOOLing = 输入井 + 输出井 + 输入进程 + 输出进程。","pitfall":"井是磁盘上的缓冲区。"},
    {"type":"choice","points":3,"question":"文件按逻辑结构可分为？",
     "options":["有结构文件（记录式）和无结构文件（流式）","文本文件和二进制文件","系统文件和用户文件","临时文件和永久文件"],
     "answer":0,"explanation":"逻辑结构：有结构（记录式）+ 无结构（流式）。","pitfall":"Unix/DOS/Windows 都用流式文件（特例：记录数为 1）。"},
    {"type":"choice","points":3,"question":"文件按物理结构可分为？",
     "options":["顺序、链接、索引","文本、二进制","共享、私有","读、写、执行"],
     "answer":0,"explanation":"物理结构：顺序结构、链接结构、索引结构（及混合索引）。","pitfall":"对应 4 种物理分配方式。"},
    {"type":"choice","points":3,"question":"连续分配的缺点是？",
     "options":["顺序读快","支持随机访问","有外部碎片，不利于文件动态增长","实现复杂"],
     "answer":2,"explanation":"连续分配：顺序读最快，但难扩展、碎片多。","pitfall":"链接分配没外部碎片但只能顺序读；索引分配支持随机访问但占空间。"},
    {"type":"choice","points":3,"question":"链接分配的优点是？",
     "options":["顺序读最快","支持随机访问","没有外部碎片，便于文件动态增长","节省空间"],
     "answer":2,"explanation":"链接分配没有外部碎片（除了指针占的字节），但只能顺序读。","pitfall":"FAT 是「链接分配的改进」，可随机读。"},
    {"type":"choice","points":3,"question":"索引分配的优点是？",
     "options":["实现最简","支持随机访问，没有外部碎片","顺序读最快","占空间最少"],
     "answer":1,"explanation":"索引分配：随机访问方便 + 无外部碎片，但占一个索引块空间。","pitfall":"大文件索引块可能不够 → 多级索引/混合索引。"},
    {"type":"choice","points":3,"question":"UNIX 文件系统采用？",
     "options":["连续分配","链接分配","索引分配","混合索引分配"],
     "answer":3,"explanation":"UNIX i-node = 10 直接 + 1 一级间接 + 1 二级间接 + 1 三级间接。","pitfall":"这就是 L9 课讲的混合索引。"},
    {"type":"choice","points":3,"question":"FCB 是？",
     "options":["文件控制块","文件大小","文件类型","文件名"],
     "answer":0,"explanation":"FCB = File Control Block，描述和控制文件的数据结构。","pitfall":"FCB 与文件一一对应，FCB 集合 = 目录。"},
    # ============ 判断 6 题 × 2 = 12 分 ============
    {"type":"tf","points":2,"question":"DMA 方式下，CPU 完全不参与 IO 过程。",
     "answer":False,"explanation":"DMA 启动时和结束时仍需 CPU 控制，传输过程中不参与。","pitfall":"通道方式才完全不用 CPU 干预。"},
    {"type":"tf","points":2,"question":"缓冲技术可以提高 CPU 和 IO 设备的并行性。",
     "answer":True,"explanation":"缓冲 = 在内存中划一块区域，CPU 算的时候设备可继续 IO。","pitfall":"单缓冲/双缓冲/循环缓冲。"},
    {"type":"tf","points":2,"question":"流式文件可看作记录式文件的一个特例。",
     "answer":True,"explanation":"课件原文：「流式文件可看作是记录式文件的一个特例，即只含一个无标识记录的文件」。","pitfall":"Unix/Windows 都用流式文件。"},
    {"type":"tf","points":2,"question":"FAT 文件分配表是一种连续分配方式。",
     "answer":False,"explanation":"FAT 是改进的链接分配，磁盘上每个块都对应 FAT 一项。","pitfall":"FAT 显式记录所有块链接，可随机访问。"},
    {"type":"tf","points":2,"question":"成组链接法用于管理文件的空闲磁盘块。",
     "answer":True,"explanation":"成组链接法是 Unix 经典的空闲块管理方法。","pitfall":"老师布置过作业，必考。"},
    {"type":"tf","points":2,"question":"索引节点（i-node）存储在文件数据区。",
     "answer":False,"explanation":"i-node 存在专门的 i-node 区，文件数据存在数据区。","pitfall":"目录项只存文件名 + i-node 号。"},
    # ============ 填空 5 题 × 3 = 15 分 ============
    {"type":"fill","points":3,"question":"IO 4 种控制方式中，CPU 干预最多的是______，最少的是______。",
     "answer":["程序轮询","通道"],"explanation":"CPU 干预：轮询 > 中断 > DMA > 通道。","pitfall":"通道是完全独立的 IO 处理器。"},
    {"type":"fill","points":3,"question":"文件按物理结构分为 3 种：______、链接、索引。",
     "answer":["顺序","连续"],"explanation":"顺序 = 连续分配。","pitfall":"顺序/连续/索引是按物理结构分。"},
    {"type":"fill","points":3,"question":"UNIX 混合索引的 i-node 包含 10 个直接地址 + 1 个一级间接 + 1 个______间接 + 1 个三级间接。",
     "answer":["二级","二"],"explanation":"10 直接 + 1 一级 + 1 二级 + 1 三级。","pitfall":"三级是「三级间接」。"},
    {"type":"fill","points":3,"question":"成组链接法中，文件分配前的栈顶 S.free 指向第 1 个可分配的______号。",
     "answer":["空闲盘块","空块","块"],"explanation":"S.free 栈存当前组的空闲块号。","pitfall":"栈满时复制下一组。"},
    {"type":"fill","points":3,"question":"磁盘调度算法 FCFS/SSTF/SCAN/CSCAN 中，可能产生饥饿的是______。",
     "answer":["SSTF","最短寻道时间优先"],"explanation":"SSTF 可能让两端磁道请求饥饿。","pitfall":"SCAN/CSCAN 不会。"},
    # ============ 计算大题 3 题 × 0 分 ============
    {"type":"calc","points":0,"question":"【老师课件·范例 1】文件系统中一个 20MB 大文件和一个 20KB 小文件，盘块 4KB，盘块号 4B。比较连续/链接/二级索引/UNIX 混合索引 4 种方案。",
     "answer":"①最大文件：连续/链接无限制；二级索引 4GB；UNIX 混合 = 40KB + 4MB + 4GB + 4TB. ②专用块数：连续 0 块（FCB 存首块号+总块数）；链接 0 块（首块号+总块数+每块存指针）；二级索引 6 块（一级 1 + 二级 5 大文件 / 1+1=2 块小文件）；UNIX 混合 6 块（直接 0 + 间接+二级）= 5+1块. ③读 5.5KB：连续 1 次 IO；链接 1 次 IO（小文件 5.5KB 在第一块）；二级索引 3 次 IO；UNIX 1 次 IO（直接块）. 读 16MB+5.5KB：连续 1 次 IO；链接 4098 次 IO（顺序读前 4097 块）；二级索引 3 次 IO；UNIX 3 次 IO.",
     "explanation":"对比「最大文件 + 专用块数 + 读不同位置 IO 次数」。",
     "pitfall":"链接的随机访问性能最差。"},
    {"type":"calc","points":0,"question":"【混合索引大小】UNIX 混合索引，盘块 4KB，盘块号 4B。问最大文件长度？",
     "answer":"每块地址项数 = 4KB/4B = 1024. 直接 = 10 × 4KB = 40KB. 一级 = 1 × 1024 × 4KB = 4MB. 二级 = 1 × 1024^2 × 4KB = 4GB. 三级 = 1 × 1024^3 × 4KB = 4TB. 最大文件 = 40KB + 4MB + 4GB + 4TB.",
     "explanation":"每级 = 间接级数 × 每块地址项数^级数 × 块大小.",
     "pitfall":"N = B/A = 4KB/4B = 1024 = 2^10。"},
    {"type":"calc","points":0,"question":"【老师课件·FAT 例题】有 FAT 表 -1 表示文件结束，-2 表示坏块，0 表示空。给一段 FAT 让你算有几个文件、每个文件占哪些块。再给一个 2 块文件要存，FAT 怎么变。",
     "answer":"示例 FAT: 假设为 [0,5,0,2,-1,3,-1,0,0,4,0,-1]，则：文件1：1→5→3→-1（块 1,5,3）；文件2：6→-1（块 6）；文件3：9→4→-1（块 9,4）；文件4：11→-1（块 11）。共 4 个文件。存 2 块文件：找两个 0 的位置（如 2,8），FAT[2]=8, FAT[8]=-1。",
     "explanation":"FAT[块号] = 下一块号（-1=结束）。",
     "pitfall":"FAT 项数 = 盘块总数。"},
    # ============ 简答 2 题 × 0 分 ============
    {"type":"short","points":0,"question":"简述连续分配、链接分配、索引分配的优缺点。",
     "answer":"连续：顺序读最快，支持随机访问，但有外部碎片，不利于文件动态增长。链接：无外部碎片，便于扩展，但只能顺序访问，每块要存指针（FAT 例外）。索引：支持随机访问，无外部碎片，但占一个索引块空间，大文件要二级/三级索引。",
     "explanation":"对比「随机访问 + 顺序访问 + 外部碎片 + 扩展性 + 空间开销」。",
     "pitfall":"没有绝对好坏，看场景选。"},
    {"type":"short","points":0,"question":"简述成组链接法的分配和回收过程。",
     "answer":"分配：从栈顶 S.free 取一个块号分配出去；若当前组只剩 1 块（这是链接下一组的指针），则把下一组的内容复制到栈中再分配。回收：把释放的块号压入栈顶；若栈满（=100 块），则把当前栈作为一组，新块作为链接指针，存到新块中。",
     "explanation":"核心：栈 = 当前组，栈满时换组。",
     "pitfall":"这是老师必考的作业题。"},
]

write("ch06-test.html", "第 6 章 文件管理 · 章节测试", ch6, 100)
print(f"  ch6 自动批 {sum(q['points'] for q in ch6 if q['type'] in ('choice','tf','fill'))} 分")
