# -*- coding: utf-8 -*-
"""Build official-IEEE-conference-format paper by reusing gen_final_report.py's
   paper body (content parity guaranteed) with a proper IEEE preamble."""
from pathlib import Path
import re

DIR = Path(__file__).parent
src = (DIR / "gen_final_report.py").read_text(encoding="utf-8")

# Extract helper preamble (imports + helpers + doc init, up to FRONT MATTER marker)
i_front = src.index("# ================= FRONT MATTER")
head = src[:i_front]

# Extract paper body (from PAPER BODY marker to ANNEXURES marker)
i_body = src.index("# ================= PAPER BODY")
i_annex = src.index("# ---- ANNEXURES (single column)")
body = src[i_body:i_annex]

out = []
out.append("# -*- coding: utf-8 -*-\n# Official IEEE conference-format paper generated from the report's paper body.")
out.append(head)
# Replace the front-matter doc init with IEEE A4 settings (reuse head's Document() as-is; margins patched below)
out.append('''
# ---- IEEE title/author/abstract block (full width, before two-column body) ----
def _ieee_par(text, size, bold=False, italic=False, align=None, space_after=4, line=1.0):
    par = doc.add_paragraph(); par.alignment = align if align else J
    par.paragraph_format.space_after = Pt(space_after); par.paragraph_format.line_spacing = line
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    return par

_ieee_par("ApplyPilot: An Honesty-Enforcing LLM-Agent Pipeline for End-to-End Job Application Automation on Free-Tier Resources", 24, bold=True, align=C, space_after=10)
_ieee_par("Shashank Tomar", 11, bold=True, align=C, space_after=2)
_ieee_par("Department of Computer Science & Engineering", 10, italic=True, align=C, space_after=0)
_ieee_par("ABES Engineering College, Ghaziabad, UP, India", 10, italic=True, align=C, space_after=0)
_ieee_par("Email: [author email] ; ORCID: [0000-0000-0000-0000]", 10, italic=True, align=C, space_after=8)

# Abstract (bold, 9pt, IEEE style) - trimmed to ~200 words
_abs = ("Automated job application is dominated by mass-submission bots that misrepresent candidates or by closed "
        "commercial services. This paper presents ApplyPilot, a free-tier, locally-run pipeline that couples large "
        "language model (LLM) agents with an honesty-enforcement architecture to automate the application lifecycle: "
        "multi-board discovery, enrichment, fit scoring, resume tailoring, cover-letter generation, and autonomous "
        "submission through the employer's own career portal. We introduce a generator-critic honesty validator that "
        "rejects content not evidenced by the candidate's verified facts, an eligibility gate that refuses jobs the "
        "candidate cannot take, and a structured verdict protocol that makes every agent action auditable. On a live "
        "deployment targeting an India+remote profile, the system discovered 731 postings from eight sources, scored "
        "48 jobs (18.8% at fit \\u22657), produced nine validator-approved tailored resumes and five cover letters, and "
        "completed an end-to-end autonomous application on a live Workday portal - account creation, form "
        "navigation, resume upload, draft saved at the Review step - while autonomously refusing two ineligible "
        "postings after verifying eligibility against the employers' own APIs. We describe the architecture, "
        "integrity mechanisms, measured results, and failure modes of free-tier agentic deployment.")
_p = doc.add_paragraph(); _p.alignment = J; _p.paragraph_format.space_after = Pt(4); _p.paragraph_format.line_spacing = 1.0
_r = _p.add_run("Abstract\\u2014"); _r.font.name = TNR; _r.font.size = Pt(9); _r.bold = True
_r2 = _p.add_run(_abs); _r2.font.name = TNR; _r2.font.size = Pt(9); _r2.bold = True; _r2.italic = True
_k = doc.add_paragraph(); _k.alignment = J; _k.paragraph_format.space_after = Pt(6); _k.paragraph_format.line_spacing = 1.0
_r3 = _k.add_run("Index Terms\\u2014"); _r3.font.name = TNR; _r3.font.size = Pt(9); _r3.bold = True; _r3.italic = True
_r4 = _k.add_run("autonomous agents; browser automation; honesty validation; job application automation; large language models; resume tailoring; web agents; Workday")
_r4.font.name = TNR; _r4.font.size = Pt(9); _r4.bold = True; _r4.italic = True

''')
out.append(body)
out.append('''
# IEEE footer line
_e = doc.add_paragraph(); _e.alignment = C; _e.paragraph_format.line_spacing = 1.0
_r = _e.add_run("Preprint version \\u2014 submitted to [CONFERENCE NAME], [DATE]. Preprint DOI: [zenodo DOI]")
_r.font.name = TNR; _r.font.size = Pt(9); _r.italic = True

doc.save(DIR + "ApplyPilot_IEEE_Submission.docx")
print("IEEE SUBMISSION PAPER SAVED")''')

code = "\n".join(out)
# Patch margins for IEEE (A4, 0.75in top/bottom handled by section setup later; set top-level here)
code = code.replace("sec.top_margin = Inches(0.9); sec.bottom_margin = Inches(0.9)", "sec.top_margin = Inches(0.75); sec.bottom_margin = Inches(0.75)")
(DIR / "gen_ieee_paper.py").write_text(code, encoding="utf-8")
print("gen_ieee_paper.py written,", len(code), "chars")
