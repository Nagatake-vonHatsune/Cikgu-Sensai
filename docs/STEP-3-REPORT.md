# Step 3 report — 11 November 2026

Implemented build checks with a frozen legacy baseline. Step 4 has not started.
The governing Google Doc was read directly, including sections 8, 12 and 13 in
full. Its URL, returned revision ID and list A coverage metadata are recorded in
`step3-charter-source.json`. No document edits were made.

## What changed, by file

| File | Change |
| --- | --- |
| `build.py` | Runs ledger-placement, register, affix and Malaysian-form checks before writing generated assets. Prints remaining exception and gap counts. |
| `language_checks.py` | Scope-aware checks, taught derivations, phrase-sensitive chunk exemptions, root exemptions, test-item scanning, frozen-baseline comparison and Git-history shrink enforcement. |
| `curriculum/malay-text-scope.json` | Explicit target spans for every existing Malay learner-body line. Rubrics, translations, explainers and teacher material are excluded. New or edited body lines require scope review; they are never silently skipped. |
| `curriculum/legacy-exceptions.json` | 86 existing violations, keyed by unit, check type and term, with reasons and source evidence. Ledger gaps are not exceptions. |
| `curriculum/legacy-baseline-lock.json` | Hashes of original exception entries, preventing expansion or alteration. Git history additionally prevents reintroducing a removed entry. |
| `curriculum/reauthored-units.json` | Initially empty. Add each unit when it is re-authored; the gate then rejects all remaining exceptions for that unit. |
| `tools/check_report.py` | Regenerates developer inventories and coverage reports without creating or expanding exceptions. |
| `docs/STEP-3-INVENTORY.md` | Complete per-unit/check baseline table and ledger-gap list with section 13 coverage. |
| `docs/step3-ledger-gaps.csv` | Machine-readable gap list, proposed chapters, coverage classification and source locations. |
| `docs/step3-check-results.json` | Full violation/gap evidence and accepted derivation inventory. |
| `docs/step3-charter-source.json` | Read provenance and proposed list A metadata only; not a replacement charter or approved vocabulary source. |
| `tests/test_language_checks.py` | Positive and negative tests for all four checks, scope exclusions, test items, derivations, shrinking exceptions and content/reference preservation. |
| `README.md` | Build, scope, baseline and re-authoring instructions. |
| `dist/bank.js`, `dist/Cikgu-Sensai-offline.zip` | Regenerated artifacts; lesson wording and page layout unchanged. Developer reports remain outside public assets and offline ZIP. |

### Baseline count per unit and check type

Counts are unique unit/check/term keys. Repeated occurrences share a key and retain
separate evidence. Existing keys permit that term/check in that unit until its
exception is removed; they are not approval of the wording.

| Unit | Ledger | Register | Affix | Malaysian form | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 5 | 0 | 0 | 0 | 5 |
| 2A | 2 | 0 | 0 | 0 | 2 |
| 2B | 0 | 0 | 0 | 0 | 0 |
| 3A | 2 | 2 | 0 | 0 | 4 |
| 3B | 21 | 6 | 0 | 0 | 27 |
| 3C | 4 | 0 | 0 | 0 | 4 |
| 4A | 1 | 0 | 0 | 0 | 1 |
| 4B | 0 | 2 | 0 | 0 | 2 |
| 5 | 4 | 3 | 0 | 0 | 7 |
| 6 | 1 | 1 | 0 | 0 | 2 |
| 7 | 0 | 2 | 0 | 0 | 2 |
| 8 | 0 | 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 |
| Future 12 | 4 | 6 | 0 | 0 | 10 |
| A2 lunch extension | 0 | 9 | 0 | 0 | 9 |
| B1 supplementary | 0 | 5 | 0 | 0 | 5 |
| B2 supplementary | 0 | 5 | 0 | 0 | 5 |
| C1 supplementary | 0 | 1 | 0 | 0 | 1 |
| **Total** | **44** | **42** | **0** | **0** | **86** |

The empty units have no authored content; zero does not certify a complete suite.

## New words or patterns proposed for the ledger

None added or newly proposed. All ledger/reference bytes are unchanged. Section
13 list A remains awaiting approval and is used only to classify gap coverage.

