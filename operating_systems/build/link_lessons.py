#!/usr/bin/env python3
"""把 7 个题库链接加到 12 个 lesson 的页脚"""
import re
from pathlib import Path

LESSONS = Path("/Users/wangzihao/Code/pass_exam/operating_systems/lessons")

# 章节测试链接（lesson → 章节测试）
# 一个 lesson 可能涉及多个章节，所以可能挂多个
LINKS = {
    "0001-overview-and-question-map.html": [("ch01-test.html", "第 1 章测试")],
    "0002-scheduling-algorithms.html":     [("ch03-test.html", "第 3 章测试"), ("ch01-test.html", "第 1 章测试")],
    "0003-bankers-algorithm.html":         [("ch03-test.html", "第 3 章测试")],
    "0004-group-linking.html":             [("ch06-test.html", "第 6 章测试")],
    "0005-paging-fundamentals.html":       [("ch04-test.html", "第 4 章测试")],
    "0006-page-replacement.html":          [("ch05-test.html", "第 5 章测试"), ("ch04-test.html", "第 4 章测试")],
    "0007-disk-scheduling.html":           [("ch06-test.html", "第 6 章测试（磁盘调度+文件管理）")],
    "0008-io-system.html":                 [("ch06-test.html", "第 6 章测试")],
    "0009-mixed-index.html":               [("ch06-test.html", "第 6 章测试（混合索引专项）")],
    "0010-process-sync.html":              [("ch02-test.html", "第 2 章测试"), ("final-test.html", "仿真期末卷")],
    "0011-classic-sync.html":              [("ch02-test.html", "第 2 章测试（PV 编程大题）")],
    "0012-process-thread-deadlock.html":   [("ch02-test.html", "第 2 章测试"), ("ch03-test.html", "第 3 章测试（死锁 4 条件）"), ("final-test.html", "仿真期末卷")],
}

FINAL_LINE = '<br><a href="../bank/final-test.html">📝 仿真期末卷（100 分，跨 6 章）</a>'

for f, links in LINKS.items():
    p = LESSONS / f
    text = p.read_text(encoding="utf-8")
    # build bank section
    bank_links = ' · '.join(f'<a href="../bank/{href}">📝 {label}</a>' for href, label in links)
    bank_section = f'<p style="margin-top:10px; padding:8px 12px; background:#fff5f3; border:1px solid #e5e5e5; border-radius:4px;"><b>📚 做练习（题库）：</b> {bank_links}{FINAL_LINE}</p>'
    # insert before <footer class="lesson-foot">
    if 'class="lesson-foot"' in text and '做练习（题库）' not in text:
        text = text.replace('<footer class="lesson-foot">', bank_section + '\n<footer class="lesson-foot">')
        p.write_text(text, encoding="utf-8")
        print(f"  ✓ {f}: 加了 {len(links)} 个章节测试 + 期末卷")
    elif '做练习（题库）' in text:
        print(f"  - {f}: 已有链接，跳过")
    else:
        print(f"  ✗ {f}: 没找到 footer")
