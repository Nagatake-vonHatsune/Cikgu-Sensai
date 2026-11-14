# Stage 2, build step 5: chapter 18, the Stage 2 close

**14 November 2026 · Claude.** Authorised by Sam (the chapter 18 instruction, 14 Nov 2026): a prep commit, then chapter 18 (the review and rehearsal blocks, the A2 test versions A and B, the fast pack and the Stage 2 record); follow `AGENTS.md` for checks, commits and the push to main; **stop at the end for Claude's review.** Started at `4f2391b`. Kata-Kata (read only) at `1987ab9`; Hanashishou (read only) at `55fd4ed`, to confirm the scene names. Kata-Kata, Hanashishou and the ledger sheet were not edited. The live charter was read through the Google Docs connector.

## Summary

| Commit | What |
| --- | --- |
| `7d45aac` (prep) | c17 and both ledger copies from Kata-Kata `1987ab9` (step 3f): card ms-c17-026 gone, L-1303 «minggu depan» Retired; `curriculum/phrases-taught-earlier.json` and its checker condition removed; **Stage 2 core 270** (17 = 25); the chapter 10 to 13 fast packs widened to all core words (44, 45, 48, 29); seven `GLOSS` entries for ledger meanings that contain Malay |
| `73b9d98` | Chapter 18: unit 18 (teaching plan, 18A, 18B, 18E), the A2 stage test A and B (with scripts and the administration sheet), the chapter 18 fast pack, the catalogue's chapter 18 record and the Stage 2 record; `tests/test_stage2_ch18.py` |
| the commit after `73b9d98` | One written-text fix (version B: «kami menyimpan», not «kami simpan»), this report, `HANDOFF.md`, the plan note |

Checks: `python3 -m unittest discover -s tests` passes (**332** tests: 310 before, 22 new) and `python3 build.py` passes (**557 packs, 3,456 pages**, all fit-checked; 542 and 3,346 before). The language checks are unchanged: 20 legacy violations (the frozen baseline) and 188 ledger gaps, none in a re-authored unit; unit 18, the fast pack and the A2 test have zero gaps and zero violations.

**Journal row 200 can be closed.** Both halves of L-1303's action are done (Kata-Kata dropped card ms-c17-026 in step 3f; this session removed `curriculum/phrases-taught-earlier.json`). The sheet is not mine to edit; `tests/test_step5h_stage1.py` allows the stale L-1303 action cell until a ledger session clears it.

## Prep

- `curriculum/reference/katakata/c17.json` and both ledger copies from Kata-Kata `1987ab9`. The ledger diff is exactly two rows (L-1303 Retired; L-0530 Action «KD4 check»); `docs/handoff/ledger-snapshot.csv` is the Kata-Kata file byte for byte, the reference copy the same file with LF. Hashes in `docs/step4-sources.json`; the catalogue link and the pinned-commit tests moved to `1987ab9`.
- With L-1303 Retired its place is empty, so «minggu depan» is again «minggu» + «depan» (chapter 4) and needs no exception: the file and the checker's `earlier_phrases` condition are gone, and a test checks the phrase at chapters 4, 10, 17 and 18. Unit 17 keeps «Saya belanja minggu depan.» as revision; its core list, card range (ms-c17-001 to 025) and fast pack lost L-1303.
- **Stage 2 core is 270** (10 = 44, 11 = 45, 12 = 48, 13 = 29, 14 = 29, 15 = 23, 16 = 27, 17 = 25). Updated in the tests, `docs/stage-2-plan.md` and `docs/stage-2-decisions.md` (new section 16).
- Fast packs 10 to 13 now hold all core words, as 14 to 17 do; their "the full course also teaches" lines became "recognise only" lines for «pindah», «tukar» / «deadline» and «nombor tracking». The page count did not change (the packs still fit).

## Chapter 18: blocks and timings

