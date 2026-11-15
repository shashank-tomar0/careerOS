# -*- coding: utf-8 -*-
"""Generate ApplyPilot Final Mini-Project Report (per ABESEC CSE 5th-sem format)."""
import docx
from docx import Document
from docx.shared import Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT

TNR = "Times New Roman"
J = WD_ALIGN_PARAGRAPH.JUSTIFY
C = WD_ALIGN_PARAGRAPH.CENTER
L = WD_ALIGN_PARAGRAPH.LEFT

def base_style(doc):
    st = doc.styles["Normal"]
    st.font.name = TNR
    st.font.size = Pt(12)
    st.paragraph_format.line_spacing = 1.5

def para(doc, text, size=12, bold=False, italic=False, align=J, space_after=6, underline=False):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = TNR; r.font.size = Pt(size); r.bold = bold; r.italic = italic; r.underline = underline
    return p

def heading(doc, text, size=14, align=L):
    return para(doc, text, size=size, bold=True, align=align, space_after=10)

def chapter(doc, text, size=16):
    return para(doc, text, size=size, bold=True, align=C, space_after=14)

def bullet(doc, text, size=12):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text); r.font.name = TNR; r.font.size = Pt(size)
    return p

def pagebreak(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

TITLE = "ApplyPilot: An Autonomous LLM-Agent Pipeline for Job Discovery, Fit Scoring, and Application Automation with Honesty Validation"

doc = Document()
base_style(doc)

# ============ COVER PAGE ============
for _ in range(3): doc.add_paragraph()
para(doc, "MINI PROJECT REPORT", 20, bold=True, align=C)
para(doc, "on", 14, align=C)
para(doc, TITLE, 18, bold=True, align=C)
doc.add_paragraph()
para(doc, "Submitted for partial fulfillment of the award of", 12, align=C)
para(doc, "BACHELOR OF TECHNOLOGY", 16, bold=True, align=C)
para(doc, "degree", 12, align=C)
para(doc, "In", 12, align=C)
para(doc, "Computer Science & Engineering", 14, bold=True, align=C)
doc.add_paragraph()
para(doc, "By", 12, align=C)
para(doc, "Shashank Tomar ([ROLL NO.])", 12, bold=True, align=C)
para(doc, "[Member Name] ([Roll No.])", 12, align=C)
para(doc, "[Member Name] ([Roll No.])", 12, align=C)
doc.add_paragraph()
para(doc, "Under the Supervision of", 12, align=C)
para(doc, "[GUIDE NAME]", 14, bold=True, align=C)
para(doc, "([Designation])", 12, align=C)
doc.add_paragraph()
para(doc, "ABES ENGINEERING COLLEGE, GHAZIABAD", 16, bold=True, align=C)
para(doc, "(Affiliated to Dr. A.P.J. Abdul Kalam Technical University, Lucknow)", 12, align=C)
pagebreak(doc)

# ============ STUDENT'S DECLARATION ============
heading(doc, "STUDENT'S DECLARATION", 15, C)
doc.add_paragraph()
para(doc, "We hereby declare that the work being presented in this report entitled \u201c" + TITLE + "\u201d is an authentic record of our own work carried out under the supervision of [Dr./Mr./Ms.] [MENTOR NAME]. The matter embodied in this report has not been submitted by us for the award of any other degree.")
doc.add_paragraph()
para(doc, "Dated:", 12, align=L)
para(doc, "\t\t\t\t\t\tSignature of student(s)", 12, align=L)
para(doc, "\t\t\t\t\t\t(Name: Shashank Tomar)", 12, align=L)
para(doc, "\t\t\t\t\t\tDepartment: Computer Science & Engineering", 12, align=L)
pagebreak(doc)

# ============ CERTIFICATE ============
heading(doc, "CERTIFICATE", 15, C)
doc.add_paragraph()
para(doc, "This is to certify that project report entitled \u201c" + TITLE + "\u201d which is submitted by Shashank Tomar in partial fulfillment of the requirement for the award of degree B. Tech. in Department of Computer Science & Engineering of Dr. A.P.J. Abdul Kalam Technical University, formerly Uttar Pradesh Technical University is a record of the candidate's own work carried out by him under my supervision. The matter embodied in this thesis is original and has not been submitted for the award of any other degree.")
doc.add_paragraph()
para(doc, "Signature of Mentor", 12, align=L)
para(doc, "(Name: [GUIDE NAME])", 12, align=L)
para(doc, "(Designation: [DESIGNATION])", 12, align=L)
para(doc, "(Computer Science & Engineering Department)", 12, align=L)
pagebreak(doc)

# ============ ACKNOWLEDGEMENT ============
heading(doc, "ACKNOWLEDGEMENT", 15, C)
doc.add_paragraph()
para(doc, "It gives us a great sense of pleasure to present the report of the B. Tech. Mini Project undertaken during B. Tech. Fifth Semester. We owe special debt of gratitude to [Dr./Mr./Ms.] [MENTOR NAME], Department of Computer Science & Engineering, ABESEC Ghaziabad for constant support and guidance throughout the course of our work.")
para(doc, "We also take the opportunity to acknowledge the contribution of Prof. (Dr.) Pankaj Kumar Sharma, Head, Department of Computer Science & Engineering, ABESEC Ghaziabad for his full support and assistance during the development of the project.")
para(doc, "We also do not like to miss the opportunity to acknowledge the contribution of all faculty members of the department for their kind assistance and cooperation during the development of our project. Last but not the least, we acknowledge our friends for their contribution in the completion of the project.")
doc.add_paragraph()
para(doc, "Signature:\t\t\t\t\tSignature:", 12, align=L)
para(doc, "Name:\t\t\t\t\tName:", 12, align=L)
para(doc, "Roll No.:\t\t\t\t\tRoll No.:", 12, align=L)
para(doc, "Date:\t\t\t\t\tDate:", 12, align=L)
pagebreak(doc)

# ============ ABSTRACT ============
heading(doc, "ABSTRACT", 15, C)
doc.add_paragraph()
para(doc, "Job hunting for entry-level engineering roles is a high-volume, repetitive process: a candidate must monitor several job boards, judge fit, tailor documents, and complete long application forms on each employer's career portal. This project, ApplyPilot (published as the author's careerOS fork), builds an autonomous, honesty-enforcing pipeline that automates the entire flow on a student's own machine using only free-tier resources. The pipeline has six stages: (1) multi-board discovery, which scraped 729 unique postings for an India + remote search profile from Indeed, Naukri, Glassdoor, LinkedIn, ZipRecruiter and employers' Workday career sites; (2) enrichment of shortlisted postings with full descriptions via browser automation; (3) LLM fit-scoring against structured resume facts (a 24-job evaluation produced a discriminating 1\u20139 score spread); (4) resume tailoring guarded by an independent fabrication validator that rejects any invented employer, project, skill or metric; (5) validated cover-letter generation and PDF conversion; and (6) an autonomous browser agent that creates the candidate account, fills the employer's real application form, uploads the tailored resume, and submits it \u2014 or stops at the Review step in dry-run mode. In end-to-end testing, the agent completed a live multi-page Workday application for a 9/10-fit job (form filled, resume uploaded, draft saved through Review), while autonomously refusing two otherwise-attractive jobs after verifying through the employers' own APIs that they were onsite and required relocation. The system is released under the AGPL-3.0 licence as a fork crediting the upstream ApplyPilot project, and its honesty layer \u2014 which makes the agent refuse to fabricate or to apply where the candidate is ineligible \u2014 is presented as a reproducible pattern for trustworthy personal-automation agents.", italic=True)
pagebreak(doc)

# ============ TABLE OF CONTENTS ============
heading(doc, "TABLE OF CONTENTS", 15, C)
toc = [
    ("CHAPTER 1: INTRODUCTION", "1"),
    ("1.1 Problem Introduction", "1"), ("1.2 Motivation", "1"), ("1.3 Project Objective", "2"),
    ("1.4 Scope of the Project", "2"), ("1.5 Related Previous Work", "3"), ("1.6 Organisation of the Report", "3"),
    ("CHAPTER 2: LITERATURE SURVEY", "4"),
    ("2.1 Mass-Application Tools", "4"), ("2.2 Research on LLM Web Agents", "4"), ("2.3 Research Gap", "5"),
    ("CHAPTER 3: SYSTEM ANALYSIS AND REQUIREMENTS", "6"),
    ("3.1 Feasibility Study", "6"), ("3.2 Software Requirements", "6"), ("3.3 Hardware Requirements", "7"),
    ("CHAPTER 4: PROPOSED METHODOLOGY AND SYSTEM DESIGN", "8"),
    ("4.1 Pipeline Architecture", "8"), ("4.2 Stage Design", "9"), ("4.3 The Honesty Validator", "10"), ("4.4 The Autonomous Apply Agent", "11"),
    ("CHAPTER 5: IMPLEMENTATION", "12"),
    ("5.1 Technology Stack", "12"), ("5.2 Key Implementation Decisions", "12"), ("5.3 Database Schema", "13"),
    ("CHAPTER 6: TESTING AND RESULTS", "14"),
    ("6.1 Pipeline Results", "14"), ("6.2 End-to-End Application Test", "15"), ("6.3 Honesty and Eligibility Tests", "15"),
    ("CHAPTER 7: CONCLUSION AND FUTURE WORK", "16"),
    ("REFERENCES", "17"),
]
for t_, p_ in toc:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(t_); r.font.name = TNR; r.font.size = Pt(12)
pagebreak(doc)

# ============ LIST OF TABLES / FIGURES ============
heading(doc, "LIST OF TABLES", 14)
for t_, d_ in [("Table 6.1", "Pipeline stage output statistics (measured run)"),
               ("Table 6.2", "Apply-stage outcomes on live jobs"),
               ("Table 3.1", "Software requirements")]:
    para(doc, f"{t_}\t{d_}", 12, align=L)
heading(doc, "LIST OF FIGURES", 14)
for f_, d_ in [("Fig 4.1", "ApplyPilot pipeline architecture (six stages around a SQLite checkpoint store)"),
               ("Fig 4.2", "Autonomous apply-agent workflow (eligibility gate \u2192 form \u2192 review gate)"),
               ("Fig 6.1", "Score distribution of the evaluated job pool")]:
    para(doc, f"{f_}\t{d_}", 12, align=L)
pagebreak(doc)

# ============ CHAPTER 1 ============
chapter(doc, "CHAPTER 1", 15)
chapter(doc, "INTRODUCTION", 16)
heading(doc, "1.1 Problem Introduction")
para(doc, "A final-year engineering student applying for internships and placements faces a process that is heavily weighted towards volume: recruiters on job boards receive hundreds of applications per posting, and students respond by sending more applications \u2014 each of which must be discovered, read, judged, customised and manually entered into the employer's career portal. A single application to a large employer (e.g., via Workday) involves creating an account, navigating 4\u20136 form pages, entering education/employment data, uploading documents and answering screening questions. Repeating this for dozens of companies consumes weeks of productive time and produces transcription errors that can silently disqualify a candidate.")
para(doc, "Large Language Models (LLMs) have recently become capable of exactly this class of work: reading unstructured text, judging semantic fit, rewriting documents under constraints, and \u2014 as agents \u2014 operating real web interfaces through a browser. This project asks: can a free-tier, locally-run LLM agent honestly and safely automate the entire application lifecycle for a real student?")
heading(doc, "1.2 Motivation")
para(doc, "The project is motivated by three observations. First, the bottleneck for fresh graduates is application volume and form-filling time, not lack of relevant skills. Second, the existing automation tools fall into two unacceptable categories: mass-submitters that send a single generic resume everywhere (misrepresenting the candidate), and closed paid bots with opaque behaviour. Third, autonomous LLM agents now demonstrably operate enterprise web UIs (WorkArena, WebArena benchmarks), making a genuinely end-to-end system feasible. A further, distinctive motivation is integrity: the agent must never fabricate experience and must refuse jobs the candidate cannot actually take. The project treats honesty as a first-class subsystem, verified by an automated validator and demonstrated by observed refusals.")
heading(doc, "1.3 Project Objective")
para(doc, "The objective is to design, implement and empirically demonstrate a single-command, staged pipeline that: (a) discovers jobs from five boards plus employer Workday sites with de-duplication in a local SQLite database; (b) enriches and scores each job for fit on a 1\u201310 scale against verified resume facts; (c) produces tailored resumes and cover letters whose every factual claim is machine-validated against the candidate's real history; (d) autonomously completes the employer's real application form in a browser, uploading the tailored resume, with a dry-run mode that stops before submission; and (e) enforces location/work-mode eligibility rules so that ineligible jobs are refused, not applied to. The complete system must run on free-tier APIs and be reproducible from a public repository.")
heading(doc, "1.4 Scope of the Project")
para(doc, "The system targets individual job seekers \u2014 particularly Indian students and early-career engineers \u2014 with a configurable search profile (locations, remote preference, salary floor). It is an application/product artefact with three broader uses: a study of honest LLM-agent behaviour under real-world incentives, a reference implementation of agent-performed enterprise form workflows, and a free replacement for paid auto-apply SaaS. Explicitly out of scope: CAPTCHA circumvention, login-wall bypass, platform terms-of-service violations, and any guarantee of interview outcomes. The pipeline uses only public APIs and forms that the employer publishes for candidates.")
heading(doc, "1.5 Related Previous Work")
para(doc, "Prior work spans open-source auto-apply agents, commercial bots, and academic agent benchmarks. Auto_Jobs_Applier_AIHawk (2024) automated LinkedIn Easy-Apply with LLM-answered screening questions but lacked honesty validation and eligibility reasoning. LazyApply (commercial) bulk-submits a fixed resume. Simplify (extension) autofills application fields from a stored profile but leaves every click to the human. On the research side, ReAct established the reason-act loop for LLM agents; Toolformer showed models can learn tool use; WebArena and WorkArena benchmark agents on realistic enterprise portals including multi-page form tasks; Wang et al. survey the agent architecture (planning, memory, tools). Section 2 elaborates. None of the reviewed systems integrates discovery, honest scoring, validated tailoring, and a real-browser apply agent into one free, auditable pipeline \u2014 the gap this project fills.")
heading(doc, "1.6 Organisation of the Report")
para(doc, "Chapter 2 surveys related tools and research. Chapter 3 analyses feasibility and requirements. Chapter 4 presents the pipeline architecture, the honesty validator, and the apply-agent design. Chapter 5 describes implementation details and key decisions. Chapter 6 reports measured results from a live run, including the end-to-end Workday application and observed agent refusals. Chapter 7 concludes and outlines future work; references follow IEEE style.")
pagebreak(doc)

# ============ CHAPTER 2 ============
chapter(doc, "CHAPTER 2", 15)
chapter(doc, "LITERATURE SURVEY", 16)
para(doc, "This chapter reviews the tools and research that define the state of the art in automated job application and LLM web agents, and identifies the gap ApplyPilot addresses.")
heading(doc, "2.1 Mass-Application Tools")
para(doc, "Auto_Jobs_Applier_AIHawk [6] is the best-known open-source auto-apply agent. It logs into LinkedIn, searches postings, and uses an LLM to answer employer screening questions and (optionally) tailor the resume, then submits via Easy-Apply. Its strengths \u2014 free, end-to-end, popular (tens of thousands of GitHub stars) \u2014 were offset by serious weaknesses: no verification that LLM answers were truthful, no location/work-mode eligibility logic, and reliance on a single platform, which led to its discontinuation after platform policy enforcement. LazyApply [commercial] is a paid desktop bot applying in bulk on multiple boards with a generic resume; its model of \u201cquantity over quality\u201d is precisely what this project avoids. Simplify [extension] stores the user profile and autofills forms, with a job tracker, but is human-driven. Sonara and similar AI job-matching startups offered LLM-based matching-as-a-service (several have shut down), demonstrating both demand and the fragility of closed centralised services.")
para(doc, "The upstream ApplyPilot project [7] provided the staged-pipeline skeleton (discover \u2192 enrich \u2192 score \u2192 tailor \u2192 apply) with an honesty validator and Workday-first apply strategy under the AGPL-3.0 licence. This project's careerOS fork [8] extends it for Indian free-tier use: a new agent backend (OpenCode with free hosted models), India-aware location-eligibility rules in the apply prompt, per-stage demo limits, a string-URL corruption fix in the discovery writer, validator fixes for legitimately-profiled skills, and a Chromium/CDP integration on Windows. All derived code remains AGPL-3.0 with credit to upstream, per the licence.")
heading(doc, "2.2 Research on LLM Web Agents")
para(doc, "ReAct [1] demonstrated that interleaving chain-of-thought reasoning with tool actions makes LLM agents substantially more reliable on interactive tasks, and is the basis of this project's apply-agent loop. Toolformer [5] showed LLMs can self-teach API/tool use, motivating tool-mediated (rather than screen-scraping) integration. WebArena [2] provides self-hostable realistic web environments (including multi-page form filling on an e-commerce and forum stack) and found agents succeed on only a minority of realistic tasks \u2014 highlighting that real form workflows remain hard and need guardrails. WorkArena [3] benchmarked agents on ServiceNow-style enterprise tasks (the same UI family as Workday); its findings that form navigation is among the harder capabilities directly informed this project's decision to drive the employer's UI step-by-step with an availability-first fallback to raw Chrome DevTools Protocol actions. Wang et al.'s survey [4] formalises the plan\u2013act\u2013observe architecture with memory and tools that this project instantiates in a lightweight form (SQLite as episodic memory, prompt as policy, Playwright/CDP as actuators).")
heading(doc, "2.3 Research Gap")
para(doc, "Synthesising the survey: (i) existing auto-apply tools optimise submission count, not truthfulness or eligibility; (ii) academic benchmarks demonstrate capability but no deployed personal system uses them with honesty enforcement; (iii) no free, open, locally-runnable system covers the full lifecycle (discovery \u2192 scoring \u2192 tailoring \u2192 submission) on multiple boards plus employer-native portals. ApplyPilot/careerOS fills this gap and, uniquely, treats fabrication prevention and eligibility refusal as testable, demonstrated features (Chapter 6).")
pagebreak(doc)

# ============ CHAPTER 3 ============
chapter(doc, "CHAPTER 3", 15)
chapter(doc, "SYSTEM ANALYSIS AND REQUIREMENTS", 16)
heading(doc, "3.1 Feasibility Study")
para(doc, "Technical feasibility: all stages are ordinary Python processes plus a browser; the only external dependencies are free-tier LLM APIs and the employers' own public career endpoints. Economic feasibility: total recurring cost is zero on free tiers (Gemini flash models + OpenCode free models); the alternative SaaS products cost US$30\u2013240/year. Operational feasibility: the system runs on the student's own laptop; configuration is three local files (.env, profile.json, searches.yaml). Ethical/legal feasibility: the tool applies only through employers' own posted forms, submits only truthful data, and is licensed AGPL-3.0 with upstream attribution; it deliberately refuses to bypass logins or anti-bot systems.")
heading(doc, "3.2 Software Requirements")
heading(doc, "3.3 Hardware Requirements")
para(doc, "Any modern laptop: quad-core CPU, 8 GB RAM, 1 GB free disk, broadband internet. (Development and testing used a Windows 11 laptop with a Chromium-based browser.)")
pagebreak(doc)

# ============ CHAPTER 4 ============
chapter(doc, "CHAPTER 4", 15)
chapter(doc, "PROPOSED METHODOLOGY AND SYSTEM DESIGN", 16)
heading(doc, "4.1 Pipeline Architecture")
para(doc, "ApplyPilot is organised as six idempotent stages around a single SQLite checkpoint store (applypilot.db). Every stage can be run independently from the CLI (applypilot run <stage>), is resumable after interruption, and carries optional --limit flags for demonstrations. The architecture is:")
para(doc, "discover \u2192 enrich \u2192 score \u2192 tailor \u2192 cover \u2192 pdf  \u2026\u2192 apply (agent)", 12, bold=True, align=C)
para(doc, "Fig 4.1 \u2014 The six batch stages write to shared tables (jobs, resumes, cover_letters, apply_attempts); the apply agent is a separate, interactive stage launched per job. Configuration lives in three user-owned files: .env (API keys), profile.json (verified candidate facts, salary floor, address), searches.yaml (locations, remote preference, board list, salary expectations).")
heading(doc, "4.2 Stage Design")
para(doc, "Stage 1 \u2014 Discover: python-jobspy scrapes Indeed, Naukri, Glassdoor, LinkedIn and ZipRecruiter for configured queries (India + remote); an additional Workday crawler walks employers' public career-site APIs (e.g., cisco.wd5.myworkdayjobs.com) for direct application URLs. Postings are de-duplicated by a company+title+URL signature and stored with full raw description.")
para(doc, "Stage 2 \u2014 Enrich: for shortlisted jobs, the full description and posting metadata are fetched (Playwright renders JavaScript-heavy pages); enrichment marks each job eligible for scoring.")
para(doc, "Stage 3 \u2014 Score: an LLM rates each job 1\u201310 for fit against structured resume facts, using a strict rubric (skills overlap, seniority, location/remote compliance, salary floor). Model output is parsed defensively (markdown stripping, integer extraction) and persisted. Low scores (below threshold) are never tailored, saving API quota.")
para(doc, "Stage 4 \u2014 Tailor: for high-fit jobs the LLM rewrites the resume emphasising relevant projects/skills. Crucially, every generated document is passed to an independent honesty validator (Section 4.3) before acceptance; rejected documents return to the LLM with specific objections (max 5 attempts), after which the job is flagged. Approved documents are converted to PDF (docx2pdf/reportlab).")
para(doc, "Stage 5 \u2014 Cover: cover letters are generated under the same validation regime.")
para(doc, "Stage 6 \u2014 Apply: per job (Section 4.4).")
heading(doc, "4.3 The Honesty Validator")
para(doc, "The validator is the project's integrity core. It maintains a watch-list of fabrication-prone patterns (invented employers, invented metrics, invented projects) derived from the candidate's verified resume facts. For each tailored document it: extracts claims; compares employers, projects, skills and metrics against profile.json; allows re-organisation and de-emphasis but rejects addition of anything not evidenced; and enforces the profile's skills boundary (skills the candidate has listed may be discussed, unknown skills may not be claimed). A skill-normalisation guard prevents false positives (e.g., the candidate's listed C++ must not be flagged). Validation failures are returned to the LLM as structured objections, making the loop a generator\u2013critic pair. This design directly answers the central ethics question of auto-apply systems: what may an agent say on a person's behalf? \u2014 Answer: only what the person could truthfully say.")
heading(doc, "4.4 The Autonomous Apply Agent")
para(doc, "The apply stage launches an LLM agent (OpenCode CLI running a free hosted model such as GLM or Gemini flash) with: a strict policy prompt (true facts only from profile.json; no invented answers; eligibility rules first; structured RESULT protocol), a browser toolset (Playwright MCP server driving the candidate's own Chromium-based browser over the Chrome DevTools Protocol on a debug port, with a raw-CDP fallback for steps the MCP tools cannot express), and the job's tailored documents. The agent workflow (Fig 4.2) is: (1) LOCATION/ELIGIBILITY CHECK first \u2014 read the posting; if onsite-only outside the candidate's country or otherwise ineligible, output RESULT:FAILED:not_eligible_location and stop; (2) open the application form; (3) create the candidate account if required; (4) fill every field from profile.json, answering screening questions truthfully (e.g., relocation \u201cNone\u201d must be reported as None, never guessed); (5) upload the tailored resume PDF; (6) reach the Review page; (7a) in submit mode, click Submit and verify; (7b) in dry-run mode, stop and save the draft without clicking Submit; (8) output RESULT:APPLIED or RESULT:FAILED:<reason> for the pipeline to record. Salary questions are answered per the profile's floor and the posting's own range (midpoint strategy), never invented.")
pagebreak(doc)

# ============ CHAPTER 5 ============
chapter(doc, "CHAPTER 5", 15)
chapter(doc, "IMPLEMENTATION", 16)
heading(doc, "5.1 Technology Stack")
para(doc, "The pipeline is ~9,600 lines of Python 3.13 (asyncio-based stage runners) with: python-jobspy (board scraping), Playwright + a Playwright MCP server under Node.js LTS (browser automation), SQLite via the standard library (checkpoint store), reportlab/docx2pdf (PDF), PyYAML and python-dotenv (configuration), and the OpenCode CLI as the agent runtime (free GLM/Gemini models via OpenAI-compatible endpoints). The fork is developed in Git and published at github.com/shashank-tomar0/careerOS.")
heading(doc, "5.2 Key Implementation Decisions")
para(doc, "(a) Editable install + CLI packaging so every stage is one command on the student's terminal. (b) Agent backend abstraction: the launcher supports both Claude Code and OpenCode; OpenCode was chosen for zero cost, driven through its headless 'run' mode with the MCP config written per worker. (c) Browser profile persistence: the worker's browser profile directory is reused across jobs, so a manual login (e.g., on a board that requires one) persists for later automated runs. (d) System-browser over bundled Chromium: the agent drives the user's installed Chromium-family browser via CDP, avoiding a large download and enabling human observation. (e) Defensive LLM parsing: scores and agent results are parsed with markdown-stripping and regex extraction so free-tier model verbosity cannot corrupt the database. (f) Rate-limit resilience: stage-level retries with backoff; the agent default model was chosen for tool-calling reliability under free-tier quotas. (g) Structured agent output protocol (RESULT:*) so every run terminates with a machine-readable verdict recorded in apply_attempts.")
heading(doc, "5.3 Database Schema")
para(doc, "Core tables: jobs (id, site, title, company, location, description, url, fit_score, tailored_resume_path, apply_status, apply_error, apply_attempts), resumes and cover_letters (job linkage, approval status, validator report), apply_attempts (per-run status, reason, transcript reference), and a search/config snapshot. The database doubles as the demo dashboard source (applypilot status / applypilot dashboard).")
pagebreak(doc)

# ============ CHAPTER 6 ============
chapter(doc, "CHAPTER 6", 15)
chapter(doc, "TESTING AND RESULTS", 16)
heading(doc, "6.1 Pipeline Results")
para(doc, "A live run on the author's own resume (B.Tech CSE student, India, remote-preferring) produced the following measured results. Discovery collected 729 unique postings (multi-board + Workday). Enrichment and a 24-job scoring evaluation yielded a discriminating distribution from 1 to 9 (median ~5), with two 9/10-fit postings identified as Cisco Software Engineer (Bangalore) with direct Workday application URLs. Six tailored resumes and five cover letters were produced, all passing the honesty validator, and converted to PDF.")
para(doc, "Table 6.1 \u2014 Measured stage outputs", 12, bold=True, align=C)
tt = doc.add_table(rows=9, cols=3); tt.style = "Table Grid"
data = [("Stage", "Output", "Measured"),
        ("Discover", "unique postings stored", "729"),
        ("Enrich", "shortlisted jobs enriched", "per-config"),
        ("Score", "jobs scored in evaluation", "24 (spread 1\u20139)"),
        ("Tailor", "approved tailored resumes", "7 (+ PDFs)"),
        ("Cover", "approved cover letters", "5 (+ PDFs)"),
        ("Apply", "dry-run completions", "1 full Workday flow"),
        ("Apply", "honest refusals", "2 (ineligible jobs)"),
        ("Apply", "login-walled failures (Indeed)", "observed & documented")]
for i, r in enumerate(data):
    for j, v in enumerate(r):
        c = tt.cell(i, j); c.text = ""
        run = c.paragraphs[0].add_run(v); run.font.name = TNR; run.font.size = Pt(11)
        if i == 0: run.bold = True
heading(doc, "6.2 End-to-End Application Test")
para(doc, "The culminating test ran the apply agent in dry-run mode against the 9/10-fit Cisco Software Engineer posting on Cisco's live Workday careers site. The agent autonomously: verified eligibility (Bangalore onsite \u2014 acceptable for an India-based candidate per the configured rules), opened the application, created the candidate account, navigated every form page (handling dropdown/listbox widgets), uploaded the tailored resume PDF (system-confirmed upload), completed the screening questions truthfully, and reached the Review page, where it stopped and reported RESULT:APPLIED (dry-run) with a complete audit trail in the worker log. The saved draft means a real submission is one click away \u2014 the human decides.")
heading(doc, "6.3 Honesty and Eligibility Tests")
para(doc, "Negative tests were as informative as the positive one. (1) Location refusal: the agent refused a Moderna posting (onsite, Massachusetts) after querying the employer's API for the work arrangement \u2014 RESULT:FAILED:not_eligible_location. (2) Relocation refusal: the agent refused a Motorola posting in another Indian city after the Workday screening revealed relocation was required and the profile says relocation \u201cNone\u201d \u2014 it reported the truthful answer rather than guessing. (3) Fabrication guard: validator correctly rejected drafts that cited metrics/projects absent from the resume, and correctly allowed the candidate's genuinely-listed skills (C++, Rust) after the skills-boundary fix. (4) Salary sanity: prompt tests caught a currency-format error (a $-formatted INR floor) which was fixed to currency-neutral formatting. (5) Failure-mode documentation: Indeed-hosted postings that require a session login terminate with a structured sso_required verdict \u2014 the system fails safely and auditable rather than attempting to bypass the wall. Together these demonstrate that the pipeline not only completes applications but demonstrably declines to do the wrong thing.")
pagebreak(doc)

# ============ CHAPTER 7 ============
chapter(doc, "CHAPTER 7", 15)
chapter(doc, "CONCLUSION AND FUTURE WORK", 16)
heading(doc, "7.1 Conclusion")
para(doc, "This project set out to answer whether a free-tier, locally-run LLM system could automate a student's entire job-application lifecycle \u2014 and do so honestly. The answer demonstrated on live systems is yes: 729 jobs discovered, AI fit-scoring with a discriminating 1\u20139 distribution, validator-approved tailored resumes and cover letters, and a fully autonomous, end-to-end completion of a real Fortune-500 Workday application (form filled, resume uploaded, draft saved at Review) with two observed refusals of ineligible jobs. The contribution is both practical (a working, free careerOS for the author) and methodological: an integrity architecture \u2014 verified-facts profile, generator\u2013critic honesty validation, eligibility gating, and a structured audit protocol \u2014 that makes personal job-application automation defensible. The work is released as an AGPL-3.0 fork crediting the upstream ApplyPilot project, consistent with the ethics of open, auditable personal automation.")
heading(doc, "7.2 Future Work")
bullet(doc, "Session persistence for login-walled boards (e.g., Indeed) so the human logs in once and the agent handles the rest of the flow.")
bullet(doc, "Interview-prep stage: generate role-specific question banks from each job description and the tailored resume.")
bullet(doc, "Response/outcome tracking: correlate applications with replies to learn which tailoring strategies work.")
bullet(doc, "Multi-profile support and a scheduling layer for daily unattended runs.")
bullet(doc, "Deeper agent reliability: native form-semantic tools (field-type aware) to reduce raw-CDP fallbacks, guided by WorkArena-style task decomposition.")
bullet(doc, "A published research evaluation of the honesty validator against adversarial tailoring attempts.")
pagebreak(doc)

# ============ REFERENCES (IEEE) ============
chapter(doc, "REFERENCES", 15)
refs = [
    "S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, \u201cReAct: Synergizing Reasoning and Acting in Language Models,\u201d in Proc. Int. Conf. on Learning Representations (ICLR), 2023. arXiv:2210.03629.",
    "S. Zhou et al., \u201cWebArena: A Realistic Web Environment for Building Autonomous Agents,\u201d in Proc. ICLR, 2024. arXiv:2307.13854.",
    "L. Boisvert et al., \u201cWorkArena: How Capable are Web Agents at Tackling Commonplace Knowledge Work Tasks?\u201d in Proc. Int. Conf. on Machine Learning (ICML), 2024. arXiv:2403.07718.",
    "L. Wang, C. Ma, X. Feng, et al., \u201cA Survey on Large Language Model based Autonomous Agents,\u201d Frontiers of Computer Science, vol. 18, no. 6, 2024. arXiv:2308.11432.",
    "T. Schick et al., \u201cToolformer: Language Models Can Teach Themselves to Use Tools,\u201d in Proc. NeurIPS, 2023. arXiv:2302.04761.",
    "feder-cr, \u201cAuto_Jobs_Applier_AIHawk,\u201d GitHub repository, 2024. [Online]. Available: https://github.com/feder-cr/AI_Hawk",
    "Pickle-Pixel, \u201cApplyPilot: A local-first autonomous job application pipeline,\u201d GitHub repository, AGPL-3.0, 2025. [Online]. Available: https://github.com/Pickle-Pixel/ApplyPilot",
    "S. Tomar, \u201ccareerOS: ApplyPilot fork for India-focused, free-tier autonomous applications,\u201d GitHub repository, AGPL-3.0, 2026. [Online]. Available: https://github.com/shashank-tomar0/careerOS",
    "Free Software Foundation, \u201cGNU Affero General Public License v3.0,\u201d Nov. 2007. [Online]. Available: https://www.gnu.org/licenses/agpl-3.0.html",
    "Google, \u201cGemini API Documentation (Free Tier),\u201d 2025. [Online]. Available: https://ai.google.dev/docs",
    "Microsoft, \u201cPlaywright: Web Automation and Testing,\u201d 2025. [Online]. Available: https://playwright.dev",
    "Slatec LLC, \u201cpython-jobspy: Multi-board job scraper library,\u201d 2025. [Online]. Available: https://github.com/cullenwatson/JobSpy",
]
for i, r in enumerate(refs, 1):
    para(doc, f"[{i}] {r}", 11, space_after=4, align=L)
pagebreak(doc)

# ============ ANNEXURES ============
chapter(doc, "ANNEXURE A \u2014 DEMONSTRATION COMMANDS", 14)
para(doc, "The complete system is demonstrated with the following commands (run from the project root; editable install):", 12)
cmds = [
    "applypilot doctor",
    "applypilot run discover --limit 2",
    "applypilot run enrich --limit 2 --workers 2",
    "applypilot run score --limit 4",
    "applypilot run tailor --validation lenient --limit 2",
    "applypilot run cover --validation lenient --limit 2",
    "applypilot run pdf --limit 2",
    "applypilot status",
    "applypilot dashboard",
    "applypilot apply --dry-run --limit 1",
    "applypilot apply --limit 1   (real submission)",
]
for c_ in cmds:
    para(doc, "> " + c_, 11, align=L, space_after=3)
chapter(doc, "ANNEXURE B \u2014 SAMPLE AGENT VERDICTS (WORKER LOG EXCERPTS)", 14)
para(doc, "Dry-run completion: \u201cRESULT:APPLIED (dry-run \u2014 application fully filled and saved as a draft through the Review step; final Submit intentionally not clicked per instructions. To finish, the candidate only needs to open the Workday application and click Submit.)\u201d", 12)
para(doc, "Eligibility refusal: \u201cRESULT:FAILED:not_eligible_location \u2014 job verified onsite in Massachusetts, USA with no remote option; candidate profile relocation: None.\u201d", 12)
para(doc, "Resume upload (system event): \u201cSuccessfully Uploaded!\u201d", 12)

doc.save("C:/Users/dell/Desktop/mini-project/docs/college/ApplyPilot_Final_Report.docx")
print("REPORT SAVED")
