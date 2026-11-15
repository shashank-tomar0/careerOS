# -*- coding: utf-8 -*-
"""Publication-grade figures (300 DPI, IEEE-safe, consistent design system)."""
import sqlite3
import collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

OUT = "C:/Users/dell/Desktop/mini-project/docs/college/"
plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 9, "axes.grid": True, "grid.alpha": 0.25, "grid.linestyle": "-", "axes.spines.top": False, "axes.spines.right": False})

NAVY = "#0F2A43"; BLUE = "#2563EB"; LBLUE = "#DBEAFE"; SLATE = "#64748B"
GREEN = "#15803D"; LGREEN = "#DCFCE7"; AMBER = "#B45309"; LAMBER = "#FEF3C7"
RED = "#B91C1C"; LRED = "#FEE2E2"; BG = "#FFFFFF"

def rbox(ax, x, y, w, h, text, fc, ec, fs=8.5, weight="normal", tc=None, radius=0.10, lw=1.1, style="round,pad=0.06"):
    b = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0.06,rounding_size={radius}", fc=fc, ec=ec, lw=lw)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs, weight=weight, color=tc or NAVY, linespacing=1.25)
    return b

def arrow(ax, x1, y1, x2, y2, color=SLATE, lw=1.2, ls="-", style="-|>", scale=12):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=scale, color=color, lw=lw, linestyle=ls))

# ============================================================
# FIG 1 — System architecture (layered, editorial)
# ============================================================
fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=300)
ax.axis("off"); ax.set_xlim(0, 10.6); ax.set_ylim(0, 4.6)
ax.add_patch(FancyBboxPatch((0.05, 0.1), 10.5, 4.4, boxstyle="round,pad=0.02", fc="#F8FAFC", ec="#CBD5E1", lw=0.8))

# Lane labels
ax.text(0.25, 3.95, "BATCH STAGES", fontsize=7.5, weight="bold", color=SLATE)
ax.text(0.25, 1.28, "STATE & AGENT", fontsize=7.5, weight="bold", color=SLATE)

stages = [("DISCOVER\n5 boards +\nWorkday APIs", LBLUE, BLUE),
          ("ENRICH\nfull text\nPlaywright", LBLUE, BLUE),
          ("SCORE\nLLM rubric\n1\u201310 fit", LBLUE, BLUE),
          ("TAILOR\nresume\nrewrite", LGREEN, GREEN),
          ("COVER\nvalidated\nletters", LGREEN, GREEN),
          ("PDF\nconvert\nreports", LGREEN, GREEN)]
x = 0.35
coords = []
for label, fc, ec in stages:
    rbox(ax, x, 2.9, 1.42, 1.0, label, fc, ec, fs=7.8, weight="bold")
    coords.append(x); x += 1.68
for i in range(len(coords) - 1):
    arrow(ax, coords[i] + 1.42, 3.4, coords[i+1], 3.4, color=BLUE)

# validator banner
rbox(ax, 3.6, 2.15, 4.6, 0.5, "HONESTY VALIDATOR \u2014 generator\u2013critic gate (code, not model)", LAMBER, AMBER, fs=7.8, style="italic")
for cx in (5.15, 6.85):
    arrow(ax, cx, 2.9, cx, 2.65, color=AMBER, ls="--", lw=0.9)
    arrow(ax, cx, 2.65, cx, 2.9, color=GREEN, ls="--", lw=0.9)

# config row
rbox(ax, 0.35, 2.15, 2.6, 0.5, ".env \u00b7 profile.json \u00b7 searches.yaml", "#F1F5F9", SLATE, fs=7.5)
arrow(ax, 1.65, 2.65, 1.65, 2.9, color=SLATE, lw=0.9)

# store + agent
rbox(ax, 3.0, 0.45, 3.4, 0.85, "SQLite CHECKPOINT STORE\njobs \u00b7 resumes \u00b7 cover_letters \u00b7 apply_attempts", "#EEF2FF", NAVY, fs=8, weight="bold")
for cx in coords:
    arrow(ax, min(max(cx + 0.71, 3.4), 6.0), 2.9, min(max(cx + 0.71, 3.4), 6.0), 1.32, color="#94A3B8", lw=0.6, ls=":", style="-")
ax.text(8.6, 3.62, "APPLY AGENT", fontsize=7.5, weight="bold", color=RED)
rbox(ax, 7.2, 0.45, 3.15, 0.85, "autonomous agent\nOpenCode + GLM\nreal Chrome via CDP", LRED, RED, fs=8, weight="bold")
arrow(ax, 9.0, 0.87, 6.4, 0.87, color=RED, lw=1.3, style="<|-")
arrow(ax, 6.4, 1.72, 8.4, 1.32, color=RED, lw=1.3, style="-")
ax.text(7.2, 1.52, "tailored docs \u2192", fontsize=7, color=RED, style="italic")
ax.text(4.7, 0.06, "every action audited \u2022 resumable \u2022 dashboard (status /)", fontsize=7, color=SLATE, style="italic", ha="center")
plt.savefig(OUT + "fig1_pipeline.png", bbox_inches="tight", facecolor=BG); plt.close()