| Block | Component | Minutes | Content |
| --- | --- | ---: | --- |
| 18A | `ms-c18-review` | 45 | recall 5 (one prompt per chapter 10 to 17); the Kata-Kata c18 working week 10 (all 22 lines, six scenes, plus the six c18 frames, word for word); pattern round 15 (every chapter 10 to 17 frame, five theme stations); notice board 10 (six questions); self-check 5 (what to repair in 18B) |
| 18B | `ms-c18-rehearsal` | 45 | recall 5; a new colleague's day 10; the parcel problem 10; the changed invitation 10 (standard to a senior colleague, then spoken to a friend); targeted repair 10 (ten choose-the-better items, one per standing rule) |
| 18C | `ms-stage2-test-{a,b}-{listening,reading,writing}` | 12 + 15 + 18 | the A2 written check |
| 18D | `ms-stage2-test-{a,b}-speaking` | 45 | about 7 minutes a learner, one examiner, six learners |
| 18E | `ms-c18-feedback` | 45 | results and feedback 10; the Stage 2 can-do review 15 (two lines per chapter, EN and JA); Hanashishou band 1 demonstration 10; personal practice plan 10 |

Plus `ms-c18-teaching-plan` (the five blocks, the spaced-return table, the fast-course note, the hours check) and the chapter 18 fast pack `ms-c18-fast-pack` (20 review words, two or more from each of chapters 10 to 17; the six c18 frames as five patterns with two examples; a 12-turn conversation of c18 lines s01 to s08 and s17 to s20, word for word; a task with a change of plan; five self-check items; "This pack is not the test" and the pointer to 18C and 18D).

**Spaced returns (plan section 6).** All 48 Kata-Kata frames of chapters 10 to 17 return in the 18A pattern round (`FRAME_RETURNS`, each line new, set in the week). Chapters 16 and 17 return a second time in 18B with different lines (`LATE_RETURNS`, all 12 frames). Their third return falls after chapter 18: the catalogue's pattern returns for chapters 16 and 17 now list «ms-stage3 (carried forward)», and the Stage 2 record has `stage3_carry_forward: ['ms-c16', 'ms-c17']`.

**Hanashishou (named only).** 18E names twelve band 1 scenes by pack: Daily life `grab_ride_chat`, `lost_wallet`; Home and condo `new_neighbour`, `guardhouse_parcel`, `ceiling_leak`, `aircon_repair`; Office `report_deadline`, `team_dinner`; Health `clinic_registration`, `clinic_visit`, `pharmacy_advice`; Social `weekend_plans`. I checked at Hanashishou `55fd4ed` that each file exists and has band 1 («#lvl: 1») choices, and that the plan's blob SHAs still match. No scene is assigned to a chapter (build step 6).

**Hours check.** 55 teaching-unit blocks (11 units × 5) + 3 reviews (after 11B, 12B, 15) + 4 writing blocks (after 10B, 12A, 14, 16) + 5 chapter 18 blocks = **67 blocks = 50.25 hours**. The test counts the blocks from the built catalogue (55 in the chapter 10 to 17 block plans, 7 built Stage 2 additional blocks, 5 in the chapter 18 block plan), not from the constant.

## The A2 stage test

Same format as the A1 test: versions A and B, four sections of 20 marks; listening 10 items of 2 marks, reading 10 items of 2 marks, writing a form (10) and a message (10), speaking a self-introduction with an invitation (8) and two role-play cards (6 each). Listening scripts sheet, administration sheet (timing, materials, procedure, scoring and the pass rule, item maps, result sheet) and complete keys with rubrics and examiner lines.

**Item map summary** (both versions, from `stage2.item_map`; every item also names the Kata-Kata patterns it tests, all of which exist):

| Chapter | Items (version A; B is the same by code) | Count |
| --- | --- | ---: |
| 10 | L3, L4, W2, S1 | 4 |
| 11 | L5, L6, R10, S1 | 4 |
| 12 | L1, L7, L8, R3, R4, S2.1, S2.2 | 7 |
| 13 | L2, R1, R2 | 3 |
| 14 | L1, L9, R3, R4, R8, W2, S1, S2.2 | 8 |
| 15 | R5, R6, W1 | 3 |
| 16 | L8, R9, R10, S2.3, S2.4 | 5 |
| 17 | L9, L10, R7, R8, W2, S1 | 6 |

Every chapter 10 to 17 is assessed in both versions by at least three items, and every chapter's patterns are tested. **No item tests a word outside chapters 1 to 17:** every tagged word is a ledger headword placed at or before chapter 17, none is a practice-pool row (L-1304 to L-1309) or a recognition row («pindah», «tukar», «deadline», «nombor tracking»), and every Malay span of chapter 18 passes the checker at chapter 17 (the one exception below). The versions are parallel: same codes, sections and marks, the same chapters per item, at least one shared pattern per item, and no shared fact line or reading text (A: Tanaka's condo, Farah, a handbag, an office dinner; B: Kimura, Hafiz, an umbrella, a team lunch).

