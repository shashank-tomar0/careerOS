# -*- coding: utf-8 -*-
"""Generate ApplyPilot Synopsis (per ABESEC Project Synopsis Format 2023-24)."""
import docx
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT

TNR = "Times New Roman"

def base_style(doc):
    st = doc.styles["Normal"]
    st.font.name = TNR
    st.font.size = Pt(12)
    st.paragraph_format.line_spacing = 1.5

def para(doc, text, size=12, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, underline=False):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = TNR; r.font.size = Pt(size); r.bold = bold; r.italic = italic; r.underline = underline
    return p

def heading(doc, text, size=14):
    return para(doc, text, size=size, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=8)

def center(doc, text, size=14, bold=False, italic=False):
    return para(doc, text, size=size, bold=bold, italic=italic, align=WD_ALIGN_PARAGRAPH.CENTER)

def bullet(doc, text, size=12):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text); r.font.name = TNR; r.font.size = Pt(size)
    return p

TITLE = "ApplyPilot: An Autonomous LLM-Agent Pipeline for Job Discovery, Fit Scoring, and Application Automation with Honesty Validation"

doc = Document()
base_style(doc)

center(doc, "ABES ENGINEERING COLLEGE, GHAZIABAD", 16, bold=True)
center(doc, "(Affiliated to Dr. A.P.J. Abdul Kalam Technical University, Lucknow)", 12)
center(doc, "Department of Computer Science & Engineering", 14, bold=True)
center(doc, "SYNOPSIS REPORT", 16, bold=True)
center(doc, "(Session 2025-26)", 12)
doc.add_paragraph()

# ---- Info table (as per format) ----
t = doc.add_table(rows=9, cols=4)
t.style = "Table Grid"
t.alignment = WD_TABLE_ALIGNMENT.CENTER
rows = [
    ("Project Title:", TITLE, "", ""),
    ("Project Type:", "Application / Product (Software)", "", ""),
    ("", "Name", "Roll Number", "Section"),
    ("Group member (1)", "Shashank Tomar", "[ROLL NO.]", "[SECTION]"),
    ("Group member (2)", "[Member Name]", "[Roll No.]", "[Section]"),
    ("Group member (3)", "[Member Name]", "[Roll No.]", "[Section]"),
    ("Project Guide", "[GUIDE NAME]", "Remarks:", ""),
    ("Signature", "", "", ""),
    ("Date of submission", "[DATE]", "", ""),
]
for i, r in enumerate(rows):
    for j, val in enumerate(r):
        cell = t.cell(i, j)
        cell.text = ""
        p = cell.paragraphs[0]
        run = p.add_run(val)
        run.font.name = TNR; run.font.size = Pt(11)
        if i in (0, 2):
            run.bold = True
doc.add_page_break()

# ---- 1. Problem Introduction ----
heading(doc, "1. Problem Introduction")
para(doc, "Manual job hunting is a high-volume, repetitive and mentally exhausting process. "
    "A candidate today must monitor multiple job portals (Indeed, Naukri, LinkedIn, Glassdoor, "
    "ZipRecruiter), read hundreds of postings, judge which roles genuinely match their skills, "
    "customise the resume for every application, and then fill long multi-page application forms "
    "on each employer's career site. For a final-year engineering student applying to dozens of "
    "companies, this activity consumes several hours every day and the repetitive copying of the "
    "same data into forms invites careless mistakes.")
para(doc, "At the same time, modern Large Language Models (LLMs) are capable of reading job "
    "descriptions, understanding a candidate's profile, and acting as autonomous software agents "
    "that can browse websites and complete form-based workflows. This project applies that "
    "capability to build an autonomous, end-to-end job application pipeline - a personal "
    "career operating system (careerOS) - that discovers jobs, enriches them with detail, scores "
    "them for fit against the candidate's real resume, tailors the resume honestly, writes cover "
    "letters, and autonomously completes the employer's own application form in a real browser.")

# ---- 2. Motivation ----
heading(doc, "2. Motivation")
para(doc, "Three observations motivated this project:")
bullet(doc, "Application volume, not lack of skill, is the main bottleneck for fresh graduates: hundreds of postings must be filtered manually before a handful of quality applications are sent.")
bullet(doc, "Existing automation tools either lie (they mass-submit unmodified resumes everywhere) or are closed and expensive (paid SaaS bots). There is a need for a transparent, honest, locally-run system.")
bullet(doc, "LLM agents can now reliably operate real web UIs (fill forms, upload documents, navigate multi-step portals), which was impossible with traditional scraping/automation scripts alone.")
para(doc, "A further motivation was integrity: an autonomous agent must never fabricate experience or apply to roles the candidate cannot legally/practically take (e.g., onsite jobs in another country). The project therefore builds an honesty-validation layer as a core feature, not an afterthought.")

