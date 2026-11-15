# -*- coding: utf-8 -*-
"""APPLYPILOT MINI PROJECT REPORT v2 — traditional chapter-wise project report.
College front matter + 7 chapters + references + annexures. 20+ pages. 7 figures."""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT

TNR = "Times New Roman"
J = WD_ALIGN_PARAGRAPH.JUSTIFY; C = WD_ALIGN_PARAGRAPH.CENTER; L = WD_ALIGN_PARAGRAPH.LEFT
DIR = "C:/Users/dell/Desktop/mini-project/docs/college/"
TITLE = "ApplyPilot: An Honesty-Enforcing LLM-Agent Pipeline for End-to-End Job Application Automation on Free-Tier Resources"

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.9); sec.bottom_margin = Inches(0.9)
sec.left_margin = Inches(1.0); sec.right_margin = Inches(1.0)
st = doc.styles["Normal"]; st.font.name = TNR; st.font.size = Pt(12)
st.paragraph_format.line_spacing = 1.5

def p(text, size=12, bold=False, italic=False, align=J, space_after=6, first_indent=0, line=1.5):
    par = doc.add_paragraph(); par.alignment = align
    par.paragraph_format.space_after = Pt(space_after); par.paragraph_format.line_spacing = line
    if first_indent: par.paragraph_format.first_line_indent = Inches(first_indent)
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    return par

def heading(text, size=14, align=L):
    return p(text, size=size, bold=True, align=align, space_after=10)

def chapter(num, title):
    p(f"CHAPTER {num}", 15, bold=True, align=C, space_after=2)
    p(title.upper(), 16, bold=True, align=C, space_after=14)

def pagebreak():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

def set_cell(cell, text, size=10, bold=False, align=None):
    cell.text = ""; par = cell.paragraphs[0]
    if align: par.alignment = align
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold

def figure(fname, width, cap):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_after = Pt(2)
    par.add_run().add_picture(DIR + fname, width=Inches(width))
    p(cap, 11, italic=False, align=C, space_after=10)

def table(caption, rows, cols_list=None, sizes=10):
    p(caption, 11, bold=True, align=C, space_after=4)
    t = doc.add_table(rows=len(rows), cols=len(rows[0])); t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            set_cell(t.cell(i, j), v, bold=(i == 0), size=sizes)
    p("", 6, space_after=2)
    return t

def bl(text, size=12):
    par = doc.add_paragraph(style="List Bullet")
    par.paragraph_format.line_spacing = 1.5
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size)
    return par

# ================= COVER PAGE =================
for _ in range(3): doc.add_paragraph()
p("MINI PROJECT REPORT", 20, bold=True, align=C, line=1.0)
p("on", 14, align=C, line=1.0)
p(TITLE, 17, bold=True, align=C, line=1.15)
doc.add_paragraph()
p("Submitted for partial fulfillment of the award of", 12, align=C, line=1.0)
p("BACHELOR OF TECHNOLOGY", 16, bold=True, align=C, line=1.0)
p("degree", 12, align=C, line=1.0); p("In", 12, align=C, line=1.0)
p("Computer Science & Engineering", 14, bold=True, align=C, line=1.0)
doc.add_paragraph(); p("By", 12, align=C, line=1.0)
p("Shashank Tomar ([ROLL NO.])", 12, bold=True, align=C, line=1.0)
p("[Member Name] ([Roll No.])", 12, align=C, line=1.0)
p("[Member Name] ([Roll No.])", 12, align=C, line=1.0)
doc.add_paragraph()
p("Under the Supervision of", 12, align=C, line=1.0)
p("[GUIDE NAME]", 14, bold=True, align=C, line=1.0)
p("([Designation])", 12, align=C, line=1.0)
doc.add_paragraph()
p("ABES ENGINEERING COLLEGE, GHAZIABAD", 16, bold=True, align=C, line=1.0)
p("(Affiliated to Dr. A.P.J. Abdul Kalam Technical University, Lucknow)", 12, align=C, line=1.0)
p("(Session 2025-26)", 12, align=C, line=1.0)
pagebreak()

# ================= DECLARATION =================
heading("STUDENT'S DECLARATION", 15, C); doc.add_paragraph()
p("We hereby declare that the work being presented in this report entitled \u201c" + TITLE + "\u201d is an authentic record of our own work carried out under the supervision of [Dr./Mr./Ms.] [MENTOR NAME]. The matter embodied in this report has not been submitted by us for the award of any other degree.")
doc.add_paragraph()
p("Dated:", 12, align=L)
p("\t\t\t\t\t\tSignature of student(s)", 12, align=L)
p("\t\t\t\t\t\t(Name: Shashank Tomar)", 12, align=L)
p("\t\t\t\t\t\tDepartment: Computer Science & Engineering", 12, align=L)
pagebreak()

# ================= CERTIFICATE =================
heading("CERTIFICATE", 15, C); doc.add_paragraph()
p("This is to certify that project report entitled \u201c" + TITLE + "\u201d which is submitted by Shashank Tomar in partial fulfillment of the requirement for the award of degree B. Tech. in Department of Computer Science & Engineering of Dr. A.P.J. Abdul Kalam Technical University, formerly Uttar Pradesh Technical University is a record of the candidate's own work carried out by him under my supervision. The matter embodied in this thesis is original and has not been submitted for the award of any other degree.")
doc.add_paragraph()
p("Signature of Mentor", 12, align=L)
p("(Name: [GUIDE NAME])", 12, align=L)
p("(Designation: [DESIGNATION])", 12, align=L)
p("(Computer Science & Engineering Department)", 12, align=L)
pagebreak()

# ================= ACKNOWLEDGEMENT =================
heading("ACKNOWLEDGEMENT", 15, C); doc.add_paragraph()
p("It gives us a great sense of pleasure to present the report of the B. Tech. Mini Project undertaken during B. Tech. Fifth Semester. We owe special debt of gratitude to [Dr./Mr./Ms.] [MENTOR NAME], Department of Computer Science & Engineering, ABESEC Ghaziabad for constant support and guidance throughout the course of our work.")
p("We also take the opportunity to acknowledge the contribution of Prof. (Dr.) Pankaj Kumar Sharma, Head, Department of Computer Science & Engineering, ABESEC Ghaziabad for his full support and assistance during the development of the project.")
p("We also do not like to miss the opportunity to acknowledge the contribution of all faculty members of the department for their kind assistance and cooperation during the development of our project. Last but not the least, we acknowledge our friends for their contribution in the completion of the project.")
doc.add_paragraph()
p("Signature:\t\t\t\t\tSignature:", 12, align=L)
p("Name:\t\t\t\t\tName:", 12, align=L)
p("Roll No.:\t\t\t\t\tRoll No.:", 12, align=L)
p("Date:\t\t\t\t\tDate:", 12, align=L)
pagebreak()

