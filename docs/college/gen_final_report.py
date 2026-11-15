# -*- coding: utf-8 -*-
"""FINAL DELIVERABLE: 'ApplyPilot_Report.docx' = college front matter + 20+ page
   IEEE-style research paper body (the report IS the research paper)."""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

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

def chapter(text, size=16):
    return p(text, size=size, bold=True, align=C, space_after=14)

def pagebreak():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

def set_cell(cell, text, size=9, bold=False, align=None):
    cell.text = ""; par = cell.paragraphs[0]
    if align: par.alignment = align
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold

# ================= FRONT MATTER =================
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

heading("STUDENT'S DECLARATION", 15, C)
doc.add_paragraph()
p("We hereby declare that the work being presented in this report entitled \u201c" + TITLE + "\u201d is an authentic record of our own work carried out under the supervision of [Dr./Mr./Ms.] [MENTOR NAME]. The matter embodied in this report has not been submitted by us for the award of any other degree.")
doc.add_paragraph()
p("Dated:", 12, align=L)
p("\t\t\t\t\t\tSignature of student(s)", 12, align=L)
p("\t\t\t\t\t\t(Name: Shashank Tomar)", 12, align=L)
p("\t\t\t\t\t\tDepartment: Computer Science & Engineering", 12, align=L)
pagebreak()

heading("CERTIFICATE", 15, C)
doc.add_paragraph()
p("This is to certify that project report entitled \u201c" + TITLE + "\u201d which is submitted by Shashank Tomar in partial fulfillment of the requirement for the award of degree B. Tech. in Department of Computer Science & Engineering of Dr. A.P.J. Abdul Kalam Technical University, formerly Uttar Pradesh Technical University is a record of the candidate's own work carried out by him under my supervision. The matter embodied in this thesis is original and has not been submitted for the award of any other degree.")
doc.add_paragraph()
p("Signature of Mentor", 12, align=L)
p("(Name: [GUIDE NAME])", 12, align=L)
p("(Designation: [DESIGNATION])", 12, align=L)
p("(Computer Science & Engineering Department)", 12, align=L)
pagebreak()

heading("ACKNOWLEDGEMENT", 15, C)
doc.add_paragraph()
p("It gives us a great sense of pleasure to present the report of the B. Tech. Mini Project undertaken during B. Tech. Fifth Semester. We owe special debt of gratitude to [Dr./Mr./Ms.] [MENTOR NAME], Department of Computer Science & Engineering, ABESEC Ghaziabad for constant support and guidance throughout the course of our work.")
p("We also take the opportunity to acknowledge the contribution of Prof. (Dr.) Pankaj Kumar Sharma, Head, Department of Computer Science & Engineering, ABESEC Ghaziabad for his full support and assistance during the development of the project.")
p("We also do not like to miss the opportunity to acknowledge the contribution of all faculty members of the department for their kind assistance and cooperation during the development of our project. Last but not the least, we acknowledge our friends for their contribution in the completion of the project.")
doc.add_paragraph()
p("Signature:\t\t\t\t\tSignature:", 12, align=L)
p("Name:\t\t\t\t\tName:", 12, align=L)
p("Roll No.:\t\t\t\t\tRoll No.:", 12, align=L)
p("Date:\t\t\t\t\tDate:", 12, align=L)
pagebreak()

heading("ABSTRACT", 15, C)
doc.add_paragraph()
p("Automated job application is dominated by either mass-submission bots that misrepresent candidates or closed commercial services. This report presents ApplyPilot (deployed by the author as a personal careerOS fork), a free-tier, locally-run pipeline that couples large language model (LLM) agents with an honesty-enforcement architecture to automate the full application lifecycle: multi-board discovery, enrichment, fit scoring, resume tailoring, cover-letter generation, and autonomous submission through the employer's own career portal. We introduce a generator-critic honesty validator that rejects any resume content not evidenced by the candidate's verified facts, an eligibility gate that refuses jobs the candidate cannot take, and a structured verdict protocol that makes every agent action auditable. On a live deployment targeting an India+remote search profile, the system discovered 731 unique postings from eight sources, scored 48 jobs against structured resume facts (a discriminating 1\u20139 distribution, 18.8% scoring \u22657), produced nine validator-approved tailored resumes and five cover letters, and completed an end-to-end autonomous application on a live Workday portal \u2014 creating the candidate account, navigating all form pages, uploading the tailored resume, and stopping at the Review step in dry-run mode \u2014 while autonomously refusing two ineligible postings after verifying eligibility against the employers' own APIs. The report is organised as an IEEE-style research paper followed by annexures.", italic=True)
pagebreak()

heading("TABLE OF CONTENTS", 15, C)
for t_ in ["ABSTRACT", "LIST OF FIGURES", "LIST OF TABLES", "ABBREVIATIONS",
           "1. INTRODUCTION", "2. RELATED WORK", "3. SYSTEM ARCHITECTURE",
           "4. THE HONESTY VALIDATOR", "5. THE AUTONOMOUS APPLY AGENT",
           "6. EVALUATION", "7. DISCUSSION AND ETHICAL CONSIDERATIONS",
           "8. CONCLUSION AND FUTURE WORK", "ACKNOWLEDGMENT OF OPEN-SOURCE HERITAGE",
           "REFERENCES", "ANNEXURE A \u2014 DEMONSTRATION COMMANDS",
           "ANNEXURE B \u2014 SAMPLE AGENT VERDICTS", "ANNEXURE C \u2014 GLOSSARY"]:
    p(t_, 12, align=L, space_after=2)
