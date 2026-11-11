# Cikgu, Sensai! worksheet library
Open dist/index.html in a browser. The site works offline. Selections exist only in memory. No remote fonts, accounts, cookies, analytics or runtime services.
## Deploy
Push the project to GitHub. Connect the repository to a Cloudflare Worker on your Free plan. Leave the build command empty and set the deploy command to npx wrangler deploy. The static asset directory is dist.
## Add lessons
Edit build.py and run python build.py with PyMuPDF, fontTools and Noto Sans CJK installed (font path in script). Commit the regenerated dist/bank.js. Every PDF page is checked for overflow at full size.

The curriculum/ directory contains scenario families for A1 through C1 in Malay, English and Japanese. Each family makes three independent packs. Edit the matching guided dialogue when changing a scenario. The optional transfer page introduces a change of plan after independent practice. Labels are teaching targets. No learner records are stored.

## Charter step 1 (11 November 2026)
Malay Stage 1 now follows nine A1 chapters, with the charter's 13 planned unit slots.
The 13 original resources keep their wording. Units 2B, 8 and 9 are empty placeholders,
not newly authored lessons. The fruit-market family is in 3B. Chapter 12 is outside
Stage 1 and marked "Stage 2, not yet active". B1/B2/C1 Malay families remain
unnumbered, unplaced and provisional. English and Japanese content is unchanged.
The existing A2 lunch extension remains linked from 3B and 5 at its original level.

Read [the step 1 report](docs/STEP-1-REPORT.md) and
[the per-unit issues log](docs/restructure-issues.md). The matching CSV contains
source locations and quoted evidence. Japanese text awaits native-speaker review.
Step 2 adds the component catalogue below. Step 3 affix/register/ledger enforcement
has not started.

To reproduce the audit, obtain Kata-Kata at the exact revision recorded in
`docs/restructure-sources.json`, then run
`python tools/restructure_audit.py /path/to/katakata` before `python build.py`.
The audit reports issues only and never edits the reference repository or lesson text.
`build.py` regenerates bank.js, chapters.js and the downloadable offline ZIP.

## Charter step 2
`catalogue.py` generates `dist/catalogue.js` from the unchanged source packs and
pinned Kata-Kata chapter snapshots in `curriculum/reference/katakata/`.
All eleven types are filterable; only existing content is extractable. The
original full-pack view remains available. Missing suites are explicitly shown.
See [the step 2 report](docs/STEP-2-REPORT.md) and [model contract](docs/DATA-MODEL.md).
Run `python -m unittest discover -s tests -v` after `python build.py`.
The downloadable offline ZIP excludes `docs`, including both audit logs.
