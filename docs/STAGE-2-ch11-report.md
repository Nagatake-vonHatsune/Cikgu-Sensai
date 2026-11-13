# Stage 2 build step 4, chapter 11: units 11A and 11B (meN- verbs)

**13 November 2026 · Claude.** Authorised by Sam (build step 4, chapter 11 instruction, 13 Nov 2026): one chapter 10 fix, then the chapter 11 suites; push to main when the checks pass; **stop after chapter 11 for Claude's review** before chapter 12. Started at `8ada95c`. Kata-Kata (read only) is the pinned copy at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited.

## Summary

- **Chapter 10 fix (its own commit, `0853da9`).** 10A pattern 3 now reads «Tidak juga. Saya lebih suka berbasikal.» (Sam: «Tidak sangat» is not natural), with an English and Japanese note on «Tidak juga» and «lebih suka». The chapter 10 report's native-read list is updated. Sam's six answers to the chapter 10 questions are recorded in `docs/stage-2-decisions.md` section 7. No word proposals from chapter 10 were added.
- **Chapter 11.** Two full A2 units (11A and 11B, five 45-minute blocks each), the **review block after 11B** and the chapter 11 fast pack. All three are registered as re-authored in `curriculum/reauthored-units.json`, so they must have zero ledger gaps and zero violations, and they do. `python3 build.py` passes (411 packs, 2,572 pages, all fit-checked; still **22 violations and 203 gaps, all from older content**, none in chapter 11). All **193** tests pass (180 before, plus 13 in the new `tests/test_stage2_ch11.py`).
- **One scope decision for you** (question 1): the plan gives chapter 11 a **review block** after 11B and no writing block (writing blocks follow 10B, 12A, 14 and 16). Your brief says "the chapter 11 writing block". I built the plan's review block and no writing block, so the 67-block, 50.25-hour total still holds.

## Blocks and timings