pagebreak()
heading("LIST OF FIGURES", 14)
for f_, d_ in [("Fig. 1", "ApplyPilot architecture"),
               ("Fig. 2", "Top discovery sources (731 postings)"),
               ("Fig. 3", "Apply-agent workflow"),
               ("Fig. 4", "Fit-score distribution of 48 scored jobs"),
               ("Fig. 5", "Measured pipeline funnel (log scale)")]:
    p(f"{f_}\t{d_}", 12, align=L, space_after=3)
heading("LIST OF TABLES", 14)
for t_, d_ in [("Table I", "Apply-stage outcomes (measured)"),
               ("Table II", "Software requirements"),
               ("Table III", "Fabrication threat model and validator responses"),
               ("Table IV", "Measured stage outputs")]:
    p(f"{t_}\t{d_}", 12, align=L, space_after=3)
heading("ABBREVIATIONS", 14)
for k, v in [("LLM", "Large Language Model"), ("ATS", "Applicant Tracking System"),
             ("CDP", "Chrome DevTools Protocol"), ("MCP", "Model Context Protocol"),
             ("CLI", "Command-Line Interface"), ("API", "Application Programming Interface"),
             ("SaaS", "Software as a Service"), ("AGPL", "Affero GNU General Public License"),
             ("SSO", "Single Sign-On"), ("XML", "Extensible Markup Language")]:
    p(f"{k}\t\u2013 {v}", 12, align=L, space_after=2)
pagebreak()

# ================= PAPER BODY (two-column IEEE) =================
new_sec = doc.add_section(WD_SECTION.CONTINUOUS)
new_sec.top_margin = Inches(0.8); new_sec.bottom_margin = Inches(0.8)
new_sec.left_margin = Inches(0.65); new_sec.right_margin = Inches(0.65)
cols = new_sec._sectPr.find(qn("w:cols"))
cols.set(qn("w:num"), "2"); cols.set(qn("w:space"), str(int(14*20)))
st2 = doc.styles["Normal"]; st2.font.name = TNR; st2.font.size = Pt(10)
st2.paragraph_format.line_spacing = 1.0

def pb(text, size=10, bold=False, italic=False, align=J, space_after=4, first_indent=0.18):
    par = doc.add_paragraph(); par.alignment = align
    par.paragraph_format.space_after = Pt(space_after); par.paragraph_format.line_spacing = 1.0
    if first_indent: par.paragraph_format.first_line_indent = Inches(first_indent)
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    return par

def pbf(text, **kw): return pb(text, first_indent=0, **kw)

def h1(text, size=10, space_before=8):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_before = Pt(space_before); par.paragraph_format.space_after = Pt(4)
    par.paragraph_format.line_spacing = 1.0
    r = par.add_run(text.upper()); r.font.name = TNR; r.font.size = Pt(size); r.bold = True
    r.font.small_caps = True
    return par

def h2(text):
    par = doc.add_paragraph(); par.alignment = L
    par.paragraph_format.space_before = Pt(6); par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.line_spacing = 1.0
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(10); r.bold = True; r.italic = True
    return par

def caption(text):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_after = Pt(8); par.paragraph_format.line_spacing = 1.0
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(9)
    return par

def figure(path, width, cap):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_after = Pt(2); par.paragraph_format.line_spacing = 1.0
    run = par.add_run(); run.add_picture(path, width=Inches(width))
    caption(cap)

def bl(text, size=10):
    par = doc.add_paragraph(style="List Bullet")
    par.paragraph_format.space_after = Pt(2); par.paragraph_format.line_spacing = 1.0
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size)
    return par

# ---- 1. INTRODUCTION ----
h1("1. Introduction")
h2("1.1 Problem Statement")
pbf("A job search for entry-level engineering roles is a volume game played against time. Recruiters on major boards receive hundreds of applications per posting, and candidates respond by applying more \u2014 each application demanding discovery, fit judgement, document customisation, and manual entry into the employer's career portal. A single application to a large employer using Workday, the enterprise HR system used by more than half of the Fortune 500, involves account creation, four to six form pages, document upload, and screening questions \u2014 typically 15\u201330 minutes of transcription work that is both cognitively draining and error-prone. For a final-year student applying across dozens of employers, the process consumes weeks of productive preparation time, and repetitive manual data entry silently disqualifies candidates through transcription errors.")
pbf("At the same time, large language models (LLMs) have become capable of exactly this class of work: reading unstructured text, judging semantic fit, rewriting documents under constraints, and \u2014 as autonomous agents \u2014 operating real web interfaces through a browser. This invites a question with both technical and ethical dimensions: can a free-tier, locally-run agent honestly and safely automate the entire application lifecycle on a person's behalf?")
h2("1.2 Contributions")
pbf("This paper makes four contributions:")
bl("An architecture integrating discovery from eight sources, LLM fit scoring, honest document tailoring, and real-browser submission into one free, locally-run pipeline (Section 3).")
bl("A generator-critic honesty validator that makes fabrication a visible, logged rejection event rather than an invisible statistical risk (Section 4).")
bl("An eligibility gate and structured verdict protocol (RESULT:*) that yield auditable refusals and human decision points (Section 5).")
bl("An empirical evaluation on a live deployment \u2014 731 postings discovered, 48 scored jobs, nine approved tailored resumes, one complete autonomous Workday application with resume upload, and two observed eligibility refusals (Section 6).")
h2("1.3 Organisation of the Report")
pbf("Section 2 surveys related tools and research. Section 3 presents the architecture. Section 4 details the honesty validator. Section 5 describes the apply agent. Section 6 reports measured results. Section 7 discusses ethics and limitations, and Section 8 concludes. Annexures provide demonstration commands, sample verdicts, and a glossary.")

