# STEP 5c REPORT: Chapter 5, Batch 3

**Scope:** Malay A1 chapter 5 (adjectives; «bagaimana» / «macam mana»; «kenapa» and «sebab»): **unit 5** with its writing block, and the chapter 5 fast pack. Sam authorised chapter 5 on 12 Nov 2026 and pre-approved publication to main when the checks pass.

**Sources read:** the live Unified Curriculum Charter (Google Doc, read in full on 12 Nov 2026; it differs from `docs/handoff/charter-snapshot.md` only by one sentence in section 8, now copied into the snapshot), `AGENTS.md`, `HANDOFF.md`, the Kata-Kata chapter 5 file (`curriculum/reference/katakata/c05.json`), the ledger snapshot, and the chapter 4 source and report used as the model.

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests` (60 tests) pass on a full Git checkout at every commit below.

| Commit | Content |
| --- | --- |
| `05041ba` | Unit 5, chapter 5 helper, tests, retirement of Taste and colour and Size and shape |
| `3f2a710` | Chapter 5 fast-course pack |
| this commit | This report, `HANDOFF.md` and the refreshed charter snapshot |

## Word accounting

All counts are unique ledger entries. A slash variant («mahu» / «nak», «tetapi» / «tapi», «jingga» / «oren») counts once.

| Unit | Theme | New core | Dunia recognition (by scene) | Revision (not counted, not tested as new) |
| --- | --- | ---: | --- | --- |
| 5 | Tastes, colours, size and shape, feelings and states, hot and cold, food and drink, «bagaimana», «kenapa» / «sebab», «yang», «atau», «tetapi» | **60** | **50**: "Masak nasi goreng" 15, "Di klinik" 12, "Gambar bayi" 12, "Lepak di kedai mamak" 11 | 23: 15 from chapters 1 to 3, 8 from chapter 4 |

**Core load: 60 in one unit** (the charter says 20 to 40; the 13-unit plan does not split chapter 5). All 60 stay core, taught in six themed groups so no block has to carry more than two:

| Group | Words |
| --- | ---: |
| Tastes (rasa, manis, masin, masam, pedas, pahit, sedap, tawar, kurang manis) | 9 |
| Colours (warna and eleven colours) | 12 |
| Size and shape (besar, kecil, pendek, rendah, ringan, tebal, nipis, sempit) | 8 |
| Feelings and states (gembira … sakit, seronok, kelakar) | 13 |
| Hot, cold, food and drink (panas, sejuk, ais, air, air kosong, teh / kopi, nasi, mi, roti) | 9 |
| Question and linking words (bagaimana, macam mana, kenapa, sebab, yang, atau, tetapi, mahu, banyak) | 9 |

The teaching plan says to teach one or two groups per block and recycle them; the vocabulary sheet, the 13-turn model conversation and the Block E scenes keep returning to them. The load is still the heaviest of any unit so far (4A has 40). Whether to split is Sam's call after the pilot.

**Ledger check: 60, not 58.** `tests/test_step5c_suite.py` recomputes the sets from the ledger with the same rule as the chapter 4 test (a row with a "Ch5" part). That gives **60** core rows, not the 58 in the brief. Fifty-eight rows are placed "Ch5" (or "Ch5 (pending)") only. The other two are **«seronok» (L-0455)** and **«tawar» (L-0520)**: the ledger places them in chapter 5 as well as in a Dunia scene ("Cuti ke pantai" for chapter 4, "Pasar pagi" for chapter 3). Unit 4A and 3B showed them as recognition words only and never taught them, so I treat them as core here and the unit says so. If you would rather count them as revision, drop them from `TASTES` and `FEELINGS` in `suite/ms_c05.py` (and change the two numbers in the test). The 50 recognition entries match the brief exactly.

**Words reused, not new.** «sedikit» / «sikit» (L-0216, now chapter 2) and «kosong» (L-0099, chapter 3, in «air kosong») are listed under **Revision · 復習**, with 21 other chapter 1 to 4 words that return (berapa, harga, mahal, murah, tinggi, berat, panjang, lebar, pisang, mangga, cili, segar, bukan; hujan, cuaca, lambat, lewat, sudah, belum, masih, payung). The test checks that none of them is counted as core or recognition.

## Evidence for charter section 6 and section 14

| Minimum | Unit 5 | Where it is tested |
| --- | --- | --- |
| Eleven components | All eleven, plus the markers drill and the writing block | `test_components_and_vocabulary` |
| Vocabulary: every ledger word, JA and EN meaning, one example each, spoken forms marked | 133 entries (60 + 50 + 23), each with an example; «macam mana», «nak», «tapi», «oren», «tak apa», «dah», «sikit» shown as spoken | entry count = example count = ID count |
| 3 to 5 patterns, 4 to 6 Q&A each, EN and JA explanation, Japanese note | 5 patterns × 5 Q&A (frames ms-c05-f01 to f05); «Kenapa … Sebab …» sits in pattern 4 | `test_patterns` |
| Drill types 1 to 5, at least 6 items each (30+) | 8 items each (40) | `test_drills_keys_and_question_words` |
| Type 6 short dialogues (3+) | 4 | same |
| Cumulative question words | apa … berapa, bila, pukul berapa, hari apa + **«bagaimana» (spoken «macam mana»)** and **«kenapa» (answer «sebab»)**; 11 tasks with model questions; the choice drill uses bagaimana, kenapa, berapa, bila, siapa, di mana, apa and bolehkah | same |
| Tense and aspect markers return (section 14) | "Markers with adjectives": «sudah», «belum», «masih», «akan» with the new adjectives, 8 items, Japanese bridge, key | `test_markers_return` |
| Real answer keys | Every drill item, markers item, reading item and self-check item has its own answer | key regex per item |
| Model conversation 10 to 16 turns, gapped, changed facts | 13 turns at a mamak stall, gapped (5 gaps, answers in key), 13-turn variant | `test_conversation_…` |
| Listening 120 to 250 Malay words, before/during/after, 6+ items | 133 words, 9 items | same |
| Reading text with 5+ questions; guided writing with model | A mamak menu (fictional prices), 6 questions, an order slip with a model; plus the 45-minute writing block (short description, peer questions, rewrite) | same, `test_tests_and_plans` |
| Task: role cards, change of plan, success criteria | Ordering at a mamak; the dish is finished and a friend arrives | same |
| Culture note 150 to 300 words, full JA translation | 226 words, four paragraphs; no leftover English in the Japanese | word count and a Japanese-cell check |
| Test 15 to 20 items + speaking, every item tagged | 19 scored (6 listening, 7 words, 2 grammar, 4 reading) + 1 speaking; every item lists the ledger words it tests, and word items use core words only | `test_tests_and_plans` |
| Teaching plan: timings, prompts, Kata-Kata before and after | Five blocks, Sedia Kelas c05, the four Dunia scenes | same |
| Writing block after unit 5 (Stage 1 plan) | `ms-c05-writing-block`, registered in the catalogue as `ms-stage1-writing-5` | `test_legacy_retirement_and_catalogue` |
| Fast pack: 2 to 4 pages, 15 to 20 words, patterns with 2 examples | 3 content pages, 20 words, 5 patterns, a 10-turn conversation, task, 5-item self-check, self-study guide | `test_fast_pack` |

**Chapter 5 Malay rules, tested:**
- No comparatives or superlatives: no «lebih», «paling», «daripada», and «kurang» only in «kurang manis». The teacher notes name them as mentions (‹lebih›, ‹paling›, ‹kurang›, ‹daripada›, each with a ledger source) so they are not taught.
- Standard first, spoken marked: «mahu», «tetapi», «bagaimana», «jingga» come before «nak», «tapi», «macam mana», «oren»; every line with a spoken form carries a "spoken" label.
- No faith-specific greetings or expressions, no food rules, and no medicine, diagnosis or dose in the clinic words (symptoms only).
- Root verbs only; no ber- or me- forms. The build's ledger, register, affix and Malaysian-form checks pass with no exceptions for unit 5 or the fast pack.
- No word placed after chapter 5 is used (this ruled out «sangat», «sini», «kedai», «baju», «kerusi», «tolong», «sila», «hospital», «yang mana»; the unit works around them).

**Natural Malay.** The dialogues are about ordering a drink and a dish at a mamak stall, a Monday talk about the weekend, a menu, a late arrival and feeling tired. Where the in-scope words could not make a natural sentence I changed the scene: for example the Kata-Kata scenario's «nasi lemak» and «sambal» (not in the ledger) became «mi goreng» and «roti canai» (Dunia recognition words); frame ms-c05-f03's «baju» (chapter 8) became «payung», «fail», «buku» and «mangga».

**Legacy packs.** Taste and colour and Size and shape (learner pack and teaching plan each) are removed from the active catalogue; their source text stays in `curriculum/malay-course.txt`. The A2 conversation «Lunch at a Malaysian stall», which was linked from Taste and colour, stays linked from chapter 5 (`AUTHORED_LINKS` in `course.py`). Seven legacy exceptions for ms-c05 (atas, bawah, kalau, yang mana, nak, sikit, tak) are removed: **41 → 34**. The chapter 5 page status now reads "Step 5c chapter 5 suite · draft for pilot".

## Files changed

- **New:** `suite/chapter5_common.py`, `suite/ms_c05.py`, `tests/test_step5c_suite.py`, this report.
- **Changed:** `suite/__init__.py` (grammar points ms-c05-g02 to g06, scene titles, "hospital" added to the English homograph list, unit loading, glosses for «mahu», «tetapi», «kenapa»), `suite/fast.py` (chapter 5 pack), `course.py` (retired packs, chapter 5 status, the stall link), `catalogue.py` (writing block after unit 5), `curriculum/reauthored-units.json` (+ms-c05, ms-c05-fast), `curriculum/legacy-exceptions.json` (seven removed), `curriculum/malay-mentions.json` (‹teh O›, ‹jambu›, ‹hospital›, ‹lebih›, ‹paling›, ‹kurang›, ‹daripada›, each with its source), `curriculum/malay-proper-nouns.json` (Rashid, Jalur Gemilang), `tests/test_catalogue.py` (retired titles), `tests/test_language_checks.py` (its "not yet re-authored" fixture moves from ms-c05 to ms-c06), `docs/handoff/charter-snapshot.md` (the faith-expression sentence), `HANDOFF.md`, and the generated files in `dist/` and `docs/step4-authored-scope.json`.
- **Not changed:** the ledger, the Kata-Kata reference files, and the legacy lesson sources.

## Proposed ledger rows (not added; waiting for Sam)

None of these is needed to finish chapter 5; each would let a mamak scene say something people actually say. Each needs the Kamus Dewan check.

| Word | Meaning | Proposed chapter | Why |
| --- | --- | --- | --- |
| nasi lemak | rice cooked in coconut milk | 5 | The Kata-Kata chapter 5 scenario orders it; the unit uses «mi goreng» and «roti canai» instead |
| sambal | chilli paste | 5 | The same scenario asks «Sambalnya pedas?»; the natural pairing with «pedas» |
| pesan | to order (food, a drink) | 5 | The verb for placing an order; the unit uses «Saya mahu …» |
| kari | curry | 5 | «roti canai» is eaten with it; the ledger gloss already says "with curry" |
| susu | milk | 5 | «teh O» is "without milk" in the card note, so the word explains the contrast |
| tambah | to add, more | 5 | «Tambah ais», «Tambah gula» at the counter |

## Real-world facts used, and their sources

| Fact (unit 5 culture note) | Source checked | Rank | Status |
| --- | --- | --- | --- |
| The national flag, the Jalur Gemilang, is red, white, blue and yellow (the note says nothing else about the flag) | CIA World Factbook, Malaysia, "Flag description": 14 red and white stripes, a blue canton with a yellow crescent and star (seen in a search summary; the page itself was not opened) | 2 | [VERIFIED] via the summary |
| Malaysia is hot and humid throughout the year | Encyclopaedia Britannica, "Malaysia: Climate"; FAO climate summary (search summaries) | 3 | [VERIFIED] in general; **not checked against MetMalaysia**, whose page the search did not return |
| ‹teh O› is tea without milk; «merah jambu» is literally "jambu-fruit red"; «yang merah» is "the red one"; «nak» is spoken; «kosong» means zero or empty | Kata-Kata cards ms-c05-055, -025, -004, -005 and -054 | Sam's reference | [VERIFIED] against the card notes |
| «kopi O» is black coffee with sugar; a «mamak» stall is a casual eatery, often open late; «tapau», «makan sini» and «Kira!» | Ledger L-0936, L-0931, L-0937, L-0938, L-0941 (Vocab Bank v4) | Sam's reference | Taken from the ledger as written; not independently checked |
| An order is built as drink, sweetness, hot or cold, ice | Kata-Kata frame ms-c05-f05 and scenario ms-c05-s01 to s11 | Sam's reference | As in Kata-Kata |

No dated, legal or faith-related facts are in the unit. The ledger's gloss for «mamak» says "Indian-Muslim eatery"; I did not print "Muslim" in learner text (the brief says to ask before anything religious, including food rules). See question 3.

## Unverified and provisional

- **All Malay example sentences are mine.** They pass the ledger, register, affix and Malaysian-form checks, but none has had a native read. Please look especially at: «Harga mangga rendah hari ini.», «Saya takut ribut.», «Teh ini tawar.» (unsweetened), «Kopi ini tawar, tetapi sedap.», «Ada yang tidak pedas?», «Encik rasa bagaimana hari ini?», «Puan mahu gula sedikit?», «Mi goreng (pedas)» and «Teh dan kopi: kurang manis, boleh.» on the menu, and «Muka dia macam muka saya.» [UNVERIFIED]
- **Usage statements in the culture note, not checked against a source:** at the counter you often hear «nak» for «mahu»; «panas» and «sejuk» are everyday words for weather and drinks. The Japanese customisation comparison (甘さ控えめ、氷少なめ) is general knowledge, not sourced. [UNVERIFIED]
- **«oren» and «jingga».** The unit teaches «jingga» as the standard form and «oren» as spoken, following the brief. The ledger lists «oren / jingga» (oren first) and the KD4 pages for both (p.2952 and p.1669) show both as headwords; no note says which is standard. [UNVERIFIED]
- **«rumah sakit».** The ledger keeps it as a Dunia recognition word. It is the usual Indonesian term; Malaysians say «hospital» (ledger L-0336, chapter 7). The vocabulary line says so with ‹hospital› as a mention, and the teacher notes say recognise only. [UNVERIFIED; see question 4]
- **«tawar».** The ledger says "to bargain; bland" and the Kata-Kata card says "bland, unsweetened". The unit teaches "bland, unsweetened" and points back to chapter 3 for "to bargain" («Boleh tawar?»).
- **Without «ke».** «pergi klinik» and «pergi pasar» follow the chapter 4 decision (no «ke» before chapter 7).
- **«kenapa» and «mengapa».** The ledger meaning says "formal: mengapa". «mengapa» is me- shaped and is not taught or quoted; it is not in Kata-Kata either.
- **Kamus Dewan check** is still pending for «kelakar» (L-1008) and «kenapa» (L-1009) (ledger actions), and for L-0983 to L-1047 in general.
- **Japanese:** all of it is a draft for native review, including the full culture-note translation.
- **In class:** timings, drill load, the 60-word unit and the writing block have not been taught.
- All prices, menus, names and situations are fictional and labelled so.

## Findings for Kata-Kata (not changed here)

- **Frame ms-c05-f03** uses «baju» (ledger chapter 8): «Saya mahu baju yang biru.»
- **The chapter 5 scenario "At the mamak"** uses «nasi lemak» and «sambalnya» (not in the ledger) and the title says «kedai mamak» (ledger chapter 7).
- **Card ms-c05-008 «sedikit / sikit»** is still a chapter 5 card although the ledger moved L-0216 to chapter 2, and the Sedia Kelas c05 list still includes it (already noted in `HANDOFF.md`).
- **No cards or frame yet for «kenapa» (L-1009), «sebab» (L-0688) and «kelakar» (L-1008).** Cikgu Sensai teaches «Kenapa …? Sebab …» under ms-c05-f04 for now; a frame such as ms-c05-f06 «Kenapa ___? Sebab ___.» is proposed.
- **«rumah sakit»** (Dunia "Di klinik"): the form Malaysians usually say is «hospital».
- **Card ms-c05-020 «oren / jingga»** has no note on which form is standard.
- **Card ms-c05-015 «tawar»** has only the "bland" sense; the ledger row has both.
- **Dunia "Lepak di kedai mamak":** the ledger gloss for «mamak» includes a religious descriptor; see question 3.

## Found in chapter 4 (not changed here)

The Japanese line of the opener in units 4A and 4B still has a leftover English "and" («"Hujan petang" and "Cuti ke pantai"»), because the helper copies the English scene list into the Japanese line. Chapter 5 fixes this in `chapter5_common.py` with a separate Japanese scene list. I did not touch chapter 4; the fix is two lines in each unit if Sam wants it.

## Questions for Sam

1. **Core count.** The ledger gives 60 core rows for chapter 5, not 58: «seronok» and «tawar» are also placed in chapter 5. I taught them as core (they were only recognition words in 4A and 3B). Keep that, or treat them as revision?
2. **«oren» and «jingga».** Is «jingga» the standard form and «oren» the spoken one, as I taught?
3. **«mamak» and religion.** The ledger gloss says "Indian-Muslim eatery". I left that out of learner text and wrote nothing about halal or food rules. May the culture note say who traditionally runs a mamak stall, or should it stay silent?
4. **«rumah sakit».** Keep it as a recognition word with the «hospital» note, or ask Kata-Kata and the ledger to swap it for «hospital» (a chapter 7 word)?
5. **Proposed rows:** nasi lemak, sambal, pesan, kari, susu, tambah.
6. **«kenapa».** Shall «mengapa» stay out until chapters 10 and 11? Shall Kata-Kata add a frame for «Kenapa …? Sebab …»?
7. **Load.** Is a 60-word unit acceptable after teaching it, or should chapter 5 split as 5A tastes and colours, 5B size, feelings and ordering?
8. **Chapter 4 opener.** May I fix the leftover English in the 4A and 4B Japanese opener lines?
9. **Chapter 6** waits for your go-ahead.
