# -*- coding: utf-8 -*-
"""Generate IEEE-conference-style research paper (2-column, figures, refs) as DOCX."""
import docx
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TNR = "Times New Roman"
J = WD_ALIGN_PARAGRAPH.JUSTIFY
C = WD_ALIGN_PARAGRAPH.CENTER
DIR = "C:/Users/dell/Desktop/mini-project/docs/college/"

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.75); sec.bottom_margin = Inches(0.9)
sec.left_margin = Inches(0.65); sec.right_margin = Inches(0.65)

st = doc.styles["Normal"]; st.font.name = TNR; st.font.size = Pt(10)
st.paragraph_format.line_spacing = 1.0; st.paragraph_format.space_after = Pt(4)

def set_col_spacing(section, pts=12):
    # two columns with spacing
    cols = section._sectPr.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols"); section._sectPr.append(cols)
    cols.set(qn("w:num"), "2"); cols.set(qn("w:space"), str(int(pts*20)))

def p(text, size=10, bold=False, italic=False, align=J, space_after=4, first_indent=0.18):
    par = doc.add_paragraph()
    par.alignment = align
    par.paragraph_format.space_after = Pt(space_after)
    if first_indent: par.paragraph_format.first_line_indent = Inches(first_indent)
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    return par

def pflat(text, size=10, bold=False, italic=False, align=J, space_after=4):
    return p(text, size, bold, italic, align, space_after, first_indent=0)

def h(text, size=10, space_before=8):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_before = Pt(space_before); par.paragraph_format.space_after = Pt(4)
    r = par.add_run(text.upper()); r.font.name = TNR; r.font.size = Pt(size); r.bold = True
    r.font.small_caps = True
    return par

def caption(text):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_after = Pt(8)
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(9); r.bold = False
    return par

def figure(path, width, cap):
    par = doc.add_paragraph(); par.alignment = C
    par.paragraph_format.space_after = Pt(2)
    run = par.add_run(); run.add_picture(path, width=Inches(width))
    caption(cap)

def bullet(text, size=10):
    par = doc.add_paragraph(style="List Bullet")
    par.paragraph_format.space_after = Pt(2)
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size)
    return par

def set_cell(cell, text, size=8, bold=False, align=None):
    cell.text = ""
    par = cell.paragraphs[0]
    if align: par.alignment = align
    r = par.add_run(text); r.font.name = TNR; r.font.size = Pt(size); r.bold = bold

# ================= TITLE / AUTHOR (full width) =================
t = doc.add_paragraph(); t.alignment = C
r = t.add_run("ApplyPilot: An Honesty-Enforcing LLM-Agent Pipeline for End-to-End Job Application Automation on Free-Tier Resources")
r.font.name = TNR; r.font.size = Pt(16); r.bold = True
a = doc.add_paragraph(); a.alignment = C
r = a.add_run("Shashank Tomar"); r.font.name = TNR; r.font.size = Pt(11); r.bold = True
a2 = doc.add_paragraph(); a2.alignment = C
r = a2.add_run("Department of Computer Science & Engineering, ABES Engineering College, Ghaziabad, India\n[Roll No.] \u2014 [email@address]")
r.font.name = TNR; r.font.size = Pt(10); r.italic = True
# separator rule
sep = doc.add_paragraph(); sep.alignment = C
pPr = sep._p.get_or_add_pPr(); pbdr = OxmlElement("w:pBdr"); bottom = OxmlElement("w:bottom")
bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "12"); bottom.set(qn("w:color"), "000000")
pbdr.append(bottom); pPr.append(pbdr)

