# Stage 2 step 6c-1: the checker and the ledger rows with no chapter

**14 November 2026 · Claude.** Authorised by Sam (step 6c-1 instruction, 14 Nov 2026; push to main when the checks pass). Started at `843c1fb`. Kata-Kata was read only, at `e4e294d`.

## Result

- `python3 -m unittest discover -s tests`: **339 tests pass** (332 before, 7 new in `tests/test_stage2_step6c1.py`; `tests/test_stage_rules.py` now runs 95 shared fixtures instead of 81).
- `python3 build.py` passes: **557 packs, 3,456 pages**, as before.
- **Violations: 20, unchanged** (the same 20 unit/check/term keys, all in the frozen baseline, all in the four unplaced packs; none in a re-authored unit).
- **Ledger gaps: 188 before, 140 after** (unit/term records; 169 and 133 distinct terms). Why: 48 gaps in the four unplaced legacy packs (supplementary B1 11, B2 19, C1 16, the A2 lunch extension 2) now have an exact ledger row, because the bridge batch added the words (pelanggan, terima, bantu, dapat, kena, langkah, sahkan, tunjuk, beri, hanya, maklumat …). Those packs have no chapter, so a row there is an entry as before. No gap in a unit with a chapter changed. (The refreshed c04 and c06 vocabulary lines now print «baru / baharu»; «baharu» is a form of L-0195, so it is no gap.)
- **Every re-authored unit still has zero gaps and zero violations** (45 units in `curriculum/reauthored-units.json`; the build blocks a gap and the baseline cannot hold a violation for them; checked again from the check results).

## What went wrong, and the rule

With the 184 bridge rows (L-1310 to L-1493, Origin «Hanashishou bridge batch 1», no chapter) in the ledger, the shared checker read «biasanya», «akhirnya» and «terlalu» (words the classes teach whole, L-0184, L-1208, L-0273) as biasa, akhir and lalu plus an affix, and failed the roots as «no chapter assignment». Old checker with the new ledger: 31 violations instead of 20 (11 new, in 11 units, including Stage 1 and Stage 2 stage units and chapter 18). Kata-Kata step 6b worked around it with an origin-based exemption in its own checker only (`tools/stage-rules.mjs`). The rule below replaces that exemption and is written into the shared rules.

1. **A form that is itself a live ledger row with a chapter is checked at that row's chapter, as a whole word.** From that chapter on it is never split into a root and an affix. Before its row's chapter a regular derivation from a root that has a chapter still applies (see the deviation below).
2. **A row with no chapter never serves as a root or base** (-nya, -kah, -lah, se-, ke-, di-, -an, and the shape tests of every family). It makes no form legal and no placed form illegal. In a unit with a chapter it counts as no ledger row (the word is a ledger gap, as before the row existed); an affixed form of it still fails the stage-aware rule. In a unit with no chapter it is an entry, as before. A retired row is not "live" and keeps its old behaviour.
3. **Practice-pool rows keep «primes Ch18»**: the place cell still places them at 18, and «disemak» in unit 11B is still di- + «semak» (chapter 11).

### One deviation from the wording of rule 1 (please confirm)

Taken literally ("never split"), rule 1 would also stop «seminggu» (L-1275, chapter 10, a backlog row) from being se- + «minggu» when Stage 1 chapter 4 and 6 use it, and «sebulan» (L-1063, chapter 7) in chapter 6, and «disemak» (practice pool, chapter 18) in unit 11B. That adds new violations to frozen Stage 1 units and one to a re-authored unit, and it contradicts rule 3. So the rule starts at the row's own chapter: from there the whole word is checked, never split; before it, the old derivation from a placed root still applies. A dry run of the literal reading found exactly those 8 new violations (seminggu 4, sebulan 2, disemak 2), which is why I did not use it. If Sam wants the literal rule, those uses must change first.

## The code (`language_checks.py`)

- `Checker.placed`: the forms that have at least one row with a chapter. `known` (roots, bases, shape tests), the -nya, -kah, -lah and se- / di- / -an derivations, the family tags and the superlative test read only this set.
- `derivation()` returns nothing for a form whose own row is placed at or before the chapter (rule 1), so such words are no longer reported as derived forms (derivation records fell from 357 to 85; they were whole words all along: «adakah», «selalu» …).
- `Checker.rows_for(term, ch)`: in a unit with a chapter an unplaced live row is no row, so a bridge-only word is a gap, an unplaced multi-word row (a phrase such as «pusat beli-belah») is skipped and its words are checked one by one.
- Two follow-ons in the suite builder, found by the build: `suite/__init__.py` no longer calls a word «unmarked Malay» in English prose when all its rows have no chapter («had», «idea», «sedia», «dewan» are English words too), and `Ledger.terms_in` does not trace an unplaced row as a taught word (it gave «seorang» the Jambatan card id as a word id).
- `curriculum/stage-rules.json`: a new `format.ledger_rows_and_chapters` entry states the rule; `family_resolution` and `shape_tests` say that only a row with a chapter counts. No gate, list or number changed, so a reader that ignores unknown keys is unaffected.