# ================= ABSTRACT =================
heading("ABSTRACT", 15, C); doc.add_paragraph()
p("Job hunting for entry-level engineering roles is a high-volume, repetitive process: a candidate must monitor several job boards, judge fit, tailor documents, and complete long application forms on each employer's career portal. This report presents ApplyPilot (published by the author as the careerOS fork), a free-tier, locally-run pipeline that couples large language model (LLM) agents with an honesty-enforcement architecture to automate the full application lifecycle: multi-board discovery, enrichment, AI fit-scoring, honest resume tailoring, cover-letter generation, and autonomous submission through the employer's own career portal. The system introduces a generator-critic honesty validator that machine-verifies every generated document against the candidate's verified resume facts, an eligibility gate that refuses jobs the candidate cannot take, and a structured verdict protocol that makes every agent action auditable. On a live deployment targeting an India+remote search profile, the pipeline discovered 731 unique postings from eight sources, scored 48 jobs (a discriminating 1\u20139 distribution with 18.8% at fit \u22657), produced nine validator-approved tailored resumes and five cover letters, and completed an end-to-end autonomous application on a live Workday portal \u2014 creating the candidate account, navigating all form pages, uploading the tailored resume, and stopping at the Review step in dry-run mode \u2014 while autonomously refusing two ineligible postings after verifying eligibility against the employers' own APIs. The report describes the system architecture, the integrity mechanisms, implementation details, measured results, and the ethical design considerations of delegating job applications to software agents, all on a zero-cost free-tier deployment.", italic=True)
pagebreak()

# ================= TOC =================
heading("TABLE OF CONTENTS", 15, C)
for t_ in ["ABSTRACT", "LIST OF FIGURES", "LIST OF TABLES", "ABBREVIATIONS",
           "CHAPTER 1: INTRODUCTION", "CHAPTER 2: LITERATURE SURVEY",
           "CHAPTER 3: SYSTEM ANALYSIS AND REQUIREMENTS", "CHAPTER 4: SYSTEM DESIGN AND METHODOLOGY",
           "CHAPTER 5: IMPLEMENTATION", "CHAPTER 6: TESTING AND RESULTS",
           "CHAPTER 7: CONCLUSION AND FUTURE WORK", "REFERENCES",
           "ANNEXURE A: DEMONSTRATION COMMANDS", "ANNEXURE B: SAMPLE AGENT VERDICTS",
           "ANNEXURE C: GLOSSARY", "ANNEXURE D: OBSERVED RUN TIMELINE"]:
    p(t_, 12, align=L, space_after=2)
pagebreak()
heading("LIST OF FIGURES", 14)
for f_, d_ in [("Fig. 1.1", "ApplyPilot architecture: six batch stages, checkpoint store, honesty validator, apply agent"),
               ("Fig. 4.1", "The honesty validator loop (generator-critic with persisted verdicts)"),
               ("Fig. 4.2", "Apply-agent workflow: eligibility gate, truthful entry, mode-dependent termination"),
               ("Fig. 6.1", "Top discovery sources in the measured run (731 postings)"),
               ("Fig. 6.2", "Fit-score distribution of the 48 scored jobs"),
               ("Fig. 6.3", "Measured pipeline funnel (log scale)"),
               ("Fig. 6.4", "Measured stage timings of the live run (log scale)")]:
    p(f"{f_}\t{d_}", 12, align=L, space_after=3)
heading("LIST OF TABLES", 14)
for t_, d_ in [("Table 3.1", "Software requirements"),
               ("Table 4.1", "Fabrication threat model and validator responses"),
               ("Table 6.1", "Discovery sources (measured)"),
               ("Table 6.2", "Apply-stage outcomes (measured)"),
               ("Table 6.3", "Feature comparison with existing tools"),
               ("Table 6.4", "Measured stage outputs")]:
    p(f"{t_}\t{d_}", 12, align=L, space_after=3)
heading("ABBREVIATIONS", 14)
for k, v in [("LLM", "Large Language Model"), ("ATS", "Applicant Tracking System"),
             ("CDP", "Chrome DevTools Protocol"), ("MCP", "Model Context Protocol"),
             ("CLI", "Command-Line Interface"), ("API", "Application Programming Interface"),
             ("SaaS", "Software as a Service"), ("AGPL", "Affero GNU General Public License"),
             ("SSO", "Single Sign-On"), ("SQLite", "Lightweight embedded SQL database engine")]:
    p(f"{k}\t\u2013 {v}", 12, align=L, space_after=2)
pagebreak()

