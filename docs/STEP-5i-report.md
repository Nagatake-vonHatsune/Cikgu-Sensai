# STEP 5i REPORT: Stage 1 follow-ups, Batch 9

**Scope:** Sam's answers to the step 5h questions (12 Nov 2026): the pass mark, the two extra test blocks, the `writing` sub-type,
a compulsory chapter 6 comparison item, five new chapter 9 ledger rows and the sourced «Selamat Pesta Kaamatan». Sam authorised the
batch and pre-approved publication to main when the checks pass. Stage 2 is not started.

**Sources read:** `AGENTS.md`, `HANDOFF.md`, `docs/STEP-5h-report.md`, `suite/stage1.py`, both test data files, `suite/ms_c09.py`,
the unit 9 and stage tests; the ledger (Ledger!A1:T1089) and Journal rows 84 to 89 from the Google Sheet. The new ledger rows and the
Journal rows were written to the sheet before this session.

**Status:** draft for Sam's pilot. `python3 build.py` and `python3 -m unittest discover -s tests` (153 tests) pass on a full Git
checkout at both commits. Each commit was fetched and rebased on `origin/main` (only `docs/stage-2-plan.md` had moved) and pushed to
`main`; the session branch `claude/nifty-edison-3lz6o9` is at the same commit.

| Commit | Content |
| --- | --- |
| `a52c6a0` | Ledger copies and hash (L-0001 to L-1088); unit 9 with 42 core words; «Selamat Pesta Kaamatan» sourced |
| `55db51d` | A1 test: compulsory comparison item and card 2, signs and notices in the reading paper, pass mark and blocks |
| next commit | This report and `HANDOFF.md` |

## Sam's answers and what I did

| # | Sam's answer | What changed |
| --- | --- | --- |
| 1 | Pass mark 48 of 80, at least 10 of 20 per section | Recorded as "Sam's decision of 12 Nov 2026" in the administration sheet (scoring text and key) and in the catalogue's Stage 1 record (`pass_rule.status`). The old "proposal for Sam" wording is gone and a test checks it |
| 2 | Two extra 45-minute blocks (papers, then speaking); charter says 76 blocks, about 57.5 hours | The administration sheet's Timing now says block 1 is the written papers (12 + 15 + 18 = 45 minutes) and block 2 is speaking, and that the plan is 76 blocks. `catalogue.py` `hour_budget.class_blocks` 74 → 76. No other block or hour count exists in the repo (the fast and full course summaries carry only self-study planning figures, which are unchanged). **See question 1 below about 57.5** |
| 3 | `writing` accepted as a test item type | Noted in `HANDOFF.md` as a charter decision and in `docs/DATA-MODEL.md`. No code change |
| 4 | One compulsory comparison item in both versions; make the chapter 6 card compulsory or replace it | See below |
| 5 | Ledger rows L-1084 to L-1088 (chapter 9), as core; use them naturally | See below |
| 6 | «Selamat Pesta Kaamatan» sourced | See below |

### 4. The compulsory comparison item

- **New item, listening L5 in both versions (2 marks, chapter 6 only).** A: two colleagues choose between «Gerai Siti» and «Gerai
  Kumar» (the learner hears «lebih dekat daripada» and «paling sedap» and notes the closer stall and the tastiest dish). B: two
  colleagues choose how to get to the bank (the learner hears «lebih cepat daripada» and «paling murah»). Each key gives both facts;
  the key marks the item "Compulsory comparison item". Every learner sits the whole listening paper, so the item cannot be skipped.
- **Sections stay at 20 marks (4 × 20 = 80, which is what the pass mark assumes).** To make room, the weakest listening item (the
  third question of the "meeting a colleague / neighbour" task, morning or afternoon plus a home or hobby fact) was removed in both
  versions. The listening paper is now five tasks and ten items. Chapter 1 and 2 coverage is unchanged in effect (each is still
  tested by four to five items).
- **Speaking card 2 is now compulsory (the choice I made, and why).** I made the chapter 6 card compulsory and did not replace
  it with the new item. The new item is listening, which is receptive; card 2 («Buying fruit» in A, «Buying a shirt» in B) is the
  only place a learner has to *produce* «lebih … daripada» or «terlalu» / «lebih». If it had stayed optional, a learner could
  reach A1 without ever saying a comparison. The examiner now always uses card 2 and picks the second card from cards 1, 3
  and 4, and should vary it from learner to learner. The speaking sheet, the key, the administration sheet ("Running the test") and
  the card title ("always used") all say so. Marks and timing are unchanged (8 + 6 + 6).
