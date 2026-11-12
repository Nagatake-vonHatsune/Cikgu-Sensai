# STEP 5h REPORT: Stage 1 close, Batch 8

**Scope:** (1) the unit 9 follow-ups Sam agreed on 12 Nov 2026 (eight new chapter 9 ledger rows and the festival notes);
(2) the Stage 1 review block (45 minutes, after unit 9); (3) the A1 stage test in two parallel versions, with keys,
listening scripts, an administration sheet and a CEFR record in the catalogue; (4) `docs/kata-kata-cleanup.md`, one
consolidated brief for a separate Kata-Kata session. Sam authorised the batch on 12 Nov 2026 and pre-approved publication to
main when the checks pass. **With this batch Stage 1 (chapters 1 to 9) is complete and awaits Sam's pilot.**

**Sources read:** `AGENTS.md`; `HANDOFF.md` in full, including "Quality rules for chapter 4 onward"; the charter (the live
Google Doc was read through the Docs connector; its sections 3, 4, 6, 7, 8 and 10 match `docs/handoff/charter-snapshot.md`);
the review blocks after 3A, 4B and 6, the unit tests of units 1 to 9, `suite/ms_c09.py` and `docs/STEP-5g-report.md`; the
ledger (the whole Ledger tab, A1:T1084, and Journal rows 80 to 86, read from the Google Sheet); the Kata-Kata frames
`c01.json` to `c09.json`; the "Findings for Kata-Kata" sections of every step report.

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests`
(149 tests at the end; 131 after Part 1) pass on a full Git checkout at every commit below. Each commit was fetched and rebased on `origin/main`
(nothing else had landed), pushed to `main`, and the session branch `claude/stage-1-final-batch-7e9zv2` was pushed to the
same commit. The session's worker restarted once during Part 4; the tree was clean at `0e46450` and work resumed from there.

| Commit | Content |
| --- | --- |
| `ec3a8f1` | Part 1: ledger copies and hash regenerated (L-0001 to L-1083); unit 9 with 37 core words; festival notes corrected |
| `3a567c3` | Part 2: the stage review block (`suite/stage1.py`, unit `ms-stage1`), registration, `tests/test_step5h_stage1.py` |
| `9c22b46` | Part 3: A1 stage test, version A (four section papers), `writing` test-item sub-type |
| `0e46450` | Part 3: version B, listening scripts sheet, administration sheet, the catalogue's Stage 1 record |
| `9beefa7` | Part 4: `docs/kata-kata-cleanup.md` and a completeness test |
| next commit | This report and `HANDOFF.md` |

## What was built

### Part 1: unit 9 follow-ups

| Sam's decision (12 Nov 2026) | What I did |
| --- | --- |
| Regenerate both ledger copies and the hash from the sheet (rows to L-1083; Journal rows 83 to 86 written by Claude) | Read Ledger!A1:T1084; both copies rewritten with the `csv` module (LF and CRLF). The diff against the old copies is exactly 3 changed rows (L-1064 Japanese ナシレマ; L-1070 «Tahun Baru Cina / Tahun Baharu Cina» with Sam's note; L-1074 note) and 8 new rows. Hash and row count updated in `docs/step4-sources.json` |
| New chapter 9 rows L-1076 to L-1083: «buat», «panggil», «cuci», «larang» (roots for the «di-» rule); «tuan rumah», «mari»; «ibu», «adik» | All eight are core in unit 9: **37 core words in six groups** («di-» verbs 18; roots 4; «oleh», «pada», «tadi», «siap» 4; signs 5; a party and an open house 4; family 2). The roots now appear as Malay (vocabulary roots, pattern 1, culture note, «Saya cuci pinggan»), the transformation drill gains items 11 and 12 («Ibu saya buat kuih ini.» → «Kuih ini dibuat oleh ibu saya.»; «Puan Aini panggil Encik Tanaka.»), the test gains G4 (20 scored items), «Mari makan» is in the model conversation and the festival notes («Jom makan» labelled spoken), «ibu» is in the variant, «adik» in the vocabulary example, «tuan rumah» in the festival notes and the Block E role-play. The four ‹buat› etc. mentions were removed from `curriculum/malay-mentions.json` |
| Kaamatan: Sabah and Labuan, 30 and 31 May | In the note, the vocabulary gloss and the key |
| Teach «Tahun Baru Cina» (everyday) and «Tahun Baharu Cina» (official) | Both in the note and the gloss; the ledger row now carries both forms |
| Greetings, including «Selamat Tahun Baru Cina» (no «Hari») and «Selamat Pesta Kaamatan» (from usage, not yet sourced) | All six in the festival intro. «pesta» is not a ledger word, so «Selamat Pesta Kaamatan» is shown as a quoted form ‹Selamat Pesta Kaamatan›, labelled "from usage; not yet sourced", with the ledger row L-1074 as its mention source. A test fails on «Selamat Hari Tahun …» or «Selamat Hari Kaamatan» |
| Keep the one general Christmas sentence | Kept; a test checks it is one sentence |
| Gawai gazetted 25 Sept 1964, first celebrated 1 June 1965 (Borneo Post, New Straits Times) | In the note, with the sources in the key |
| «angpau» is the Malay spelling; «Krismas» and «Deepavali» stand | The note and the gloss say English-language papers often write "ang pow" |
| No explicit ‹se-› checker rule | None added |

Unit 9 now has 37 core, 33 recognition and 74 revision entries (144 in the vocabulary list); the ledger copy places 71 live
rows in chapter 9 (37 + 33 + «pinggan» carried from chapter 8). The festival note is 256 English words (limit 300).

### Part 2: the Stage 1 review block (`ms-stage1-review`, 45 minutes, after unit 9)

One integrated, fictional scenario: **Encik Kimura's first week in Kuala Lumpur.** Monday: greetings, introductions and a
staff form (chapters 1 to 3); Tuesday: lunch at a «gerai», choosing, comparing, ordering with counters and paying (3, 5, 6,
8); Wednesday: the meeting day (4); Thursday: the way to the bank (7); Friday: the office «jamuan», a notice and taking leave
(9, 1). Timing: recall 5 (one prompt per chapter), model in six scenes 10, role cards with a change of plan 15 (the
meeting moves from ten to two), a notice board with six questions and a message to write 10, and the can-do self-check 5.

- **Spaced return (charter rule 7):** all 54 Kata-Kata frames of chapters 1 to 9 come back in the block; the key lists the
  line for each, and a test checks every one. ms-c07-f03 is said «Jalan terus, kemudian belok kiri …» (Sam's correction).
  «Ketinggian dua meter» and «diskaun sepuluh peratus» appear as written labels on the notice board, as in unit 3C.
- **Can-do self-check:** every charter Stage 1 goal (section 4), split into 21 "I can" ticks with Japanese.
- **Registration:** listed with chapter 9 after unit 9 (`stage_items` in `dist/chapters.js`), catalogued as the additional
  block `ms-stage1-review` (status "pilot draft"), with all 54 frame IDs as its pattern tags.

### Part 3: the A1 stage test

A summative test for Stage 1 in the Irodori / JF Standard style: every item is a task with a real outcome (understand an
announcement, act on a sign, find a price, fill in a form, write a message that arranges a meeting, order, buy, ask the way).

| Section | Version A (fictional content) | Marks | Time |
| --- | --- | ---: | ---: |
| Listening | 4 tasks, 10 items: a shop and an office announcement; a first meeting; ordering at a «gerai»; directions on the phone | 20 | 12 min |
| Reading | 4 parts, 10 items: six signs; a price board; a WhatsApp message; a clinic notice with «Dilarang» | 20 | 15 min |
| Writing | a ten-field form (with an optional persona card); a five-to-seven-sentence message, rubric 4 + 4 + 2 | 20 | 18 min |
| Speaking | self-introduction with two follow-ups (8); two of four role-play cards with a change of plan (6 each) | 20 | about 7 min each |

Version B is parallel (same sections, item codes, marks and chapter spread; a bookshop, a condo neighbour, a breakfast order,
a «kedai mamak», a fruit stall, a party invitation, a bank notice, a staff form, a late-for-the-party message, and cards for
a «kedai mamak», buying a shirt, arranging to meet and a Monday at the office). Use A for the main sitting and B for a
second group or a re-sit.

- **Pass mark (a proposal for Sam):** 48 of 80 (60 per cent) and at least 10 of 20 in every section. A pass is recorded as
  "Malay A1 · Stage 1 complete". The figure is mine; it is not taken from a JF or CEFR document.
- **Keys:** item by item. Listening and reading: one mark per fact, each fact named. Writing and speaking: a rubric per item
  (content, language, accuracy or interaction), a model answer and the examiner's lines. A test checks that the marks in
  every rubric add up and that every quoted Malay answer is in its script.
- **Teacher sheets:** "Listening scripts (teacher)" for both versions, and an "Administration sheet": purpose, timing,
  materials, procedure, scoring and the pass mark, the item maps (each item's marks and chapters; each chapter's can-do goal
  with its items), and a paper result sheet. Cikgu Sensai keeps no learner records.
- **Components:** 11 in unit `ms-stage1`, all draft: the review, 8 section papers (`ms-stage1-test-a-listening` … `-b-speaking`),
  the scripts and the administration sheet; 54 tagged test items (27 per version). They print through the normal PDF system (the papers are
  6 to 7 pages each including the explainer and key pages).
- **Contract change:** `catalogue.py` now accepts the test-item sub-type `writing`, used only by the stage test (the charter's
  tag table lists words, grammar, listening, reading and speaking). `docs/DATA-MODEL.md` says so. **Sam to confirm.**

### The CEFR label for the Evaluator

The charter's roadmap (section 10, phase 3) wants a "CEFR label shown in the Evaluator" in Hanashishou. The catalogue already
carries CEFR data as `level` on every chapter and component. I added, next to the chapters, a **`stages` list with one
record, `ms-stage1`**: `cefr: "A1"`, the nine chapter IDs, the review block, the test versions and teacher sheets, the
section marks, the pass rule (marked "proposal for Sam"), a map from every test-item ID to its chapters, and
`completion: {flag: "stage1_complete", label: "Malay A1 · Stage 1 complete", cefr: "A1", rule: …}`. Every chapter record
also gains `stage_id: "ms-stage1"`. The record is a definition only: Cikgu Sensai stores no learner results, so Hanashishou
(or a teacher) sets the flag; the Evaluator can then show "A1" beside a learner who has completed Stage 1, before
Hanashishou's band 1 (Foundation), which the charter maps to A2. Nothing was built in Hanashishou.

### Part 4: the Kata-Kata clean-up list

`docs/kata-kata-cleanup.md` merges the "Findings for Kata-Kata" of steps 4 to 5g, the Kata-Kata notes in `HANDOFF.md`, the
step 5h findings and the 116 ledger rows whose open action names Kata-Kata, deduplicated and grouped by chapter and by type:
107 new cards with ledger IDs; moved cards (saya and the four time-of-day words to Ch1, sedikit to Ch2); the card to remove
(ms-c01-009 Assalamualaikum) and the retired duplicate (L-0592 → one card for L-0330); notes and frames to correct
(ms-c07-024 and ms-c07-f03 «jalan lurus» → «jalan terus»; the «kurang suku» note on ms-c06-002; the open ‹se-› and ‹ter-›
slots in the chapter 6 frames; the counter senses of ms-c08-001, -003 and -010; register notes); scenes to rename or change
(the general «Rumah terbuka» scene with Sam's festival decisions, the chapter 2, 4, 5, 6, 7 and 9 scenarios that use later
words, and the missing chapter 1 Dunia scene); and the Hanashishou mapping L-0592 → L-0330. Findings Sam has since overruled
(‹se-› with every counter in chapter 8) are marked closed. A test keeps the list complete against the ledger.

## Can-do coverage: each chapter's goals → review and test items

| Ch | Charter goal | Stage review (day, frames) | Test version A | Test version B |
| --- | --- | --- | --- | --- |
| 1 | Greet by time of day, use titles, ask after someone, take leave | Monday lobby, Friday leave-taking; f01 to f05 | L3, L5, R8, W2, S1, S2.3 | L3, L5, R8, W2, S1 |
| 2 | Introduce yourself and ask the same of others | Monday lobby; f01 to f08 | L3, L4, L5, W1, S1 | L3, L4, L5, W1, S1 |
| 3 | Ask and pay a price, check change, age and phone number, sequence | Monday form, Tuesday bill, notice board; f01 to f07 | L1, L8, R3, R5, R7, W1, S2.1 to S2.3 | L1, L8 to L10, R3, R5, W1, S2.1, S2.2 |
| 4 | Time and day, routine, done / not yet / under way | Wednesday; f01 to f07 | L1, L2, L10, R6, R9, W1, W2, S1, S2.4 | L1, L2, R6, R9, W1, W2, S1, S2.3, S2.4 |
| 5 | Describe food, objects and feelings; choose | Tuesday; f01 to f05 | L7, S1, S2.1, S2.4 | L7, S1, S2.1, S2.2 |
| 6 | Compare two, say equal, pick the best of three | Tuesday; f01 to f06 | R4, S2.2 | R4, S2.2 |
| 7 | Ask where, follow and give a route, name transport | Thursday, notice board; f01 to f05 | L2, L9, L10, R1, R6, R7, W2, S2.3 | L2, L9, L10, R1, R6, R7, S2.3 |
| 8 | Order and count with the right classifier | Tuesday; f01 to f05 | L6, L7, R3, W2, S2.1, S2.2 | L6, L7, R3, R5, R7, W2, S2.1, S2.2 |
| 9 | Read signs and notices; say what was done and by whom | Friday, notice board; f01 to f06 | L1, R2, R9, R10, S2.4 | L1, R2, R9, R10, W2, S2.4 |

Every chapter is tested by at least two items in each version (a test checks it). **Chapter 6 is the thinnest:** one reading
item and speaking card 2, which the examiner may not choose (cards 1 and 2 are alternatives). See question 4.

## Word accounting

- **Unit 9:** 37 core (29 + Sam's 8), 33 Dunia recognition, 74 revision; 71 live ledger rows placed in chapter 9.
- **Stage review and A1 test:** no new words. Every marked Malay span uses ledger words placed in chapters 1 to 9 (the build
  blocks anything else because `ms-stage1` is a re-authored unit; a test re-runs the checker at chapter 9 and checks every
  traced word's placement). The 11 components trace 274 distinct ledger entries: by first chapter 31 (Ch1), 43 (Ch2),
  48 (Ch3), 36 (Ch4), 31 (Ch5), 10 (Ch6), 36 (Ch7), 18 (Ch8), 21 (Ch9). The review block alone uses 207.
- **Words I could not use** (not in the ledger, or placed after chapter 9), so the Malay was written around them:
  «perhatian» (announcements), «hingga» (opening hours), «tolak» / «tarik» (door signs), «restoran», «farmasi», «percuma»,
  «perlu», «hilang», «bangunan», «beratur» and «membaca» (ber- and me- forms), «pesta». See the proposals below.

## Real-world facts and sources

| Fact | Source | Rank | Status |
| --- | --- | --- | --- |
| Gawai: Sarawak, 1 June; gazetted 25 September 1964, first celebrated 1 June 1965 | Sam (ledger Journal), citing The Borneo Post and the New Straits Times. Re-checked in step 5h in search summaries of The Borneo Post and Free Malaysia Today (1 June 2026), which agree on both dates | 3 | Sam's source; the NST piece itself was not seen. The summaries disagree only on an earlier, unofficial celebration (1963 or 1964), which the note does not mention |
| Kaamatan: 30 and 31 May, a public holiday in Sabah and Labuan | Sam (ledger L-1074, citing officeholidays.com); step 5h search summaries of officeholidays.com and others list both territories for 30 and 31 May 2026 | 3 | Search summaries only; the state gazettes were not opened |
| «Tahun Baharu Cina» is the form on the federal public-holiday list; «Tahun Baru Cina» is everyday | Sam (ledger L-1070), citing the federal list on ecentral.my and Education Ministry notices; a step 5h search summary of ecentral.my shows «Tahun Baharu Cina» in the 2027 list | 3 | The cabinet's own list and the ministry notices were not opened |
| «angpau» is the Malay spelling; "ang pow" is common in English-language papers | Sam, 12 Nov 2026 | Sam's reference | Not checked in Kamus Dewan (KD4 check pending) |
| «Selamat Pesta Kaamatan» | Sam: from usage | none | **Not yet sourced** (shown so on the page) |
| Christmas is celebrated by Malaysia's Christian communities | General knowledge | none | No source retrieved (kept at Sam's request) |
| The other festival facts (open houses; Deepavali; the Raya words) | As in the step 5g report | 3 | Unchanged |
| The review block and the test | All names, places, prices, numbers and times are fictional, and the pages say so | — | — |

## Unverified items

- **All Malay in the review block and the test is mine** [UNVERIFIED]: it passes the ledger, register, affix and
  Malaysian-form checks but has had no native read. Please look especially at «Saya belajar bahasa Melayu di Bangsar,
  setiap hari Sabtu.», «Mari kita makan.», «Kami mahu dua keping pisang goreng juga.», «Kopi di gerai ini yang termurah.»,
  «Dia lambat sedikit hari ini.», «Saya mahu sebiji telur.» with «roti canai», «Secawan kopi, ais sedikit.», «Kereta api
  lambat.», «Tempat letak kereta di tingkat bawah. Ketinggian dua meter.», «Kedai di tingkat bawah: diskaun sepuluh peratus
  pada hari Jumaat.», and the examiner lines («Epal dan oren, encik?», «Yang kecil warna merah sahaja.»). In unit 9:
  «Isteri saya buat kek ini.», «Saya cuci pinggan sekarang.», «Kuih ibu saya dijual di gerai dekat stesen.».
- **The pass mark** (60 per cent, half of each section), the section weights (four × 20) and the timings are my proposals,
  not taken from a JF, Irodori or CEFR document. The "Irodori / JF Standard style" is the charter's description, applied as
  "tasks with real outcomes"; I did not open the JF materials.
- **The CEFR A1 label** is the course's (charter section 8: chapters 1 to 9 are A1); it is not checked against KSBM or an
  external A1 exam.
- **Japanese** everywhere is a draft for native review.
- **Kamus Dewan** check still pending for L-0983 to L-1083 (now including «Tahun Baharu Cina», «angpau», the four roots,
  «tuan rumah», «mari», «ibu», «adik»).

## Questions for Sam

1. **Pass mark.** Is 48 of 80 (60 per cent), with at least 10 of 20 in each section, right for the A1 stage test?
2. **Time for the test.** The Stage 1 plan's 74 blocks include the stage review but not the test. The written paper takes one
   45-minute block and the speaking test about 7 minutes a learner (another block for six learners). Add one or two blocks
   to the plan (charter section 6)?
3. **The `writing` test sub-type.** The charter's tag table lists words, grammar, listening, reading and speaking for tests.
   May the stage test's writing items carry `writing` (added to the catalogue contract), or should the charter table change?
4. **Chapter 6 in the test.** Comparing is tested by one reading item and by card 2, which the examiner may skip. Add a
   comparison item to listening, or make card 2 compulsory?
5. **The catalogue's Stage 1 record** (`stages` → `ms-stage1`, `completion.flag` = `stage1_complete`, label "Malay A1 · Stage 1
   complete"): is this the shape you want Hanashishou's Evaluator to read?
6. **Proposed ledger rows** (none added): «pesta» (so that «Selamat Pesta Kaamatan» can be a ledger phrase once sourced),
   «perhatian» (announcements), «hingga» (opening hours: «Isnin hingga Jumaat»), «tolak» and «tarik» (door signs). Add any?
7. **«Selamat Pesta Kaamatan».** Do you have a source (a state or newspaper greeting), so the "not yet sourced" label can go?
8. **The Kata-Kata clean-up session.** `docs/kata-kata-cleanup.md` is ready. It contains a few proposals for you first: a
   chapter 1 Dunia scene, whole words in the chapter 6 frames, ledger L-0188 «sekali» "very", one card for «depan /
   hadapan», a «Saya pilih ___» frame and a "why" frame ms-c05-f06.
9. **Pilot.** Please teach unit 9 with the new words, the stage review and one version of the test, and tell me the timings,
   whether the review's 54-frame model is too long for 10 minutes, and how learners do on each section.

Stage 2 (chapters 10 to 18) is not started and waits for your go-ahead.
