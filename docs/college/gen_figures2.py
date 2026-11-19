# -*- coding: utf-8 -*-
"""Build the final report's evidence-backed, print-readable figures.

Charts read the local ApplyPilot SQLite snapshot. The Workday screenshot is a
separately supplied demonstration asset; it is evidence of an intermediate UI
state, not of a successful submission.
"""
from collections import Counter
from pathlib import Path
import sqlite3

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

OUT = Path(__file__).resolve().parent
DB_PATH = Path.home() / ".applypilot" / "applypilot.db"
NAVY = "#18324B"
BLUE = "#2E6F9E"
PALE_BLUE = "#EAF2F8"
TEAL = "#187E82"
PALE_TEAL = "#E8F4F2"
AMBER = "#A86512"
PALE_AMBER = "#FFF4DD"
RED = "#A94343"
PALE_RED = "#F9EAEA"
GREEN = "#33745B"
PALE_GREEN = "#EAF4EE"
SLATE = "#566779"
PALE = "#F5F7F9"
INK = "#172B3A"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "text.color": INK,
    "axes.labelcolor": INK,
    "axes.edgecolor": "#A8B4BF",
    "xtick.color": SLATE,
    "ytick.color": SLATE,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})


def frame(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("auto")
    ax.axis("off")


def box(ax, x, y, w, h, text, *, fc=PALE_BLUE, ec=BLUE, fs=8.2,
        weight="semibold", color=INK, radius=0.1, lw=1.25):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.035,rounding_size={radius}",
        facecolor=fc, edgecolor=ec, linewidth=lw,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, weight=weight, color=color, linespacing=1.25)
    return patch


def arrow(ax, start, end, *, color=SLATE, lw=1.25, style="-|>",
          linestyle="-", rad=0.0, scale=11):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle=style, mutation_scale=scale,
        linewidth=lw, color=color, linestyle=linestyle,
        connectionstyle=f"arc3,rad={rad}", shrinkA=2, shrinkB=2,
    ))