# ================= ABSTRACT + KEYWORDS (full width, bold-italic per IEEE) =================
absr = doc.add_paragraph(); absr.alignment = J; absr.paragraph_format.space_after = Pt(4)
r = absr.add_run("Abstract\u2014")
r.font.name = TNR; r.font.size = Pt(9); r.bold = True
r2 = absr.add_run(
 "Automated job application is dominated by either mass-submission bots that misrepresent candidates or closed commercial services. "
 "This paper presents ApplyPilot (deployed by the author as a personal careerOS fork), a free-tier, locally-run pipeline that couples "
 "large language model (LLM) agents with an honesty-enforcement architecture to automate the full application lifecycle: multi-board "
 "discovery, enrichment, fit scoring, resume tailoring, cover-letter generation, and autonomous submission through the employer's own "
 "career portal. We introduce a generator-critic honesty validator that rejects any resume content not evidenced by the candidate's "
 "verified facts, an eligibility gate that refuses jobs the candidate cannot take, and a structured verdict protocol that makes every "
 "agent action auditable. On a live deployment targeting an India+remote search profile, the system discovered 731 unique postings from "
 "eight sources, scored 48 jobs against structured resume facts (a discriminating 1-9 distribution, 18.8% scoring >=7), produced nine "
 "validator-approved tailored resumes and five cover letters, and completed an end-to-end autonomous application on a live Workday "
 "portal - creating the candidate account, navigating all form pages, uploading the tailored resume, and stopping at the Review step in "
 "dry-run mode - while autonomously refusing two ineligible postings (onsite-only in another country; required relocation) after "
 "verifying eligibility against the employers' own APIs. We describe the architecture, the integrity mechanisms, measured results, "
 "failure modes, and the ethical design considerations of delegating job applications to software agents.")
r2.font.name = TNR; r2.font.size = Pt(9); r2.bold = True; r2.italic = True
kw = doc.add_paragraph(); kw.alignment = J; kw.paragraph_format.space_after = Pt(6)
r = kw.add_run("Index Terms\u2014"); r.font.name = TNR; r.font.size = Pt(9); r.bold = True; r.italic = True
r2 = kw.add_run("autonomous agents; large language models; job application automation; resume tailoring; honesty validation; web agents; Workday; browser automation")
r2.font.name = TNR; r2.font.size = Pt(9); r2.bold = True; r2.italic = True

# ================= TWO-COLUMN BODY =================
new_sec = doc.add_section(WD_SECTION.CONTINUOUS)
new_sec.top_margin = Inches(0.75); new_sec.bottom_margin = Inches(0.9)
new_sec.left_margin = Inches(0.65); new_sec.right_margin = Inches(0.65)
set_col_spacing(new_sec, 14)

# ---- I. INTRODUCTION ----
h("I. Introduction")
pflat("A job search for entry-level engineering roles is a volume game played against time. Recruiters on major boards receive hundreds of applications per posting, and candidates respond by applying more \u2014 each application demanding discovery, fit judgement, document customisation, and manual entry into the employer's career portal. A single application to a large employer using Workday, the enterprise HR system used by more than half of the Fortune 500, involves account creation, four to six form pages, document upload, and screening questions \u2014 typically 15-30 minutes of transcription work that is both cognitively draining and error-prone.")
pflat("Recent work on LLM agents has demonstrated that models can reason over unstructured text, operate interactive web environments, and follow long-horizon procedures [1], [2], [3]. This capability invites a question with both technical and ethical dimensions: can a free-tier, locally-run agent honestly and safely automate the entire application lifecycle on a person's behalf?")
pflat("Existing answers are unsatisfactory. Open-source mass-appliers (e.g., Auto_Jobs_Applier_AIHawk [7]) demonstrated end-to-end feasibility but submit with minimal verification, lack eligibility reasoning, and were ultimately curtailed by platform enforcement. Commercial bots (LazyApply) monetise bulk submission with a single generic resume. Autofill extensions (Simplify) keep the human in the loop for every click. Academic benchmarks (WebArena [2], WorkArena [3]) prove capability on enterprise-like portals but are not deployed personal systems.")
pflat("This paper makes four contributions: (1) an architecture integrating discovery from eight sources, LLM fit scoring, honest tailoring, and real-browser submission in one free pipeline; (2) a generator-critic honesty validator that makes fabrication a rejection event rather than an invisible risk; (3) an eligibility gate and structured verdict protocol (RESULT:*) that yield auditable refusals; and (4) an empirical evaluation on a live deployment \u2014 731 postings, 48 scored jobs, nine approved tailored resumes, one complete autonomous Workday application with resume upload, and two observed eligibility refusals.")
figure(DIR+"fig1_pipeline.png", 3.1, "Fig. 1. ApplyPilot architecture: six batch stages around a SQLite checkpoint store, plus the interactive apply agent (red) with the honesty validator (yellow) supervising document generation.")

