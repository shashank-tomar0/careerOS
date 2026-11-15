# -*- coding: utf-8 -*-
"""Second expansion pass: deep-dive sections for 20+ page paper body."""
from pathlib import Path
p = Path(__file__).parent / "gen_final_report.py"
s = p.read_text(encoding="utf-8")

# 1. Historical context after 1.1
old = 'h2("1.2 Contributions")'
new = ('pbf("Historical context. Recruitment automation has evolved through three generations: form-autofill '
       'extensions (password-manager style profile replay), keyword-matching mass submitters (the quantity era), and '
       'now agentic systems that read, judge, and act. Each generation increased capability without adding '
       'corresponding safeguards; the third generation makes safeguards both possible and urgent, because an agent '
       'that can answer employer questions can also answer them falsely at scale. This report\'s central design claim '
       'is that the third generation must ship with honesty machinery built in.\")\n'
       'h2("1.2 Contributions")')
assert old in s; s = s.replace(old, new, 1)

# 2. CLI design after 3.6 quota paragraph (before section 4 marker)
old = '# ---- 4. VALIDATOR ----'
new = ('h2("3.7 Command Surface and Human Interaction Model")\n'
 'pbf("The human interface is a small, deliberate CLI. applypilot doctor verifies environment health (API keys, '
 'browser availability, Node/MCP installation) before any run. Each stage is a first-class command '
 '(applypilot run <stage> [--limit N --workers W --model M]) with checkpointed state, so the human can inspect '
 'results between stages; applypilot status and applypilot dashboard render the database as a live scoreboard. '
 'Two batch scripts (launch-run.bat, apply-real.bat) wrap the daily flows. The design principle is that the human '
 'always has a decision point between stages \\u2014 automation handles transcription and navigation; the human owns '
 'thresholds, targeting, and submission. This is also a safety property: nothing expensive runs without a '
 'human-initiated command.\")\n\n'
 '# ---- 4. VALIDATOR ----')
assert old in s; s = s.replace(old, new, 1)

# 3. Worked example after 4.3 observed behaviour paragraph
old = 'h2("4.2 Generator-Critic Loop")'
# place worked example AFTER the loop section instead; find marker after 4.3
old = '# ---- 5. AGENT ----'
new = ('h2("4.4 Worked Example")\n'
 'pbf("A real trace illustrates the loop. An early tailored draft for the Cisco Software Engineer role contained: '
 '\\"maintaining a production system with 99.9% uptime\\" (true \\u2014 evidenced by profile), a CGPA cited as 9.1 '
 '(false \\u2014 profile says 8.3), and a mention of project \\"signal-sentinel\\" reworded into an enterprise '
 'deployment (false \\u2014 the resume does not contain that project). The validator returned three objections: '
 '[sentence 4, metric 9.1 vs 8.3, metric-inflation], [sentence 7, project signal-sentinel, entity-not-in-facts], '
 '[sentence 9, phrase enterprise deployment, capability-inflation]. The generator rewrote with objections applied; '
 'the second attempt passed. The final approved document and its validator report (objection list, attempt count, '
 'timestamp) were persisted \\u2014 the rejection is a first-class, inspectable artefact, which is precisely what '
 'distinguishes mechanical honesty checks from prompt-level \\"please be honest\\" instructions.")\n\n'
 '# ---- 5. AGENT ----')
assert old in s; s = s.replace(old, new, 1)

# 4. Agent reliability engineering after case studies (before 6 marker) 
old = '# ---- 6. EVALUATION ----'
new = ('h2("5.6 Agent Reliability Engineering")\n'
 'pbf("Deploying the agent across dozens of live runs surfaced a debugging sequence worth recording, because it '
 'generalises to any free-tier agentic deployment. (1) Quota collapse: the default agent model exhausted its daily '
 'cap mid-form; mitigation \\u2014 stage-level model overrides plus a fallback ordering of providers. (2) Rate-limit '
 'thrash: Gemini Flash\'s 15-requests/minute cap broke the agent\'s rapid tool loop; mitigation \\u2014 retry with '
 'backoff and, decisively, model substitution. (3) The tool-catalog race: fast models issued tool-search queries '
 'before the Playwright MCP server finished spawning, concluded \\"no browser connected\\", and quit with a plausible '
 'but wrong verdict; mitigation \\u2014 pinning a slower tool-reliable model (GLM) as default and injecting explicit '
 'tool-catalog hints (\\u201cyour browser tools are tools.playwright.*; never conclude no browser exists without '
 'calling them\\u201d). (4) Improvisation drift: agents invented their own CDP helper scripts (eval-in-tab.js, '
 'form-state.js) when MCP tools did not cover a widget; rather than fight this, the configuration pins the browser '
 'actuator while permitting scripted fallbacks \\u2014 pragmatically trading purity for capability. (5) Disconnected '
 'built-in tools: the agent runtime also ships a desktop browser tool that is unavailable headless; agents '
 'repeatedly preferred it. The fix \\u2014 disabling the built-in browser namespace in the worker\'s agent '
 'configuration so only the CDP-attached MCP tools exist \\u2014 was the single highest-impact reliability change of '
 'the project. Each fix is a published commit in the fork\'s history.\")\n\n'
 '# ---- 6. EVALUATION ----')
