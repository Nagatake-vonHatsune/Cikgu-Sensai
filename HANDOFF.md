# Handoff

Update this file at the end of every session. The next builder (ChatGPT or Claude) starts here, after the charter and `AGENTS.md`.

## Stage 2 clean-up pass (open list)

Do these together, after the Kata-Kata sync that brings in the ledger change, in one commit.

1. **«tandatangan»** (Sam, 13 Nov 2026; ledger row L-0530 is now «tandatangan», joined, the Malaysian spelling; «tanda tangan» is Indonesian). Switch every «tanda tangan» in the units to «tandatangan»: 11B pattern 1 «Tolong tanda tangan di sini.» (`suite/ms_c11b.py`) and the Stage 1 example `suite/ms_c02b.py` («Ini tanda tangan saya.»). Check the ledger copy and the Kata-Kata reference copy have the new row first.
2. **Disallowed form:** add «tanda tangan» to the disallowed forms in `curriculum/stage-rules.json` (and the fixtures file), allowed only in a ‹…› "do not use" mention. Kata-Kata must copy the same rules file.

## Word proposals backlog (not in the ledger; Sam approves in one batch after chapter 17)

Collected from every chapter. Builders rewrote the lines instead and added no rows. Sam will approve (or drop) them together after chapter 17; then a ledger session adds the approved rows.

