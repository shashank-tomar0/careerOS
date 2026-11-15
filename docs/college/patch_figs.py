# -*- coding: utf-8 -*-
"""Integrate fig6 (validator loop) + fig7 (timings); renumber figure captions."""
from pathlib import Path
p = Path(__file__).parent / "gen_final_report.py"
s = p.read_text(encoding="utf-8")

# --- 1. Renumber captions: agent Fig3->Fig4, scores Fig4->Fig5, funnel Fig5->Fig6 ---
s = s.replace('"Fig. 3. Apply-agent workflow', '"Fig. 4. Apply-agent workflow')
s = s.replace('"Fig. 4. Real fit-score distribution', '"Fig. 5. Real fit-score distribution')
s = s.replace('"Fig. 5. Pipeline funnel', '"Fig. 6. Pipeline funnel')
# in-text refs
s = s.replace("Fig. 3 shows the workflow", "Fig. 4 shows the workflow")
s = s.replace("The distribution (Fig. 4) is discriminating", "The distribution (Fig. 5) is discriminating")

# --- 2. Insert validator figure (Fig 3) after 4.2 Generator-Critic Loop paragraph ---
anchor = 'h2("C. Validator Algorithm")'
fig3_code = ('figure(DIR+"fig6_validator.png", 2.6, "Fig. 3. The honesty validator loop: deterministic claim '
             'resolution against verified facts; rejection returns structured objections to the generator (max 5 '
             'attempts), acceptance persists a report artefact.")\n')
assert anchor in s
s = s.replace(anchor, fig3_code + anchor, 1)

# --- 3. Insert timings figure (Fig 7) inside Timings subsection ---
anchor2 = 'pbf("Measured stage timings under free-tier conditions'
assert anchor2 in s
idx = s.index(anchor2)
end_par = s.index("\n", s.index('not by guesswork.")', idx)) + 1
fig7_code = ('figure(DIR+"fig7_timings.png", 2.6, "Fig. 7. Measured stage timings of the live run (log scale): '
             'batch stages are quota-bound and fast; the interactive dry-run application is navigation-bound.")\n')
s = s[:end_par] + fig7_code + s[end_par:]

# --- 4. LOF front-matter list -> 7 figures ---
old_lof = '''heading("LIST OF FIGURES", 14)
for f_, d_ in [("Fig. 1", "ApplyPilot architecture"),
               ("Fig. 2", "Top discovery sources (731 postings)"),
               ("Fig. 3", "Apply-agent workflow"),
               ("Fig. 4", "Fit-score distribution of 48 scored jobs"),
               ("Fig. 5", "Measured pipeline funnel (log scale)")]:
    p(f"{f_}\\t{d_}", 12, align=L, space_after=3)'''
new_lof = '''heading("LIST OF FIGURES", 14)
for f_, d_ in [("Fig. 1", "ApplyPilot architecture: batch stages, checkpoint store, honesty validator, apply agent"),
               ("Fig. 2", "Top discovery sources in the measured run (731 postings)"),
               ("Fig. 3", "The honesty validator loop (generator-critic with persisted verdicts)"),
               ("Fig. 4", "Apply-agent workflow: eligibility gate, truthful entry, mode-dependent termination"),
               ("Fig. 5", "Fit-score distribution of the 48 scored jobs"),
               ("Fig. 6", "Measured pipeline funnel (log scale)"),
               ("Fig. 7", "Measured stage timings of the live run (log scale)")]:
    p(f"{f_}\\t{d_}", 12, align=L, space_after=3)'''
assert old_lof in s
s = s.replace(old_lof, new_lof, 1)

p.write_text(s, encoding="utf-8")
print("FIGURES INTEGRATED")
