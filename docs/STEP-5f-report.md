# STEP 5f REPORT: Chapter 8, Batch 6

**Scope:** (1) the unit 7 follow-ups from Sam's answers to the step 5e review, including the unit 7 writing block ("directions by message"); (2) Malay A1 chapter 8 (penjodoh bilangan, classifiers): **unit 8** and the chapter 8 fast pack. Sam authorised the batch on 12 Nov 2026 and pre-approved publication to main when the checks pass. Nothing from chapter 9 was started.

**Sources read:** `AGENTS.md`, `HANDOFF.md` (in full, including "Quality rules for chapter 4 onward"), the charter (`docs/handoff/charter-snapshot.md`, as refreshed on 12 Nov 2026; the live Google Doc was not opened in this session, so any later change is not reflected), the Kata-Kata chapter 8 file (`curriculum/reference/katakata/c08.json`), the ledger (read from the Google Sheet: Journal rows 60 to 70 and the rows for L-0318, L-0342, L-0620 and L-1050 to L-1058 at the start; the whole Ledger tab, A1:T1064, after my additions), and chapters 7, 6 and 5 (source, helper, tests, report) as models.

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests` (111 tests) pass on a full Git checkout at every commit below (after `pip install pymupdf fonttools`, `apt-get update`, `apt-get install fonts-noto-cjk` and `git fetch --unshallow`). Every commit was fetched, rebased on `origin/main` (no changes had landed there) and pushed to `main`; I created no other branch.

| Commit | Content |
| --- | --- |
| `41dd100` | Unit 7 follow-ups: «terus» for «jalan lurus»; «sesak» core beside «jam»; ledger rows L-1059 to L-1063; both repo copies and the hash regenerated; «tumpang tanya» as revision; tests |
| `4b828aa` | Unit 7 writing block "Directions by message" (`ms-c07-writing-block`, registered as `ms-stage1-writing-7`) |
| `2ca2d48` | Unit 8 (helper `suite/chapter8_common.py`, `suite/ms_c08.py`, `tests/test_step5f_suite.py`, registration, mentions, grammar points) |
| `a48808f` | Chapter 8 fast-course pack |
| next commit | This report and `HANDOFF.md` |

## Part 1: unit 7 follow-ups

| Sam's answer (step 5e review) | What I did |
| --- | --- |
| 1. «jalan lurus» is not used for directions. Say «terus», «jalan terus», «pergi terus», «terus depan». Keep «lurus» (L-0318) only as the adjective | Every «jalan lurus» is gone from unit 7 (vocabulary, patterns, model conversation and variant, listening, reading, task, test, writing, teacher notes, the Japanese cells) and from the chapter 7 fast pack. «lurus» is now taught as "straight (of a road or line); for directions say «terus»" with the example «Jalan ini lurus.» «terus» (L-1060) is core: «Jalan terus, kemudian belok kanan di lampu isyarat.», «Pergi terus.», «Terus depan. Hospital di seberang gereja.» The pattern 3 explanation says «lurus» is not used to say go straight on. A new test (`test_no_jalan_lurus_for_directions`) fails if «jalan lurus» appears in any Malay line and requires 25 or more uses of «terus». A grep of the repository finds «jalan lurus» only in explanations of why it is not used, in this test, in the ledger notes, in the unfixed Kata-Kata file `c07.json`, and in the (historic) step 5e report. The charter table (chapter 7 pattern «Jalan lurus, kemudian belok ___») needs the same fix: see "Questions" |
| 2. Traffic: «kalau tidak jam / sesak» | «sesak» (L-0620) is core in "Landmarks and transport" beside «jam» (spoken, L-0342). Both vocabulary entries show «kalau tidak jam / sesak»; pattern 5 says «jam» alone could be heard as an hour and pairs it with «sesak»; the lines use both: «kalau tidak sesak» (model conversation), «kalau jalan tidak sesak» (variant), «Jangan naik teksi pagi ini, jalan sesak.» (listening), «kalau tidak jam / sesak» and «Kalau jam / sesak, lebih lama.» (pattern 5). Spoken «jam» lines are labelled (test `test_jam_and_sesak_taught_together`) |
| 3. «gurdwara» spelling confirmed; no word for a Buddhist temple; «tokong» stays | Teacher notes updated (they used to say the question was open). Journal row 73 records it |
| 4. "Di, ke and dari" stays retired | No change |
| 5. «tumpang tanya» is L-0019 (chapter 1): use as revision | Added to the revision list (chapter 1, politeness) and used: «Maaf, tumpang tanya, bank di mana?» opens the model conversation, the variant, pattern 3, the task key and the fast pack. No new row |
| 6. Add «kilometer», «terus», «tangga», «jangan», «sebulan» (chapter 7) to the sheet first, with Journal entries from row 71, then regenerate both copies and the hash | **Done in that order.** Rows L-1059 to L-1063 appended to the Ledger tab (Review status Draft, KD4 "Not yet checked", "Ch7 (pending)", "Claude (Sam approved)"); one cell corrected after writing (L-1059 note: meter is L-0152). Journal rows 71 to 74 (the five rows; «tumpang tanya»; «gurdwara»; the Kata-Kata finding on ms-c07-024). The copies were regenerated from the sheet (Ledger!A1:T1064: the header and L-0001 to L-1063): `malay-ledger.csv` (LF) and `ledger-snapshot.csv` (CRLF). The only differences from the earlier copies are the five new rows and the three rows Claude had changed (L-0318, L-0342, L-0620). The hash in `docs/step4-sources.json` is `781cb4b6…6e15` (1,063 ledger rows). Used naturally: «Jalan terus, kemudian belok kanan», «Naik tangga ke tingkat dua.», «Jangan belok kiri di sini.», «Lebih kurang dua kilometer.», «Tiga ribu ringgit sebulan.» «sebulan» is taught as a whole word (no productive ‹se-› drill) |
| 7. Write the unit 7 writing block | Written: 45-minute Skills block `ms-c07-writing-block`, title "Writing block · Directions by message", registered in the catalogue as `ms-stage1-writing-7` (status "pilot draft"). Model: a message asking the way and a reply with a route, a landmark, a «lebih kurang» distance, a time in «minit» and one «jangan». Three-part task (read and mark the model; write a question and swap for a reply; check and answer), five-item peer check, model answer in the key. Tested |

**Unit 7 counts after the follow-ups.** The ledger copy places **64** rows in chapter 7 (53 as handed over, the five places-of-worship rows, «sesak», and L-1059 to L-1063). Two are not new core (L-0592, a duplicate of L-0330, and L-0304, the same «depan» as L-0173), so **62 core** (was 56): position words 13; distance, time and direction 11 (adds «kilometer», «sebulan»); turning and moving 11 (adds «terus», «jangan»); landmarks and transport 23 (adds «tangga», «sesak»); compass points 4. Dunia recognition 33 (unchanged). Revision 44 (adds «tumpang tanya»). The teacher notes' A/B cut still stands: position, distance, direction and turning words first; landmarks, transport and compass points second. It is now the heaviest unit by a clear margin (62 words), which the pilot should judge. The unit 7 listening was rewritten (19 turns, 163 Malay words, nine questions) so that it contains «terus», «jangan», «tangga», «sesak», «kilometer» and «sebulan» in a natural scene (a newcomer walking to the office, asking about rent near the station).

## Part 2: chapter 8

## Word accounting

All counts are unique ledger entries. A slash variant counts once.

| Unit | Theme | New core | Dunia recognition | Revision (not counted, not tested as new) |
| --- | --- | ---: | ---: | ---: |
| 7 (after the follow-ups) | Places and directions | 62 | 33 | 44 |
| 8 | Classifiers (penjodoh bilangan) | **35** | **11**: "Beli baju" | 53 |

**Ledger check for chapter 8.** The ledger copy places **54** rows in chapter 8. `tests/test_step5f_suite.py` recomputes the sets from the ledger:

- **Core, 35:** first placed in chapter 8 and carrying a chapter 8 card. These are L-0343 to L-0376 (34 rows) and **«baju» (L-0500)**, which is both the first Dunia "Beli baju" card and chapter 8 card ms-c08-031. «baju» is therefore core, not recognition.
- **Dunia recognition, 11:** the other "Beli baju" rows (L-0501 to L-0511: seluar, stokin / stoking, topi, beg, butang, saiz, cuba, longgar, ketat, batik, corak).
- **Placed in chapter 8 and earlier, 8 rows:** «orang» (L-0058, chapter 2), «surat» (L-0426), «payung» (L-0437), «buku» (L-0487), «kaki» (L-0488), «buah» (L-0514), «ikan» (L-0515) and «kertas» (L-0524). They carry a chapter 8 card but were placed earlier, so they are revision. «orang» and «buah» are taught as counters in revision with a new use; the others return as the things counted. 34 + 1 + 11 + 8 = 54.

**Core load: 35 in one unit** (charter: 20 to 40 typically; the 13-unit plan has one unit for chapter 8), plus 11 recognition words. Groups:

| Group | Words | N |
| --- | --- | ---: |
| Classifiers | ekor, biji, batang, helai, keping, pucuk, kuntum, pasang, ulas, naskhah, **seekor, sebiji, sebuah** | 13 |
| Containers and portions | bungkus, cawan, pinggan, mangkuk, botol, tin, kotak | 7 |
| The things counted | kucing, ayam, telur, pen, pokok, gambar, surat khabar, bunga, kasut, sup, tisu, baju | 12 |
| All, please and takeaway | semua, tolong, Makan sini atau bungkus? | 3 |

The teacher notes give the A/B cut if the pilot shows 35 is too many: «ekor», «biji», «batang», «helai», «orang», «buah», the three whole words, the containers and «semua», «tolong» first; «keping», «pucuk», «kuntum», «pasang», «ulas» and «naskhah» second.

**Revision, 53 (four labelled groups).** Manners, numbers and money (22: «terima kasih», «sama-sama», «jumpa lagi», «hati-hati», «Pak cik», «satu», «dua», «tiga», «sepuluh», «dua puluh», «berapa», «harga», «ringgit», «sen», «baki», «bayar», «beli», «tunai», «jumlah», «cukup», «mahal», «murah»); the market and shop (11: «orang», «buah», «pasar», «kedai», «ikan», «segar», «epal», «surat», «buku», «kertas», «payung»); food, drink and the «mamak» stall (12: «mi», «goreng», «roti canai», «roti», «teh tarik», «air», «air kosong», «kuah», «kurang manis», «tapau», «makan sini», «mamak»); colours, sizes and wanting (8: «merah», «biru», «putih», «hitam», «besar», «kecil», «mahu / nak», «atau»). A test (`test_revision_words_really_return`) fails if a revision word is not used in a marked Malay line outside the vocabulary list, so the list is not padding; it removed «mangga» and «bawang» from my first draft because the scenes did not use them. **Earlier units deliberately avoided counters**: unit 3B has «dua epal» and unit 5 has «Mi goreng satu» and «roti canai dua». Those stay as they are (everyday speech); unit 8 shows the counter form beside them («dua biji epal», «satu pinggan mi goreng») and the vocabulary entries for «tiga biji epal», «dua cawan teh tarik» and «dua biji epal» carry "everyday speech: «tiga epal» / «dua teh tarik» / «dua epal»".

## Evidence for charter section 6 and section 14 (unit 8)

| Minimum | Unit 8 | Where it is tested |
| --- | --- | --- |
| Eleven components | All eleven, plus the markers drill. No extra block (the Stage 1 plan gives none) | `test_components_and_vocabulary` |
| Vocabulary: every ledger word, JA and EN meaning, one example each, spoken forms marked | 99 entries (35 + 11 + 53), each with an example; «tapau» and «mahu / nak» marked spoken; «orang» and «buah» marked as counters; «naskhah» marked written | entry count = example count = ID count |
| 3 to 5 patterns, 4 to 6 Q&A each, EN and JA explanation, Japanese note | 5 patterns × 6 Q&A, one per Kata-Kata frame: f01 «Saya mahu» + number + counter + noun; f02 «seekor» / «sebiji» / «sebuah» and «satu» + counter; f03 «Berapa» + counter; f04 price per counter and «semua»; f05 «Tolong bungkus» and «Makan sini atau bungkus?» | `test_patterns` |
| Drill types 1 to 5, at least 6 items each (30+) | 8 items each (40) | `test_drills_keys_and_question_words` |
| Type 6 short dialogues (3+) | 4 | same |
| Cumulative question words | all earlier ones + **«berapa» with a counter** («Berapa biji?», «Berapa ekor?», «Berapa orang?»); 17 tasks with model questions, each checked; the Q&A drill asks «Berapa biji telur?» and «Berapa orang?»; the choice drill contrasts «Berapa» (a count) with «Berapa» (a price) | same |
| Tense and aspect markers return (section 14) | "Markers with buying and counting": «sudah», «belum», «masih», «akan», «baru» with «beli», «bayar», «ada», «ambil»; 8 items, Japanese bridge, key | `test_markers_return` |
| Real answer keys | Every drill item, markers item, reading item and test item has its own answer | key regex per item |
| Model conversation 10 to 16 turns, gapped, changed facts | 11 turns (fish, eggs and a chicken at the morning market), 5 gaps (answers in the key), 11-turn variant at a stationery stall with different things and prices | `test_conversation_…` |
| Listening 120 to 250 Malay words, before/during/after, 6+ items | 124 words (a flower stall, then a «mamak» stall with «Makan sini atau bungkus?»), 9 items. The margin over 120 is small | same |
| Reading text with 5+ questions; guided writing with model | A price board (fictional), 7 questions; a three- or four-sentence order with a model | same |
| Task: role cards, change of plan, success criteria | Ordering at a «mamak» stall (eat here and take away); halfway «Dua orang kawan datang. Dua cawan teh tarik lagi, tolong.» and B gives the new total | same |
| Culture note 150 to 300 words, full JA translation | 184 words, four paragraphs; no leftover English in the Japanese | word count and a Japanese-cell check |
| Test 15 to 20 items + speaking, every item tagged | 19 scored (6 listening, 6 words, 3 grammar, 4 reading) + 1 speaking; word items use core words only | `test_tests_and_plans` |
| Teaching plan: timings, prompts, Kata-Kata before and after | Five blocks, Sedia Kelas c08 (13 cards, frames f01 and f02), the Dunia scene "Beli baju" | same |
| Fast pack: 2 to 4 pages, 15 to 20 words, patterns with 2 examples | 3 content pages, 20 words, 5 patterns × 2 examples, 10-turn conversation, task with change of plan, 5-item self-check, self-study guide | `test_fast_pack` |

**Chapter 8 Malay rules, tested:**
- **Whole words only.** «seekor», «sebiji» and «sebuah» are core ledger words (each used 3 or more times). A test fails if any marked Malay span contains another fused counter («sebatang», «sehelai», «secawan» …). «satu» + counter is used throughout (10 or more uses; «satu batang pen», «satu helai baju», «satu pinggan mi goreng»). ‹sebatang› and ‹sehelai› appear only as ‹…› mentions, with their Kata-Kata card notes (ms-c08-005, -006) in `curriculum/malay-mentions.json`.
- **The counter dropped in everyday speech** («dua teh tarik», «roti canai tiga», «tiga epal») is marked "everyday speech" in pattern 5, the vocabulary examples, the culture note and the teacher notes (tested). The careful form is what the task key and the models use.
- **Standard first, spoken marked.** «mahu» first, «nak» spoken; «bungkus» first, «tapau» spoken (the Q&A line that uses it says "(spoken)"); a test fails if «nak», «tapi», «sikit», «dah», «tak», «senang», «saja» or «tapau» sits on a line without a spoken label.
- **Malaysian, never Indonesian:** «kasut», «beg», «stokin / stoking», «tisu», «sup», «epal»; «koran», «apel», «kantong», «toko» and the earlier look-alikes are banned by test and by the build.
- **No ber- or me- verbs** (the build's affix check passes with no exceptions); the root verbs «beli», «bayar», «bungkus», «goreng», «cuba», «hantar».
- **No faith-specific expressions and no food rules** (regex test). Nothing religious was added.
- **Nothing placed after chapter 8 and nothing missing from the ledger** (the build fails on either in a re-authored unit). Words that were out of reach are listed under "Proposed ledger rows".

**Natural Malay.** Where the in-scope words could not make a natural sentence I changed the scene, not the Malay:
- The Kata-Kata scenario uses «nasi lemak» (not in the ledger), so the mamak scenes use «roti canai dengan kuah» and «teh tarik» (ledger L-0935, L-1048, L-0934). The scenario's totals are not used; all prices are mine and a test checks that they add up (35, 19, 40, 14.50 with 5.50 change, 17 and 24).
- The flower stall and the egg and fish stall are two separate stalls with two separate sellers, not one conversation.
- «Berapa orang?» is shown as what restaurant staff ask at the door.
- «naskhah» and «pucuk» are taught because the ledger has them, but the examples are plain («satu naskhah surat khabar», «satu pucuk surat») and the entry says they are mostly written; no scene depends on them.

**Dunia scene "Beli baju".** The 11 words are for recognition only (Block E). «Saiz berapa?», «Boleh saya cuba baju ini?», «Baju ini ketat.» and «Seluar ini longgar.» appear as chunks in the vocabulary examples; none is tested as new vocabulary (tested).

## Files changed

- **New:** `suite/chapter8_common.py` (copy of the chapter 7 helper: ms-c08 ids, `GRAMMAR8`, «berapa» with a counter added to the question words, "Markers with buying and counting", the "Beli baju" scene, Sedia Kelas c08), `suite/ms_c08.py`, `tests/test_step5f_suite.py` (18 tests), this report.
- **Changed:** `suite/ms_c07.py`, `suite/fast.py` (chapter 7 changes, chapter 8 pack), `suite/ms_c06.py` (one teacher note), `suite/__init__.py` (grammar points ms-c07 labels and ms-c08-g02 to g06, GLOSS for L-1060 and L-1063, English homographs «kilometer», «pen», «tin», «batik», unit loading, "Beli baju" as a scene title), `course.py` (chapter 8 status), `catalogue.py` (`writing-7`), `curriculum/reauthored-units.json` (+ms-c08, ms-c08-fast), `curriculum/malay-mentions.json` (+‹sebatang›, ‹sehelai›, ‹nasi lemak›, ‹penjodoh bilangan›), `curriculum/malay-proper-nouns.json` (+Rina), both ledger copies and `docs/step4-sources.json`, `tests/test_step5e_suite.py`, `tests/test_language_checks.py` (its "not yet re-authored" fixture moves from ms-c08 to ms-c09), `HANDOFF.md`, and the generated files in `dist/` and `docs/step4-authored-scope.json`.
- **Not changed:** the charter snapshot, the Kata-Kata reference files, the legacy lesson sources, `legacy-exceptions.json` (still 30; nothing retired because chapter 8 had no legacy packs).
- **The ledger sheet was changed by me:** rows L-1059 to L-1063 and Journal rows 71 to 74 (Sam's approval in the brief), as above. I changed no other row.

## Proposed ledger rows

Words the chapter 8 scenes could not use. None is used. Each would be "Not yet checked" for Kamus Dewan; I added none.

| Word | Meaning | Why |
| --- | --- | --- |
| nasi lemak | coconut rice dish | The Kata-Kata chapter 8 scenario and frame f05 use it (the usual takeaway order); today the scenes use «roti canai dengan kuah» |
| gerai | stall (food or market) | The natural word for a market or food stall; the scenes use «kedai» and «mamak» |
| tambah | to add; extra | «Tambah satu teh tarik» is how people add to an order; the task uses «lagi» («Dua cawan teh tarik lagi, tolong.») |
| (meaning edit) L-0488 kaki | add "counter: umbrellas" | Kata-Kata card ms-c08-010 teaches «kaki» as the counter for umbrellas («sekaki payung» in the card note); the ledger has only "foot, leg", so the counter use is not taught |
| (meaning edit) L-0514 buah | add "counter: large or general things" | Card ms-c08-003; the ledger has only "fruit". The unit teaches the counter use in revision and says so |

## Real-world facts used, and their sources

| Fact | Source checked | Rank | Status |
| --- | --- | --- | --- |
| The counter is often dropped in everyday speech at a stall («dua teh tarik», «roti canai tiga»); the careful form keeps it | Sam's brief of 12 Nov 2026 and the earlier units' use of «Mi goreng satu» and «dua epal» | Sam's reference | Taken from the brief; Kamus Dewan not opened |
| «ekor» lit. tail, «biji» seed, «batang» stem, «helai» strand, «kuntum» bud, «pucuk» shoot | Kata-Kata chapter 8 cards ms-c08-002, -004, -005, -006, -009, -008 (the "lit." glosses) | Sam's reference | [VERIFIED] against the cards; none of these etymologies is in the ledger's "Sam's notes", so none is a corrected note |
| «Makan sini atau bungkus?» is heard at food stalls | Kata-Kata card ms-c08-043 note ("Heard at every food stall"); the note says "food stalls", not "every" | Sam's reference | [VERIFIED] against the card; no wider claim |
| «tapau» is a spoken word for taking food away | Ledger L-0937 (Dunia "Lepak di kedai mamak"); the ledger gloss only | Sam's reference | Gloss only; no usage source |
| Unit 7: «terus», «jalan terus», «pergi terus», «terus depan» for straight on; «kalau tidak jam / sesak» | Sam's brief of 12 Nov 2026 and ledger Journal rows 68 to 70 | Sam's reference | Recorded in the ledger |
| Unit 7 (unchanged): traffic keeps to the left; the 2020 census groups | As in the step 5e report (secondary sources only; no percentages) | 3 | Still open (question 3) |

The unit 8 culture note makes no claim about any real stall, price, law or custom beyond the rows above. All stalls, prices, names and totals are fictional and labelled so.

## Unverified and provisional

- **All Malay example sentences are mine.** They pass the ledger, register, affix and Malaysian-form checks, but none has had a native read. Please look especially at: «Ikan ini berapa seekor?», «Telur lima puluh sen sebiji.», «Ayam besar, empat belas ringgit seekor.», «Bunga ini berapa satu kuntum?», «satu kuntum» and «satu pasang» (the «satu» + counter form for counters I do not fuse), «Saya goreng tiga ulas bawang putih.», «Saya makan dua keping roti pagi ini.», «Saya hantar satu pucuk surat.», «Saya beli satu naskhah surat khabar.», «Dia beli dua tin air.», «Sebuah buku dan sebiji epal.», «Ada lagi?» / «Cukup, terima kasih.», «Boleh bungkus?» (for flowers), «Roti canai dengan kuah?», «Dua teh tarik kurang manis, tolong.», «Hari ini ramai orang.», «Meja untuk tiga orang.», «Berapa orang?» (as the restaurant question), «Dua orang kawan datang. Dua cawan teh tarik lagi, tolong.», «Tunai sahaja. Terima kasih. Datang lagi.» on a price board, «Pak cik» to a stallholder; and in unit 7 «Jangan naik teksi pagi ini, jalan sesak.», «Kalau jam / sesak, lebih lama.», «Berapa sewa sebulan?» and «Naik lif atau naik tangga» [UNVERIFIED]
- **Register of «pucuk» and «naskhah»** ("mostly written", spoken «satu surat» / «surat khabar» alone) is my reading, not checked in Kamus Dewan. So is the idea that «sesak» is the form to read where «jam» is spoken; the ledger only marks «jam» as spoken.
- **«terus» meaning "directly"** (ledger gloss) is not exemplified anywhere; only "straight on" is taught.
- **Fused counters.** Whether «tiga ulas bawang putih», «dua keping roti» and «satu pasang kasut» are the most natural wordings (against «tiga biji», «dua helai roti» or «sepasang») is not checked.
- **The ledger's Japanese for L-0931 «mamak»** reads ママッ（…）, which looks like a truncated ママック; I overrode it in the unit (ママック) and did not edit the ledger.
- **The Japanese** (all cells, including the full culture-note translation, 助数詞 glosses such as 〜匹 / 〜個 / 〜枚 / 〜本 for each counter, and the bridges 何個 / 何匹 / 何枚) is a draft for native review; the counter glosses are general knowledge, not sourced.
- **In class:** timings, drill load, 62 words in unit 7 and 35 + 11 in unit 8 have not been taught.
- **Kamus Dewan check** is still pending for L-0983 to L-1063.
- **Layout.** The pattern pages are dense; the pack-fit check passes for all 304 packs.

## Findings for Kata-Kata (not changed here)

- **Unit 7:** card ms-c07-024 («lurus», note) and its frame still teach «jalan lurus»; Sam: «terus», «jalan terus», «pergi terus» and «terus depan» (Journal rows 68 and 74). Cards are also needed for L-1059 to L-1063, L-0620 (it has only a Jambatan card) and the five places-of-worship rows.
- **Chapter 8 scenario "Morning market and takeaway" (ms-c08-s01 to s11)** uses «nasi lemak» (not in the ledger).
- **Frame ms-c08-f05** («Tolong bungkus (number) ___.») uses «nasi lemak» in its example.
- **Frames f02 and f04** («se-(counter) (noun)» and «___ ringgit se-(counter)») and the examples «sekuntum», «sebatang», «seulas», «senaskhah», «sepasang» show productive ‹se-› with every counter. Sam's rule for this step: only «seekor», «sebiji» and «sebuah» are whole words; the others are «satu» + counter. The frames need a decision (see question 2).
- **Card ms-c08-010** (kaki, "counter: umbrellas") conflicts with ledger L-0488 (foot, leg); **ms-c08-003** (buah, "counter: large or general objects") with L-0514 ("fruit"); **ms-c08-001** (orang, counter) with L-0058.
- **Cards ms-c08-005 and -006** show ‹sebatang› and ‹sehelai› in their notes, so those words are named only as mentions here.
- **Card ms-c08-008** (pucuk) glosses "letters, guns"; the unit teaches letters only.
- **Card ms-c08-019** (tin) has no note or example; **ms-c08-013** (naskhah) has «senaskhah surat khabar», which looks formal.
- **Card ms-c08-043** has the only usage note in the chapter ("Heard at every food stall").
- **Card ms-c08-031** (baju) duplicates the first Dunia "Beli baju" card (L-0500); the ledger counts it once, as core.
- **Sedia Kelas c08** (13 cards, frames f01 and f02, scene "pakaian-kedai") works as the pre-class set.

## Questions for Sam

1. **Chapter 9 waits for your go-ahead.** Also, how should the "Rumah terbuka Hari Raya" scene be handled? I did not look at it or start chapter 9; you said you will decide.
2. **Productive ‹se-› in the Kata-Kata frames.** Frames f02 and f04 (and the card examples) teach ‹sekuntum›, ‹sebatang›, ‹sehelai› and the like. The unit teaches only «seekor», «sebiji», «sebuah», and says «satu» + counter for the rest, as you asked. Should Kata-Kata change its frames to match, or should the unit teach more fused forms later (for example from chapter 10)?
3. **Still open from the step 5e report:** the left-hand traffic and census sentences in the unit 7 culture note (keep, or leave out until you have read the primary sources?); retire L-0592 «pintu masuk» and merge L-0304 into L-0173?; «hospital» and «kapal terbang» (chapter 7 cards, placed in chapters 5 and 4); the Kamus Dewan check for L-0983 to L-1063; the L-0188 «sekali» meaning edit.
4. **Proposed rows:** add «nasi lemak», «gerai», «tambah»? Without them the scenes use «roti canai», «kedai» and «lagi». And do you want the two meaning edits (L-0488 kaki and L-0514 buah gain their counter sense)?
5. **Charter edits (read-only to me).** The chapter 7 pattern in the chapter table reads «Jalan lurus, kemudian belok ___»; it should read «Jalan terus, kemudian belok ___». The chapter 8 pattern «se-(counter) (noun)» should become «(number) (counter) (noun); seekor, sebiji, sebuah» if you agree with question 2.
6. **Register labels.** Please confirm, or correct, that «pucuk» and «naskhah» are mostly written, that «tapau» is the spoken word for «bungkus», and that «sesak» is the word to read where «jam» is spoken.
7. **Load.** Does the heaviest pair feel too much: 62 core words in unit 7 (A/B cut in the teacher notes) and 35 + 11 in unit 8? Which groups of unit 7 should be taught second?
8. **Ledger Japanese for L-0931.** ママッ… looks truncated. May I correct it to ママック in the sheet?
9. **Pilot:** please teach the unit 7 writing block (does the three-part task fit 45 minutes?) and unit 8, and say whether the 124-word listening and the two-stall scene feel natural.