- **Chapter 6 is now tested in three places in each version:** L5, R4 and S2.2 (see the mapping below). The item map in the
  administration sheet marks L5 and S2.2 as "compulsory (chapter 6)", and the catalogue record lists them under
  `stage_test.compulsory_items` (A: A-L5, A-S2.2; B: B-L5, B-S2.2).

**Item-to-chapter map after the change** (the administration sheet generates it from the data, so it always matches the papers):

| Ch | Version A | Version B |
| --- | --- | --- |
| 1 | L3, R8, W2, S1, S2.3 | L3, R8, W2, S1 |
| 2 | L3, L4, W1, S1 | L3, L4, W1, S1 |
| 3 | L1, L8, R3, R5, R7, W1, S2.1 to S2.3 | L1, L8, L9, L10, R3, R5, W1, S2.1, S2.2 |
| 4 | L1, L2, L10, R6, R9, W1, W2, S1, S2.4 | L1, L2, R6, R9, W1, W2, S1, S2.3, S2.4 |
| 5 | L7, S1, S2.1, S2.4 | L7, S1, S2.1, S2.2 |
| 6 | **L5**, R4, **S2.2** | **L5**, R4, **S2.2** |
| 7 | L2, L9, L10, R1, R6, R7, W2, S2.3 | L2, L9, L10, R1, R6, R7, S2.3 |
| 8 | L6, L7, R3, W2, S2.1, S2.2 | L6, L7, R3, R5, R7, W2, S2.1, S2.2 |
| 9 | L1, R2, R8, R9, R10, S2.4 | L1, R2, R8, R9, R10, W2, S2.4 |

### 5. The five new rows (L-1084 to L-1088, chapter 9 pending)

- **Ledger.** Both copies and the hash were regenerated from Ledger!A1:T1089 (the old copies regenerated byte for byte first; the
  diff is the changed L-1074 note and the five new rows). Hash `f96f3725…8355`; `docs/step4-sources.json` updated. The ledger has
  1,088 rows; 76 live rows are placed in chapter 9.
- **Unit 9: 42 core words in six groups** (18 / 4 / 4 / 9 / 5 / 2). «perhatian», «hingga», «tolak», «tarik» join "Signs and
  notices" (5 → 9); «pesta» joins "A party and an open house" (4 → 5). 33 recognition and 74 revision words are unchanged.
- **Where they are used, naturally (outside the vocabulary list):**
  - door signs «TOLAK» / «TARIK»: pattern 5 («Pintu ini tolak atau tarik?» «Tarik, bukan tolak.»), the notice board (lobby door and
    meeting-room door), two reading questions and a culture note sentence;
  - a «PERHATIAN» notice: the notice board («PERHATIAN: Bilik mesyuarat ditutup hingga hari Isnin.»), the writing task and model, the
    test reading passage and the pattern 5 dialogue;
  - «Ditutup hingga …» and «Dibuka Isnin hingga Jumaat»: pattern 5, the notice board, the test reading question («Until when is the
    office closed?»). «hingga» is labelled as the written word and «sampai» (L-0203, chapter 4) as the everyday one, on the pattern
    page, in the vocabulary gloss and in the teacher notes;
  - «Selamat Pesta Kaamatan»: the festival note's greetings line, the vocabulary glosses for «pesta» and «Kaamatan», the example for
    L-1084.
- **A1 test, reading section.** Version A: signs C «TOLAK» and D «TARIK» (R2 asks which door you pull), a «PERHATIAN: Klinik ditutup
  hingga hari Rabu» clinic notice with «dari pukul … hingga pukul …» (R9), and a WhatsApp message that opens «Selamat Pesta Kaamatan!»
  (R8 asks the time of day and the festival). Version B: signs E «TOLAK» and G «TARIK» (R2 asks which door you push), a «PERHATIAN: Bank
  ditutup hingga hari Isnin» notice (R9), and «Selamat Hari Gawai» in the message (R8). B uses the Gawai greeting so the two
  versions stay different in facts; both greetings are on Sam's list.