# ---- 3. Project Objective ----
heading(doc, "3. Project Objective")
para(doc, "The expected outcomes after completion of the project are:")
bullet(doc, "A single-command pipeline that discovers jobs from multiple boards (Indeed, Naukri, Glassdoor, LinkedIn, ZipRecruiter) and from employers' own Workday career sites, removing duplicates in a local SQLite database.")
bullet(doc, "An AI fit-scoring stage that rates every job 1-10 against the candidate's verified resume facts, with a fabrication watch-list that rejects resume content not backed by evidence.")
bullet(doc, "Honest resume tailoring: job-specific rewrites that may re-organise or de-emphasise content but may never invent employers, projects, skills, or metrics - enforced by an automated validator.")
bullet(doc, "Automatic cover-letter generation and PDF conversion of tailored documents.")
bullet(doc, "An autonomous browser agent that opens the employer's real application form, creates the candidate account, fills every field from a profile of true facts, uploads the tailored resume, and either submits the application or stops at the Review step (dry-run mode).")
bullet(doc, "Eligibility guarding: the agent verifies location/work-mode rules (India + remote for this candidate) and refuses applications the candidate is not eligible for, instead of blindly submitting.")
bullet(doc, "A reproducible, free-tier-only deployment (local Python pipeline + free LLM APIs), documented for demonstration.")

# ---- 4. Scope of the Project ----
heading(doc, "4. Scope of the Project")
para(doc, "The system is an application/product for individual job seekers, particularly students "
    "and early-career engineers in India seeking remote or domestic roles. Application areas:")
bullet(doc, "Personal job-search automation for B.Tech students and working professionals.")
bullet(doc, "ATS-friendly resume tailoring with provable honesty constraints.")
bullet(doc, "A generalisable demonstration of LLM agents completing real enterprise web workflows (Workday is used by Fortune-500 employers).")
bullet(doc, "A study artefact for the ethics of automated job applications (what should an agent be allowed to say and do on behalf of a person?).")
para(doc, "Out of scope: solving CAPTCHAs illegitimately, bypassing login walls or terms of service of any platform, and guaranteeing interview outcomes. The pipeline respects employer systems - it uses official public job APIs and posted application forms only.")

# ---- 5. Related Previous Work ----
heading(doc, "5. Related Previous Work")
para(doc, "Literature and prior tools in this space were reviewed, including the following:")
para(doc, "(i) Auto_Jobs_Applier_AIHawk (open-source, 2024): an open-source agent that automates LinkedIn Easy-Apply submissions using an LLM to answer screening questions. It demonstrated mass auto-apply feasibility but had no honesty validation and no location-eligibility reasoning; it was later discontinued under platform pressure. ApplyPilot deliberately keeps the honest-apply capability of such tools while removing the mass-spam behaviour.")
para(doc, "(ii) LazyApply (commercial SaaS): a paid desktop bot that submits applications in bulk on LinkedIn/Indeed with a fixed generic resume. Its weakness is exactly the lack of tailoring and verification, which lowers response rates and can misrepresent candidates.")
para(doc, "(iii) Simplify (browser extension): autofills common application fields from a stored profile and tracks applications; it is manual-first (human clicks every submit) and does not perform discovery, scoring or tailoring.")
para(doc, "(iv) Research on web agents: ReAct (Yao et al., 2023) showed that interleaving reasoning and acting lets LLM agents reliably operate interactive environments; WebArena (Zhou et al., 2023) and WorkArena (Boisvert et al., 2024) benchmarked LLM agents on realistic enterprise web tasks, including form-filling on ServiceNow-style portals - the same class of workflow this project automates on Workday. Surveys of LLM-based autonomous agents (Wang et al., 2023) formalise the plan-act-observe loop that our application agent implements.")
para(doc, "No reviewed prior system combines multi-board discovery + honest AI scoring + validated tailoring + a real-browser autonomous apply agent in one free, locally-runnable pipeline, which is the contribution of this project.")