# ================= CHAPTER 1: INTRODUCTION =================
chapter("1", "Introduction")
heading("1.1 Problem Introduction")
p("A job search for entry-level engineering roles is a volume game played against time. Recruiters on major job boards receive hundreds of applications per posting, and candidates respond by applying more \u2014 each application demanding discovery, fit judgement, document customisation, and manual entry into the employer's career portal. A single application to a large employer using Workday, the enterprise HR system used by more than half of the Fortune 500, involves account creation, four to six form pages, document upload, and screening questions \u2014 typically 15\u201330 minutes of transcription work that is both cognitively draining and error-prone. For a final-year student applying across dozens of employers, the process consumes weeks of productive preparation time, and repetitive manual data entry silently disqualifies candidates through transcription errors.")
p("At the same time, large language models (LLMs) have become capable of exactly this class of work: reading unstructured text, judging semantic fit, rewriting documents under constraints, and \u2014 as autonomous software agents \u2014 operating real web interfaces through a browser. This convergence invites a question with both technical and ethical dimensions: can a free-tier, locally-run agent honestly and safely automate the entire application lifecycle on a person's behalf?")
heading("1.2 Motivation")
p("Three observations motivated this project. First, the bottleneck for fresh graduates is application volume and form-filling time, not lack of relevant skills. Second, existing automation tools fall into two unacceptable categories: mass-submitters that send a single generic resume everywhere (misrepresenting the candidate), and closed paid bots with opaque behaviour. Third, autonomous LLM agents now demonstrably operate enterprise web UIs, making a genuinely end-to-end system feasible.")
p("A further, distinctive motivation is integrity. An autonomous agent must never fabricate experience, and must refuse jobs the candidate cannot actually take \u2014 an agent that answers employer screening questions can also answer them falsely at scale. This project therefore treats honesty as a first-class subsystem, enforced by an automated validator and demonstrated by observed refusals, rather than as a prompt-level hope.")
heading("1.3 Project Objective")
p("The objective is to design, implement and empirically demonstrate a single-command, staged pipeline that:")
bl("discovers jobs from five boards (Indeed, Naukri, Glassdoor, LinkedIn, ZipRecruiter) plus employers' Workday career sites, with de-duplication in a local SQLite database;")
bl("scores each job for fit on a 1\u201310 scale against verified resume facts using an LLM rubric;")
bl("produces tailored resumes and cover letters whose every factual claim is machine-validated against the candidate's real history;")
bl("autonomously completes the employer's real application form in a browser, uploading the tailored resume, with a dry-run mode that stops before submission; and")
bl("enforces location/work-mode eligibility rules so that ineligible jobs are refused, not applied to.")
p("The complete system must run on free-tier APIs only, be reproducible from a public repository, and remain fully under the candidate's ownership and control.")
heading("1.4 Scope of the Project")
p("The system targets individual job seekers \u2014 particularly Indian students and early-career engineers \u2014 with a configurable search profile (locations, remote preference, salary floor). Application areas include personal job-search automation, ATS-friendly honest resume tailoring, a reference implementation of agent-performed enterprise form workflows, and a study artefact for the ethics of automated applications. Explicitly out of scope: CAPTCHA circumvention, login-wall bypass, platform terms-of-service violations, and any guarantee of interview outcomes. The pipeline uses only public APIs and application forms that employers publish for candidates.")
heading("1.5 Related Previous Work")
p("Prior work spans open-source auto-apply agents, commercial bots, autofill extensions, and academic agent benchmarks. Auto_Jobs_Applier_AIHawk (2024) automated LinkedIn Easy-Apply with LLM-answered screening questions but had no honesty validation and no eligibility reasoning, and was later curtailed by platform enforcement. LazyApply (commercial) bulk-submits a fixed resume. Simplify (extension) autofills application fields from a stored profile but leaves every click to the human. On the research side, ReAct established the reason-act loop for LLM agents; Toolformer showed models can learn tool use; WebArena and WorkArena benchmark agents on realistic enterprise portals including multi-page form tasks. Chapter 2 elaborates. No reviewed system integrates discovery, honest scoring, validated tailoring, and a real-browser apply agent into one free, auditable pipeline \u2014 the gap this project fills.")
heading("1.6 Organisation of the Report")
p("Chapter 2 surveys related tools and research. Chapter 3 analyses feasibility and requirements. Chapter 4 presents the system design: pipeline architecture, the honesty validator, and the apply agent. Chapter 5 describes implementation. Chapter 6 reports measured results from a live run, including the end-to-end Workday application and observed agent refusals. Chapter 7 concludes and outlines future work. References follow IEEE style; annexures provide demonstration commands, sample verdicts, a glossary, and the observed run timeline.")
pagebreak()

# ================= CHAPTER 2: LITERATURE SURVEY =================
chapter("2", "Literature Survey")
p("This chapter reviews the tools and research that define the state of the art in automated job application and LLM web agents, and identifies the gap ApplyPilot addresses.")
heading("2.1 Mass-Application Tools")
p("Auto_Jobs_Applier_AIHawk [6] is the best-known open-source auto-apply agent. It logs into LinkedIn, searches postings, and uses an LLM to answer employer screening questions and (optionally) tailor the resume, then submits via Easy-Apply. Its strengths \u2014 free, end-to-end, popular \u2014 were offset by serious weaknesses: no verification that LLM answers were truthful, no location/work-mode eligibility logic, and reliance on a single platform, which led to discontinuation after platform policy enforcement. LazyApply (commercial) is a paid desktop bot applying in bulk on multiple boards with a generic resume; its quantity-over-quality model is precisely what this project avoids. Simplify (browser extension) stores the user profile and autofills forms, with a job tracker, but is human-driven. Matching-as-a-service products (e.g., Sonara, since shut down) demonstrated demand for centralised solutions while illustrating their fragility.")
p("Beyond features, these tools raise a documented ethical debate: platforms actively enforce against bulk automation, while candidates face real time costs. The position taken in this project is that the defensible boundary is not automation per se but misrepresentation and system abuse; hence the design makes each application individually truthful, tailored, and human-gated for submission.")
heading("2.2 Research on LLM Web Agents")
p("ReAct [1] demonstrated that interleaving chain-of-thought reasoning with tool actions makes LLM agents substantially more reliable on interactive tasks, and is the basis of this project's apply-agent loop. Toolformer [5] showed LLMs can self-teach API/tool use, motivating tool-mediated integration over screen scraping. WebArena [2] provides self-hostable realistic web environments (including multi-page form filling) and found agents succeed on only a minority of realistic tasks \u2014 highlighting that real form workflows remain hard and need guardrails. WorkArena [3] and WorkArena++ [14] benchmarked agents on ServiceNow-style enterprise tasks, the same UI family as Workday; their finding that form navigation is among the harder capabilities informed this project's decision to drive the employer's UI step-by-step with an availability-first fallback to raw Chrome DevTools Protocol actions. Wang et al. [4] survey the plan\u2013act\u2013observe agent architecture with memory and tools that this project instantiates in lightweight form: SQLite as episodic memory, a policy prompt as the agent's charter, and Playwright/CDP as actuators.")
p("Reliability engineering for such agents is an active research area: models must be selected for tool-calling discipline, tool catalogs must be pinned to available actuators, and every run must terminate in a machine-readable verdict. The Gemini family technical report [15] and the OpenCode runtime [10] provide the free-tier model and agent substrate that make the deployment feasible at zero cost \u2014 a constraint treated as a feature, since it forces the architecture to be reproducible by any student.")
heading("2.3 The Upstream Project and This Fork")
p("The upstream ApplyPilot project [8] provided the staged-pipeline skeleton (discover \u2192 enrich \u2192 score \u2192 tailor \u2192 apply) with an honesty validator and Workday-first apply strategy under the AGPL-3.0 licence [13]. This project's careerOS fork [9] extends it for Indian free-tier use: a new agent backend (OpenCode with free hosted models), India-aware location-eligibility rules in the apply prompt, per-stage demonstration limits, a string-URL corruption fix in the discovery writer, validator fixes for legitimately-profiled skills, currency-neutral salary formatting, and a Chromium/CDP integration on Windows. All derived code remains AGPL-3.0 with credit to upstream, per the licence and the ethics of open personal automation.")
heading("2.4 Research Gap")
p("Synthesising the survey: (i) existing auto-apply tools optimise submission count, not truthfulness or eligibility; (ii) academic benchmarks demonstrate capability but no deployed personal system uses them with honesty enforcement; (iii) no free, open, locally-runnable system covers the full lifecycle (discovery \u2192 scoring \u2192 tailoring \u2192 submission) on multiple boards plus employer-native portals. ApplyPilot/careerOS fills this gap and, uniquely, treats fabrication prevention and eligibility refusal as testable, demonstrated features (Chapter 6).")
pagebreak()