# ---- 2. RELATED WORK ----
h1("2. Related Work")
h2("2.1 Mass-Application Tools")
pbf("Auto_Jobs_Applier_AIHawk [7] automated LinkedIn Easy-Apply using an LLM to answer screening questions, accumulating tens of thousands of GitHub stars before platform policy enforcement curtailed much of its workflow. Its design had no independent check that LLM-generated answers were true, and no model of where the candidate is eligible to work \u2014 the two failure classes our validator (Section 4) and eligibility gate (Section 5) address. LazyApply (commercial) bulk-submits a fixed resume across boards; Simplify (extension) autofills from a stored profile under human control; matching-as-a-service products (e.g., Sonara, since shut down) demonstrated demand for centralised solutions while illustrating their fragility.")
h2("2.2 Research on LLM Web Agents")
pbf("ReAct [1] established the reasoning\u2013acting interleaving that our apply agent executes. Toolformer [5] showed models can self-teach tool use, motivating tool-mediated integration over screen scraping. WebArena [2] benchmarks agents on realistic self-hostable web environments, finding low success rates on long-horizon form tasks; WorkArena [3] and WorkArena++ [14] extend this to ServiceNow-style enterprise portals \u2014 the same UI family as Workday \u2014 and identify form navigation among the harder capabilities. Wang et al. [4] survey the plan\u2013act\u2013observe agent architecture with memory and tools that our system instantiates in lightweight form: SQLite as episodic memory, a policy prompt as the agent's charter, and Playwright/CDP as actuators.")
h2("2.3 Research Gap")
pbf("To our knowledge, no reviewed system combines multi-board discovery, honest LLM scoring, validated document tailoring, and a real-browser autonomous apply agent in a single free, auditable, locally-run deployment with published refusal behaviour. The upstream ApplyPilot project [8] provided the staged pipeline skeleton under AGPL-3.0 [13]; the author's careerOS fork [9] contributes the free-tier agent backend, India-aware eligibility rules, robustness fixes, and the empirical evaluation reported here, remaining AGPL-3.0 with attribution per the licence.")

# ---- 3. ARCHITECTURE ----
h1("3. System Architecture")
h2("3.1 Design Principles")
pbf("Four principles shaped the architecture. (1) Local-first: all data \u2014 the profile, the database, the documents \u2014 lives on the candidate's machine; nothing is sent to third parties beyond the LLM APIs and the employers' own career endpoints. (2) Checkpoint everything: every stage writes its output to a SQLite store, making the pipeline resumable and auditable. (3) Free-tier operational: the system must run without any paid API; this constrains model choice, rate handling, and prompt budgets. (4) Honesty as architecture, not aspiration: integrity mechanisms are separate, testable components with logged behaviour.")
h2("3.2 Stage Pipeline")
pbf("ApplyPilot is organised as six idempotent batch stages around a single SQLite checkpoint database, followed by an interactive agent stage (Fig. 1). Each stage is independently runnable from the CLI (applypilot run <stage>), resumable after interruption, and carries optional --limit flags for controlled demonstrations. Stage 1, Discover, scrapes Indeed, Naukri, Glassdoor, LinkedIn and ZipRecruiter via python-jobspy [12] with an India+remote configuration, and additionally crawls employers' public Workday career-site APIs for direct application URLs; postings are de-duplicated by a company-title-URL signature. Stage 2, Enrich, fetches full descriptions for shortlisted jobs, rendering JavaScript-heavy pages with Playwright [11]. Stage 3, Score, prompts an LLM to rate each job 1\u201310 against structured resume facts under a rubric covering skills overlap, seniority, location compliance and salary floor; outputs are parsed defensively (markdown stripping, regex integer extraction) so free-tier model verbosity cannot corrupt the store. Stage 4, Tailor, rewrites the resume per role subject to Section 4's validator; Stage 5, Cover, generates cover letters under the same regime; Stage 6, PDF, converts approved documents. The Apply agent (Section 5) operates one job at a time in a real browser.")
figure(DIR+"fig1_pipeline.png", 3.1, "Fig. 1. ApplyPilot architecture: six batch stages around a SQLite checkpoint store, plus the interactive apply agent (red) with the honesty validator (yellow) supervising document generation.")
h2("3.4 Worker Isolation Model")
pbf("Each apply run executes inside an isolated worker: a per-worker working directory (apply-workers/worker-N) holding the agent's configuration, the job prompt, and the tailored documents, plus a persistent browser profile directory that is deliberately not reset between jobs. The working directory is cleaned and rebuilt per run (so agent side-effects cannot accumulate), while browser state (cookies, logins) persists so that a one-time human login on a walled board remains reusable. The agent runs headless (opencode run --auto --standalone) with its MCP browser config written per worker, pointing at the CDP debug port of a browser instance the pipeline launches itself. This isolation model yields three properties: reproducibility (same inputs, same environment), safety (the agent cannot mutate the host configuration), and observability (every run leaves a worker log feeding the audit trail.)")
h2("3.5 Configuration and Data Model")
pbf("Configuration is three user-owned files: .env (API keys), profile.json (verified candidate facts: employers, projects, skills, metrics, education, salary floor, work-mode constraints, contact details), and searches.yaml (locations, remote preference, boards, queries, salary expectations). The database's core tables are jobs (id, site, title, company, location, description, url, fit_score, tailored_resume_path, apply_status, apply_error, apply_attempts), resumes and cover_letters (job linkage, approval status, validator report), and apply_attempts (per-run status, reason, transcript reference). The database doubles as the dashboard source (applypilot status / applypilot dashboard).")
figure(DIR+"fig4_sources.png", 2.9, "Fig. 2. Top discovery sources in the measured run (731 postings; employer Workday portals dominate over aggregators).")