- **Not used:** no word is built from «perhatian» (the teacher notes say so and a test checks it). «tarik» also sits inside «teh tarik»
  and «tarik duit» (chapters 3 and 5); the Kata-Kata card note for L-1088 says so in `docs/kata-kata-cleanup.md`.
- **Kata-Kata list.** `docs/kata-kata-cleanup.md` now has the five rows (112 new cards in all; the completeness test now expects the
  121 rows whose ledger action names Kata-Kata).

### 6. «Selamat Pesta Kaamatan» is sourced

"Not yet sourced" is removed everywhere. The festival note now reads: «Selamat Pesta Kaamatan» (Bernama, 30 May 2026), with the fuller
formal greeting shown only as the quotation ‹Selamat Menyambut Pesta Kaamatan› (it contains a ‹me-› verb). `curriculum/malay-mentions.json`
swaps the old mention for ‹selamat menyambut pesta kaamatan›, with the Journal row 87 source. The Japanese is a draft.

**What I checked this session:** a web search returned Bernama's 30 May 2026 report, in which the Communications Minister's message
ends «Selamat Pesta Kaamatan dan Hari Gawai kepada semua yang meraikannya», and an RTM headline with "selamat menyambut Pesta Kaamatan
dan Hari Gawai". This is from search summaries; I did not open the Bernama or RTM pages (they are in the source note as such).

## Verification status

- **Verified in this batch:** the ledger rows against the sheet (cell for cell, both copies); the Bernama and RTM wording (search
  summaries only, above); all Malay in the unit and test passes the ledger, register, affix and Malaysian-form checks at chapter 9.
- **[UNVERIFIED]:** all new Malay is mine and has had no native read. Please look at: «Pintu ini tolak atau tarik?» «Tarik, bukan
  tolak.»; «Kedai itu dibuka bila?» «Ditutup hingga hari Isnin. Perhatian di pintu.»; «PERHATIAN: Bilik mesyuarat ditutup hingga hari
  Isnin.»; «Klinik dibuka dari pukul lapan pagi hingga pukul sepuluh malam.»; «Tetapi nasi lemak di Gerai Kumar paling sedap.»;
  «Teksi lebih cepat daripada bas.»; «Tetapi jalan kaki paling murah. Bank dekat.»; «Selamat pagi, Encik Tanaka, dan Selamat Pesta
  Kaamatan!» (a colleague greeting a non-Sabahan on the day is my guess at natural usage).
- **Register of «hingga»:** "formal on notices, «sampai» everyday" is Sam's note on L-1086; the Kamus Dewan check is still pending
  (now L-0983 to L-1088).
- **Unchanged:** the Gawai and Kaamatan dates and the other festival facts are as in steps 5g and 5h.
- **Japanese:** all new Japanese is a draft for native review.

## Questions for Sam

1. **Hours.** 76 blocks of 45 minutes is 57.0 hours, not 57.5 (the charter table's own rows add up to 48.75 + 3 + 3.75 = 55.5 hours
   for 74 blocks, plus 1.5 for the two test blocks = 57.0). The charter text and `docs/handoff/charter-snapshot.md` say "about 57.5".
   I wrote only "76 blocks" in the repo and left the hours to the charter. Which figure do you want: 57 or 57.5?
2. **Listening item removed.** To keep every section at 20 marks I removed one listening item per version (third question of the
   introductions task). If you would rather keep it and make listening 22 marks or move 2 marks from another item, say so.
3. **Card 2 compulsory.** Do you agree with making the comparison card compulsory (rather than replacing it with the listening item)?
   It means the second card now has three choices (1, 3, 4) instead of two.
4. **Kamus Dewan.** The KD4 check for «pesta», «perhatian», «hingga», «tolak», «tarik» is still to run (Journal row 88).
5. **Kaamatan greeting in the test.** Is it acceptable that version A's WhatsApp message greets with «Selamat Pesta Kaamatan» and
   version B's with «Selamat Hari Gawai» (the Kaamatan and Gawai dates are 30 and 31 May and 1 June)?

Stage 2 (chapters 10 to 18) is not started and waits for your go-ahead.
