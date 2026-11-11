# Step 4 report: pilot suites for units 1, 2A and 2B (11 November 2026)

Step 4 is built and has stopped for your review. Units 1, 2A and 2B each have the full eleven-component suite. Unit 1 also has the pronunciation block, and unit 2B the writing block. Both fast-course summary packs (chapters 1 and 2) are done.

Every component meets the section 6 content minimum, and every unit has all six section 14 drills plus the cumulative question-word drill. A test checks each minimum (`tests/test_step4_suite.py`), so none of this rests on my word alone.

All pilot Malay passes the ledger, register, affix and Malaysian-form checks with no exceptions. It also contains no word missing from the ledger. The next step is for you to teach the pilot; the suite template is frozen only after your feedback (charter section 10).

## Sources read

- **Charter:** the live Google Doc, read in full through Drive. Its content matches `docs/handoff/charter-snapshot.md`; the differences are formatting only.
- **Ledger:** the live sheet (Ledger tab, rows L-0001 to L-1015) is identical, cell for cell, to `docs/handoff/ledger-snapshot.csv`. I refreshed `curriculum/reference/katakata/malay-ledger.csv` from it. Line endings are kept as before, so the diff shows only the 8 changed and 33 new rows. Provenance and the file hash are in `docs/step4-sources.json`.
- **Kata-Kata chapter files:** `c01.json` to `c09.json` are unchanged.

## What was built

| Unit | Components (sheets) | Ledger words in its vocabulary focus | Test items | Listening (Malay words) | Culture note (English words) |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 (ms-c01) | 11 types; 7 drill sheets; pronunciation block (18 sheets) | 45 (all chapter 1 rows) | 17 + 1 speaking | 122 | 191 |
| 2A (ms-c02a) | 11 types; 7 drill sheets (17 sheets) | 40 | 17 + 1 speaking | 124 | 192 |
| 2B (ms-c02b) | 11 types; 7 drill sheets; writing block (18 sheets) | 52, plus «di manakah» as review | 17 + 1 speaking | 124 | 187 |
| Fast pack, chapter 1 | 1 pack, 3 pages | 20 core words | 4 self-check items | n/a | n/a |
| Fast pack, chapter 2 | 1 pack, 3 pages | 20 core words | 4 self-check items | n/a | n/a |

### Section 6 minimums, unit by unit

All three units meet every minimum below.

| Component | Minimum | Status |
| --- | --- | --- |
| Vocabulary focus | Every ledger word for the unit, grouped, with JA and EN meanings and an example; spoken forms marked | Met |
| Pattern and grammar | 3 to 5 patterns; each with a box, 4 to 6 Q&A examples, explanations in JA and EN, and a "Japanese helps or misleads" note | Met (5 / 4 / 5 patterns) |
| Drills | Six section 14 types; at least 6 items each for types 1 to 5; at least 3 dialogues for type 6; cumulative question-word drill | Met (8 to 10 items per type; 4 dialogues) |
| Model conversation | 10 to 16 turns, a gapped version, and a variant with changed facts | Met (12 / 14 / 14 turns) |
| Listening | Encik Tanaka script of 120 to 250 words; before, during and after tasks; at least 6 items | Met (8 or 9 items) |
| Reading and writing | Real text with at least 5 questions; guided writing with a model answer | Met |
| Task | Role cards A and B, change of plan, success criteria | Met |
| Culture note | 150 to 300 words | Met |
| Test | 15 to 20 items (listening, words and grammar, reading) plus 1 speaking; all tagged; separate key | Met (17 + 1) |
| Teaching plan | Block timings, prompts, expected answers, Kata-Kata set before and after | Met |
| Fast pack | 2 to 4 pages; goals, 15 to 20 words, patterns with 2 examples each, conversation, task, self-check, self-study guide | Met |

Every sheet prints with a header giving language, level, unit, type, minutes and draft status. The header also says the Japanese is awaiting native review.

Malay target text prints in dark blue, and roots quoted from Kata-Kata notes print in italics. On the Malay explainer page, A1 sheets say that explainers are in Japanese or English (your 11 Nov decision).

## What changed, by file