# ---- 4. VALIDATOR ----
h1("4. The Honesty Validator")
h2("4.1 Threat Model")
pbf("The validator answers the central ethics question of auto-apply systems: what may an agent say on a person's behalf? Our answer: only what the person could truthfully say, verified mechanically. We formalise the fabrication threat model in Table III: three fabrication classes, each with a detection strategy and an observed example from the deployment.")
caption("TABLE III. FABRICATION THREAT MODEL AND VALIDATOR RESPONSES")
t3 = doc.add_table(rows=4, cols=3); t3.style = "Table Grid"; t3.alignment = WD_TABLE_ALIGNMENT.CENTER
rows3 = [("Fabrication class", "Detection strategy", "Observed example"),
         ("Entity invention", "Compare named employers/projects against profile facts", "Hallucinated project and employer references caught in early drafts"),
         ("Metric inflation", "Extract numbers; compare against evidenced metrics", "Invented CGPA value removed after validator objection"),
         ("Capability inflation", "Skills boundary: listed skills may be discussed; unknown may not be claimed", "Out-of-bound skill claims rejected; listed C++/Rust correctly allowed")]
for i, row in enumerate(rows3):
    for j, v in enumerate(row): set_cell(t3.cell(i, j), v, bold=(i == 0))
h2("4.2 Generator-Critic Loop")
pbf("Design. The validator holds a watch-list of fabrication-prone patterns derived from the candidate's verified resume facts. For each LLM-generated document it (a) extracts claims, (b) compares named entities and metrics against profile.json, (c) permits re-organisation and de-emphasis of true content but rejects addition of anything unevidenced, and (d) enforces a skills boundary with normalisation guards to prevent false positives on legitimately listed skills. Rejected documents return to the LLM with structured objections (which sentence, which claim, why), with up to five revision attempts before the job is flagged for human review. This turns fabrication from an invisible statistical risk into a visible, logged rejection event, and yields natural metrics \u2014 validator acceptance rate and an objection taxonomy \u2014 which we intend to evaluate adversarially in future work.")

h2("4.3 Validator Algorithm")
pbf("The validation procedure is deliberately deterministic so that identical documents always receive identical verdicts. The steps are: (1) normalise the document text (case, whitespace, entity aliases); (2) segment into claims — sentences containing a named entity, a number, or a skill term; (3) for each claim, resolve entities against the profile's verified sets (employers, projects, education, metrics, skills); (4) classify each unresolved entity as: paraphrase (allowed), omission-context (allowed), or invention (rejected); (5) enforce the skills boundary: any skill term not in the profile's skills set and not a generic term is rejected, with normalisation guards for legitimately listed skills; (6) if any claim is rejected, compose a structured objection (sentence index, entity, reason class) and return the document to the generator; (7) accept only when zero claims are rejected, writing the validator report alongside the document. Deterministic rejection makes the audit trail meaningful: a human can inspect exactly which sentence violated which rule, and the objection taxonomy becomes a measurable property of the system.")
pbf("Observed behaviour. During the deployment the validator rejected early tailored drafts containing a hallucinated CGPA value and an invented project reference, and initially produced a false positive on the candidate's listed skill C++ (flagged as generic-text pattern); the skills-boundary normalisation guard corrected this, after which all nine tailored resumes and five cover letters passed. The false positive and its fix are recorded in the fork's commit history — an example of the audit-first engineering approach this project takes.")