# ============================================================
# FIG 5 — Apply agent flow (decision diamonds)
# ============================================================
fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=300)
ax.axis("off"); ax.set_xlim(0, 10.6); ax.set_ylim(0, 4.0)
steps = [("ELIGIBILITY\nCHECK\n(posting +\nemployer API)", 0.25, LAMBER, AMBER),
         ("APPLY gate:\neligible?", 1.85, "#FFF7ED", AMBER),
         ("OPEN FORM\naccount\ncreation", 3.45, LBLUE, BLUE),
         ("FILL FIELDS\ntrue facts\nonly", 5.05, LBLUE, BLUE),
         ("UPLOAD\ntailored\nresume PDF", 6.65, LBLUE, BLUE),
         ("SCREENING\ntruthful\nanswers", 8.25, LBLUE, BLUE)]
for label, x, fc, ec in steps:
    rbox(ax, x, 2.55, 1.5, 1.05, label, fc, ec, fs=7.6, weight="bold")
for i in range(len(steps) - 1):
    arrow(ax, steps[i][1] + 1.5, 3.07, steps[i+1][1], 3.07, color=SLATE)
rbox(ax, 9.9 - 1.5, 2.55, 1.5, 1.05, "REVIEW\nPAGE\nreached", LGREEN, GREEN, fs=7.6, weight="bold")
arrow(ax, 9.75, 3.07, 9.9 - 1.5 + 1.5, 3.07, color=SLATE)
# decision outcomes
rbox(ax, 1.85, 0.6, 2.9, 0.8, "NOT ELIGIBLE \u2192\nRESULT:FAILED:not_eligible_location", LRED, RED, fs=7.2, tc="#7F1D1D")
arrow(ax, 2.6, 2.55, 2.9, 1.42, color=RED, ls="--", lw=1.1)
ax.text(2.5, 2.05, "no", fontsize=7, color=RED, style="italic")
rbox(ax, 5.6, 0.6, 4.7, 0.8, "submit mode \u2192 click Submit & verify \u2192 RESULT:APPLIED   |   dry-run \u2192 save draft, stop", LGREEN, GREEN, fs=7.2, tc="#14532D")
arrow(ax, 8.3, 2.55, 8.3, 1.42, color=GREEN, ls="--", lw=1.1)
ax.text(8.45, 2.05, "yes", fontsize=7, color=GREEN, style="italic")
ax.text(5.3, 0.22, "verdict protocol: RESULT:* persisted per attempt \u2014 complete audit trail", fontsize=7, color=SLATE, style="italic", ha="center")
plt.savefig(OUT + "fig5_agent.png", bbox_inches="tight", facecolor=BG); plt.close()

# ============================================================
# FIG 6 (NEW) — Honesty validator loop (portrait, column width)
# ============================================================
fig, ax = plt.subplots(figsize=(3.5, 3.8), dpi=300)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 11.6)
flow = [("TAILOR (LLM)\ngenerates document", 9.9, LBLUE, BLUE),
        ("NORMALISE +\nsegment claims", 8.0, "#F1F5F9", SLATE),
        ("RESOLVE entities vs\nprofile.json facts", 6.1, "#F1F5F9", SLATE),
        ("CLAIM VERDICT:\nparaphrase | omission | invention", 4.2, LAMBER, AMBER),
        ("SKILLS BOUNDARY\nlisted \u2713  unknown \u2717", 2.3, LAMBER, AMBER)]
for label, y, fc, ec in flow:
    rbox(ax, 1.2, y - 0.75, 7.6, 1.3, label, fc, ec, fs=7.6, weight="bold")
for y1, y2 in [(9.15, 8.75), (7.25, 6.85), (5.35, 4.95), (3.45, 3.05)]:
    arrow(ax, 5.0, y1, 5.0, y2, color=SLATE)
rbox(ax, 1.2, 0.35, 3.4, 1.15, "objections \u2192 back to\nLLM (\u2264 5 attempts)", LRED, RED, fs=7.4, tc="#7F1D1D")
arrow(ax, 3.4, 2.3, 3.0, 1.5, color=RED, ls="--", lw=1.1)
ax.text(2.7, 1.95, "rejected", fontsize=6.8, color=RED, style="italic")
rbox(ax, 5.4, 0.35, 3.4, 1.15, "ACCEPT + report\n(persisted artefact)", LGREEN, GREEN, fs=7.4, tc="#14532D")
arrow(ax, 6.6, 2.3, 7.0, 1.5, color=GREEN, ls="--", lw=1.1)
ax.text(7.3, 1.95, "clean", fontsize=6.8, color=GREEN, style="italic")
plt.savefig(OUT + "fig6_validator.png", bbox_inches="tight", facecolor=BG); plt.close()

