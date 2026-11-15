# -*- coding: utf-8 -*-
"""IEEE audit pass for gen_final_report.py: Roman sections, lettered subsections, Roman cross-refs, TOC."""
from pathlib import Path
import re
p = Path(__file__).parent / "gen_final_report.py"
s = p.read_text(encoding="utf-8")
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII"}
LET = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I"}

# 1. Dotted cross-references first
s = s.replace("Section 5.6", "Section V")
s = s.replace("Section 3.4", "Section III")

# 2. General cross-references (Section N not followed by more digits/dot)
s = re.sub(r"Section (\d)(?![.\d])", lambda m: "Section " + ROMAN[int(m.group(1))], s)

# 3. Section headings h1("N. Title") -> h1("ROMAN. Title")
def h1_repl(m):
    return 'h1("' + ROMAN[int(m.group(1))] + ". " + m.group(2)
s = re.sub(r'h1\("(\d)\. ([^"]+)"\)', h1_repl, s)

# 4. Subsection headings h2("N.N Title") -> h2("LET. Title")
def h2_repl(m):
    return 'h2("' + LET[int(m.group(1))] + ". " + m.group(2)
s = re.sub(r'h2\("(\d)\.(\d+) ([^"]+)"\)', h2_repl, s)

# 5. TOC entries
toc_map = [
    ('"1. INTRODUCTION"', '"I. INTRODUCTION"'), ('"2. RELATED WORK"', '"II. RELATED WORK"'),
    ('"3. SYSTEM ARCHITECTURE"', '"III. SYSTEM ARCHITECTURE"'),
    ('"4. THE HONESTY VALIDATOR"', '"IV. THE HONESTY VALIDATOR"'),
    ('"5. THE AUTONOMOUS APPLY AGENT"', '"V. THE AUTONOMOUS APPLY AGENT"'),
    ('"6. EVALUATION"', '"VI. EVALUATION"'),
    ('"7. DISCUSSION AND ETHICAL CONSIDERATIONS"', '"VII. DISCUSSION AND ETHICAL CONSIDERATIONS"'),
    ('"8. CONCLUSION AND FUTURE WORK"', '"VIII. CONCLUSION AND FUTURE WORK"'),
]
for a, b in toc_map:
    s = s.replace(a, b)

p.write_text(s, encoding="utf-8")
print("IEEE AUDIT APPLIED")
