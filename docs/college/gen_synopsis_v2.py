# -*- coding: utf-8 -*-
"""APPLYPILOT SYNOPSIS v2 — polished, detailed, with embedded diagrams."""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

TNR = "Times New Roman"
J = WD_ALIGN_PARAGRAPH.JUSTIFY; C = WD_ALIGN_PARAGRAPH.CENTER; L = WD_ALIGN_PARAGRAPH.LEFT
DIR = "C:/Users/dell/Desktop/mini-project/docs/college/"
TITLE = "ApplyPilot: An Honesty-Enforcing LLM-Agent Pipeline for End-to-End Job Application Automation on Free-Tier Resources"

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.8); sec.bottom_margin = Inches(0.8)
sec.left_margin = Inches(0.9); sec.right_margin = Inches(0.9)
st = doc.styles["Normal"]; st.font.name = TNR; st.font.size = Pt(12)
st.paragraph_format.line_spacing = 1.4

def p(text, size=12, bold=False, italic=False, align=J, space_after=6, line=1.4):
    par = doc.add_paragraph(); par.alignment = align
    par.paragraph_format.space_after = Pt(space_after); par.paragraph_format.line_spacing = line
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    return par

def heading(text, size=14):
    return p(text, size=size, bold=True, align=L, space_after=8)

def bullet(text, size=12):
    par = doc.add_paragraph(style="List Bullet")
    par.paragraph_format.line_spacing = 1.4
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size)
    return par

def figure(fname, width, cap):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_after = Pt(2)
    par.add_run().add_picture(DIR + fname, width=Inches(width))
    p(cap, 10, italic=True, align=C, space_after=10)

# ---------- Header ----------
p("ABES ENGINEERING COLLEGE, GHAZIABAD", 16, bold=True, align=C, space_after=2)
p("(Affiliated to Dr. A.P.J. Abdul Kalam Technical University, Lucknow)", 11, align=C, space_after=2)
p("Department of Computer Science & Engineering", 13, bold=True, align=C, space_after=8)
p("SYNOPSIS REPORT", 16, bold=True, align=C, space_after=2)
p("(Session 2025-26)", 11, align=C, space_after=12)

# ---------- Info table ----------
rows = [
    ("Project Title:", TITLE, "", ""),
    ("Project Type:", "Application / Product (Software)", "", ""),
    ("", "Name", "Roll Number", "Section"),
    ("Group member (1)", "Shashank Tomar", "[ROLL NO.]", "[SECTION]"),
    ("Group member (2)", "[Member Name]", "[Roll No.]", "[Section]"),
    ("Group member (3)", "[Member Name]", "[Roll No.]", "[Section]"),
    ("Project Guide", "[GUIDE NAME] ([Designation])", "", ""),
    ("Signature", "", "", ""),
    ("Date of submission", "[DATE]", "", ""),
]
t = doc.add_table(rows=len(rows), cols=4); t.style = "Table Grid"
t.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, r in enumerate(rows):
    for j, v in enumerate(r):
        cell = t.cell(i, j); cell.text = ""
        run = cell.paragraphs[0].add_run(v)
        run.font.name = TNR; run.font.size = Pt(10)
        if i in (0, 2): run.bold = True
p("", 6, space_after=2)

# ---------- 1. Problem Introduction ----------
heading("1. Problem Introduction")
p("Manual job hunting is a high-volume, repetitive and mentally exhausting process. A candidate today must monitor multiple job portals (Indeed, Naukri, LinkedIn, Glassdoor, ZipRecruiter), read hundreds of postings, judge which roles genuinely match their skills, customise the resume for every application, and then fill long multi-page application forms on each employer's career site. A single application to a large employer using Workday \u2014 the HR system used by over half the Fortune 500 \u2014 involves account creation, four to six form pages, document upload and screening questions, taking 15\u201330 minutes of pure transcription. For a final-year engineering student applying to dozens of companies, this consumes weeks of productive time, and repetitive manual entry invites disqualifying mistakes.")
p("Meanwhile, modern Large Language Models (LLMs) can read job descriptions, understand a candidate's profile, and act as autonomous agents that browse websites and complete form-based workflows. This project applies that capability to build an autonomous, end-to-end job application pipeline \u2014 a personal career operating system (careerOS) \u2014 that discovers jobs, scores them honestly, tailors documents truthfully, and completes the employer's own application form in a real browser.")