# ---- 5. AGENT ----
h1("5. The Autonomous Apply Agent")
h2("5.1 Runtime and Browser Bridge")
pbf("The apply stage launches an LLM agent per job (OpenCode CLI [10] running a free hosted model such as GLM or Gemini Flash) with three assets: a policy prompt built from profile.json with hard rules; a browser toolset \u2014 a Playwright MCP server [11] driving the candidate's own Chromium-family browser over the Chrome DevTools Protocol (CDP) on a debug port, with raw-CDP script fallback for steps the MCP tools cannot express; and the tailored documents. The worker's browser profile persists across jobs, so a one-time human login on a walled board is reusable while the agent never sees credentials.")
h2("5.2 Policy Prompt and Eligibility Gate")
pbf("The prompt enforces: true facts only from the profile; relocation None must be reported as None, never guessed; an eligibility check first \u2014 read the posting and the employer's own API where necessary, and if the job is onsite-only outside the candidate's country or otherwise ineligible, output RESULT:FAILED:not_eligible_location and stop before any form work; salary answers from the posting's own range and the profile floor, never invented; currency-aware formatting; and dry-run discipline \u2014 in dry-run mode the agent must not click the final Submit. Representative prompt rules, quoted from the implementation:")
bl("\u201cNever invent information not in the profile. If you don't know something, answer honestly (e.g., 'None') rather than guessing.\u201d")
bl("\u201cThe candidate is based in {primary_city}, {candidate_country}. Remote or work-from-anywhere \u2192 ELIGIBLE. Onsite only in a different country with no remote option \u2192 NOT ELIGIBLE.\u201d")
bl("\u201cDo NOT click the final Submit button (dry-run). Complete and verify the application form; the candidate makes the submission decision.\u201d")
bl("\u201cYour browser tools are the MCP playwright tools (tools.playwright.*), already connected to a real Chrome with remote debugging. Never conclude that no browser is available without calling them first.\u201d")
h2("5.3 Structured Verdict Protocol")
pbf("Every run terminates with a machine-readable verdict (RESULT:APPLIED | RESULT:FAILED:<reason>) recorded in apply_attempts, producing a complete audit trail per application. In dry-run mode the agent stops at the Review page and saves the draft; in submit mode it clicks Submit and verifies. Fig. 3 shows the workflow.")
figure(DIR+"fig5_agent.png", 3.1, "Fig. 3. Apply-agent workflow: eligibility gate before any form work, truthful field entry, and mode-dependent termination (submit vs. dry-run) with structured verdicts.")

h2("5.4 Verdict Taxonomy")
pbf("The protocol distinguishes success, eligibility refusal, and system failure: APPLIED (real submit verified), APPLIED dry-run (draft saved at Review), FAILED:not_eligible_location (agent refused after verification), FAILED:sso_required or indeed_login_wall (employer login wall; agent stops safely), FAILED:browser_unavailable (no browser attached; retried next run), FAILED:no_result_line (agent terminated without a verdict; retried). Because every outcome is persisted with its reason and worker transcript, the apply stage can be replayed and audited — an operational property that generic auto-apply bots do not offer.")

# ---- 6. EVALUATION ----
h1("6. Evaluation")
h2("6.1 Setup")
pbf("We evaluate a live deployment on the author's own resume (B.Tech CSE student, India, remote-preferring, salary floor configured). All numbers are read from the production SQLite store, not a simulation. The environment: Windows 11 laptop, Chromium-family browser, free-tier LLM APIs (Gemini Flash; OpenCode-hosted GLM as the agent default).")
h2("6.2 Discovery Results")
pbf("The pipeline stored 731 unique postings across eight sources; employer Workday portals dominated (Fig. 2): Thomson Reuters postings aggregated on boards contributed 230, Cisco 103, Moderna 85, Mastercard 76, Motorola Solutions 75, and direct Indeed results 72, with the remainder from Salesforce, LinkedIn, Ciena and others. The dominance of employer-native portals validates the Workday-first apply strategy: the highest-value application targets publish their own structured endpoints.")
h2("6.3 Scoring Results")
pbf("48 jobs were scored under the free-tier configuration. The distribution (Fig. 4) is discriminating: a weak band at 1\u20133 (21 jobs), a marginal band at 4\u20136 (16), and a fit tail at 7\u20139 (11). 18.8% of scored jobs reached \u22657, a plausible precision-oriented threshold for expensive downstream stages. The three 9/10 postings were Cisco Software Engineer (Bangalore) roles with direct Workday application URLs \u2014 exactly the profile the apply agent handles best.")
figure(DIR+"fig2_scores.png", 2.9, "Fig. 4. Real fit-score distribution of the 48 scored jobs (author's live run). Red/amber/green encode weak/marginal/strong fit.")
h2("6.4 Document Generation")
pbf("Nine tailored resumes and five cover letters were produced and converted to PDF, all passing the honesty validator after the generator-critic loop. Observed objection classes matched the threat model: unevidenced project mentions (a hallucinated CGPA and an invented project were caught and removed in early iterations) and out-of-bound skill claims.")
h2("6.5 Apply Outcomes")
pbf("Table I summarises the measured outcomes. The culminating test ran the agent in dry-run mode against a 9/10-fit Cisco Software Engineer posting on Cisco's live Workday portal: the agent verified eligibility, created the candidate account, navigated every form page (handling dropdown and listbox widgets), uploaded the tailored resume PDF (system-confirmed upload), completed screening questions truthfully, and stopped at the Review page with a saved draft, returning RESULT:APPLIED (dry-run). Two ineligible postings were refused autonomously: an onsite-only Moderna role in Massachusetts (rejected after querying the employer's API) and a Motorola role requiring relocation that the profile forbids, where the agent reported the truthful relocation answer rather than guessing. Indeed-hosted postings requiring session login failed safely with a structured sso_required verdict rather than attempting bypass.")
caption("TABLE I. APPLY-STAGE OUTCOMES (MEASURED)")
tt = doc.add_table(rows=6, cols=3); tt.style = "Table Grid"; tt.alignment = WD_TABLE_ALIGNMENT.CENTER
rowsd = [("Outcome", "Jobs", "Verdict observed"),
         ("Dry-run completed (Workday)", "1", "RESULT:APPLIED (dry-run); draft saved at Review"),
         ("Eligibility refusal", "2", "RESULT:FAILED:not_eligible_location"),
         ("Login wall (Indeed smart apply)", ">12", "RESULT:FAILED:sso_required / indeed_login_wall"),
         ("Tailored+queued for apply", "9", "documents approved; awaiting runs"),
         ("Real submissions", "0", "held for human decision by design")]
