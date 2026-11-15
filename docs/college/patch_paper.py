# -*- coding: utf-8 -*-
"""Expand gen_final_report.py paper body to true 20+ page IEEE content."""
from pathlib import Path
p = Path(__file__).parent / "gen_final_report.py"
s = p.read_text(encoding="utf-8")

# 1. Ethics debate paragraph after 2.1
old = 'h2("2.2 Research on LLM Web Agents")'
new = ('pbf("Beyond feature comparison, these tools raise a documented ethical debate: platforms have actively '
       'enforced against bulk automation (LinkedIn\'s actions against AIHawk-style tools), while candidates face real '
       'time costs. Our position, elaborated in Section 7, is that the defensible boundary is not automation per se but '
       'misrepresentation and system abuse; hence this project\'s design makes each application individually truthful, '
       'tailored, and human-gated for submission.")\n'
       'h2("2.2 Research on LLM Web Agents")')
assert old in s; s = s.replace(old, new, 1)

# 2. Agent reliability paragraph before 2.3
old = 'h2("2.3 Research Gap")'
new = ('pbf("Reliability engineering for such agents is an active research area: models must be selected for '
       'tool-calling discipline (not just benchmark intelligence), tool catalogs must be pinned to available '
       'actuators (our MCP-only configuration, Section 5), and every run must terminate in a machine-readable verdict '
       'for downstream audit. The Gemini family technical report [15] and the OpenCode runtime [10] provide the '
       'free-tier model and agent substrate that make our deployment feasible at zero cost \u2014 a constraint we treat '
       'as a feature, since it forces the architecture to be reproducible by any student.")\n'
       'h2("2.3 Research Gap")')
assert old in s; s = s.replace(old, new, 1)

# 3. Section 3.6 LLM layer after fig2
old = 'figure(DIR+"fig4_sources.png", 2.9, "Fig. 2. Top discovery sources in the measured run (731 postings; employer Workday portals dominate over aggregators).")'
new = old + '''
h2("3.6 The LLM Layer")
pbf("Three LLM interaction patterns appear in the pipeline, each with its own reliability contract. (1) Batch scoring/tailoring calls (Gemini Flash): stateless, structured-output prompts with defensive parsing \u2014 the pipeline strips markdown fences, extracts integers via regex, and re-prompts on parse failure, so free-tier verbosity cannot corrupt the database. (2) Validator critiques: deterministic post-processing of LLM documents (Section 4), where the critic is code, not a model, making verdicts reproducible. (3) The interactive agent (OpenCode-hosted GLM by default): a long-horizon tool-calling conversation in which model choice materially matters \u2014 during development we observed that faster models query the tool catalog before the MCP server finishes connecting and conclude no browser exists; the default was therefore pinned to a slower but tool-reliable model, with explicit tool-catalog hints injected into the prompt.")
pbf("Quota strategy. Free-tier limits (15 requests/minute and daily caps on Gemini Flash; daily quotas on hosted GLM) are handled at three levels: stage-level retries with exponential backoff; checkpointing so a quota-interrupted batch resumes exactly where it stopped; and optional model overrides per stage (applypilot run score --model ...) so a single exhausted provider never blocks the whole pipeline. In the measured run, quota pressure shaped the operating rhythm (batch stages at night, interactive apply by day) but never blocked completion of any stage.")'''
assert old in s; s = s.replace(old, new, 1)

# 4. Case studies 5.5 before section 6
old = '# ---- 6. EVALUATION ----'
new = ('h2("5.5 Case Studies")\n'
 'pbf("Case 1 \u2014 Successful dry-run (Cisco Workday, 9/10 fit). The agent opened the posting, verified '
 'Bangalore-onsite eligibility for an India-based candidate per the configured rules, launched the application, '
 'created the candidate account, navigated every form page (handling dropdown and listbox widgets via the browser '
 'bridge, falling back to raw-CDP scripts for two custom widgets), uploaded the tailored resume PDF '
 '(platform-confirmed \u201cSuccessfully Uploaded!\u201d), answered screening questions strictly from profile facts, and '
 'reached the Review page. Per dry-run discipline it saved the draft without clicking Submit and returned '
 'RESULT:APPLIED (dry-run). The saved draft meant a real submission was one click away \u2014 deliberately left to the '
 'human.")\n'
 'pbf("Case 2 \u2014 Eligibility refusal (Moderna). A high-salary posting scored well on skills, but the agent queried '
 'the employer\'s career API before any form work, determined the role was onsite-only in Massachusetts with no '
 'remote option, and terminated with RESULT:FAILED:not_eligible_location. Notably, the refusal came after '
 'verification, not keyword matching \u2014 the agent read the posting\'s structured work-arrangement data.")\n'
 'pbf("Case 3 \u2014 Truthful screening (Motorola). A Bangalore posting scored 8/10, but its screening questionnaire '
 'required relocation the candidate\'s profile forbids (relocation: None). The agent reported None truthfully '
 'rather than guessing \u2014 the outcome was a refusal, and the agent\'s log shows it explicitly reasoning that '
 'misreporting would be fabrication. This case demonstrates the honesty mechanism operating inside the form, not '
 'just at the gate.")\n'
 'pbf("Case 4 \u2014 Safe failure (Indeed login wall). Remote-India postings aggregated on Indeed render their '
 'application inside an embedded flow requiring a session login. Rather than attempting bypass, the agent failed '
 'safely with RESULT:FAILED:sso_required / indeed_login_wall; the browser-profile persistence design (Section 3.4) '
 'allows a one-time human login to unlock these flows in later runs. All failures are persisted with reasons and '
 'worker transcripts, making them replayable and auditable.")\n\n'
 '# ---- 6. EVALUATION ----')
