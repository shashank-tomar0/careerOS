# -*- coding: utf-8 -*-
"""Repair h2 headings: sequential per-section title queues, in document order."""
from pathlib import Path
import re
p = Path(__file__).parent / "gen_final_report.py"
s = p.read_text(encoding="utf-8")
QUEUES = {
 "A": ["Problem Statement", "Contributions", "Organisation of the Report"],
 "B": ["Mass-Application Tools", "Research on LLM Web Agents", "Research Gap"],
 "C": ["Design Principles", "Stage Pipeline", "Worker Isolation Model", "Configuration and Data Model", "The LLM Layer", "Command Surface and Human Interaction Model"],
 "D": ["Threat Model", "Generator-Critic Loop", "Validator Algorithm", "Worked Example"],
 "E": ["Runtime and Browser Bridge", "Policy Prompt and Eligibility Gate", "Structured Verdict Protocol", "Verdict Taxonomy", "Case Studies", "Agent Reliability Engineering"],
 "F": ["Setup", "Discovery Results", "Scoring Results", "Document Generation", "Apply Outcomes", "Failure Modes and Mitigations", "Software Requirements", "Timings and Observability", "Threats to Validity"],
 "G": ["Is Autonomous Applying Legitimate?", "Risks and Mitigations", "Comparison with Existing Tools", "Deployment Economics", "Generalisability of the Pattern", "Limitations"],
}
LET = "ABCDEFGHI"
counts = {k: 0 for k in QUEUES}
fixed = 0
out = []
for line in s.splitlines(True):
    m = re.match(r'^h2\("([A-H])\. (\d)$', line.rstrip("\n"))
    if m:
        sec = m.group(1)
        idx = counts[sec]
        titles = QUEUES[sec]
        assert idx < len(titles), f"queue exhausted for {sec} at index {idx}"
        out.append('h2("' + LET[idx] + ". " + titles[idx] + '")\n')
        counts[sec] += 1
        fixed += 1
    else:
        out.append(line)
p.write_text("".join(out), encoding="utf-8")
print("FIXED", fixed, "headings; counts:", {k: v for k, v in counts.items()})
