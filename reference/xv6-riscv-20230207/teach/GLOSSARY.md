# xv6-riscv 术语表

xv6 文件系统讲解专用术语。**所有 lessons/ 和讲稿必须使用本表术语**。
中文译名以汤小丹《计算机操作系统》第四版 Ch6 文件管理为准。

## 缓冲层 (bio.c)

**Buffer / 缓冲区**:
磁盘块在内存中的缓存对象。`struct buf` 字段:dev/blockno(哪个磁盘哪一块)/valid(是否读过)/refcnt(引用计数)/lock/sleep lock/data[BSIZE]。
_Avoid_: 缓存块、buffer cache 单个元素

**LRU list / 最近最少使用链表**:
所有 buffer 通过 `b->next` / `b->prev` 串成双向链表。`bcache.head.next` 是最新用过的,`bcache.head.prev` 是最久没用的。
_Avoid_: 链表(必须点明是 LRU,不是 FIFO)

**Spinlock vs sleeplock 双锁**:
- `bcache.lock`(spinlock):保护整个 LRU 链表,持锁时间短(纳秒级)
- `b->lock`(sleeplock):保护单个 buffer 内容,持锁时间可长(可包含磁盘 IO)
**为什么双锁**?保护"链表结构"和"buffer 内容"两种粒度,前者必须原子,后者可以睡。
_Avoid_: 大锁、小锁(术语模糊)

**brelse 协议**:
调用方约定:拿到 buffer 后必须调用 brelse 释放。brelse 做两件事:释放 sleeplock + 把 buffer 移到 LRU 链表头(MRU 端)。
_Avoid_: 释放缓存(不准确,它还更新 LRU 位置)

## 日志层 (log.c)

**Log / 日志**:
磁盘上一段固定区域(log start..log start+log size),用于"先写日志,再写 home"的两阶段提交。xv6 用整块日志(物理 redo log),不是 ext4 那种按 inode 粒度的逻辑日志。
_Avoid_: journaling、journal(那是 Linux 词,xv6 直接叫 log)

**Transaction / 事务**:
一次 FS 系统调用期间,所有 buffer 修改的集合。`log_write` 把 blockno 记入 `log.lh.block[]`,`commit()` 一次性把多个 block 写盘。
_Avoid_: 操作、操作集(粒度不对)

**Log absorption / 日志合并**:
同一 block 在一个事务内多次 `log_write` 时,只记一次 blockno(log.lh.block[i] 已存在则不增加 n)。**减少日志空间占用 + 减少 commit 工作量**。
_Avoid_: 去重、合并(不够精确)

**Outstanding / 进行中计数**:
`log.outstanding` 记录"正在执行的 FS 系统调用数"。`begin_op` +1,`end_op` -1。**最后一个 end_op 触发 commit**。
_Avoid_: 引用计数(那会让人想到 refcnt)

**Recover from log / 崩溃恢复**:
`initlog()` → `recover_from_log()` → 如果磁盘上的 log header 指出有未安装事务,`install_trans(1)` 把日志块拷到 home 位置。
_Avoid_: 回滚、undo(那是另一种日志策略)

## 文件系统层 (fs.c)

**Superblock / 超级块**:
`struct superblock`(fs.h:5-12),记录 magic、size、nblocks、ninodes、logstart、nlog 等关键参数。读一次缓存在内存。
_Avoid_: 超级块(直译没错,但要加"sblock"缩写)

**Dinode / 磁盘 inode**:
`struct dinode`(fs.h:32-39),磁盘上 inode 的样子:type/size/nlink/addr[NDIRECT+1]。**NDIRECT=12,最后一个 addr[] 是间接块指针**。
_Avoid_: inode(那是内存版 in-memory inode,磁盘版必须叫 dinode)

**Indirect block / 间接块**:
一个 512 字节的磁盘块,内容是 128 个 uint32 的 blockno(BSIZE=1024 时是 256 个)。`addr[NDIRECT]` 指向它,实现"超过 12 块的文件"。
_Avoid_: 一级间接块(那是 ext2 词,xv6 只有一级)

**bmap / 块映射**:
`bmap(struct inode *ip, uint bn)` 返回"文件第 bn 个逻辑块"对应的磁盘 blockno。如果还没分配,**自动分配**并填到 addr[] 或间接块。
_Avoid_: 块映射函数(口语,正式场合用 bmap)

**Dirent / 目录项**:
`struct dirent`(fs.h:42-46),`inum + name[14]`。目录就是"一个文件,内容是若干 dirent 数组"。
_Avoid_: 目录条目

## 锁与一致性术语

**Lock ordering / 锁顺序**:
xv6 FS 的固定顺序:`bcache.lock` → `b->lock`(spinlock 在前,sleeplock 在后;**绝不反过来**)。违反会死锁。
_Avoid_: 锁嵌套(模糊)

**Pinned buffer / 钉住的 buffer**:
bget 拿到后,调用 `bpin` 增加 refcnt,buffer 不会被 LRU 淘汰。`log_write` 内部调用 bpin 保护日志块。
_Avoid_: 锁定的 buffer(那是 locked,不是 pinned)

## RISC-V 硬件相关(老师爱问)

**virtio / VirtIO 磁盘驱动**:
RISC-V 上 xv6 用 virtio 模拟磁盘(virtio_disk.c + virtio.h)。`virtio_disk_rw(buf, write)` 用 MMIO 寄存器与设备交互。
_Avoid_: virtio 协议(那是协议层词,这里是设备驱动)

**PLIC / Platform-Level Interrupt Controller**:
RISC-V 平台级中断控制器,统一管理外设中断(xv6 在 plic.c)。`virtio_disk_intr` 中断 → PLIC → trap → 唤醒 IO 等待者。
_Avoid_: 中断控制器(模糊,PLIC 是 RISC-V 特定实现)

**sfence.vma / TLB 刷新指令**:
RISC-V 专用汇编指令,内核修改页表后必须执行,否则 TLB 残留旧映射。**xv6 在 vm.c 切换用户页表前调用**。
_Avoid_: TLB flush(那是 x86 词 INVLPGA / MOV CR3)

## 标识规范

- **函数名**: 用 `backtick` 包,例 `brelse()` `log_write()` `bmap()`
- **结构体字段**: 用 `backtick` 包,例 `b->refcnt` `log.lh.n`
- **文件 + 行号**: `bio.c:60` 格式
- **xv6 book 章节**: §8.1 / §8.5 格式
- **Linux 对照引用**: 用"ext4 怎么做的" / "jbd2 怎么做的"引出