# ---------- 2. Motivation ----------
heading("2. Motivation")
bullet("Application volume, not lack of skill, is the main bottleneck for fresh graduates: hundreds of postings must be filtered manually before a handful of quality applications are sent.")
bullet("Existing automation tools either misrepresent candidates (mass-submitters with one generic resume) or are closed, opaque and paid (SaaS bots). There is a need for a transparent, honest, locally-run system.")
bullet("LLM agents can now reliably operate real web UIs (fill forms, upload documents, navigate multi-step portals) \u2014 impossible for traditional automation scripts alone.")
bullet("Integrity as a first-class goal: an autonomous agent must never fabricate experience and must refuse jobs the candidate cannot take. The project builds an honesty-validation layer as a core subsystem, verified by an automated validator and demonstrated by observed refusals.")

# ---------- 3. Project Objective ----------
heading("3. Project Objective")
p("The expected outcomes after completion of the project are:")
bullet("A single-command pipeline that discovers jobs from five boards and employers' Workday career sites, de-duplicated in a local SQLite database.")
bullet("An AI fit-scoring stage rating every job 1\u201310 against the candidate's verified resume facts, with a fabrication watch-list.")
bullet("Honest resume tailoring: job-specific rewrites that may re-organise content but may never invent employers, projects, skills or metrics \u2014 enforced by an automated validator.")
bullet("Automatic cover-letter generation and PDF conversion of tailored documents.")
bullet("An autonomous browser agent that opens the employer's real application form, creates the candidate account, fills every field from true facts, uploads the tailored resume, and submits \u2014 or stops at the Review step in dry-run mode.")
bullet("Eligibility guarding: the agent verifies location/work-mode rules (India + remote for this candidate) and refuses ineligible applications instead of blindly submitting.")
bullet("A reproducible, free-tier-only deployment (local Python pipeline + free LLM APIs), published as an AGPL-3.0 fork for demonstration.")

# ---------- 4. Scope ----------
heading("4. Scope of the Project")
p("The system is an application/product for individual job seekers, particularly students and early-career engineers in India seeking remote or domestic roles. Application areas:")
bullet("Personal job-search automation for B.Tech students and working professionals.")
bullet("ATS-friendly resume tailoring with provable honesty constraints.")
bullet("A generalisable demonstration of LLM agents completing real enterprise web workflows (Workday is used by Fortune-500 employers).")
bullet("A study artefact for the ethics of automated job applications (what may an agent say and do on a person's behalf?).")
p("Out of scope: solving CAPTCHAs illegitimately, bypassing login walls or platform terms of service, and guaranteeing interview outcomes. The pipeline respects employer systems \u2014 it uses official public job APIs and posted application forms only.")

# ---------- 5. Proposed Method (with figures) ----------
heading("5. Proposed Method (Methodology)")
p("The system is a staged pipeline; each stage is idempotent, checkpointed in SQLite, and independently runnable from the CLI with optional --limit flags:")
bullet("Stage 1 \u2014 Discover: scrape multiple boards with python-jobspy (India + remote) and crawl employers' Workday career sites via public APIs; de-duplicate and store.")
bullet("Stage 2 \u2014 Enrich: fetch full descriptions for shortlisted jobs (Playwright renders JavaScript-heavy pages).")
bullet("Stage 3 \u2014 Score: an LLM rates each job 1\u201310 for fit against structured resume facts under a strict rubric; outputs parsed defensively and persisted.")
bullet("Stage 4 \u2014 Tailor: the LLM rewrites the resume per role; an independent honesty validator compares every claim against verified resume facts and returns specific objections on any fabrication (max 5 attempts). Approved documents are converted to PDF.")
bullet("Stage 5 \u2014 Cover: cover letters generated under the same validation regime.")
bullet("Stage 6 \u2014 Apply: an autonomous agent (OpenCode CLI driving the candidate's real Chrome via Playwright/CDP) checks eligibility first, fills the employer's application form from profile.json (true facts only), uploads the tailored resume PDF, and submits \u2014 or, in dry-run mode, stops at the Review step. Every outcome (applied / refused:reason / failed:reason) is logged to the database.")
figure("fig1_pipeline.png", 6.3, "System architecture: six batch stages around a SQLite checkpoint store, the honesty validator supervising generation, and the apply agent driving a real browser.")
figure("fig5_agent.png", 6.3, "Apply-agent workflow: eligibility gate before any form work, truthful field entry, and mode-dependent termination with structured verdicts.")

