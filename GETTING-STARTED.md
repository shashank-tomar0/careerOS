# careerOS — Beginner's Guide (from zero, any device)

A complete walkthrough for someone who has never used this before.
Budget: ~30 minutes of setup + 1-2 hours for the first full run.

---

## Part 0 — What you need before starting

Install these three things (all free):

1. **Python 3.11 or newer** — https://python.org/downloads
   - On Windows: run the installer, and CHECK "Add Python to PATH" ✅
2. **Node.js 18 or newer** — https://nodejs.org (needed for the auto-apply browser tools)
3. **Chrome** (or any Chromium browser: Brave, Edge work too)

Then get one free API key:

4. **Gemini API key** — go to https://aistudio.google.com → sign in → "Get API key" → create. Copy it. It's free.

---

## Part 1 — Install careerOS

Open a terminal (CMD / PowerShell / Terminal) and run:

```bash
pip install git+https://github.com/shashank-tomar0/careerOS.git
pip install --no-deps python-jobspy
pip install pydantic tls-client requests markdownify regex curl_cffi
```

> Why three commands? `python-jobspy` (the job board scraper) declares a
> dependency that conflicts with pip's resolver but works fine — so it is
> installed separately, then its real runtime deps are installed after.

Now install **OpenCode** — this is the free AI agent that will fill out job
application forms for you (no Claude subscription needed):

```bash
npm install -g opencode-ai
```

---

## Part 2 — One-time setup wizard

```bash
applypilot init
```

It asks questions in order. Here is what each one means and what to type:

### Step 1: Resume
- **Resume file path** — a PDF or TXT of your resume, e.g. `C:\Users\you\Downloads\my-resume.pdf`
- **Plain-text version (.txt)** — paste the same resume in Notepad, save as
  `resume.txt`, and give the path. (The AI reads the text version.)

### Step 2: Profile — powers scoring, tailoring and form auto-fill
| Question | What it means | Example answer |
|---|---|---|
| Full name | Your legal name | `Priya Sharma` |
| Preferred/nickname | What forms should call you | `Priya` |
| Email | Where recruiters reach you | `priya@example.com` |
| Phone | With country code | `+91 98xxxxxx` |
| City / State / Country / PIN | Where you live | `Pune` / `Maharashtra` / `India` / `411001` |
| Street address | Optional; some forms ask for it | your address, or blank |
| LinkedIn URL | Your profile link | `https://linkedin.com/in/...` |
| GitHub URL | Optional | `https://github.com/...` |
| Portfolio / website | Optional | or blank |
| Job site password | Only if you want auto-apply to log into sites for you | blank is fine |
| Legally authorized to work? | In the country you're targeting | `y` |
| Need sponsorship? | Answer honestly — it filters jobs | `n` |
| Work permit type | Citizen / PR / visa — or blank | `Citizen` |
| Expected annual salary | A number, no commas | `1200000` |
| Currency | Your currency code | `INR` |
| Acceptable range | `min-max` | `800000-2000000` |
| Current/most recent job title | Truthful | `Junior Developer` |
| Target role | What you WANT to be hired as | `AI Engineer` |
| Years of professional experience | Best guess is fine | `1` |
| Highest education | | `Bachelor's Degree` |
| Programming languages | Comma-separated | `Python, JavaScript, SQL` |
| Frameworks & libraries | Comma-separated | `React, FastAPI, Django` |
| Tools & platforms | Comma-separated | `Git, Docker, AWS, MySQL` |
| Companies to always keep | Where you actually worked | `TCS` |
| Projects to always keep | Projects you actually built | `Expense tracker app` |
| School name(s) to preserve | Your college | `XYZ University` |
| Real metrics to preserve | True numbers from your work | `20% faster, 500 users` |
| Earliest start date | | `Immediately` |

> **Important:** everything you enter must be TRUE. The tool's "honesty
> checker" preserves these facts and will refuse to let the AI invent
> companies, numbers or skills you don't have.

### Step 3: Job search
- Target location (e.g. `Remote`), radius (`0` for remote-only), and job titles
  (comma-separated, e.g. `AI Engineer, Backend Developer`).

