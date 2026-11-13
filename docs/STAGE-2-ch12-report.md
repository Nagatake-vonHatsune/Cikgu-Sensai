# Stage 2 build step 4, chapter 12: units 12A and 12B (-kan and -i verbs)

**13 November 2026 · Claude.** Authorised by Sam (build step 4, chapter 12 instruction, 13 Nov 2026): the chapter 11 fixes in their own commit, then the chapter 12 suites; push to main when the checks pass; **stop after chapter 12 for Claude's review** before chapter 13. Started at `839ea18`. Kata-Kata (read only) is the pinned copy at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited.

## Summary

- **Chapter 11 fixes (own commit, `76964a3`).** 11A pattern 2 «Siapa yang membaca emel itu?»; the 11A model conversation «Encik Tanaka yang membeli kopi itu.» (I also changed the question before it to «Siapa yang membeli kopi itu?» so the pair matches; the teacher note says to focus with «yang» in speech and keep «di-» … «oleh» for drills and written notices); «dari atas meja»; 11B listening «Seratus ringgit untuk satu hari.» The 11B revision word «setiap» no longer returned, so it left the revision list. Sam's seven answers are in `docs/stage-2-decisions.md` section 8. «tandatangan» is on the new HANDOFF "Stage 2 clean-up pass" list (with «tanda tangan» as a disallowed form for `stage-rules.json`), and the HANDOFF "Word proposals backlog" section is started.
- **Chapter 12.** Two full A2 units (12A and 12B, five 45-minute blocks each), the **writing block after 12A**, the **review block after 12B** and the chapter 12 fast pack, all registered as re-authored in `curriculum/reauthored-units.json` (zero gaps, zero violations). `python3 build.py` passes (450 packs, 2,797 pages, all fit-checked; still **22 violations and 203 gaps, all from older content**, none in chapter 12). All **207** tests pass (193 before, plus 14 in `tests/test_stage2_ch12.py`).
- **One scope decision for you** (question 1): your brief named the writing block after 12A and the fast pack. The plan also gives chapter 12 **Review 2 after 12B**, as it gave chapter 11 Review 1, so I built it; the 67-block, 50.25-hour total needs it.

## Blocks and timings

