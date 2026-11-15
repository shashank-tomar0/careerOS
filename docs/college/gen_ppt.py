# -*- coding: utf-8 -*-
"""Build the 13-slide mini-project presentation with real figures."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

DIR = "C:/Users/dell/Desktop/mini-project/docs/college/"
NAVY = RGBColor(0x0F, 0x2A, 0x43); ACCENT = RGBColor(0x1E, 0x40, 0xAF)
GRAY = RGBColor(0x33, 0x41, 0x55); WHITE = RGBColor(0xFF, 0xFF, 0xFF)
RED = RGBColor(0xB9, 0x1C, 0x1C); GREEN = RGBColor(0x14, 0x65, 0x34)

prs = Presentation()
prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

def add_slide(title, subtitle=None):
    s = prs.slides.add_slide(BLANK)
    bar = s.shapes.add_shape(1, Inches(0), Inches(0), prs.slide_width, Inches(1.0))
    bar.fill.solid(); bar.fill.fore_color.rgb = NAVY; bar.line.fill.background()
    tf = bar.text_frame; tf.text = title
    tf.margin_left = Inches(0.5)
    r = tf.paragraphs[0].runs[0]; r.font.size = Pt(30); r.font.bold = True; r.font.color.rgb = WHITE
    if subtitle:
        t = s.shapes.add_textbox(Inches(0.6), Inches(1.05), Inches(12.1), Inches(0.5)).text_frame
        r = t.paragraphs[0].add_run(); r.text = subtitle
        r.font.size = Pt(16); r.font.italic = True; r.font.color.rgb = ACCENT
    return s

def bullets(s, items, top=1.7, size=18, left=0.7, width=12.0):
    t = s.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(5.2)).text_frame
    t.word_wrap = True
    for i, (txt, lvl) in enumerate(items):
        para = t.paragraphs[0] if i == 0 else t.add_paragraph()
        para.level = lvl
        run = para.add_run(); run.text = ("\u2022 " if lvl == 0 else "\u2013 ") + txt
        run.font.size = Pt(size - lvl * 3); run.font.color.rgb = GRAY

def pic(s, path, left, top, width):
    s.shapes.add_picture(path, Inches(left), Inches(top), width=Inches(width))

# 1 Title
s = prs.slides.add_slide(BLANK)
bg = s.shapes.add_shape(1, Inches(0), Inches(0), prs.slide_width, prs.slide_height)
bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
t = s.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(3.4)).text_frame; t.word_wrap = True
r = t.paragraphs[0].add_run(); r.text = "ApplyPilot / careerOS"
r.font.size = Pt(48); r.font.bold = True; r.font.color.rgb = WHITE
p2 = t.add_paragraph(); r = p2.add_run(); r.text = "An Honesty-Enforcing LLM-Agent Pipeline for End-to-End Job Application Automation"
r.font.size = Pt(26); r.font.color.rgb = RGBColor(0xBF, 0xDB, 0xFE)
p3 = t.add_paragraph(); r = p3.add_run(); r.text = "Shashank Tomar  \u2022  B.Tech CSE  \u2022  Mini Project (BCS554)  \u2022  ABES Engineering College, Ghaziabad"
r.font.size = Pt(18); r.font.color.rgb = WHITE
p4 = t.add_paragraph(); r = p4.add_run(); r.text = "Under the Supervision of: [GUIDE NAME]"
r.font.size = Pt(16); r.font.italic = True; r.font.color.rgb = RGBColor(0xBF, 0xDB, 0xFE)

# 2 Problem
s = add_slide("The Problem", "Why job applications need automation \u2014 done honestly")
bullets(s, [
 ("A Workday application = account creation + 4\u20136 form pages + upload + screening questions", 0),
 ("15\u201330 minutes of pure transcription per employer \u2014 repeated dozens of times", 0),
 ("Volume game: recruiters get hundreds of applications per posting", 0),
 ("Manual repetition silently disqualifies candidates via data-entry errors", 0),
 ("Existing tools: mass-spam bots (dishonest) or closed paid SaaS (opaque)", 0),
 ("Central question: can a free-tier LLM agent do this end-to-end \u2014 and never lie?", 0),
])

# 3 Existing tools
s = add_slide("Related Work \u2014 The Landscape", "Two unacceptable categories of prior tools")
bullets(s, [
 ("Auto_Jobs_Applier_AIHawk (open-source, 2024)", 0),
 ("  LLM answers screening questions on LinkedIn Easy-Apply \u2014 no truth-check, no eligibility logic; curtailed by platform enforcement", 1),
 ("LazyApply (paid SaaS)", 0),
 ("  Bulk-submits one fixed resume everywhere \u2014 misrepresents the candidate", 1),
 ("Simplify (extension)", 0),
 ("  Autofills fields; human still clicks everything \u2014 manual-first", 1),
 ("Research: ReAct, WebArena, WorkArena prove LLM agents can operate real enterprise portals", 0),
 ("Gap: nobody combined discovery + honest scoring + validated tailoring + real-browser apply in one free pipeline", 0),
])

# 4 Idea
s = add_slide("Our Idea: careerOS", "One pipeline, six stages, one honesty rule: never invent")
bullets(s, [
 ("Discover \u2192 Enrich \u2192 Score \u2192 Tailor \u2192 Cover \u2192 PDF \u2192 Apply", 0),
 ("Local SQLite checkpoint store \u2014 resumable, auditable, dashboard built in", 0),
 ("Runs 100% on free tiers (Gemini Flash + OpenCode-hosted GLM) on the student's own laptop", 0),
 ("Honesty enforced by architecture: validator + eligibility gate + verdict protocol", 0),
 ("Published as AGPL-3.0 fork crediting upstream ApplyPilot", 0),
])

# 5 Architecture (fig1)
s = add_slide("Architecture")
pic(s, DIR + "fig1_pipeline.png", 1.0, 1.4, 11.2)
bullets(s, [("Every stage checkpoints to SQLite; the apply agent drives a real browser (red)", 0)], top=6.6, size=15)

# 6 Validator
s = add_slide("The Honesty Validator", "What may an agent say on your behalf? Only what you could truthfully say.")
bullets(s, [
 ("Compares every generated claim against verified profile facts", 0),
 ("3 fabrication classes: entity invention, metric inflation, capability inflation", 0),
 ("Caught in testing: hallucinated CGPA 9.1 (profile says 8.3) + invented project \u2014 removed by the generator-critic loop", 0),
 ("Skill normalisation guard: your listed C++ is allowed; unknown skills are rejected", 0),
 ("Objections return to the LLM with sentence-level reasons \u2014 max 5 attempts", 0),
 ("Verdict, objections and timestamps persisted \u2014 fabrication is a logged event, not a risk", 0),
])

# 7 Discovery results (fig4 sources)
s = add_slide("Measured Results \u2014 Discovery", "731 real postings from 8 sources")
pic(s, DIR + "fig4_sources.png", 1.4, 1.5, 8.0)
bullets(s, [("Employer Workday portals dominate \u2192 validates the Workday-first apply strategy", 0)], top=6.7, size=15, left=9.6, width=3.5)

# 8 Scoring (fig2 scores)
s = add_slide("Measured Results \u2014 AI Fit Scoring", "48 jobs scored against real resume facts")
pic(s, DIR + "fig2_scores.png", 2.2, 1.4, 7.4)
bullets(s, [("Discriminating 1\u20139 spread \u2014 18.8% reached \u22657", 0), ("Three 9/10 postings = Cisco SWE Bangalore with direct Workday URLs", 0)], top=6.4, size=15)

# 9 Apply agent (fig3)
s = add_slide("The Autonomous Apply Agent", "Eligibility gate first \u2014 then the real form")
pic(s, DIR + "fig5_agent.png", 1.0, 1.4, 11.2)
bullets(s, [("OpenCode agent + Playwright MCP over CDP; raw-CDP fallback for custom widgets", 0)], top=6.7, size=15)

# 10 Demo evidence
s = add_slide("Demo Evidence \u2014 It Actually Worked", "Live Workday run, worker-log verdicts")
bullets(s, [
 ("Cisco Software Engineer (9/10 fit), live Workday portal:", 0),
 ("  Account created \u2192 every form page filled \u2192 resume uploaded (\u201cSuccessfully Uploaded!\u201d) \u2192 Review reached", 1),
 ("  RESULT:APPLIED (dry-run) \u2014 draft saved, Submit left to the human", 1),
 ("It refused to apply for me:", 0),
 ("  Moderna (onsite Massachusetts, verified via employer API) \u2192 not_eligible_location", 1),
 ("  Motorola (requires relocation; profile says None) \u2192 answered truthfully, refused", 1),
 ("Indeed login walls \u2192 fails safely with sso_required, never bypasses", 0),
])

# 11 Funnel (fig3 funnel)
s = add_slide("Measured Results \u2014 The Funnel", "Discovery feeds a precision-filtered application path")
pic(s, DIR + "fig3_funnel.png", 2.2, 1.4, 7.4)
bullets(s, [("Every number from the production SQLite store \u2014 no simulation", 0)], top=6.4, size=15)

# 12 Ethics
s = add_slide("Ethics & Limitations", "The defensible boundary is misrepresentation, not automation")
bullets(s, [
 ("Submits only through forms employers publish \u2014 only true candidate data", 0),
 ("Dry-run by default: the human makes the final submission decision", 0),
 ("No CAPTCHA circumvention, no login-wall bypass, no ToS violations", 0),
 ("Free (vs $30\u2013240/yr SaaS), open (AGPL), auditable (verdicts + transcripts)", 0),
 ("Limitations: single-candidate deployment, no response-rate study yet, quota-bounded operation", 0),
])

# 13 Conclusion
s = add_slide("Conclusion \u2014 and a Live Demo", "Thank you. Questions?")
bullets(s, [
 ("731 jobs discovered \u2192 48 scored \u2192 9 tailored (validator-approved) \u2192 full Workday dry-run + 2 honest refusals", 0),
 ("Contribution: an integrity architecture for personal automation \u2014 verified facts, generator-critic validation, eligibility gating, audit verdicts", 0),
 ("Future: session persistence, outcome tracking, adversarial validator evaluation, multi-candidate studies", 0),
 ("Live demo (if time permits):  applypilot apply --dry-run --limit 1", 0),
 ("github.com/shashank-tomar0/careerOS", 0),
])
# highlight the command
last = prs.slides[-1]
for shp in last.shapes:
    if shp.has_text_frame:
        for para in shp.text_frame.paragraphs:
            for r in para.runs:
                if r.text.startswith("Live demo"):
                    r.font.bold = True; r.font.color.rgb = ACCENT

prs.save(DIR + "ApplyPilot_Presentation.pptx")
print("PPT SAVED: 13 slides")
