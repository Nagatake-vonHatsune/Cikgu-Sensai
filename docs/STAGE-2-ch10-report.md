# Stage 2 build step 4: Kata-Kata refresh and chapter 10 (units 10A and 10B)

**13 November 2026 · Claude.** Authorised by Sam (build step 4 instruction, 13 Nov 2026): refresh the Kata-Kata reference copy, then author the chapter 10 suites; push to main when the checks pass; stop after chapter 10 for Claude's review before chapters 11 to 17. Started at `a24a993`. Kata-Kata (read only) at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited.

## Summary

Part 1 (commit `382dfec`) brought in Kata-Kata's chapters 10 to 18 and the ledger as Kata-Kata synced it. Stage 2 now has **240 core words** (233 planned + 7 that Sam added later). The checker results did not change: **22 violations and 203 ledger gaps before and after.** Part 2 adds chapter 10 as two full A2 units (10A and 10B, five 45-minute blocks each), the writing block after 10B and the chapter 10 fast pack. All three are registered as re-authored, so they must have **zero ledger gaps and zero violations**, and they do. `python3 build.py` passes (373 packs, 2,356 pages, all fit-checked; still 22 violations and 203 gaps, all from older content). All **180** tests pass (167 before, plus 13 in the new `tests/test_stage2_ch10.py`).

## Part 1: refresh

- **Copied** Kata-Kata `content/ms/kelas/c10.json` to `c18.json` into `curriculum/reference/katakata/`. `c01` to `c09` are byte for byte the same as before (Kata-Kata 34710c6). Both ledger copies come from Kata-Kata `content/ledger/malay-ledger.csv`, following the Stage 1 sync (f06aefd): `docs/handoff/ledger-snapshot.csv` is the Kata-Kata file byte for byte (CRLF), and `curriculum/reference/katakata/malay-ledger.csv` is the same file with LF line endings. The ledger now has 1,272 rows (L-0001 to L-1272) and 237 changed rows: class card IDs on 194 rows that had none, Jambatan IDs replaced by class cards on 43 rows, affix tags on 20 rows, and the L-1261 note. There are 7 new rows: L-1266 «takpe», L-1267 «tidak boleh tahan», L-1268 to L-1272. Hashes and the commit are pinned in `docs/step4-sources.json`, and `catalogue.py` links to 7fbe173.
- **Stage rules:** Kata-Kata `content/rules/SOURCE.json` pins Cikgu Sensai `a24a993`. Its `stage-rules.json`, `stage-rules-fixtures.json` and `malay-proper-nouns.json` are **byte for byte** the files in `curriculum/` here (same SHA-256).
- **Counts:** 240 Stage 2 core rows = 56 existing + 184 new. By chapter: 10 = 40, 11 = 41, 12 = 44, 13 = 25, 14 = 22, 15 = 21, 16 = 23, 17 = 24. I recounted these from the ledger and updated them in `docs/stage-2-plan.md` (the totals table, the unit totals for 13, 14, 15 and 17, the per-chapter line and a new "Build step 4" section) and in `HANDOFF.md`.
- **Tests changed** (for the new pin only): `test_catalogue.test_pinned_sources` and `test_language_checks.test_no_content_or_reference_edits` now pin c01 to c18 at 7fbe173. In `test_step5h_stage1`, the ledger row count is 1,272 and the card check reads every pinned chapter.
- **Before and after:** 22 violations and 203 gaps in both, with 167 tests passing.

### Every other place that states 233 (for the charter update)

The **live charter does not state 233** (I read revision `AHj4eMSiZ2Bi…`, the same one HANDOFF records; no 23x figure appears) and neither does `docs/handoff/charter-snapshot.md`. These places do:

| File | Where | Status |
| --- | --- | --- |
| `docs/stage-2-plan.md` | Section 2 heading line, the totals table, unit 13/14/15/17 totals, the "Core totals by chapter" line, the build step 1 note, the audit log item 1 | Updated to 240 (the audit log keeps 233 as history) |
| `HANDOFF.md` | The build step 1 and Batch 1b entries | 240 added beside the historical 233 |
| `docs/stage-2-decisions.md` | Section 2 lead line ("233 … with «bertolak» 234") | Not changed: it is Sam's answered brief |
| `docs/STAGE-2-audit-report.md` | Item 2 (211 of 235 kept …) | Not changed: audit history |