# ================= CHAPTER 3: ANALYSIS & REQUIREMENTS =================
chapter("3", "System Analysis and Requirements")
heading("3.1 Feasibility Study")
p("Technical feasibility: all stages are ordinary Python processes plus a browser; the only external dependencies are free-tier LLM APIs and the employers' own public career endpoints. Economic feasibility: total recurring cost is zero on free tiers (Gemini Flash models and OpenCode-hosted GLM); the alternative commercial SaaS products cost US$30\u2013240 per year. Operational feasibility: the system runs on the student's own laptop; configuration is three local files (.env, profile.json, searches.yaml). Ethical/legal feasibility: the tool applies only through employers' own posted forms, submits only truthful data, and is licensed AGPL-3.0 with upstream attribution; it deliberately refuses to bypass logins or anti-bot systems.")
heading("3.2 Functional Requirements")
bl("FR1 \u2014 Discovery: collect postings from configured boards and Workday career sites; de-duplicate; persist with full raw description.")
bl("FR2 \u2014 Enrichment: fetch complete descriptions and employer metadata for shortlisted jobs, including JavaScript-rendered pages.")
bl("FR3 \u2014 Scoring: assign an integer fit score 1\u201310 per job against structured resume facts; persist with rubric metadata.")
bl("FR4 \u2014 Tailoring: generate job-specific resumes subject to validator approval; maximum 5 generator-critic rounds; convert to PDF.")
bl("FR5 \u2014 Cover letters: generate under the same validation regime.")
bl("FR6 \u2014 Application: autonomously complete the employer's form with truthful data; support submit and dry-run modes; record structured verdicts.")
bl("FR7 \u2014 Eligibility: refuse applications violating configured location/work-mode rules, with reasons persisted.")
bl("FR8 \u2014 Audit: persist every stage output, every validator verdict, and every apply attempt with transcripts.")
bl("FR9 \u2014 Dashboard: expose pipeline state (counts, scores, statuses) without SQL.")
heading("3.3 Software Requirements")
table("Table 3.1 \u2014 Software requirements",
      [("Component", "Choice"),
       ("OS", "Windows 10/11 64-bit (Linux compatible)"),
       ("Runtime", "Python 3.13; Node.js LTS (MCP server); SQLite (bundled)"),
       ("LLM APIs", "Google Gemini (flash) free tier; OpenCode free hosted models (GLM)"),
       ("Agent runtime", "OpenCode CLI, headless run mode"),
       ("Browser automation", "Playwright + Playwright MCP server over CDP; Chromium-family browser"),
       ("Libraries", "python-jobspy, python-dotenv, PyYAML, reportlab/docx2pdf, python-docx")])
heading("3.4 Hardware Requirements")
p("Any modern laptop: quad-core CPU, 8 GB RAM, ~1 GB free disk, broadband internet. Development and testing used a Windows 11 laptop with a Chromium-family browser (Brave).")
pagebreak()

# ================= CHAPTER 4: DESIGN =================
chapter("4", "System Design and Methodology")
heading("4.1 Architecture Overview")
p("ApplyPilot is organised as six idempotent batch stages around a single SQLite checkpoint database, followed by an interactive agent stage (Fig. 1.1). Every stage is independently runnable from the CLI (applypilot run <stage>), is resumable after interruption, and carries optional --limit flags for controlled demonstrations. Configuration lives in three user-owned files: .env (API keys), profile.json (verified candidate facts, salary floor, work-mode constraints), and searches.yaml (locations, remote preference, boards, queries).")
figure("fig1_pipeline.png", 6.2, "Fig. 1.1  ApplyPilot architecture: six batch stages around a SQLite checkpoint store, the honesty validator supervising document generation, and the interactive apply agent driving a real browser.")
p("Four design principles shaped the architecture. (1) Local-first: all data \u2014 the profile, the database, the documents \u2014 lives on the candidate's machine; nothing is sent to third parties beyond the LLM APIs and the employers' own career endpoints. (2) Checkpoint everything: every stage writes its output to SQLite, making the pipeline resumable and auditable. (3) Free-tier operational: the system must run without any paid API. (4) Honesty as architecture, not aspiration: integrity mechanisms are separate, testable components with logged behaviour.")
heading("4.2 Stage Design")
p("Stage 1 \u2014 Discover: python-jobspy [12] scrapes Indeed, Naukri, Glassdoor, LinkedIn and ZipRecruiter for configured queries (India + remote); an additional Workday crawler walks employers' public career-site APIs (e.g., cisco.wd5.myworkdayjobs.com) for direct application URLs. Postings are de-duplicated by a company+title+URL signature and stored with full raw description.")
p("Stage 2 \u2014 Enrich: for each shortlisted job, the full description and employer metadata are fetched, rendering JavaScript-heavy pages with Playwright [11]; enrichment marks each job eligible for scoring.")
p("Stage 3 \u2014 Score: an LLM rates each job 1\u201310 for fit against structured resume facts, using a strict rubric covering skills overlap, seniority, location/remote compliance and salary floor. Model output is parsed defensively (markdown stripping, regex integer extraction) and persisted. Jobs below the threshold are never tailored, saving API quota.")
p("Stage 4 \u2014 Tailor: for high-fit jobs the LLM rewrites the resume for the role. Every generated document is passed to the honesty validator (Section 4.3) before acceptance; rejected documents return to the LLM with specific objections (maximum 5 attempts), after which the job is flagged for human review. Approved documents are converted to PDF.")
p("Stage 5 \u2014 Cover: cover letters are generated under the same validation regime. Stage 6 \u2014 PDF: approved documents are converted and filed per job.")
heading("4.3 The Honesty Validator")
p("The validator is the project's integrity core. It answers the central ethics question of auto-apply systems: what may an agent say on a person's behalf? The answer designed here: only what the person could truthfully say, verified mechanically.")
table("Table 4.1 \u2014 Fabrication threat model and validator responses",
      [("Fabrication class", "Detection strategy", "Observed example"),
       ("Entity invention", "Compare named employers/projects against profile facts", "Hallucinated project and employer references caught in early drafts"),
       ("Metric inflation", "Extract numbers; compare against evidenced metrics", "Invented CGPA value removed after validator objection"),
       ("Capability inflation", "Skills boundary: listed skills may be discussed; unknown skills may not be claimed", "Out-of-bound skill claims rejected; listed C++/Rust correctly allowed")])