# ---- II. RELATED WORK ----
h("II. Related Work")
pflat("A. Mass-Application Tools. Auto_Jobs_Applier_AIHawk [7] automated LinkedIn Easy-Apply using an LLM to answer screening questions, accumulating tens of thousands of GitHub stars before platform policy enforcement discontinued much of its workflow. Its design had no independent check that LLM-generated answers were true, and no model of where the candidate is eligible to work \u2014 the two failure classes our validator and eligibility gate address. LazyApply (commercial) bulk-submits a fixed resume across boards; Simplify (extension) autofills from a stored profile under human control. Matching-as-a-service products (e.g., Sonara, since shut down) demonstrated demand for centralised solutions while illustrating their fragility.")
pflat("B. LLM Web Agents. ReAct [1] established the reasoning-acting interleaving that our apply agent executes. Toolformer [5] showed models can self-teach tool use, motivating tool-mediated integration over screen scraping. WebArena [2] benchmarks agents on realistic self-hostable web environments, finding low success on long-horizon form tasks; WorkArena [3] extends this to ServiceNow-style enterprise portals, the same UI family as Workday, and identifies form navigation among the harder capabilities. Wang et al. [4] survey the plan-act-observe agent architecture with memory and tools that our system instantiates in lightweight form: SQLite as episodic memory, a policy prompt, and Playwright/CDP as actuators.")
pflat("C. Positioning. To our knowledge, no reviewed system combines multi-board discovery, honest LLM scoring, validated document tailoring, and a real-browser autonomous apply agent in a single free, auditable, locally-run deployment with published refusal behaviour. The upstream ApplyPilot project [8] provided the staged pipeline skeleton under AGPL-3.0; the author's careerOS fork [9] contributes the free-tier agent backend (OpenCode with GLM/Gemini models), India-aware eligibility rules, robustness fixes, and the empirical evaluation reported here, remaining AGPL-3.0 with attribution per the licence.")

# ---- III. SYSTEM ARCHITECTURE ----
h("III. System Architecture")
pflat("ApplyPilot is organised as six idempotent batch stages around a single SQLite checkpoint database, followed by an interactive agent stage (Fig. 1). Each stage is independently runnable from the CLI (applypilot run <stage>), resumable after interruption, and carries optional --limit flags for controlled demonstrations. Configuration is three user-owned files: .env (API keys), profile.json (verified candidate facts, salary floor, work-mode constraints), and searches.yaml (locations, remote preference, boards, queries).")
pflat("Stage 1, Discover, scrapes Indeed, Naukri, Glassdoor, LinkedIn and ZipRecruiter via python-jobspy [12] with an India+remote configuration, and additionally crawls employers' public Workday career-site APIs for direct application URLs. Postings are de-duplicated by a company-title-URL signature. Stage 2, Enrich, fetches full descriptions for shortlisted jobs, rendering JavaScript-heavy pages with Playwright [11]. Stage 3, Score, prompts an LLM to rate each job 1-10 against structured resume facts under a rubric covering skills overlap, seniority, location compliance and salary floor; outputs are parsed defensively (markdown stripping, regex integer extraction) so free-tier model verbosity cannot corrupt the store. Stage 4, Tailor, rewrites the resume per role subject to Section IV's validator. Stage 5, Cover, generates cover letters under the same regime. Stage 6, PDF, converts approved documents. The Apply agent (Section V) operates one job at a time in a real browser.")
figure(DIR+"fig4_sources.png", 2.9, "Fig. 2. Top discovery sources in the measured run (731 postings; employer Workday portals dominate over aggregators).")

# ---- IV. HONESTY VALIDATION ----
h("IV. The Honesty Validator")
pflat("The validator is the system's integrity core and answers the central ethics question of auto-apply systems: what may an agent say on a person's behalf? Our answer: only what the person could truthfully say, verified mechanically.")
pflat("Design. The validator holds a watch-list of fabrication-prone patterns derived from the candidate's verified resume facts (employers, projects, skills, metrics, education). For each LLM-generated document it (a) extracts claims, (b) compares named entities and metrics against profile.json, (c) permits re-organisation and de-emphasis of true content but rejects addition of anything unevidenced, and (d) enforces a skills boundary: skills listed by the candidate may be discussed; unknown skills may not be claimed. A skill-normalisation guard prevents false positives (e.g., the candidate's listed C++ must not be flagged).")
pflat("Generator-critic loop. Rejected documents return to the LLM with structured objections (which sentence, which claim, why), with up to five revision attempts before the job is flagged for human review. This turns fabrication from an invisible statistical risk into a visible, logged rejection event, and yields a natural metric: validator acceptance rate and objection taxonomy, which we intend to evaluate adversarially in future work.")

