"""Publication figures for the scoping review. Counts match the manuscript."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

OUT = Path(__file__).resolve().parent
FONT_FILES = {
    ("normal", "normal"): r"C:\Windows\Fonts\times.ttf",
    ("bold", "normal"): r"C:\Windows\Fonts\timesbd.ttf",
    ("normal", "italic"): r"C:\Windows\Fonts\timesi.ttf",
    ("bold", "italic"): r"C:\Windows\Fonts\timesbi.ttf",
}


def fp(size=9, weight="normal", style="normal"):
    return font_manager.FontProperties(fname=FONT_FILES[(weight, style)], size=size)
NAVY = "#1B365D"
INK = "#1A1A1A"
SLATE = "#4A5568"
FILL_ID = "#EEF2F6"
FILL_ASSESS = "#F7F4EC"
FILL_EXCL = "#F4E8E8"
FILL_INCL = "#E7F0EA"
FILL_PREVIEW = "#E8EEF5"
FILL_CONTROL = "#F3EEE4"
FILL_BIND = "#E6EFEA"
FILL_WHITE = "#FFFFFF"
FILL_MUTED = "#F4F5F7"

plt.rcParams.update(
    {
        "font.family": "Times New Roman",
        "font.size": 9,
        "text.color": INK,
        "axes.unicode_minus": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)


def save(fig, stem):
    fig.savefig(OUT / f"{stem}.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def rounded(ax, x, y, w, h, facecolor, edgecolor=NAVY, lw=1.15, radius=0.012):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.004,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=lw,
        mutation_aspect=1,
        zorder=2,
    )
    ax.add_patch(patch)
    return patch


def text_block(ax, x, y, lines, size=8.2, weight="normal", color=INK, va="center", ha="center", style="normal"):
    ax.text(
        x,
        y,
        "\n".join(lines),
        ha=ha,
        va=va,
        color=color,
        zorder=3,
        linespacing=1.28,
        fontproperties=fp(size, weight, style),
    )


def arrow(ax, x1, y1, x2, y2, color=NAVY):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.15,
            color=color,
            zorder=1,
        )
    )


def label(ax, x, y, text, size=9, weight="bold", color=NAVY, ha="center", va="center", style="normal"):
    ax.text(x, y, text, ha=ha, va=va, color=color, zorder=3, fontproperties=fp(size, weight, style))


def stage_label(ax, x, y, text):
    label(ax, x, y, text.upper(), size=8, weight="bold", color=NAVY, ha="left")


def figure_1_prisma():
    fig, ax = plt.subplots(figsize=(7.28, 8.55))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    stage_label(ax, 3.2, 96.6, "Identification")
    rounded(ax, 12, 74.8, 85, 20.4, FILL_ID, radius=0.01)
    text_block(
        ax,
        54.5,
        85.0,
        [
            "Sources searched on 1 October 2026",
            "Passes 1–2: 15 queries (open web, then public ACM and IEEE pages).",
            "Hit totals and the duplicate count were not retained and are not reconstructed.",
            "Pass 3: arXiv cs.HC 19; cs.CR 111; phrase query 6 (overlaps the category queries).",
            "Semantic Scholar citing He et al. (2025): 91 works; first 50 titles scanned.",
            "Citing lists for Weng (2026) and Mozannar et al. (2025): not obtained (HTTP 429).",
            "Pass 4: OpenAlex 47; 190; 47; 27; 437; 5. Every returned title was retrieved.",
            "Scopus and Web of Science were not searched.",
        ],
        size=7.7,
    )

    arrow(ax, 54.5, 74.8, 54.5, 70.6)
    stage_label(ax, 3.2, 68.8, "Assessment")
    rounded(ax, 12, 50.4, 50.5, 19.8, FILL_ASSESS)
    text_block(
        ax,
        37.25,
        60.3,
        [
            "Records with a retained screening decision",
            "n = 59",
            "",
            "Passes 1–2: 21 assessed in full text",
            "Pass 3: 11 assessed at abstract / HTML",
            "Pass 4: 27 assessed at abstract",
        ],
        size=8.0,
    )

    arrow(ax, 62.5, 60.3, 67.4, 60.3)
    rounded(ax, 67.6, 50.4, 29.4, 19.8, FILL_EXCL, edgecolor="#7A3030")
    text_block(
        ax,
        82.3,
        60.3,
        [
            "Excluded after assessment",
            "n = 44",
            "",
            "Passes 1–2: 8",
            "Pass 3: 9",
            "Pass 4: 27",
        ],
        size=8.0,
        color="#5C2424",
    )

    arrow(ax, 37.25, 50.4, 37.25, 45.8)
    stage_label(ax, 3.2, 43.8, "Inclusion")
    rounded(ax, 12, 31.6, 50.5, 13.8, FILL_INCL, edgecolor="#1F5C3A")
    text_block(
        ax,
        37.25,
        38.5,
        [
            "Reports included in the chart",
            "n = 15",
        ],
        size=9.2,
        weight="bold",
        color="#1F5C3A",
    )

    rounded(ax, 12, 6.4, 85, 21.6, FILL_WHITE, lw=0.9)
    text_block(
        ax,
        54.5,
        17.2,
        [
            "How the 15 inclusions were reached",
            "Passes 1–2: 21 assessed → 8 excluded → 13 included",
            "Pass 3: 11 assessed → 9 excluded → 2 included (Irshad et al., 2026; Q. Zhang, 2026)",
            "Pass 4: 27 assessed → 27 excluded → 0 included",
            "The numeric record is Table 1. Exclusion reasons are Table 2.",
        ],
        size=7.6,
        color=SLATE,
    )

    save(fig, "figure-1-prisma-flow")


def mini_icon(ax, kind, cx, cy, s=2.1, color=NAVY):
    if kind == "preview":
        ax.add_patch(Rectangle((cx - s, cy - 1.3 * s), 2 * s, 2.2 * s, fill=False, lw=1.1, edgecolor=color, zorder=4))
        ax.plot([cx - 0.7 * s, cx + 0.7 * s], [cy + 0.6 * s, cy + 0.6 * s], color=color, lw=1.0, zorder=4)
        ax.plot([cx - 0.7 * s, cx + 0.4 * s], [cy, cy], color=color, lw=1.0, zorder=4)
        ax.plot([cx - 0.7 * s, cx + 0.2 * s], [cy - 0.6 * s, cy - 0.6 * s], color=color, lw=1.0, zorder=4)
    elif kind == "control":
        ax.add_patch(Circle((cx - 0.7 * s, cy), 0.38 * s, fill=False, lw=1.1, edgecolor=color, zorder=4))
        ax.add_patch(Circle((cx + 0.7 * s, cy), 0.38 * s, facecolor=color, edgecolor=color, lw=1.0, zorder=4))
        ax.plot([cx - 0.25 * s, cx + 0.25 * s], [cy, cy], color=color, lw=1.1, zorder=4)
    elif kind == "bind":
        ax.plot([cx - s, cx + s], [cy + 0.7 * s, cy + 0.7 * s], color=color, lw=1.2, zorder=4)
        ax.plot([cx - s, cx + s], [cy - 0.7 * s, cy - 0.7 * s], color=color, lw=1.2, zorder=4)
        ax.annotate(
            "",
            xy=(cx + 0.15 * s, cy - 0.7 * s),
            xytext=(cx - 0.15 * s, cy + 0.7 * s),
            arrowprops=dict(arrowstyle="<->", color=color, lw=1.1),
            zorder=4,
        )


def figure_2_framework():
    fig, ax = plt.subplots(figsize=(7.28, 7.15))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    label(ax, 50, 96.6, "What the review charts", size=12)

    frames = [
        (4.2, 71.4, 28.8, 21.4, FILL_PREVIEW, "Question 1", "Preview", "What object is shown", "before the action leaves", "the conversation?"),
        (35.6, 71.4, 28.8, 21.4, FILL_CONTROL, "Question 2", "Control", "What can the person still", "edit, refuse, limit in", "advance, or undo?"),
        (67.0, 71.4, 28.8, 21.4, FILL_BIND, "Question 3", "Binding", "Does the approved object", "remain the object that", "executes?"),
    ]
    for x, y, w, h, fill, q, title, a, b, c in frames:
        rounded(ax, x, y, w, h, fill)
        label(ax, x + w / 2, y + h - 3.0, q, size=7.4, weight="normal", color=SLATE)
        label(ax, x + w / 2, y + h - 6.4, title, size=11)
        text_block(ax, x + w / 2, y + 6.6, [a, b, c], size=7.8, color=SLATE)

    arrow(ax, 33.0, 82.1, 35.6, 82.1)
    arrow(ax, 64.4, 82.1, 67.0, 82.1)

    label(ax, 50, 66.8, "Approval-integrity chain", size=10.4)

    chain = [
        (3.6, 48.8, 21.6, 15.6, "Approved object", "Plan, draft, diff,", "command, card fields,", "or stored predicate"),
        (27.4, 48.8, 21.6, 15.6, "Approval decision", "Proceed, allow, deny,", "silence, standing rule,", "or a runtime policy"),
        (51.2, 48.8, 21.6, 15.6, "Execution state", "May change by alias,", "reload, pointer, or", "later lookup"),
        (75.0, 48.8, 21.4, 15.6, "Executed object", "The command, request,", "or effect that", "commits"),
    ]
    for x, y, w, h, title, a, b, c in chain:
        rounded(ax, x, y, w, h, FILL_WHITE)
        label(ax, x + w / 2, y + h - 2.8, title, size=8.3)
        text_block(ax, x + w / 2, y + 5.6, [a, b, c], size=7.2, color=SLATE)
    for x1, x2 in ((25.2, 27.4), (49.0, 51.2), (72.8, 75.0)):
        arrow(ax, x1, 56.6, x2, 56.6)

    label(
        ax,
        50,
        45.0,
        "Approval integrity holds when the executed object is still the approved object, or still inside the approved predicate.",
        size=7.6,
        weight="normal",
        style="italic",
        color=SLATE,
    )

    label(ax, 50, 40.2, "Three included prototypes bind different objects", size=9.4)

    binds = [
        (4.2, 17.6, 29.4, 19.4, "Weng (2026)", "Command hash", "The dialog is rendered from", "the command. A later swap", "is refused if every path is", "mediated."),
        (35.3, 17.6, 29.4, 19.4, "Irshad et al. (2026)", "Fields re-read at dispatch", "Recipient and amount are", "stored, then read again on", "the outgoing request.", "A mismatch aborts."),
        (66.4, 17.6, 29.4, 19.4, "Q. Zhang (2026)", "Commit-time effect", "The consent predicate is", "rechecked against the effect", "at commit, which can change", "after the call is approved."),
    ]
    for x, y, w, h, cite, obj, a, b, c, d in binds:
        rounded(ax, x, y, w, h, FILL_BIND, edgecolor="#1F5C3A")
        label(ax, x + w / 2, y + h - 2.6, cite, size=8.0, color="#1F5C3A")
        label(ax, x + w / 2, y + h - 5.6, obj, size=8.0, weight="normal", style="italic")
        text_block(ax, x + w / 2, y + 6.2, [a, b, c, d], size=7.1, color=SLATE)

    rounded(ax, 4.2, 3.6, 91.6, 11.2, FILL_MUTED, lw=0.9)
    text_block(
        ax,
        50,
        9.2,
        [
            "Twelve of the 15 included reports do not describe a binding check.",
            "Huq et al. (2025) treat silence as acceptance. Pochampally et al. (2026) sent email with no approval of that email.",
            "No included study tests whether people notice when the approved object and the executed object diverge.",
        ],
        size=7.4,
        color=SLATE,
    )

    save(fig, "figure-2-approval-integrity")


def form_icon(ax, kind, cx, cy, color=NAVY):
    if kind == "plan":
        for i, w in enumerate((2.4, 2.0, 2.2, 1.6)):
            ax.plot([cx - 1.4, cx - 1.4 + w], [cy + 1.35 - 0.9 * i, cy + 1.35 - 0.9 * i], color=color, lw=1.15, zorder=4)
            ax.add_patch(Circle((cx - 1.85, cy + 1.35 - 0.9 * i), 0.16, facecolor=color, edgecolor=color, zorder=4))
    elif kind == "highlight":
        ax.add_patch(Rectangle((cx - 2.1, cy - 1.3), 4.2, 2.6, fill=False, lw=1.1, edgecolor=color, zorder=4))
        ax.add_patch(Rectangle((cx - 0.35, cy - 0.15), 1.55, 0.95, fill=False, lw=1.35, edgecolor=color, zorder=4))
        ax.annotate("", xy=(cx + 1.2, cy + 0.8), xytext=(cx + 1.95, cy + 1.55), arrowprops=dict(arrowstyle="-|>", color=color, lw=1.05), zorder=4)
    elif kind == "description":
        ax.add_patch(Rectangle((cx - 2.0, cy - 1.45), 4.0, 2.9, fill=False, lw=1.1, edgecolor=color, zorder=4))
        ax.plot([cx - 1.35, cx + 1.35], [cy + 0.85, cy + 0.85], color=color, lw=1.0, zorder=4)
        ax.plot([cx - 1.35, cx + 0.95], [cy + 0.15, cy + 0.15], color=color, lw=1.0, zorder=4)
        ax.plot([cx - 1.35, cx + 1.15], [cy - 0.55, cy - 0.55], color=color, lw=1.0, zorder=4)
    elif kind == "draft":
        ax.add_patch(Polygon([(cx - 1.6, cy - 1.7), (cx - 1.6, cy + 1.7), (cx + 0.7, cy + 1.7), (cx + 1.6, cy + 0.8), (cx + 1.6, cy - 1.7)], fill=False, lw=1.15, edgecolor=color, zorder=4))
        ax.plot([cx + 0.7, cx + 0.7], [cy + 1.7, cy + 0.8], color=color, lw=1.0, zorder=4)
        ax.plot([cx + 0.7, cx + 1.6], [cy + 0.8, cy + 0.8], color=color, lw=1.0, zorder=4)
    elif kind == "diff":
        ax.text(cx - 1.35, cy + 0.55, "+", ha="center", va="center", fontsize=10, fontweight="bold", color="#1F5C3A", zorder=4)
        ax.text(cx - 1.35, cy - 0.7, "−", ha="center", va="center", fontsize=11, fontweight="bold", color="#7A3030", zorder=4)
        ax.plot([cx - 0.55, cx + 1.7], [cy + 0.55, cy + 0.55], color="#1F5C3A", lw=1.15, zorder=4)
        ax.plot([cx - 0.55, cx + 1.15], [cy - 0.7, cy - 0.7], color="#7A3030", lw=1.15, zorder=4)
    elif kind == "risk":
        ax.add_patch(Rectangle((cx - 2.05, cy - 1.5), 4.1, 3.0, fill=False, lw=1.1, edgecolor=color, zorder=4))
        ax.add_patch(Rectangle((cx - 2.05, cy + 0.85), 4.1, 0.65, facecolor=color, edgecolor=color, lw=0.6, zorder=4))
        ax.plot([cx - 1.35, cx + 1.2], [cy + 0.15, cy + 0.15], color=color, lw=0.95, zorder=4)
        ax.plot([cx - 1.35, cx + 0.7], [cy - 0.55, cy - 0.55], color=color, lw=0.95, zorder=4)
    elif kind == "none":
        ax.add_patch(Rectangle((cx - 2.1, cy - 1.35), 4.2, 2.7, fill=False, lw=1.15, edgecolor="#7A3030", linestyle=(0, (2.2, 1.6)), zorder=4))


def figure_3_preview_forms():
    fig, ax = plt.subplots(figsize=(7.28, 6.55))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    label(ax, 50, 96.2, "Preview forms in the included evidence", size=12)
    label(
        ax,
        50,
        91.8,
        "Counts are of reports that expose that object. A report can appear in more than one form.",
        size=7.6,
        weight="normal",
        style="italic",
        color=SLATE,
    )

    forms = [
        (3.6, 58.4, "plan", "Plan", "n = 4", "Intended sequence of steps", FILL_PREVIEW),
        (36.2, 58.4, "highlight", "Highlight", "n = 1", "Target of the next web action", FILL_PREVIEW),
        (68.8, 58.4, "description", "Description", "n = 3", "Action in prose, or a resolved effect", FILL_PREVIEW),
        (3.6, 27.2, "draft", "Draft", "n = 4", "Content that would be sent or inserted", FILL_CONTROL),
        (36.2, 27.2, "diff", "Diff", "n = 1", "Command beside the file change", FILL_CONTROL),
        (68.8, 27.2, "risk", "Risk card", "n = 2", "Safety-relevant fields beyond the call", FILL_CONTROL),
    ]
    for x, y, kind, title, n, blurb, fill in forms:
        rounded(ax, x, y, 27.6, 27.6, fill)
        form_icon(ax, kind, x + 13.8, y + 20.4)
        label(ax, x + 13.8, y + 13.6, title, size=10.4)
        label(ax, x + 13.8, y + 10.2, n, size=8.6, color=SLATE)
        text_block(ax, x + 13.8, y + 5.4, [blurb], size=7.3, color=SLATE)

    rounded(ax, 3.6, 5.2, 92.8, 17.8, FILL_EXCL, edgecolor="#7A3030")
    form_icon(ax, "none", 14.2, 14.1)
    label(ax, 32.6, 16.6, "No usable preview", size=10.4, color="#5C2424", ha="left")
    label(ax, 32.6, 12.8, "n = 2", size=8.6, color="#7A3030", ha="left")
    label(
        ax,
        32.6,
        8.8,
        "Pochampally et al. (2026): email sent with no draft.  S. Zhang et al. (2026): web actions without an inspectable confirmation.",
        size=7.4,
        weight="normal",
        color="#5C2424",
        ha="left",
    )

    save(fig, "figure-3-preview-forms")


if __name__ == "__main__":
    figure_1_prisma()
    figure_2_framework()
    figure_3_preview_forms()
    print("wrote figures to", OUT)