# ---- 6. Software and Hardware Requirements ----
heading(doc, "6. Software and Hardware Requirements")
para(doc, "Software:")
bullet(doc, "Windows 10/11 (64-bit); Python 3.13; SQLite (bundled); Git.")
bullet(doc, "Free-tier LLM APIs: Google Gemini (flash models) via API key; OpenCode CLI with free hosted models (GLM / Gemini) as the agent backend.")
bullet(doc, "Chromium-based browser (Chrome/Brave) with remote-debugging (CDP) for the apply agent; Playwright MCP server (Node.js LTS).")
bullet(doc, "Libraries: python-jobspy (multi-board scraping), Playwright (browser automation), python-docx/reportlab (PDF), docx2pdf, python-dotenv, PyYAML, requests.")
para(doc, "Hardware:")
bullet(doc, "Any modern laptop/PC: 4-core CPU, 8 GB RAM, ~1 GB free disk; internet connection. A headless Linux VPS would also run the discovery stages.")

# ---- 7. Proposed Method ----
heading(doc, "7. Proposed Method (Methodology)")
para(doc, "The system is a staged pipeline; each stage is idempotent, checkpointed in SQLite, and independently runnable from the CLI:")
bullet(doc, "Stage 1 - Discover: scrape multiple boards with python-jobspy (configured for India + remote) and crawl employers' Workday career sites via their public APIs; store unique postings in SQLite.")
bullet(doc, "Stage 2 - Enrich: for each shortlisted job, fetch the full description and employer details (Playwright for JavaScript-rendered pages), so scoring sees complete information.")
bullet(doc, "Stage 3 - Score: an LLM rates each job 1-10 for fit against structured resume facts, using a strict prompt with a fabrication watch-list; scores are parsed to integers and persisted.")
bullet(doc, "Stage 4 - Tailor: for jobs above a threshold, the LLM rewrites the resume for the role; an independent honesty validator compares every claim against the verified resume facts (employers, projects, skills, metrics) and rejects/returns-to-LLM any fabricated content (max 5 attempts). Approved documents are converted to PDF.")
bullet(doc, "Stage 5 - Cover letter + Apply: cover letters are generated with the same validation; then an autonomous agent (OpenCode CLI driving a real Chrome via Playwright/CDP) opens the employer's application form, checks eligibility first (location/work-mode rules from the search config), fills all fields from profile.json (true facts only), uploads the tailored resume PDF, and submits - or, in dry-run mode, stops at the Review step. Every outcome (applied / refused:reason / failed:reason) is logged to the database.")
para(doc, "The agent follows a structured output protocol (RESULT:APPLIED / RESULT:FAILED:<reason>) so the pipeline can record and audit every action. All configuration (profile, search preferences, API keys) is user-owned local files; no data is sent to any third-party service other than the LLM APIs and the employers' own career sites.")

# ---- 8. References ----
heading(doc, "8. References")
refs = [
    "S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, \"ReAct: Synergizing Reasoning and Acting in Language Models,\" in Proc. ICLR, 2023. arXiv:2210.03629.",
    "S. Zhou et al., \"WebArena: A Realistic Web Environment for Building Autonomous Agents,\" in Proc. ICLR, 2024. arXiv:2307.13854.",
    "L. Boisvert et al., \"WorkArena: How Capable are Web Agents at Tackling Commonplace Knowledge Work Tasks?\" in Proc. ICML, 2024. arXiv:2403.07718.",
    "L. Wang, C. Ma, X. Feng, et al., \"A Survey on Large Language Model based Autonomous Agents,\" Front. Comput. Sci., vol. 18, no. 6, 2024. arXiv:2308.11432.",
    "T. Schick et al., \"Toolformer: Language Models Can Teach Themselves to Use Tools,\" in Proc. NeurIPS, 2023. arXiv:2302.04761.",
    "feder-cr, \"Auto_Jobs_Applier_AIHawk,\" GitHub repository, 2024. [Online]. Available: https://github.com/feder-cr/AI_Hawk",
    "Pickle-Pixel, \"ApplyPilot: A local-first autonomous job application pipeline,\" GitHub repository, AGPL-3.0, 2025. [Online]. Available: https://github.com/Pickle-Pixel/ApplyPilot",
    "Free Software Foundation, \"GNU Affero General Public License v3.0,\" 2007. [Online]. Available: https://www.gnu.org/licenses/agpl-3.0.html",
    "Google, \"Gemini API Documentation (Free Tier),\" 2025. [Online]. Available: https://ai.google.dev/docs",
    "Microsoft, \"Playwright: Web automation and testing,\" 2025. [Online]. Available: https://playwright.dev",
]
for i, r in enumerate(refs, 1):
    para(doc, f"[{i}] {r}", size=11, space_after=4)

doc.save("C:/Users/dell/Desktop/mini-project/docs/college/ApplyPilot_Synopsis.docx")
print("SYNOPSIS SAVED")
