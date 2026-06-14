# xv6-riscv 源码讲解 Resources

## Knowledge

- [Book: _xv6: a simple, Unix-like teaching operating system_ (riscv 版)](https://pdos.csail.mit.edu/6.828/2022/xv6/book-riscv-rev3.pdf)
  官方配套教材,xv6 book 是**唯一权威**。每一章对应一组源码,讲解设计意图。
  **Use for**: 任何代码细节的"为什么这样写",优先于一切二手资料。
- [Course: MIT 6.1810 Operating System Engineering (2022 fall)](https://pdos.csail.mit.edu/6.828/2022/schedule.html)
  MIT 课程主页,lecture 视频 + lab + xv6 book 全套资源。
  **Use for**: 视频讲解片段(每个 lab 有对应 lecture),理解 xv6 设计哲学。
- [Code: xv6-riscv 源码(本仓库 `reference/xv6-riscv-20230207/`)](file:///E:/CODE/pass_exam/reference/xv6-riscv-20230207/kernel/)
  实际讲解目标,主战场。48 个 .c/.h/.S 文件,核心在 `proc.c` `vm.c` `trap.c` `syscall.c` `trampoline.S`。
  **Use for**: 所有源码引用、line number 引用必须基于此版本。
- [Book: 汤小丹《计算机操作系统》第四版(本仓库 `operating_systems_tangxiaodan/`)](file:///E:/CODE/pass_exam/operating_systems/operating_systems_tangxiaodan/)
  你的主教材,术语权威。Ch2 进程管理 + Ch3 处理机调度 对应本次讲解。
  **Use for**: 术语对齐(进程控制块 PCB、就绪/运行/阻塞、临界资源、调度算法)。
- [Code: Linux 0.11 fork 精讲(本仓库 `operating_systems/linux/0014-0019`)](file:///E:/CODE/pass_exam/operating_systems/linux/)
  你已有的 6 节 fork 源码精讲,类比复用。
  **Use for**: xv6 vs Linux 0.11 对照(调度器结构、PCB 字段、复制方式)。

## Wisdom (Communities)

- [r/xv6](https://reddit.com/r/xv6) — 信号偏弱,但偶尔有 OSDI 风格讨论
- [OSDev Wiki](https://wiki.osdev.org/) — 通用 OS 概念百科,适合补"页表/中断/上下文切换"基础
- **校内**: 你的同学和老师 — 课堂展示后第一时间答疑,反馈最直接

## Gaps
- 没有可信的中文 xv6 资源;如果老师要求中文术语,统一用汤小丹教材的"进程控制块 / 处理机调度 / 临界区"等
- MIT 6.1810 视频在墙内访问可能不稳,本课程**默认不依赖视频**,只引用书 + 源码