p("The validation procedure is deliberately deterministic so that identical documents always receive identical verdicts. The steps (Fig. 4.1) are: (1) normalise the document text; (2) segment it into claims \u2014 sentences containing a named entity, a number, or a skill term; (3) resolve each claim's entities against the profile's verified sets (employers, projects, education, metrics, skills); (4) classify unresolved entities as paraphrase (allowed), omission-context (allowed), or invention (rejected); (5) enforce the skills boundary, with normalisation guards for legitimately listed skills; (6) on any rejection, compose a structured objection (sentence index, entity, reason class) and return the document to the generator; (7) accept only when zero claims are rejected, persisting the validator report alongside the document.")
p("Rejected documents return to the LLM with structured objections, with up to five revision attempts before the job is flagged for human review. This turns fabrication from an invisible statistical risk into a visible, logged rejection event. During the deployment the validator rejected early tailored drafts containing a hallucinated CGPA value and an invented project reference, and initially produced a false positive on the candidate's listed skill C++; the skills-boundary normalisation guard corrected this, after which all nine tailored resumes and five cover letters passed. The false positive and its fix are recorded in the fork's commit history.")
figure("fig6_validator.png", 4.2, "Fig. 4.1  The honesty validator loop: deterministic claim resolution against verified facts; rejection returns structured objections to the generator, acceptance persists a report artefact.")
heading("4.4 The Autonomous Apply Agent")
p("The apply stage launches an LLM agent per job (OpenCode CLI [10] running a free hosted model such as GLM or Gemini Flash) with three assets: a policy prompt built from profile.json with hard rules; a browser toolset \u2014 a Playwright MCP server [11] driving the candidate's own Chromium-family browser over the Chrome DevTools Protocol (CDP) on a debug port, with raw-CDP script fallback for steps the MCP tools cannot express; and the tailored documents.")
p("The workflow (Fig. 4.2) begins with an eligibility check before any form interaction: the agent reads the posting and, where necessary, the employer's own API; ineligible jobs terminate immediately with RESULT:FAILED:not_eligible_location. Eligible jobs proceed through account creation, field entry, resume upload, and truthful screening answers to the Review page. In submit mode the agent clicks Submit and verifies; in dry-run mode it stops and saves the draft. Every run terminates with a structured verdict (RESULT:APPLIED | RESULT:FAILED:<reason>) recorded in apply_attempts, producing a complete audit trail per application.")
p("The prompt enforces: true facts only from the profile; relocation None must be reported as None, never guessed; salary answers from the posting's own range and the profile floor, never invented; currency-aware formatting; and dry-run discipline. Representative rules quoted from the implementation:")
bl("\u201cNever invent information not in the profile. If you don't know something, answer honestly rather than guessing.\u201d")
bl("\u201cRemote or work-from-anywhere \u2192 ELIGIBLE. Onsite only in a different country with no remote option \u2192 NOT ELIGIBLE.\u201d")
bl("\u201cDo NOT click the final Submit button (dry-run). The candidate makes the submission decision.\u201d")
bl("\u201cYour browser tools are the MCP playwright tools (tools.playwright.*), already connected to a real Chrome with remote debugging. Never conclude that no browser is available without calling them first.\u201d")
figure("fig5_agent.png", 6.2, "Fig. 4.2  Apply-agent workflow: eligibility gate before any form work, truthful field entry, and mode-dependent termination (submit vs. dry-run) with structured verdicts.")
heading("4.5 Worker Isolation Model")
p("Each apply run executes inside an isolated worker: a per-worker working directory (apply-workers/worker-N) holding the agent's configuration, the job prompt, and the tailored documents, plus a persistent browser profile directory that is deliberately not reset between jobs. The working directory is cleaned and rebuilt per run, so agent side-effects cannot accumulate, while browser state (cookies, logins) persists so that a one-time human login on a walled board remains reusable. The agent runs headless (opencode run --auto --standalone) with its MCP browser config written per worker, pointing at the CDP debug port of a browser instance the pipeline launches itself. This isolation model yields reproducibility, safety (the agent cannot mutate the host configuration), and observability.")
heading("4.6 The LLM Layer")
p("Three LLM interaction patterns appear, each with its own reliability contract. (1) Batch scoring/tailoring calls (Gemini Flash): stateless, structured-output prompts with defensive parsing \u2014 the pipeline strips markdown fences, extracts integers via regex, and re-prompts on parse failure. (2) Validator critiques: deterministic post-processing where the critic is code, not a model, making verdicts reproducible. (3) The interactive agent (GLM by default): a long-horizon tool-calling conversation in which model choice materially matters \u2014 faster models were observed querying the tool catalog before the MCP server finished connecting and concluding no browser exists; the default was therefore pinned to a slower but tool-reliable model, with explicit tool-catalog hints injected into the prompt.")
p("Quota strategy. Free-tier limits are handled at three levels: stage-level retries with exponential backoff; checkpointing so a quota-interrupted batch resumes exactly where it stopped; and optional model overrides per stage so a single exhausted provider never blocks the whole pipeline.")
heading("4.7 Database Schema")
p("Core tables: jobs (id, site, title, company, location, description, url, fit_score, tailored_resume_path, apply_status, apply_error, apply_attempts), resumes and cover_letters (job linkage, approval status, validator report), and apply_attempts (per-run status, reason, transcript reference). The database doubles as the dashboard source (applypilot status / applypilot dashboard).")
pagebreak()