# ============================================================
# FIG 7 (NEW) — Measured stage timings (real data)
# ============================================================
fig, ax = plt.subplots(figsize=(3.5, 2.4), dpi=300)
items = [("24-job scoring batch", 78/60, "1.3 min"),
         ("48-job scoring pass", 4, "~4 min"),
         ("Tailoring + validation (per doc)", 1, "<1 min"),
         ("Full dry-run Workday application", 18, "~18 min")]
names = [i[0] for i in items][::-1]; vals = [i[1] for i in items][::-1]; labs = [i[2] for i in items][::-1]
bars = ax.barh(range(4), vals, color=[BLUE, BLUE, GREEN, RED], edgecolor=NAVY, lw=0.5, height=0.6)
ax.set_yticks(range(4)); ax.set_yticklabels(names, fontsize=7)
ax.set_xscale("log"); ax.set_xlim(0.4, 40)
for i, (v, l) in enumerate(zip(vals, labs)):
    ax.text(v * 1.15, i, l, va="center", fontsize=7, weight="bold")
ax.set_xlabel("minutes (log scale)", fontsize=7.5)
ax.set_title("Measured stage timings (live run)", fontsize=8.5)
plt.tight_layout(); plt.savefig(OUT + "fig7_timings.png", bbox_inches="tight", facecolor=BG); plt.close()

# ============================================================
# Charts 2/3/4 restyle (same real data)
# ============================================================
DB = sqlite3.connect(r"C:/Users/dell/.applypilot/applypilot.db")
scores = [r[0] for r in DB.execute("select fit_score from jobs where fit_score is not null").fetchall()]
cnt = collections.Counter(scores)
fig, ax = plt.subplots(figsize=(3.5, 2.4), dpi=300)
xs = list(range(0, 11)); ys = [cnt.get(x, 0) for x in xs]
colors = ["#EF4444" if x <= 3 else ("#F59E0B" if x <= 6 else "#16A34A") for x in xs]
ax.bar(xs, ys, color=colors, edgecolor=NAVY, lw=0.6)
for x, y in zip(xs, ys):
    if y: ax.text(x, y + 0.18, str(y), ha="center", fontsize=7.5)
ax.axvline(6.5, color=NAVY, ls="--", lw=1.0)
ax.text(6.65, max(ys)*0.92, "apply threshold \u22657\n18.8% of scored jobs", fontsize=6.8, color=NAVY)
ax.set_xlabel("LLM fit score"); ax.set_ylabel("jobs")
ax.set_title(f"Fit-score distribution, n={len(scores)} (live run)", fontsize=8.5)
ax.set_xticks(range(0, 11)); ax.set_ylim(0, max(ys) + 1.4)
plt.tight_layout(); plt.savefig(OUT + "fig2_scores.png", bbox_inches="tight", facecolor=BG); plt.close()

fig, ax = plt.subplots(figsize=(3.5, 2.4), dpi=300)
stages_f = ["Discovered", "Scored", "Tailored\nresumes", "Cover\nletters", "Dry-run\napplied"]
vals_f = [731, 48, 9, 5, 1]
ax.bar(range(5), vals_f, color=["#1E40AF", "#3B82F6", "#16A34A", "#4ADE80", "#F59E0B"], edgecolor=NAVY, lw=0.6)
ax.set_yscale("log"); ax.set_ylim(0.7, 1600)
labels = ["731", "48", "9", "5", "1 + 2\nrefusals"]
for i, (v, l) in enumerate(zip(vals_f, labels)):
    ax.text(i, v * 1.3, l, ha="center", fontsize=7.2, weight="bold")
ax.set_xticks(range(5)); ax.set_xticklabels(stages_f, fontsize=7)
ax.set_ylabel("jobs (log scale)"); ax.set_title("Pipeline funnel (measured run)", fontsize=8.5)
plt.tight_layout(); plt.savefig(OUT + "fig3_funnel.png", bbox_inches="tight", facecolor=BG); plt.close()

rows = DB.execute("select site, count(*) from jobs group by site order by 2 desc limit 10").fetchall()
fig, ax = plt.subplots(figsize=(3.5, 2.4), dpi=300)
names = [r[0][:20] for r in rows][::-1]; counts = [r[1] for r in rows][::-1]
ax.barh(range(len(rows)), counts, color="#4F46E5", edgecolor=NAVY, lw=0.5)
ax.set_yticks(range(len(rows))); ax.set_yticklabels(names, fontsize=7)
for i, v in enumerate(counts):
    ax.text(v + 3, i, str(v), va="center", fontsize=7)
ax.set_xlabel("postings"); ax.set_title("Top discovery sources (731 total)", fontsize=8.5)
ax.set_xlim(0, max(counts) * 1.2)
plt.tight_layout(); plt.savefig(OUT + "fig4_sources.png", bbox_inches="tight", facecolor=BG); plt.close()

print("7 PUBLICATION FIGURES DONE (300 DPI)")