# ---- V. APPLY AGENT ----
h("V. The Autonomous Apply Agent")
pflat("The apply stage launches an LLM agent per job (OpenCode CLI [10] running a free hosted model such as GLM or Gemini Flash) with three assets: a policy prompt built from profile.json with hard rules (true facts only; relocation None must be reported as None, never guessed; eligibility first; salary from the posting's own range and the profile floor), a browser toolset (a Playwright MCP server [11] driving the candidate's own Chromium-family browser over the Chrome DevTools Protocol on a debug port, with raw-CDP script fallback for steps the MCP tools cannot express), and the tailored documents.")
pflat("The workflow (Fig. 3) begins with an eligibility check before any form interaction: the agent reads the posting and the employer's own API where necessary; ineligible jobs terminate immediately with RESULT:FAILED:not_eligible_location. Eligible jobs proceed through account creation, field entry, resume upload, and truthful screening answers to the Review page. In submit mode the agent clicks Submit and verifies; in dry-run mode it stops and saves the draft. Every run terminates with a structured verdict (RESULT:APPLIED | RESULT:FAILED:<reason>) recorded in apply_attempts, producing a complete audit trail per application. Notably, the browser profile persists across jobs, so a one-time human login on a walled board is reusable while the agent never sees credentials.")
figure(DIR+"fig5_agent.png", 3.1, "Fig. 3. Apply-agent workflow: eligibility gate before any form work, truthful field entry, and mode-dependent termination (submit vs. dry-run) with structured verdicts.")

# ---- VI. EVALUATION ----
h("VI. Evaluation")
pflat("We evaluate a live deployment on the author's own resume (B.Tech CSE student, India, remote-preferring, salary floor configured). All numbers are from the production SQLite store, not a simulation.")
pflat("A. Discovery. The pipeline stored 731 unique postings across eight sources; employer Workday portals dominated (Fig. 2): a single aggregator channel (Thomson Reuters postings on boards) contributed 230, Cisco 103, Moderna 85, Mastercard 76, Motorola Solutions 75, and direct Indeed results 72, with the remainder from Salesforce, LinkedIn, Ciena, and others.")
pflat("B. Scoring. 48 jobs were scored under the free-tier configuration. The distribution (Fig. 4) is discriminating and bimodal-tailed: mode 2 (11 jobs) through mode 4 (11), with a fit tail at 7-8 (8 jobs) and a top tier of three 9/10 postings. 18.8% of scored jobs reached >=7, a plausible precision-oriented threshold for expensive downstream stages.")
figure(DIR+"fig2_scores.png", 2.9, "Fig. 4. Real fit-score distribution of the 48 scored jobs (author's live run). Red/amber/green encode weak/marginal/strong fit.")
figure(DIR+"fig3_funnel.png", 2.9, "Fig. 5. Pipeline funnel of the measured run (log scale): discovery feeds a precision-filtered document-generation and application path, with two eligibility refusals recorded.")
pflat("C. Document generation. Nine tailored resumes and five cover letters were produced and converted to PDF, all passing the honesty validator after the generator-critic loop; observed objection classes included unevidenced project mentions (a hallucinated CGPA and an invented project were caught and removed in early iterations) and out-of-bound skill claims.")
pflat("D. Apply outcomes. Table I summarises the measured outcomes. The culminating test ran the agent in dry-run mode against a 9/10-fit Cisco Software Engineer posting on Cisco's live Workday portal: the agent verified eligibility, created the candidate account, navigated every form page (handling dropdown and listbox widgets), uploaded the tailored resume PDF (system-confirmed upload), completed screening questions truthfully, and stopped at the Review page with a saved draft, returning RESULT:APPLIED (dry-run). Two ineligible postings were refused autonomously: an onsite-only Moderna role in Massachusetts (rejected after querying the employer's API) and a Motorola role requiring relocation that the profile forbids, where the agent reported the truthful relocation answer rather than guessing. Indeed-hosted postings requiring session login failed safely with a structured sso_required verdict rather than attempting bypass.")
caption("TABLE I. APPLY-STAGE OUTCOMES (MEASURED)")
tt = doc.add_table(rows=6, cols=3); tt.style = "Table Grid"; tt.alignment = WD_TABLE_ALIGNMENT.CENTER
rowsd = [("Outcome", "Jobs", "Verdict observed"),
         ("Dry-run completed (Workday)", "1", "RESULT:APPLIED (dry-run); draft saved at Review"),
         ("Eligibility refusal", "2", "RESULT:FAILED:not_eligible_location"),
         ("Login wall (Indeed smart apply)", ">12", "RESULT:FAILED:sso_required / indeed_login_wall"),
         ("Tailored+queued for apply", "9", "documents approved; awaiting runs"),
         ("Real submissions", "0", "held for human decision by design")]