### Step 4: AI features
- Enable? `y`
- Provider: `gemini`
- API key: paste the key from Part 0
- Model: **type the exact ID** `gemini-2.0-flash` (or `gemini-3.1-flash-lite`
  if that one is unavailable on your account — use the ID, not a display name!)

### Step 5: Auto-apply
- Enable? `y` — it will detect OpenCode automatically (or ask for Claude Code).

---

## Part 3 — Two small config fixes (recommended)

### 3a. Browser path (only if auto-apply can't find Chrome)
If you use Brave/Edge instead of Chrome, open `~\.applypilot\.env` in Notepad
and add a line:

```
CHROME_PATH=C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe
```

### 3b. Search config for your country
The default search config is US-oriented. Open `~\.applypilot\searches.yaml`
and adjust:

- `country_indeed:` under `defaults:` — set to your country, e.g. `"india"`
- `locations:` — your cities, e.g.
  ```yaml
  locations:
    - location: "Remote"
      remote: true
    - location: "Bengaluru, India"
      remote: false
  ```
- `location_accept:` — words that must appear in a job's location for it to
  count (your country + cities + "Remote")
- `location_reject_non_remote:` — locations you never want

Keep the same key names and indentation — this file is read by the program.

---

## Part 4 — Verify everything

```bash
applypilot doctor
```

Every line should show OK, ending with:
`Current tier: Tier 3 — Full Auto-Apply`
(Tier 2 = "discovery + AI tailoring only, no auto-apply" — also fine.)

---

## Part 5 — Run it!

The simple way (everything, in order, ~1-2 hours total):

```bash
applypilot run --validation lenient
applypilot status
applypilot dashboard
```

Or stage by stage, to watch each part work:

```bash
applypilot run discover        # scrapes job boards (~10-30 min)
applypilot run enrich --workers 4   # fetches full descriptions (~10 min)
applypilot run score           # AI scores every job 1-10 (~10-20 min)
applypilot run tailor --validation lenient   # custom resume per good job
applypilot run cover --validation lenient    # cover letter per good job
applypilot run pdf             # converts to PDFs
```

> Rate-limit warnings during the AI stages are normal on the free tier —
> it waits and retries automatically.

Your results:
- Tailored resumes → `~\.applypilot\tailored_resumes\`
- Cover letters → `~\.applypilot\cover_letters\`
- Stats in the terminal (`status`) or browser (`dashboard`)

---

## Part 6 — Auto-apply (the robot fills forms for you)

First watch it work without submitting anything:

```bash
applypilot apply --dry-run
```

A Chrome window opens and the AI fills out a real application form live —
but never clicks Submit. When that looks good:

```bash
applypilot apply --limit 1    # one real application, then stops
applypilot apply              # keep going until the queue is empty
```

Useful extras:

```bash
applypilot apply --mark-applied "https://job-url"   # you applied manually
applypilot apply --mark-failed "https://job-url"    # never retry this one
applypilot apply --reset-failed                     # retry all failed
```

---

## Part 7 — Everyday use (after the first run)

```bash
applypilot run --validation lenient   # picks up only NEW work — fast
applypilot status                     # see where everything stands
applypilot dashboard                  # pretty view
```

Run it daily or weekly. The built-in database remembers every job ever
seen, so nothing is processed twice and nothing is lost.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `'applypilot' is not recognized` | Reinstall Python with "Add to PATH" checked, reopen terminal |
| `LLM error: 400 Bad Request` | Your model name is wrong — in `.env` use an exact ID like `gemini-2.0-flash` |
| Discovery finds 0 jobs | Check `searches.yaml`: right country, right accept patterns |
| "No tailored resumes ready" | Run `applypilot run score tailor` first |
| Auto-apply can't find browser | Set `CHROME_PATH` in `.env` (Part 3a) |
| Scoring stuck on rate limits | Normal on free tier; or use `--validation lenient` (fewest AI calls) |

---

## License note

careerOS is a fork of ApplyPilot by Pickle-Pixel, licensed AGPL-3.0.
Personal use is completely free. If you modify and deploy it as a service,
you must release your changes under the same license.