# ================= CHAPTER 5: IMPLEMENTATION =================
chapter("5", "Implementation")
heading("5.1 Technology Stack")
p("The pipeline is approximately 9,600 lines of Python 3.13 with asyncio-based stage runners, plus: python-jobspy (board scraping), Playwright and a Playwright MCP server under Node.js LTS (browser automation), SQLite via the standard library (checkpoint store), reportlab/docx2pdf (PDF generation), PyYAML and python-dotenv (configuration), and the OpenCode CLI as the agent runtime (free GLM/Gemini models). The fork is developed in Git and published at github.com/shashank-tomar0/careerOS.")
heading("5.2 Key Implementation Decisions")
p("(a) Editable install plus CLI packaging so every stage is one command on the student's terminal. (b) Agent backend abstraction: the launcher supports both Claude Code and OpenCode; OpenCode was chosen for zero cost, driven through its headless run mode with the MCP configuration written per worker. (c) Browser profile persistence: the worker's browser profile directory is reused across jobs, so a manual login persists for later automated runs. (d) System-browser over bundled Chromium: the agent drives the user's installed Chromium-family browser via CDP, avoiding a large download and enabling human observation. (e) Defensive LLM parsing: scores and agent results are parsed with markdown-stripping and regex extraction so free-tier model verbosity cannot corrupt the database. (f) Rate-limit resilience: stage-level retries with backoff; the agent default model was chosen for tool-calling reliability under free-tier quotas. (g) Structured agent output protocol (RESULT:*) so every run terminates with a machine-readable verdict recorded in apply_attempts.")
heading("5.3 Command Surface and Human Interaction Model")
p("The human interface is a small, deliberate CLI. applypilot doctor verifies environment health (API keys, browser availability, Node/MCP installation) before any run. Each stage is a first-class command (applypilot run <stage> [--limit N --workers W --model M]) with checkpointed state, so the human can inspect results between stages; applypilot status and applypilot dashboard render the database as a live scoreboard. The design principle is that the human always has a decision point between stages \u2014 automation handles transcription and navigation; the human owns thresholds, targeting, and submission. This is also a safety property: nothing expensive runs without a human-initiated command.")
pagebreak()

# ================= CHAPTER 6: TESTING & RESULTS =================
chapter("6", "Testing and Results")
heading("6.1 Setup")
p("All evaluation was performed on a live deployment on the author's own resume (B.Tech CSE student, India, remote-preferring, salary floor configured), on a Windows 11 laptop with a Chromium-family browser and free-tier LLM APIs. Every number reported below is read from the production SQLite store \u2014 none is simulated.")
heading("6.2 Discovery Results")
p("The pipeline stored 731 unique postings across eight sources; employer Workday portals dominated (Fig. 6.1 and Table 6.1). The dominance of employer-native portals validates the Workday-first apply strategy: the highest-value application targets publish their own structured endpoints.")
figure("fig4_sources.png", 4.4, "Fig. 6.1  Top discovery sources in the measured run (731 postings; employer Workday portals dominate over aggregators).")
table("Table 6.1 \u2014 Discovery sources (measured, top 8 of 18)",
      [("Source", "Postings", "Share"),
       ("Thomson Reuters (board-aggregated)", "230", "31.4%"),
       ("Cisco (Workday)", "103", "14.1%"),
       ("Moderna (Workday)", "85", "11.6%"),
       ("Mastercard (Workday)", "76", "10.4%"),
       ("Motorola Solutions (Workday)", "75", "10.3%"),
       ("Indeed (direct)", "72", "9.8%"),
       ("Salesforce (Workday)", "35", "4.8%"),
       ("Others (LinkedIn, Ciena, PwC, ...)", "55", "7.6%")])
heading("6.3 Scoring Results")
p("48 jobs were scored under the free-tier configuration. The distribution (Fig. 6.2) is discriminating: a weak band at 1\u20133 (21 jobs), a marginal band at 4\u20136 (16), and a fit tail at 7\u20139 (11). 18.8% of scored jobs reached \u22657, a plausible precision-oriented threshold for expensive downstream stages. The three 9/10 postings were Cisco Software Engineer (Bangalore) roles with direct Workday application URLs \u2014 exactly the profile the apply agent handles best.")
figure("fig2_scores.png", 4.4, "Fig. 6.2  Real fit-score distribution of the 48 scored jobs (author's live run); red/amber/green encode weak/marginal/strong fit; dashed line marks the \u22657 apply threshold.")
heading("6.4 Document Generation Results")
p("Nine tailored resumes and five cover letters were produced and converted to PDF, all passing the honesty validator after the generator-critic loop. Observed objection classes matched the threat model: unevidenced project mentions (a hallucinated CGPA and an invented project were caught and removed in early iterations) and out-of-bound skill claims.")
heading("6.5 Apply Outcomes")
p("Table 6.2 summarises the measured outcomes. The culminating test ran the agent in dry-run mode against a 9/10-fit Cisco Software Engineer posting on Cisco's live Workday careers site. The agent autonomously verified eligibility, opened the application, created the candidate account, navigated every form page (handling dropdown and listbox widgets), uploaded the tailored resume PDF (system-confirmed upload), completed screening questions truthfully, and reached the Review page, where it stopped and reported RESULT:APPLIED (dry-run) with a complete audit trail. The saved draft means a real submission is one click away \u2014 the human decides.")
table("Table 6.2 \u2014 Apply-stage outcomes (measured)",
      [("Outcome", "Jobs", "Verdict observed"),
       ("Dry-run completed (Workday)", "1", "RESULT:APPLIED (dry-run); draft saved at Review"),
       ("Eligibility refusal", "2", "RESULT:FAILED:not_eligible_location"),
       ("Login wall (Indeed smart apply)", ">12", "RESULT:FAILED:sso_required / indeed_login_wall"),
       ("Tailored + queued for apply", "9", "documents approved; awaiting runs"),
       ("Real submissions", "0", "held for human decision by design")])
