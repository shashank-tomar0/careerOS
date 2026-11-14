# careerOS — Live Demo Script

Run these commands yourself in a terminal, in order. Each one is a stage
of the pipeline. Timings assume the demo search config (2 queries x Remote).

```
# 0. Sanity check — shows Tier 3 (opencode + Brave + Gemini all detected)
applypilot doctor

# 1. DISCOVER — scrapes 5 job boards live (~5 min, ~100-200 jobs)
applypilot run discover

# 2. ENRICH — visits every job page for full descriptions (~10 min)
applypilot run enrich --workers 4

# 3. SCORE — AI rates every job 1-10 against your resume (~10-15 min)
applypilot run score

# 4. TAILOR — AI writes a custom resume per 7+ job (~5-10 min)
applypilot run tailor --validation lenient

# 5. COVER — targeted cover letters for the same jobs (~5-10 min)
applypilot run cover --validation lenient

# 6. PDF — converts everything to PDFs (instant)
applypilot run pdf

# 7. RESULTS — score distribution + per-source stats
applypilot status
applypilot dashboard

# 8. AUTO-APPLY (dry run — fills forms but does NOT submit; watch it drive Brave)
applypilot apply --dry-run --model opencode/big-pickle

# 9. AUTO-APPLY (real — one application, then stops)
applypilot apply --limit 1 --model opencode/big-pickle
```

Or run everything in one shot (skip per-stage viewing):

```
applypilot run --validation lenient --workers 4
applypilot apply --limit 1 --model opencode/big-pickle
```

After the demo, restore the full India search config:

```
copy /Y "C:\Users\dell\.applypilot\searches-full.yaml" "C:\Users\dell\.applypilot\searches.yaml"
```

Notes:
- The demo uses a fresh database. Your previous 678-job database is kept
  at `~\.applypilot\applypilot-main-backup.db`.
- `--model opencode/big-pickle` = the free OpenCode model driving the browser.
- Rate-limit warnings during scoring are normal; it retries automatically.
