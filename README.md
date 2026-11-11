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
Step 2 adds the component catalogue below. Step 3 adds the language checks; step 4 the pilot suites.


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

## Charter step 3: frozen baseline

The governing charter is the living [Google Doc](https://docs.google.com/document/d/1d-uiYfQixReMUlPAcUEJ6R4onWOh-4Aa9urr14DL2lw).
Re-read it at the start of every step; it is read-only to this builder.

`python build.py` runs `language_checks.py` before generating assets. The build
fails on unlisted unit/check/term violations. Missing ledger terms are separately
reported as non-blocking gaps. `curriculum/legacy-exceptions.json` may only shrink;
never regenerate it from the current content. The frozen hash ceiling and Git
history reject additions, edits and reintroduced keys. Use a full Git checkout.

For a re-authored unit: remove all its exception entries, add its ID to
`curriculum/reauthored-units.json`, review its explicit target/rubric spans in
`curriculum/malay-text-scope.json`, and make it pass with no exceptions. Stage 1
rubrics/explainers must then be Japanese or English. Do not edit the ledger or
reference snapshot to make the check pass without Sam's approval.

`python tools/check_report.py` regenerates developer-only reports under `docs`.
It never writes exceptions. Read [the step 3 report](docs/STEP-3-REPORT.md) and
[complete inventory](docs/STEP-3-INVENTORY.md). Section 13 list A is now in the ledger.


## Charter step 4: pilot suites (units 1, 2A, 2B and the chapter 1 and 2 fast packs)

The pilot content lives in `suite/` (one Python module per unit, plus `fast.py`). Mark
every Malay target span `«…»`; quote a root or standard form from a Kata-Kata note as
`‹…›` and list it with its source in `curriculum/malay-mentions.json`. Unmarked text
must be Japanese or English: the build fails if it contains a ledger word. Names go in
`curriculum/malay-proper-nouns.json`. Pages are paginated by measurement; teacher keys
may run to several pages.

Re-authored units (`curriculum/reauthored-units.json`) are ledger-only: a word missing
from the ledger fails the build there. `tests/test_step4_suite.py` checks the charter
section 6 minimums and section 14 drills. PDF previews: MuPDF's rasteriser garbles this
CJK subset on screen, so render previews with poppler (`pdftoppm`); the PDF itself is
correct. See [the step 4 report](docs/STEP-4-REPORT.md).