# ---------- 6. Related Previous Work ----------
heading("6. Related Previous Work")
p("(i) Auto_Jobs_Applier_AIHawk (open-source, 2024): an agent automating LinkedIn Easy-Apply with LLM-answered screening questions. It demonstrated mass auto-apply feasibility but had no honesty validation and no location-eligibility reasoning, and was later curtailed by platform enforcement. ApplyPilot deliberately keeps the honest-apply capability of such tools while removing the mass-spam behaviour.")
p("(ii) LazyApply (commercial SaaS): a paid desktop bot that bulk-submits applications with a fixed generic resume \u2014 its lack of tailoring and verification lowers response rates and can misrepresent candidates.")
p("(iii) Simplify (browser extension): autofills common application fields from a stored profile and tracks applications; it is manual-first (human clicks every submit) and performs no discovery, scoring or tailoring.")
p("(iv) Research on web agents: ReAct (Yao et al., 2023) showed that interleaving reasoning and acting lets LLM agents operate interactive environments reliably; WebArena (Zhou et al., 2023) and WorkArena (Boisvert et al., 2024) benchmarked agents on realistic enterprise portals, including the multi-page form workflows this project automates on Workday. Wang et al. (2023) formalise the plan-act-observe agent architecture that our apply agent implements.")
p("No reviewed prior system combines multi-board discovery + honest AI scoring + validated tailoring + a real-browser autonomous apply agent in one free, locally-runnable pipeline \u2014 which is the contribution of this project.")

# ---------- 7. Software & Hardware ----------
heading("7. Software and Hardware Requirements")
p("Software:")
bullet("Windows 10/11 (64-bit); Python 3.13; SQLite (bundled); Git.")
bullet("Free-tier LLM APIs: Google Gemini (flash models); OpenCode CLI with free hosted models (GLM) as the agent backend.")
bullet("Chromium-based browser (Chrome/Brave) with remote debugging (CDP) for the apply agent; Playwright MCP server (Node.js LTS).")
bullet("Libraries: python-jobspy, Playwright, reportlab/docx2pdf, python-dotenv, PyYAML, requests.")
p("Hardware:")
bullet("Any modern laptop: 4-core CPU, 8 GB RAM, ~1 GB free disk, broadband internet.")

# ---------- 8. Expected Outcomes ----------
heading("8. Expected Outcomes")
bullet("A working end-to-end demo: discovery \u2192 scoring \u2192 validated documents \u2192 autonomous application on a live employer portal.")
bullet("Measured results on the author's own search profile (early deployment already produced 731 discovered postings, 48 scored jobs, 9 validated tailored resumes, and a complete dry-run Workday application).")
bullet("An open-source, AGPL-3.0, reproducible system crediting the upstream ApplyPilot project.")
bullet("A reusable honesty-architecture pattern for personal automation agents.")

# ---------- 9. References ----------
heading("9. References")
refs = [
    "S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, \u201cReAct: Synergizing Reasoning and Acting in Language Models,\u201d in Proc. ICLR, 2023. arXiv:2210.03629.",
    "S. Zhou et al., \u201cWebArena: A Realistic Web Environment for Building Autonomous Agents,\u201d in Proc. ICLR, 2024. arXiv:2307.13854.",
    "L. Boisvert et al., \u201cWorkArena: How Capable are Web Agents at Tackling Commonplace Knowledge Work Tasks?\u201d in Proc. ICML, 2024. arXiv:2403.07718.",
    "L. Wang et al., \u201cA Survey on Large Language Model based Autonomous Agents,\u201d Front. Comput. Sci., vol. 18, no. 6, 2024. arXiv:2308.11432.",
    "feder-cr, \u201cAuto_Jobs_Applier_AIHawk,\u201d GitHub repository, 2024. [Online]. Available: https://github.com/feder-cr/AI_Hawk",
    "Pickle-Pixel, \u201cApplyPilot,\u201d GitHub repository, AGPL-3.0, 2025. [Online]. Available: https://github.com/Pickle-Pixel/ApplyPilot",
    "S. Tomar, \u201ccareerOS,\u201d GitHub repository, AGPL-3.0, 2026. [Online]. Available: https://github.com/shashank-tomar0/careerOS",
    "Google, \u201cGemini API Documentation (Free Tier),\u201d 2025. [Online]. Available: https://ai.google.dev/docs",
    "Microsoft, \u201cPlaywright: Web automation and testing,\u201d 2025. [Online]. Available: https://playwright.dev",
]
for i, r in enumerate(refs, 1):
    p(f"[{i}] {r}", 10, space_after=3, align=J)

doc.save(DIR + "ApplyPilot_Synopsis_v2.docx")
print("SYNOPSIS v2 SAVED")
