# -*- coding: utf-8 -*-
"""careerOS final project report — college chapter-wise format with evidence-based figures."""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT

TNR = "Times New Roman"
J = WD_ALIGN_PARAGRAPH.JUSTIFY; C = WD_ALIGN_PARAGRAPH.CENTER; L = WD_ALIGN_PARAGRAPH.LEFT
DIR = "C:/Users/dell/Desktop/mini-project/docs/college/"
TITLE = "careerOS: Job Discovery, Resume Tailoring, and Browser-Assisted Application Preparation"

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
    image_path = fname if fname.startswith("C:/") else DIR + fname
    par.add_run().add_picture(image_path, width=Inches(width))
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
p("SUBMISSION CHECK: Complete bracketed fields for roll numbers, team members (if applicable), guide/mentor, signatures, and dates.", 9, italic=True, align=C, line=1.0, space_after=2)
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
p("Job applications require repeated discovery, fit assessment, document preparation, and data entry into employer portals. This report documents careerOS, an India-oriented fork of ApplyPilot that combines Python pipeline stages, hosted language-model services, a local SQLite job store, and browser automation to assist with this workflow. Its integrity controls are layered rather than absolute: deterministic resume checks cover required structure, selected preserved facts, a limited skills watch-list, and text rules; a prompt-based LLM judge is available in normal/strict resume modes but is skipped in lenient mode; cover-letter checks do not establish factual accuracy. In the inspected local database snapshot, 731 unique job URLs were stored (645 via the Workday CXS path and 86 via JobSpy), 48 were scored, and 13 (27.1%) had scores of at least 7. Nine job rows referenced seven distinct resume paths and nine referenced seven distinct cover-letter paths. A worker transcript records a Cisco Workday dry run reaching Review with the final Submit button left untouched; it also records two eligibility refusals. These are single-user, observational results, not evidence of application submission or hiring outcomes. The report presents the architecture, implementation, evaluation limits, ethical considerations, and IEEE-numbered references.", italic=True)
pagebreak()

# ================= TOC =================
heading("TABLE OF CONTENTS", 15, C)
for t_ in ["ABSTRACT", "LIST OF FIGURES", "LIST OF TABLES", "ABBREVIATIONS",
           "CHAPTER 1: INTRODUCTION", "CHAPTER 2: LITERATURE SURVEY",
           "CHAPTER 3: SYSTEM ANALYSIS AND REQUIREMENTS", "CHAPTER 4: SYSTEM DESIGN AND METHODOLOGY",
           "CHAPTER 5: IMPLEMENTATION", "CHAPTER 6: TESTING AND RESULTS",
           "CHAPTER 7: CONCLUSION AND FUTURE WORK", "REFERENCES",
           "ANNEXURE A: DEMONSTRATION COMMANDS", "ANNEXURE B: SAMPLE AGENT VERDICTS",
           "ANNEXURE C: GLOSSARY", "ANNEXURE D: EVIDENCE NOTES"]:
    p(t_, 12, align=L, space_after=2)
pagebreak()
heading("LIST OF FIGURES", 14)
for f_, d_ in [("Fig. 4.1", "careerOS architecture and data boundaries"),
               ("Fig. 4.2", "Implemented document checks and validation-mode limits"),
               ("Fig. 4.3", "Browser-assisted application workflow and mode-specific action"),
               ("Fig. 6.1", "Database acquisition strategies and largest source labels"),
               ("Fig. 6.2", "Database-derived fit-score histogram"),
               ("Fig. 6.3", "Snapshot outputs and distinct evidence types")]: 
    p(f"{f_}\t{d_}", 12, align=L, space_after=3)
