# Handoff

Update this file at the end of every session. The next builder (ChatGPT or Claude) starts here, after the charter and `AGENTS.md`.

## Current state

- **Last updated:** 12 Nov 2026, Claude: step 5c, chapter 5 (unit 5, its writing block and the fast pack). Details in `docs/STEP-5c-report.md`.
- **Most recent approved scope:** chapter 5 only. Sam authorised it on 12 Nov 2026 and pre-approved publication to main when the checks pass. Chapter 4 (step 5b) is complete and Sam's answers to its questions are applied (see below).
- **Last commit on main:** the commit that updates this file after `3f2a710` (chapter 5 fast pack). Build and all 60 tests pass.
- **Chapter 5 source:** `suite/chapter5_common.py` (generalised from the chapter 4 helper), `suite/ms_c05.py`; the fast pack is `chapter5` in `suite/fast.py`. Tests: `tests/test_step5c_suite.py`.
- **Words:** 60 core in one unit, six themed groups (tastes 9; colours 12; size and shape 8; feelings and states 13; hot, cold, food and drink 9; question and linking words 9). The brief said 58: «seronok» (L-0455) and «tawar» (L-0520) are also placed in chapter 5 and were only recognition words in 4A and 3B, so they are core here (question 1 in the report). Dunia recognition 50 by scene ("Masak nasi goreng" 15, "Di klinik" 12, "Gambar bayi" 12, "Lepak di kedai mamak" 11). Revision 23 in two labelled groups (chapters 1 to 3; chapter 4), including «sedikit» and «kosong». The test recomputes both sets from the ledger.
- **Question words now:** apa, siapa, di mana, -kah, adakah, bolehkah, berapa, bila, pukul berapa, hari apa, **bagaimana (spoken macam mana)** and **kenapa with the answer sebab**. The tense markers return in a "Markers with adjectives" drill.
- **Legacy:** Taste and colour and Size and shape are retired from the catalogue (source kept); «Lunch at a Malaysian stall» stays linked from chapter 5. Legacy exceptions 41 → 34. Re-authored units now include ms-c05 and ms-c05-fast.
- **Unverified:** all Malay example sentences (mine, ledger-checked only; list in the report), «oren» vs «jingga» as the standard form, the «rumah sakit» form (Indonesian-leaning; Malaysians say «hospital»), usage statements in the culture note, MetMalaysia for the climate line, Kamus Dewan for L-1008 «kelakar» and L-1009 «kenapa», Japanese (draft). All prices and situations are fictional.
- **Nothing religious is in unit 5.** The ledger's «mamak» gloss says "Indian-Muslim"; learner text leaves that out until Sam decides (report question 3).
- **Chapter 3 and chapter 4** are unchanged by this step and still await Sam's pilot feedback.
- **Chapter 6 waits for Sam's explicit go-ahead.** Do not start it until he gives it.
- **Sam's answers to the step 5b questions (12 Nov 2026)** are recorded in `docs/STEP-5b-report.md` (last section): «hari bulan» for the day of the month and «tarikh» for the full date; the working-week line for KL and Selangor; split approved; «jam tiga» allowed if explained; ‹ke› shown in explainers only; proposed ledger rows approved. Second round: «Hari bulan sebelas» (hari bulan first); Kedah, Kelantan and Terengganu have a Friday and Saturday weekend and Johor returned to Saturday and Sunday on 1 Jan 2025; «Hari ini hari bulan apa?» can be heard as the weekday or the date.
- **Ledger (done, Journal rows 50 to 56):** L-1032 to L-1047 added; L-1045 retired as a duplicate of L-0702 «hujung minggu»; L-0614 «sarapan» placed in Ch4. Kata-Kata still needs cards for these words.
- **Charter snapshot** `docs/handoff/charter-snapshot.md` was refreshed on 12 Nov 2026 from the live Google Doc (one added sentence in section 8: no faith-specific greetings; ask Sam before any other faith-specific expression).

## Done

| Step | What | Report |
| --- | --- | --- |
| 1 | Malay units regrouped into 9 A1 chapters and 13 unit slots; wording preserved; issues logged | `docs/STEP-1-REPORT.md` |
| 2 | Catalogue: chapter records, 11 component types, tags, test-item contract | `docs/STEP-2-REPORT.md` |
| 3 | Build checks (ledger, register, affix, Malaysian form) with a frozen, shrink-only exception baseline of 86 keys | `docs/STEP-3-REPORT.md` |
| 4 | Pilot: full 11-component suites for units 1, 2A, 2B (plus pronunciation and writing blocks) and fast packs for chapters 1 and 2; all section 6 minimums and section 14 drills met and tested; baseline 86 → 79 | `docs/STEP-4-REPORT.md` |
| 5a | Chapter 3 (3A, 3B, 3C) and its one-session fast pack, with 73 unique core and 24 recognition entries; source and printed packs tested in the step-5a gate; no chapter 4 | docs/STEP-5a-report.md |
| 5b | Chapter 4 (4A, 4B) and its fast pack: 71 core, 55 Dunia recognition by scene, timeline drill, review block after 4B; legacy chapter 4 packs retired | `docs/STEP-5b-report.md` |
| 5c | Chapter 5 (unit 5, writing block) and its fast pack: 60 core in six groups, 50 Dunia recognition by scene, «bagaimana» and «kenapa» / «sebab» added to the question words, markers drill; legacy chapter 5 packs retired | `docs/STEP-5c-report.md` |

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