for i, row in enumerate(rowsd):
    for j, v in enumerate(row):
        set_cell(tt.cell(i, j), v, bold=(i == 0), align=(C if j == 1 else None))
pflat("E. Failure modes and robustness. Free-tier operation surfaced three reproducible failure classes, all mitigated: (1) quota exhaustion and 15-requests/minute rate limits on Gemini Flash, addressed by model fallback and stage-level retries with backoff; (2) agent-browser desynchronisation, in which fast models queried for browser tools before the MCP server finished connecting \u2014 mitigated by model selection (a slower tool-reliable default) and explicit tool-catalog hints in the prompt; and (3) verbose model output corrupting parsers, mitigated by defensive extraction. These constraints, not model intelligence, were the binding engineering limits of free-tier agentic deployment.")

# ---- VII. DISCUSSION ----
h("VII. Discussion and Ethical Considerations")
pflat("A. Is autonomous applying legitimate? The system submits only through forms employers publish for candidates, with only the candidate's true data, at the candidate's explicit configuration. The dry-run mode makes the human's decision the final gate; the refusal log demonstrates the agent declining, not fabricating. We argue this is materially different from both spam bots (which misrepresent) and manual applying (which wastes the human's hours on transcription).")
pflat("B. Risks and mitigations. Automated submission at scale could harm employer systems or the candidate's reputation; our design limits risk by (a) default thresholds that restrict expensive stages to high-fit jobs, (b) per-job agent runs with audit trails rather than unbounded loops, (c) refusal to bypass login walls or CAPTCHAs, and (d) an explicit human decision before any real submission. Residual risks include employer perception of automated applications \u2014 the system is designed to make each submitted application individually truthful and tailored, arguably higher-quality than the median manual submission.")
pflat("C. Limitations. The evaluation is a single-candidate deployment (n=48 scored, n=1 completed application); no A/B response-rate measurement yet; board coverage depends on third-party scrapers' health; and free-tier quotas make unattended daily operation bursty. These are engineering limits, not conceptual ones.")

# ---- VIII. CONCLUSION ----
h("VIII. Conclusion and Future Work")
pflat("We presented ApplyPilot/careerOS, a free-tier, locally-run LLM-agent pipeline that automates job discovery, fit scoring, honest document tailoring, and autonomous real-browser application submission, with honesty enforcement as a first-class subsystem demonstrated by live behaviour: one complete Workday application (form filled, resume uploaded, draft saved at Review) and two autonomous refusals of ineligible jobs. The contribution is both practical and methodological: an integrity architecture \u2014 verified-facts profile, generator-critic validation, eligibility gating, and structured audit verdicts \u2014 that makes personal job-application automation defensible, released under AGPL-3.0 with upstream attribution.")
pflat("Future work includes: session-persistent operation on login-walled boards; an outcome-tracking stage correlating tailoring strategies with employer replies; adversarial evaluation of the honesty validator; multi-candidate studies with response-rate A/B measurement; and form-semantic agent tools to reduce raw-CDP fallbacks, benchmarked against WorkArena-style task decompositions.")

# ---- REFERENCES ----
h("References")
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
    par.paragraph_format.space_after = Pt(2)
    par.paragraph_format.left_indent = Inches(0.18); par.paragraph_format.first_line_indent = Inches(-0.18)
    run = par.add_run(f"[{i}] {r}"); run.font.name = TNR; run.font.size = Pt(8.5)

# funnel figure + funnel caption into column flow (after refs? better: before refs) 
doc.save(DIR+"ApplyPilot_Research_Paper.docx")
print("PAPER SAVED")