def save(fig, name):
    fig.savefig(OUT / name, dpi=300, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


if not DB_PATH.exists():
    raise FileNotFoundError(f"Expected the local measurement database at {DB_PATH}")
con = sqlite3.connect(f"file:{DB_PATH.as_posix()}?mode=ro", uri=True)
con.row_factory = sqlite3.Row
jobs_total = con.execute("SELECT COUNT(*) FROM jobs").fetchone()[0]
scored = [r[0] for r in con.execute(
    "SELECT fit_score FROM jobs WHERE fit_score IS NOT NULL ORDER BY fit_score"
)]
strategies = con.execute(
    "SELECT COALESCE(strategy, 'unknown'), COUNT(*) FROM jobs GROUP BY strategy ORDER BY COUNT(*) DESC"
).fetchall()
sources = con.execute(
    "SELECT COALESCE(site, 'unknown'), COUNT(*) FROM jobs GROUP BY site ORDER BY COUNT(*) DESC"
).fetchall()
resume_rows = con.execute(
    "SELECT COUNT(*) FROM jobs WHERE tailored_resume_path IS NOT NULL"
).fetchone()[0]
resume_paths = con.execute(
    "SELECT COUNT(DISTINCT tailored_resume_path) FROM jobs WHERE tailored_resume_path IS NOT NULL"
).fetchone()[0]
cover_rows = con.execute(
    "SELECT COUNT(*) FROM jobs WHERE cover_letter_path IS NOT NULL"
).fetchone()[0]
cover_paths = con.execute(
    "SELECT COUNT(DISTINCT cover_letter_path) FROM jobs WHERE cover_letter_path IS NOT NULL"
).fetchone()[0]
apply_status = con.execute(
    "SELECT COALESCE(apply_status, 'not recorded'), COUNT(*) FROM jobs GROUP BY apply_status"
).fetchall()
con.close()

# Figure 1 — compact, legible system architecture with actual data boundaries.
fig, ax = plt.subplots(figsize=(7.2, 4.6))
frame(ax, (0, 12), (0, 8))
ax.text(0.22, 7.62, "CAREEROS · SYSTEM ARCHITECTURE", fontsize=11, weight="bold", color=NAVY)
ax.text(0.24, 7.26, "Batch preparation → local job state → optional browser-assisted application", fontsize=8.8, color=SLATE)
box(ax, 0.35, 6.10, 4.75, 0.78, "JOB INPUTS\nJobSpy boards · Workday APIs\nsearch rules", fc=PALE, ec=SLATE, fs=8.0)
box(ax, 6.90, 6.10, 4.75, 0.78, "CANDIDATE PROFILE\nresume facts · skills\napplication information", fc=PALE, ec=SLATE, fs=8.0)
# Stage sequence.
labels = ["1  Discover", "2  Enrich", "3  Score", "4  Tailor", "5  Cover", "6  Export"]
subs = ["JobSpy + ATS", "Job details", "LLM fit score", "Resume draft", "Letter draft", "PDF files"]
xs = [0.32, 2.28, 4.24, 6.20, 8.16, 10.12]
for i, x in enumerate(xs):
    color, fill = (BLUE, PALE_BLUE) if i < 3 else (TEAL, PALE_TEAL)
    box(ax, x, 4.72, 1.55, 0.92, f"{labels[i]}\n{subs[i]}", fc=fill, ec=color, fs=8.0)
    if i < len(xs) - 1:
        arrow(ax, (x + 1.58, 5.18), (xs[i + 1] - 0.04, 5.18), color=color, scale=10)
arrow(ax, (2.58, 6.10), (1.08, 5.66), color=SLATE, rad=0.05)
arrow(ax, (8.95, 6.10), (7.10, 5.66), color=SLATE, rad=-0.05)
# Checks and data store.
box(ax, 0.40, 3.18, 5.20, 0.90,
    "LOCAL SQLITE · one jobs table\nscores · statuses · artifact paths\ngenerated files/logs stored separately",
    fc=PALE_BLUE, ec=NAVY, fs=7.7)
box(ax, 6.35, 3.18, 5.20, 0.90,
    "DOCUMENT CHECKS · limited scope\nresume checks vary by mode\ncover-letter checks do not verify facts",
    fc=PALE_AMBER, ec=AMBER, fs=7.7)
arrow(ax, (5.02, 4.72), (3.10, 4.10), color=NAVY, linestyle="--", rad=0.05)
arrow(ax, (7.00, 4.72), (8.50, 4.10), color=AMBER, rad=-0.05)
ax.text(0.43, 2.77, "Reviewed resume sidecars: lenient mode; LLM judge skipped.", fontsize=8.0, color=AMBER, style="italic")
# Application boundary.
box(ax, 0.45, 0.88, 4.70, 1.15,
    "OPTIONAL APPLY WORKER\nOpenCode · Playwright MCP\nChrome DevTools Protocol",
    fc=PALE_RED, ec=RED, fs=7.8)
box(ax, 6.85, 0.88, 4.70, 1.15,
    "EMPLOYER PORTAL\ndry-run and submit modes\nseparately configurable",
    fc=PALE, ec=SLATE, fs=7.8)
arrow(ax, (5.62, 3.18), (3.15, 2.04), color=NAVY, rad=0.05)
arrow(ax, (5.16, 1.45), (6.82, 1.45), color=RED)
ax.text(0.46, 0.35, "External services receive requests; candidate/job content may be sent to the configured hosted model.", fontsize=7.7, color=SLATE)
save(fig, "fig1_architecture.png")

# Figure 2 — provenance: acquisition mechanism and largest stored source labels.
fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.25), gridspec_kw={"width_ratios": [0.88, 1.38]})
ax = axes[0]
strat_labels = [str(r[0]) for r in strategies]
strat_vals = [int(r[1]) for r in strategies]
pretty = ["Employer Workday APIs" if "workday" in s.lower() else "JobSpy boards" if "jobspy" in s.lower() else s for s in strat_labels]
colors = [TEAL if "workday" in s.lower() else BLUE if "jobspy" in s.lower() else SLATE for s in strat_labels]
y = list(range(len(pretty)))
ax.barh(y, strat_vals, color=colors, height=0.52)
ax.set_yticks(y, pretty)
ax.invert_yaxis()
ax.set_xlim(0, max(strat_vals, default=1) * 1.26)
ax.set_xlabel("Stored postings")
ax.set_title("A. Acquisition strategy", loc="left", color=NAVY, weight="bold", fontsize=9)
for i, v in enumerate(strat_vals):
    ax.text(v + max(strat_vals, default=1) * 0.025, i, f"{v:,}", va="center", fontsize=8, weight="bold")
ax.grid(axis="x", alpha=0.2)
ax.set_axisbelow(True)

ax = axes[1]
top = [(str(r[0]), int(r[1])) for r in sources[:8]]
rest = sum(int(r[1]) for r in sources[8:])
if rest:
    top.append((f"Other {len(sources) - 8} labels", rest))
top = top[::-1]
ylabels = [name if len(name) <= 27 else name[:25] + "…" for name, _ in top]
vals = [val for _, val in top]
ax.barh(range(len(vals)), vals, color=BLUE, height=0.56)
ax.set_yticks(range(len(vals)), ylabels)
ax.set_xlim(0, max(vals, default=1) * 1.22)
ax.set_xlabel("Stored postings")
ax.set_title(f"B. Largest stored source labels (n={len(sources)})", loc="left", color=NAVY, weight="bold", fontsize=9)
for i, v in enumerate(vals):
    ax.text(v + max(vals, default=1) * 0.018, i, f"{v:,}", va="center", fontsize=7.7)
