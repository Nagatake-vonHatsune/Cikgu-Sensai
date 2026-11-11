# Step 2 report — 11 November 2026

Scope: data model, component tags and test-item tag infrastructure only. Charter
Context and sections 6, 7 and 12 re-read. No step 3 guards or new teaching content.

## What changed, by file

| File | Change |
| --- | --- |
| `docs/restructure-issues.md`, `.csv` | Moved out of `dist`; updated inventory to recognise Sam's five roots. Other legacy issues remain recorded, not corrected. |
| `tools/restructure_audit.py` | Writes to docs and reads the local root classifications. Reporting only. |
| `curriculum/malay-roots.json` | Records beri, mesej, memang, mesti and beritahu as roots, not productive affix violations. |
| `curriculum/reference/katakata/c01.json` through `c09.json`, `malay-ledger.csv` | Byte-identical pinned snapshots for reproducible chapter IDs, words and frames. No ledger edits. |
| `catalogue.py` | Nine Stage 1 chapter records, 13 units, 65 unit block plans plus nine review/skills blocks; 143 component slots; 216 independently selectable extracts; neutral scene records and separate language layers; test-item validation and prerequisite matching. |
| `curriculum/test-items.json` | Empty authoring collection with a validated item contract. No chapter tests currently exist. |
| `build.py` | Generates the catalogue; excludes docs and audit logs from the public offline archive. Existing PDF overflow check retained. |
| `dist/catalogue.js` | Generated chapter/component/scene/language-layer metadata and original word/pattern IDs. |
| `dist/app.js`, `dist/index.html`, `dist/style.css` | All 11 exercise types; combined tag filters; chapter availability; independent component selection and export headers; original full-pack view retained; public audit link removed. |
| `dist/bank.js`, `dist/chapters.js`, `dist/Cikgu-Sensai-offline.zip` | Rebuilt outputs. All 111 source packs and their wording preserved; topic genres normalised to the charter's provisional set. |
| `tests/test_catalogue.py` | Five passing test groups: source wording, pinned snapshot integrity, model structure, test-item references/matching, public audit exclusion. |
| `docs/DATA-MODEL.md`, `README.md` | Data contract, reproduction steps and limitations. |
| `docs/step2-preview.png` | Browser evidence of the component picker. |

Validation: `python build.py` passed all 899 page overflow checks;
`python -m unittest discover -s tests -v` passed; `node --check dist/app.js`
passed. Browser checks covered combined filters, selections across two chapters,
merged PDF, editable Word, ZIP with separate teacher keys and the honest
unavailable prerequisite-check state. Downloaded PDF had six pages, both chapter
headers were present in Word, and ZIP contained two student PDFs plus a key PDF.

## New words or patterns proposed for the ledger

None. No words added. The 982-row ledger snapshot and all nine chapter source
files retain their recorded SHA-256 hashes. Original word and frame IDs remain
unchanged. The five root decisions are local classifications, not ledger entries.

## Anything unverified or provisional

- All catalogue content remains draft. Japanese text awaits native-speaker review.
- 216 extracts are placements of existing material, not 216 newly authored lessons.
  Full suites, drill ladders, listening, culture, tests and fast summaries are not
  claimed complete. Missing component slots are marked not yet authored.
- Chapter goals follow the charter's drafts. Grammar mappings are provisional;
  source-word surface matches are incomplete evidence, not ledger compliance.
- Subtypes, timings, textbook links, prerequisite mappings and per-block goals
  without source support are explicitly unverified or awaiting authoring.
- Original source keys are retained and may answer other sections of that source.
  Component-specific keys are not invented in this step.
- Test-item fields and matching logic are implemented and fixture-tested. Actual
  prerequisite revision packs cannot yet be produced because no chapter tests or
  prerequisite mappings have been authored.
- English/Japanese grammar sequences and textbook alignments remain unassigned;
  no new courses or cross-language scene equivalences were invented.
- Legacy off-ledger, spoken-before-standard and forward-reference issues remain.
  Future chapter 12 stays inactive; Malay B1/B2/C1 families stay unplaced.

## Questions that block the next step

Step 3 introduces build-failing checks, while the preserved legacy bank contains
known violations. Before a passing step 3 release, Sam must decide whether to
authorise correction of those lesson texts or explicitly approve scoped legacy
exceptions. No exception or correction has been introduced here. Step 3 has not
started.