## The fixtures (81 before, 95 after)

`curriculum/stage-rules-fixtures.json` has 14 new cases (two optional keys: `expect_gaps`, `expect_no_gaps`, terms that must or must not be ledger gaps, because a gap is not a violation):

| Case | What it holds |
| --- | --- |
| `biasanya-own-chapter-passes`, `akhirnya-…`, `terlalu-…` | pass at the row's chapter (4, 14, 6) and at 17; neither the word nor its bridge root is a gap |
| `biasanya-before-own-chapter-fails`, `akhirnya-…`, `terlalu-…` | fail (ledger) one chapter early (3, 13, 5) |
| `bridge-root-nya-form-stays-a-gap` | «salahnya» at 17: no violation, a gap |
| `bridge-root-ter-form-stays-a-gap` | «terakhir» at 17: no violation, a gap |
| `bridge-only-words-are-gaps-not-violations` | «salah», «biasa», «akhir», «lalu» at 17: gaps |
| `bridge-row-meN-form-stays-illegal` | «membantu» at 17 still fails (affix) |
| `placed-word-from-bridge-root-passes` | «selalu» (4), «terputus» (16), «rancangan» (11): placed words that are also derived forms of bridge rows pass, no root gap |
| `placed-word-from-bridge-root-before-own-chapter-fails` | «terputus» at 15 fails (affix) |
| `derivation-before-row-chapter-still-applies` | «seminggu» at 4 passes |
| `practice-pool-disemak-keeps-its-derivation` | «disemak» at 11 passes |

All 95 pass here. **Kata-Kata's guard must implement the two optional keys** and drop its bridge-batch exemption in step 6c-2; its case count and `SOURCE.json` hashes change (81 to 95).

## The refresh

Copied from Kata-Kata `e4e294d` (full hash `e4e294d8aa794a3e552470af5b1afd483098d44e`), read only:

- `curriculum/reference/katakata/c01.json` to `c18.json`: only **c04 and c06 changed** (cards ms-c04-041 and ms-c06-021, L-0195, now «baru / baharu»); the other sixteen are byte for byte what they were.
- Both ledger copies: **1,493 rows** (1,309 + 184). The reference copy keeps LF, `docs/handoff/ledger-snapshot.csv` is the Kata-Kata file byte for byte (CRLF).
- `docs/step4-sources.json` (commit, full hash, row count, ledger and chapter hashes, a refresh note), the two pinned-source tests, the row-count and open-action tests, and `catalogue.py` (source URLs) now name `e4e294d`. L-0195 and L-1303 keep a Kata-Kata Action cell on the sheet (Kata-Kata did not clear them; the sheet is not ours), and the test allows both.
- The rebuilt `dist/` and `docs/step4-authored-scope.json` carry the «baru / baharu» vocabulary lines.

### Core is still 270

Compared row by row with the previous ledger: 184 rows added (all Draft, all no chapter, all place «Jambatan · …»), 80 rows changed (group (a): 78 got a Jambatan card id and place, 2 are the practice-pool rows L-1308 and L-1309, which got a Jambatan scene note and keep «primes Ch18»), 2 rows with a changed Hanashishou or In-both cell, L-0195 and L-1303 with new Action text. The set of rows with a chapter is unchanged (1,042), the Stage 2 core set is the same 270 rows, none of the 184 or 80 rows is in any unit's core list or fast pack (`tests/test_stage2_step6c1.py`).

## For Kata-Kata step 6c-2

Copy `curriculum/stage-rules.json` and `curriculum/stage-rules-fixtures.json` from the rules commit **909596e03db373b14de213ad64f8a0a73afdeea7** (the same two files are in every later commit of this step). The final `main` hash is in `HANDOFF.md` and in the session reply.

## Left alone, for Sam

- Kata-Kata step 6c-2 copies the rules and fixtures from the commit named in `HANDOFF.md` and removes its exemption.
- The ledger sheet's Action cells on L-0195 and L-1303 still name Kata-Kata work that is done.
- Ledger Journal row 217 (the «biasa / akhir / lalu» question) is answered by this rule; the sheet is not ours to edit.
- The rule 1 deviation above.
