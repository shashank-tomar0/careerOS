# -*- coding: utf-8 -*-
"""Generate research-paper figures from REAL ApplyPilot run data."""
import sqlite3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = "C:/Users/dell/Desktop/mini-project/docs/college/"
plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.grid": True, "grid.alpha": 0.3})
DB = sqlite3.connect(r"C:/Users/dell/.applypilot/applypilot.db")

# ---------- Fig 1: pipeline architecture ----------
fig, ax = plt.subplots(figsize=(7.0, 3.4), dpi=300)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4.4)
stages = [("Discover\n731 jobs", 0.4), ("Enrich\nfull text", 1.9), ("Score\n1-10 fit", 3.4),
          ("Tailor\nhonest resume", 4.9), ("Cover\nletter", 6.4), ("PDF\nconvert", 7.9)]
boxes = []
for label, x in stages:
    b = FancyBboxPatch((x, 2.6), 1.5, 1.0, boxstyle="round,pad=0.08",
                       fc="#dbeafe", ec="#1e40af", lw=1.2)
    ax.add_patch(b); ax.text(x+0.75, 3.1, label, ha="center", va="center", fontsize=8.5, weight="bold")
    boxes.append(b)
for i in range(len(stages)-1):
    ax.add_patch(FancyArrowPatch((stages[i][1]+1.5, 3.1), (stages[i+1][1], 3.1),
                 arrowstyle="-|>", mutation_scale=12, color="#1e40af", lw=1.2))
db = FancyBboxPatch((3.4, 0.5), 3.2, 0.9, boxstyle="round,pad=0.08", fc="#f1f5f9", ec="#475569", lw=1.2)
ax.add_patch(db); ax.text(5.0, 0.95, "SQLite checkpoint store\n(jobs · resumes · attempts)", ha="center", va="center", fontsize=8.5)
for _, x in stages:
    ax.add_patch(FancyArrowPatch((x+0.75, 2.6), (min(max(x+0.75, 3.4), 6.6), 1.4),
                 arrowstyle="-", color="#94a3b8", lw=0.7, linestyle=":"))
agent = FancyBboxPatch((8.2, 0.5), 1.7, 0.9, boxstyle="round,pad=0.08", fc="#fee2e2", ec="#b91c1c", lw=1.2)
ax.add_patch(agent); ax.text(9.05, 0.95, "Apply agent\n(real browser)", ha="center", va="center", fontsize=8.5, weight="bold")
ax.add_patch(FancyArrowPatch((7.9+0.75, 2.6), (9.05, 1.4), arrowstyle="-|>", mutation_scale=12, color="#b91c1c", lw=1.2))
val = FancyBboxPatch((4.6, 3.9), 3.2, 0.42, boxstyle="round,pad=0.05", fc="#fef9c3", ec="#a16207", lw=1.0)
ax.add_patch(val); ax.text(6.2, 4.11, "Honesty validator (generator-critic)", ha="center", va="center", fontsize=7.8, style="italic")
plt.tight_layout(); plt.savefig(OUT+"fig1_pipeline.png", bbox_inches="tight"); plt.close()

# ---------- Fig 2: real score distribution ----------
scores = [r[0] for r in DB.execute("select fit_score from jobs where fit_score is not null").fetchall()]
fig, ax = plt.subplots(figsize=(3.4, 2.3), dpi=300)
import collections
cnt = collections.Counter(scores)
xs = list(range(0, 11)); ys = [cnt.get(x, 0) for x in xs]
colors = ["#ef4444" if x <= 3 else ("#f59e0b" if x <= 6 else "#22c55e") for x in xs]
ax.bar(xs, ys, color=colors, edgecolor="#1e293b", lw=0.5)
for x, y in zip(xs, ys):
    if y: ax.text(x, y+0.15, str(y), ha="center", fontsize=7.5)
ax.set_xlabel("LLM fit score"); ax.set_ylabel("jobs")
ax.set_title(f"Fit-score distribution, n={len(scores)} scored jobs", fontsize=9)
ax.set_xticks(range(0, 11)); ax.set_ylim(0, max(ys)+1.2)
plt.tight_layout(); plt.savefig(OUT+"fig2_scores.png", bbox_inches="tight"); plt.close()

