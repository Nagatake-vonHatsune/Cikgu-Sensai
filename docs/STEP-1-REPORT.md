# Step 1: restructure for Sam's review

11 November 2026. Governing document: Unified Curriculum Charter v0.1,
sections Context and 12, with Sam's follow-up decisions in this chat.
Step 2 has not started. Kata-Kata and Hanashishou have not been modified.

Publication approval: Sam approved pushing step 1 to `main` and deploying the
Worker on 11 November 2026, following the initial automatic-review hold.
The matching GitHub commit and Cloudflare Worker check record publication status.
This approval does not authorize starting step 2.

## What changed, by file

| File | Change |
|---|---|
| `course.py` | Regroups existing resources into nine A1 chapters and the 13 planned unit slots. Moves the fruit-market family to 3B, chapter 12 outside Stage 1, and B1/B2/C1 families to unnumbered, unplaced provisional groups. Retains existing A2 lunch extension links. Generates recall from the reordered resource sequence. |
| `curriculum/malay-course.txt` | Reorders all 13 original six-line blocks; every block's text is unchanged. |
| `dist/app.js` | Adds unit filtering, shows resources in teaching order, displays placement status and empty-unit messages, and prevents Previous/Next from crossing out of Stage 1. Print-pack selections persist across chapter changes. |
| `dist/index.html` | Adds the unit control, issues-log link and Japanese-review notice. |
| `dist/style.css` | Ensures the unit control is hidden where no unit grouping applies. |
| `build.py` | Refreshes the offline ZIP after rebuilding the bank, preserving its source-plus-dist layout. Existing PDF overflow checks remain unchanged. |
| `dist/bank.js` | Regenerated 111-resource, 899-page bank. Eight generated resource level labels change A2 to A1; 12 generated recall lines change. All other resource text is preserved. |
| `dist/chapters.js` | Regenerated chapter navigation and unit placements. |
| `dist/Cikgu-Sensai-offline.zip` | Refreshed offline library, including the issues log and current source. |
| `tools/restructure_audit.py` | Reproducible reporting-only audit against a pinned external Kata-Kata snapshot. It does not edit lesson text, import curriculum into the runtime, or enforce build failures. |
| `dist/restructure-issues.md` | Human-readable issues log for all 13 planned units, future chapter 12, three advanced families and the linked A2 lunch extension. |
| `dist/restructure-issues.csv` | Occurrence-level evidence: unit, category, term, source, excerpt and ledger/affix detail. Includes exemptions and repeated occurrences, so row count is not an error count. |
| `docs/restructure-sources.json` | Reference revisions and SHA-256 hashes for the ledger, chapter files and affix guard used in the audit. |
| `docs/step1-preview.png` | Browser screenshot of the restructured chapter and unit guide. |
| `README.md` | Scope, content gaps and audit/build reproduction instructions. |
| `docs/STEP-1-REPORT.md` | This review report. |

### Resulting Stage 1 placement

| Chapter | Units | Existing resources |
|---|---|---|
| 1 Greetings | 1 | Greetings |
| 2 Pronouns and self-introduction | 2A, 2B | Introductions in 2A; 2B empty |
| 3 Numbers and money | 3A, 3B, 3C | Counting and quantities; Ringgit and sen plus the Beli buah di pasar family; Order and floors |
| 4 Time and routines | 4A, 4B | Clock time and Dates and days; Frequency and routines |
| 5 Adjectives | 5 | Taste and colour; Size and shape |
| 6 Comparatives and superlatives | 6 | Comparisons and superlatives |
| 7 Directions and locations | 7 | Asking where; Directions and orientation; linked Di, ke and dari sheet |
| 8 Penjodoh bilangan | 8 | Empty placeholder |
| 9 Passive di-, signs and notices | 9 | Empty placeholder |

All nine chapter labels are A1. The A2 lunch sheet retains its level as an
existing optional extension from 3B and 5; it is not a new A1 core lesson.
The 13 planned slots do not mean 13 complete charter units have been authored.

### Validation

- `python build.py`: all 899 PDF pages pass the existing full-size overflow assertion.
- Compared all 111 generated resources with baseline commit
  `d4813c3cb56cdc0a7cbe756284faae78c1d194dd`: same titles, page labels and lesson
  text, except the expressly permitted level and recall changes. Page indices
  are regenerated. All 13 raw lesson blocks are byte-for-byte equal after
  matching by title, disregarding their new order.
- Checked nine A1 chapter groups, 13 ordered unit slots, 3B placement, future
  chapter separation, three supplementary groups, and complete resource coverage.
- `node --check dist/app.js` passes.
- Browser checks: 3B shows the fruit-market family; 2B and chapter 9 show empty
  placeholders; chapter 9 Next is disabled; chapter 12 cannot be reached via
  Stage 1 Previous/Next; future and supplementary status labels are visible.
- Browser exports: merged PDF with included key, cross-chapter Word documents
  with separate keys, and separate PDFs with keys omitted all download
  successfully. Opened the downloaded PDF/ZIP/DOCX containers and checked page
  counts and Word document XML. Existing print buttons still use the same PDF
  generation path; a physical printer was not tested.

## New words or patterns proposed for the ledger

None. The log lists unmatched surface forms for review, not approved additions.
Each needs reconciliation with existing roots, phrases and placement before
Sam decides whether to add a ledger entry or revise a lesson in a later step.

## Anything unverified or provisional

- Existing vocabulary, register and affix issues are preserved, not corrected.
  The audit is provisional and includes Malay instruction language as well as
  taught examples. Exact-match failures are not automatically lexical errors.
- The reference ledger contains 982 rows; all 427 cards in chapter files c01–c09
  were available. This is a pinned snapshot, not a live spreadsheet check.
- Confirmed sequencing concerns include biji/sebiji in 3B before chapter 8;
  the reordered unit 5 uses atas/bawah before chapter 7; unit 6 uses antara/dalam
  before chapter 7. The CSV provides source excerpts and ledger IDs.
- Nak occurs in the greetings Malay explainer before standard mahu teaching.
  Short forms are not explicitly marked spoken in these legacy materials.
- Units 2B, 8 and 9 are placeholders. Existing content also falls short of the
  expanded grammar coverage in other units. No new content was written.
- B1/B2/C1 Malay packs remain unplaced and provisional at their existing levels.
  Chapter 12 is marked “Stage 2, not yet active”.
- Japanese text remains a draft awaiting native review. This step does not
  certify Malay usage, CEFR attainment or ledger compliance.

## Questions that block the next step

No unresolved restructure decision. Sam's approval is required before step 2.
The chapter-record schema, eleven selectable component types, prerequisite
tagging and build guards have not been started.
