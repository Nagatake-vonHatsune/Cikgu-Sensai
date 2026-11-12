# Handoff

Update this file at the end of every session. The next builder (ChatGPT or Claude) starts here, after the charter and `AGENTS.md`.

## Current state

- **Last updated:** 12 Nov 2026, Claude: step 5g, the unit 8 follow-ups, the six festival ledger rows, chapter 9 (unit 9 and the fast pack). Details in `docs/STEP-5g-report.md`.
- **Chapters 1 to 9 are written** (units 1, 2A, 2B, 3A, 3B, 3C, 4A, 4B, 5, 6, 7, 8, 9, their fast packs, the review blocks after 3A, 4B and 6, and the writing blocks after 2B, 3C, 5 and 7). **The remaining Stage 1 work is the stage review and the A1 test, which wait for Sam's go-ahead.** Do not start either before he says.
- **Most recent approved scope:** step 5g only. Sam authorised it on 12 Nov 2026 and pre-approved publication to main when the checks pass.
- **Last commit on main:** the commit that updates this file (it follows `56887d7`, the chapter 9 fast pack; `625772b` unit 9; `4b98f45` the festival ledger rows; `e8b2059` the unit 8 follow-ups). Build and all 130 tests pass. The session branch `claude/serene-feynman-3x1cq2` was pushed to the same commit as main.
- **Chapter 9 source:** `suite/chapter9_common.py` (generalised from the chapter 8 helper; it also builds a second Culture note component for the festival notes), `suite/ms_c09.py`; the fast pack is `chapter9` in `suite/fast.py`. Tests: `tests/test_step5g_suite.py`.
- **Words, unit 9:** 29 core in four groups (18 «di-» verbs; «oleh», «pada», «tadi», «siap»; 5 signs and notices; «kek», «jamuan»). Dunia recognition 33: the general «rumah terbuka» scene 19 (the 13 Raya words plus Sam's six festival words L-1070 to L-1075) and the 14 "Simpulan bahasa harian" idioms (recognition only, never drilled). Revision 74. The ledger copy places 63 live rows in chapter 9; the test recomputes the sets from the ledger.
- **Words, unit 8 after the follow-ups:** 41 core in five groups (classifiers 14 including L-1067 «buah»; containers 7; things counted 12; the «gerai» 5: «nasi lemak», «gerai», «tambah», «pisang goreng», «keropok lekor»; «semua», «tolong», «Makan sini atau bungkus?» 3), 11 recognition ("Beli baju"), 53 revision. «se-» + any counter is taught and drilled with every counter beside «satu» + counter (Sam's correction); «seekor», «sebiji», «sebuah» are also whole ledger words; ‹sebatang› and ‹sehelai› are no longer mentions. «pisang goreng» is standard, «goreng pisang» everyday. «kaki» as a counter is not added.
- **Register (Sam, 12 Nov):** «pucuk» and «naskhah» are formal counters mostly seen in writing; «tapau» is everyday speech; «sesak» is standard, «jam» everyday speech. L-0592 «pintu masuk» is Retired (unit 7: 63 live rows, 62 core). L-0931 «mamak» Japanese is ママック. The unit 7 culture note keeps the left-hand traffic and 2020 census sentences.
- **The «di-» rule:** the 18 ledger forms are core; «di-» + any ledger verb root is taught as the rule («digoreng», «dipilih», «ditunggu», «dijemput», «ditanya»). The language checks accept «di-» + any ledger word placed in chapters 1 to 9 (no part-of-speech check), so `test_di_rule` is stricter: a ledger «di-» form or «di-» + a ledger verb; no ber- or me- verb; ‹buat›, ‹panggil›, ‹cuci›, ‹larang› (roots of four ledger forms that are not ledger words) are mentions only. The doer before the verb («Pinggan saya bawa ke dapur.», Kata-Kata frame f06) is taught inside pattern 3.
- **Festival notes (Sam, 12 Nov):** the scene is a general «rumah terbuka» scene; each festival has a short culture note in `Culture note · Open houses in Malaysia` (Block E): Hari Raya (the Raya words sit only here), Tahun Baru Cina, Deepavali, Krismas, Gawai and Kaamatan. Greetings are «Selamat Hari …» built from ledger words (no greeting rows, no faith-specific greeting). **All festival facts come from search summaries only (Wikipedia was unreachable); the Christmas sentence is general knowledge with no source.** Sources are named in the key and the report.
- **Ledger (sheet, by Claude):** L-1064 to L-1069 (written earlier, Journal rows 75 to 80) and L-1070 to L-1075 (Journal rows 81 and 82). Both repo copies and the hash in `docs/step4-sources.json` match the sheet (1,075 rows).
- **Question words now:** all earlier ones plus **«siapa» with «oleh»** (chapter 9 adds no new question word).
- **Unverified:** all Malay example sentences (mine, ledger-checked only), the counters used with «pisang goreng» and «keropok lekor», the Kamus Dewan spelling of the new festival words and of «Tahun Baru Cina», the festival facts, Japanese (draft). All places, notices, prices and times are fictional.
- **Proposed, awaiting Sam:** the roots «buat», «panggil», «cuci», «larang» as ledger rows; «ibu», «adik», «tuan rumah», «mari»; the Japanese of L-1064 (ナシレマッ looks truncated); an explicit narrow ‹se-› + counter rule in the checker (not needed so far); the charter table's chapter 9 scene list (Rumah terbuka Hari Raya → Rumah terbuka).
- **Charter snapshot** `docs/handoff/charter-snapshot.md` matches the live Google Doc for the chapter 7, 8 and 9 rows (read on 12 Nov 2026).

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

## Next: Sam's feedback, then the stage review and the A1 test only on his go-ahead

1. Answer the questions at the end of `docs/STEP-5g-report.md` (load of units 8 and 9; the festival facts and the Christmas sentence; the greetings; the proposed rows; the spellings for the Kamus Dewan check and the Japanese of L-1064; the explicit «se-» rule; the charter table; the pilot).
2. Kata-Kata (Claude Code) adds the cards and frame changes listed in the step 5b to 5g reports (including cards for L-1032 to L-1075 and L-0614, L-0702, L-0688, the "why" frame, «hospital» in "Di klinik", the «jalan lurus» fix on ms-c07-024, the general "Rumah terbuka" scene, and the chapter 6 to 9 findings above); the Kamus Dewan check covers L-0983 to L-1075.
3. Chapter 3 to 9 pilot feedback: timings, drill load, the fast packs, the review blocks after 3A, 4B and 6, the writing blocks after 2B, 3C, 5 and 7.
4. **The stage review and the A1 test** (after unit 9, charter section 6) are the remaining Stage 1 work and wait for Sam's go-ahead. Do not start them, and do not start Stage 2 (chapters 10 to 18).

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