p("Negative tests were as informative as the positive one. (1) Location refusal: the agent refused a Moderna posting (onsite, Massachusetts) after querying the employer's API for the work arrangement. (2) Relocation refusal: the agent refused a Motorola posting in another Indian city after the Workday screening revealed relocation was required and the profile says relocation \u201cNone\u201d \u2014 it reported the truthful answer rather than guessing. (3) Fabrication guard: the validator correctly rejected drafts citing metrics/projects absent from the resume, and correctly allowed genuinely-listed skills after the skills-boundary fix. (4) Salary sanity: prompt tests caught a currency-format error (a $-formatted INR floor), fixed to currency-neutral formatting. (5) Failure-mode documentation: Indeed-hosted postings requiring a session login terminate with a structured sso_required verdict \u2014 the system fails safely and auditable rather than attempting bypass.")
figure("fig3_funnel.png", 4.4, "Fig. 6.3  Measured pipeline funnel (log scale): discovery feeds a precision-filtered document-generation and application path, with two eligibility refusals recorded.")
heading("6.6 Timings and Observability")
p("Measured stage timings under free-tier conditions (Fig. 6.4): a 24-job scoring batch completed in approximately 78 seconds (limited by the API rate cap, not model latency); a full 48-job scoring pass ran in the low minutes; tailoring with validator rounds averaged under a minute per document; the culminating dry-run application ran about 18 minutes end-to-end, dominated by form navigation and two raw-CDP fallbacks, not model latency. Observability is a design goal: every stage appends to per-run logs, the database records per-stage row counts, and the dashboard exposes progress without SQL.")
figure("fig7_timings.png", 4.4, "Fig. 6.4  Measured stage timings of the live run (log scale): batch stages are quota-bound and fast; the interactive dry-run application is navigation-bound.")
heading("6.7 Failure Modes and Mitigations")
p("Free-tier operation surfaced three reproducible failure classes, all mitigated. (1) Quota exhaustion and 15-requests/minute rate limits on Gemini Flash, addressed by model fallback and stage-level retries with backoff. (2) Agent-browser desynchronisation, in which fast models queried for browser tools before the MCP server finished connecting \u2014 mitigated by model selection (a slower, tool-reliable default) and explicit tool-catalog hints in the prompt. (3) Verbose model output corrupting parsers, mitigated by defensive extraction. Agent improvisation drift (composing raw-CDP helper scripts when MCP tools did not cover a widget) was tolerated within the pinned browser actuator \u2014 pragmatically trading purity for capability. Each fix is a published commit in the fork's history.")
table("Table 6.3 \u2014 Feature comparison with existing tools",
      [("Capability", "AIHawk", "LazyApply", "Simplify", "ApplyPilot/careerOS"),
       ("Multi-board discovery", "LinkedIn only", "Multi-board", "Extension-scoped", "5 boards + Workday APIs"),
       ("Honest tailoring", "None", "None (fixed resume)", "Profile autofill only", "Generator-critic validator"),
       ("Eligibility reasoning", "None", "None", "None", "Location/work-mode gate"),
       ("Autonomous real-browser apply", "Platform-embedded", "Bot emulation", "Human clicks", "CDP+MCP agent, Workday-native"),
       ("Auditability / cost", "Logs / free", "Opaque / paid", "Tracker / free tier", "SQLite verdicts+transcripts / free")], sizes=9)
heading("6.8 Threats to Validity")
p("Internal validity: all LLM outputs (scores, documents, agent actions) pass through deterministic parsing or code-based validation, so the reported numbers are not re-reads of model prose; however, LLM scoring itself has no ground truth beyond the rubric \u2014 a human-rater agreement study is future work. External validity: the deployment is a single candidate profile in one market (India, entry-level, remote-preferring); transferability to other profiles is plausible but unmeasured. Construct validity: dry-run completion measures form-completion capability, not application success; response-rate measurement is future work. Reliability: free-tier quotas introduce run-to-run variance in stage latency, though checkpointing makes outputs deterministic once a stage completes.")
table("Table 6.4 \u2014 Measured stage outputs",
      [("Stage", "Output", "Measured"),
       ("Discover", "unique postings stored", "731"),
       ("Score", "jobs scored", "48 (1\u20139 spread; 18.8% \u22657)"),
       ("Tailor", "approved tailored resumes", "9 (+PDFs)"),
       ("Cover", "approved cover letters", "5 (+PDFs)"),
       ("Apply", "dry-run completions / refusals", "1 / 2")])
pagebreak()

# ================= CHAPTER 7: CONCLUSION =================
chapter("7", "Conclusion and Future Work")
heading("7.1 Conclusion")
p("This project set out to answer whether a free-tier, locally-run LLM system could automate a student's entire job-application lifecycle \u2014 and do so honestly. The answer demonstrated on live systems is yes: 731 jobs discovered, AI fit-scoring with a discriminating 1\u20139 distribution, validator-approved tailored resumes and cover letters, and a fully autonomous, end-to-end completion of a real Fortune-500 Workday application (form filled, resume uploaded, draft saved at Review) with two observed refusals of ineligible jobs. The contribution is both practical (a working, free careerOS for the author) and methodological: an integrity architecture \u2014 verified-facts profile, generator-critic honesty validation, eligibility gating, and structured audit protocol \u2014 that makes personal job-application automation defensible. The work is released as an AGPL-3.0 fork crediting the upstream ApplyPilot project, consistent with the ethics of open, auditable personal automation.")
heading("7.2 Future Work")
bl("Coverage: session-persistent operation on login-walled boards (the human logs in once; the agent owns the flow thereafter), extending the Workday crawler to additional employer ATS families (Greenhouse, Lever, SuccessFactors).")
bl("Learning: an outcome-tracking stage correlating tailoring strategies and cover-letter styles with employer replies, turning the pipeline into a feedback-driven system.")
bl("Integrity science: adversarial evaluation of the honesty validator \u2014 attack it with subtly-inflated documents, measure catch rate, and publish the objection taxonomy as a benchmark.")
bl("Evaluation at scale: multi-candidate studies with response-rate A/B measurement against manual applications.")
bl("Agent capability: form-semantic tools (field-type aware fill/verify primitives) to reduce raw-CDP fallbacks, benchmarked against WorkArena-style task decompositions, plus a scheduling layer for unattended daily operation within free-tier quotas.")
bl("Generalisation: the honest-agent harness pattern (verified-facts profile + generator-critic validation + eligibility gate + auditable verdicts) applies to any domain where an agent transacts on a person's behalf against rules-bound institutions \u2014 government forms, university applications, vendor onboarding.")
pagebreak()