for i, row in enumerate(rowsd):
    for j, v in enumerate(row): set_cell(tt.cell(i, j), v, bold=(i == 0), align=(C if j == 1 else None))
figure(DIR+"fig3_funnel.png", 2.9, "Fig. 5. Pipeline funnel of the measured run (log scale): discovery feeds a precision-filtered document-generation and application path, with two eligibility refusals recorded.")
h2("6.6 Failure Modes and Mitigations")
pbf("Free-tier operation surfaced three reproducible failure classes, all mitigated. (1) Quota exhaustion and 15-requests/minute rate limits on Gemini Flash, addressed by model fallback and stage-level retries with backoff. (2) Agent-browser desynchronisation, in which fast models queried for browser tools before the MCP server finished connecting \u2014 mitigated by model selection (a slower, tool-reliable default) and explicit tool-catalog hints in the prompt. (3) Verbose model output corrupting parsers, mitigated by defensive extraction. These constraints, not model intelligence, were the binding engineering limits of free-tier agentic deployment. Table IV consolidates the stage outputs.")
caption("TABLE IV. MEASURED STAGE OUTPUTS")
t4 = doc.add_table(rows=6, cols=3); t4.style = "Table Grid"; t4.alignment = WD_TABLE_ALIGNMENT.CENTER
rows4 = [("Stage", "Output", "Measured"),
         ("Discover", "unique postings stored", "731"),
         ("Score", "jobs scored", "48 (1\u20139 spread; 18.8% \u22657)"),
         ("Tailor", "approved tailored resumes", "9 (+PDFs)"),
         ("Cover", "approved cover letters", "5 (+PDFs)"),
         ("Apply", "dry-run completions / refusals", "1 / 2")]
for i, row in enumerate(rows4):
    for j, v in enumerate(row): set_cell(t4.cell(i, j), v, bold=(i == 0))
h2("6.7 Software Requirements")
pbf("Table II lists the stack. The only paid components are none: every service runs on free tiers.")
caption("TABLE II. SOFTWARE REQUIREMENTS")
t2 = doc.add_table(rows=7, cols=2); t2.style = "Table Grid"; t2.alignment = WD_TABLE_ALIGNMENT.CENTER
rows2 = [("Component", "Choice"),
         ("OS", "Windows 10/11 64-bit (Linux compatible)"),
         ("Runtime", "Python 3.13; Node.js LTS (MCP server); SQLite (bundled)"),
         ("LLM APIs", "Google Gemini (flash) free tier; OpenCode free hosted models (GLM)"),
         ("Agent runtime", "OpenCode CLI, headless run mode"),
         ("Browser automation", "Playwright + Playwright MCP server over CDP; Chromium-family browser"),
         ("Libraries", "python-jobspy, python-dotenv, PyYAML, reportlab/docx2pdf, python-docx")]
for i, row in enumerate(rows2):
    for j, v in enumerate(row): set_cell(t2.cell(i, j), v, bold=(i == 0))

# ---- 7. DISCUSSION ----
h1("7. Discussion and Ethical Considerations")
h2("7.1 Is Autonomous Applying Legitimate?")
pbf("The system submits only through forms employers publish for candidates, with only the candidate's true data, at the candidate's explicit configuration. The dry-run mode makes the human's decision the final gate; the refusal log demonstrates the agent declining, not fabricating. We argue this is materially different from both spam bots (which misrepresent) and manual applying (which wastes the human's hours on transcription).")
h2("7.2 Risks and Mitigations")
pbf("Automated submission at scale could harm employer systems or the candidate's reputation. Our design limits risk by (a) default thresholds that restrict expensive stages to high-fit jobs, (b) per-job agent runs with audit trails rather than unbounded loops, (c) refusal to bypass login walls or CAPTCHAs, and (d) an explicit human decision before any real submission. Residual risks include employer perception of automated applications \u2014 the system is designed to make each submitted application individually truthful and tailored, arguably higher-quality than the median manual submission.")
h2("7.3 Limitations")
pbf("The evaluation is a single-candidate deployment (n=48 scored, n=1 completed application); no A/B response-rate measurement yet; board coverage depends on third-party scrapers' health; and free-tier quotas make unattended daily operation bursty. These are engineering limits, not conceptual ones.")

h2("7.4 Deployment Economics")
pbf("The recurring cost of the deployment is zero. Free-tier limits (Gemini Flash: 15 requests/minute and a daily request cap; OpenCode-hosted GLM: daily quota) shape the operating rhythm rather than blocking it: batch stages are checkpointed, so a daily discover-enrich-score cycle fits comfortably within quota, while the interactive apply agent consumes a bounded number of model calls per application. For comparison, the commercial auto-apply SaaS this project replaces charges US$30\u2013240 per year for closed, unverifiable behaviour. The fork's total external dependency footprint is four free services (two LLM API providers, one agent runtime, one browser), each replaceable independently.")