assert old in s; s = s.replace(old, new, 1)

# 5. Expand future work into paragraphs (replace the future work sentence)
old = 'pbf("Future work: session-persistent operation on login-walled boards; an outcome-tracking stage correlating tailoring strategies with employer replies; adversarial evaluation of the honesty validator; multi-candidate studies with response-rate A/B measurement; and form-semantic agent tools to reduce raw-CDP fallbacks, benchmarked against WorkArena-style task decompositions.")'
new = ('pbf("Future work falls into five tracks. (1) Coverage: session-persistent operation on login-walled boards '
       '(the human logs in once; the agent owns the flow thereafter), extending the Workday crawler to additional '
       'employer ATS families (Greenhouse, Lever, SuccessFactors). (2) Learning: an outcome-tracking stage that '
       'correlates tailoring strategies and cover-letter styles with employer replies, turning the pipeline into a '
       'feedback-driven system rather than a static one. (3) Integrity science: adversarial evaluation of the '
       'honesty validator \\u2014 attack it with subtly-inflated documents and measure catch rate; publish the '
       'objection taxonomy as a benchmark. (4) Evaluation at scale: multi-candidate studies with response-rate A/B '
       'measurement against manual applications, the number that ultimately justifies or retires the approach. '
       '(5) Agent capability: form-semantic tools (field-type aware fill/verify primitives) to reduce raw-CDP '
       'fallbacks, benchmarked against WorkArena-style task decompositions; and a scheduling layer for unattended '
       'daily operation within free-tier quotas.")')
assert old in s; s = s.replace(old, new, 1)

# 6. Generalizability paragraph in discussion before limitations (now 7.4)
old = 'h2("7.4 Limitations")'
new = ('h2("7.5 Generalisability of the Pattern")\n'
 'pbf("While this report focuses on job applications, the architecture \\u2014 verified-facts profile + '
 'generator-critic validation + eligibility gate + structured verdicts + auditable browser agent \\u2014 is a '
 'general pattern for any domain where an agent transacts on a person\'s behalf against rules-bound institutions: '
 'government form filing, university applications, vendor onboarding, benefits claims. In each, the honesty '
 'validator\'s core trick applies: define the claim space against a verified profile, make rejection a logged '
 'first-class event, and keep the final transactional click under human control by default. We suggest this '
 '\\u201chonest agent harness\\u201d as a reusable contribution beyond the job-search domain.")\n'
 'h2("7.6 Limitations")')
assert old in s; s = s.replace(old, new, 1)

# 7. Per-source table in 6.2
old = 'h2("6.3 Scoring Results")'
new = ('caption("TABLE VI. DISCOVERY SOURCES (MEASURED, TOP 8 OF 18)")\n'
 't6 = doc.add_table(rows=9, cols=3); t6.style = "Table Grid"; t6.alignment = WD_TABLE_ALIGNMENT.CENTER\n'
 'rows6 = [("Source", "Postings", "Share"),\n'
 '         ("Thomson Reuters (board-aggregated)", "230", "31.4%"),\n'
 '         ("Cisco (Workday)", "103", "14.1%"),\n'
 '         ("Moderna (Workday)", "85", "11.6%"),\n'
 '         ("Mastercard (Workday)", "76", "10.4%"),\n'
 '         ("Motorola Solutions (Workday)", "75", "10.3%"),\n'
 '         ("Indeed (direct)", "72", "9.8%"),\n'
 '         ("Salesforce (Workday)", "35", "4.8%"),\n'
 '         ("Others (LinkedIn, Ciena, PwC, ...)", "55", "7.6%")]\n'
 'for i, row in enumerate(rows6):\n'
 '    for j, v in enumerate(row): set_cell(t6.cell(i, j), v, bold=(i == 0), size=8, align=(C if j else None))\n'
 'h2("6.3 Scoring Results")')
assert old in s; s = s.replace(old, new, 1)

p.write_text(s, encoding="utf-8")
print("SECOND EXPANSION APPLIED")