heading("LIST OF TABLES", 14)
for t_, d_ in [("Table 3.1", "Software and external service requirements"),
               ("Table 4.1", "Document risks and implemented checks"),
               ("Table 6.1", "Largest stored source labels"),
               ("Table 6.2", "Evidence sources and observed application state"),
               ("Table 6.3", "Descriptive feature comparison"),
               ("Table 6.4", "Database snapshot outputs")]: 
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
p("A job search involves discovering openings, assessing fit, preparing documents, and entering information into employer career portals. Repeating these tasks can consume time and introduce data-entry errors. Some employers use enterprise applicant-tracking systems such as Workday, where applicants may encounter account setup, multi-step forms, document upload, and screening questions. The amount of effort varies by role and portal; this report does not measure average application time or the effect of automation on candidate outcomes.")
p("Large language models (LLMs) can process unstructured text, produce job-fit assessments, and generate documents under constraints. Coupled with browser automation, they can also interact with web interfaces. These capabilities motivate an engineering question: how can such tools assist with the job-application workflow while making their limits and risks visible?")
heading("1.2 Motivation")
p("This project is motivated by the repetitive work of identifying relevant roles and completing application forms. Language models can summarize postings and generate role-specific documents, while browser automation can interact with web forms. These capabilities also introduce risks, including unsupported generated claims, incorrect field entries, privacy exposure, and unintended submission; the implementation and evaluation must be considered in that context.")
p("A further motivation is data integrity. An agent can produce inaccurate statements or answer screening questions incorrectly, so generated documents and form entries need human review. The repository includes several checks, but their coverage varies by document type and validation mode; they should not be interpreted as proof that every statement is true.")
heading("1.3 Project Objective")
p("The objective is to implement and inspect a staged workflow that:")
bl("discovers and stores job postings from configured JobSpy sources and employer Workday career endpoints;")
bl("assigns each job a fit score on a 1\u201310 scale using an LLM prompt and candidate information;")
bl("generates tailored resumes and cover letters with checks whose coverage depends on document type and validation mode;")
bl("supports browser-assisted form completion with configurable dry-run and submit modes; and")
bl("uses prompt-guided location/work-mode checks before application steps.")
p("The evaluated configuration used free-tier services, but quotas, terms, availability, and pricing can change. Reproducing results requires equivalent configuration, model access, candidate data, and employer-site behavior. ‘Free tier’ describes the observed access conditions, not a guarantee of zero cost for future or larger runs.")
heading("1.4 Scope and Responsible-Use Boundary")
p("The repository targets individual job seekers, particularly early-career candidates, using a configurable search profile. This report evaluates job discovery, enrichment, scoring, document generation, and a browser-assisted Workday dry run. It does not establish compatibility with every job board, portal, or candidate profile, nor improved interview or employment outcomes. Source review found optional third-party CAPTCHA-solving instructions in the apply-agent prompt. This conflicts with any blanket claim that the current repository never attempts CAPTCHA circumvention. A conservative deployment should disable that path and stop for human review at anti-bot challenges, while complying with applicable employer and platform terms. CAPTCHA solving is not claimed as an evaluated feature.")
heading("1.5 Related Previous Work")
p("Related work spans job-application automation, browser autofill, and benchmarks for language-model agents. AIHawk describes a job-search and application workflow [1]. ReAct studies interleaved reasoning and action [2], while WebArena, WorkArena, and WorkArena++ provide benchmark environments for web and enterprise tasks [3], [4], [5]. These works motivate tool-mediated interaction and careful evaluation; they do not establish careerOS behavior or effectiveness. Chapter 2 reviews the sources and positions this project as an engineering integration rather than a novel agent benchmark.")
heading("1.6 Organisation of the Report")
p("Chapter 2 surveys related tools and research. Chapter 3 analyses feasibility and requirements. Chapter 4 presents the pipeline, document checks, and browser workflow. Chapter 5 describes implementation. Chapter 6 reports database snapshot counts and selected transcript observations, including a Workday dry run that reached Review without final submission. Chapter 7 concludes and outlines future work. References follow IEEE numbering; annexures provide commands, evidence notes, and a glossary.")
pagebreak()