If Sam wants the charter to state a Stage 2 total, the figure is **240 core words (56 existing + 184 new)**.

## Part 2: chapter 10

### Blocks and timings

| Block | Unit 10A: the working day | Unit 10B: background and neighbours | Minutes |
| --- | --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns f01 and f02 20, first substitutions 5 | Same timings: patterns f05 and f06 | 45 + 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | Same; the transformation drill starts with spoken to standard | 45 + 45 |
| C | Listening (Aini's routine) 15, reading (a team message) and writing 10, task (find a time to play badminton) 15, recall 5 | Listening (Siti's gathering) 15, reading (a residents' chat message) and writing 10, task (meeting a neighbour at the lift) 15, recall 5 | 45 + 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview 10 | Same | 45 + 45 |
| E | Scene transfer: Kata-Kata scenario s01 to s09 as listening 10, role-play 15, changed workday 10, culture note 5, recall 5 | Kata-Kata s10 to s19 as listening 10, role-play at the lift 15, a different neighbour 10, culture note 5, recall 5 | 45 + 45 |
| Extra | — | **Writing block** after 10B: recall 5, model and notice 10, guided draft 15, feedback 10, rewrite 5 | 45 |
| Fast | Chapter 10 fast pack, one 45-minute session for both units | | 45 |

Full course: **11 blocks = 8.25 class hours** for chapter 10, as in the plan (two units × 5 + the writing block). Self-study planning figure: 3 hours per unit. Fast course: 1 block and 9 to 10 hours of self-study.

### What each unit contains

Both units have all 11 components and meet every section 6 and section 14 minimum. The test file checks them.

| | 10A | 10B |
| --- | --- | --- |
| Core / recognition / revision | 20 / 0 / 35 | 20 / 1 («pindah») / 35 |
| Patterns (Kata-Kata frames) | f01, f02, f03, f04 (6 Q&A each) | f05, f06, f04, f03 (6 Q&A each) |
| Drills | 8 + 8 + 10 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks | 8 + 8 + 10 + 8 + 8, 5 short dialogues, 8 markers, 18 question words |
| Model conversation | 14 turns (Kata-Kata s01 to s09 extended), gapped, a 10-turn variant (Rahman and Mei Ling) | 14 turns (s10 to s19 extended), gapped, a 10-turn variant (Kumar and Rina) |
| Listening | 136 Malay words, 9 questions (Aini's day) | 131 words, 8 questions (Siti's gathering: Rashid, Farah, Encik Lim) |
| Reading and writing | A team chat message and a bus-stop sign, 7 questions; write your routine | A residents' chat welcome, 7 questions; a self-introduction message |
| Task | Find a time for badminton; change: B works until eight on Thursday | Meeting at the lift with persona cards; change: B is moving to Penang next month |
| Culture and usage note | 211 words: standard ber- forms against everyday roots, the ber- spelling rule, «bertolak» and «berhenti kerja» | 182 words: «hidup berjiran», gatherings and open houses, formal «bernama» and «berumur», «pindah», «belanja» |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) | Same (20 + 1) |

**Kata-Kata alignment:** the same frames f01 to f06. All six frame examples and all 19 scenario lines appear word for word in the units, with 10A using s01 to s09 and 10B using s10 to s19. Card IDs are cited in the openers (10A: ms-c10-001 to -020; 10B: ms-c10-021 to -041), the vocabulary (root notes), the teacher notes (traps ms-c10-013, -015, -020, -021, -025, -032, -041) and the culture sources. The classroom version adds role-plays with a change of plan, pair work in every block, a teacher-read listening, a written message in Block C and the 45-minute writing block.