# ---------- Fig 3: funnel ----------
fig, ax = plt.subplots(figsize=(3.4, 2.3), dpi=300)
stages_f = ["Discovered", "Scored", "Tailored\n(resumes)", "Cover\nletters", "Dry-run\napplied"]
vals_f = [731, 48, 9, 5, 1]
bars = ax.bar(range(5), vals_f, color=["#1e40af", "#3b82f6", "#10b981", "#34d399", "#f59e0b"], edgecolor="#1e293b", lw=0.5)
ax.set_yscale("log"); ax.set_ylim(0.7, 1500)
labels = ["731", "48", "9", "5", "1 (+2 refusals)"]
for i, (v, l) in enumerate(zip(vals_f, labels)):
    ax.text(i, v*1.25, l, ha="center", fontsize=7.5, weight="bold")
ax.set_xticks(range(5)); ax.set_xticklabels(stages_f, fontsize=7.5)
ax.set_ylabel("jobs (log scale)"); ax.set_title("Pipeline funnel (measured run)", fontsize=9)
plt.tight_layout(); plt.savefig(OUT+"fig3_funnel.png", bbox_inches="tight"); plt.close()

# ---------- Fig 4: sources ----------
rows = DB.execute("select site, count(*) from jobs group by site order by 2 desc limit 10").fetchall()
fig, ax = plt.subplots(figsize=(3.4, 2.3), dpi=300)
names = [r[0][:18] for r in rows][::-1]; counts = [r[1] for r in rows][::-1]
ax.barh(range(len(rows)), counts, color="#6366f1", edgecolor="#1e293b", lw=0.4)
ax.set_yticks(range(len(rows))); ax.set_yticklabels(names, fontsize=7.5)
for i, v in enumerate(counts):
    ax.text(v+3, i, str(v), va="center", fontsize=7.5)
ax.set_xlabel("postings"); ax.set_title("Top discovery sources (731 total)", fontsize=9)
ax.set_xlim(0, max(counts)*1.18)
plt.tight_layout(); plt.savefig(OUT+"fig4_sources.png", bbox_inches="tight"); plt.close()

# ---------- Fig 5: agent flow ----------
fig, ax = plt.subplots(figsize=(7.0, 2.9), dpi=300)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 3.2)
flow = [("Eligibility\ncheck", 0.3, "#fef3c7", "#a16207"), ("Open form\n+ account", 1.9, "#dbeafe", "#1e40af"),
        ("Fill fields\n(true facts)", 3.5, "#dbeafe", "#1e40af"), ("Upload\ntailored PDF", 5.1, "#dbeafe", "#1e40af"),
        ("Screening\nquestions", 6.7, "#dbeafe", "#1e40af"), ("Review page\n(dry-run stop)", 8.3, "#dcfce7", "#166534")]
for label, x, fc, ec in flow:
    ax.add_patch(FancyBboxPatch((x, 1.7), 1.5, 0.95, boxstyle="round,pad=0.08", fc=fc, ec=ec, lw=1.1))
    ax.text(x+0.75, 2.18, label, ha="center", va="center", fontsize=7.8, weight="bold")
for i in range(len(flow)-1):
    ax.add_patch(FancyArrowPatch((flow[i][1]+1.5, 2.18), (flow[i+1][1], 2.18), arrowstyle="-|>", mutation_scale=11, color="#374151", lw=1.0))
ref = FancyBboxPatch((0.3, 0.25), 2.6, 0.75, boxstyle="round,pad=0.06", fc="#fee2e2", ec="#b91c1c", lw=1.1)
ax.add_patch(ref); ax.text(1.6, 0.63, "NOT eligible ->\nRESULT:FAILED:not_eligible_location", ha="center", va="center", fontsize=7.2, color="#7f1d1d")
ax.add_patch(FancyArrowPatch((1.05, 1.7), (1.4, 1.0), arrowstyle="-|>", mutation_scale=10, color="#b91c1c", lw=1.0, linestyle="--"))
sub = FancyBboxPatch((6.6, 0.25), 3.2, 0.75, boxstyle="round,pad=0.06", fc="#dcfce7", ec="#166534", lw=1.1)
ax.add_patch(sub); ax.text(8.2, 0.63, "submit mode -> click Submit & verify\nRESULT:APPLIED | dry-run -> save draft", ha="center", va="center", fontsize=7.2, color="#14532d")
ax.add_patch(FancyArrowPatch((9.05, 1.7), (8.6, 1.0), arrowstyle="-|>", mutation_scale=10, color="#166534", lw=1.0, linestyle="--"))
plt.tight_layout(); plt.savefig(OUT+"fig5_agent.png", bbox_inches="tight"); plt.close()

print("FIGURES DONE:", len(scores), "real scores used")