- **One unit.** Unit 5 (13-unit plan), five blocks plus the 45-minute writing block (`ms-c05-writing-block`, registered as `ms-stage1-writing-5`). 60 core words are taught in six themed groups; the plan says one or two groups per block. Whether 60 is too many is for the pilot to say (report question 7).
- **Malay rules applied:** standard first («mahu», «tetapi», «bagaimana», «jingga») with «nak», «tapi», «macam mana», «oren» marked spoken; no comparatives («lebih», «paling», «daripada» are named only as ‹…› mentions in the teacher notes; «kurang manis» is the one fixed «kurang»); root verbs only; no word placed after chapter 5 («sangat», «sini», «kedai», «baju», «kerusi», «tolong», «hospital», «yang mana» are out of reach, so scenes were changed rather than the Malay).
- **Scenes:** a mamak order (model conversation, task, menu reading, writing), a Monday weekend talk (listening), a late arrival and feeling tired (patterns 4 and the short dialogues). The Kata-Kata scenario's «nasi lemak» and «sambal» are not in the ledger, so «mi goreng» and «roti canai» (Dunia recognition words) carry the scene. The clinic words are symptoms only.
- **Culture note:** ordering a drink, colours and the flag (CIA World Factbook), hot and humid climate (Britannica; not checked against MetMalaysia), «nak» as spoken. Word notes come only from Kata-Kata card notes. No religious content.
- **Helper:** `chapter5_common.py` is `chapter4_common.py` with these differences: the timeline drill became a general "markers" drill, the test accepts 15 to 20 scored items (this unit has 19 plus the speaking task), the opener's Japanese scene list is separate (`dunia_list_ja`; units 4A and 4B still have a leftover English "and" there), and the unit ID is `ms-c05`. Use it as the starting point for chapter 6.
- **Mentions added** to `curriculum/malay-mentions.json`: ‹teh O›, ‹jambu›, ‹hospital›, ‹lebih›, ‹paling›, ‹kurang›, ‹daripada›, each with its source.
- **Kata-Kata findings:** frame f03 uses «baju» (Ch8); the scenario uses «nasi lemak», «sambalnya» and «kedai mamak»; card ms-c05-008 «sedikit» is still a chapter 5 card; no cards or frame for «kenapa», «sebab», «kelakar»; «rumah sakit» is Indonesian-leaning; no note on «oren» / «jingga» (details in the report).

## Next: Sam's feedback, then chapter 6 only on his go-ahead

1. Answer the questions at the end of `docs/STEP-5c-report.md` (core count, «oren» / «jingga», «mamak» and religion, «rumah sakit», proposed ledger rows, «mengapa» and a «Kenapa … Sebab …» frame, the 60-word load, the chapter 4 opener fix).
2. Kata-Kata (Claude Code) adds cards for L-1032 to L-1044, L-1046, L-1047, L-0614 and L-0702 (chapter 4) and for L-1008, L-1009 and L-0688 (chapter 5); the Kamus Dewan check covers L-0983 to L-1047.
3. Chapter 3, 4 and 5 pilot feedback: timings, drill load, the fast packs.
4. **Chapter 6 waits for Sam's go-ahead.** The chapter 6 words «lebih», «paling», «kurang», «daripada», «sangat», «amat», «terlalu» and «sama» are placed there; the unit 5 teacher notes already tell teachers not to anticipate them.

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

Kata-Kata (Claude Code) still needs the same ledger changes: new cards for L-0983 to L-1031, saya and the time words moved to chapter 1, Ch2 cards for «sedikit», «cakap» and «badminton», and card ms-c01-009 (Assalamualaikum, L-0009) removed. Tracked in the ledger Journal as pending.

Step 4 findings for Kata-Kata:
- The chapter 2 scenario uses «dari mana» (ledger chapter 7) and «badminton» (chapter 6) at chapter 2.
- Chapter 1 still has no Dunia scene; Block E of unit 1 uses the chapter 1 scenario instead.