# ================= CHAPTER 2: LITERATURE SURVEY =================
chapter("2", "Literature Survey")
p("This chapter reviews selected job-application tools and language-model agent research relevant to careerOS. Comparisons are descriptive and limited to cited public materials.")
heading("2.1 Mass-Application Tools")
p("AIHawk [1] describes an automated job-search and application agent. Product features and platform support change over time, so this report avoids treating a repository snapshot or marketing description as a definitive account of current behavior. Commercial services and autofill extensions provide other points in the design space, from bulk automation to user-confirmed field entry. careerOS exposes local pipeline state and includes configurable document checks and a dry-run browser mode; this does not establish superiority over other tools.")
p("Automation raises questions about candidate consent, employer expectations, platform rules, privacy, and inaccurate answers. Dry-run mode reduces the risk of an unintended submission in that run, but submit mode is also available. The software cannot be described as always human-gated; safe operation depends on configuration and review.")
heading("2.2 Research on LLM Web Agents")
p("ReAct [2] presents interleaved reasoning and actions as an agent prompting approach; careerOS uses a tool-driven loop but does not implement or evaluate ReAct as a method. Toolformer [6] studies learning to invoke tools. WebArena [3] evaluates web agents on realistic multi-step tasks, and WorkArena [4] and WorkArena++ [5] study enterprise workflows in ServiceNow environments. These benchmarks show why one live form run should not be generalized into broad reliability. Wang et al. [7] survey LLM-based agent architectures. In careerOS, SQLite provides persistent pipeline state, the prompt carries task policy, and browser automation is the actuator layer.")
p("Operational reliability depends on the chosen model, tool availability, browser and employer-site state, quota limits, and terminal status parsing. OpenCode [8] supplies an agent runtime, while hosted models are external dependencies. The local deployment used free-tier access at the time of testing; zero cost and ongoing free access are not guaranteed.")
heading("2.3 Upstream Project and careerOS Fork")
p("The repository identifies careerOS as a fork of Pickle-Pixel's ApplyPilot [9], distributed under the GNU Affero General Public License version 3.0 [10]. The careerOS repository [11] contains downstream changes including an OpenCode backend, search/demo controls, location prompt adjustments, and Windows browser integration. Git history and source files are the primary evidence for implementation differences; this report does not claim the fork is an independent system from first principles. Attribution and license obligations remain part of the project context.")
heading("2.4 Project Positioning")
p("The engineering objective is to integrate multi-source discovery, local persistence, fit scoring, per-role document generation, configurable checks, and browser-assisted form completion in one personal workflow. A single-user observational run does not establish a broad research gap, comparative advantage, comprehensive fabrication prevention, or general platform coverage. Those claims would require a systematic literature review and controlled comparative testing.")
pagebreak()

# ================= CHAPTER 3: ANALYSIS & REQUIREMENTS =================
chapter("3", "System Analysis and Requirements")
heading("3.1 Feasibility Study")
p("Technical feasibility was demonstrated for one Windows laptop configuration using Python, SQLite, external model access, and a Chromium-family browser. Economic feasibility is conditional: the measured setup used free-tier access, but quotas and provider pricing are mutable. Operational feasibility depends on user-managed files, browser state, and employer portals. Responsible use requires review of generated answers and compliance with applicable site rules. Source inspection found an optional CAPTCHA-solving integration; it was not part of the measured dry run and should be disabled for a conservative deployment.")
heading("3.2 Functional Requirements")
bl("FR1 \u2014 Discovery: collect postings from configured sources, de-duplicate records, and persist available descriptions.")
bl("FR2 \u2014 Enrichment: attempt to retrieve fuller descriptions and employer metadata for selected jobs.")
bl("FR3 \u2014 Scoring: assign an integer fit score 1\u201310 per job against structured resume facts; persist with rubric metadata.")
bl("FR4 \u2014 Tailoring: generate job-specific resume files and run configured structure/content checks; retries and validation mode are configurable.")
bl("FR5 \u2014 Cover letters: generate job-specific letters and run formatting/style checks; these checks do not establish factual accuracy.")
bl("FR6 \u2014 Application: support browser-assisted form completion in dry-run or submit mode, with profile-driven answers and available status information.")
bl("FR7 \u2014 Eligibility: use prompt-guided location/work-mode checks and report a refusal when the agent determines a job is ineligible.")
bl("FR8 \u2014 Observability: retain job fields, generated artifact paths, status fields, and available worker logs; coverage is not a complete append-only audit record.")
bl("FR9 \u2014 Dashboard: expose pipeline state (counts, scores, statuses) without SQL.")
heading("3.3 Software Requirements")
table("Table 3.1 \u2014 Software and external service requirements", 
      [("Component", "Choice"),
       ("OS", "Windows 10/11 (tested environment; other systems not evaluated here)"),
       ("Runtime", "Python >=3.11; Node.js for MCP server; SQLite"),
       ("LLM APIs", "Configured hosted provider(s); free-tier quota availability can change"),
       ("Agent runtime", "OpenCode CLI, headless run mode"),
       ("Browser automation", "Playwright + Playwright MCP server over CDP; Chromium-family browser"),
       ("Libraries", "python-jobspy, python-dotenv, PyYAML, reportlab/docx2pdf, python-docx")])
heading("3.4 Hardware Requirements")
p("Any modern laptop: quad-core CPU, 8 GB RAM, ~1 GB free disk, broadband internet. Development and testing used a Windows 11 laptop with a Chromium-family browser (Brave).")
pagebreak()

