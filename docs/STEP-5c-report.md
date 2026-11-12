# STEP 5c REPORT: Chapter 5, Batch 3

**Scope:** Malay A1 chapter 5 (adjectives; «bagaimana» / «macam mana»; «kenapa» and «sebab»): **unit 5** with its writing block, and the chapter 5 fast pack. Sam authorised chapter 5 on 12 Nov 2026 and pre-approved publication to main when the checks pass.

**Sources read:** the live Unified Curriculum Charter (Google Doc, read in full on 12 Nov 2026; it differs from `docs/handoff/charter-snapshot.md` only by one sentence in section 8, now copied into the snapshot), `AGENTS.md`, `HANDOFF.md`, the Kata-Kata chapter 5 file (`curriculum/reference/katakata/c05.json`), the ledger snapshot, and the chapter 4 source and report used as the model.

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests` (62 tests) pass on a full Git checkout at every commit below. **Updated the same day for Sam's answers** (last section): the figures below are the current ones.

| Commit | Content |
| --- | --- |
| `05041ba` | Unit 5, chapter 5 helper, tests, retirement of Taste and colour and Size and shape |
| `3f2a710` | Chapter 5 fast-course pack |
| `476cd55` | First version of this report, `HANDOFF.md` and the refreshed charter snapshot |
| next commit | Sam's answers applied: ledger rows, unit 5 changes, chapter 4 opener fix |
| this commit | This report and `HANDOFF.md` brought up to date |

## Word accounting

All counts are unique ledger entries. A slash variant («mahu» / «nak», «tetapi» / «tapi», «jingga» / «oren») counts once.

| Unit | Theme | New core | Dunia recognition (by scene) | Revision (not counted, not tested as new) |
| --- | --- | ---: | --- | --- |
| 5 | Tastes, colours, size and shape, feelings and states, hot and cold, food and drink, «bagaimana», «kenapa» / «mengapa», «sebab» / «kerana», «yang», «atau», «tetapi» | **63** (60 first built, plus «kuah», «mengapa», «kerana» on Sam's instruction) | **50**: "Masak nasi goreng" 15, "Di klinik" 12, "Gambar bayi" 12, "Lepak di kedai «mamak»" 11 | 23: 15 from chapters 1 to 3, 8 from chapter 4 |

**Core load: 63 in one unit** (the charter says 20 to 40; the 13-unit plan does not split chapter 5; Sam: "more is ok"). All 63 stay core, taught in six themed groups so no block has to carry more than two:

| Group | Words |
| --- | ---: |
| Tastes (rasa, manis, masin, masam, pedas, pahit, sedap, tawar, kurang manis) | 9 |
| Colours (warna and eleven colours) | 12 |
| Size and shape (besar, kecil, pendek, rendah, ringan, tebal, nipis, sempit) | 8 |
| Feelings and states (gembira … sakit, seronok, kelakar) | 13 |
| Hot, cold, food and drink (panas, sejuk, ais, air, air kosong, teh / kopi, nasi, mi, roti, kuah) | 10 |
| Question and linking words (bagaimana, macam mana, kenapa, mengapa, sebab, kerana, yang, atau, tetapi, mahu, banyak) | 11 |

The teaching plan says to teach one or two groups per block and recycle them; the vocabulary sheet, the 13-turn model conversation and the Block E scenes keep returning to them. The load is still the heaviest of any unit so far (4A has 40). Sam left the split to me; I kept one unit (see the last section).

**Ledger check: 60 at first, 63 now, not 58.** `tests/test_step5c_suite.py` recomputes the sets from the ledger with the same rule as the chapter 4 test (a row with a "Ch5" part). That gave **60** core rows, not the 58 in the brief; Sam accepted that ("more is ok"), and the three rows added on 12 Nov bring it to **63**. Fifty-eight rows were placed "Ch5" (or "Ch5 (pending)") only. The other two are **«seronok» (L-0455)** and **«tawar» (L-0520)**: the ledger places them in chapter 5 as well as in a Dunia scene ("Cuti ke pantai" for chapter 4, "Pasar pagi" for chapter 3). Unit 4A and 3B showed them as recognition words only and never taught them, so I treat them as core here and the unit says so. The 50 recognition entries match the brief exactly; «hospital» (L-0336) now stands in for the retired «rumah sakit» in "Di klinik".

**Words reused, not new.** «sedikit» / «sikit» (L-0216, now chapter 2) and «kosong» (L-0099, chapter 3, in «air kosong») are listed under **Revision · 復習**, with 21 other chapter 1 to 4 words that return (berapa, harga, mahal, murah, tinggi, berat, panjang, lebar, pisang, mangga, cili, segar, bukan; hujan, cuaca, lambat, lewat, sudah, belum, masih, payung). The test checks that none of them is counted as core or recognition.

## Evidence for charter section 6 and section 14

| Minimum | Unit 5 | Where it is tested |
| --- | --- | --- |
| Eleven components | All eleven, plus the markers drill and the writing block | `test_components_and_vocabulary` |
| Vocabulary: every ledger word, JA and EN meaning, one example each, spoken forms marked | 136 entries (63 + 50 + 23), each with an example; «macam mana», «nak», «tapi», «tak apa», «dah», «sikit» shown as spoken («jingga» and «oren» are both taught as correct) | entry count = example count = ID count |
| 3 to 5 patterns, 4 to 6 Q&A each, EN and JA explanation, Japanese note | 5 patterns × 5 or 6 Q&A (frames ms-c05-f01 to f05); «Kenapa» / «mengapa» / «apa sebab» with «sebab» / «kerana» sits in pattern 4 | `test_patterns` |
| Drill types 1 to 5, at least 6 items each (30+) | 8 items each (40) | `test_drills_keys_and_question_words` |
| Type 6 short dialogues (3+) | 4 | same |
| Cumulative question words | apa … berapa, bila, pukul berapa, hari apa + **«bagaimana» (spoken «macam mana»)** and **«kenapa» (= «mengapa», «apa sebab»; answers «sebab» or «kerana»)**; 11 tasks with model questions; the choice drill uses bagaimana, kenapa, berapa, bila, siapa, di mana, apa and bolehkah | same |
| Tense and aspect markers return (section 14) | "Markers with adjectives": «sudah», «belum», «masih», «akan» with the new adjectives, 8 items, Japanese bridge, key | `test_markers_return` |
| Real answer keys | Every drill item, markers item, reading item and self-check item has its own answer | key regex per item |
| Model conversation 10 to 16 turns, gapped, changed facts | 13 turns at a mamak stall, gapped (5 gaps, answers in key), 13-turn variant | `test_conversation_…` |
| Listening 120 to 250 Malay words, before/during/after, 6+ items | 133 words, 9 items | same |
| Reading text with 5+ questions; guided writing with model | A mamak menu (fictional prices), 7 questions, an order slip with a model; plus the 45-minute writing block (short description, peer questions, rewrite) | same, `test_tests_and_plans` |
| Task: role cards, change of plan, success criteria | Ordering at a mamak; the dish is finished and a friend arrives | same |
| Culture note 150 to 300 words, full JA translation | 240 words, four paragraphs; no leftover English in the Japanese | word count and a Japanese-cell check |
| Test 15 to 20 items + speaking, every item tagged | 19 scored (6 listening, 7 words, 2 grammar, 4 reading) + 1 speaking; every item lists the ledger words it tests, and word items use core words only | `test_tests_and_plans` |
| Teaching plan: timings, prompts, Kata-Kata before and after | Five blocks, Sedia Kelas c05, the four Dunia scenes | same |
| Writing block after unit 5 (Stage 1 plan) | `ms-c05-writing-block`, registered in the catalogue as `ms-stage1-writing-5` | `test_legacy_retirement_and_catalogue` |
| Fast pack: 2 to 4 pages, 15 to 20 words, patterns with 2 examples | 3 content pages, 20 words, 5 patterns, a 10-turn conversation, task, 5-item self-check, self-study guide | `test_fast_pack` |

**Chapter 5 Malay rules, tested:**
- No comparatives or superlatives: no «lebih», «paling», «daripada», and «kurang» only in «kurang manis». The teacher notes name them as mentions (‹lebih›, ‹paling›, ‹kurang›, ‹daripada›, each with a ledger source) so they are not taught.
- Standard first, spoken marked: «mahu», «tetapi», «bagaimana» come before «nak», «tapi», «macam mana»; every line with a spoken form carries a "spoken" label. «jingga» and «oren» are both correct (Sam).
- No faith-specific greetings or expressions, no food rules, and no medicine, diagnosis or dose in the clinic words (symptoms only).
- Root verbs only; no ber- or me- forms. The build's ledger, register, affix and Malaysian-form checks pass with no exceptions for unit 5 or the fast pack.
- No word placed after chapter 5 is used (this ruled out «sangat», «sini», «kedai», «baju», «kerusi», «tolong», «sila», «yang mana»; the unit works around them; «hospital» now has a chapter 5 recognition placement).

**Natural Malay.** The dialogues are about ordering a drink and a dish at a mamak stall, a Monday talk about the weekend, a menu, a late arrival and feeling tired. Where the in-scope words could not make a natural sentence I changed the scene: for example the Kata-Kata scenario's «nasi lemak» and «sambal» (not in the ledger) became «mi goreng» and «roti canai» (Dunia recognition words); frame ms-c05-f03's «baju» (chapter 8) became «payung», «fail», «buku» and «mangga».

**Legacy packs.** Taste and colour and Size and shape (learner pack and teaching plan each) are removed from the active catalogue; their source text stays in `curriculum/malay-course.txt`. The A2 conversation «Lunch at a Malaysian stall», which was linked from Taste and colour, stays linked from chapter 5 (`AUTHORED_LINKS` in `course.py`). Seven legacy exceptions for ms-c05 (atas, bawah, kalau, yang mana, nak, sikit, tak) are removed: **41 → 34**. The chapter 5 page status now reads "Step 5c chapter 5 suite · draft for pilot".

## Files changed

- **New:** `suite/chapter5_common.py`, `suite/ms_c05.py`, `tests/test_step5c_suite.py`, this report.
- **Changed:** `suite/__init__.py` (grammar points ms-c05-g02 to g06, scene titles, "hospital" added to the English homograph list, unit loading, glosses for «mahu», «tetapi», «kenapa»), `suite/fast.py` (chapter 5 pack), `suite/chapter4_common.py`, `suite/ms_c04a.py`, `suite/ms_c04b.py` (Japanese scene list in the opener), `course.py` (retired packs, chapter 5 status, the stall link), `catalogue.py` (writing block after unit 5), `curriculum/reauthored-units.json` (+ms-c05, ms-c05-fast), `curriculum/legacy-exceptions.json` (seven removed), `curriculum/malay-mentions.json` (‹teh O›, ‹jambu›, ‹lebih›, ‹paling›, ‹kurang›, ‹daripada›, ‹rumah sakit›, each with its source), `curriculum/malay-roots.json` (+mengapa), `curriculum/malay-proper-nouns.json` (Rashid, Jalur Gemilang), the ledger copies (`curriculum/reference/katakata/malay-ledger.csv`, `docs/handoff/ledger-snapshot.csv`) and `docs/step4-sources.json` (see the ledger update below), `tests/test_catalogue.py` (retired titles, the roots list), `tests/test_language_checks.py` (its "not yet re-authored" fixture moves from ms-c05 to ms-c06), `docs/handoff/charter-snapshot.md` (the faith-expression sentence), `HANDOFF.md`, and the generated files in `dist/` and `docs/step4-authored-scope.json`.
- **Not changed:** the Kata-Kata reference files and the legacy lesson sources.

## Proposed ledger rows

| Word | Meaning | Status |
| --- | --- | --- |
| kuah | gravy, sauce | **Added** as L-1048 (Ch5), on Sam's instruction |
| mengapa | why (same as kenapa and apa sebab) | **Added** as L-1049 (Ch5), after Sam's answer to question 6 |
| kerana | because | **Added** as L-1050 (Ch5), after Sam's answer to question 6 |
| nasi lemak | rice cooked in coconut milk | Still proposed (Ch5): the Kata-Kata scenario orders it |
| sambal | chilli paste | Still proposed (Ch5): «Sambalnya pedas?» in the same scenario |
| pesan | to order (food, a drink) | Still proposed (Ch5) |
| susu | milk | Still proposed (Ch5): explains ‹teh O› "without milk" |
| tambah | to add, more | Still proposed (Ch5): «Tambah ais» |

Sam did not mention the five "still proposed" rows; they stay unused. «kari» was dropped from the list because «kuah» now covers it. All new rows are "Not yet checked" for Kamus Dewan.

## Real-world facts used, and their sources

| Fact (unit 5 culture note) | Source checked | Rank | Status |
| --- | --- | --- | --- |
| The national flag, the Jalur Gemilang, is red, white, blue and yellow (the note says nothing else about the flag) | CIA World Factbook, Malaysia, "Flag description": 14 red and white stripes, a blue canton with a yellow crescent and star (seen in a search summary; the page itself was not opened) | 2 | [VERIFIED] via the summary |
| Malaysia is hot and humid throughout the year | Encyclopaedia Britannica, "Malaysia: Climate"; FAO climate summary (search summaries) | 3 | [VERIFIED] in general; **not checked against MetMalaysia**, whose page the search did not return |
| A «mamak» stall is a casual eatery serving Tamil Muslim-derived food, run by Indian-Muslim families, with roti canai and teh tarik as its centre; the word is best used for the stall and not for a person | Wikipedia, "Mamak stall" and "Mamak people" (search summaries; the pages themselves were not opened) | 3 | [VERIFIED] against Wikipedia only; no primary source |
| Stalls are "often open late" | Ledger L-0931 (Sam's Vocab Bank v4). A travel blog says Kuala Lumpur has 24-hour mamak stalls; I found no independent source that all of them are | Sam's reference | Taken from the ledger; not independently checked |
| ‹teh O› is tea without milk; «merah jambu» is literally "jambu-fruit red"; «yang merah» is "the red one"; «nak» is spoken; «kosong» means zero or empty | Kata-Kata cards ms-c05-055, -025, -004, -005 and -054 | Sam's reference | [VERIFIED] against the card notes |
| «kopi O» is black coffee with sugar; «tapau», «makan sini», «Kira!»; «kuah» is gravy or sauce | Ledger L-0936, L-0937, L-0938, L-0941, L-1048 | Sam's reference | Taken from the ledger as written |
| An order is built as drink, sweetness, hot or cold, ice | Kata-Kata frame ms-c05-f05 and scenario ms-c05-s01 to s11 | Sam's reference | As in Kata-Kata |

The culture note now says who traditionally runs a mamak stall, as Sam approved. It has no food rules, religious expressions, dated or legal facts.

## Unverified and provisional

- **All Malay example sentences are mine.** They pass the ledger, register, affix and Malaysian-form checks, but none has had a native read. Please look especially at: «Harga mangga rendah hari ini.», «Saya takut ribut.», «Teh ini tawar.» (unsweetened), «Kopi ini tawar, tetapi sedap.», «Ada yang tidak pedas?», «Encik rasa bagaimana hari ini?», «Puan mahu gula sedikit?», «Roti canai dengan kuah» and «kuah banyak», «Mi goreng (pedas)» and «Teh dan kopi: kurang manis, boleh.» on the menu, and «Muka dia macam muka saya.» [UNVERIFIED]
- **«kenapa», «mengapa», «apa sebab», «kerana», «sebab».** Taught as Sam said (equivalent questions; the answers are «sebab» or «kerana», mainly). I did not say which is more formal or more common: the unit says «kenapa» is the everyday one, which is Sam's own earlier "formal: mengapa" gloss. [UNVERIFIED beyond Sam's judgement]
- **Usage statements in the culture note, not checked against a source:** at the counter you often hear «nak» for «mahu»; «panas» and «sejuk» are everyday words for weather and drinks. The Japanese customisation comparison (甘さ控えめ、氷少なめ) is general knowledge, not sourced. [UNVERIFIED]
- **«tawar».** The ledger says "to bargain; bland" and the Kata-Kata card says "bland, unsweetened". The unit teaches "bland, unsweetened" and points back to chapter 3 for "to bargain" («Boleh tawar?»).
- **Without «ke».** «pergi klinik» and «pergi pasar» follow the chapter 4 decision (no «ke» before chapter 7).
- **Kamus Dewan check** is still pending for «kelakar» (L-1008), «kenapa» (L-1009), «kuah», «mengapa» and «kerana» (L-1048 to L-1050), and for L-0983 to L-1047 in general.
- **Japanese:** all of it is a draft for native review, including the full culture-note translation.
- **In class:** timings, drill load, the 63-word unit and the writing block have not been taught.
- All prices, menus, names and situations are fictional and labelled so.

## Findings for Kata-Kata (not changed here)

- **Frame ms-c05-f03** uses «baju» (ledger chapter 8): «Saya mahu baju yang biru.»
- **The chapter 5 scenario "At the mamak"** uses «nasi lemak» and «sambalnya» (not in the ledger) and the title says «kedai mamak» (ledger chapter 7).
- **Card ms-c05-008 «sedikit / sikit»** is still a chapter 5 card although the ledger moved L-0216 to chapter 2, and the Sedia Kelas c05 list still includes it (already noted in `HANDOFF.md`).
- **New cards and a frame are needed** for «kenapa» (L-1009), «mengapa» (L-1049), «sebab» (L-0688), «kerana» (L-1050), «kuah» (L-1048) and «kelakar» (L-1008). Cikgu Sensai teaches the "why" set under ms-c05-f04 for now; a frame such as ms-c05-f06 «Kenapa / Mengapa / Apa sebab ___? Sebab / Kerana ___.» is proposed.
- **Dunia "Di klinik":** the scene card ms-d-badan-klinik-11 («rumah sakit», L-0416, now retired) should become «hospital» (L-0336, now placed in the scene).
- **Card ms-c05-020 «oren / jingga»:** Sam says both are correct; the card could say so.
- **Card ms-c05-015 «tawar»** has only the "bland" sense; the ledger row has both.
- **Dunia "Lepak di kedai mamak":** Sam approved a culture note on who runs a mamak stall; the scene could use the same wording.

## Found in chapter 4 (fixed)

The Japanese line of the opener in units 4A and 4B had a leftover English "and" («"Hujan petang" and "Cuti ke pantai"»), because the helper copied the English scene list into the Japanese line. Fixed on Sam's instruction: both units now carry a separate Japanese scene list (`dunia_list_ja`), and a test checks the openers of 4A, 4B and 5.

## Sam's answers (12 Nov 2026) and what changed

| # | Sam's answer | What changed |
| --- | --- | --- |
| 1 | Core count is fine; more is OK. | Kept (60 at the time, 63 now). The report and test say 58 + 2 + 3. |
| 2 | Both «jingga» and «oren». | Both are taught as correct; «oren» is no longer marked spoken or demoted (vocabulary line, example, teacher notes, tests). |
| 3 | The culture note may say who runs a mamak stall. | The note now says "traditionally run by Indian-Muslim families" and adds that «mamak» is for the stall, not for a person (Wikipedia, Rank 3). The vocabulary gloss is the ledger's own. Still no food rules or religious expressions. |
| 4 | Use «hospital»; no need for «rumah sakit». | **Ledger (sheet first, Journal rows 57 to 62):** L-0336 «hospital» now reads "Dunia · Di klinik (primes Ch5); Ch7"; L-0416 «rumah sakit» is Retired (place cleared; IDs are never deleted). «hospital» replaces it in the "Di klinik" list with «Dia di hospital.»; «rumah sakit» is named only as a ‹mention› in the teacher notes. Recognition stays 50, 12 in the scene. |
| 5 | Add «kuah» (gravy, sauce) if it is not in the ledger. | It was not. Added as **L-1048** (Ch5) and taught in the food group: «Roti canai dengan kuah.», a pattern 5 exchange («Roti canai, dengan kuah?» «Ya, kuah banyak.»), the menu line and a reading question, and the variant conversation. |
| 6 | Frame is fine, but «kenapa», «mengapa» and «apa sebab» are equivalents; answers are «kerana» or «sebab», mainly. | Added **L-1049 «mengapa»** (affix tag lex; added to the root allow-list in `curriculum/malay-roots.json`, like «memang» and «mesti») and **L-1050 «kerana»**. Pattern 4, the question-word set and its key, a grammar test item, the fast pack and the teacher notes now teach the three as one question and accept «sebab» or «kerana». A note on L-1009 records it; the edit to L-1009's Meaning (EN) cell was refused by the permission check, so that cell still reads "why (formal: mengapa)". |
| 7 | Split: my call; A/B if I like. | **No split.** Chapter 5 stays one unit: the charter's 13-unit plan, the catalogue's 65-block check and the unit's own tests assume it, and Sam said more words are fine. For the A/B, the teaching plan now gives two routes through the same five blocks (whole unit, or two halves: ordering, tastes and question words first, then colours, size and feelings). If the pilot shows the load is too heavy, the natural cut is 5A = tastes, question and linking words, hot, cold, food and drink (patterns 2, 4, 5) and 5B = colours, size and shape, feelings (patterns 1, 3). |
| 8 | Fix the chapter 4 opener. | Done (above). |

**Ledger update (done):**
- The sheet was written first and logged in the Journal (rows 57 to 62). Rows changed: L-0336 (place, action, note), L-0416 (Retired), L-1009 (Sam's note); new rows L-1048 to L-1050. The repo copies and the hash in `docs/step4-sources.json` follow the sheet; the changed rows were read back from the sheet and compared. The ledger now has 1,050 rows.
- The Journal and sheet are the record of Sam's decisions; Kata-Kata still needs cards for the new rows.

## Questions for Sam

1. **L-1009 «kenapa» Meaning (EN):** the permission check refused my edit of that cell. Please change it to "why (same as mengapa and apa sebab)" in the sheet if you want it (the note on the row already says so).
2. **Five proposed rows** still waiting: nasi lemak, sambal, pesan, susu, tambah (none is used).
3. **Kamus Dewan check** for L-1008 and L-1048 to L-1050.
4. **Pilot:** which route (whole unit or two halves) worked better, and did 63 words feel like too many?
5. **Chapter 6** waits for your go-ahead.