| Block | Unit 11A: who did what at the office | Unit 11B: the draft, the deadline and the weekend | Minutes |
| --- | --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns f01 and f02 20, first substitutions 5 | Same timings: patterns f04 and f06 | 45 + 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | Same; the transformation drill starts with spoken to standard | 45 + 45 |
| C | Listening (Rahman and the file from Osaka) 15, reading (a team message) and writing 10, task (who did what with the file?) 15, recall 5 | Listening (Mei Ling's weekend and the draft) 15, reading (a message about a draft, a room-for-rent notice) and writing 10, task (check a draft and confirm when it will be ready) 15, recall 5 | 45 + 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview 10 | Same | 45 + 45 |
| E | Scene transfer: Kata-Kata scenario s01 to s08 as listening 10, role-play 15, changed morning 10, culture note 5, recall 5 | Kata-Kata s09 to s18 as listening 10, role-play 15, moved deadline 10, culture note 5, recall 5 | 45 + 45 |
| Extra | — | **Review block** after 11B (Review 1: chapters 10 and 11 with the Stage 1 passive and the markers): recall 5, mixed input 10, alternating role task 15, changed situation 10, self-check 5 | 45 |
| Fast | Chapter 11 fast pack, one 45-minute session for both units | | 45 |

Full course: **11 blocks = 8.25 class hours** for chapter 11 (two units × 5 + the review block), as in the plan. Self-study planning figure: 3 hours per unit. Fast course: 1 block and 9 to 10 hours of self-study.

## What each unit contains

Both units have all 11 components and meet every section 6 and section 14 minimum. The test file checks them.

| | 11A | 11B |
| --- | --- | --- |
| Core / recognition / revision | 20 / 0 / 38 | 21 / 2 («tukar», «deadline») / 34 |
| Patterns (Kata-Kata frames) | f01, f02, f03, f05 (6 Q&A each) | f04, f06, f01, f03 (6 Q&A each) |
| Drills | 8 + 8 + 10 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks | Same counts |
| Model conversation | 14 turns (Kata-Kata s01 to s08 extended), gapped, a 10-turn variant (Rahman and Mei Ling, a letter from the bank) | 12 turns (s09 to s18 extended), gapped, a 10-turn variant (Rahman and Aini, a moved deadline) |
| Listening | 127 Malay words, 9 questions (Rahman and the file) | 128 words, 9 questions (Mei Ling's weekend and the draft) |
| Reading and writing | A team chat message and a door sign, 7 questions; write what you did with a file | A message about a draft and a room-for-rent notice, 7 questions; write a short message about a draft |
| Task | Who did what with the file; change: it was Aini, not Rahman, who sent the reply | Check a draft and confirm the date; change: the deadline moves to Thursday |
| Culture and usage note | 235 words: standard meN- against the everyday root, «menerima» and «melihat» as whole words, «menghantar» also means to take someone, doer first or thing first | 249 words: «tarikh akhir» and «deadline», «menukar» and «tukar», «menyewa» against «meminjam», the short request, charging a phone |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) | Same (20 + 1) |

**meN- verbs, as the Kata-Kata c11 cards show them.** Each verb is its own ledger row and appears with its root, the chapter of the root («Dunia, chapter 4» where the card says so), the nasal change, and the chapter 9 di- partner where the card names one. Roots that are ledger words placed by chapter 11 are shown as «root»; «terima», «lihat», «daki», «lancong», «pinjam», «pesan» and «ajar» are ‹…› mentions, sourced in `curriculum/malay-mentions.json` (four of them are new: ‹lihat›, ‹daki›, ‹pinjam›, ‹pesan›). 11A teaches mem- before b; men- before c, d and j; meng- before h or a vowel; me- before l and m; and the dropped t and p. 11B completes the table: s drops and meny- is used («menyewa», «menyimpan», «menyemak»), k drops and meng- is used («mengira»), and a one-syllable root takes menge- («mengecas»). The complete rule is written once in 11B pattern 3 and once in the fast pack. Spoken bare roots («Puan Aini baca emel itu», «Saya tengok jam», «tukar») are shown after the standard form and labelled spoken.

**Kata-Kata alignment:** the same frames f01 to f06. All six frame examples and all **18** scenario lines appear word for word (11A uses s01 to s08, 11B uses s09 to s18). Card IDs are cited in the openers (11A: ms-c11-001 to -020; 11B: ms-c11-021 to -043), the vocabulary entries (the root notes), the teacher notes (traps ms-c11-003, -013, -014, -015, -017, -021, -022, -027, -030, -032, -038, -041, -042, -043) and the culture sources. The classroom version adds role-plays with a change of plan, pair work in every block, a teacher-read listening, a written message in Block C and the review block.

**Rules applied:** standard forms first. «tukar» and «deadline» are recognition only: labelled spoken wherever they appear, never in a key, a dialogue or the listening (the test file checks this). «nak» appears only as a labelled spoken partner of «mahu». No «lah», «kan», «tak», «dah», «takpe» or «tak apa» appears in either unit. No faith-specific expression and no Indonesian form. A request takes the plain root («Tolong semak draf ini»); the meN- form after «Tolong» appears only as a starred wrong form in a teacher note, and the test file checks this too.

## Core-word coverage

All 41 core words appear in their unit outside the vocabulary list (the test file checks this, and that every revision word is really used). "Practised only" means the word is drilled and used in scenes but is not one of the scored test items; each unit test samples 20 core words. **19 of the 41 words are tested**; the rest are practised.

| Ledger | Word | Unit | Kata-Kata card | Components that use it (outside the vocabulary list) | Unit test | Fast pack |
| --- | --- | --- | --- | ---: | --- | --- |
| L-1124 | membaca | 11A | ms-c11-002 | 17 | tested | yes |
| L-1125 | menulis | 11A | ms-c11-003 | 14 | tested | yes |
| L-1136 | menghantar | 11A | ms-c11-014 | 17 | tested | yes |
| L-1137 | menerima | 11A | ms-c11-015 | 12 | tested | yes |
| L-1129 | membuka | 11A | ms-c11-007 | 13 | tested | yes |
| L-1130 | menutup | 11A | ms-c11-008 | 3 | practised only | — |
| L-1138 | menjawab | 11A | ms-c11-016 | 4 | practised only | yes |
| L-1123 | membeli | 11A | ms-c11-001 | 10 | practised only | yes |
| L-1142 | menjual | 11A | ms-c11-020 | 3 | tested | — |
| L-1132 | membayar | 11A | ms-c11-010 | 4 | practised only | yes |
| L-1131 | membawa | 11A | ms-c11-009 | 5 | practised only | — |
| L-1127 | mengambil | 11A | ms-c11-005 | 1 | practised only | yes |
| L-1133 | mencari | 11A | ms-c11-011 | 8 | tested | yes |
| L-1139 | melihat | 11A | ms-c11-017 | 3 | practised only | — |
| L-1140 | mendengar | 11A | ms-c11-018 | 2 | practised only | — |
| L-1135 | memanggil | 11A | ms-c11-013 | 4 | tested | — |
| L-1141 | menunggu | 11A | ms-c11-019 | 12 | tested | yes |
| L-1126 | memasak | 11A | ms-c11-004 | 4 | practised only | yes |
| L-1134 | mencuci | 11A | ms-c11-012 | 1 | practised only | — |
| L-1128 | membuat | 11A | ms-c11-006 | 4 | practised only | — |
| L-0819 | menyemak | 11B | ms-c11-025 | 17 | tested | yes |
| L-1153 | semak | 11B | ms-c11-038 | 14 | tested | — |
| L-0680 | draf | 11B | ms-c11-034 | 18 | tested | — |
| L-0696 | slaid | 11B | ms-c11-035 | 10 | practised only | — |
| L-0849 | tarikh akhir | 11B | ms-c11-036 | 14 | tested | — |
| L-0684 | rancangan | 11B | ms-c11-037 | 3 | practised only | — |
| L-1154 | mesej | 11B | ms-c11-039 | 8 | practised only | — |
| L-1155 | menelefon | 11B | ms-c11-040 | 10 | tested | yes |
| L-1156 | mengecas | 11B | ms-c11-041 | 11 | tested | yes |
| L-1145 | menukar | 11B | ms-c11-026 | 4 | practised only | — |
| L-1146 | mengira | 11B | ms-c11-027 | 6 | practised only | yes |
| L-1147 | mengisi | 11B | ms-c11-028 | 1 | practised only | — |
| L-1148 | memilih | 11B | ms-c11-029 | 5 | practised only | — |
| L-0865 | mendaki | 11B | ms-c11-023 | 14 | tested | yes |
| L-1144 | melancong | 11B | ms-c11-022 | 11 | tested | — |
| L-1143 | menyewa | 11B | ms-c11-021 | 12 | tested | yes |
| L-1149 | meminjam | 11B | ms-c11-030 | 6 | tested | — |
| L-1150 | memesan | 11B | ms-c11-031 | 8 | practised only | yes |
| L-1151 | menolong | 11B | ms-c11-032 | 2 | practised only | — |
| L-1152 | mengajar | 11B | ms-c11-033 | 4 | practised only | yes |
| L-0792 | menyimpan | 11B | ms-c11-024 | 2 | practised only | — |
| L-0604 | tukar | 11B (recognise only) | ms-c11-042 | vocabulary and labelled notes only | never in a key | named as spoken |
| L-0678 | deadline | 11B (recognise only) | ms-c11-043 | vocabulary and labelled notes only | never in a key | named as spoken |

Thin spots: «mengambil», «mencuci» and «mengisi» each appear outside the vocabulary list in only one component. They pass the check, but a pilot teacher may want one more drill item for each.

## Code and data changed

- `suite/ms_c11a.py`, `suite/ms_c11b.py` (with the review block), and the chapter 11 fast pack in `suite/fast.py` (`STAGE2_PACKS`). Both unit files import `chapter10_common.unit_dict` unchanged; the helper was not copied or edited.
- `suite/__init__.py`: grammar points ms-c11-g02 to g08; the two units are loaded; `BM_NOTE_STAGE2` now records Sam's answer (Japanese and English explainers only), which also changes the Malay-explainer note on the chapter 10 pages; «hiking» and «deadline» are English homographs in prose; GLOSS entries for «kira» and «roti canai» (their ledger meanings contain Malay).
- `course.py`: chapter 11 «meN- verbs» (11A, 11B), genre Work, and its status line. `catalogue.py`: eleven chapters, chapter 11 goal and focus, the additional block `ms-stage2-review-11b`.
- `curriculum/reauthored-units.json`: ms-c11a, ms-c11b and ms-c11-fast added. `curriculum/malay-mentions.json`: 12 entries added (the four new roots above, ‹meN-›, ‹mem-›, ‹men-›, ‹meng-›, ‹meny-›, ‹me-›, ‹menge-›, and ‹menyapu› quoted only as the s → ny example, sourced to the plan (W3) and your brief). Each entry names its source.
- Tests: `tests/test_stage2_ch11.py` is new (13 tests, copied from the chapter 10 file and adapted: ledger partition, core-word use, the meN- rule, Kata-Kata alignment with all 18 scenario lines, spoken partners, minimums, the review block, the fast pack, registration). `test_catalogue.test_structure` now expects 11 chapters, 17 units, 85 blocks and 187 slots, levels A1 × 9 + A2 × 2. No Stage 1 content changed.
- `tools/check_spans.py` was run on both unit files and the fast pack at chapter 11 before building: 0 problems.

## Lines a native speaker should read first

These are my judgement calls, so please read them first. Everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. 11A listening: «Belum. Fail itu tidak boleh dibuka. Saya sedang mencari kata laluan.» (a file that will not open, and the password).
2. 11A model conversation: «Kopi itu dibeli oleh Encik Tanaka. Saya yang membayar kuih.» Is the di- reply natural in an office chat, or would people say «Encik Tanaka yang beli kopi»?
3. 11A pattern 2: «Siapa membaca emel itu?» → «Emel itu dibaca oleh Puan Aini.» The question uses the active verb without «yang»; is it natural?
4. 11A vocabulary and culture: «Saya menghantar anak ke sekolah» as "take my child to school". Is meN- natural here, or only the everyday «hantar»?
5. 11A pattern 4: «Saya sedang memasak nasi dan sup.»
6. 11B pattern 1: «Tolong semak borang ini.» → «Sudah betul. Tolong tanda tangan di sini.»
7. 11B model conversation (my two added turns): «Terima kasih, cik. Saya mahu memesan kopi O.» / «Saya pula mahu memesan teh tarik dan roti canai.» Is «memesan» natural when ordering at a cafe, or is «order» (spoken) the norm?
8. 11B listening: «Kami menyewa kereta di sana.» «Seratus ringgit setiap hari. Kawan saya membayar dulu.» (renting a car on a trip).
9. 11B pattern 2: «Saya mahu menyewa rumah dekat stesen.»; variant: «Saya mahu menyewa basikal dan berbasikal dengan kawan.»
10. 11B culture: «tukar» as what people "usually say" for «menukar», and «deadline» in a chat or at a meeting (both [INFERRED] from the card notes «Spoken: the everyday word»).
11. 11A culture and teacher notes: the claim that the Japanese passive often has an adversative reading while di- is neutral. This is a teaching hypothesis from the plan (section 5), not a checked fact.
12. 11A and 11B vocabulary: the Japanese for «menyewa» (賃借する), «meminjam» ((一時的に)借りる) and «menghantar» (送る・届ける, also taking a person).

All Japanese is a draft for the native review. The bridges (聞く and 見る each covering several Malay verbs; 借りる covering both «menyewa» and «meminjam») are teaching hypotheses.

## Word proposals for Sam (not in the ledger; I rewrote the lines instead and added no rows)

| Proposed form | Why it came up | What the unit says instead |
| --- | --- | --- |
| «kepada» (to, for a person) | «menghantar emel kepada pengurus» | «Saya menghantar fail itu ke Osaka.»; the person is not named as a goal |
| «bukit» (hill) | «mendaki bukit» | «mendaki dengan kawan saya» |
| «menempah» (to book) | Booking a car for the trip | «Kami menyewa kereta di sana.» («tempah» is chapter 4, but «menempah» is not a row) |
| the di- partners «disemak», «disimpan», «dipesan», «dipilih», «dipinjam», «dikira», «diisi» | Passive of the 11B verbs; the ledger has di- rows only for the chapter 9 list | These verbs stay active; 11A's pattern 2 says only verbs with a chapter 9 partner get one |
| «sehari» (a day, per day) | The price of a rented car | «setiap hari» |
| «menyapu» (to sweep) | The s → ny trap you named | Quoted as a ‹menyapu› mention only, in a teacher note; it is not taught |

## Questions for Sam

1. **Review block, not a writing block.** The plan (section 1) puts Review 1 after 11B and gives chapter 11 no writing block; writing blocks come after 10B, 12A, 14 and 16. I built the review block. Do you want a chapter 11 writing block as well? It would make 68 blocks and 51 hours, and the plan totals would change.
2. **«menelefon» in 11A.** The Kata-Kata lines s06 and s07 («Siapa yang akan menelefon …», «Saya akan menelefon mereka …») use «menelefon», which the ledger places in 11B. I kept the scene lines word for word in 11A and told the teacher to gloss it as recognition (teacher notes). Alternatively the ledger could move «menelefon» to 11A. Which?
3. **«menghantar» = take someone to a place.** The plan's audit note says this is a Malaysian sense. I taught it in the culture note and one vocabulary example. Is it right to teach at A2?
4. **A request takes the plain root.** I teach «Tolong semak draf ini» (not «Tolong menyemak») and say the same for «Tolong baca emel ini». Is that what you want taught as the rule?
5. **Spoken «tukar» and «deadline».** I labelled them spoken and kept them out of every key. Is «deadline» as normal in a Malaysian office as the card says?
6. **Scene s06 to s07 and 11A's load.** If the pilot shows 20 core words in 11A is too many, the natural cut is listed in the teacher notes (10 words first).
7. **Page note change.** `BM_NOTE_STAGE2` now says "Japanese or English only (Sam, 13 Nov 2026)". This changes the same note on the chapter 10 pages. Confirm this is what you intended by answer 1.

## Not verified

- **Kamus Dewan:** none of the chapter 11 forms was checked (end of the project, ledger Journal row 128). «mengecas» is your confirmed form (W6). The meN- rules are standard Malay grammar (plan section 3) and were not re-checked against Tatabahasa Dewan.
- **Facts:** the culture notes state no figure, rule or date about Malaysia. The statements about «tukar» and «deadline» come from the Kata-Kata card notes («Spoken: the everyday word»).
- **PDF:** the build's fit check passed for every page. I could not render the pages visually here: the PDF stores subset fonts, and a plain PDF renderer shows the committed chapter 10 pages the same garbled way, so I did not compare layouts by eye.
- **Environment:** the build needed `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk`; I installed them in the session. The checkout was shallow and was unshallowed first, because the exception check reads Git history.
