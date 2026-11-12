# Handoff

Update this file at the end of every session. The next builder (ChatGPT or Claude) starts here, after the charter and `AGENTS.md`.

## Current state

- **Last updated:** 12 Nov 2026, Claude: step 5e, the unit 6 follow-ups, the review block after unit 6, and chapter 7 (unit 7 and the fast pack). Details in `docs/STEP-5e-report.md`.
- **Most recent approved scope:** step 5e only. Sam authorised it on 12 Nov 2026 and pre-approved publication to main when the checks pass. Chapters 4 to 6 (steps 5b to 5d) are complete.
- **Last commit on main:** the commit that updates this file (it follows `6d49e03`, the chapter 7 fast pack; `4d4a4d6` unit 7; `b628ff3` review block; `c43f7e2` unit 6 follow-ups). Build and all 91 tests pass.
- **Chapter 7 source:** `suite/chapter7_common.py` (generalised from the chapter 6 helper), `suite/ms_c07.py`; the fast pack is `chapter7` in `suite/fast.py`. Tests: `tests/test_step5e_suite.py`.
- **Words, unit 7:** 56 core in five themed groups (position words 13; distance and direction 9; turning and moving 9; landmarks and transport 21; compass points 4). The ledger places 53 rows in chapter 7; with the five rows added in this step it is 58, less L-0592 (duplicate «pintu masuk» of L-0330) and L-0304 («depan», already L-0173 in chapter 4). Dunia recognition 33 ("Di ruang tamu" 13, "Telefon baru" 12, "Lintas jalan" 8). Revision 43 (including «hospital», «kapal terbang», «bilik», «lama», «depan»). The test recomputes all sets from the ledger.
- **Words, unit 6 after the follow-ups:** 35 core («sewa», «bilik», «luas» added), 14 recognition, 30 revision. «senang» is marked spoken beside «mudah».
- **Question words now:** apa, siapa, di mana, -kah, adakah, bolehkah, berapa, bila, pukul berapa, hari apa, bagaimana (macam mana), kenapa = mengapa = apa sebab, yang mana, and **ke mana, dari mana, berapa jauh, berapa lama**.
- **Scene:** asking the way to a bank and the bus, a phone call giving directions to an office (listening), a building directory (reading), asking the way to the hospital (task). All routes, distances and times are fictional.
- **«ke» is taught.** «pergi ke pejabat» and «balik ke rumah» are the standard form; «pergi kerja» and «balik rumah» are everyday speech (tested on every line).
- **Places of worship (Sam, in the session):** «masjid» (L-0337) plus new rows L-1054 «gereja», L-1055 «kuil», L-1056 «tokong», L-1057 «gurdwara» and L-1058 «surau» are one even-handed set of plain landmarks, used evenly (tested). No worship, dress or etiquette content. «vihara» was offered and not chosen.
- **Review block after unit 6:** written (`ms-c06-review-block`, chapters 1 to 6, registered as `ms-stage1-review-6`). Review blocks after 3A, 4B and 6 are now all written.
- **Legacy:** "Asking where", "Directions and orientation" and the grammar pack "Di, ke and dari" are retired from the catalogue (source kept; the last had «kampus» and «tren», not in the ledger). Legacy exceptions 32 → 30. Re-authored units now include ms-c07 and ms-c07-fast.
- **Not written:** the writing block after unit 7 ("directions by message", Stage 1 plan); Sam decides (question 6 in the report).
- **Unverified:** all Malay example sentences (mine, ledger-checked only), «gurdwara» spelling and the Kamus Dewan status of L-1054 to L-1058, «jam» (traffic) and «tengok» as spoken, the left-hand-traffic and census sentences in the unit 7 culture note (secondary sources), Japanese (draft). All places, routes, distances and times are fictional.
- **Ledger (sheet, by Claude in this and the previous session):** L-1051 to L-1053 (Journal rows 64, 65), the L-0285 note, L-1054 to L-1058 and Journal rows 66 and 67. Both repo copies and the hash in `docs/step4-sources.json` match the sheet (1,058 rows).
- **Proposed, awaiting Sam:** «kilometer», «sebulan», «tumpang tanya», «terus», «jangan», «tangga»; retire L-0592; merge L-0304 into L-0173; a Meaning edit for L-0188 «sekali».
- **Chapter 8 waits for Sam's explicit go-ahead.** Do not start it until he gives it. Chapters 3 to 7 still await Sam's pilot feedback.
- **Sam's answers to the step 5d questions (12 Nov 2026):** the three ledger rows added; «senang» spoken; only the six whole ter- and se- words until chapter 16; keep the Strata Management Act and rail-network note; «sekali» (Q3) updated by Claude if Sam confirms. Questions 2 («tengok») and 7 (pilot) remain open.
- **Sam's answers to the step 5c questions (12 Nov 2026)** are in `docs/STEP-5c-report.md` ("Sam's answers"). **Sam's answers to the step 5b questions** are in `docs/STEP-5b-report.md` (last section).
- **Charter snapshot** `docs/handoff/charter-snapshot.md` was refreshed on 12 Nov 2026 from the live Google Doc.

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

## Next: Sam's feedback, then chapter 8 only on his go-ahead

1. Answer the questions at the end of `docs/STEP-5e-report.md` (the «gurdwara» spelling and the five rows; duplicates L-0592 and L-0304; the retired "Di, ke and dari" pack; proposed words; «hospital» and «kapal terbang»; the writing block after unit 7; the culture note; the pilot).
2. Kata-Kata (Claude Code) adds the cards and frame changes listed in the step 5b to 5e reports (including cards for L-1032 to L-1058 and L-0614, L-0702, L-0688, the "why" frame, «hospital» in "Di klinik", and the chapter 6 and 7 findings above); the Kamus Dewan check covers L-0983 to L-1058.
3. Chapter 3 to 7 pilot feedback: timings, drill load, the fast packs, the review blocks after 3A, 4B and 6.
4. **Chapter 8 (Penjodoh bilangan) waits for Sam's go-ahead.** Words placed in chapter 8 (for example «tolong», «baju», «butang») stay out of the chapter 7 scenes; the unit 7 teacher notes say so. Chapter 8's cumulative question word is «berapa» with a counter.

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