# ---- 8. CONCLUSION ----
h1("8. Conclusion and Future Work")
pbf("We presented ApplyPilot/careerOS, a free-tier, locally-run LLM-agent pipeline that automates job discovery, fit scoring, honest document tailoring, and autonomous real-browser application submission, with honesty enforcement as a first-class subsystem demonstrated by live behaviour: one complete Workday application (form filled, resume uploaded, draft saved at Review) and two autonomous refusals of ineligible jobs. The contribution is both practical and methodological: an integrity architecture \u2014 verified-facts profile, generator-critic validation, eligibility gating, and structured audit verdicts \u2014 that makes personal job-application automation defensible, released under AGPL-3.0 with upstream attribution.")
pbf("Future work: session-persistent operation on login-walled boards; an outcome-tracking stage correlating tailoring strategies with employer replies; adversarial evaluation of the honesty validator; multi-candidate studies with response-rate A/B measurement; and form-semantic agent tools to reduce raw-CDP fallbacks, benchmarked against WorkArena-style task decompositions.")

h1("Acknowledgment of Open-Source Heritage")
pbf("This work builds on the AGPL-3.0 licensed ApplyPilot project by Pickle-Pixel [8]. The careerOS fork [9] credits upstream in its README and documentation, publishes all modifications, and remains available under AGPL-3.0, per the licence and the ethics of open personal automation.")

# ---- REFERENCES ----
h1("References")
refs = [
    "S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, \u201cReAct: Synergizing reasoning and acting in language models,\u201d in Proc. Int. Conf. on Learning Representations (ICLR), 2023, arXiv:2210.03629.",
    "S. Zhou et al., \u201cWebArena: A realistic web environment for building autonomous agents,\u201d in Proc. ICLR, 2024, arXiv:2307.13854.",
    "L. Boisvert et al., \u201cWorkArena: How capable are web agents at tackling commonplace knowledge work tasks?\u201d in Proc. Int. Conf. on Machine Learning (ICML), 2024, arXiv:2403.07718.",
    "L. Wang, C. Ma, X. Feng, et al., \u201cA survey on large language model based autonomous agents,\u201d Frontiers of Computer Science, vol. 18, no. 6, 2024, arXiv:2308.11432.",
    "T. Schick et al., \u201cToolformer: Language models can teach themselves to use tools,\u201d in Proc. NeurIPS, 2023, arXiv:2302.04761.",
    "feder-cr, \u201cAuto_Jobs_Applier_AIHawk,\u201d GitHub repository, 2024. [Online]. Available: https://github.com/feder-cr/AI_Hawk",
    "Pickle-Pixel, \u201cApplyPilot: A local-first autonomous job application pipeline,\u201d GitHub repository, AGPL-3.0, 2025. [Online]. Available: https://github.com/Pickle-Pixel/ApplyPilot",
    "S. Tomar, \u201ccareerOS: ApplyPilot fork for India-focused, free-tier autonomous applications,\u201d GitHub repository, AGPL-3.0, 2026. [Online]. Available: https://github.com/shashank-tomar0/careerOS",
    "OpenCode, \u201cOpenCode: terminal-based AI coding agent,\u201d 2025. [Online]. Available: https://opencode.ai",
    "Microsoft, \u201cPlaywright: Web automation and testing,\u201d 2025. [Online]. Available: https://playwright.dev",
    "Slatec LLC, \u201cJobSpy: multi-board job scraper library,\u201d 2025. [Online]. Available: https://github.com/cullenwatson/JobSpy",
    "Free Software Foundation, \u201cGNU Affero General Public License v3.0,\u201d Nov. 2007. [Online]. Available: https://www.gnu.org/licenses/agpl-3.0.html",
    "S. Zhang et al., \u201cWorkArena++: Towards compositional planning and reasoning-based common knowledge work tasks,\u201d in Proc. ACL, 2024, arXiv:2407.05265.",
]
for i, r in enumerate(refs, 1):
    par = doc.add_paragraph(); par.alignment = J
    par.paragraph_format.space_after = Pt(2); par.paragraph_format.line_spacing = 1.0
    par.paragraph_format.left_indent = Inches(0.18); par.paragraph_format.first_line_indent = Inches(-0.18)
    run = par.add_run(f"[{i}] {r}"); run.font.name = TNR; run.font.size = Pt(8.5)

# ---- ANNEXURES (single column) ----
end_sec = doc.add_section(WD_SECTION.CONTINUOUS)
end_sec.top_margin = Inches(0.9); end_sec.bottom_margin = Inches(0.9)
end_sec.left_margin = Inches(1.0); end_sec.right_margin = Inches(1.0)
cols2 = end_sec._sectPr.find(qn("w:cols")); cols2.set(qn("w:num"), "1")
doc.add_page_break()

chapter("ANNEXURE A \u2014 DEMONSTRATION COMMANDS", 14)
p("The complete system is demonstrated with the following commands (run from the project root; editable install):", 12)
for c_ in ["applypilot doctor",
           "applypilot run discover --limit 2",
           "applypilot run enrich --limit 2 --workers 2",
           "applypilot run score --limit 4",
           "applypilot run tailor --validation lenient --limit 2",
           "applypilot run cover --validation lenient --limit 2",
           "applypilot run pdf --limit 2",
           "applypilot status",
           "applypilot dashboard",
           "applypilot apply --dry-run --limit 1",
           "applypilot apply --limit 1   (real submission)"]:
    p("> " + c_, 11, align=L, space_after=3)