# ================= CHAPTER 4: DESIGN =================
chapter("4", "System Design and Methodology")
heading("4.1 Architecture Overview")
p("careerOS is organized as six batch stages around a local SQLite jobs table, followed by an optional browser-agent stage (Fig. 4.1). The CLI exposes stage commands and demonstration limits; the database stores job state and output paths, while generated files and worker logs live on disk. Configuration is held in user-managed environment, profile, and search files. Persistence is local-first, not fully local: candidate and job content may be sent to the configured model service and employer endpoints.")
figure("fig1_architecture.png", 6.30, "Fig. 4.1. careerOS architecture and data boundaries. Job state is stored in one SQLite jobs table; files and worker logs are external to that table.")
p("Design goals include retaining enough state to resume stages, using replaceable model and browser components, keeping personal configuration under user control, and adding checks around generated content. These goals are bounded by external service availability, validation mode, and user review. The database is not a complete audit log, and hosted model requests are not confined to the local machine.")
heading("4.2 Stage Design")
p("Stage 1 \u2014 Discover: JobSpy [12] queries configured job boards, while the Workday module calls employer career-site CXS endpoints. The inspected database contains 731 unique job URLs: 645 records tagged with the Workday API strategy and 86 with JobSpy. The site field contains 18 labels, many of which identify individual employers; these are not 18 independent job boards.")
p("Stage 2 \u2014 Enrich: the system can fetch fuller job descriptions and application URLs; browser rendering is available for supported pages. Successful enrichment is a data-completeness step, not proof that a job is eligible or that an employer accepts automation.")
p("Stage 3 \u2014 Score: an LLM assigns each selected job a 1\u201310 fit score against candidate and search information. The score is parsed and stored; it is a model output, not a human-validated relevance label. The configured threshold determines which jobs are selected for downstream tailoring.")
p("Stage 4 \u2014 Tailor: for selected jobs, the LLM rewrites the resume. The result passes through the configured checks described in Section 4.3; the LLM judge runs only outside lenient mode. Retry behavior is configurable in source. Accepted files can be exported to PDF.")
p("Stage 5 \u2014 Cover: cover letters are generated and checked for formatting/style issues; their checker does not compare every claim against profile evidence. Stage 6 \u2014 PDF: generated documents can be converted and filed.")
heading("4.3 Resume and Cover-Letter Checks")
p("careerOS includes several document checks, but they do not prove that every generated statement is true. Resume generation applies deterministic JSON-field checks for required fields, selected preserved companies/school, a limited skills watch-list, formatting, and boilerplate. A separate prompt-based LLM judge runs in normal and strict modes, but is skipped in lenient mode. In lenient mode, banned-word checking is also disabled. Cover-letter checks do not compare each factual claim with the candidate profile. Table 4.1 summarizes this limited coverage.")
table("Table 4.1 \u2014 Document risks and checks present in source",
      [("Artifact / risk", "Implemented check", "Coverage limit"),
       ("Resume structure", "Required fields; selected school/company checks", "No general semantic entailment or complete metric audit"),
       ("Resume skill additions", "Limited watch-list and profile skill boundary", "Watch-list is incomplete; mode matters"),
       ("Resume factual rewrite", "Optional prompt-based LLM judge", "Heuristic judge; skipped in lenient mode"),
       ("Cover-letter claims", "Formatting, phrase, punctuation and optional length checks", "No factual-claim comparison with profile")])
