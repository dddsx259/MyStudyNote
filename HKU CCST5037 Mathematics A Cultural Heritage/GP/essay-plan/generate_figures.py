#!/usr/bin/env python3
"""Generate DOCX-ready figures for CCST5037 Essay Plan."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams["font.family"] = "Arial Unicode MS"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42


def rounded_box(ax, x, y, w, h, title, lines, *, face="#F7F7F5", edge="#2F2F2F", lw=1.4, title_size=11, body_size=8.5):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=lw,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h - 0.18, title, ha="center", va="top", fontsize=title_size, fontweight="bold", color="#1F1F1F")
    body = "\n".join(lines)
    ax.text(x + w / 2, y + h / 2 - 0.05, body, ha="center", va="center", fontsize=body_size, color="#333333", linespacing=1.35)


def arrow(ax, x1, y1, x2, y2, label=None, label_xy=None):
    arr = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=1.3,
        color="#444444",
    )
    ax.add_patch(arr)
    if label:
        lx, ly = label_xy if label_xy else ((x1 + x2) / 2 + 0.18, (y1 + y2) / 2)
        ax.text(lx, ly, label, fontsize=8, color="#555555", ha="left", va="center")


def figure1():
    fig, ax = plt.subplots(figsize=(10.5, 12.5), dpi=220)
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 12.5)
    ax.axis("off")
    ax.set_title(
        "Figure 1. Conceptual change in the meaning of infinity\n图 1. 无穷含义的概念变化",
        fontsize=13,
        pad=14,
        fontweight="bold",
    )

    # Main vertical flow
    boxes = [
        (
            2.1,
            10.2,
            6.3,
            1.7,
            "Before Cantor / 康托尔以前",
            [
                "Potential infinity: an endless process",
                "潜无穷: 可无限继续的过程",
                "Actual infinity: often rejected / reserved for theology",
                "实无穷: 常遭拒绝或被留给神学",
            ],
            "#EEF3F8",
        ),
        (
            2.1,
            7.35,
            6.3,
            1.7,
            "Cantor / 康托尔",
            [
                "Transfinite sets and numbers: comparable objects",
                "超限集合与超限数: 可比较的数学对象",
                "Already not 'before', not yet 'today'",
                "已不是「以前」, 也还不是「今日」",
            ],
            "#F4F0E8",
        ),
        (
            2.1,
            4.5,
            6.3,
            1.7,
            "Axiomatic set theory / 公理化集合论",
            [
                "Infinity Axiom: permits an infinite set",
                "无穷公理: 允许无穷集合",
                "Restricted set formation: blocks unrestricted totalities",
                "受限制的集合构造: 阻止不受限制的总体",
            ],
            "#EAF4EA",
        ),
        (
            2.1,
            1.7,
            6.3,
            1.55,
            "Today's standard mathematics / 今日标准数学",
            [
                "Restricted completed infinity in ordinary proofs",
                "日常证明中使用的受限制完成无穷",
                "e.g. natural numbers, infinite series",
                "例如自然数集, 无穷级数",
            ],
            "#F8F1F1",
        ),
    ]

    for x, y, w, h, title, lines, face in boxes:
        rounded_box(ax, x, y, w, h, title, lines, face=face)

    arrow(ax, 5.25, 10.2, 5.25, 9.1, "Cantor's conceptual shift\n康托尔的概念转变", (5.5, 9.65))
    arrow(ax, 5.25, 7.35, 5.25, 6.25, "axiomatization / 公理化", (5.5, 6.8))
    arrow(ax, 5.25, 4.5, 5.25, 3.3)

    # Absolute Infinite side box
    rounded_box(
        ax,
        0.35,
        6.95,
        1.55,
        2.45,
        "Absolute Infinite\n绝对无穷",
        [
            "Beyond math",
            "超出数学处理",
            "Not an ordinary set",
            "不是普通集合",
            "Not next stage",
            "不是下一阶段",
        ],
        face="#FFFFFF",
        edge="#888888",
        lw=1.2,
        title_size=9,
        body_size=7.5,
    )
    # dashed outline overlay
    dash = FancyBboxPatch(
        (0.35, 6.95),
        1.55,
        2.45,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=1.5,
        edgecolor="#777777",
        facecolor="none",
        linestyle=(0, (4, 3)),
    )
    ax.add_patch(dash)
    arrow(ax, 2.1, 8.2, 1.95, 8.2, "excluded later\n后被排除", (0.2, 9.55))

    # Boundary mark near axiomatization
    ax.add_patch(Rectangle((8.55, 4.55), 0.08, 1.6, color="#B33A3A"))
    ax.text(
        8.75,
        5.35,
        "boundary\n边界:\nAbsolute Infinite /\nunrestricted totality\n不得进入日常数学",
        fontsize=7.5,
        color="#8A2F2F",
        va="center",
        ha="left",
    )

    ax.text(
        5.25,
        0.55,
        "Core takeaway / 核心结论:\nAxiomatization did not merely rename infinity;\nit specified which infinite objects mathematics may use.\n公理化不只是给无穷换名称; 它规定了数学可以使用哪些无穷对象.",
        ha="center",
        va="center",
        fontsize=9,
        color="#222222",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#FBFBFB", edgecolor="#CCCCCC"),
    )

    path = OUT / "figure1_conceptual_change.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def figure2():
    fig, ax = plt.subplots(figsize=(12.5, 9.2), dpi=220)
    ax.set_xlim(0, 12.5)
    ax.set_ylim(0, 9.2)
    ax.axis("off")
    ax.set_title(
        "Figure 2. Mind map for the essay\n图 2. 论文思维导图",
        fontsize=13,
        pad=12,
        fontweight="bold",
    )

    rounded_box(
        ax,
        3.4,
        7.55,
        5.7,
        1.25,
        "Central theme / 中心主题",
        [
            "Axiomatization rewrote what mathematical infinity may mean",
            "公理化改写了数学无穷可以指什么",
        ],
        face="#EAF0F7",
        title_size=11,
        body_size=8.2,
    )

    branches = [
        (
            0.5,
            4.55,
            3.5,
            2.2,
            "Before / 康托尔以前",
            [
                "Potential vs actual",
                "潜无穷 vs 实无穷",
                "Historical boundary",
                "历史边界",
            ],
            "#EEF3F8",
        ),
        (
            4.5,
            4.55,
            3.5,
            2.2,
            "Cantor / 康托尔",
            [
                "Transfinite vs Absolute",
                "超限 vs 绝对无穷",
                "New mathematical objects",
                "新的数学对象",
            ],
            "#F4F0E8",
        ),
        (
            8.5,
            4.55,
            3.5,
            2.2,
            "Axiomatization / 公理化",
            [
                "Infinity Axiom",
                "无穷公理",
                "Permitted / excluded",
                "允许 / 排除",
            ],
            "#EAF4EA",
        ),
    ]
    for x, y, w, h, title, lines, face in branches:
        rounded_box(ax, x, y, w, h, title, lines, face=face, title_size=10, body_size=8)

    # connectors from center to branches
    arrow(ax, 4.4, 7.55, 2.25, 6.8)
    arrow(ax, 6.25, 7.55, 6.25, 6.8)
    arrow(ax, 8.1, 7.55, 10.25, 6.8)

    rounded_box(
        ax,
        3.6,
        2.45,
        5.3,
        1.35,
        "Today / 今日",
        [
            "Natural numbers and infinite series",
            "自然数集与无穷级数",
            "Restricted completed infinity in use",
            "使用中的受限制完成无穷",
        ],
        face="#F8F1F1",
        title_size=10,
        body_size=8,
    )
    arrow(ax, 2.25, 4.55, 5.0, 3.85)
    arrow(ax, 6.25, 4.55, 6.25, 3.85)
    arrow(ax, 10.25, 4.55, 7.5, 3.85)

    rounded_box(
        ax,
        3.1,
        0.35,
        6.3,
        1.35,
        "Course outcomes / CLO",
        [
            "CLO 2: cultural development of mathematics",
            "CLO 2: 数学作为人类文化的发展",
            "CLO 4: restricted infinity as later foundation",
            "CLO 4: 受限制无穷成为后来的基础",
        ],
        face="#F7F7F5",
        title_size=10,
        body_size=8,
    )
    arrow(ax, 6.25, 2.45, 6.25, 1.75)

    ax.text(
        6.25,
        8.95,
        "Caption: from historical debates, through Cantor's mathematical transfinite,\nto restricted infinite objects of axiomatic mathematics.",
        ha="center",
        va="center",
        fontsize=8,
        color="#555555",
    )

    path = OUT / "figure2_mind_map.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def figure_hotel():
    fig, ax = plt.subplots(figsize=(11.5, 7.2), dpi=220)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 7.2)
    ax.axis("off")
    ax.set_title(
        "Optional opening diagram: Hilbert's Hotel\n可选开场图: 希尔伯特旅馆",
        fontsize=13,
        pad=12,
        fontweight="bold",
    )

    def draw_rooms(y, labels, fills, title, rule):
        ax.text(0.4, y + 1.15, title, fontsize=11, fontweight="bold", ha="left")
        ax.text(0.4, y + 0.85, rule, fontsize=8.5, color="#555555", ha="left")
        for i, (lab, fill) in enumerate(zip(labels, fills)):
            x = 0.6 + i * 1.7
            rect = FancyBboxPatch(
                (x, y),
                1.4,
                0.7,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                linewidth=1.2,
                edgecolor="#333333",
                facecolor=fill,
            )
            ax.add_patch(rect)
            ax.text(x + 0.7, y + 0.35, lab, ha="center", va="center", fontsize=10)

    # Row 1: one new guest
    draw_rooms(
        4.7,
        ["1 free", "2 ←1", "3 ←2", "4 ←3", "5 ←4", "..."],
        ["#E8F6E8", "#F4F0E8", "#F4F0E8", "#F4F0E8", "#F4F0E8", "#F7F7F5"],
        "One new guest / 一位新客人",
        "Room n → Room n+1; room 1 becomes free.  /  原住客 n 号房 → n+1 号房; 1 号房空出.",
    )
    for i in range(4):
        x1 = 2.0 + i * 1.7
        arrow(ax, x1, 5.4, x1 + 0.55, 5.4)

    # Row 2: infinitely many
    draw_rooms(
        2.0,
        ["1 free", "2 ←1", "3 free", "4 ←2", "5 free", "..."],
        ["#E8F6E8", "#F4F0E8", "#E8F6E8", "#F4F0E8", "#E8F6E8", "#F7F7F5"],
        "Infinitely many new guests / 再来无穷多位客人",
        "Room n → Room 2n; odd-numbered rooms become free.  /  原住客 n 号房 → 2n 号房; 奇数房空出.",
    )

    ax.text(
        5.75,
        0.55,
        "Opening illustration only: a countably infinite completed collection.\n仅作直觉开场: 展示可数的完成无穷集合; 不是 ZFC 公理的证据.",
        ha="center",
        va="center",
        fontsize=9,
        color="#333333",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#FBFBFB", edgecolor="#CCCCCC"),
    )

    path = OUT / "figure_optional_hilbert_hotel.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def main():
    paths = [figure1(), figure2(), figure_hotel()]
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