| Proposed form | Chapter | Why it came up |
| --- | --- | --- |
| «kepada» (to, for a person) | 11 (Claude recommends) | «menghantar emel kepada pengurus»; the unit says «Saya menghantar fail itu ke Osaka.» |
| «sehari» (a day, per day) | 11 (Claude recommends) | the price of a rented car; the unit says «untuk satu hari» |
| «bukit» (hill) | 11 | «mendaki bukit»; the unit says «mendaki dengan kawan saya» |
| «menempah» (to book) | 11 | booking a car for the trip («tempah» is chapter 4, «menempah» is not a row) |
| the di- partners «disemak», «disimpan», «dipesan», «dipilih», «dipinjam», «dikira», «diisi» | 11 | passive of the 11B verbs; the ledger has di- rows only for the chapter 9 list |
| «menyapu» (to sweep) | 11 | the s → ny trap; quoted only as a ‹menyapu› mention |
| «kolam renang», «taman», «seminggu», «penuh», «bersukan», «hidup» | 10 | recorded in `docs/STAGE-2-ch10-report.md` (word proposals) |
| «salinan» (copy) | 12 | **recommended** (Sam, 13 Nov): review block: «simpankan salinan di pejabat» (rewritten to «simpankan borang itu») |
| «sejak» (since) | 12 | **now a chapter 14 core word (L-1212), taught there; the chapter 12 rewrite stays.** Sam, 13 Nov: recommended, especially: «Sejak semalam» for when a leak started (rewritten to «Bila kebocoran itu bermula?» / «Malam tadi.») |
| «melapor» / «melaporkan» (to report) | 12 | **recommended** (Sam, 13 Nov): Hanashishou band 2 uses «melaporkan kebocoran»; the unit says «Ada kebocoran di … saya.» |
| the di- partners «dihubungi», «dibaiki» | 12 | the ledger has only «membaiki» and «menghubungi». **The meN-…-kan forms «menyimpankan», «menghantarkan», «membawakan» are dropped: Sam (13 Nov) says they are not natural and are not taught.** |
| «sihat» (healthy) | 13 (**recommended**, Sam 13 Nov) | the root of the ledger word «kesihatan»; «Saya sihat.» / «Saya tidak sihat.» (the unit says «Saya demam dan sakit tekak.») |
| «ahli farmasi» (pharmacist) | 13 | the Kata-Kata speaker label for s16 and s18; the unit uses the English label «Pharmacist» |
| «beritahu» (to tell) | 13 (**recommended**, Sam 13 Nov) | "tell the doctor"; the unit says «Saya cakap dengan doktor nanti.» |
| «tinggalkan» (to leave behind) | 13 | leaving a bag at the counter; the unit says «Boleh saya letak beg di sini?» |
| «baiklah» and «begini» | 14 (Sam's natural casual phrase) | «Baiklah, kita buat begini» for stating a plan; no line needs them, the unit says «Baik. Ini rancangan kita.» (Kata-Kata s08) |
| «ikut» (to come along) | 14 | inviting a friend: «Puan Aini mahu ikut?»; the unit says «mahu datang?» |
| «kata» (to say) | 14 | "what does the message say?"; the unit says «Apa dalam mesej itu?» |
| «pengumuman» (announcement) | 14 | the heading of a written notice; the unit starts «Ada perubahan rancangan.» |
| «menangguhkan» and «membatalkan» (meN- forms of «tangguhkan» and «batalkan») | 14 (**recommended**, Claude's review) | a third person in standard speech and writing («Mei Ling menangguhkan rancangan itu.»); the unit uses the bare form with a noun object for now |
| «kakitangan» (staff) | 15 (**approved by Sam**, 13 Nov) | the Kata-Kata speaker label for the counter clerk (s02 to s10); the unit uses the English label «Staff» |
| «bola» (ball) | 15 (**approved by Sam**, 13 Nov) | the natural comparison for a round thing («bulat, seperti bola»); the unit says «bulat, seperti jam» |
| «tidak apa-apa» (never mind, it's nothing) | 16 (**recommended**, Sam 13 Nov) | the everyday answer to «Maaf»; the unit uses «Jangan risau.» (Kata-Kata s07) |
| «berlaku» (to happen) | 16 | "what happened" in a report or a clinic form; the form says «Sebab: tergelincir di tangga.» |
| «masalah» (problem) | 16 (**recommended**, Sam 13 Nov) | «Ada masalah?» asked of a late colleague; the unit says «Kenapa?» |
| «pinjam» (to borrow) | 16 | «Pemandu teksi pinjamkan telefon …»; the unit says «Pemandu teksi menelefon pejabat untuk saya» |

## Latest session: Stage 2 build step 4, chapter 15 fix and chapter 16 (13 Nov 2026, Claude)

- **Authorised:** Sam (build step 4, chapter 16 instruction, 13 Nov 2026): one chapter 15 fix and Sam's chapter 15 answers in their own commit, then the chapter 16 suite; push to main when the checks pass; **stop after chapter 16 for Claude's review** before chapter 17. Started at `e83eaca`. Report: `docs/STAGE-2-ch16-report.md`.
- **Fix (`7389195`):** the review block line is now «Walaupun saya sibuk, saya akan menunggu doktor di sini.»; Sam's six chapter 15 answers are in `docs/stage-2-decisions.md` section 12 (join of s11 and s12, f01 and f03 merged, fast packs hold all core words from now on, «ciri» common and «ciri-ciri» a mention only, review setting and menu names fine, «kakitangan» and «bola» **approved by Sam** on the backlog). 258 tests passed on that commit.
- **Chapter 16 (`f73c68b`):** unit 16 (the locked door, the spilt coffee and the slip at the clinic: 23 core words, no recognition word), the **writing block after chapter 16** (a brief factual incident message; the plan gives chapter 16 no review block) and the chapter 16 fast pack (all 23 core words): 6 blocks = 4.5 h, plus 1 fast block. All in `curriculum/reauthored-units.json` with zero gaps and zero violations. Build: 523 packs, 3,219 pages, still 20 violations and 199 gaps (none in chapter 16). **277 tests** pass (19 new in `tests/test_stage2_ch16.py`).
- **Waiting for:** Claude's review of chapter 16; Sam's answers to the questions at the end of the report and the 12 native-read lines.
- **Next:** after the review, chapter 17 (standard and spoken choices, particles, invitations and refusals; «lah» joined from 17; Kata-Kata c17 is already in the snapshot). Chapter 17 has no writing or review block in the plan; chapter 18 is the integrated review. Use the template note below.
- **Environment note:** `build.py` needs `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (apt; run `apt-get update` first), and a full Git checkout (`git fetch --unshallow`).

### What chapter 16 added to the template below

- A **single-unit chapter with a writing block** is the chapter 14 pattern: `label='16'`, `unit_id='ms-c16'`, menu entry `("…", "Accidents", [("16", [])])`, `extra=EXTRA` with `kind='writing'` (block id `ms-c16-writing-block`; register `writing-16` in `catalogue.py` `extra_blocks` and `stage2_blocks`; the additional block is `ms-stage2-writing-16`). Chapter 16 has no review block.
- **All the core words, not only the ones the brief names.** The brief listed eleven ter- words; the ledger places 23 core words at chapter 16 (also «terjatuh», «tertidur», «terbakar», «tidak sengaja», «kemalangan», «kunci», «tumpah», «luka», «lebam», «bengkak», «licin», «pecah»). Recompute the core list from the ledger, as the template says; the test fails if a core word is not used.
- **ter- roots:** a root that is a ledger word placed at or before 16 is «root» with its chapter in the vocabulary entry («tinggal», chapter 2; «lupa», «tidur», «lepas», chapter 4; «tumpah», «kunci», this chapter); the others (‹jatuh›, ‹silap›, ‹langgar›, ‹gelincir›, ‹cedera›, ‹bakar›, ‹putus›, ‹sangkut›, ‹malang›) are ‹…› mentions with a Kata-Kata card as source. `‹ter-›` is also a mention: **write the prefix as ‹ter-›, never «ter-»** (the span check reads «ter-» as a ledger gap), in English and Japanese text and in `fast.py`.
- **A phrase in «…» must be a ledger phrase:** «mana» alone is a gap («di mana», «yang mana», «dari mana» pass); the spoken ‹tak sengaja› is a mention, not a «…» span.
- **Speaker labels:** «Pengawal» and «Penyambut tetamu» are ledger words, so the labels are the English «Guard» and «Receptionist» (the chapter 15 rule).
- **Clinic safety:** Kata-Kata describes the injury only as «bengkak», «luka kecil», «lebam»; the unit adds no diagnosis, no treatment advice and no medicine, the receptionist only registers and asks to wait, and `test_clinic_safety` checks the Malay spans for banned words and the receptionist's three lines.
- **A scene change inside one turn:** turn 11 joins s11 and s12 (both Tanaka); here s12 starts the clinic scene, so the join crosses a scene change. A teacher note says so (a question for Sam in the report).

## Previous session: Stage 2 build step 4, chapter 14 fixes and chapter 15 (13 Nov 2026, Claude)

- **Authorised:** Sam (build step 4, chapter 15 instruction, 13 Nov 2026): the chapter 14 fixes in their own commit, then the chapter 15 suite; push to main when the checks pass; **stop after chapter 15 for Claude's review** before chapter 16. Started at `ea61fef`. Report: `docs/STAGE-2-ch15-report.md`.
- **Fixes (`40b3c59`):** «tangguhkan» and «batalkan» take a noun object («tangguhkan rancangan mendaki», «batalkan rancangan mendaki», «Rancangan mendaki batal …»; written notices give it, short spoken replies may drop it); inclusive «kita» in the group-chat messages, notices and writing models (a teacher note on «kami» against «kita»); `docs/stage-2-decisions.md` section 11 now says "Sam's answers, given directly in the chapter 14 session" and records the two fixes as Claude's later review; «menangguhkan» and «membatalkan» on the backlog (recommended). 240 tests passed on that commit.
- **Chapter 15 (the commit after `40b3c59`):** unit 15 (the lost wallet at the station counter and the Japanese visitors: 21 core words, no recognition word), the **review block after chapter 15** (the plan's Review 3: chapters 13 to 15 plus earlier verb contrasts) and the chapter 15 fast pack (all 21 core words): 6 blocks = 4.5 h, plus 1 fast block. All in `curriculum/reauthored-units.json` with zero gaps and zero violations. Build: 503 packs, 3,100 pages, still 20 violations and 199 gaps (none in chapter 15). **258 tests** pass (18 new in `tests/test_stage2_ch15.py`, 1 new in the chapter 14 file).
- **Waiting for:** Claude's review of chapter 15; Sam's answers to the six questions at the end of the report (the turn that joins s11 and s12, the five-pattern grouping, the fast pack with all 21 words, «ciri-ciri» as a mention, the review setting, menu names) and the 12 native-read lines.
- **Next:** after the review, chapter 16 (accidental ter-, apology and complaint; Kata-Kata c16 is already in the snapshot) **with the writing block after chapter 16**, using the template note below. Chapter 16 teaches ‹tertinggal›; chapter 15 only names it.
- **Environment note:** `build.py` needs `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (apt; run `apt-get update` first), and a full Git checkout.

### What chapter 15 added to the template below

- A **single-unit chapter with a review block** uses `label='15'`, `unit_id='ms-c15'`, the menu entry `("…", "Lost property", [("15", [])])` and `extra=EXTRA` with `kind='review'` (block id `ms-c15-review-block`; register `review-15` in `catalogue.py` `extra_blocks` and `stage2_blocks`; the additional block is `ms-stage2-review-15`). Its key says "review block after unit 15" (the label), not "after chapter 15".
- **Seventeen scenario lines, 16 turns:** join two consecutive lines of one speaker into one turn (turn 11 = s11 + s12) and test that the turn equals the two Kata-Kata lines joined by a space. A speaker label that is a ledger word or a new Malay word (Kata-Kata's «Kakitangan stesen») becomes an English label («Staff»).
- **A word that is also English** («zip») goes in `ENGLISH_HOMOGRAPHS`. A ledger meaning with Malay in it («seperti», «memakai», «berwarna») needs a `GLOSS` entry for the fast-pack word list.
- **A quoted but not taught form** is a ‹…› mention with a source: ‹tertinggal› (chapter 16), ‹macam tu› (chapter 17), ‹ciri-ciri›, ‹jalur›, ‹-nya›, ‹ber-›, ‹me-›. A reduplicated form or a chapter-gated form inside «…» fails the span check (`tools/check_spans.py 15 suite/ms_c15.py`).
- In a review block, `-nya` on a placed root («bentuknya») is allowed; the test strips «nya» before looking the word up.
- **Noun objects (Sam, 13 Nov 2026):** «tangguhkan» and «batalkan» take a noun («rancangan»), never a verb; chapter 15 does not use them, chapter 16 and later may.

## Previous session: Stage 2 build step 4, chapter 13 fixes and chapter 14 (13 Nov 2026, Claude)

- **Authorised:** Sam (build step 4, chapter 14 instruction, 13 Nov 2026): the chapter 12 and 13 fixes in their own commit, then the chapter 14 suite; push to main when the checks pass; **stop after chapter 14 for Claude's review** before chapter 15. Started at `1fd7862`. Report: `docs/STAGE-2-ch14-report.md`.
- **Fixes (`11db7f0`):** «dari» for places and times, «daripada» for people and organisations (13 «cuti sakit … daripada doktor» in five places, 12A «mesej daripada kedai itu», and 11A «surat daripada bank itu», the one extra hit); 13 «Sila jangan bising.» and «Tolong jangan bising di bilik menunggu.» (the core word «elakkan» now has «Tolong elakkan lif itu. Lif itu rosak.»); «terima kasih atas mesej itu»; no visiting hours (health-form and photo rules kept); the bare-root rule and the «dari» / «daripada» rule in the template; Sam's chapter 13 answers in `docs/stage-2-decisions.md` section 10; «sihat» and «beritahu» "recommended".
- **Chapter 14 (the commit after `11db7f0`):** unit 14 (the weekend hike, the rain plan and the change to Sunday: 22 core words, no recognition word), the **writing block after unit 14** (explain and rearrange a plan) and the chapter 14 fast pack: 6 blocks = 4.5 h, plus 1 fast block. All in `curriculum/reauthored-units.json` with zero gaps and zero violations. Build: 483 packs, 2,981 pages, still 20 violations and 199 gaps (none in chapter 14). **239 tests** pass (16 new in `tests/test_stage2_ch14.py`).
- **Sam's answers (13 Nov, `docs/stage-2-decisions.md` section 11):** all six accepted. Third-person «Mei Ling tangguhkan …» / «batalkan» is allowed until a later chapter teaches the meN- forms (‹menangguhkan›, ‹membatalkan›; **a later chapter must introduce them**); the fast pack has all 22 core words.
- **Waiting for:** Claude's review of chapter 14 and the 12 native-read lines.
- **Next:** after the review, chapter 15 (lost property: «yang» descriptions and the cumulative question words; Kata-Kata c15 is already in the snapshot) **with the review block after chapter 15** (the plan's Review 3), using the template note below.
- **Environment note:** `build.py` needs `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (apt; run `apt-get update` first), and a full Git checkout.

### What chapter 14 added to the template below

- A **single-unit chapter with a writing block** uses `label='14'`, `unit_id='ms-c14'`, the menu entry `("…", "Plans", [("14", [])])` and `extra=EXTRA` (the same `EXTRA` dict as chapter 12A; the block id is `ms-c14-writing-block`). Register the block in `catalogue.py` (`extra_blocks['writing-14']` and `stage2_blocks`).
- **Six frames, five patterns:** f02 and f03 share pattern 2 (the pattern ID string is `ms-c14-f02 and f03`; `pattern_ids` lists all six). The 15 scenario lines all fit the 16-turn model conversation, so the whole scene is the model; the variant is a second change of facts.
- **Written against everyday words:** a connector pair is shown in the vocabulary entry of the formal word («jika» beside «kalau»), in the transformation drill (written to everyday) and in a test; the casual lines use the everyday words and the reading and the notice use the written ones. A spoken partner (‹lepas tu›) is a ‹…› mention with a source; «tapi» appears only with the label "spoken".
- **-kan words that have no meN- form** («tangguhkan», «batalkan») stay in «kita» sentences and requests; a third-person doer or an aspect word is rephrased («Mendaki batal.»). `tests/test_stage2_ch14.py::test_kan_rule_and_dari` holds the regex and the «dari» / «daripada» check.
- A **dialogue line may keep Kata-Kata's everyday bare root** («Saya sudah tulis mesej …»); the models, keys, readings and the markers drill use the meN- form («menulis»).
- Speaker labels are «Tanaka», «Mei Ling», «Aini» (no «Cik»/«Puan» in a label); English prose marks «Cik» and «Puan» with «…».

## Previous session: Stage 2 build step 4, chapter 12 fixes and chapter 13 (13 Nov 2026, Claude)

- **Authorised:** Sam (build step 4, chapter 13 instruction, 13 Nov 2026): the chapter 12 fixes in their own commit, then unit 13; push to main when the checks pass; **stop after chapter 13 for Claude's review** before chapter 14. Started at `b54fde6`. Report: `docs/STAGE-2-ch13-report.md`.
- **Chapter 12 fixes (`732e336`):** the ‹-kan› rule (bare ‹-kan› for requests and first-person offers or replies; the meN- verb the ledger has after a third-person doer or an aspect word; rephrase where there is no meN- verb; no meN-…-kan forms; the same for the ‹-i› verbs), «… akan menukar paip itu», 12B «Tolong kosongkan lantai itu juga.» deleted, «Penerima Puan Siti, ya?» (no «ialah» in conversation), «Ada berapa kotak di lobi?», the guardhouse and management-office notes in two lines, the old «Ambil bungkusan di lobi» placeholder retired from the course menu with its six legacy lessons and ten legacy exceptions (30 to 20), Sam's answers in `docs/stage-2-decisions.md` section 9, and «sejak», «melaporkan» and «salinan» marked "recommended" in the backlog.
- **Chapter 13 (the commit after `732e336`):** unit 13 (the panel clinic and the pharmacy: 25 core words, no recognition word) and the chapter 13 fast pack: 5 blocks = 3.75 h, plus 1 fast block. The plan gives chapter 13 no writing or review block, so none was built. Both are in `curriculum/reauthored-units.json` with zero gaps and zero violations. Build: 463 packs, 2,862 pages, 20 violations and 199 gaps (none in chapter 13). **223 tests** pass (15 new in `tests/test_stage2_ch13.py`, 1 new in the chapter 12 file).
- **Waiting for:** Claude's review of chapter 13; Sam's answers to the four questions at the end of the report (the five-pattern grouping, «mendaftar» first, «MC» as recognition, the fictional notices) and the 12 native-read lines.
- **Next:** after the review, chapter 14 (reasons, conditions, purpose, contrast and sequence; Kata-Kata c14 is already in the snapshot), with its writing block, using the template note below.
- **Environment note:** `build.py` needs `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (apt; run `apt-get update` first), and a full Git checkout.

### What chapter 13 added to the template below

- A **single-unit chapter** uses `label='13'`, `unit_id='ms-c13'`, `extra=None` and the menu entry `("…", "Health", [("13", [])])`; there is no Block "Skills" and no additional block. Genre names are free text (`Health`).
- Kata-Kata gives **six frames**; the charter allows five patterns, so a pattern can carry two frames (the pattern ID string is `ms-c13-f05 and f06`; `pattern_ids` still lists all six). The model conversation is limited to 16 turns: put the first 14 scenario lines in it and the rest (the pharmacy) in the task key and the E-block listening. Every scenario line must still appear word for word somewhere in the unit.
- A statement with a third-person doer or an aspect word uses the meN- verb the ledger has (the chapter 12 -kan rule); a bare ‹-i› or ‹-kan› verb is for requests and first-person replies. `tests/test_stage2_ch12.py::test_kan_rule_in_statements` and `tests/test_stage2_ch13.py::test_kan_rule_in_statements` hold the regex.
- **Safety units:** a test checks that no diagnosis, medicine, dose or dosing instruction appears in Malay and that the doctor and pharmacist lines are from a short allowed list. Reuse it for any later health-adjacent chapter.
- A spoken form that is part of a ledger headword (L-1200 «cuti sakit / MC») needs a `GLOSS` entry when the meaning contains Malay; label «MC» spoken wherever it appears. Test-item `words` are headwords («dibenarkan», not «tidak dibenarkan»). A quoted formal word to avoid («ialah») is a «…» mention in a teacher note and is checked out of the pupil-facing lines only.
- Retiring a legacy pack: add its lesson titles to `superseded` in `course.py`, drop its group from the final list, remove exactly its keys from `curriculum/legacy-exceptions.json`, add the titles to `retired` in `tests/test_catalogue.py`, and lower the exception count in the tests (now 20).

## Previous session: Stage 2 build step 4, chapter 11 fixes and chapter 12 (13 Nov 2026, Claude)

- **Authorised:** Sam (build step 4, chapter 12 instruction, 13 Nov 2026): the chapter 11 fixes in their own commit, then units 12A and 12B; push to main when the checks pass; **stop after chapter 12 for Claude's review** before chapter 13. Started at `839ea18`. Report: `docs/STAGE-2-ch12-report.md`.
- **Chapter 11 fixes (`76964a3`):** 11A pattern 2 «Siapa yang membaca emel itu?»; 11A model conversation «Encik Tanaka yang membeli kopi itu.» (the question before it is now «Siapa yang membeli kopi itu?»; teacher note: focus with «yang» in speech, di- … oleh for drills and written notices); «dari atas meja»; 11B listening «Seratus ringgit untuk satu hari.» (the revision word «setiap» was dropped from 11B). Sam's seven answers are in `docs/stage-2-decisions.md` section 8. «tandatangan» and the word-proposals backlog are in the two lists below.
- **Chapter 12 (the commit after `76964a3`):** unit 12A (parcels at the guardhouse, ‹-kan› requests: 23 core + «nombor tracking» to recognise), unit 12B (the ceiling leak, ‹-i› and more ‹-kan›: 21 core), the **writing block after 12A**, the **review block after 12B** (the plan's Review 2; your brief named the writing block only: see question 1 in the report) and the chapter 12 fast pack: 12 blocks = 9 h, plus 1 fast block. All three are in `curriculum/reauthored-units.json` with zero gaps and zero violations. Build: 450 packs, 2,797 pages, still 22 violations and 203 gaps (none in chapter 12). **207 tests** pass (14 new in `tests/test_stage2_ch12.py`).
- **Waiting for:** Claude's review of chapter 12; Sam's answers to the questions at the end of the report and the 12 native-read lines.
- **Next:** after the review, chapter 13 (negation, permission and advice in health situations; Kata-Kata c13 is already in the snapshot) with the template note below.
- **Environment note:** `build.py` needs `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (apt; run `apt-get update` first), and a full Git checkout.

### What chapter 12 added to the template below

- A unit can have **one recognition word in 12A and none in 12B**; speaker labels must be English («Guard», «Office») because «pengawal» and «pejabat» are ledger words and an unmarked Malay speaker label stops the build.
- A suffix is shown with ‹-kan›, ‹-i›, ‹pe-›, ‹ke-an›, ‹-an› (all in `curriculum/malay-mentions.json`); a root that is a ledger word placed by the chapter is «root», otherwise ‹root› with a sourced mention (new: ‹beri›, ‹tunjuk›, ‹pasti›, ‹kawal›, ‹milik›, ‹jejak›, ‹hubung›, ‹bocor›, ‹hidup›, ‹mati›, ‹adu›, ‹kepada›, ‹sih›). A bare ledger form such as «mana» or «pondok» is a ledger gap: write «di mana», «pondok pengawal».
- Test-item `words` must be ledger headwords («borang», «aduan», not «borang aduan»). English prose uses "slot" (added to `ENGLISH_HOMOGRAPHS`); ledger meanings that contain Malay need a `GLOSS` entry (done for L-1179 and L-1180).
- A word in the starred wrong form that has two parts fails the unmarked-Malay check; describe it in words («a に-word such as «dengan»»).
- `ROOTS` for a suffix unit holds `(root, where, where_ja, what the suffix adds, in Japanese)`.
- The old "future" placeholder «Ambil bungkusan di lobi» was listed as Chapter 12 beside the new chapter 12; Sam decided to retire it (13 Nov 2026) and it is gone (see the chapter 13 session above).

## Previous session: Stage 2 build step 4, chapter 10 fix and chapter 11 (13 Nov 2026, Claude)

- **Authorised:** Sam (build step 4, chapter 11 instruction, 13 Nov 2026): one chapter 10 fix, then units 11A and 11B; push to main when the checks pass; **stop after chapter 11 for Claude's review** before chapter 12. Started at `8ada95c`. Report: `docs/STAGE-2-ch11-report.md`.
- **Chapter 10 fix (`0853da9`):** 10A pattern 3 is now «Tidak juga. Saya lebih suka berbasikal.» (Sam: «Tidak sangat» is not natural). Sam's six answers to the chapter 10 questions are in `docs/stage-2-decisions.md` section 7: Japanese and English explanations only; the fast pack and writing block belong with each chapter; «Belum.» confirmed; «berminat untuk» + a verb stays the taught pattern (a noun waits for chapter 18); Hanashishou links are named only until step 6; `ms-stage2-<name>` ids are fine. No word proposals from chapter 10 were added.
- **Chapter 11 (the commit after `0853da9`):** unit 11A (who did what at the office with «Puan» Aini, «Encik» Rahman: 20 core), unit 11B (the draft, the deadline and the weekend with «Cik» Mei Ling: 21 core, «tukar» and «deadline» recognise only), the **review block after 11B** (the plan's Review 1; the plan gives chapter 11 no writing block, see question 1 in the report) and the chapter 11 fast pack: 11 blocks = 8.25 h, plus 1 fast block. All three are in `curriculum/reauthored-units.json` with zero gaps and zero violations. Build: 411 packs, 2,572 pages, still 22 violations and 203 gaps (none in chapter 11). **193 tests** pass (13 new in `tests/test_stage2_ch11.py`).
- **Waiting for:** Claude's review of chapter 11; Sam's answers to the seven questions at the end of the report (review block or writing block, «menelefon» in 11A, «menghantar» = take someone, the plain-root request rule, spoken «tukar» and «deadline», the pilot cut, the changed page note) and the 12 lines for the native reader. Word proposals (none added to the ledger): «kepada», «bukit», «menempah», the di- partners of the 11B verbs, «sehari», «menyapu».
- **Next:** after the review, chapter 12 (-kan and -i) with the template note below (Kata-Kata c12 is already in the snapshot).
- **Environment note for the next builder:** `build.py` needs `pymupdf`, `fonttools`, `brotli` and the `fonts-noto-cjk` package (the Noto Sans CJK path in `build.py`), and a full (not shallow) Git checkout.

### What chapter 11 added to the template below

- `chapter10_common` was imported unchanged again. A unit can pass `extra` for a review block with `kind='review'`; it needs `plan`, `model`, `task`, `check`, `answer` and `explain`.
- When a Kata-Kata scenario has more lines than fit one unit, split it by scene (11A s01 to s08, 11B s09 to s18) and check every line is in the right unit. A scene line may use a core word of the other unit of the same chapter (11A uses «menelefon» from 11B): gloss it in the teacher notes.
- Test-item `words` must be ledger headwords: write «tarikh akhir» and «hujung minggu», not their parts.
- A starred wrong form (*mempanggil) in a teacher note is fine; a wrong form inside «…» in a pupil-facing line is not. English prose needs «di-» (marked) for the prefix and «…» for every Malay name, title and food word; Japanese cells quote Malay with «…», not 「…」.
- English words that are also ledger entries (hiking, deadline, travel, badminton) go in `ENGLISH_HOMOGRAPHS` in `suite/__init__.py`. A ledger gloss that contains Malay needs a `GLOSS` entry (done for «kira» and «roti canai»).
- A revision word must appear in a «…» span outside the vocabulary list, or the test fails; drop it from the list rather than force it in.

## Previous session: Stage 2 build step 4, Kata-Kata refresh and chapter 10 (13 Nov 2026, Claude)

- **Authorised:** Sam (build step 4 instruction, 13 Nov 2026): refresh the Kata-Kata reference copy, then author units 10A and 10B; push to main when the checks pass; **stop after chapter 10 for Claude's review** before chapters 11 to 17. Started at `a24a993`. Report: `docs/STAGE-2-ch10-report.md`.
- **Part 1, refresh (`382dfec`):** `curriculum/reference/katakata/c10.json` to `c18.json` added and both ledger copies replaced from Kata-Kata **7fbe173** (c01 to c09 unchanged). `docs/handoff/ledger-snapshot.csv` is the Kata-Kata file byte for byte (CRLF); the reference copy is the same file with LF. Kata-Kata `content/rules/SOURCE.json` pins a24a993, and its three rule files match ours byte for byte. Ledger: 1,272 rows; **Stage 2 core 240** (56 existing + 184 new), recounted and updated in `docs/stage-2-plan.md`. The live charter states no 233; the other places that do are listed in the report. Build before and after: 22 violations, 203 gaps.
- **Part 2, chapter 10 (the commit after `382dfec`):** unit 10A (the working day with «Puan» Aini: 20 core), unit 10B (background and the new neighbour «Puan» Siti: 20 core, «pindah» recognise only), the writing block after 10B, and the chapter 10 fast pack: 11 blocks = 8.25 h, plus 1 fast block. All three are in `curriculum/reauthored-units.json`, with zero gaps and zero violations. Build: 373 packs, 2,356 pages, still 22 violations and 203 gaps (none in chapter 10). **180 tests** pass (13 new in `tests/test_stage2_ch10.py`).
- **Waiting for:** Claude's review of chapter 10; Sam's answers to the six questions at the end of the report (Malay explainers for Stage 2, scope of this step, «Belum.» for marriage, «berminat» + a noun, the Hanashishou links, block ids) and the 12 lines for the native reader. Word proposals (none added to the ledger): «kolam renang», «taman», «seminggu», «penuh», «bersukan», «hidup».
- **Next:** after the review, chapters 11 to 17 with the template note below (Kata-Kata c11 to c17 are already in the snapshot).

### Template for the chapter 11 to 17 sessions (from chapter 10)

**What to copy**
1. **Helper:** import `suite/chapter10_common.py` unchanged (`components`, `unit_dict`). It takes everything chapter-specific from the unit config: `chapter`, `unit_id`, `label`, `grammar_ids`, `question_note` (and `questions_added` when a chapter adds a question word), `markers` (title, grammar key, items, bridge, key, explain), `card_range`, `frame_list`, `plan` with `E_listening`, `E_roleplay`, `E_variation` (Block E is a scene transfer), `hanashishou_note`, `next_note`, and `extra` for a writing or review block (it needs `plan`; set `kind='review'` for a review block). Do not copy the helper per chapter.
2. **Unit file:** start from `suite/ms_c10a.py` or `ms_c10b.py`. Core groups are the rows the ledger places as `ChN (unit X)` (recompute them; never type the list from the plan). Recognition rows are those whose place says "recognition". `ROOTS` / `VOCAB_OPTS` show each affixed form with its root as the Kata-Kata card note gives it: «root» when the root is a ledger word placed at or before the chapter, ‹root› (with a sourced entry in `curriculum/malay-mentions.json`) otherwise. Revision lists hold only words placed earlier that the unit really uses outside the vocabulary list (the test fails otherwise).
3. **Grammar points:** add `ms-cNN-g02…` to `GRAMMAR` in `suite/__init__.py` and the chapter's FOCUS and GOALS to `catalogue.py` (`CHAPTERS_BUILT` follows `GOALS`).
4. **Menu:** add the chapter to `MALAY_CHAPTERS` in `course.py` with its unit labels, and give its status line in the `status=` chain.
5. **Fast pack:** a `chapterNN(ledger)` function and a `STAGE2_PACKS.append(…)` in `suite/fast.py` (`level='A2'`; 20 core words; 5 patterns with two examples each; a conversation of 10 to 16 turns; task; 5 self-check items; self-study guide with `pack_cards(n)` and `last_card(n)`).
6. **Extra blocks:** add them to `extra_blocks` and `stage2_blocks` in `catalogue.py` (reviews after 11B, 12B and 15; writing after 12A, 14 and 16).
7. **Register** the units and the fast pack in `curriculum/reauthored-units.json`.
8. **Tests:** copy `tests/test_stage2_ch10.py` and change the chapter, units, frame lists and scenario ranges. Then update `test_catalogue.test_structure` (chapters, units, blocks and slots).

**What to check before each commit**
- **«dari» and «daripada» (Sam, 13 Nov 2026):** «dari» is for places, times and directions («dari Osaka», «dari pukul sembilan», «dari atas meja»); «daripada» is for people and organisations («mesej daripada kedai itu», «cuti sakit daripada doktor», «surat daripada bank itu») and for comparisons («lebih … daripada»). «daripada» is ledger row L-0267 (Ch6). Check every «dari» before a person or an organisation.
- **Bare roots in dialogue (Sam, 13 Nov 2026):** a dialogue line may use the everyday bare root after an aspect word or a modal, as Kata-Kata does («Saya belum isi borang.», «Encik perlu daftar dulu.», «Doktor akan panggil cik.»). Pattern models, drills, answer keys, notices and written texts (readings, writing models) use the meN- form the ledger has («Saya belum mengisi borang.»). Bare ‹-kan› stays for requests and first-person offers («Tolong simpankan …», «Saya hantarkan sekarang.»); the chapter 12 -kan rule is unchanged otherwise.
- **Natural speech in casual turns:** no ruling-style words («keputusan», «ialah», di- … oleh) in casual dialogue lines; rewrite the line, and list any needed word that is not in the ledger on the backlog instead of adding it.
- Check every new «…» line at the chapter with the checker before it goes into the file: `Checker().inspect([...])` at chapter N, kind `model`, with `python3 tools/check_spans.py N suite/ms_cNN….py` (added in this step; it prints every span with a violation or a ledger gap). Fix any gap by rewriting the line, or list the word as a proposal. **Never add a ledger row.**
- Gates: meN- from 11 (meN-…-kan and meN-…-i need 12 as well); -kan and -i from 12; accident ter- from 16; «lah» joined from 17. Every affixed form must be its own ledger row placed by the chapter. **«lah» and «kan» are never in an answer key.** A spoken form needs its standard form taught earlier with a "spoken" label in a vocabulary or model line (the register check reads the order of the components).
- English prose: mark Malay titles and words («Encik» Lim, «Puan» Siti's) or the build stops. Names go in `curriculum/malay-proper-nouns.json`; a word quoted but not taught is a ‹…› mention with a source.
- Kata-Kata alignment: the chapter's frames as pattern IDs; every scenario line and frame example used word for word; card IDs in the openers, the vocabulary, the teacher notes (the card traps) and the culture sources.
- Minimums (the copied test enforces them): 3 to 5 patterns with 4 to 6 Q&A; drill types 1 to 5 with at least 6 items each (30+), 3+ short dialogues, the markers drill, the cumulative question-word drill (18 tasks); model 10 to 16 turns with gaps and a variant; listening 120 to 250 Malay words with 6+ questions; reading with 5+ questions and a model answer; task with a change of plan; culture note of 150 to 300 words with a full Japanese translation and named sources; 15 to 20 scored items plus speaking.
- Run `python3 build.py` and `python3 -m unittest discover -s tests`; commit the rebuilt `dist/` when lesson content changed; fetch, rebase and push to main.

## Previous session: Stage 2 step 4a, two changes to the shared stage rules (13 Nov 2026, Claude)

- **Authorised:** Sam, so Kata-Kata can finish chapter 17. Details in `docs/STAGE-2-step2-report.md` ("Step 4a amendments"). Rules file and fixtures are ready to copy to Kata-Kata unchanged in format.
- **Done:** (1) R3 pair is now tak tahan / **tidak boleh tahan**. (2) Written -lah joined to a word is read from chapter 17 (`-lah` derivation), as in Kata-Kata. Fixtures 72 to 77. 167 tests pass (165 before, plus 2 new test methods); `build.py` unchanged (335 packs, 2,140 pages, 22 violations, 203 gaps).
- **Not done (by instruction):** `curriculum/reference/katakata/` not refreshed (step 4, after Kata-Kata is final); Kata-Kata, Hanashishou and the ledger untouched. I did not run Kata-Kata's checker on the new fixtures (the run was blocked); Kata-Kata should confirm all 77 agree.
- **Next:** Kata-Kata copies `stage-rules.json` and `stage-rules-fixtures.json` from the commit named in the report (update its 72-case count and SOURCE.json hashes), builds the L-0690 card; then step 4 here refreshes the snapshot (which will also make «takpe» a known form).

## Previous session: Stage 2 build step 2, stage-aware language checks (13 Nov 2026, Claude)

- **Authorised scope:** Sam's build step 2 instruction (13 Nov 2026): make the Malay checks stage-aware; no chapter content, no ledger edits; publication to main pre-approved when the checks pass. Started at `9474aeb`. Report: `docs/STAGE-2-step2-report.md`.
- **Done:** `language_checks.py` now reads its gates, whole words, look-alike roots, register pairs, particles and disallowed forms from the new shared file `curriculum/stage-rules.json`. Gates: ber- 10, meN- 11, -kan and -i 12, accident ter- 16; a gated form also needs its own ledger row placed at or before the unit's chapter. Placement is read strictly from the place column; every pinned Kata-Kata chapter file is loaded. New R3 register pairs (tak apa and takpe with «tidak mengapa», tak tahan, set, kat), the R4 particle rule (no test answer key may require «lah» or «kan») and the new disallowed forms (berbicara, perbaiki, musik, film, olahraga, apotek, kantor, bersepeda, antre, berwisata, kecelakaan; mobil and uang already listed), allowed only in a ‹…› "do not use" mention.
- **Stage 1 unchanged:** old and new checkers give identical violations, reasons, gaps and derivations on all 13,586 checked segments. `python3 build.py` passes (335 packs, 2,140 pages; 22 violations, all in the baseline of 30); all **165** tests pass (10 new in `tests/test_stage_rules.py`, which also runs the 72 shared cases in `curriculum/stage-rules-fixtures.json`).
- **Sam's answers (13 Nov 2026, in chat; recorded here and in the report):** (1) teach **«tidak mengapa» (spoken: «takpe» / «tak apa»)** so all three are covered; both spoken forms are paired with it (the «tak apa» pair from chapter 10, because Stage 1 unit 5 shows «tak apa» as Dunia recognition; «takpe», tak tahan, set and kat in every chapter). (2) The disallowed forms as added, and saku, darurat, berdagang, berteman and menikah left out: confirmed. (3) Stative ter- words («terbuka» alone) stay gated at 16 unless Sam approves a whole word: confirmed.
- **Ledger follow-up (needs a ledger session; not done here):** a Journal row for answer (1); L-1261 «tidak mengapa» stays Ch17 core, with its meaning cells naming both spoken forms; a row (or an L-0940 variant) for «takpe» as a marked spoken form in chapter 17, written before any content uses it.
- **Next:** build step 3 in Kata-Kata (packs c10 to c18 and the stage-aware affix guard reading `curriculum/stage-rules.json`, with chapter-scoped exemptions and the shared fixtures), then step 4 here. When a Stage 2 unit is built, register it in `curriculum/reauthored-units.json`, and add any ‹…› "do not use" note to `curriculum/malay-mentions.json` with its source.

### Shared stage rules: `curriculum/stage-rules.json` (format v1)

One JSON file for Cikgu Sensai and Kata-Kata; its `format` key is the full specification. In short:

| Key | Contents |
| --- | --- |
| `affix_gates` | `{family, chapter, ledger_tags, detect, enforced_by, note}` for every affix rule, Stage 1 (-nya, -kah, -an 2; ke- ordinal 3; ter- superlative and se- comparison 6; se- + classifier 8; di- 9) and Stage 2 (ber- 10, meN- 11, -kan and -i 12, ter- accident 16) |
| `stage_aware_rule`, `family_resolution`, `shape_tests` (in `format`) | How a word's families are found (ledger tag first, else spelling) and when it passes (all gates open and its own row placed at or before the chapter) |
| `whole_words` | `{form, chapter, ledger_id, reason}`: lexicalised or allow-listed words that look affixed, whole words at their own chapter (a test checks each chapter against the ledger) |
| `ter_superlatives` | termurah, terbesar, terbaik, tercantik (chapter 6; never open accident ter-) |
| `lookalike_roots` | The Kata-Kata allow-list and Sam's local list (must equal `curriculum/malay-roots.json`) |
| `register_pairs` | `{spoken, standard, from_chapter, decision}` |
| `particles` | «lah» and «kan»: recognition only in tests (R4) |
| `disallowed_forms` | Indonesian form → Malaysian form, with sources in `disallowed_forms_sources` |

`curriculum/stage-rules-fixtures.json` holds the shared cases (segments, expected pass or fail, the failing check). Change either file only with Sam's approval, recorded in the ledger Journal or here.

## Previous session: Stage 2 build step 1, the ledger (13 Nov 2026, Claude)

- **Authorised scope:** Sam asked Claude to do build step 1 in this session: Journal entries for the 13 Nov answers first, then the new rows and placements, reading the sheet back after each batch, then regenerate the copies, build, test and push.
- **Sheet:** Journal rows 130 to 132 (Sam's answers) and 133 to 145 (the changes). Ledger rows **L-1089 to L-1265** (177 new, chapters 10 to 17, Draft, Action "KD4 check"); 56 existing rows placed as Stage 2 core and L-0604, L-0608, L-0667, L-0678 as recognition; L-0623 narrowed to "Handbag". Written in three new-row batches and one placement batch; after each, the whole Ledger tab was read back and compared cell by cell with the plan (zero unplanned differences). Before writing, a local dry run with the planned ledger found the problems below, so they were fixed before the sheet was touched.
- **For Sam to confirm:** L-0657 «tempat kerja» was **not** placed in 10A, because the A1 test (version A) already uses the form label «Tempat kerja» (two Stage 1 words); placing it in Ch10 would make approved Stage 1 content a forward reference. Stage 2 core in the ledger is therefore 233 (56 existing + 177 new). Journal row 144. **Now 240** (56 existing + 184 new, L-1089 to L-1272) since the build step 4 refresh: Sam's seven later rows L-1266 «takpe», L-1267 «tidak boleh tahan», L-1268 to L-1272 «mendaftar», «tangguhkan», «batalkan», «memakai», «berwarna».
- **Code and content changed because of the new rows:** six lines of the legacy chapter 12 pack "Ambil bungkusan di lobi" (`curriculum/foundation.txt`, `curriculum/foundation-guided.txt`) no longer use «ni», «jadi», «perlu», «macam tu» (now placed in chapters 13, 14, 17), with `curriculum/malay-text-scope.json` updated for exactly those lines (Journal row 145); `ENGLISH_HOMOGRAPHS` in `suite/__init__.py` gains «bernama» (Bernama in English source notes) and «label»; tests: the ledger row count (1,265), and the two legacy-content tests list the six edited lines. Build passes (335 packs, 2,140 pages; current violations 22, was 24); all 155 tests pass.
- **Next:** build step 2 (Cikgu Sensai stage-aware language checks and affix allow-list; recommended model Opus), then steps 3 to 6 as in section 6 of `docs/stage-2-plan.md`, all chapters without a pilot pause.

## Previous session: Stage 2, Batch 1b, audit of the Stage 2 plan (12 Nov 2026, Claude)

- **Authorised scope:** Sam decided that Claude builds Stage 2 and authorised this audit: planning only, no ledger writes except regenerating the copies, no chapter suites; publication to main pre-approved when the checks pass. Started at `f06aefd`.
- **Commits:** `29f0217` both ledger copies and the hash regenerated from the sheet (only the "Action (open)" column changed: 119 rows, Journal row 129; old copies regenerated byte for byte first); `3f3c367` Stage 1 tidy-up (unit 5 pattern 4 tagged `ms-c05-f04, ms-c05-f06`, unit 6 pattern 4 tagged `ms-c06-f05, ms-c06-f07`, both fast packs and the two pattern tests); then the commit with the audited plan, `docs/stage-2-decisions.md`, `docs/STAGE-2-audit-report.md` and this note. `python3 build.py` passes and all **155** tests pass at each commit. The session branch `claude/stage-2-audit-batch-1b-pckuxt` is kept at the same commit as main.
- **Stage 2 state:** `docs/stage-2-plan.md` is now an **audited draft**: 233 core words (57 existing ledger rows, 176 new; the draft had 235 = 53 + 182; **240 in the ledger since build step 4**, see the latest session), every unit 19 to 24, each form marked kept / changed / added / moved, dropped forms listed under each unit, and an Audit log at the end. Section 3's checker design is simplified (the ledger drives the gate; one row per taught form); section 6 is the six-step build order with a model per step. Report: `docs/STAGE-2-audit-report.md`.
- **Decided by Sam earlier, not to be asked again:** the Kamus Dewan check and the native Japanese review happen once, at the end of the whole project (Journal row 128), so they do not block the Stage 2 ledger writes.
- **Sam's decisions (13 Nov 2026, in chat):** every recommendation in `docs/stage-2-decisions.md` accepted (answers filled in there and listed at the end of `docs/stage-2-plan.md`). Specifics: W6, W7, W8 yes («mengecas», «jemputan», «cuti sakit» with spoken «MC»); W9 yes («bertolak» added to 10A, so 234 core = 57 existing + 177 new); R1 (a) («nombor penjejakan» new row, L-0608 spoken partner); **G3 no: no chapter 10 pilot, build every chapter** (Opus review after each); B1 yes (build order and models). **R7: Claude edited the charter** on 13 Nov at Sam's request: section 5 now says ber- has no nasal sound changes, with be- (berehat, bekerja) and bel- (belajar) as its only variants; live doc revision after the edit `AHj4eMSiZ2Bi0VYza6rfuGEwhR0jNx-K08GRWRaGFfRS5EPNdsErDIThh77qP-biwg8OHRd9oaw9TU2awOU3r63hS25VE1kndIA2GEIrdYw`; `docs/handoff/charter-snapshot.md` matches.
- **Next: build step 1, the ledger session** (section 6 of `docs/stage-2-plan.md`; recommended model Sonnet). First write Journal rows recording Sam's 13 Nov answers; then write the 234 approved forms to the Ledger tab (177 new rows as Draft with "KD4 check" in Action and the root in "Root (KD4)"; the 57 existing rows placed in their units; the recognition rows L-0667, L-0604, L-0678, L-0608 placed as recognition), regenerate both copies and the hash, and check the diff row by row. Then steps 2 to 6 in order, all chapters without a pilot pause. The Kamus Dewan check and the Japanese review stay at the end of the project.
- **Environment:** as before (`pip install pymupdf fonttools`, `apt-get update` then `apt-get install fonts-noto-cjk`, `git fetch --unshallow`). Hanashishou was attached read-only (`add_repo`) and shallow-cloned to `/home/user/hanashishou` at `55fd4ed` to verify the scene links; nothing was changed there. Build output in `dist/` was committed only where lesson content changed (`3f3c367`); the ledger-only commit left the nondeterministic PDF IDs out.
- **Left open from the sync session below, now done:** the sheet's Action column is cleared and both copies follow it; units 5 and 6 tag f06 and f07. Still open: the Hanashishou mapping of L-0592 to L-0330 (build step 6).

## Previous session: sync with the Kata-Kata Stage 1 clean-up (12 Nov 2026, Claude)

- **Authorised scope:** Sam authorised the sync and pre-approved publication to main when the checks pass. Started at `a82dcd0`. Nothing was changed in the ledger sheet or the Kata-Kata repository (read only).
- **What synced:** `curriculum/reference/katakata/c01.json` to `c09.json` are now Kata-Kata `content/ms/kelas/` at **Kata-Kata 34710c6** (end of the clean-up; report `docs/CLEANUP-2026-11-12.md` in that repo). Both ledger copies are Kata-Kata `content/ledger/malay-ledger.csv` at 34710c6 (L-0001 to L-1088, same rows in both; new card IDs and places, no "(pending)", L-0188 now «once; very (after an adjective)»). Line endings kept: LF for `curriculum/reference/katakata/malay-ledger.csv`, CRLF for `docs/handoff/ledger-snapshot.csv`. `docs/step4-sources.json` has the new ledger hash and, new, `kata_kata_commit` and `kata_kata_chapter_sha256`. `docs/restructure-sources.json` is left as the old baseline (0f78179). `catalogue.py` `source_url` now points at 34710c6.
- **Build and tests:** `python3 build.py` passes (335 packs, 2,140 pages fit-checked); all **155** unit tests pass (153 plus two new Kata-Kata clean-up tests).
- **Tests changed, and why** (all now check the real current state):
  1. `test_catalogue.test_pinned_sources` and `test_language_checks.test_no_content_or_reference_edits`: re-pinned the nine chapter files to the 34710c6 hashes in `docs/step4-sources.json`; the legacy-source part of the second test still compares with `c067e22`.
  2. `test_step5b` ch4 partition: the helper now ignores bracketed notes in the place cell ("Ch4 (reviewed in Ch7)"); the ledger now has **72 live Ch4 rows, one more than the 71 teaching entries**, because L-0304 «depan / hadapan» is "one card with L-0173" (ms-c04-019, merged from ms-c07-009). The 4B entry for L-0173 now shows «depan» / «hadapan» (formal), so both rows are taught; the test checks the shared card ID and that «hadapan» appears. 4A 40 + 4B 31 = 71 entries, unchanged.
  3. `test_step5e` ch7 partition: **62 rows** placed in Ch7 (was 63) because L-0304 left; all 62 are new core, so the "minus L-0304" step is gone. Unit 7 core is still 62.
  4. `test_step5f` ch8 partition: **58 rows** placed in Ch8 (was 60): «kaki» (L-0488, counter card removed) and the fruit «buah» (L-0514, card re-pointed to L-1067) are no longer placed in Ch8; 41 core + 11 recognition + 6 carried. Unit 8 core is still 41.
  5. `test_step5g` ch9 partition: the Dunia scene is now the general "Rumah terbuka" (13 Raya rows L-0537 to L-0549 plus 6 festival rows L-1070 to L-1075 share one place cell); new rows have their cards instead of "Ch9 (pending)". Unit 9 is unchanged: 42 core, 33 recognition. No Dunia word became a class card.
  6. Openers (`test_step5d` to `5g`): **cause of the chapter 9 failure:** the Sedia Kelas card counts in the openers were typed by hand and the clean-up changed every chapter's list (c01 26, c02 29, c03 31, c04 26, c05 27, c06 22, c07 28, c08 14, c09 16; the tests for 6 to 8 only compared the text with the same typed number, so they would never have noticed). The counts now come from `suite.sedia_cards(n)` (the pinned file), and the tests read the file through `tests/katakata_ref.py`. Fast-pack self-study lines use `pack_cards` and `last_card` the same way (all cards of chapters 3 to 9, their ID ranges, new frames f06 and f07).
  7. `test_step5h` stage review: **56 frames** (54 plus ms-c05-f06 «Kenapa / Mengapa» and ms-c06-f07 «Saya pilih»). The Tuesday scene now has «Baik, saya pilih mi goreng.» / «Kenapa encik tidak pilih nasi lemak?» / «Sebab nasi lemak lebih mahal.»; both frames are in `FRAME_RETURNS`, the role card, success criteria and can-do check. The count rule itself is unchanged (all frames of chapters 1 to 9).
  8. `test_step5h` Kata-Kata clean-up: replaced the "121 ledger rows name Kata-Kata" test with three: no ledger row has an open Kata-Kata action and every remaining action is a known kind (KD4 check, "refresh Cikgu Sensai snapshot", Hanashishou, retired rows); no "(pending)" or "Hari Raya" scene in a place cell; all 112 cards the brief listed exist in the pinned files.
- **Catalogue-tag failures:** none remained once the build ran on the new files; the stage review's `pattern_ids` and the catalogue's word and pattern lists follow the pinned files.
- **Old forms (grep):** «jalan lurus» appears only as "not used" teacher notes and tests; «kurang suku» only as "do not teach"; no Assalamualaikum or Waalaikumsalam in any lesson (only in the ledger's Retired row L-0009 and in notes about the removal); the Ch7 «depan» duplicate: Cikgu Sensai already taught one entry, and references to card ms-c07-009 now name ms-c04-019; «kaki» is never a counter (references to ms-c08-010 say it was removed). Text that said cards were "pending" or that a card "still teaches «jalan lurus»" was updated (units 1, 2A, 2B, 5, 7, 8, 9 keys and fast-pack lines).
- **Left open (not done here):** the sheet's Action column still says "refresh Cikgu Sensai snapshot" on 117 rows (Sam or a session with sheet access clears it, with a Journal row; this sync is that refresh); the Kamus Dewan checks and the native Japanese review (Kata-Kata report); unit 5 still teaches the «kenapa» set inside pattern 4 (tagged ms-c05-f04) and unit 6 «Saya pilih» inside pattern 5 (tagged ms-c06-f05), without tagging f06 or f07 as their own patterns, as with ms-c09-f06; the Hanashishou mapping of L-0592 to L-0330.
- **Next (superseded by Batch 1b above):** Sam's pilot of Stage 1; the seven Stage 2 plan questions are replaced by `docs/stage-2-decisions.md`.

## Previous session: Stage 2, Batch 1 planning (12 Nov 2026, ChatGPT)

- **Authorised scope:** Sam explicitly authorised the Stage 2 plan and word lists, planning only, and pre-approved publishing `docs/stage-2-plan.md` to main. This supersedes the older “wait for go-ahead” wording for planning only. No Stage 2 suites, ledger writes or checker implementation are authorised.
- **Completed:** all six sections of `docs/stage-2-plan.md`: 11 teaching units; 67 blocks / 50.25 hours; nine fast packs; 235 proposed core forms (53 existing unplaced rows, 182 proposed new forms); chapter 18 review-only; chapter affix gates; can-do refinements; inspected Hanashishou links; cross-tool build order and seven questions for Sam.
- **Sources reconciled:** started at `bb72bc5`; preserved concurrent Stage 1 commits `a52c6a0`, `55db51d`, `9d719e8`, and the docs-only hours correction `a4099cf`. Read the updated handoff and `docs/STEP-5i-report.md`. Final ledger copy has L-0001–L-1088; no ledger file was changed by this planning session. The current Google Doc was read and rechecked; Japanese remains draft.
- **Publication:** sections 1–5 were saved as separate main commits, most recently `3e2c1ac83fc9d1ceebb4c55627fe0e733182dc86`. The final commit is the one containing this note and completed section 6; see its Git history for the exact SHA. Shell push lacked credentials, so commits used the connected GitHub service with current-file/branch checks. No external repository was edited.
- **Validation:** final full-history build and 153 tests pass against updated main (335 packs, 2,139 pages fit-checked). This is docs-only validation, not approval of proposed Malay/Japanese. Generated PDF/archive changes were excluded. Existing core IDs, uniqueness, prior placements and totals were checked separately.
- **Half-done work:** none within this planning batch. Dictionary/native review, proposed family mappings, stage-aware checkers, c10–c18, scene adaptations and A2 assessment are future work, not partially built features.
- **Next and stop point:** Claude reviews the plan with Sam. Sam answers the seven questions at the end of section 6; any approved vocabulary/placement decision must then be recorded in the ledger Journal before a separately authorised ledger session. Do not write Stage 2 rows or suites on the strength of this plan alone. Stage 1 pilot and step 5i questions remain as below.

## Stage 1 state at the step 5i handoff

- **Last updated:** 12 Nov 2026, Claude: step 5i, the Stage 1 follow-ups (Sam's answers to the step 5h questions). Details in `docs/STEP-5i-report.md`.
- **Stage 1 is complete and awaits Sam's pilot:** chapters 1 to 9 (units 1, 2A, 2B, 3A, 3B, 3C, 4A, 4B, 5, 6, 7, 8, 9 and the nine fast packs), the review blocks after 3A, 4B and 6, the writing blocks after 2B, 3C, 5 and 7, the pronunciation block, the **stage review** after unit 9 and the **A1 stage test** (versions A and B). **Do not start Stage 2 (chapters 10 to 18) before Sam says so.**
- **Most recent approved scope:** step 5i only (Sam authorised it on 12 Nov 2026 and pre-approved publication to main when the checks pass).
- **Last commit on main:** the commit that updates this file (it follows `55db51d` the A1 test changes and `a52c6a0` the ledger and unit 9 changes). Build and all 153 tests pass. The session branch `claude/nifty-edison-3lz6o9` is at the same commit as main.
- **Stage close source:** `suite/stage1.py` (unit `ms-stage1`: the review block, the test builders, scripts, administration sheet, `item_map`, `compulsory_codes`, `stage_record`), `suite/stage1_test_a.py` and `suite/stage1_test_b.py` (test data). Tests: `tests/test_step5h_stage1.py`.
- **Unit 9 now:** **42 core words** in six groups (18 «di-» verbs; 4 roots; «oleh», «pada», «tadi», «siap»; 9 signs and notices, now with «perhatian», «hingga», «tolak», «tarik»; 5 for a party and an open house, now with «pesta»; 2 family), 33 recognition, 74 revision. «Selamat Pesta Kaamatan» is taught (sourced: Bernama, 30 May 2026); the formal «Selamat Menyambut Pesta Kaamatan» is a ‹…› mention only.
- **Ledger:** both copies and the hash match the sheet, L-0001 to L-1088 (Journal rows to 89). L-1084 to L-1088 are Ch9 (pending); KD4 check not yet run.
- **Charter decisions by Sam, 12 Nov 2026 (ledger Journal row 89 and the charter):**
  1. **Pass mark:** 48 of 80 with at least 10 of 20 in each section (recorded as Sam's decision in the administration sheet and the catalogue's `pass_rule`).
  2. **Class time:** the A1 test takes two extra 45-minute blocks (written papers, then speaking); the Stage 1 plan is **76 blocks** = 57 class hours (Claude corrected the charter from "about 57.5" on 12 Nov; 76 × 45 minutes is 57.0). `catalogue.py` `hour_budget.class_blocks` is 76.
  3. **`writing` is an accepted test-item type** (stage test only). This is a charter decision; `catalogue.py` accepts it and `docs/DATA-MODEL.md` says so.
  4. **Chapter 6 is compulsory in both test versions:** listening item L5 («lebih … daripada», «paling») and speaking card 2, which the examiner always uses (the second card is chosen from cards 1, 3 and 4). To keep sections at 20 marks, one earlier listening item per version was removed; the listening paper is five tasks, ten items.
- **Catalogue:** a `stages` record `ms-stage1` (CEFR A1, completion flag `stage1_complete`, label "Malay A1 · Stage 1 complete", pass rule, `compulsory_items`, item-to-chapter map); chapters carry `stage_id`.
- **Proposed, awaiting Sam:** the proposals in `docs/kata-kata-cleanup.md`; the answers to the five questions at the end of `docs/STEP-5i-report.md` (hours 57 or 57.5; the removed listening item; card 2; the Kaamatan and Gawai greetings in the test).

## Done

| Step | What | Report |
| --- | --- | --- |
| 1 | Malay units regrouped into 9 A1 chapters and 13 unit slots; wording preserved; issues logged | `docs/STEP-1-REPORT.md` |
| 2 | Catalogue: chapter records, 11 component types, tags, test-item contract | `docs/STEP-2-REPORT.md` |
| 3 | Build checks (ledger, register, affix, Malaysian form) with a frozen, shrink-only exception baseline of 86 keys | `docs/STEP-3-REPORT.md` |
| 4 | Pilot: full 11-component suites for units 1, 2A, 2B (plus pronunciation and writing blocks) and fast packs for chapters 1 and 2; all section 6 minimums and section 14 drills met and tested; baseline 86 → 79 | `docs/STEP-4-REPORT.md` |
| 5a | Chapter 3 (3A, 3B, 3C) and its one-session fast pack, with 73 unique core and 24 recognition entries; source and printed packs tested in the step-5a gate; no chapter 4 | docs/STEP-5a-report.md |
| 5b | Chapter 4 (4A, 4B) and its fast pack: 71 core, 55 Dunia recognition by scene, timeline drill, review block after 4B; legacy chapter 4 packs retired | `docs/STEP-5b-report.md` |
| 5c | Chapter 5 (unit 5, writing block) and its fast pack: 63 core in six groups, 50 Dunia recognition by scene, «bagaimana» and «kenapa» / «mengapa» / «apa sebab» with «sebab» / «kerana» added to the question words, markers drill; legacy chapter 5 packs retired | `docs/STEP-5c-report.md` |
| 5d | Chapter 6 (unit 6) and its fast pack: 32 core in six groups, 14 Dunia recognition, «yang mana» added to the question words, markers drill with comparisons, six whole ter-/se- words; legacy chapter 6 pack retired | `docs/STEP-5d-report.md` |
| 5e | Unit 6 follow-ups («sewa», «bilik», «luas»; 35 core), review block after unit 6, chapter 7 (unit 7: 56 core in five groups, 33 Dunia recognition by scene) and its fast pack; «ke» taught; places of worship as an even-handed landmark set (five ledger rows); «ke mana», «dari mana», «berapa jauh», «berapa lama» added to the question words; legacy chapter 7 packs retired | `docs/STEP-5e-report.md` |
| 5f | Unit 7 follow-ups («terus» not «jalan lurus»; «sesak»; five new ledger rows; «tumpang tanya» as revision; 62 core), the unit 7 writing block (directions by message), chapter 8 (unit 8: 35 core in four groups, 11 Dunia recognition «Beli baju», «seekor» / «sebiji» / «sebuah» as whole words, «berapa» with a counter) and its fast pack | `docs/STEP-5f-report.md` |
| 5g | Unit 8 follow-ups («se-» with every counter, the «gerai» scene, six new ledger rows, register labels; 41 core), six festival ledger rows, chapter 9 (unit 9: 29 core in four groups, 33 Dunia recognition including a general «rumah terbuka» scene with a note for each festival, the «di-» rule, `siapa` + `oleh`) and its fast pack | `docs/STEP-5g-report.md` |
| 5h | Unit 9 follow-ups (Sam's eight chapter 9 rows; 37 core; festival notes), the stage review block (a new colleague's first week; all 54 frames return; can-do self-check), the A1 stage test (versions A and B, four sections of 20 marks, keys, scripts, administration sheet, catalogue Stage 1 record) and the Kata-Kata clean-up list | `docs/STEP-5h-report.md` |
| 5i | Stage 1 follow-ups: ledger rows L-1084 to L-1088 (unit 9 is 42 core), «Selamat Pesta Kaamatan» sourced, pass mark 48 of 80, 76 blocks, `writing` accepted, compulsory chapter 6 comparison item and card in both A1 test versions, door signs / notices / «hingga» in unit 9 and the test reading paper | `docs/STEP-5i-report.md` |

## How step 4 works (for the next builder)

- Pilot content is in `suite/` (`ms_c01.py`, `ms_c02a.py`, `ms_c02b.py`, `fast.py`). Malay target text is marked `«…»`. Roots and standard forms quoted from Kata-Kata notes are marked `‹…›` and listed with their source in `curriculum/malay-mentions.json`. Names go in `curriculum/malay-proper-nouns.json`.
- Unmarked ledger Malay fails the build, and so does any ledger gap in a unit listed in `curriculum/reauthored-units.json`.
- `tests/test_step4_suite.py` encodes the charter section 6 minimums. Reuse it for chapters 3 to 9.
- Builds are not byte-reproducible: the PDF inside `bank.js` changes IDs on every build. Commit the build you tested, and compare the lesson JSON, not the bytes.
- A fresh cloud container needs `pip install pymupdf fonttools`, `apt-get install fonts-noto-cjk` and `git fetch --unshallow` before `python3 build.py` will run.
- Preview PDFs with poppler (`pdftoppm`). PyMuPDF's rasteriser garbles this font subset on screen; the PDF itself is fine.

## Chapter 3 review fixes (12 Nov 2026, Claude)

Sam asked for a targeted fix after Claude's review of step 5a. Word lists, the 3A/3B/3C split, components and tests are unchanged.

- **3C measurements rebuilt around a parcel at the post office.** In speech: «Berapa panjang / lebar / tinggi / berat bungkusan ini?» «Panjang tiga puluh sentimeter.» The ke-…-an nouns («ketinggian», «kepanjangan», «kelebaran», «kedalaman») are taught as written labels on forms and parcel labels only. Removed the "house" measurements («Kepanjangan rumah ini sepuluh meter», «Kedalaman ini dua meter»).
- **New natural scenes:** 3C model conversation and variant (post office), 3C listening (morning market, then post office), 3A listening (opening a bank account), 3B listening (fruit stall with «Kurang sikit, boleh?» and cash only). Removed filler such as «Ini nombor untuk kelas ini» and «Ini latihan nombor sahaja». The chapter 3 fast-pack conversation is now one coherent market exchange.
- **Fixed examples:** «Kosong ringgit» → phone digits; «Selepas kali pertama, kali kedua» and «Sebelum kali ketiga, kali kedua» → prices before and after a discount; post-office words were mislabelled "bank sign".
- **Culture notes rewritten as real culture, with full Japanese translations:** 3A mobile numbers (01x prefixes, digit groups, «kosong» vs «sifar»), tens and teens from card notes, age and forms of address; 3B ringgit and sen, Bank Negara Malaysia's 5-sen rounding of cash totals (BNM, 2007 announcement, in force since 2008), DuitNow QR, polite bargaining; 3C metric market weights, spoken sizes vs written ke-…-an nouns, «pertama» vs ‹kesatu›.
- **Real answer keys** for drills 1 to 5 in all three units (they had only a generic instruction).
- `chapter3_common.py` accepts an optional `test_listen_lines` so the listening test items use lines that contain a value.
- New mentions: ‹dalam›, ‹kesatu›, ‹se-› (Kata-Kata card notes).

## Quality rules for chapter 4 onward (from the chapter 3 review)

- **Natural Malaysian Malay first.** Every Malay line must be something a Malaysian would actually say in that situation. If the in-scope vocabulary cannot make a natural sentence, change the scene, not the Malay.
- **No filler to reach a count.** No classroom meta-talk inside scenes («untuk kelas ini», «latihan sahaja»), no repeated lines to pad listening, no empty example sentences.
- **Culture notes are about Malaysia,** not teaching instructions. Use facts that can be checked; name the source for anything specific (rules, dates, institutions). Teaching advice belongs in the teacher notes.
- **Japanese is a full translation** of the English, not a summary, and contains no leftover English.
- **Answer keys are real answers,** item by item.
- **Affixed nouns taught as labels:** if a ledger word is formal or written (like the ke-…-an measurement nouns), say so and show the everyday spoken form beside it.

## Step 5b: chapter 4 (12 Nov 2026, Claude)

- **Split.** 4A: clock, days and dates, frequency, «bila». 4B: tense and aspect markers, root routine verbs, the working day. «masa», «waktu», «depan» and «lepas» moved to 4B to reach 27/27 (reasons in the report); «tidak pernah» stays in 4A with the frequency scale.
- **Malay rules applied:** «pukul» for clock time with «pagi», «tengah hari», «petang», «malam»; «pukul empat suku», «pukul dua setengah»; :45 said in minutes; no «kurang suku» (ledger Journal, 6 Nov). «jam» for duration. Standard first: «dah» after «sudah», «tengah» after «sedang», both marked spoken; «balik» beside «pulang». Root verbs only. «ke», «kopi», «nasi», «mahu», «kedai» are placed after chapter 4, so scenes use «pergi kerja», «balik rumah», «sampai di …», «makanan».
- **Helper:** `chapter4_common.py` is a generalised copy of the chapter 3 helper. Differences: no automatic «…» marking (every Malay span is marked by hand), explicit word tags per test item, Dunia groups per scene, several revision groups, an optional timeline drill, and an optional extra block. Use it as the starting point for chapter 5 onward.
- **Culture notes:** 4A covers the 12-hour clock in speech, Malaysian Standard Time (UTC+8 since 1 Jan 1982) and the 45-hour week under the Employment Act (from 1 Jan 2023), with sources in the report. 4B covers «Sudah makan?», «belum» versus «tidak», and the spoken forms. Nothing religious; the state differences in the weekend are left out (Sam's rule).
- **Mentions added** to `curriculum/malay-mentions.json`: ‹biasa› (card ms-c04-030), ‹kurang suku› (named in teacher notes only so it is not taught), ‹ke› (to explain why it is not used).
- **Kata-Kata findings:** its c04 frames and scenario use «kopi», «ke», «durian», «kedai mamak», «nasi kandar» and «di sana» before their chapters (see the report).

## Step 5c: chapter 5 (12 Nov 2026, Claude)

- **One unit.** Unit 5 (13-unit plan), five blocks plus the 45-minute writing block (`ms-c05-writing-block`, registered as `ms-stage1-writing-5`). 63 core words are taught in six themed groups; the plan gives two routes (whole unit, or two halves) for the pilot to compare. Sam: more words are fine; I did not split.
- **Malay rules applied:** standard first («mahu», «tetapi», «bagaimana», «jingga») with «nak», «tapi», «macam mana», «oren» marked spoken; no comparatives («lebih», «paling», «daripada» are named only as ‹…› mentions in the teacher notes; «kurang manis» is the one fixed «kurang»); root verbs only; no word placed after chapter 5 («sangat», «sini», «kedai», «baju», «kerusi», «tolong», «hospital», «yang mana» are out of reach, so scenes were changed rather than the Malay).
- **Scenes:** a mamak order (model conversation, task, menu reading, writing), a Monday weekend talk (listening), a late arrival and feeling tired (patterns 4 and the short dialogues). The Kata-Kata scenario's «nasi lemak» and «sambal» are not in the ledger, so «mi goreng» and «roti canai» (Dunia recognition words) carry the scene. The clinic words are symptoms only.
- **Culture note:** the mamak stall and who traditionally runs it (Wikipedia, Rank 3), ordering a drink, colours and the flag (CIA World Factbook), hot and humid climate (Britannica; not checked against MetMalaysia), «nak» as spoken. Word notes come only from Kata-Kata card notes. No food rules or religious expressions.
- **Helper:** `chapter5_common.py` is `chapter4_common.py` with these differences: the timeline drill became a general "markers" drill, the test accepts 15 to 20 scored items (this unit has 19 plus the speaking task), the opener's Japanese scene list is separate (`dunia_list_ja`, now also used by 4A and 4B), and the unit ID is `ms-c05`. Use it as the starting point for chapter 6.
- **Mentions added** to `curriculum/malay-mentions.json`: ‹teh O›, ‹jambu›, ‹rumah sakit›, ‹lebih›, ‹paling›, ‹kurang›, ‹daripada›, each with its source. «mengapa» is on the root allow-list (`curriculum/malay-roots.json`).
- **Kata-Kata findings:** frame f03 uses «baju» (Ch8); the scenario uses «nasi lemak», «sambalnya» and «kedai mamak»; card ms-c05-008 «sedikit» is still a chapter 5 card; no cards or frame for «kenapa», «mengapa», «sebab», «kerana», «kuah», «kelakar»; the Dunia "Di klinik" card should say «hospital», not «rumah sakit» (details in the report).

## Step 5d: chapter 6 (12 Nov 2026, Claude)

- **One unit.** Unit 6 (13-unit plan), five blocks and no extra block. 32 core words in six themed groups; the teacher notes give the A/B cut if the pilot shows 32 is too many (comparing, equal and most first; very, too, choosing and describing words second).
- **Malay rules applied:** standard first («mudah», «tetapi») with «senang» and «tapi» marked spoken; whole ter- and se- words only («termurah», «terbesar», «terbaik», «tercantik», «setinggi», «semahal»; a test fails if a new one appears); «paling» + adjective and «sama … dengan» are the productive forms; «sekali» (very) goes after an adjective, «sangat»/«amat»/«terlalu» before it; root verbs only; no word from chapter 7 or later (no «dekat», «jauh», «ke», «kedai», «sini», «tengok»).
- **Scenes:** the condo choice (model conversation, task, listing, writing), the Monday talk (listening), the "Main badminton" Dunia scene for Block E (recognition only). The 14 Dunia words include body parts; they are labels, no injuries or advice.
- **Culture note:** «kondo», the Strata Management Act 2013 (secondary sources; scope Peninsular Malaysia and Labuan), the Klang Valley rail network (no lines or dates), Kata-Kata word notes. Sources are in the teacher key and the report.
- **Helper:** `chapter6_common.py` is `chapter5_common.py` with these differences: `GRAMMAR6`, «yang mana» in the question-word set, a single Dunia scene, "Markers with comparisons", the unit id `ms-c06`. Use it as the starting point for chapter 7.
- **Mentions added** to `curriculum/malay-mentions.json`: ‹ter› (Kata-Kata affix tag and card ms-c06-014 note), ‹dekat› and ‹jauh› (ledger, chapter 7); ‹se› gained cards ms-c06-005 and -006. E, F and G added as proper-noun condo labels.
- **Kata-Kata findings:** its scenario uses «dekat», «jauh» and LRT; frames f03 and f04 show open se- and ter- slots; card ms-c06-002 «kurang» has a "minus in telling time" note against Sam's 6 Nov decision; ledger L-0188 lacks "very" (details in the report).

## Step 5e: unit 6 follow-ups, review block, chapter 7 (12 Nov 2026, Claude)

- **Environment.** A fresh cloud container needs `apt-get update` before `apt-get install fonts-noto-cjk` (otherwise the package is not found), as well as `pip install pymupdf fonttools` and `git fetch --unshallow`. The Google Sheet and Doc connectors work from the session; `get_values` on the whole ledger is too large for the reply and is saved to a file, which can be turned into the CSV with the `csv` module (LF for `malay-ledger.csv`, CRLF for `ledger-snapshot.csv`; the earlier copies match byte for byte).
- **Unit 6 follow-ups.** 35 core words; rent is «setiap bulan» (not in the ledger: «sebulan»); fast pack swaps «susah», «cantik», «stesen» for «sewa», «bilik», «luas». `GLOSS` entries for L-1051 and L-1052 in `suite/__init__.py` keep the fast-pack word list marked (it prints the ledger meaning, which contains unmarked Malay). ‹menyewa› is a mention with its ledger source.
- **Review block.** `extra` in `suite/ms_c06.py` (`kind='review'` in `chapter6_common.py`); `catalogue.py` maps `review-6`.
- **Unit 7.** One unit, five blocks, no extra block. Teacher notes give the A/B cut (position, distance, direction and turning words first; landmarks, transport and compass points second). Duplicates: L-0592 is not core (duplicate of L-0330); L-0304 is not core (revision via L-0173 «depan»; «hadapan» is the formal form said in the entry).
- **Malay rules applied:** «ke» taught with the earlier forms as everyday speech; standard first; «jam» (traffic) and «tengok» labelled; no ber- or me- verbs; nothing placed after chapter 7; places of worship rotated evenly and tested; Japanese is a full translation.
- **Helper:** `chapter7_common.py` is `chapter6_common.py` with: `GRAMMAR7`, four more question words, "Markers with places and routes", three Dunia scenes, the opener's Sedia Kelas c07 text (27 cards), unit id `ms-c07`, genre "Wayfinding", prerequisites ms-c01 to ms-c06. Use it as the starting point for chapter 8.
- **Mentions added** to `curriculum/malay-mentions.json`: ‹menyewa› (ledger L-1051 note) and ‹bulat› (Kata-Kata card ms-c07-035). «internet» was added to the English homographs in `suite/__init__.py`.
- **Layout.** The pack-fit check can pass while the final PDF render fails on a dense page (a pattern page overflowed once). If `build.py` stops at `assert space>=0`, shorten the longest explanation on that page.
- **Legacy.** `course.py`: "Asking where", "Directions and orientation" in `RETIRED`; "Di, ke and dari" in `superseded` (removed from the bank, source in `build.py`). `tests/test_catalogue.py` lists the retired titles.
- **Kata-Kata findings.** Its scenario uses «tumpang tanya», LRT, Grab, Pavilion, KLCC and «tak» before «tidak»; ms-c07-036 is shared by L-0330 and L-0592; ms-c07-009 «depan» duplicates ms-c04-019; hospital and kapal terbang are chapter 7 cards placed in chapters 5 and 4; no cards exist for L-1051 to L-1058 (details in the report).

## Step 5f: unit 7 follow-ups and chapter 8 (12 Nov 2026, Claude)

- **Environment.** Same as step 5e: `pip install pymupdf fonttools`, `apt-get update` then `apt-get install fonts-noto-cjk`, `git fetch --unshallow`. The session branch was a harness branch; every commit was pushed with `git push origin HEAD:main` after `git fetch` and `git rebase origin/main`. No other branch was created.
- **Ledger workflow.** The five new rows were appended to the Ledger tab and four Journal rows to the Journal tab (the sheet first), then the whole tab was read (`get_values` saves it to a file because it is too large for the reply) and both copies rewritten with the `csv` module (LF for `malay-ledger.csv`, CRLF for `ledger-snapshot.csv`); the diff against the old copies was exactly the changed and new rows.
- **Unit 7 follow-ups.** See the report's part 1 table. `GLOSS` in `suite/__init__.py` has entries for L-1060 and L-1063 (their ledger meanings contain Malay). «kilometer» is an English homograph for the unmarked-Malay guard. The unit 7 test now expects 64 placed rows, 62 core and groups 13 / 11 / 11 / 23 / 4.
- **Chapter 8.** One unit, five blocks, no extra block (the Stage 1 plan gives none). `chapter8_common.py` is `chapter7_common.py` with: `GRAMMAR8`, «berapa» with a counter in the question words, "Markers with buying and counting", one Dunia scene ("Beli baju"), Sedia Kelas c08 (13 cards), unit id `ms-c08`, genre "Shopping and ordering", prerequisite unit ms-c07. Use it as the starting point for chapter 9.
- **Core rule for chapter 8:** a ledger row is core if its first chapter is 8 and it carries a chapter 8 card (35), recognition if it is a Dunia row that primes chapter 8 with no chapter 8 card (11); the 8 rows with a chapter 8 card placed earlier are revision (see the test `ch8_core` and `ch8_recognition`).
- **Revision words must be used** in the unit outside the vocabulary list (`test_revision_words_really_return`); add a word to a revision group only if a scene uses it.
- **Unmarked Malay in English prose** fails the build: mark «mamak», «roti canai», «ringgit», «sen» and similar in English text, or add an English homograph («pen», «tin», «batik», «kilometer» are on the list). Names in marked Malay (here «Rina») go in `curriculum/malay-proper-nouns.json`; Malay words quoted but not taught (‹nasi lemak›, ‹penjodoh bilangan›, ‹sebatang›, ‹sehelai›) go in `curriculum/malay-mentions.json` with a source.
- **Legacy.** Chapter 8 had no legacy packs, so nothing was retired; legacy exceptions stay at 30. `tests/test_language_checks.py` now uses ms-c09 as its "not yet re-authored" unit.
- **Kata-Kata findings** (details in the report): card ms-c07-024 and its frame teach «jalan lurus»; the chapter 8 scenario and frame f05 use «nasi lemak»; frames f02 and f04 teach productive ‹se-›; cards ms-c08-001, -003, -010 give counter senses the ledger does not; no cards yet for L-1059 to L-1063.

## Step 5g: unit 8 follow-ups and chapter 9 (12 Nov 2026, Claude)

- **Environment.** Same as steps 5e and 5f: `pip install pymupdf fonttools`, `apt-get update` then `apt-get install fonts-noto-cjk`, `git fetch --unshallow`. Every commit was fetched, rebased on `origin/main` and pushed with `git push origin HEAD:main`; the session branch was pushed to the same commit (`git push origin HEAD:refs/heads/claude/serene-feynman-3x1cq2`). The Wikipedia host did not resolve from the session (the web-fetch tool gets `ENOTFOUND`); web search worked. I did not change network settings.
- **Ledger workflow.** New rows were appended to the Ledger tab and the Journal tab first (the sheet), then the whole Ledger tab was read (`get_values` saves it to a file; use the `csv` module: LF for `malay-ledger.csv`, CRLF for `ledger-snapshot.csv`), both copies rewritten, and the hash and row count in `docs/step4-sources.json` updated. The old copies regenerate byte for byte from their own rows, so the diff is exactly the changed and new rows.
- **Unit 8 follow-ups.** `suite/ms_c08.py` now has `SE` (the «se-» form of every counter, appended to each counter entry), the `GERAI` group, a «gerai» listening and price board, and register labels. `GLOSS` in `suite/__init__.py` has entries for L-1064 and L-1066 to L-1069 (the fast pack word list prints the ledger meaning, which contains Malay). Bare «se-» is not a ledger word, so it is written as the mention ‹se-›.
- **Chapter 9.** One unit, five blocks, no extra block. `chapter9_common.py` is `chapter8_common.py` with: `GRAMMAR9`, «siapa» with «oleh» in the question words, "Markers with passive verbs", two Dunia scenes, Sedia Kelas c09 (12 cards), unit id `ms-c09`, genre "Social life", and the second Culture note (`culture-open-houses`, `festival_notes` in the config). Use it as the starting point for anything that follows.
- **Core rule for chapter 9:** a ledger row is core if its first chapter is 9 and it carries a chapter 9 card (29); recognition if it is a Dunia row that primes chapter 9 with no chapter 9 card (33, including Sam's six festival words, whose place says "Dunia · Rumah terbuka (primes Ch9; pending)"). «pinggan» (L-0355) carries a chapter 9 card but was placed in chapter 8: revision.
- **Mentions added** to `curriculum/malay-mentions.json`: ‹di›, ‹buat›, ‹panggil›, ‹cuci›, ‹larang›, ‹jamu›, ‹an›, ‹me›, ‹ber›, each with its source. Names go in `curriculum/malay-proper-nouns.json` (+Dayak). The Dunia scene titles "Rumah terbuka Hari Raya", "Rumah terbuka" and "Simpulan bahasa harian" are product names in `suite/__init__.py`.
- **Tests.** `tests/test_language_checks.py` now uses ms-c10 as its "not yet re-authored" unit. `tests/test_step5g_suite.py` has 17 tests (partition, revision, components, patterns, the «di-» rule, idioms never drilled, drills and question words, markers, scenes, festival notes and sources, Japanese, plan, Malay rules, registration, fast pack).
- **Kata-Kata findings** (details in the report): the scene must become a general "Rumah terbuka" with cards for L-1070 to L-1075; the scenario uses «durian», «jom kemas», «tak ada» and a non-ledger «cuci»; frame f06 has no card; card ms-c09-028 duplicates ms-c08-016; cards are still missing for L-1032 to L-1075.

## Step 5h: the Stage 1 close (12 Nov 2026, Claude)

- **Environment.** Same as steps 5e to 5g (`pip install pymupdf fonttools`, `apt-get update` then `apt-get install fonts-noto-cjk`, `git fetch --unshallow`). The Google Sheets and Docs connectors worked; web search worked. The worker restarted once mid-session without losing work.
- **Ledger workflow.** As in step 5g: read the whole Ledger tab with `get_values` (saved to a file), rewrite both copies with the `csv` module (LF and CRLF), update the hash in `docs/step4-sources.json`; the diff is exactly the changed and new rows.
- **How the stage unit works.** `suite/stage1.UNIT` has `stage='stage1'` and no label, so `course.py` lists its components with chapter 9 (after the unit and the fast pack) instead of treating it as a fast pack; `catalogue.py` places them from `stage_items`. `chapter_id` is `ms-c09`, so the language checks allow words placed in chapters 1 to 9 only. Test-item IDs are `ms-stage1-test-{a,b}-{section}-NN`; `stage1.item_ids()` reproduces them for the catalogue's item map.
- **Writing new Malay for the stage close:** check every «…» span first with `Ledger().checker.inspect` at chapter 9 (as `test_only_ledger_words_from_chapters_1_to_9` does); words not in the ledger were avoided and are proposed in the report.
- **Kata-Kata:** `docs/kata-kata-cleanup.md` replaces the scattered Kata-Kata lists; a test fails if a ledger row whose action names Kata-Kata is missing from it.

## Step 5i: Stage 1 follow-ups (12 Nov 2026, Claude)

- **Environment.** As in steps 5e to 5h: `pip install pymupdf fonttools`, `apt-get update` then `apt-get install fonts-noto-cjk`, `git fetch --unshallow`. The Sheets connector's `get_values` for the whole ledger is saved to a file; write both copies with the `csv` module (LF and CRLF) and check first that the old copies regenerate byte for byte. `main` moved twice during the session (only `docs/stage-2-plan.md`); each push was fetched, rebased and re-tested. The session branch was force-pushed to the main commit after the rebase.
- **Core rule for new chapter 9 rows:** a ledger row placed exactly "Ch9 (pending)" is core in unit 9 (`ch9_core` in `tests/test_step5g_suite.py` recomputes the 42 from the ledger).
- **Adding a test item without changing the 20 marks:** a listening item may be flagged `compulsory='comparison'` in the version data; `suite/stage1.compulsory_codes` and the administration sheet's item map pick it up. Remember the unit tests expect 10 listening items and four speaking cards.
- **Reading section words:** «TOLAK», «TARIK», «PERHATIAN:», «hingga» and the festival greeting are in both versions' reading texts (`tests.StageTest.test_signs_and_notices_in_the_reading_paper`). English prose that names a Malay proper noun or festival must mark it («Gerai Siti», «Kaamatan»), or the build stops.

## Next: Sam's pilot, then the projects below (each needs Sam's go-ahead)

1. **Sam's answers** to the questions at the end of `docs/STEP-5i-report.md` and his pilot of Stage 1 (timings, load, the review blocks, the stage review, one version of the A1 test).
2. **The Kata-Kata clean-up session** (Claude Code, in the Kata-Kata repository). Brief: `docs/kata-kata-cleanup.md`. Afterwards refresh `curriculum/reference/katakata/c01.json` to `c09.json` and the ledger card-ID column.
3. **The Kamus Dewan check** of every ledger row marked "Not yet checked" (at least L-0983 to L-1088).
4. **The Japanese native review** of all Japanese in Cikgu Sensai (every sheet is marked draft).
5. **Stage 2 (chapters 10 to 18, A2):** Sam has decided Claude builds it. The plan is audited; next is Sam's answers to `docs/stage-2-decisions.md`, then the build order in section 6 of `docs/stage-2-plan.md`.

## Earlier: Sam's pilot of chapter 3

Sam approved Step 5a publication to main once checks pass. Do not revisit word load, the three-unit split, recognition-only Dunia items or retirement of the superseded chapter 3 packs. Collect chapter 3 pilot feedback on unit timings, drills, fictional numerical practice and the fast pack. (Chapter 4 was later authorised without waiting for this feedback; see step 5b.)

### Current builder notes for Step 5a

The authored source is in suite/chapter3_common.py, suite/ms_c03a.py, suite/ms_c03b.py, suite/ms_c03c.py and suite/fast.py. The three vocabulary groups are separate and test-new-vocabulary only draws from core entries. The 3A review block and 3C writing block are registered in the catalogue.

The GitHub Actions Step-5a verify workflow on the recovery branch builds with the full history and runs the entire test suite; successful runs commit generated dist assets and the authored scope to the branch. Verify that the *final* commit is pushed to main and confirm Cloudflare deployment from the hosting pipeline. No build should be promoted without successful checks.

## Legacy notes: Sam's review of the original step 4 pilot

Feedback to collect: timings per block, vocabulary load (core words: unit 1 44, 2A 35, 2B 37; recognition and hobby words listed separately), drill difficulty, and whether the fast packs fit one 45-minute session. After that, freeze the template and start step 5 (chapters 3 to 9).

## Decided after step 4 (11 Nov 2026)

- **No faith-specific greetings.** Sam: Assalamualaikum and Waalaikumsalam are not taught anywhere (charter section 8; ledger Rules tab). Ledger L-0009 is Retired. Both were removed from unit 1 (vocabulary, culture note, pronunciation list, teaching plan, culture-note key) and from `curriculum/malay-mentions.json`; Waalaikumsalam is not added to the ledger. Rebuilt; 31 tests pass. Ask Sam before adding any other faith-specific expression.
- **Languages in chapter 2.** Sam agreed that learners say «Saya boleh cakap bahasa Melayu sedikit.» in chapter 2. Ledger: new rows L-1016 «bahasa», L-1017 «Melayu», L-1018 «Inggeris»; L-0216 «sedikit» moved from Ch5 to Ch2 (reused in Ch5); L-0473 «cakap» placed in Ch2. The spoken «sikit je» (L-0948) is now allowed and is taught in unit 2A as a chat word. «Melayu» and «Inggeris» are listed as proper nouns, so the affix check does not read «Melayu» as me- + ‹layu›.
- **Hobby word bank (chapter 2).** Sam's list: karaoke, golf, cafe hopping, travelling, hiking, oshikatsu, plus muzik, filem, sukan, lagu, masak and badminton. Ledger L-1019 to L-1031, and L-0968 «badminton» placed in Ch2. Malaysian forms («muzik», «filem», «sukan», «kafe», not the Indonesian ‹musik›, ‹film›, ‹olahraga›). «travelling» and «hiking» use «jalan-jalan» and the spoken loans «travel» and «hiking»: ‹melancong› and ‹mendaki› are me- verbs and wait for chapter 11. In unit 2B the bank is a separate vocabulary group: each learner keeps the words that are true for them, and only those are tested.
- **Vocabulary parity (Sam: "ease some of the excess 52 words … and have parity").** Unit 1 already carries 44 words, so nothing more moves into chapter 1; the balance is between 2A and 2B. «dengan» moved from 2B to 2A (example «Saya cakap bahasa Melayu dengan kawan saya.»). Each unit now separates core words from recognition words:
  - unit 1: 44 core;
  - unit 2A: 35 core, plus 12 chat words from "Sembang di pantri" to recognise;
  - unit 2B: 37 core, plus 14 office words from "Pagi di pejabat" to recognise and the 14-word hobby bank.
  Unit 2A also gained drill items (substitution 9 and 10, question and answer 9 and 10) and two model-conversation turns (now 16) for the language sentence; unit 2B gained a hobby example in pattern 3 and substitution items 11 and 12. The chapter 2 fast pack shows both sentences.
- **Etymology notes come from Kata-Kata only for now** (Sam). Do not write new etymology into Cikgu Sensai; quote Kata-Kata card notes and mark roots with ‹…›.
- **Ledger copies refreshed** (both `curriculum/reference/katakata/malay-ledger.csv` and `docs/handoff/ledger-snapshot.csv`, now L-0001 to L-1031); new hash pinned in `docs/step4-sources.json`. Journal rows 43 to 49.

## Open questions for Sam

- **Unverified items to confirm:** the pronunciation notes (unit 1), the name-customs paragraph (unit 2A culture note), and every "Japanese helps or misleads" note.
- **Still open from before:** which textbooks the other Japanese teachers use, and the explainer language for Japanese packs. The Kamus Dewan check for L-0983 to L-1031 has still not been run (L-1031 «oshikatsu» will not be in Kamus Dewan; it is kept as a fans' loanword).

## Other repositories

**The full, current list is `docs/kata-kata-cleanup.md` (step 5h); it supersedes the notes below, which are kept for history.**

Kata-Kata (Claude Code) still needs the same ledger changes: new cards for L-0983 to L-1031, saya and the time words moved to chapter 1, Ch2 cards for «sedikit», «cakap» and «badminton», and card ms-c01-009 (Assalamualaikum, L-0009) removed. Tracked in the ledger Journal as pending.

Step 4 findings for Kata-Kata:
- The chapter 2 scenario uses «dari mana» (ledger chapter 7) and «badminton» (chapter 6) at chapter 2.
- Chapter 1 still has no Dunia scene; Block E of unit 1 uses the chapter 1 scenario instead.