p("Figure 4.2 shows the implemented validation flow. The resume judge is a model, not a formal fact checker; its prompt tolerates some minor stretches. The reviewed artifact sidecars report validation_mode=lenient and judge=SKIPPED, so the files passed configured static checks only. This report does not claim comprehensive fabrication prevention or a verified 100% truth rate.")
figure("fig3_validator.png", 6.15, "Fig. 4.2. Implemented document-check flow, including the lenient-mode judge bypass and lack of factual-claim verification for cover letters.")
heading("4.4 Browser-Assisted Application Worker")
p("The apply worker combines an agent runtime (OpenCode [8] in the observed fork configuration), browser connection (Playwright MCP [13] and Chrome DevTools Protocol), policy prompt, selected job, and generated documents. The browser interacts with real employer portals, which increases both capability and the consequences of incorrect or unauthorized actions.")
p("The intended workflow (Fig. 4.3) checks location/work arrangement, enters the form, reviews visible fields, and follows either dry-run or submit mode. Dry-run instructions prohibit clicking final Submit. In submit mode, the source prompt authorizes submission after the agent's review; human approval is therefore configurable, not guaranteed. Eligibility handling is prompt-guided rather than a deterministic gate. The database stores status fields but has no dedicated append-only apply_attempts table; evidence may instead reside in worker logs.")
p("The prompt instructs the model to avoid inventing information and to follow dry-run mode. Source review also found an optional CAPTCHA-solving integration, which was not part of the measured dry run and should be disabled for conservative use. At anti-bot checks, a safer policy is to stop and request human intervention.")
bl("The prompt instructs the agent to use candidate-profile facts and avoid inventing answers.")
bl("Dry-run instructions prohibit clicking final Submit; submit mode has a different instruction.")
bl("Location handling and unsupported screening answers rely on model interpretation of the prompt and visible posting.")
bl("The source includes an optional anti-bot/CAPTCHA-solving path; this report does not endorse or claim it as evaluated behavior.")
figure("fig4_apply_flow.png", 6.25, "Fig. 4.3. Browser-assisted form workflow and mode-dependent final action; the observed dry run stopped at Review.")
heading("4.5 Worker Isolation Model")
p("Apply runs use per-worker directories for configuration, prompts, and selected documents, alongside a browser profile whose state can persist between runs. This separation organizes worker inputs, but should not be interpreted as a security sandbox: the browser session may hold authenticated state, and the agent can interact with live sites. Configuration and browser persistence are useful operational features that also require careful access control and cleanup.")
heading("4.6 The LLM Layer")
p("The system uses LLM calls for scoring and document generation, an optional prompt-based LLM judge for tailored resumes, and a long-horizon browser agent. Deterministic parsing and static rules surround some model outputs, but they do not make the underlying scores or judgments deterministic. Provider and model selection are deployment-dependent; model availability, tool-calling behavior, and quotas may change.")
p("The code includes retry/backoff and checkpoint mechanisms in selected stages. These can reduce interruption impact, but do not guarantee exact resumption for every failure or prevent a provider quota from blocking a run.")
heading("4.7 Database Schema and Persistence")
p("The inspected SQLite schema is centered on one jobs table keyed by URL. It stores discovery/enrichment fields, score and reasoning, resume/cover-letter file paths, and application status/error/count/timing fields. Generated files, validator sidecars, and worker transcripts are stored on disk. The schema does not define separate resumes, cover_letters, or apply_attempts tables, so database row associations must be distinguished from unique artifact files and log observations.")
pagebreak()

# ================= CHAPTER 5: IMPLEMENTATION =================
chapter("5", "Implementation")
heading("5.1 Technology Stack")
p("The implementation uses Python, SQLite, JobSpy for selected boards, a Workday CXS client, external language-model APIs, and Chromium-family browser automation through Playwright MCP. The apply runtime can be configured through the OpenCode CLI in this fork. The source repository is github.com/shashank-tomar0/careerOS; the local checkout's Git remote identifies the upstream ApplyPilot repository at github.com/Pickle-Pixel/ApplyPilot. The report uses careerOS for the evaluated fork and ApplyPilot for upstream; confirm naming conventions with the course guide. Provider names, quotas, model behavior, and browser support are deployment settings rather than codebase guarantees.")
heading("5.2 Key Implementation Decisions")
p("Implementation decisions include a CLI for individual stages; profile-driven prompt assembly; local SQLite persistence; configurable model providers; and persistent browser profiles for supported sessions. Worker artifacts and logs are stored outside the database. Result parsing uses a textual protocol, but transcripts are not an append-only event store and cannot guarantee a complete independently verifiable record of every action.")
heading("5.3 Command Surface and Human Interaction Model")
p("The CLI exposes health checks, pipeline stages, status, and dashboard commands. Stage boundaries allow inspection when the workflow is run interactively. The apply command also supports submit mode, so the software does not guarantee approval before each final submission. The demonstration instructions below use dry-run; if a real submission is considered, review the employer's Review page manually and follow applicable rules.")
pagebreak()