**Compulsory cards (Sam's decision A2).** One request card (chapter 12: card 1 parcel or card 2 leak) and one mishap card (chapter 16: card 3 locked out or left behind, card 4 a spill or a broken cup) are always used; each function has two parallel cards so the examiner can change cards between learners, as in Stage 1. Chapter 17 enters speaking through the invitation in Part 1.

**Pass rule: 48 of 80, at least 10 of 20 in each section.** The live charter gives **no A2 pass rule** (section 5 says only "Pass the A2 exit tasks"). The rule is **Sam's decision A1 in `docs/stage-2-decisions.md` (13 Nov 2026)**, which carries the Stage 1 rule over; it is labelled so on the administration sheet and in the Stage 2 record (`status`), and called "not a validated CEFR cut score". Completion label "Malay A2 · Stage 2 complete" (A4); extra speaking blocks for more than six learners sit outside the 67 (A3).

**Assessment rules in the keys.** Standard production is always accepted; spoken forms are accepted where clear and never required; ‹lah› and ‹kan› are never required (a test checks every key with the build's R4 rule and a word search); the writing keys accept and list «kalau» / «jika», «kerana» / «sebab», «kemudian» / «selepas itu», «tangguhkan» / «menangguhkan» (third person).

## Standing rules

All kept, and `test_standing_rules` checks the ones a pattern can catch in every chapter 18 span: «dari» for places and times, «daripada» for people and senders; no aspect word before a bare ‹-kan› / ‹-i› verb; no meN-…-kan form except «menangguhkan» / «membatalkan»; the bare root only in dialogue (written texts and keys use the meN- form; the fix in the last commit); «tangguhkan» with a noun object («rancangan …»); inclusive «kita» in the group messages (B's «makan tengah hari dengan kami» is the exclusive «kami», correctly); «Lain kali, ya?» never after a new day is offered; «sudi» for invitations, «boleh» for requests; no «keputusan» in a casual turn; no faith-specific expression; the clinic lines give no diagnosis, medicine or treatment advice (the only advice is «Encik patut tanya doktor dulu.» and Kata-Kata's «Cik patut berehat.»). Spoken forms are labelled where they appear (the Kata-Kata lines «tengok», «Set!», «kat»; the «Jom … kat … tu/ni» lines).

**One practice-pool word, on purpose:** the 18A notice board has «Semua bungkusan disimpan di pondok pengawal.» with the note "«disimpan» is a Kata-Kata practice word: recognise it from «simpan»; it is not tested". It is the only practice-pool use in chapter 18 and appears in no key (a test checks both).

**Deliberately wrong lines:** the 18B targeted repair shows one wrong line beside one right line in each of ten items («Mesej dari kedai itu …», «Pengawal sudah simpankan …», «Saya mencari merah yang beg.» and so on), so learners can name the rule. The wrong lines use only taught words and are excluded from the standing-rules test; the key gives the answer and the rule for each.

## Native-read lines (12)

My judgement calls; the checks cannot judge naturalness.

1. «Esok air dipotong dari pukul sepuluh pagi hingga pukul dua petang, kerana juruteknik akan membaiki paip di Blok B.» (test A, listening)
2. «Kalau ini kali pertama anda di sini, anda perlu mendaftar di kaunter dulu.» (test A, listening; «anda» in an announcement)
3. «Tidak mengapa. Nama encik ada pada label kotak ini.» («pada» against «di» for a label)
4. «Satu kotak basah, jadi kami menyimpan kotak itu di pejabat.» (test B, guardhouse message)
5. «Sila hati-hati di dapur.» (test B, office note)
6. «Saya baru berpindah ke unit 9-2.» (test B, listening)
7. «Encik Kimura, sudikah encik makan tengah hari dengan kami hari Khamis?»
8. «Kotak saya yang terbesar, tetapi telefon saya tertinggal di pejabat.» (18B, the chapter 16 f05 frame in a parcel setting)
9. «Air dari siling tertumpah di atas kotak itu.» (18B; is «tertumpah» natural for water from a ceiling, or «menitis»?)
10. «Bos menukar hari: hari Ahad, pukul tujuh.» (18B change of plan)
11. «Saya bersihkan meja ini sekarang.» (first-person offer, test A card 4 key)
12. «Kalau lif rosak, kita guna tangga.» (18A, chapter 14 f01)

## Pages looked at

Rendered with PyMuPDF `get_pixmap` at 100 dpi from the built `dist/bank.js` (before the last one-word fix, which changes no layout) and looked at by eye: **page 3366** (18A, the Friday scene of the working week, the six c18 frames and station 1 of the pattern round); **page 3377** (18B, targeted repair items 2 to 10); **page 3396** (test A reading: instructions, part 1 clinic notice, part 2 message); **page 3445** (listening scripts, version B tasks 3 to 5); **page 3410** (test A speaking: cards 2 to 4 with the compulsory-pair labels); **page 3452** (administration sheet, item map of version A with chapters and patterns, and the chapter lines). All render as written: blue Malay, Japanese, the «» marks removed, no overflow. Two fixes came from the look: 18B item 9 read "accident?:", and card 4 was tagged chapter 11 as well as 16 (now 16 only, both versions).

## Not verified

- Kamus Dewan: no line was checked (end of the project). The Japanese is a draft, as everywhere.
- The naturalness of the new lines (the twelve above are the ones I am least sure of).
- Hanashishou: I confirmed the scene files and their band 1 choices exist, not that every band 1 line uses only chapter 1 to 17 words (that is build step 6; the 18E key warns about «tertinggal» and «perlu» from the plan's audit).
- The fit check passed for every page; I looked at the six pages above, not all 110 new ones.

## Questions for Sam

1. **The A2 pass rule.** The charter has none; I used your decision A1 (48/80, 10/20 per section). Do you want it written into the charter (section 5, chapter 18 row), as the Stage 1 rule is in the charter's Stage 1 table?
2. **Compulsory cards.** I read A2 as "one request card and one mishap card, always", with two parallel cards for each so cards can change between learners. If you meant exactly two fixed cards, cards 2 and 4 become spare cards for a re-sit.
3. **Wrong lines in the 18B repair.** Ten pupil-facing wrong lines, each beside the right one. Keep, or show only the right lines with a rule to name?
4. **Practice-pool recognition.** One use (18A notice, «disimpan»). Keep it, or remove the practice words from Cikgu Sensai entirely?
5. **The native-read lines** above, especially 9 («tertumpah» for water from a ceiling) and 3 («pada label»).
6. **Words I avoided** (not proposed, the lines were rewritten): «pesakit» (patient), «restoran», «laporan», «penghuni», «pasukan», «tepi», «kain», «lap». «pesakit» would make clinic notices more natural at Stage 3; say if you want it on the backlog.