ax.grid(axis="x", alpha=0.2)
ax.set_axisbelow(True)
fig.suptitle(f"Discovery snapshot · {jobs_total:,} unique job URLs", x=0.02, ha="left", fontsize=10, weight="bold", color=NAVY)
fig.tight_layout(rect=(0, 0, 1, 0.91), w_pad=2.0)
save(fig, "fig2_data_provenance.png")

# Figure 3 — compact validation flow with clear mode-dependent branches.
fig, ax = plt.subplots(figsize=(7.0, 4.55))
frame(ax, (0, 12), (0, 8))
ax.text(0.25, 7.58, "DOCUMENT CHECKS · SCOPE AND MODE MATTER", fontsize=10.5, weight="bold", color=NAVY)
box(ax, 3.65, 6.35, 4.70, 0.78, "RESUME DRAFT\nLLM-generated JSON → formatted resume", fc=PALE_BLUE, ec=BLUE, fs=8.6)
box(ax, 2.50, 4.92, 7.00, 0.90,
    "STATIC CHECKS\nrequired fields · selected company/school · limited skill watch-list · text rules",
    fc=PALE, ec=SLATE, fs=8.3)
arrow(ax, (6.00, 6.35), (6.00, 5.84), color=BLUE)
# Mode branch.
diamond = Polygon([(6, 4.30), (7.05, 3.72), (6, 3.14), (4.95, 3.72)],
                  closed=True, facecolor=PALE_AMBER, edgecolor=AMBER, linewidth=1.3)
ax.add_patch(diamond)
ax.text(6, 3.72, "MODE", ha="center", va="center", fontsize=8.8, weight="bold", color=INK)
arrow(ax, (6.0, 4.92), (6.0, 4.31), color=AMBER)
box(ax, 0.55, 2.05, 4.35, 0.95, "LENIENT\nLLM judge skipped\nbanned-word checks off", fc=PALE_RED, ec=RED, fs=7.8)
box(ax, 7.10, 2.05, 4.35, 0.95, "NORMAL / STRICT\noptional prompt-based\nLLM judge runs", fc=PALE_AMBER, ec=AMBER, fs=7.8)
arrow(ax, (4.98, 3.55), (3.85, 3.01), color=RED)
arrow(ax, (7.02, 3.55), (8.15, 3.01), color=AMBER)
ax.text(0.60, 1.27, "MEASURED RESUMES: lenient mode · static checks passed · judge not run", fontsize=8.0, color=RED, weight="semibold")
# Limits in two uncluttered notes.
box(ax, 0.55, 0.25, 5.15, 0.72, "LLM judge is heuristic\nnot proof of factual accuracy", fc=PALE, ec=SLATE, fs=7.5)
box(ax, 6.30, 0.25, 5.15, 0.72, "Cover-letter checks: style/format only\nno factual-claim audit", fc=PALE, ec=SLATE, fs=7.5)
save(fig, "fig3_validator.png")

# Figure 4 — application flow with explicit dry-run and submit branches.
fig, ax = plt.subplots(figsize=(7.2, 3.75))
frame(ax, (0, 12), (0, 6.5))
ax.text(0.25, 6.15, "BROWSER-ASSISTED APPLICATION WORKFLOW", fontsize=10.5, weight="bold", color=NAVY)
main = [
    (0.30, 4.35, 2.15, 0.95, "JOB SELECTED\nposting + role", PALE_BLUE, BLUE),
    (2.70, 4.35, 2.15, 0.95, "ELIGIBILITY\nprompt-guided\ncheck", PALE_AMBER, AMBER),
    (5.10, 4.35, 2.15, 0.95, "FORM ENTRY\nprofile +\ndocuments", PALE_BLUE, BLUE),
    (7.50, 4.35, 1.75, 0.95, "REVIEW\nvisible fields", PALE_TEAL, TEAL),
    (9.50, 4.35, 2.15, 0.95, "SELECT MODE\ndry run or\nsubmit", PALE, SLATE),
]
for x, y, w, h, text, fc, ec in main:
    box(ax, x, y, w, h, text, fc=fc, ec=ec, fs=8.2)
for i in range(len(main) - 1):
    x, y, w, h, *_ = main[i]
    nx, ny, *_ = main[i + 1]
    arrow(ax, (x + w, y + h / 2), (nx - 0.02, ny + h / 2), color=BLUE, scale=10)
