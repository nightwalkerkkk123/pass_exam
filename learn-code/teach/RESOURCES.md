# xv6 内核 Resources

本课程的脊椎是 **xv6 官方教材(rev3)** 的章节划分,所有讲解都应回到这本书 + 本地真实源码。

## Knowledge

- [Book: _xv6: a simple, Unix-like teaching operating system_ (rev3) — Cox, Kaashoek, Morris](https://pdos.csail.mit.edu/6.1810/2023/xv6/book-riscv-rev3.pdf)
  **主资源**。与本地 `xv6-riscv-20230207/` 逐行对应,章节即课程脊椎(接口→组织→页表→陷阱→中断→锁→调度→文件系统→并发)。任何机制讲解都先回到对应章节。
- [MIT 6.1810 (原 6.S081) 课程主页 — 2023](https://pdos.csail.mit.edu/6.1810/2023/)
  官方课程站,含 schedule(逐周对应章节)、lecture notes、lab 说明。Use for: 确认某章配套哪个讲座主题、官方阅读顺序。
- [本地源码: `../xv6-riscv-20230207/`](../xv6-riscv-20230207/)
  **最高可信度**:真实可编译的 RISC-V xv6。`kernel/` 是内核,`user/` 是用户态程序。任何讲解都要能指到这里的具体行。

## Wisdom (Communities)
- 暂未确认用户社区偏好。后续可考虑:课程同学/助教、r/osdev(写内核向)。
  (用户当前目标是"读懂并按章节讲清楚",社区实战需求暂不迫切。)

## Gaps
- 尚未确认本地 RISC-V 工具链 / QEMU 是否安装——若要"跑起来看现象",需先确认 `make qemu` 可用。
- 中文配套资料未筛选(官方书为英文)。如需要,后续补一份高质量中文导读。