**The ber- rule:** each ber- verb is its own ledger row and appears with its root, using the root given in the Kata-Kata card note. A root that is a ledger word placed by chapter 10 is shown as Malay; any other root is a ‹…› mention, sourced in `curriculum/malay-mentions.json` (19 new entries). Pattern 1 teaches the spelling: no nasal sound changes, ‹be-› before r and in «bekerja», ‹bel-› only in «belajar». The test file checks that every ber-shaped word is a ledger row placed by chapter 10, and that no meN-, -kan or -i form appears. Misspellings appear only as starred plain text, for example *berrehat.

**Rules applied:** standard forms first. Everyday roots («kerja», «sarapan», «Asal saya …», «Nama saya …») are taught as correct speech, with the ber- form taught first. «pindah» is recognise only: it is labelled spoken wherever it appears, and it never appears in a key, a dialogue or the listening. No «lah», «kan», «tak», «dah», «takpe» or «tak apa» appears in either unit (the «tak apa» register pair applies from chapter 10, but «tidak mengapa» is not taught until chapter 17). No faith-specific expression and no Indonesian form. Learners never have to give real family details: there are persona cards, and «Belum.» counts as a complete answer.

### Core-word coverage

All 40 core words appear in their unit outside the vocabulary list. The test file checks this, and also checks that every revision word is really used.

| Ledger | Word | Unit | Kata-Kata card | Components that use it (outside the vocabulary list) | Unit test | Fast pack |
| --- | --- | --- | --- | ---: | --- | --- |
| L-0807 | bersiap | 10A | ms-c10-016 | 5 | practised only | — |
| L-1101 | bersarapan | 10A | ms-c10-013 | 16 | tested | yes |
| L-1106 | bertolak | 10A | ms-c10-020 | 16 | tested | yes |
| L-1090 | berjalan | 10A | ms-c10-002 | 6 | tested | — |
| L-1100 | beratur | 10A | ms-c10-012 | 3 | tested | — |
| L-1102 | bermula | 10A | ms-c10-014 | 15 | tested | yes |
| L-1089 | bekerja | 10A | ms-c10-001 | 9 | tested | yes |
| L-1093 | berehat | 10A | ms-c10-005 | 10 | tested | yes |
| L-1103 | berhenti | 10A | ms-c10-015 | 10 | tested | yes |
| L-1105 | rutin | 10A | ms-c10-019 | 2 | practised only | — |
| L-1091 | bercakap | 10A | ms-c10-003 | 8 | practised only | yes |
| L-1099 | berbual | 10A | ms-c10-011 | 6 | tested | — |
| L-1098 | berjumpa | 10A | ms-c10-010 | 8 | tested | yes |
| L-0916 | bersedia | 10A | ms-c10-017 | 6 | tested | — |
| L-1092 | bermain | 10A | ms-c10-004 | 8 | practised only | — |
| L-1094 | bersenam | 10A | ms-c10-006 | 11 | tested | yes |
| L-1095 | berenang | 10A | ms-c10-007 | 11 | tested | yes |
| L-1096 | berlari | 10A | ms-c10-008 | 3 | practised only | — |
| L-1097 | berbasikal | 10A | ms-c10-009 | 7 | practised only | — |
| L-1104 | berlatih | 10A | ms-c10-018 | 5 | tested | — |
| L-1110 | berasal | 10B | ms-c10-024 | 17 | tested | yes |
| L-1111 | bernama | 10B | ms-c10-025 | 8 | tested | — |
| L-1107 | berumur | 10B | ms-c10-021 | 10 | tested | — |
| L-1108 | berkahwin | 10B | ms-c10-022 | 10 | tested | yes |
| L-1109 | berkeluarga | 10B | ms-c10-023 | 4 | practised only | — |
| L-1112 | bersekolah | 10B | ms-c10-026 | 8 | tested | yes |
| L-1122 | berdua | 10B | ms-c10-040 | 9 | tested | yes |
| L-0714 | sepupu | 10B | ms-c10-038 | 4 | tested | — |
| L-0660 | jiran | 10B | ms-c10-037 | 8 | tested | yes |
| L-0779 | berjiran | 10B | ms-c10-028 | 9 | tested | yes |
| L-0781 | berkenalan | 10B | ms-c10-034 | 12 | tested | yes |
| L-1113 | berkawan | 10B | ms-c10-027 | 4 | practised only | — |
| L-1118 | berkumpul | 10B | ms-c10-033 | 15 | tested | yes |
| L-1114 | berpindah | 10B | ms-c10-029 | 17 | tested | yes |
| L-1115 | bercuti | 10B | ms-c10-030 | 7 | practised only | yes |
| L-1116 | berniaga | 10B | ms-c10-031 | 6 | tested | — |
| L-1117 | berbelanja | 10B | ms-c10-032 | 5 | practised only | — |
| L-1119 | berminat | 10B | ms-c10-035 | 4 | practised only | — |
| L-1120 | berpakaian | 10B | ms-c10-036 | 2 | practised only | — |
| L-1121 | pengalaman | 10B | ms-c10-039 | 4 | tested | — |
| L-0667 | pindah | 10B (recognise only) | ms-c10-041 | vocabulary and labelled notes only | never in a key | named as spoken |

