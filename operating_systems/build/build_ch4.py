#!/usr/bin/env python3
"""第 4 章 存储器管理 — 35 题（100 分）"""
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
    out = render(TPL, title, qs, total, "../lessons/0005-paging-fundamentals.html")
    (BANK / name).write_text(out, encoding="utf-8")
    auto = sum(q['points'] for q in qs if q['type'] in ('choice','tf','fill'))
    ref  = len([q for q in qs if q['type'] in ('short','calc','code')])
    print(f"  {name}: {len(qs)} 题 / 自动批 {auto} 分 / {ref} 参考题 / {(BANK/name).stat().st_size//1024}KB")

ch4 = [
    # ============ 选择 16 题 × 3 = 48 分 ============
    {"type":"choice","points":3,"question":"存储管理的 4 大功能是？",
     "options":["内存分配、地址映射、内存保护、内存扩充","装入、链接、运行、退出","读、写、打开、关闭","分配、回收、置换、对换"],
     "answer":0,"explanation":"存储管理 4 功能：分配、映射、保护、扩充。","pitfall":"老师课件原文。"},
    {"type":"choice","points":3,"question":"【老师课件·引子】int a; printf(\"%p\", &a); 打印出的 a 的地址是？",
     "options":["真实物理地址","逻辑地址（虚幻）","段号","不确定"],
     "answer":1,"explanation":"程序中看到的地址都是逻辑地址（虚地址），不是真实物理地址。","pitfall":"这是老师课件第 1 张引入题。"},
    {"type":"choice","points":3,"question":"绝对装入方式的特点是？",
     "options":["程序中地址在编译时已经确定","装入时动态重定位","运行时动态重定位","硬件自动完成"],
     "answer":0,"explanation":"绝对装入：编译时地址就已经定好，只能装入固定位置。","pitfall":"可重定位装入 = 静态重定位；运行时重定位 = 动态重定位。"},
    {"type":"choice","points":3,"question":"连续分配方式的主要缺点是？",
     "options":["实现复杂","产生外部碎片","地址转换慢","不能多道程序"],
     "answer":1,"explanation":"连续分配（可变分区）会产生外部碎片，需要「紧凑」合并。","pitfall":"分页产生内部碎片；连续/分段产生外部碎片。"},
    {"type":"choice","points":3,"question":"首次适应（FF）算法是？",
     "options":["从空闲分区链首查找第一个满足的分区","从上次查找位置继续","找最小的满足分区","找最大的满足分区"],
     "answer":0,"explanation":"FF = First Fit，顺序查找第一个满足的。","pitfall":"NF = Next Fit（下次适应）；BF = Best Fit；WF = Worst Fit。"},
    {"type":"choice","points":3,"question":"最佳适应（BF）算法的缺点是？",
     "options":["分配慢","产生很多难以利用的小碎片","实现复杂","不能多道程序"],
     "answer":1,"explanation":"BF 优先用最小满足的，剩下大量微小碎片，无法利用。","pitfall":"WF 反过来，剩大碎片但缺大分区。"},
    {"type":"choice","points":3,"question":"分页存储管理中，页表的作用是？",
     "options":["记录文件名到目录项的映射","记录页号到页框号的映射","记录进程优先级","记录磁盘坏块位置"],
     "answer":1,"explanation":"页表 = 页号 → 物理块号（页框号）的映射。","pitfall":"页表服务于地址转换。"},
    {"type":"choice","points":3,"question":"分页系统中，逻辑地址的组成是？",
     "options":["段号 + 段内地址","页号 + 页内地址","基址 + 限长","块号 + 偏移"],
     "answer":1,"explanation":"分页：逻辑地址 = 页号 + 页内地址（页内偏移）。","pitfall":"分段是「段号 + 段内地址」。"},
    {"type":"choice","points":3,"question":"页面大小 4KB，页内地址占几位？",
     "options":["10 位","12 位","14 位","16 位"],
     "answer":1,"explanation":"4KB = 2^12，所以页内地址占 12 位。","pitfall":"1KB=2^10, 4KB=2^12, 1MB=2^20, 4MB=2^22。"},
    {"type":"choice","points":3,"question":"分段的优点不包括？",
     "options":["便于编程","便于共享和保护","可动态增长","产生内部碎片少"],
     "answer":3,"explanation":"分段便于编程/共享/保护/动态增长，但**产生外部碎片**（段长可变）。","pitfall":"分页产生内部碎片；分段产生外部碎片。"},
    {"type":"choice","points":3,"question":"虚拟存储器的理论基础是？",
     "options":["时间局部性","空间局部性","局部性原理","程序顺序执行"],
     "answer":2,"explanation":"局部性原理 = 时间局部性 + 空间局部性，是虚存的基础。","pitfall":"Denning 1968 年提出。"},
    {"type":"choice","points":3,"question":"请求分页系统中，页表项中哪个字段表示该页是否在内存？",
     "options":["访问字段 A","修改位 M","状态位 P","外存地址"],
     "answer":2,"explanation":"状态位 P（Present）= 1 在内存，= 0 不在内存（缺页）。","pitfall":"P 是 Presence/Present；A 是 Accessed；M 是 Modified。"},
    {"type":"choice","points":3,"question":"【老师课件·习题 1】32 位地址，二级页表分 9 位顶级 + 11 位二级（偏移），页面长度是？",
     "options":["2^9=512B","2^11=2048B","2^(32-9-11)=2^12=4KB","2^32=4GB"],
     "answer":2,"explanation":"32 - 9 - 11 = 12 位页内地址 → 2^12 = 4KB。","pitfall":"注意是「偏移位数」对应「页大小」。"},
    {"type":"choice","points":3,"question":"【同上】该系统共有多少个页面？",
     "options":["2^9=512","2^11=2048","2^20","2^9 × 2^11=2^20"],
     "answer":2,"explanation":"顶级页号 9 位 + 二级页号 11 位 → 总页号 20 位 → 2^20 个页面。","pitfall":"2^9 × 2^11 = 2^20 也能算出。"},
    {"type":"choice","points":3,"question":"请求分页系统中，进程获得的最少物理块数取决于？",
     "options":["进程大小","计算机硬件结构（指令格式/寻址方式）","OS 调度","页面大小"],
     "answer":1,"explanation":"最少物理块数 = 让进程能正常运行所需的最少块数，取决于硬件。","pitfall":"单地址直接寻址 → 2 块；间接寻址 → 3 块。"},
    {"type":"choice","points":3,"question":"抖动（thrashing）是指？",
     "options":["CPU 切换太快","页面频繁换入换出导致系统效率急剧下降","进程频繁切换","磁盘 I/O 错误"],
     "answer":1,"explanation":"抖动 = 缺页率极高，CPU 大部分时间在等换页。","pitfall":"工作集模型用来防止抖动。"},
    # ============ 判断 7 题 × 2 = 14 分 ============
    {"type":"tf","points":2,"question":"连续分配方式不会产生内部碎片。",
     "answer":False,"explanation":"连续分配的固定分区会有内部碎片；可变分区没内部碎片但有外部碎片。","pitfall":"分页才有内部碎片。"},
    {"type":"tf","points":2,"question":"分页系统的页表长度 = 进程的页数。",
     "answer":True,"explanation":"页表一项对应一页，进程多大（多少页）页表就多长。","pitfall":"页框号 = 物理块号；每项大小固定。"},
    {"type":"tf","points":2,"question":"分页系统中，页面大小由 OS 决定，进程不能改。",
     "answer":True,"explanation":"页面大小是 OS 全局参数，进程不参与决定。","pitfall":"页面大小通常 4KB，进程按页对齐。"},
    {"type":"tf","points":2,"question":"分页对用户可见，分段对用户不可见。",
     "answer":False,"explanation":"反过来：分页对用户**不可见**（OS 自动分），分段对用户**可见**（按逻辑分）。","pitfall":"分段是面向程序员的逻辑结构。"},
    {"type":"tf","points":2,"question":"缺页中断发生在访问的页面不在内存时。",
     "answer":True,"explanation":"缺页中断 = Page Fault，触发页面调入。","pitfall":"缺页是「需要但没在」，不是错误。"},
    {"type":"tf","points":2,"question":"虚拟存储器的容量由内存 + 外存共同决定。",
     "answer":False,"explanation":"虚存最大容量 = min(内存+外存, 计算机地址位数能表示的范围)。","pitfall":"例：32 位系统虚存最大 4GB。"},
    {"type":"tf","points":2,"question":"请求分页系统的页表项比基本分页多了几个字段。",
     "answer":True,"explanation":"请求分页页表项多了状态位 P、访问字段 A、修改位 M、外存地址。","pitfall":"基本分页只有页框号。"},
    # ============ 填空 7 题 × 3 = 21 分 ============
    {"type":"fill","points":3,"question":"存储管理的 4 大功能：内存分配、地址映射、内存保护和______。",
     "answer":["内存扩充","扩充","虚存"],"explanation":"4 大功能：分配、映射、保护、扩充。","pitfall":"不要写「对换」（那是中级调度）。"},
    {"type":"fill","points":3,"question":"【老师课件·引子】int a; &a 打印的地址属于______地址。",
     "answer":["逻辑","虚","虚拟"],"explanation":"程序里看到的都是逻辑地址。","pitfall":"不是物理地址。"},
    {"type":"fill","points":3,"question":"分页存储管理中，逻辑地址结构为：页号 + ______。",
     "answer":["页内地址","页内偏移","偏移"],"explanation":"页内地址 = 页内偏移。","pitfall":"不要写「段内地址」（那是分段）。"},
    {"type":"fill","points":3,"question":"【老师课件·练习 2】逻辑地址 16 位，页大小 4096B = 2^12B，页号占 ______ 位。",
     "answer":["4","16-12","四"],"explanation":"页号 = 16 - 12 = 4 位。","pitfall":"4096B=2^12B，12 位页内地址。"},
    {"type":"fill","points":3,"question":"分段地址结构是二维的：段号 + ______。",
     "answer":["段内地址","段内偏移","偏移"],"explanation":"分页 = 一维（页号+偏移），分段 = 二维（段号+段内地址）。","pitfall":"分段是面向逻辑的。"},
    {"type":"fill","points":3,"question":"请求分页的页表项比基本分页多了：状态位、访问字段、修改位和______。",
     "answer":["外存地址","外存块号","磁盘地址"],"explanation":"4 个字段：P、A、M、外存地址。","pitfall":"外存地址是「该页在外存的物理块号」。"},
    {"type":"fill","points":3,"question":"【老师课件·习题 1】32 位地址系统，9 位顶级页表 + 11 位二级页表 + 12 位偏移，总地址位数 = ______。",
     "answer":["32","三十二"],"explanation":"9 + 11 + 12 = 32 位。","pitfall":"检查是否等于计算机位数。"},
    # ============ 计算 3 题 × 0 分 ============
    {"type":"calc","points":0,"question":"【老师课件·练习 2 改编】逻辑地址 16 位，页大小 4096B，第 0/1/2 页存在物理块 10/12/14。逻辑地址 2F6AH 求物理地址。",
     "answer":"2F6AH = 0010 1111 0110 1010B, 高 4 位页号 = 0010B = 2, 页内地址 = 1111 0110 1010B. 第 2 页 → 物理块 14. 物理地址 = 14 × 4096 + 0xF6A = 14 × 0x1000 + 0xF6A = 0xE000 + 0xF6A = 0xEF6A.",
     "explanation":"物理地址 = 物理块号 × 页大小 + 页内地址。",
     "pitfall":"物理块号 14 转十六进制是 0xE。"},
    {"type":"calc","points":0,"question":"【老师课件·练习 3】页式管理，逻辑地址空间最大 16 页，每页 2048B，内存 8 块。问逻辑地址至少多少位？内存空间多大？",
     "answer":"16 页 = 2^4 → 页号 4 位. 每页 2048B = 2^11 → 页内 11 位. 逻辑地址 = 4+11 = 15 位. 内存空间 = 8 × 2048 = 16384B = 16KB.",
     "explanation":"逻辑地址 = 页号 + 页内. 内存 = 块数 × 块大小.",
     "pitfall":"注意「逻辑地址空间最大 16 页」= 2^N。"},
    {"type":"calc","points":0,"question":"【扩展】某系统页大小 4KB，页表项 4B。采用一级页表，最大可寻址多少虚拟空间？采用二级页表呢？",
     "answer":"一级页表：一页页表 = 4KB / 4B = 1024 项 = 2^10 项 → 最大寻址 1024 × 4KB = 4MB. 二级页表：每级 1024 项 → 1024 × 1024 = 1M 项 → 1M × 4KB = 4GB.",
     "explanation":"页大小 = 4KB = 2^12B；每页页表项数 = 4KB/4B = 2^10。",
     "pitfall":"一级寻址能力受页表页大小限制。"},
    # ============ 简答 2 题 × 0 分 ============
    {"type":"short","points":0,"question":"简述分页和分段的主要区别。",
     "answer":"分页：按固定大小划分，面向系统内存管理，页对用户不可见，一维地址（页号+偏移）；分段：按程序逻辑结构划分，段长可变，面向用户逻辑，二维地址（段号+段内地址），便于共享和保护。分页内部碎片少、外部无；分段外部碎片多。",
     "explanation":"对比「固定/可变 + 系统/用户 + 一维/二维 + 碎片类型」。",
     "pitfall":"不要说「分段比分页好」或反之。"},
    {"type":"short","points":0,"question":"简述什么是「抖动」，如何减少抖动？",
     "answer":"抖动 = 页面频繁换入换出，CPU 大部分时间在等换页，系统效率急剧下降。减少方法：① 给进程分配足够多的物理块；② 调整置换算法（如 LRU 比 FIFO 抖动少）；③ 采用工作集模型；④ 暂停部分进程减少多道度。",
     "explanation":"抖动 = thrashing，常见原因是多道度太高。",
     "pitfall":"工作集是「进程在某个时间段实际使用的页面集合」。"},
]

write("ch04-test.html", "第 4 章 存储器管理 · 章节测试", ch4, 100)
print(f"  ch4 自动批 {sum(q['points'] for q in ch4 if q['type'] in ('choice','tf','fill'))} 分")