# ================= CHAPTER 6: TESTING & RESULTS =================
chapter("6", "Testing and Results")
heading("6.1 Setup and Evidence")
p("The evaluation combines a read-only inspection of the local SQLite snapshot and generated-file directory with selected worker transcripts. The observed setup used a Windows laptop, Chromium-family browser, and hosted model access. Counts below are database snapshot values unless labeled as transcript observations; this is not a controlled benchmark.")
heading("6.2 Discovery Results")
p("The inspected database contained 731 distinct job URLs: 645 records tagged with the Workday API strategy and 86 with JobSpy. The site field contains 18 labels, including employer names and aggregator labels, so these are not 18 independent job boards. Figure 6.1 separates acquisition strategy from the largest site labels.")
figure("fig2_data_provenance.png", 6.25, "Fig. 6.1. Local database snapshot: acquisition strategies and largest stored source labels; employer labels are not independent job boards.")
table("Table 6.1 \u2014 Largest stored source labels in the snapshot",
      [("Source label", "Rows", "Share"),
       ("Thomson Reuters", "230", "31.5%"),
       ("Cisco", "103", "14.1%"),
       ("Moderna", "85", "11.6%"),
       ("Mastercard", "76", "10.4%"),
       ("Motorola Solutions", "75", "10.3%"),
       ("indeed", "72", "9.8%"),
       ("Salesforce", "35", "4.8%"),
       ("linkedin", "14", "1.9%")])
heading("6.3 Scoring Results")
p("Forty-eight job records had scores in the snapshot: 17 scored 1\u20133, 18 scored 4\u20136, and 13 scored 7\u20139. Thus, 13/48 (27.1%) meet a score threshold of at least 7. This is a distribution of model-assigned scores, not a precision or validated relevance rate; no independent human-rating labels were available.")
figure("fig5_scores.png", 5.90, "Fig. 6.2. Database-derived fit-score histogram. The dashed line marks the configured threshold; no ground-truth relevance labels were available.")
heading("6.4 Document Generation Results")
p("Nine job rows reference tailored-resume paths and nine reference cover-letter paths. These resolve to seven distinct paths for each document type in the inspected directories, reflecting shared filenames across rows. The resume sidecars report validation_mode=lenient and judge=SKIPPED, so the resumes passed configured static checks only. The report does not claim each factual statement in any generated document was independently verified.")
heading("6.5 Apply Outcomes")
p("The SQLite schema stores current application status on job rows, not as a dedicated attempt-history table. In the inspected snapshot, 725 rows had no apply status and six were marked failed. Separately, the Cisco worker transcript records the application reaching Review with the final Submit control left untouched. The user-supplied screenshot shows an earlier in-progress state and is not used as evidence of completion. Two eligibility refusals are documented in worker logs. These evidence sources are kept distinct in Table 6.2.")
table("Table 6.2 \u2014 Evidence sources and observed application state",
      [("Evidence source", "Observation", "Interpretation"),
       ("SQLite snapshot", "725 status unset; 6 failed; no success status", "Current job state, not full attempt history"),
       ("Cisco worker transcript", "Reached Review; Submit untouched", "One dry-run completion observed"),
       ("User-supplied screenshot", "Intermediate dashboard state: APPLYING", "Not proof of completion"),
       ("Worker transcripts", "Two eligibility refusals described", "Log observations, not DB attempt rows"),
       ("Successful real submissions", "None evidenced in reviewed sources", "No submission or hiring outcome claimed")])
p("The transcripts describe refusals for an onsite Massachusetts role and a role involving relocation. These are case observations, not evidence of a measured refusal rate or general policy correctness. Resume artifacts used lenient validation; their sidecars do not show an LLM judge pass. The optional CAPTCHA solver and configurable submit mode remain safety concerns and should be disabled or guarded for a conservative demonstration.")
figure("fig6_outputs.png", 6.25, "Fig. 6.3. Snapshot outputs. Database associations, distinct artifact paths, current status fields, and transcript observations are reported separately.")
heading("6.6 Observability")
p("The inspected SQLite database records current job state, artifact paths, and selected application status fields. Worker transcripts provide additional action-level details but are incomplete and contain sensitive personal information; they should be redacted before sharing. The available evidence does not support reliable historical stage timing measurements, so timing claims are omitted.")
heading("6.7 Failure Modes and Mitigations")
p("Observed operational issues include provider quota limits, browser-tool startup timing, LLM output parsing, dynamic form widgets, and dependence on employer portal availability. Source code includes retries, explicit tool configuration, and browser scripting fallbacks, but residual failure rates were not measured under controlled conditions. The optional CAPTCHA integration and submit mode are separate safety decisions, not resolved reliability issues.")
table("Table 6.3 \u2014 Feature comparison with existing tools",
      [("Capability", "AIHawk [1]", "Other tools", "careerOS"),
       ("Workflow", "See cited repository", "Vendor/product dependent", "Job discovery through browser-assisted form workflow"),
       ("Resume checks", "Not compared here", "Not compared here", "Rule checks; judge depends on mode"),
       ("Eligibility", "Not compared here", "Not compared here", "Prompt-guided; policy is configurable"),
       ("Browser workflow", "See [1]", "Product dependent", "Dry-run and submit modes"),
       ("Persistence / cost", "See [1]", "Product dependent", "Local SQLite and files; model access may change")], sizes=9)