# ================= REFERENCES =================
p("REFERENCES", 15, bold=True, align=C, space_after=10)
refs = [
    "S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, \u201cReAct: Synergizing Reasoning and Acting in Language Models,\u201d in Proc. ICLR, 2023. arXiv:2210.03629.",
    "S. Zhou et al., \u201cWebArena: A Realistic Web Environment for Building Autonomous Agents,\u201d in Proc. ICLR, 2024. arXiv:2307.13854.",
    "L. Boisvert et al., \u201cWorkArena: How Capable are Web Agents at Tackling Commonplace Knowledge Work Tasks?\u201d in Proc. ICML, 2024. arXiv:2403.07718.",
    "L. Wang, C. Ma, X. Feng, et al., \u201cA Survey on Large Language Model based Autonomous Agents,\u201d Front. Comput. Sci., vol. 18, no. 6, 2024. arXiv:2308.11432.",
    "T. Schick et al., \u201cToolformer: Language Models Can Teach Themselves to Use Tools,\u201d in Proc. NeurIPS, 2023. arXiv:2302.04761.",
    "feder-cr, \u201cAuto_Jobs_Applier_AIHawk,\u201d GitHub repository, 2024. [Online]. Available: https://github.com/feder-cr/AI_Hawk",
    "Pickle-Pixel, \u201cApplyPilot: A local-first autonomous job application pipeline,\u201d GitHub repository, AGPL-3.0, 2025. [Online]. Available: https://github.com/Pickle-Pixel/ApplyPilot",
    "S. Tomar, \u201ccareerOS: ApplyPilot fork for India-focused, free-tier autonomous applications,\u201d GitHub repository, AGPL-3.0, 2026. [Online]. Available: https://github.com/shashank-tomar0/careerOS",
    "Free Software Foundation, \u201cGNU Affero General Public License v3.0,\u201d Nov. 2007. [Online]. Available: https://www.gnu.org/licenses/agpl-3.0.html",
    "OpenCode, \u201cOpenCode: terminal-based AI coding agent,\u201d 2025. [Online]. Available: https://opencode.ai",
    "Microsoft, \u201cPlaywright: Web Automation and Testing,\u201d 2025. [Online]. Available: https://playwright.dev",
    "Slatec LLC, \u201cJobSpy: multi-board job scraper library,\u201d 2025. [Online]. Available: https://github.com/cullenwatson/JobSpy",
    "Gemini Team, Google, \u201cGemini: A Family of Highly Capable Multimodal Models,\u201d Technical Report, 2023. arXiv:2312.11805.",
    "S. Zhang et al., \u201cWorkArena++: Towards Compositional Planning and Reasoning-Based Common Knowledge Work Tasks,\u201d in Proc. ACL, 2024. arXiv:2407.05265.",
]
for i, r in enumerate(refs, 1):
    p(f"[{i}] {r}", 11, space_after=4, align=J)
pagebreak()

# ================= ANNEXURES =================
p("ANNEXURE A \u2014 DEMONSTRATION COMMANDS", 14, bold=True, align=C, space_after=10)
p("The complete system is demonstrated with the following commands (run from the project root; editable install):", 12)
for c_ in ["applypilot doctor", "applypilot run discover --limit 2", "applypilot run enrich --limit 2 --workers 2",
           "applypilot run score --limit 4", "applypilot run tailor --validation lenient --limit 2",
           "applypilot run cover --validation lenient --limit 2", "applypilot run pdf --limit 2",
           "applypilot status", "applypilot dashboard", "applypilot apply --dry-run --limit 1",
           "applypilot apply --limit 1   (real submission)"]:
    p("> " + c_, 11, align=L, space_after=3)
pagebreak()
p("ANNEXURE B \u2014 SAMPLE AGENT VERDICTS (WORKER LOG EXCERPTS)", 14, bold=True, align=C, space_after=10)
p("Dry-run completion: \u201cRESULT:APPLIED (dry-run \u2014 application fully filled and saved as a draft through the Review step; final Submit intentionally not clicked per instructions. To finish, the candidate only needs to open the Workday application and click Submit.)\u201d", 12)
p("Eligibility refusal: \u201cRESULT:FAILED:not_eligible_location \u2014 job verified onsite in Massachusetts, USA with no remote option; candidate profile relocation: None.\u201d", 12)
p("Resume upload (system event): \u201cSuccessfully Uploaded!\u201d", 12)
p("Scoring tail (fit spread): \u201c9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 4 \u2026 2 \u2026 1\u201d across the 48 scored jobs.", 12)
pagebreak()
p("ANNEXURE C \u2014 GLOSSARY", 14, bold=True, align=C, space_after=10)
for k, v in [("Workday", "Enterprise HR platform whose career portal is used by most Fortune-500 employers for applications."),
             ("Easy Apply", "LinkedIn's one-click application flow."),
             ("Fit score", "LLM-assigned 1\u201310 rating of job-candidate match against verified resume facts."),
             ("Dry run", "Agent completes the application but stops before final submission."),
             ("Generator-critic", "Pattern where an LLM generates content and an independent checker rejects non-compliant output."),
             ("CDP", "Chrome DevTools Protocol \u2014 low-level browser control channel used as automation fallback."),
             ("Free tier", "Cloud API usage allowance with zero cost, subject to rate limits.")]:
    p(k + ": " + v, 12, align=J, space_after=4)
pagebreak()
p("ANNEXURE D \u2014 OBSERVED RUN TIMELINE (SELECTED EVENTS)", 14, bold=True, align=C, space_after=10)
for t_ in ["Pipeline scored 24 evaluation jobs in ~78 seconds under free-tier quota management.",
           "Two 9/10-fit Cisco Bangalore postings identified with direct Workday application URLs; an 8/10 kept as backup.",
           "First dry-run: agent correctly refused a Moderna posting (onsite Massachusetts) after querying the employer's API \u2014 RESULT:FAILED:not_eligible_location.",
           "Second dry-run: agent refused a Motorola Bangalore posting whose screening required relocation; profile says relocation None \u2014 truthful answer reported.",
           "Prompt audit caught and fixed a currency-format error (a $-formatted INR salary floor) and a dry-run/submit contradiction in the mission statement.",
           "Agent desynchronisation diagnosed: fast models queried browser tools before the MCP server connected; fixed by model choice plus tool-catalog hints.",
           "Culminating dry-run: full Workday flow \u2014 account created, all form pages filled (dropdown/listbox widgets handled), tailored resume uploaded (\u201cSuccessfully Uploaded!\u201d), Review page reached, draft saved, RESULT:APPLIED (dry-run).",
           "Validator false positive on listed skill C++ identified and fixed via skills-boundary normalisation guard; all documents subsequently approved."]:
    p("\u2022 " + t_, 12, align=J, space_after=4)

doc.save(DIR + "ApplyPilot_Project_Report.docx")
print("PROJECT REPORT v2 SAVED")