"Practised only" means the word is drilled and used in scenes but is not one of the 19 or 20 scored test items. Each unit test samples its 20 core words (charter: 15 to 20 items).

### Code and data changed

- `suite/chapter10_common.py`: a **Stage 2 helper** based on `chapter9_common.py`. Its differences: the chapter number, unit id, grammar ids, question-word note, markers drill and Block E all come from the unit config; Block E is a scene transfer (no Dunia scene primes chapter 10); the "To recognise" group holds the ledger's recognition rows and is omitted when empty; the test key accepts any natural Malaysian answer; the extra block has a timed plan. Chapters 11 to 17 can **import it unchanged** and pass their own config.
- `suite/ms_c10a.py`, `suite/ms_c10b.py` (with the writing block), and the chapter 10 fast pack in `suite/fast.py` (`STAGE2_PACKS`).
- `suite/__init__.py`: grammar points ms-c10-g02 to g08. A unit's `level` (A2) now sets the page header and the bank level; Stage 2 pages carry a Malay-explainer note (see question 1). There are three `GLOSS` entries for the fast-pack word list, and «badminton» and «travel» are now English homographs.
- `course.py`: chapter 10 «ber- verbs» (10A, 10B), level A2, sequence "stage2".
- `catalogue.py`: ten chapters, chapter 10 at A2 with stage id `ms-stage2`, planned pattern returns 11, 13 and 18, and the additional block `ms-stage2-writing-10b`. An authored component takes its level from the page.
- `curriculum/reauthored-units.json`: ms-c10a, ms-c10b and ms-c10-fast added. `curriculum/malay-mentions.json`: 19 entries added (the roots, ‹be-›, ‹bel-›, ‹pe-›, ‹hidup berjiran›) and `latih` extended. Each entry names its Kata-Kata card note or ledger row.
- `tools/check_spans.py`: checks every «…» span in a file at one chapter (the build's checker, register pairs excepted). Run it on each unit file before building; both chapter 10 units report 0 problems.
- Tests: `tests/test_stage2_ch10.py` is new, with 13 tests written so chapters 11 to 17 can copy them. `test_catalogue.test_structure` now expects 10 chapters, 15 units, 75 blocks and 165 slots, levels A1 × 9 + A2, and stage ids. In `test_step5h_stage1`, the goals test compares the first nine goals and the catalogue test allows A2 from chapter 10. No Stage 1 content changed.

## Lines a native speaker should read first

These are my judgement calls, so please read them first. Everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. 10A P3: «Tidak sangat. Saya suka berbasikal.» Is "not really" natural in this form, or would «Kurang suka» or «Tak sangat» (spoken) be better?
2. 10A P4 and the 10B listening: «Saya berbual dengan rakan sekerja.» «rakan sekerja» comes from Dunia, chapter 2. Is it natural here?
3. 10A listening: «Waktu pagi, ramai orang beratur di stesen. Kereta api selalu sesak.» Is «sesak» natural for a crowded train? The ledger glosses it as traffic.
4. 10A listening: «Saya hantar anak ke sekolah dulu.» Everyday root «hantar» (Dunia, chapter 2).
5. 10A task key: «… tetapi petang saya ada masa.»
6. 10A Block E: «Hari ini saya bekerja dari rumah.» (working from home).
7. 10B P2 and the teacher notes: the claim that «Belum.» is the natural answer to «Sudah berkahwin?», and that «Tidak berkahwin» sounds like a firm "I don't marry". [INFERRED; please confirm.]
8. 10B P4 and the reading: «Isteri saya berminat untuk belajar masak.» Should it be «belajar memasak» (chapter 11) or «belajar masak»? I teach «berminat» only with «untuk» + a verb, so «berminat dengan / dalam» + a noun is not taught; see question 4.
9. 10B listening: «Saya sudah berkeluarga. Anak saya bernama Ken.» Is «bernama» natural in speech when introducing your own child?
10. 10B dialogue (Kata-Kata s18, Sam's question there too): «Encik dan isteri datang, ya!» as an invitation, and «Itu pun bagus!» (s08).
11. 10B drill: «Rumah Puan Siti yang mana?» → «Yang di sebelah lif.»
12. 10B culture: the sentence that many Japanese professionals live in a condominium or terrace house. This is general knowledge and I found no source, so it is labelled that way in the key.

All Japanese is a draft for the native review. The pattern bridges («やめる» covering both stop and quit, «休む» covering both «berehat» and «bercuti») are teaching hypotheses.

## Word proposals for Sam (not in the ledger; I rewrote the lines instead and added no rows)

| Proposed form | Why it came up | What the unit says instead |
| --- | --- | --- |
| «kolam renang» (swimming pool) | Where people swim | «Pada hari Sabtu saya berenang.» |
| «taman» (park) | Where people run or cycle | «Saya berlari selepas kerja.», «berbasikal dengan kawan» |
| «seminggu» (a week; «tiga kali seminggu») | Frequency of exercise | «setiap hari Isnin, Rabu dan Jumaat» |
| «penuh» (full: a full train) | Morning trains | «Kereta api selalu sesak.» (see native line 3) |
| «bersukan» (to do sport) | A natural general verb | «bersenam» or «bermain» + the sport; *bersukan is named only as "not taught" |
| «hidup» (for ‹hidup berjiran›) | The ledger gloss of L-0779 | Quoted as a ‹…› mention, not taught |

## Questions for Sam

1. **Malay explainers for Stage 2.** Stage 1 pages say "no Malay explainer" (your 11 Nov decision). I kept that rule for chapter 10 and worded the note as "until Sam decides otherwise". Should Stage 2 keep Japanese and English explainers only?
2. **Scope check.** I built the chapter 10 fast pack and the writing block as well as the two units, because the plan's step 4 lists them with chapter 10. Is that what you wanted for this step?
3. **Native line 7.** Is «Belum.» the right thing to teach as the polite "not married (yet)"?
4. **«berminat» + a noun** («berminat dengan muzik», «berminat dalam sukan»). Teach one form at chapter 10, or keep «berminat untuk» + a verb (my default)?
5. **Hanashishou.** The plan links chapter 10 to `grab_ride_chat` and `new_neighbour`, but neither is tagged by chapter yet (build step 6), so the units name them and do not assign them. Is that acceptable until step 6?
6. **Additional-block ids.** Stage 2 blocks are named `ms-stage2-<name>` (for example `ms-stage2-writing-10b`), following Stage 1's `ms-stage1-<name>`. Is that fine?

## Not verified

- **Kamus Dewan:** none of the chapter 10 forms was checked (end of the project, ledger Journal row 128). The be- spelling rule remains [INFERRED] from secondary sources (plan section 3).
- **Facts:** the culture notes state no figure, rule or date about Malaysia. The open-house sentence reuses chapter 9's sources (search summaries only). One general-knowledge sentence is labelled as such.
- **PDF:** I rendered four pages for a visual check (10A pattern page, 10B vocabulary, the writing block and the fast pack). The rest were checked only by the build's fit check.