heading("6.8 Threats to Validity")
p("Internal validity is limited by artifact reuse, mutable external services, and one observational run. The score threshold has no human-labeled ground truth; the reviewed resume artifacts used lenient mode; and cover-letter checks do not verify facts. External validity is limited to one profile, one workstation, selected job sources, and one employer portal flow. Reaching Review in dry-run mode measures form-completion progress, not successful submission or hiring. The database stores current job state, while transcript coverage is incomplete. Source inspection also found a CAPTCHA-solving integration despite earlier report text claiming circumvention was out of scope; this narrows any safety conclusion.")
table("Table 6.4 \u2014 Measured stage outputs",
      [("Stage", "Output", "Measured"),
       ("Discover", "unique job URLs in DB", "731"),
       ("Score", "scored rows; score >= 7", "48; 13 (27.1%)"),
       ("Tailor", "DB rows / distinct paths", "9 / 7"),
       ("Cover", "DB rows / distinct paths", "9 / 7"),
       ("Apply", "transcript observations", "one dry run at Review; two refusals")])
pagebreak()

# ================= CHAPTER 7: CONCLUSION =================
chapter("7", "Conclusion and Future Work")
heading("7.1 Conclusion")
p("This report documents careerOS as an engineering integration for job discovery, fit scoring, tailored-document generation, and browser-assisted application preparation. The inspected snapshot contains 731 job URLs and 48 scores. A separate Cisco Workday transcript records a dry run reaching Review without final submission; other transcripts describe two eligibility refusals. The evidence does not establish comprehensive factual verification, successful submission, hiring effectiveness, or general agent reliability. Follow-up work should strengthen responsible-use controls, preserve auditable per-attempt evidence, and evaluate document claims under clearly specified validation modes. careerOS remains an attributed ApplyPilot fork under AGPL-3.0.")
heading("7.2 Future Work")
bl("Safety: disable CAPTCHA solving, default to dry-run, and require an explicit human approval step before final submission.")
bl("Integrity: improve factual comparison, record validation mode and judge result with each artifact, and evaluate false positives and false negatives on labeled examples.")
bl("Observability: persist per-attempt events and redact personal data from logs before sharing.")
bl("Evaluation: test multiple profiles, portals, and model configurations; compare fit scores with human ratings and report failures.")
bl("Coverage: add ATS integrations only where permitted and document supported flows and stop conditions.")
pagebreak()

# ================= REFERENCES =================
p("REFERENCES", 15, bold=True, align=C, space_after=10)
refs = [
    "feder-cr, \u201cJobs Applier AI Agent (AIHawk),\u201d GitHub repository. [Online]. Available: https://github.com/feder-cr/Jobs_Applier_AI_Agent_AIHawk",
    "S. Yao et al., \u201cReAct: Synergizing reasoning and acting in language models,\u201d in Proc. Int. Conf. Learn. Represent. (ICLR), 2023. [Online]. Available: https://arxiv.org/abs/2210.03629",
    "S. Zhou et al., \u201cWebArena: A realistic web environment for building autonomous agents,\u201d in Proc. Int. Conf. Learn. Represent. (ICLR), 2024. [Online]. Available: https://arxiv.org/abs/2307.13854",
    "A. Drouin et al., \u201cWorkArena: How capable are web agents at solving common knowledge work tasks?\u201d in Proc. 41st Int. Conf. Mach. Learn., Proc. Mach. Learn. Res., vol. 235, pp. 11642\u201311662, 2024. [Online]. Available: https://proceedings.mlr.press/v235/drouin24a.html",
    "L. Boisvert et al., \u201cWorkArena++: Towards compositional planning and reasoning-based common knowledge work tasks,\u201d in Adv. Neural Inf. Process. Syst., vol. 37, pp. 5996\u20136051, 2024. [Online]. Available: https://proceedings.neurips.cc/paper_files/paper/2024/file/0b82662b6c32e887bb252a74d8cb2d5e-Paper-Datasets_and_Benchmarks_Track.pdf",
    "T. Schick et al., \u201cToolformer: Language models can teach themselves to use tools,\u201d in Adv. Neural Inf. Process. Syst., vol. 36, 2023. [Online]. Available: https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html",
    "L. Wang et al., \u201cA survey on large language model based autonomous agents,\u201d Front. Comput. Sci., vol. 18, no. 6, Art. no. 186345, 2024, doi: 10.1007/s11704-024-40231-1.",
    "OpenCode, \u201cOpenCode documentation,\u201d [Online]. Available: https://opencode.ai/docs/",
    "Pickle-Pixel, \u201cApplyPilot,\u201d GitHub repository, AGPL-3.0. [Online]. Available: https://github.com/Pickle-Pixel/ApplyPilot",
    "Free Software Foundation, \u201cGNU Affero General Public License, version 3,\u201d Nov. 2007. [Online]. Available: https://www.gnu.org/licenses/agpl-3.0.html",
    "S. Tomar, \u201ccareerOS,\u201d GitHub repository (fork of ApplyPilot), AGPL-3.0. [Online]. Available: https://github.com/shashank-tomar0/careerOS",
    "c. watson, \u201cJobSpy,\u201d GitHub repository. [Online]. Available: https://github.com/cullenwatson/JobSpy",
    "Microsoft, \u201cPlaywright documentation,\u201d [Online]. Available: https://playwright.dev/docs/intro",
]
for i, r in enumerate(refs, 1):
    p(f"[{i}] {r}", 11, space_after=4, align=J)