| Block | Unit 12A: parcels at the guardhouse | Unit 12B: the leak and the repair | Minutes |
| --- | --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns f01 and f02 20, first substitutions 5 | Same timings: patterns f05 and f04 | 45 + 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | Same; the transformation drill starts with standard to everyday | 45 + 45 |
| C | Listening (Mei Ling at the guardhouse) 15, reading (a notice and a chat message) and writing 10, task (collect a parcel) 15, recall 5 | Listening (Mei Ling's call to the office) 15, reading (a complaint form and a sign) and writing 10, task (report a leak and book a slot) 15, recall 5 | 45 + 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview 10 | Same | 45 + 45 |
| E | Scene transfer: Kata-Kata s01 to s10 as listening 10, role-play 15, a parcel in the wrong place 10, culture note 5, recall 5 | Kata-Kata s11 to s19 as listening 10, role-play 15, a changed time 10, culture note 5, recall 5 | 45 + 45 |
| Extra | **Writing block** after 12A: collecting a parcel (recall 5, model 10, draft 15, feedback 10, rewrite 5) | **Review block** after 12B (Review 2: chapters 10 to 12, request and reply): recall 5, mixed input 10, alternating role task 15, changed situation 10, self-check 5 | 45 + 45 |
| Fast | Chapter 12 fast pack, one 45-minute session for both units | | 45 |

Full course: **12 blocks = 9 class hours** for chapter 12 (two units × 5 + the writing block + the review block). Self-study planning figure: 3 hours per unit. Fast course: 1 block and 9 to 10 hours of self-study.

## What each unit contains

Both units have all 11 components and meet every section 6 and section 14 minimum. The test file checks them.

| | 12A | 12B |
| --- | --- | --- |
| Core / recognition / revision | 23 / 1 («nombor tracking») / 33 | 21 / 0 / 31 |
| Patterns (Kata-Kata frames) | f01, f02, f03 (6 Q&A each; three patterns, the plan's minimum) | f05, f04, f06, f01 (6 Q&A each) |
| Drills | 8 + 8 + 8 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks | Same counts |
| Model conversation | 12 turns (Kata-Kata s01 to s10 plus two turns), gapped, a 10-turn variant (Siti collects a parcel) | 11 turns (s11 to s19 plus two turns), gapped, a 10-turn variant (a kitchen pipe) |
| Listening | 123 Malay words, 9 questions (Mei Ling and the guard) | 136 words, 9 questions (Mei Ling's call to the office) |
| Reading and writing | A guardhouse notice and a chat message, 7 questions; write requests to a guard | A complaint form and a sign, 7 questions; write a short message to the office |
| Task | Collect a parcel; change: the owner of unit 8-1 is home, B takes the small parcel and asks for it with «Tolong berikan …» | Report a leak and book a slot; change: the technician now comes at two |
| Culture and usage note | 4 paragraphs: the plain root against ‹-kan›, double k and «berikan», the guardhouse (general knowledge, labelled), a short polite request | 4 paragraphs: ‹-kan› against ‹-i›, «buka lampu» and «tutup lampu», the management office (general knowledge, labelled), the slip of putting ‹-kan› on every verb |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) | Same (20 + 1) |

**-kan and -i, as the Kata-Kata c12 cards show them.** Every vocabulary entry shows the root, the chapter of the root (Dunia or Stage 1), and what the suffix adds: ‹-kan› is to do it for someone or to make it happen («simpankan», «hantarkan», «tunjukkan», «matikan», «bersihkan»); ‹-i› is to or at a person or place («hubungi»). Spelling is taught in 12A pattern 1 and the fast pack: two k in «letakkan» and «tunjukkan», and «berikan» is ‹beri› + ‹-kan›, not ‹ber-› + «ikan» (card ms-c12-010); 12B adds «bersihkan» = ‹bersih› + ‹-kan›, not ‹ber-› + ‹sih›, «baiki» (same spelling as «baik», a different meaning) and «membaiki» / «menghubungi» (‹mem-› before b, ‹meng-› before h). «pengawal», «pemilik», «penerima», «kebocoran», «kerosakan», «aduan» and «tempahan» are whole words. **Requests:** «Tolong simpankan …» and «Boleh tunjukkan …?» are taught first, with the plain root («Tolong simpan …», «Boleh bagi …?») shown beside them as the everyday form and never marked wrong.

**Kata-Kata alignment:** the same frames f01 to f06; all six frame examples and all **19** scenario lines appear word for word (12A uses s01 to s10, 12B uses s11 to s19; «hubungi» in s09 is glossed as recognition in 12A). Card IDs are cited in the openers (12A: ms-c12-001 to -024; 12B: ms-c12-025 to -045), the vocabulary entries (the root notes), the teacher notes (cards -003, -008, -010, -011, -013, -017, -019, -025, -026, -028, -032, -033, -034, -035, -041, -042) and the culture sources.

**Rules applied:** standard forms first. «nombor tracking» is recognition only: labelled spoken wherever it appears, never in a key, a dialogue or the listening (the test checks this). No «lah», «kan» (the particle), «tak», «dah», «takpe», «tak apa» or «nak» in either unit. No faith-specific expression and no Indonesian form (the teacher note names *perbaiki only as the form not to use). No figure, price, rule or time is stated about Malaysia; the two guardhouse and management-office paragraphs are labelled "General knowledge, not a rule and not a checked fact", and the test checks the label and that they contain no digit or "RM".

## Core-word coverage

All 44 core words appear in their unit outside the vocabulary list (the test file checks this, and that every revision word is really used). "Practised only" means the word is drilled and used in scenes but is not one of the scored test items. **24 of the 44 words are tested**; 20 are in the fast pack.

| Unit | Tested | Practised only |
| --- | --- | --- |
| 12A | hantarkan, simpankan, bawakan, letakkan, tunjukkan, pastikan, pengawal, pondok pengawal, unit, blok, label, penerima, nombor penjejakan, koyak | ambilkan, belikan, tutupkan, bukakan, pulangkan, berikan, pejabat pengurusan, pemilik, lobi |
| 12B | kebocoran, siling, paip, aduan, juruteknik, baiki, membaiki, hubungi, gantikan, matikan, perlahankan | kerosakan, kontraktor, slot, menghubungi, ganti, tempahan, isikan, kosongkan, hidupkan, bersihkan |

Thin spots: «ganti» and «pejabat pengurusan» each appear outside the vocabulary list in only one component; «belikan», «pulangkan» and «tempahan» in two. They pass the check, but a pilot teacher may want one more drill item for each.

## Code and data changed

- `suite/ms_c12a.py` (with the writing block), `suite/ms_c12b.py` (with the review block), and the chapter 12 fast pack in `suite/fast.py` (`STAGE2_PACKS`). Both unit files import `chapter10_common.unit_dict` unchanged.
- `suite/__init__.py`: grammar points ms-c12-g02 to g08; the two units are loaded; «slot» is an English homograph in prose; GLOSS entries for L-1179 and L-1180 (their ledger meanings contain «buka» and «tutup»). Speaker labels in the dialogues are English («Guard», «Office»): «pengawal» and «pejabat» are ledger words and an unmarked Malay label stops the build.
- `course.py`: chapter 12 «-kan and -i verbs» (12A, 12B), genre Housing, and its status line. `catalogue.py`: twelve chapters, chapter 12 goal and focus, the additional blocks `ms-stage2-writing-12a` and `ms-stage2-review-12b`.
- `curriculum/reauthored-units.json`: ms-c12a, ms-c12b and ms-c12-fast added. `curriculum/malay-mentions.json`: 19 entries added (the suffixes ‹-kan›, ‹-i›, ‹-an›, ‹pe-›, ‹ke-an›; the roots ‹beri›, ‹tunjuk›, ‹pasti›, ‹kawal›, ‹milik›, ‹jejak›, ‹hubung›, ‹bocor›, ‹hidup›, ‹mati›, ‹adu›; ‹sih› for the wrong split; ‹kepada› quoted only as the word not to add after «hubungi»). Each entry names its source.
- Tests: `tests/test_stage2_ch12.py` is new (14 tests, copied from the chapter 11 file and adapted: ledger partition, core-word use, the -kan / -i rule and its labels, Kata-Kata alignment with all 19 scenario lines, the spoken partner, minimums, writing and review blocks, the fast pack, registration). `test_catalogue.test_structure` now expects 12 chapters, 19 units, 95 blocks and 209 slots, levels A1 × 9 + A2 × 3. No Stage 1 content changed.
- `tools/check_spans.py` was run on both unit files at chapter 12 before building: 0 problems.

## Lines a native speaker should read first

These are my judgement calls, so please read them first. Everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. 12A model conversation, my added turn: «Ya, encik. Saya letakkan bungkusan kecil itu di atas meja dan pastikan pintu pondok pengawal ditutup.»
2. 12A pattern 2: «Boleh berikan nombor telefon puan?» → «Boleh. Saya tulis di kertas ini.» (and the everyday «Boleh bagi nombor telefon puan?»)
3. 12A pattern 3: «Saya tidak ada di rumah. Boleh ambilkan bungkusan saya?» → «Boleh. Saya ambilkan petang ini.» (a guard fetching a parcel for a resident).
4. 12A listening: «Pastikan label itu tidak koyak, ya?» and «Saya bawakan kotak besar itu dan saya letakkan di depan lif.»
5. 12A reply forms: the bare ‹-kan› verb after a pronoun («Saya simpankan …», «Saya hantarkan …», «Saya bawakan …»), as in Kata-Kata s08, with no meN-…-kan form taught.
6. 12A variant: «Penerima ialah Puan Siti, ya? Boleh tunjukkan mesej dari kedai itu?»
7. 12B listening: «Kalau paip itu rosak, juruteknik gantikan paip itu.» and «Tolong perlahankan muzik di unit sebelah. Bising sangat.»
8. 12B dialogue, my added turns: «Boleh saya kosongkan meja dan kerusi di bawah siling itu?» / «Boleh, encik. Tolong kosongkan lantai itu juga.»
9. 12B pattern 1: «Awak sudah hubungi pemilik unit itu?» and «Kami akan menghubungi juruteknik» beside «Kami akan hubungi kontraktor» (both heard after a doer; the course teaches «menghubungi» first).
10. 12B pattern 4: «Tolong hidupkan kipas itu.» → «Baik. Saya hidupkan kipas sekarang.»; «hidupkan» / «matikan» as the standard forms against the everyday «buka lampu» / «tutup lampu».
11. 12B and 12A: «Tolong isikan borang aduan ini.» against «Sila isi borang ini.»; and «Ada kerosakan di paip dapur saya.»
12. The two general-knowledge paragraphs (the guardhouse in 12A, the management office in 12B), especially "a torn label can mean a call to the owner or to the management office" and "who arranges and pays for a repair can depend on the building and on whether you own or rent". Both are labelled as unchecked general knowledge.

All Japanese is a draft for the native review. The bridges (取る against «ambil» / «ambilkan»; 直す covering «membaiki» and correcting a mistake; 連絡する and the に-word) are teaching hypotheses.

## Word proposals for Sam (not in the ledger; I rewrote the lines instead and added no rows)

| Proposed form | Why it came up | What the unit says instead |
| --- | --- | --- |
| «salinan» (copy) | the review block: keep a copy of the form | «simpankan borang itu» |
| «sejak» (since) | when the leak started | «Bila kebocoran itu bermula?» / «Malam tadi.» |
| «melapor» / «melaporkan» (to report) | Hanashishou band 2 uses «melaporkan kebocoran» | «Ada kebocoran di … saya.» |
| the meN-…-kan partners «menyimpankan», «menghantarkan», «membawakan» and the di- partners «dihubungi», «dibaiki» | the plan allows meN-…-kan from chapter 12; the ledger has only «membaiki» and «menghubungi» | the bare ‹-kan› verb after a pronoun, as in Kata-Kata s08 |
| «kepada» (already on the backlog) | «hubungi» and «hantarkan» with a named person | not used; ‹kepada› is only named as the word not to add after «hubungi» |

All of these are on the HANDOFF "Word proposals backlog" list with the earlier ones.

## Questions for Sam

1. **Review block after 12B.** I built Review 2 as the plan gives it (the brief named only the writing block after 12A). Keep it, or drop it? Dropping it would make the plan's totals 66 blocks.
2. **The old placeholder «Ambil bungkusan di lobi».** It is still listed as a "future" Chapter 12 in the course menu beside the new chapter 12 (the plan says to move and re-author it, not relabel it). Retiring it changes the legacy exceptions, which may only shrink. Do you want me to retire it in the next step?
3. **Three patterns in 12A.** Kata-Kata gives 12A the frames f01, f02 and f03 only (f05 «Boleh hubungi juruteknik?» belongs to 12B), so 12A has three patterns, the minimum. Is that enough, or should 12A also show f05 in a fourth pattern?
4. **Bare ‹-kan› after a pronoun** («Saya simpankan …», «Saya matikan …») is the form Kata-Kata uses. Should the course also teach the full meN-…-kan form («menyimpankan») once the ledger has rows for it?
5. **The guardhouse and management-office paragraphs** are general knowledge, labelled, with no figure. Do you want them kept as they are, or shortened to a one-line "ask at your own building"?

## Not verified

- **Kamus Dewan:** none of the chapter 12 forms was checked (end of the project, ledger Journal row 128). The ‹-kan› / ‹-i› rules and spellings come from the Kata-Kata card notes and plan section 3; they were not re-checked against Tatabahasa Dewan.
- **Facts:** the culture notes state no figure, rule or date about Malaysia. The two paragraphs on guardhouses and management offices are general knowledge, labelled as such and not source-checked.
- **PDF:** the build's fit check passed for every page. I did not review the pages by eye (the PDF stores subset fonts).
- **Environment:** the build needed `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (after `apt-get update`); I installed them in the session. The checkout was shallow and was unshallowed first.