| File | Change |
| --- | --- |
| `suite/__init__.py`, `ms_c01.py`, `ms_c02a.py`, `ms_c02b.py`, `fast.py` | **New.** The pilot content and its builder (markup, ledger lookups, pagination, scope generation). |
| `build.py` | Builds the suites and paginates them by measuring each page. Renders the compact style. Supports multi-page teacher keys. Writes `docs/step4-authored-scope.json` and adds `suite/` to the offline ZIP. Legacy pages render exactly as before. |
| `course.py` | Units 1, 2A and 2B now point to the suites, and fast packs are placed in their chapters. The legacy Greetings and Introductions packs are retired. Also fixes an index (`groups[13:]`) that the retirement would have broken. |
| `catalogue.py` | Authored components carry their full tag set from the source. Adds the 54 test items, the new grammar points, pilot block goals, prerequisites for chapter 2, and Kata-Kata Dunia and ledger-only words in the word registry. Prerequisite matching now includes earlier units. |
| `language_checks.py` | Adds a proper-noun list, sourced mentions (Malaysian-form check only) and checking of authored keys, plans and explainers. Re-authored units now fail on any ledger gap. An unplaced multi-word ledger row such as "encik pula" no longer hides the placed words it is built from. |
| `curriculum/legacy-exceptions.json` | 86 → 79 entries: the 5 unit 1 and 2 unit 2A exceptions are removed. |
| `curriculum/reauthored-units.json` | Lists ms-c01, ms-c02a, ms-c02b, ms-c01-fast and ms-c02-fast. |
| `curriculum/malay-proper-nouns.json`, `curriculum/malay-mentions.json` | **New.** Names used in the suites, and the 29 quoted roots and forms, each with its source. |
| `curriculum/malay-text-scope.json` | Removes the 32 lines of the retired packs and updates one 3B line (next row). |
| `curriculum/foundation-guided.txt` | **One legacy line changed (unit 3B).** "Pukul lapan. Nak datang lagi?" becomes "Pukul lapan. Nak beli lagi?". The refreshed ledger places «datang» in chapter 4 (L-1006), and that row's action note asks for this rewrite. Without the change the build fails, because the baseline cannot grow. |
| `curriculum/reference/katakata/malay-ledger.csv` | Refreshed from the sheet (see Sources read). |
| `dist/app.js`, `dist/index.html` | Multi-page keys and pilot status text. The "Check prerequisites" button now adds the matching earlier test sheets to the front of the pack and lists the matching item IDs. |
| `tests/` | Step 2 and 3 tests updated to the step 4 invariants (only the retired packs and the one 3B line differ). New tests cover the check changes, and `test_step4_suite.py` covers the minimums and drills. 31 tests pass. |
| `docs/step4-sources.json`, `docs/step4-authored-scope.json`, `docs/step4-preview.png`, `.gitignore` | **New.** |

Check totals now: 79 legacy exceptions; 70 current violations, all covered by those exceptions; 283 ledger gaps, all outside the re-authored units. There are 0 gaps in the pilot.

## New words or patterns proposed for the ledger

None were added. Please decide on each:

1. **‹Waalaikumsalam›**, chapter 1. It is the reply to «Assalamualaikum». It appears only in the Kata-Kata card note, and the culture note quotes it from there.
2. **Hobby nouns for chapter 2.** The ledger has none at chapter 2. Kata-Kata's own frame example uses «badminton», which the ledger places in chapter 6. The pilot uses «Saya suka masakan Malaysia» and has learners supply their own hobby word.
3. **«sikit je» (L-0948, chapter 2 via a Dunia scene).** Its standard form ‹sedikit› is in chapter 5, so the register rule bars it before then. I left it out of unit 2A. Either move «sedikit» to chapter 2 or drop «sikit je» from the scene.
4. **Patterns.** No new frames. Unit 2A teaches «Ini ___. Namanya ___.» inside frame f01. Unit 2B's pe- and -an box is a grammar point (ms-c02-g10 and g11), not a frame.

## Findings for Kata-Kata (not changed here)

- The chapter 2 scenario uses «dari mana» (ledger chapter 7) and «badminton» (chapter 6). The pilot asks «Kampung encik di mana?» instead.
- Chapter 1 still has no Dunia scene. Block E of unit 1 uses the Kata-Kata chapter 1 scenario "First day at the office" in its place.

## Unverified or provisional

- **All Japanese** is an AI draft awaiting native review. Every sheet says so.
- **Pronunciation notes** (unit 1) are general knowledge, not checked against a reference: the two sounds of e, the final k, kh and stress.
- **Name customs** (unit 2A culture note): the paragraph on Malay and Chinese Malaysian names is general knowledge.
- **Etymologies** come from Kata-Kata card notes only. Your own etymology notes were not available to me; each culture note's key says where to add them.
- **"Japanese helps or misleads" notes and usage remarks**, for example that «Apa khabar?» is used more widely than お元気ですか. These are my drafts for you to check.
- **The Kamus Dewan check** for L-0983 to L-1015 has still not been run.
- **Unit 2B's vocabulary list is long**: 52 ledger rows against the usual 20 to 40. Chapter 2 has 95 rows, 26 of them Kata-Kata Dunia scene words, which I marked "recognise". Unit 2A has 40.
- **Timings** are planning figures until you have taught the pilot. So are the self-study hours.
- **Prerequisite check:** the button adds whole earlier test sheets and lists the matching item IDs. It does not yet print a cut-down sheet with only those items.

## Questions for Sam

1. Approve or reject the three ledger proposals above: ‹Waalaikumsalam›, hobby nouns for chapter 2, and «sikit je».
2. Is a 52-word vocabulary list acceptable for unit 2B, or should the 14 office scene words move to Block E only?
3. Where are your etymology notes, so the culture notes can draw on them?
4. Still open from before: which textbooks the other Japanese teachers use, and the explainer language for Japanese packs.

How to review: open `dist/index.html`, choose Malay, chapter 1 or 2, and pick a unit. `docs/step4-preview.png` shows three sample pages.