assert old in s; s = s.replace(old, new, 1)

# 5. Table V comparison before 7.4 limitations
old = 'h2("7.3 Limitations")'
new = ('h2("7.3 Comparison with Existing Tools")\n'
 'pbf("Table V contrasts the deployed system with the reviewed alternatives across the dimensions that matter for '
 'personal automation: breadth of discovery, tailoring honesty, eligibility reasoning, submission autonomy, '
 'auditability, and cost.")\n'
 'caption("TABLE V. FEATURE COMPARISON WITH EXISTING TOOLS")\n'
 't5 = doc.add_table(rows=6, cols=5); t5.style = "Table Grid"; t5.alignment = WD_TABLE_ALIGNMENT.CENTER\n'
 'rows5 = [("Capability", "AIHawk", "LazyApply", "Simplify", "ApplyPilot/careerOS"),\n'
 '         ("Multi-board discovery", "LinkedIn only", "Multi-board", "Extension-scoped", "5 boards + Workday APIs"),\n'
 '         ("Honest tailoring", "None", "None (fixed resume)", "Profile autofill only", "Generator-critic validator"),\n'
 '         ("Eligibility reasoning", "None", "None", "None", "Location/work-mode gate"),\n'
 '         ("Autonomous real-browser apply", "Platform-embedded", "Bot emulation", "Human clicks", "CDP+MCP agent, Workday-native"),\n'
 '         ("Auditability / cost", "Logs / free", "Opaque / paid", "Tracker / free tier", "SQLite verdicts+transcripts / free")]\n'
 'for i, row in enumerate(rows5):\n'
 '    for j, v in enumerate(row): set_cell(t5.cell(i, j), v, bold=(i == 0), size=8)\n'
 'h2("7.4 Limitations")')
assert old in s; s = s.replace(old, new, 1)

# 6. Threats to validity before section 7
old = '# ---- 7. DISCUSSION ----'
new = ('h2("6.8 Threats to Validity")\n'
 'pbf("Internal validity: all LLM outputs (scores, documents, agent actions) pass through deterministic parsing or '
 'code-based validation, so the reported numbers are not re-reads of model prose; however, LLM scoring itself has no '
 'ground truth beyond the rubric \u2014 a human-rater agreement study is future work. External validity: the deployment '
 'is a single candidate profile in one market (India, entry-level, remote-preferring); transferability to other '
 'profiles is plausible but unmeasured. Construct validity: \u201cdry-run completion\u201d measures form-completion '
 'capability, not application success; response-rate measurement is future work. Reliability: free-tier quotas '
 'introduce run-to-run variance in stage latency, though checkpointing makes outputs deterministic once a stage '
 'completes.")\n\n'
 '# ---- 7. DISCUSSION ----')
assert old in s; s = s.replace(old, new, 1)

# 7. Gemini reference (already applied via direct edit; optional)
old = '    "S. Zhang et al., \u201cWorkArena++: Towards compositional planning and reasoning-based common knowledge work tasks,\u201d in Proc. ACL, 2024, arXiv:2407.05265.",\n]'
if old in s:
    s = s.replace(old, '    "S. Zhang et al., \\u201cWorkArena++: Towards compositional planning and reasoning-based common knowledge work tasks,\\u201d in Proc. ACL, 2024, arXiv:2407.05265.",\n    "Gemini Team, Google, \\u201cGemini: A Family of Highly Capable Multimodal Models,\\u201d Technical Report, 2023, arXiv:2312.11805.",\n]', 1)
    print("gemini ref added")

p.write_text(s, encoding="utf-8")
print("ALL EXPANSIONS APPLIED")
