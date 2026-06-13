#!/usr/bin/env python3
"""生成 6 套章节测试 + 1 套仿真期末卷。"""
import json
import re
from pathlib import Path

BANK = Path("/Users/wangzihao/Code/pass_exam/operating_systems/exams")
TPL  = (BANK / "_template.html").read_text(encoding="utf-8")

def render(template, title, qs, total, back_href):
    qs_json = json.dumps(qs, ensure_ascii=False, separators=(",", ":"))
    out = template
    out = out.replace("{{TITLE}}", title)
    out = out.replace("{{QUESTIONS_JSON}}", qs_json)
    out = out.replace("{{TOTAL}}", str(total))
    out = out.replace("{{BACK_HREF}}", back_href)
    return out

def write_chapter(filename, title, qs, total):
    html = render(TPL, title, qs, total, "../lessons/0001-overview-and-question-map.html")
    (BANK / filename).write_text(html, encoding="utf-8")
    print(f"  wrote {filename} ({len(qs)} 题, {total} 分, {(BANK/filename).stat().st_size//1024}KB)")

# ============================================================
# 第 1 章 操作系统引论  (25 题, 100 分)
# 包含：课本基础 60% + 老师课件作业题-1/2 10% + 算法速查表 10% + 综合 20%
# ============================================================
ch1 = [
    # 选择 12 题 × 5 = 60 分
    {"type":"choice","points":5,"question":"操作系统是下列哪一类软件？",
     "options":["系统软件","应用软件","工具软件","语言处理程序"],
     "answer":0,"explanation":"OS 属于系统软件，是最核心的系统软件。","pitfall":"不要和杀毒、Office 等应用软件混。"},
    {"type":"choice","points":5,"question":"操作系统的四大基本特征（口诀「并共异虚」）是？",
     "options":["并发、共享、虚拟、异步","并发、分时、实时、网络","批处理、分时、实时、网络","单道、多道、分时、实时"],
     "answer":0,"explanation":"四大基本特征：并发、共享、虚拟、异步。","pitfall":"分时/实时/批处理/网络是 OS 类型，不是特征。"},
    {"type":"choice","points":5,"question":"区分程序和进程最关键的 OS 特征是？",
     "options":["并发性","开放性","可移植性","安全性"],
     "answer":0,"explanation":"并发环境中程序的一次执行活动形成进程。","pitfall":"「动态性」是程序 vs 进程的本质区别；并发是 OS 特征。"},
    {"type":"choice","points":5,"question":"以下哪种资源属于 CPU 管理的范畴？",
     "options":["进程调度","内存分配","磁盘读写","打印机使用"],
     "answer":0,"explanation":"处理机管理核心是进程调度。","pitfall":"内存归「存储器管理」，打印机/磁盘归「设备管理」。"},
    {"type":"choice","points":5,"question":"【老师课件·作业题-1 改编】设计分时操作系统时，首先要考虑的是？",
     "options":["灵活性和可适应性","交互性和响应时间","周转时间和系统吞吐量","实时性和可靠性"],
     "answer":1,"explanation":"分时 OS 强调交互性，响应时间在秒级。","pitfall":"批处理要吞吐量，实时要可靠性，分时必答「交互性和响应时间」。"},
    {"type":"choice","points":5,"question":"【老师课件·作业题-1 改编】设计批处理系统时，首先要考虑的是？",
     "options":["灵活性和可适应性","交互性和响应时间","周转时间和系统吞吐量","实时性和可靠性"],
     "answer":2,"explanation":"批处理要尽可能提高系统吞吐量和缩短周转时间。","pitfall":"批处理没有交互。"},
    {"type":"choice","points":5,"question":"【老师课件·作业题-1 改编】设计实时操作系统时，首先要考虑的是？",
     "options":["灵活性和可适应性","交互性和响应时间","周转时间和系统吞吐量","实时性和可靠性"],
     "answer":3,"explanation":"实时 OS 强调在规定时间内完成响应，可靠性极高。","pitfall":"实时 ≠ 分时；分时对响应时间容忍度高（秒级），实时是毫秒级。"},
    {"type":"choice","points":5,"question":"【老师课件·作业题-2 改编】多个用户在终端设备上交互输入、排错和控制程序运行，是哪一种 OS？",
     "options":["批处理 OS","分时 OS","实时 OS","网络 OS"],
     "answer":1,"explanation":"分时 OS 提供多用户交互能力。","pitfall":"批处理无交互；实时面向控制。"},
    {"type":"choice","points":5,"question":"【老师课件·作业题-2 改编】把一个程序划分成若干个同时执行的程序模块的设计方法是？",
     "options":["多重程序设计","多道程序设计","并发程序设计","分布式系统"],
     "answer":2,"explanation":"并发程序设计 = 在程序内部划分并发模块。","pitfall":"多道程序设计是 OS 同时跑多个独立程序；并发程序设计是单个程序内部并发。"},
    {"type":"choice","points":5,"question":"【老师课件·作业题-2 改编】由多个计算机组成、互相通信、共享资源、无主次之分的系统，对应的 OS 是？",
     "options":["网络 OS","分布式 OS","分时 OS","批处理 OS"],
     "answer":1,"explanation":"分布式 OS 强调「无主次、协同工作」；网络 OS 强调「通信和资源共享」但仍有主从。","pitfall":"网络 vs 分布式是常考易混点。"},
    {"type":"choice","points":5,"question":"系统调用是用户程序请求 OS 服务的接口，调用时会发生？",
     "options":["用户态 → 核心态 切换","核心态 → 用户态 切换","用户态内部切换","核心态内部切换"],
     "answer":0,"explanation":"系统调用触发从用户态到核心态的切换。","pitfall":"返回时是核心态 → 用户态。"},
    {"type":"choice","points":5,"question":"微内核 OS 结构的主要缺点是？",
     "options":["灵活性低","性能开销大","可移植性差","不支持多线程"],
     "answer":1,"explanation":"微内核 OS 把服务移到用户态，进程间通信多，性能开销大。","pitfall":"微内核优点：灵活/可靠/可移植；缺点：性能。"},
    # 判断 6 题 × 4 = 24 分
    {"type":"tf","points":4,"question":"操作系统的并发性指的是同一时刻多个事件同时发生。",
     "answer":False,"explanation":"并发是「同一时间间隔内」发生；「同一时刻」是并行。","pitfall":"单核 OS 只有并发，没有并行。"},
    {"type":"tf","points":4,"question":"操作系统的异步性指进程以不可预知的速度推进，但运行结果可重复。",
     "answer":True,"explanation":"异步性定义：以不可预知速度推进，但只要环境相同，结果可重复。","pitfall":"异步 ≠ 不可重复。"},
    {"type":"tf","points":4,"question":"操作系统的虚拟性是把一个物理实体映射为多个逻辑实体。",
     "answer":True,"explanation":"时分复用（CPU）和空分复用（内存）都属于虚拟。","pitfall":"虚拟 ≠ 虚假。"},
    {"type":"tf","points":4,"question":"分时系统的响应时间通常要求在 1-2 秒内。",
     "answer":True,"explanation":"课件原文：「通常为 1-2 秒」。","pitfall":"实时系统是毫秒级。"},
    {"type":"tf","points":4,"question":"实时系统比批处理系统更注重系统资源的利用率。",
     "answer":False,"explanation":"实时系统首先保证「及时响应」和「可靠性」，不追求资源利用率。","pitfall":"批处理才追求资源利用率。"},
    {"type":"tf","points":4,"question":"多道批处理系统可以提高 CPU 和 I/O 设备的利用率。",
     "answer":True,"explanation":"多道程序使 CPU 在 I/O 期间可以跑别的作业，资源利用率提升。","pitfall":"单道批处理时 CPU 大量时间在等 I/O。"},
    # 填空 4 题 × 4 = 16 分
    {"type":"fill","points":4,"question":"操作系统的五大基本功能包括处理机管理、存储器管理、设备管理、文件管理和______。",
     "answer":["用户接口","用户/作业接口"],"explanation":"用户接口包括命令接口、程序接口、图形接口。","pitfall":"不要写成「用户管理」。"},
    {"type":"fill","points":4,"question":"操作系统的四大基本特征口诀是「并、共、______、虚」。",
     "answer":["异","异步"],"explanation":"并发、共享、异步、虚拟。","pitfall":"不要把「异步」写成「异常」。"},
    {"type":"fill","points":4,"question":"【老师课件·作业题-2 改编】把多个程序同时放入主存储器在宏观上并行运行的设计方法称为______程序设计。",
     "answer":["多道","多道程序设计","多重"],"explanation":"多道程序设计是 OS 层面的，多重程序设计是同义。","pitfall":"不要和「并发程序设计」混。"},
    {"type":"fill","points":4,"question":"操作系统提供给程序员的 4 大抽象是：进程、______、文件、read/write/open/close。",
     "answer":["虚拟地址空间","虚存","虚拟存储器"],"explanation":"4 大抽象：进程（CPU）、虚拟地址空间（内存）、文件（磁盘）、文件操作接口（IO）。","pitfall":"不是「进程通信」或「信号量」。"},
    # 简答 3 题 × 0 分（参考题）
    {"type":"short","points":0,"question":"简述操作系统为什么要提供「虚拟性」。",
     "answer":"通过时分复用（CPU、IO 设备）或空分复用（内存、磁盘），把有限的物理资源抽象为多个逻辑实体，使用户感觉独占或拥有更大的资源，例如虚拟处理机、虚拟存储器。",
     "explanation":"答题三要素：复用技术（时分/空分）+ 逻辑实体 + 例子。","pitfall":"不要只说「让资源看起来更多」。"},
    {"type":"short","points":0,"question":"多道批处理系统比单道批处理系统有哪些优点？",
     "answer":"① 提高了 CPU 利用率（CPU 在 IO 期间可跑别的作业）；② 提高了内存和 IO 设备利用率；③ 增加了系统吞吐量。",
     "explanation":"答题扣「资源利用率 + 吞吐量」两个关键词。","pitfall":"别忘了吞吐量这一点。"},
    {"type":"short","points":0,"question":"简述分时系统与实时系统的区别。",
     "answer":"分时：多用户通过终端交互使用计算机，响应时间在 1-2 秒级别；实时：要求对外部事件在规定毫秒/微秒内响应，可靠性更高、交互性弱，应用于卫星/导弹控制。",
     "explanation":"对比「响应时间 + 用途 + 交互性」。","pitfall":"实时 ≠ 立刻，是「在截止时间前」。"},
]
write_chapter("ch01-test.html", "第 1 章 操作系统引论 · 章节测试", ch1, 100)
print(f"  ch1 total: {sum(q['points'] for q in ch1)} 分 (含参考题)")