There are **371 unit/term gap records, representing 264 distinct surface/base
terms** across Stage 1, future 12 and supplementary material. The complete list
is in [STEP-3-INVENTORY.md](STEP-3-INVENTORY.md) and
[step3-ledger-gaps.csv](step3-ledger-gaps.csv).

List A covers 80 unit/term gap records (25 distinct surface forms):
45 would close the gap at the current chapter; 33 concern unplaced packs whose
chapter compliance cannot yet be determined; two add the term later than its
current use: **datang in 3B** and **selepas in 3C**, both proposed for chapter 4.
The other 291 unit/term records are not covered by list A.

Stage 1 has 36 distinct gap terms. Those appearing in list A are: barat, belas,
betul, cukup, datang, epal, ialah, ini, itu, kelakar, kelas, lintasan, mangga,
nombor, oh, pisang, puluh, pun, saja, selatan, selepas, timur, untuk, utara.
Those outside list A are: begitu, campur, cerita, kampus, lucu, memang, ni, rak,
setandan, sos, tali, tren. These are findings, not requests to add them. Several
are expressly designated for later rewriting in section 13 C.

## Anything unverified or provisional

- **Indonesian forms found: none** in scoped learner-facing Malay for the explicit
  charter list: nomor, bis, apel, setelah, beda, mobil, toilet, WC, karcis, toko,
  uang. This finite check does not certify every word against Kamus Dewan.
  `lucu`, for example, remains a gap designated for rewriting in section 13 C;
  it is not silently added to the section 8 deny-list.
- `beri`, `mesej`, `memang`, `mesti`, `beritahu` remain root exemptions. Their
  absence from the ledger, where applicable, is separately reported as a gap.
- `keempat` and `seminggu` pass through taught-rule/base checks. `ceritanya` is
  recognised as `cerita` + `-nya`; the unresolved gap is `cerita`, not a demand
  for a separate `ceritanya` card. `sebiji` still reports the counter's chapter 8
  placement when used in 3B. Derivation recognition is deliberately bounded by
  known bases/POS and chapter rules; uncertain lexical formations need review.
- All new gaps are non-blocking, as instructed. Existing ledger entries with a
  later chapter or no assigned chapter are lesson violations. A proposed list A
  entry never becomes taught vocabulary merely because it is proposed.
- Register checking requires an earlier target-language teaching occurrence of
  the standard form and a visible spoken label. Rubrics and task context do not
  establish teaching. This is a content-order check, not learner progress tracking.
- Chapter-relative ledger/affix checks cannot establish sequence compliance for
  unplaced B1/B2/C1 packs or the A2 lunch extension. Their register and
  Malaysian-form checks and ledger-gap reporting remain active. No chapter
  number was invented. Future 12 permits ber-/me-; full chapter 10–12 word data
  is not yet available.
- **Stage 1 rubrics and explainers must be Japanese or English when re-authored.**
  Existing Malay instructions remain unchanged and excluded from this baseline.
- Shrink enforcement requires a non-shallow Git checkout. A source ZIP can still
  be used offline as a site, but rebuilding the baseline requires Git history.

Validation: 14 tests pass, including unlisted-violation rejection, non-blocking
new gaps, every Indonesian deny-list entry, the five roots, chapter boundaries,
derivations, rubric exclusion, test-item scanning and forbidden baseline growth.
All existing source lesson files, 111 generated pack records, and reference
snapshots match the approved content. The full PDF build passes its 899 page
fit checks. Step 4 content was not authored or corrected.

## Questions that block step 4

1. List A is still unapproved. For the chapter 1/2 pilot, may `pun`, `oh` and the
   proposed chapter 2 terms enter the ledger through its owner/workflow, or must
   the pilot avoid them? No ledger addition will be made without approval.
2. Unit 1 currently uses bare `pagi`, `petang`, `malam` assigned to chapter 4 and
   `saya`, `awak` assigned to chapter 2. Should the pilot use chapter 1 fixed
   greeting chunks and remove those forward references, or should their ledger
   placement be revised by the ledger owner? The frozen exceptions must be
   removed when unit 1 is re-authored.

No charter changes are proposed. Later issues such as datang/selepas placement,
remaining gaps and supplementary sequencing can be resolved before their own
units are re-authored; they need not delay the chapter 1/2 pilot.
