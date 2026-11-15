# -*- coding: utf-8 -*-
"""Third pass: timing section + Annexure G run narrative (+TOC update)."""
from pathlib import Path
p = Path(__file__).parent / "gen_final_report.py"
s = p.read_text(encoding="utf-8")

# 0. Repair pass (idempotent): remove corrupted block from prior attempts
bad_start = 'pagebreak()\nchapter("ANNEXURE G \\u2014 CULMINATING RUN NARRATIVE'
idx = s.find(bad_start)
if idx != -1:
    end_marker = 'pagebreak()\nchapter("ANNEXURE C \\u2014 GLOSSARY", 14)'
    eidx = s.find(end_marker, idx)
    if eidx != -1:
        s = s[:idx] + s[eidx:]
        print("repaired corrupted block")

# 1. TOC: add annexures D-G
old = '"ANNEXURE B \u2014 SAMPLE AGENT VERDICTS", "ANNEXURE C \u2014 GLOSSARY"]'
if old in s:
    new = ('"ANNEXURE B \u2014 SAMPLE AGENT VERDICTS", "ANNEXURE C \u2014 GLOSSARY",\n'
           '           "ANNEXURE D \u2014 OBSERVED RUN TIMELINE", "ANNEXURE E \u2014 REPOSITORY & REPRODUCIBILITY",\n'
           '           "ANNEXURE F \u2014 SAMPLE DOCUMENT EXCERPTS", "ANNEXURE G \u2014 CULMINATING RUN NARRATIVE"]')
    s = s.replace(old, new, 1)
    print("TOC updated")

# 2. Timing section before 6.8
old = 'h2("6.8 Threats to Validity")'
if "6.7 Timings and Observability" not in s:
    new = ('h2("6.7 Timings and Observability")\n'
     'pbf("Measured stage timings under free-tier conditions: a 24-job scoring batch completed in approximately 78 '
     'seconds (limited by the API rate cap, not model latency); a full 48-job scoring pass ran in the low minutes; '
     'tailoring with validator rounds averaged under a minute per document; the culminating dry-run application ran '
     'about 18 minutes end-to-end, dominated by form navigation and two raw-CDP fallbacks, not model latency. '
     'Observability is a design goal: every stage appends to per-run logs, the database records per-stage row '
     'counts, and the dashboard exposes progress without SQL. This made the debugging sequence of Section 5.6 '
     'tractable \u2014 every fix was found by reading an audit trail, not by guesswork.")\n'
     'h2("6.8 Threats to Validity")')
    assert old in s; s = s.replace(old, new, 1)
    print("timing added")

# 3. Annexure G before glossary
old = 'pagebreak()\nchapter("ANNEXURE C \u2014 GLOSSARY", 14)'
if "ANNEXURE G" in s and old in s and "CULMINATING RUN NARRATIVE" not in s.split("ANNEXURE C")[0]:
    pass
    g = '''pagebreak()
chapter("ANNEXURE G \u2014 CULMINATING RUN NARRATIVE (THE DRY-RUN, AS OBSERVED)", 14)
p("The following is a condensed, factual narrative of the culminating demonstration run, reconstructed from the worker log and system events.", 12, align=J)
for t_ in [
  "The pipeline selected the 9/10-fit Cisco Software Engineer (Bangalore) posting and assembled the worker environment: fresh working directory, persistent browser profile, agent configuration with the playwright MCP server bound to the pipeline-launched browser debug port, the policy prompt, profile facts, and the validator-approved tailored resume PDF.",
  "The agent began with the mandated eligibility check: it read the posting page and the employer career API, confirmed the role is onsite in Bangalore for an India-based candidate \u2014 eligible under the configured India+remote rules \u2014 and proceeded.",
  "It opened the Workday application, created the candidate account, and began form entry: personal details from profile.json (name, address in Ghaziabad UP, contact), education (B.Tech CSE, CGPA 8.3), employment history (Technoledge India internship), and skills \u2014 all sourced exclusively from the verified profile.",
  "Two custom widgets exceeded the MCP tool vocabulary; the agent composed raw-CDP helper scripts (form-state.js, a listbox handler) against the debug port \u2014 an improvisation the harness tolerates within the pinned browser actuator.",
  "It uploaded the tailored resume PDF; the platform confirmed \u201cSuccessfully Uploaded!\u201d. Screening questions were answered truthfully (relocation: None reported as None).",
  "The agent reached the Review page, recognised the dry-run boundary, saved the draft, and terminated with the structured verdict: RESULT:APPLIED (dry-run \u2014 application fully filled and saved as a draft through the Review step; final Submit intentionally not clicked per instructions).",
  "Audit trail: worker log (full transcript), database apply_attempts row, and the draft application left in the candidate's Workday account \u2014 one click from submission, deliberately left to the human."]:
    p("\u2022 " + t_, 12, align=J, space_after=4)
pagebreak()
chapter("ANNEXURE C \u2014 GLOSSARY", 14)'''
    s = s.replace(old, g, 1)
    print("annexure G added")

p.write_text(s, encoding="utf-8")
print("THIRD PASS APPLIED")