# Mode branches.
box(ax, 2.00, 2.25, 3.15, 0.95, "REFUSAL\nagent judges role\nineligible", fc=PALE_RED, ec=RED, fs=7.8)
box(ax, 6.35, 2.25, 2.20, 0.95, "DRY RUN\nstop before\nfinal Submit", fc=PALE_GREEN, ec=GREEN, fs=7.5)
box(ax, 9.15, 2.25, 2.50, 0.95, "SUBMIT MODE\nagent may click\nSubmit", fc=PALE_AMBER, ec=AMBER, fs=7.7)
arrow(ax, (3.75, 4.34), (3.60, 3.21), color=RED, linestyle="--")
arrow(ax, (10.15, 4.34), (7.50, 3.21), color=GREEN, linestyle="--", rad=0.10)
arrow(ax, (10.85, 4.34), (10.40, 3.21), color=AMBER, linestyle="--")
ax.text(0.35, 1.25, "Observed: Workday dry run reached Review; final Submit was left untouched.", fontsize=8.1, color=NAVY)
ax.text(0.35, 0.67, "Submit mode exists, so human approval is not guaranteed by the architecture.", fontsize=8.1, color=SLATE)
save(fig, "fig4_apply_flow.png")

# Figure 5 — fit-score histogram generated directly from the database.
fig, ax = plt.subplots(figsize=(7.2, 3.5))
counts = Counter(int(v) for v in scored)
xs = list(range(1, 11))
ys = [counts.get(x, 0) for x in xs]
colors = [RED if x <= 3 else AMBER if x <= 6 else TEAL for x in xs]
ax.bar(xs, ys, color=colors, width=0.72, edgecolor="white", linewidth=0.8)
for x, y in zip(xs, ys):
    if y:
        ax.text(x, y + 0.24, str(y), ha="center", va="bottom", fontsize=8, weight="bold", color=NAVY)
threshold = sum(v >= 7 for v in scored)
rate = 100 * threshold / len(scored) if scored else 0
ax.axvline(6.5, color=NAVY, linestyle=(0, (4, 3)), linewidth=1.25)
ax.text(6.63, max(ys or [0]) * 0.93,
        f"configured threshold ≥ 7\n{threshold}/{len(scored)} = {rate:.1f}%",
        fontsize=7.2, color=NAVY, va="top")
ax.set_xticks(xs)
ax.set_xlim(0.4, 10.6)
ax.set_ylim(0, max(ys or [1]) * 1.28)
ax.set_xlabel("LLM-assigned fit score")
ax.set_ylabel("Job records")
ax.set_title(f"Scoring snapshot · n={len(scored)}", loc="left", color=NAVY, weight="bold", fontsize=9.5)
ax.grid(axis="y", alpha=0.22)
ax.set_axisbelow(True)
fig.tight_layout()
save(fig, "fig5_scores.png")

# Figure 6 — concise evidence summary; keep database and transcript counts distinct.
fig, ax = plt.subplots(figsize=(7.2, 3.20))
frame(ax, (0, 12), (0, 5.6))
ax.text(0.25, 5.25, "OBSERVED OUTPUTS · DATABASE SNAPSHOT", fontsize=10.2, weight="bold", color=NAVY)
metrics = [
    (0.32, "JOB URLS", f"{jobs_total:,}", BLUE),
    (2.68, "SCORED", f"{len(scored):,}\n{threshold}/{len(scored)} ≥ 7", BLUE),
    (5.04, "RESUME", f"{resume_rows} rows\n{resume_paths} paths", TEAL),
    (7.40, "COVER LETTER", f"{cover_rows} rows\n{cover_paths} paths", AMBER),
]
for x, label, value, color in metrics:
    box(ax, x, 3.45, 2.15, 1.35, f"{label}\n\n{value}", fc="white", ec=color, fs=8.1)
status_text = " · ".join(f"{name}: {count}" for name, count in apply_status)
box(ax, 0.45, 1.65, 5.30, 1.05,
    "SQLITE STATUS\nnot recorded: 725 · failed: 6",
    fc=PALE, ec=SLATE, fs=7.8)
box(ax, 6.25, 1.65, 5.30, 1.05,
    "WORKER LOGS\n1 dry run reached Review\n2 eligibility refusals",
    fc=PALE_GREEN, ec=GREEN, fs=7.8)
ax.text(0.47, 0.82, "Rows are job-record associations; paths are distinct files.", fontsize=7.8, color=SLATE)
ax.text(0.47, 0.38, "Dry-run/refusal counts come from transcripts, not a dedicated attempt-history table.", fontsize=7.8, color=SLATE, style="italic")
save(fig, "fig6_outputs.png")

print(f"Created 6 report figures from the local snapshot: {jobs_total} jobs, {len(scored)} scored, "
      f"{threshold if scored else 0}/{len(scored)} scores >=7, "
      f"{resume_rows} resume links/{resume_paths} paths, {cover_rows} cover links/{cover_paths} paths.")