pagebreak()

# ================= ANNEXURES =================
p("ANNEXURE A \u2014 DEMONSTRATION COMMANDS", 14, bold=True, align=C, space_after=10)
p("Use only after reviewing current platform terms and generated answers. Keep CAPTCHA-solving integrations disabled, prefer dry-run, and require human review before submission.", 12)
for c_ in ["applypilot doctor", "applypilot run discover --limit 2", "applypilot run enrich --limit 2 --workers 2",
           "applypilot run score --limit 4", "applypilot run tailor --validation lenient --limit 2",
           "applypilot run cover --validation lenient --limit 2", "applypilot run pdf --limit 2",
           "applypilot status", "applypilot dashboard", "applypilot apply --dry-run --limit 1"]:
    p("> " + c_, 11, align=L, space_after=3)
pagebreak()
p("ANNEXURE B \u2014 EVIDENCE SUMMARY", 14, bold=True, align=C, space_after=10)
p("Reviewed evidence summary: one Cisco Workday worker transcript reached the Review stage with the final Submit button untouched. Two other worker logs record eligibility refusals. These are transcript observations, not database attempt-history rows; personal details and raw transcripts are intentionally omitted.", 12)
pagebreak()
p("ANNEXURE C \u2014 GLOSSARY", 14, bold=True, align=C, space_after=10)
for k, v in [("Workday", "Cloud enterprise platform whose career portals are used by some employers for job applications."),
             ("Easy Apply", "LinkedIn's one-click application flow."),
             ("Fit score", "LLM-assigned 1\u201310 rating of job-candidate match based on the supplied prompt and profile."),
             ("Dry run", "Application workflow mode that instructs the agent to stop before final submission."),
             ("Generator-critic", "Pattern where generated content is checked against selected constraints; checks are not necessarily independent or comprehensive."),
             ("CDP", "Chrome DevTools Protocol \u2014 low-level browser control channel used as automation fallback."),
             ("Free tier", "Provider-defined usage allowance that may have quotas, restrictions, or change over time.")]:
    p(k + ": " + v, 12, align=J, space_after=4)
pagebreak()
p("ANNEXURE D \u2014 EVIDENCE NOTES", 14, bold=True, align=C, space_after=10)
for t_ in ["Database snapshot inspection: 731 unique job URLs and 48 scored rows.",
           "Score distribution: 13 of 48 rows (27.1%) scored at least 7; this is not a precision measure.",
           "Output path inspection: nine job-row references and seven distinct file paths for each document type.",
           "Cisco worker transcript reached Review in dry-run mode; final Submit was left untouched.",
           "Two worker logs contain eligibility-refusal observations.",
           "Resume sidecars show lenient validation mode and a skipped LLM judge.",
           "Source audit found optional CAPTCHA-solving instructions; their use is not part of the evaluated demonstration."]: 
    p("\u2022 " + t_, 12, align=J, space_after=4)

doc.save(DIR + "ApplyPilot_Project_Report.docx")
print("careerOS final project report saved")