pagebreak()
chapter("ANNEXURE B \u2014 SAMPLE AGENT VERDICTS (WORKER LOG EXCERPTS)", 14)
p("Dry-run completion: \u201cRESULT:APPLIED (dry-run \u2014 application fully filled and saved as a draft through the Review step; final Submit intentionally not clicked per instructions. To finish, the candidate only needs to open the Workday application and click Submit.)\u201d", 12)
p("Eligibility refusal: \u201cRESULT:FAILED:not_eligible_location \u2014 job verified onsite in Massachusetts, USA with no remote option; candidate profile relocation: None.\u201d", 12)
p("Resume upload (system event): \u201cSuccessfully Uploaded!\u201d", 12)
p("Scoring tail (fit spread): \u201c9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 4 \u2026 2 \u2026 1\u201d across the 48 scored jobs.", 12)
pagebreak()
chapter("ANNEXURE D \u2014 OBSERVED RUN TIMELINE (SELECTED EVENTS)", 14)
for t_ in [
    "Pipeline scored 24 evaluation jobs in ~78 seconds under free-tier quota management.",
    "Two 9/10-fit Cisco Bangalore postings identified with direct Workday application URLs; an 8/10 kept as backup.",
    "First dry-run: agent correctly refused a Moderna posting (onsite Massachusetts) after querying the employer's API \u2014 RESULT:FAILED:not_eligible_location.",
    "Second dry-run: agent refused a Motorola Bangalore posting whose screening required relocation; profile says relocation None \u2014 truthful answer reported.",
    "Prompt audit caught and fixed a currency-format error (a $-formatted INR salary floor) and a dry-run/submit contradiction in the mission statement.",
    "Agent desynchronisation diagnosed: fast models queried browser tools before the MCP server connected; fixed by model choice plus tool-catalog hints.",
    "Culminating dry-run: full Workday flow \u2014 account created, all form pages filled (dropdown/listbox widgets handled), tailored resume uploaded (\u201cSuccessfully Uploaded!\u201d), Review page reached, draft saved, RESULT:APPLIED (dry-run).",
    "Validator false positive on listed skill C++ identified and fixed via skills-boundary normalisation guard; all documents subsequently approved."]:
    p("\u2022 " + t_, 12, align=J, space_after=4)
pagebreak()
chapter("ANNEXURE E \u2014 PROJECT REPOSITORY AND REPRODUCIBILITY", 14)
p("The complete system is published as a public AGPL-3.0 fork with full commit history:", 12)
for t_ in [
    "Repository: https://github.com/shashank-tomar0/careerOS (fork of Pickle-Pixel/ApplyPilot, AGPL-3.0).",
    "Upstream credit: README attributes the pipeline design to the upstream project per licence requirements.",
    "Fork modifications (published as individual commits): OpenCode agent backend (config, launcher, doctor); India-aware location-eligibility rules in the apply prompt; per-stage --limit demo flags; string-URL corruption fix in the discovery writer; skills-boundary normalisation guard in the honesty validator; currency-neutral salary formatting; browser-tools pinning (MCP-only) and model-reliability fixes.",
    "Configuration artefacts (user-owned, not committed): .env (API keys), profile.json (verified candidate facts), searches.yaml (search profile).",
    "Reproduction: clone the fork; pip install -e .; create ~/.applypilot/.env with a free Gemini key; run applypilot doctor; then the Annexure A stage commands.",
    "The database snapshot, worker logs, and validator reports referenced in Section 6 are retained locally and available on request for verification."]:
    p("\u2022 " + t_, 12, align=J, space_after=4)
pagebreak()
chapter("ANNEXURE F \u2014 SAMPLE GENERATED DOCUMENT EXCERPTS", 14)
p("Tailored resume excerpt (validator-approved; facts preserved, emphasis re-ordered for a software-engineer role):", 12, align=L)
p("\u201cB.Tech CSE (CGPA 8.3) | Built TalentScout-AI (500+ DAU, 99.9% uptime) and RIFT (1000+ weekly downloads); cut API latency 45% via caching and async I/O at Technoledge India internship; 400+ DSA problems; 3 hackathon placements.\u201d", 12, italic=True, align=J)
p("Cover-letter excerpt (validator-approved):", 12, align=L)
p("\u201cI build and ship backend systems in Python \u2014 my projects have served 500+ daily users with 99.9% uptime, and my internship work cut API latency by 45%. For Cisco's Software Engineer (Bangalore) role, that combination of scale-minded engineering and full-stack delivery is directly relevant.\u201d", 12, italic=True, align=J)
p("Validator report fields recorded per document: verdict, objection list (sentence index, entity, reason class), revision attempt count, final acceptance timestamp \u2014 each stored alongside the document in the SQLite store.", 12, align=J)
pagebreak()
chapter("ANNEXURE C \u2014 GLOSSARY", 14)
for k, v in [("Workday", "Enterprise HR platform whose career portal is used by most Fortune-500 employers for applications."),
             ("Easy Apply", "LinkedIn's one-click application flow."),
             ("Fit score", "LLM-assigned 1\u201310 rating of job-candidate match against verified resume facts."),
             ("Dry run", "Agent completes the application but stops before final submission."),
             ("Generator-critic", "Pattern where an LLM generates content and an independent checker rejects non-compliant output."),
             ("CDP", "Chrome DevTools Protocol \u2014 low-level browser control channel used as automation fallback."),
             ("Free tier", "Cloud API usage allowance with zero cost, subject to rate limits.")]:
    p(k + ": " + v, 12, align=J, space_after=4)

doc.save(DIR+"ApplyPilot_Report.docx")
print("REPORT SAVED: ApplyPilot_Report.docx")
