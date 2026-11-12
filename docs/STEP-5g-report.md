# STEP 5g REPORT: Chapter 9, Batch 7

**Scope:** (1) the unit 8 follow-ups from Sam's answers to the step 5f questions, including six new ledger rows and the correction of the «se-» rule; (2) Malay A1 chapter 9 (the passive «di-», signs and notices): **unit 9** and the chapter 9 fast pack, with the "Rumah terbuka Hari Raya" scene turned into a general «rumah terbuka» (open house) scene with a short note for each festival. Sam authorised the batch on 12 Nov 2026 and pre-approved publication to main when the checks pass. The stage review and the A1 test were not started; they wait for Sam.

**Sources read:** `AGENTS.md`, `HANDOFF.md` (in full, including "Quality rules for chapter 4 onward"), the charter (the live Google Doc was read; its chapter 7, 8 and 9 rows match `docs/handoff/charter-snapshot.md`), the Kata-Kata chapter 9 file (`curriculum/reference/katakata/c09.json`), the ledger (read from the Google Sheet: the whole Ledger tab twice, A1:T1070 at the start and A1:T1076 after my additions, and Journal rows 60 to 82), and chapters 8 and 7 (source, helper, tests, report) as models.

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests` (130 tests) pass on a full Git checkout at every commit below (after `pip install pymupdf fonttools`, `apt-get update`, `apt-get install fonts-noto-cjk` and `git fetch --unshallow`). Each commit was fetched, rebased on `origin/main` (nothing had landed there), pushed to `main`, and the session branch `claude/serene-feynman-3x1cq2` was pushed to the same commit so it stays in step with main.

| Commit | Content |
| --- | --- |
| `e8b2059` | Unit 8 follow-ups: «se-» with every counter, the «gerai» scene, six new ledger rows (L-1064 to L-1069), register labels, L-0592 retired, L-0931 Japanese, both ledger copies and the hash regenerated, chapter 7 and 8 tests updated |
| `4b98f45` | The six festival ledger rows Sam approved in the session (L-1070 to L-1075), written to the sheet first, both copies and the hash regenerated |
| `625772b` | Unit 9 (helper `suite/chapter9_common.py`, `suite/ms_c09.py`, `tests/test_step5g_suite.py`, registration, mentions, grammar points) |
| `56887d7` | Chapter 9 fast-course pack |
| next commit | This report and `HANDOFF.md` |

## Part 1: unit 8 follow-ups

| Sam's answer (step 5f review) | What I did |
| --- | --- |
| 1. «se-» + a classifier is normal Malay and is the chapter 8 pattern; rework unit 8 and the fast pack to teach and drill it with every counter, beside «satu» + counter. Kata-Kata frames f02 and f04 are correct | Done. Every counter entry now shows its «se-» form beside «satu» + counter («sehelai» = «satu helai», «secawan», «sepinggan», «sebotol», «sekotak», «seulas», «senaskhah», «sepucuk», «seorang» …) with 17 forms listed in the entries and 19 forms (with «seekor», «sebiji», «sebuah», «seorang») used in the unit. Pattern 2 is now ‹se-› + (counter) (noun). / «satu» (counter) (noun)., pattern 4 prices use «lima ringgit sekuntum», the model conversation, variant and listening use «sebatang», «sekotak», «sekuntum», «sebungkus», «secawan». The transformation drill has the direction both ways («Satu helai baju» → «Sehelai baju»; «Sekeping roti» → «Satu keping roti») and the substitution drill uses «Semangkuk sup», «Sebotol air kosong», «sepinggan». The fast pack, the culture note and the teacher notes say both forms are right. ‹sebatang› and ‹sehelai› are no longer "mentions": they are taught forms (the two mention entries were removed; the `se` mention now cites frames f02 and f04). A new test (`test_se_with_every_counter`) fails if a counter's fused form is not used |
| «se-» + classifier flagged as ledger gaps by the language checks? Add a narrow rule rather than rows, and explain | **Not flagged, so no new rule was needed.** `language_checks.Checker.derivation` already has a generic "‹se-› + noun" rule (the base must be a ledger noun, counter or card noun placed in the unit's chapter or earlier). I ran all 19 forms through `Checker.inspect` at chapter 8: no violation, no ledger gap, and each is derived to its counter. `test_se_forms_pass_the_language_checks` pins this. The rule is broad (it also accepts ‹se-› + any other noun); if you would rather have an explicit narrow rule that only accepts ‹se-› + a ledger counter or classifier, it is a four-line change in `derivation` plus a test, but I did not change the checker without a failing case |
| 2. New ledger rows L-1064 «nasi lemak», L-1065 «gerai», L-1066 «tambah», L-1067 «buah» (classifier), L-1068 «pisang goreng / goreng pisang», L-1069 «keropok lekor» (written by Claude to the sheet, Journal rows 75 to 80) | Regenerated both copies and the hash from the sheet (Ledger!A1:T1070; the only differences from the old copies were the six new rows and the two changed rows). All six are core in unit 8: «buah» joins the classifiers (14); a new group "At the «gerai»" holds «nasi lemak», «gerai», «tambah», «pisang goreng», «keropok lekor» (5). **Unit 8 is now 41 core words in five groups** (classifiers 14, containers 7, things counted 12, the «gerai» 5, «semua» / «tolong» / «Makan sini atau bungkus?» 3) plus 11 Dunia recognition words and 53 revision words. The ledger copy places 60 rows in chapter 8 (41 core, 11 recognition, 8 carried from earlier chapters). «pisang goreng» is taught as the standard order of the words and «goreng pisang» as the everyday name (entry, example, pattern 5, culture note, teacher notes); a test requires both. «kaki» as a counter is not added (the ledger keeps "foot, leg"; a test checks that it is not used as a counter). The «gerai» scene Sam suggested is in the listening (a flower stall, then a «gerai»: «Sebungkus nasi lemak dan dua keping pisang goreng, tolong.» «Tambah satu lagi pisang goreng.» «Ada keropok lekor?» «Secawan teh tarik kurang manis.»), the reading text (a «Gerai Pagi» price board), pattern 4 and 5, the writing model and the Q&A drill; the «mamak» task stays (with «Tambah dua cawan teh tarik, tolong.» as the change of plan). Prices add up (a test checks 3 + 3 + 5 + 3.50 = 14.50, change 5.50, and the board totals) |
| 3. Register: «pucuk» and «naskhah» are formal counters, mostly seen in writing; «tapau» is everyday speech; «sesak» is standard | Marked in the vocabulary entries, the culture note and the teacher notes of units 8 and 7 («sesak» standard, «jam» everyday speech), with tests (`test_gerai_scene_and_register`). The old "builder's reading, not checked" remark is gone from the teacher notes |
| 4. L-0592 «pintu masuk» Retired (duplicate of L-0330). L-0931 «mamak» Meaning (JA) is ママック | Both in the new copies. Unit 7 now counts 63 live rows in chapter 7 and still has **62 core** (63 − «depan» = 62); the unit 7 and test text say L-0592 is Retired. The ママック override in the unit 5 and unit 8 vocabulary lists is now the same as the ledger |
| 5. Keep the left-hand traffic and 2020 census sentences in the unit 7 culture note | Kept; the unit 7 sources line records Sam's decision. They remain secondary sources (see "Real-world facts") |

Tests updated: `tests/test_step5e_suite.py` (63 live rows, L-0592 Retired, 62 core), `tests/test_step5f_suite.py` (partition 60 / 41 / 11 / 8, five groups, `test_se_with_every_counter`, `test_se_forms_pass_the_language_checks`, `test_gerai_scene_and_register`, prices), `tests/test_language_checks.py` (the "not yet re-authored" fixture moves from ms-c09 to ms-c10).

## Part 2: chapter 9

### Word accounting

All counts are unique ledger entries. A slash variant counts once.

| Unit | Theme | New core | Dunia recognition | Revision (not counted, not tested as new) |
| --- | --- | ---: | ---: | ---: |
| 8 (after the follow-ups) | Classifiers | 41 | 11: "Beli baju" | 53 |
| 9 | Passive «di-», signs and notices | **29** | **33**: "Rumah terbuka" 19, "Simpulan bahasa harian" 14 | 74 |

**Ledger check for chapter 9.** The ledger copy places 63 live rows in chapter 9. `tests/test_step5g_suite.py` recomputes the sets from the ledger:

- **Core, 29:** first placed in chapter 9 and carrying a chapter 9 card: L-0377 to L-0405. «pinggan» (L-0355) also carries a chapter 9 card but was placed in chapter 8, so it is revision.
- **Dunia recognition, 33:** the 27 rows the ledger already had (the 13 "Rumah terbuka Hari Raya" words, L-0537 to L-0549, and the 14 "Simpulan bahasa harian" idioms, L-0954 to L-0967) plus Sam's six festival words (L-1070 to L-1075), which Sam approved in the session after seeing the exact proposal. 29 + 33 + 1 = 63.

**Core load: 29 in one unit** (charter: 20 to 40 typically), plus 33 recognition words, which makes the vocabulary list 136 entries long (29 + 33 + 74). The recognition words are labels and are never tested as new. Groups:

| Group | Words | N |
| --- | --- | ---: |
| «di-» verbs | dibuat, dibeli, dijual, dimakan, diminum, dibaca, ditulis, dibuka, ditutup, dibayar, dihantar, diambil, dipanggil, dimasak, dicuci, dibawa, disewa, dilarang | 18 |
| «oleh», «pada», «tadi», «siap» | oleh, pada, tadi, siap | 4 |
| Signs and notices | Dilarang masuk, Dilarang makan dan minum, Dilarang merokok, sila, papan tanda | 5 |
| A party | kek, jamuan | 2 |

The teacher notes give the A/B cut if the pilot shows 29 is too many: «dibuat», «dibeli», «dimakan», «diminum», «dibuka», «ditutup», «dibayar», «dihantar», «dilarang», «oleh», «pada», «tadi», «siap», «sila» and the signs first; «dibaca», «ditulis», «diambil», «dipanggil», «dimasak», «dicuci», «dibawa», «disewa», «dijual», «kek», «jamuan» second.

**Revision, 74 (four labelled groups).** Manners, time and markers (21), verbs, the kitchen and the office (26), food, drink and the stall (12, including the chapter 8 «gerai» words), question words, people and places (15). A test (`test_revision_words_really_return`) fails if a revision word is not used in a marked Malay line outside the vocabulary list.

### The «di-» rule

Passive «di-» with roots learners already know is the point of the chapter. What the language checks allow, and what I did:

- **The checker rule.** `language_checks.Checker.derivation` accepts «di-» + root when the unit's chapter is 9 or later and the root is *any* ledger entry placed in that chapter or earlier. It does not look at the part of speech (so «dikedai» would pass), and before chapter 9 a «di-» form of a card verb is flagged ("di- passive before chapter 9"). The ber- and me- guards are unchanged (a me-shaped base is flagged unless a chunk or root exemption applies; «Dilarang merokok» passes because the Kata-Kata card is a `chunk*`).
- **What the unit does.** The 18 ledger «di-» forms are core. Other «di-» + root forms are taught as the rule, not as new words: «digoreng», «dipilih», «ditunggu», «dijemput», «ditanya» (pattern 2 and the culture note), and the transformation drill makes «Ikan digoreng.» and «Encik Tanaka ditunggu.» from the active root verbs.
- **A stricter rule in the test** (`test_di_rule`): every «di-» form in marked Malay is either one of the 18 ledger forms or «di-» + a ledger *verb* placed in chapters 1 to 9; no ber- or me- verb appears (the only me- word is the sign chunk); and ‹buat›, ‹panggil›, ‹cuci› and ‹larang› (roots of four ledger «di-» forms that are not themselves ledger words) are never used as Malay, only as ‹…› mentions with their Kata-Kata card-note sources (ms-c09-004, -016, -018, -021). Active sentences in the drills use ledger root verbs only («beli», «tulis», «bawa», «masak», «baca», «goreng», «tunggu»).
- **The doer before the verb** (Kata-Kata frame f06, «Pinggan saya bawa ke dapur.») is taught inside pattern 3 as the natural way to say "I will do it", and appears in the model conversation, the listening and the task. It is not a sixth pattern, because the charter allows 3 to 5.

### Scenes

The Kata-Kata chapter 9 scenario ("The office jamuan") uses «durian», «jom kemas», «tak ada» and «nasi lemak»; I kept the setting (an office «jamuan») and wrote my own lines from in-scope words, so no Malay was forced:

- **Model conversation (12 turns) and its variant (11):** who made the cake, where the nasi lemak was bought, the tea is all drunk, the cake was cut, the plates are not washed («Pinggan saya bawa ke dapur.»); the variant changes the dishes and times.
- **Listening (131 Malay words, 16 turns):** Tanaka arrives early and asks what has been made, bought and washed; the sign «Dilarang makan dan minum» in the meeting room; nine questions.
- **Reading and writing:** a fictional office notice board (hours, «Dilarang makan dan minum», «Dilarang merokok», «Sila ambil nombor», the «jamuan»), seven questions, and a notice to write.
- **Task:** "Who made it?" with role cards (organiser and guest) and a change of plan ("teh tarik belum dibuat").
- **Culture note (211 words):** the neutral passive (and 受身), signs, word-building from the Kata-Kata card notes, the doer-before-verb form. No claim about any real sign, law or custom.
- **Culture note · Open houses in Malaysia (246 words), a second Culture note component for Block E:** a general introduction and one short note per festival (Hari Raya, Tahun Baru Cina, Deepavali, Krismas, Gawai and Kaamatan). The festival-specific Raya words («maaf zahir dan batin», «duit raya», «ketupat», «pelita», «rendang», «kuih», «baju Melayu», «balik kampung») are inside the Hari Raya note as culture, not as a religious lesson; a test checks they appear in that note only. Greetings are built from ledger words («Selamat Hari Raya», «Selamat Hari Deepavali», «Selamat Hari Krismas», «Selamat Hari Gawai»); there are no greeting rows (Sam's answer), no Assalamualaikum, and no Kaamatan greeting in Malay.
- **Idioms** ("Simpulan bahasa harian", 14): listed in the vocabulary with the ledger's plain meanings and one short example; a test fails if any of them appears in a drill, task, listening, reading, model conversation, pattern or test item, and the teacher notes say "do not drill them".

## Evidence for charter section 6 and section 14 (unit 9)

| Minimum | Unit 9 | Where it is tested |
| --- | --- | --- |
| Eleven components | All eleven, plus the markers drill and a second Culture note (the festival notes). No skills block (the Stage 1 plan gives none after unit 9; the stage review and the A1 test come next) | `test_components_and_vocabulary` |
| Vocabulary: every ledger word, JA and EN meaning, one example each, spoken forms marked | 136 entries (29 + 33 + 74), each with an example; the «di-» entries show their root; «Dilarang merokok» is marked "recognise only"; entry count = example count = ID count | same |
| 3 to 5 patterns, 4 to 6 Q&A each, EN and JA explanation, Japanese note | 5 patterns × 6 Q&A, one per Kata-Kata frame f01 to f05 (f06 inside pattern 3) | `test_patterns` |
| Drill types 1 to 5, at least 6 items each (30+) | 8, 8, 10, 8, 8 = 42 items | `test_drills_keys_and_question_words` |
| Type 6 short dialogues (3+) | 4 | same |
| Cumulative question words | all earlier ones + **«siapa» with «oleh»**; 18 tasks with model questions, each checked; the Q&A and choice drills ask «Kek ini dibuat oleh siapa?» | same |
| Tense and aspect markers return (section 14) | "Markers with passive verbs": «sudah», «belum», «masih», «akan», «baru» with «di-» verbs; 8 items, Japanese bridge, key | `test_markers_return` |
| Real answer keys | Every drill, markers, reading and test item has its own answer | key regex per item |
| Model conversation 10 to 16 turns, gapped, changed facts | 12 turns, 5 gaps, an 11-turn variant with changed facts | `test_conversation_…` |
| Listening 120 to 250 Malay words, before/during/after, 6+ items | 131 words, 9 items | same |
| Reading text with 5+ questions; guided writing with model | A notice board, 7 questions; a notice with a model | same |
| Task: role cards, change of plan, success criteria | "Who made it?" | same |
| Culture note 150 to 300 words, full JA translation | 211 words (main), 246 (festival notes); no leftover English in the Japanese | word count and a Japanese-cell check |
| Test 15 to 20 items + speaking, every item tagged | 19 scored (6 listening, 6 words, 3 grammar, 4 reading) + 1 speaking; word items use core words only | `test_tests_and_plans` |
| Teaching plan: timings, prompts, Kata-Kata before and after | Five blocks, Sedia Kelas c09 (12 cards, frames f01 and f02), the Dunia scenes | same |
| Fast pack: 2 to 4 pages, 15 to 20 words, patterns with 2 examples | 3 content pages, 20 words, 5 patterns × 2 examples, 10-turn conversation, task with change of plan, 5-item self-check, self-study guide | `test_fast_pack` |

**Chapter 9 Malay rules, tested.** Standard first, spoken forms labelled (a test fails if «nak», «tapi», «sikit», «dah», «tak», «senang», «saja», «tapau» or «jom» sits on a line without a label). Malaysian forms only. No ber- or me- verbs. No faith-specific expressions, no food rules (regex over every line: Assalamualaikum, Waalaikumsalam, doa, solat, puasa, halal, haram and similar are absent, and the festival notes contain no belief or rule). Nothing placed after chapter 9 and nothing missing from the ledger (the build fails on either in a re-authored unit). Names, notices, times and prices are fictional and labelled.

## Files changed

- **New:** `suite/chapter9_common.py` (copy of the chapter 8 helper: ms-c09 ids, `GRAMMAR9`, "siapa with oleh", "Markers with passive verbs", the two Dunia scenes, Sedia Kelas c09, a second Culture note for the festival notes, genre "Social life"), `suite/ms_c09.py`, `tests/test_step5g_suite.py` (17 tests), this report.
- **Changed:** `suite/ms_c08.py`, `suite/ms_c07.py`, `suite/ms_c05.py` (ママック), `suite/fast.py` (chapter 8 changes; the chapter 9 pack), `suite/__init__.py` (grammar points ms-c08-g03 label and ms-c09-g02 to g06, `GLOSS` for L-1064, L-1066 to L-1069, unit loading, scene titles), `course.py` (chapter 9 status), `curriculum/reauthored-units.json` (+ms-c09, ms-c09-fast), `curriculum/malay-mentions.json` (−‹sebatang›, −‹sehelai›, −‹nasi lemak›; +‹di›, ‹buat›, ‹panggil›, ‹cuci›, ‹larang›, ‹jamu›, ‹an›, ‹me›, ‹ber›; ‹se› source extended), `curriculum/malay-proper-nouns.json` (+Dayak), both ledger copies and `docs/step4-sources.json`, `tests/test_step5e_suite.py`, `tests/test_step5f_suite.py`, `tests/test_language_checks.py`, `HANDOFF.md`, and the generated files in `dist/` and `docs/step4-authored-scope.json`.
- **Not changed:** the charter snapshot, the Kata-Kata reference files, the legacy lesson sources, `legacy-exceptions.json` (still 30; chapter 9 had no legacy packs, so nothing was retired).
- **The ledger sheet was changed by me:** rows L-1070 to L-1075 and Journal rows 81 and 82, after Sam approved the exact proposal in the session. Rows L-1064 to L-1069 and Journal rows 75 to 80 had been written earlier by the other Claude session. I changed no other row.

## Proposed ledger rows

Words the chapter 9 scenes could not use. None is used. Each would be "Not yet checked" for Kamus Dewan; I added none.

| Word | Meaning | Why |
| --- | --- | --- |
| buat, panggil, cuci, larang | make, call, wash, forbid | Roots of the ledger forms «dibuat», «dipanggil», «dicuci», «dilarang». Without them the unit cannot show the active verb («Dia buat kek»), so the transformation drill uses other roots and these four appear only as ‹…› mentions. Sam may prefer to keep it that way |
| ibu | mother | The natural way to say who cooked at home («dimasak oleh ibu saya»); the unit uses «isteri saya» and «suami saya» |
| adik | younger sibling | «Duit raya untuk adik» is the natural example; the unit uses «anak saya» |
| tuan rumah | host | «Buah tangan untuk tuan rumah» for the idiom example; the unit uses «kawan saya» |
| mari | come, let's | Kata-Kata scenario uses «jom» (spoken); «mari» is the standard word |
| apa-apa (in «Tidak apa-apa») | never mind | Replaced by «Baik.» in the scenes |
| durian | durian | Kata-Kata scenario ("Durian dilarang di pejabat!") |

## Real-world facts used, and their sources

| Fact | Source checked | Rank | Status |
| --- | --- | --- | --- |
| The Malay passive is neutral and very common, unlike 受身 | Charter chapter 9 row (Sam's table) | Sam's reference | Taken from the charter |
| «Dilarang merokok» contains me- and is to be learned as a sign only; «jamuan» ← ‹jamu› (treat a guest); roots buat, panggil, cuci, larang | Kata-Kata cards ms-c09-024, -029, -004, -016, -018, -021 (notes) | Sam's reference | [VERIFIED] against the cards; none is a note Sam has corrected (the ledger "Sam's notes" column has nothing for these rows) |
| The Raya words and their meanings (ketupat, rendang, kuih, duit raya, pelita, baju Melayu, balik kampung, maaf zahir dan batin) | Ledger glosses L-0537 to L-0549 and the Kata-Kata Dunia scene name | Sam's reference | Gloss only; no usage source added |
| Open houses (rumah terbuka) are a Malaysian custom in which hosts welcome relatives, friends, neighbours and colleagues at festivals, with people of other communities often invited | EMGS Connect, "You've been invited to an Open House: Hari Raya Traditions"; Arab News, "Malaysia's 'Open House' ensures all are welcome on Eid" | 3 | **Seen in search summaries only**; the pages were not opened. Where the open house began is not stated (the sources disagree) |
| Chinese New Year open houses are widely held; red packets with money (angpau) are among the customs | EMGS Connect, "Chinese New Year in Malaysia"; Malay Mail, 10 Feb 2026 (a party's open house in Kuala Lumpur) | 3 | Search summaries only. The word «angpau» as spelled is Sam's approved ledger row |
| Deepavali open houses for all Malaysians; a family hosting Malay and Chinese friends and neighbours | Malay Mail, 8 Nov 2026, "Eat, mingle, celebrate: five Deepavali open houses from Brickfields to Ipoh for all Malaysians" and a Malay Mail piece on a family open house the same day | 3 | Search summaries only |
| Gawai (Sarawak, from 1 June; a public holiday there since 1965) and Kaamatan (Sabah, 30 and 31 May) are harvest festivals and state holidays; Gawai open houses are held | The Borneo Post, Zafigo and Sarawak Premier's Department pages as returned by search | 3 | Search summaries only. I did not state whether they are national holidays (the summaries say NGOs have asked for it and I found no confirmation) |
| Christmas is celebrated by Malaysia's Christian communities | General knowledge | none | **No source retrieved** (I found nothing checkable on Christmas open houses, so the note says nothing about them) |
| «Selamat Hari Raya», «Selamat Hari Deepavali», «Selamat Hari Krismas», «Selamat Hari Gawai» are built from ledger words | The ledger rows and Sam's answer on greetings (Journal row 82) | Sam's reference | These are my constructions after the L-0538 pattern, not checked in Kamus Dewan or against usage |
| «pisang goreng» is the standard order of the words and «goreng pisang» the everyday name; «keropok lekor» is a Terengganu speciality | Ledger L-1068 (Sam's note, Journal row 77, which records a Sinar Harian column on Peraturan D-M and recipe sites) and the ledger gloss of L-1069 | Sam's reference | Not reopened in this session |
| Unit 7 (kept at Sam's request): traffic keeps to the left; the 2020 census groups | As in the step 5e report (secondary sources, no percentages) | 3 | Still secondary sources |

I tried to read the Wikipedia pages on Gawai Dayak, Kaamatan, Public holidays in Malaysia, Hari Raya Aidilfitri, Chinese New Year and Deepavali, but the host does not resolve from this session (`ENOTFOUND en.wikipedia.org`), so nothing in the notes is read from them. I did not change the session's network settings. Each festival note names its source in the teacher key.

## Unverified and provisional

- **All Malay example sentences are mine.** They pass the ledger, register, affix and Malaysian-form checks, but none has had a native read. Please look especially at: «Kek ini dibuat oleh siapa?», «Dibeli oleh Encik Tanaka di gerai pagi tadi.», «Kek itu dipotong oleh Rahman tadi.», «Pisang goreng pun sudah dimakan semua.», «Pinggan saya bawa ke dapur.», «Kek saya beli.», «Pintu masih dibuka.» (the «masih» + «di-» order), «Kedai ditutup pada pukul enam.» and the plain «Kedai buka pukul sembilan.», «Sila ambil nombor.», «Dilarang makan dan minum di bilik mesyuarat.», «Kek dan kuih dibawa oleh semua orang.», «Surat itu dihantar ke pejabat.», the productive forms «digoreng», «dipilih», «ditunggu», «dijemput», «ditanya», and in unit 8 «Sebungkus nasi lemak, dua keping pisang goreng.», «Tambah satu lagi pisang goreng.», «Sebungkus keropok lekor», «Seulas bawang putih sahaja.», «senaskhah surat khabar», «sepinggan mi goreng» and «seorang» [UNVERIFIED].
- **Which counter goes with «pisang goreng» and «keropok lekor»** («dua keping pisang goreng» is Sam's wording; «sebungkus keropok lekor» is mine).
- **Kamus Dewan spelling** of «Tahun Baru Cina» (against «Tahun Baharu Cina»), «angpau», «Krismas», «Deepavali», «Gawai», «Kaamatan» and «gurdwara» is not checked; the KD4 check is "Not yet checked" for L-1064 to L-1075.
- **The Japanese** (all cells, including both culture notes, the festival notes and the 受身 comparisons) is a draft for native review. The Japanese for L-1064 «nasi lemak» in the ledger reads ナシレマッ…, which looks truncated like the earlier ママッ; the unit uses ナシレマ (as in the Kata-Kata frame). The ledger's Japanese for L-1071 to L-1075 is mine.
- **The festival facts** are from search summaries only, as listed above.
- **In class:** timings, drill load, 41 core words in unit 8 and 29 + 33 recognition words in unit 9 (136 vocabulary entries) have not been taught.
- **Kamus Dewan check** is still pending for L-0983 to L-1075.

## Findings for Kata-Kata (not changed here)

- **Scene name.** The scene is "Rumah terbuka Hari Raya" in Kata-Kata and in the ledger's place column for L-0537 to L-0549; the ledger rows for L-1070 to L-1075 say "Dunia · Rumah terbuka (primes Ch9; pending)". The Kata-Kata scene needs to become a general "Rumah terbuka" scene (Sam's decision), with cards for L-1070 to L-1075; the charter table's chapter 9 scene list also says "Rumah terbuka Hari Raya".
- **Cards missing:** L-1064 to L-1075 (pending), the cards listed in earlier reports for L-1032 to L-1063.
- **Scenario "The office jamuan"** (ms-c09-s01 to s10): uses «durian» (not in the ledger), «jom kemas» («jom» is spoken, «kemas» is chapter 4), «tak ada» before «tidak», and «Pinggan saya cuci», where «cuci» is not a ledger word. Frame ms-c09-f02 and the scenario now use «nasi lemak», which is a ledger word since 12 Nov.
- **Frame ms-c09-f06** («(thing) saya / awak (verb).») has no card of its own and a verb root («cuci») outside the ledger; the unit teaches the shape with «bawa», «beli» and «ambil».
- **Card ms-c09-028** («pinggan») duplicates the chapter 8 card ms-c08-016; the ledger counts it once, in chapter 8.
- **Card ms-c09-024** («Dilarang merokok», `chunk*`) is the only card that carries a me- verb; the unit teaches it as a sign only.
- **Chapter 8 frames f02 and f04** (‹se-› + counter) are now correct for the unit (Sam's answer). The Kata-Kata chapter 8 cards for «buah» (ms-c08-003) and «kaki» (ms-c08-010) still differ from the ledger (L-1067 is the counter «buah»; «kaki» is not a counter in the ledger).
- **Ledger L-0592** is Retired; Hanashishou's daily-life card should map to L-0330.

## Questions for Sam

1. **Load.** Unit 8 is now 41 core words (the heaviest unit after unit 7's 62) and unit 9 has 29 core + 33 recognition words (136 vocabulary entries, because 74 revision words are listed). Is the festival group (19 recognition words) too much beside the 29 core words? The A/B cut for each unit is in the teacher notes.
2. **Festival facts.** The notes rest on search summaries, because Wikipedia was not reachable. Would you like me to re-check them against full pages if the host is allowed, or to cut the notes to the ledger glosses only? Also: may the Christmas note stay as one general sentence, or should it be dropped until a source is found?
3. **Greetings.** I built «Selamat Hari Deepavali», «Selamat Hari Krismas» and «Selamat Hari Gawai» from ledger words after your answer (no greeting rows). Are these the forms you want shown? No Malay greeting is given for Kaamatan; do you want one?
4. **Proposed rows** (above): add the four roots (buat, panggil, cuci, larang)? ibu, adik, tuan rumah, mari? Without them the scenes use the other words listed.
5. **Spellings for the Kamus Dewan check:** «Tahun Baru Cina» or «Tahun Baharu Cina»; «angpau» or «ang pow»; «Krismas»; «Deepavali». And the Japanese of L-1064 (ナシレマッ… looks truncated; may I correct it to ナシレマ in the sheet?).
6. **The «se-» rule in the checker.** The existing rule already covers «se-» + counter. Do you want an explicit narrow rule anyway (only ‹se-› + a ledger counter or classifier)?
7. **Charter table.** The chapter 8 row already reads «se-(counter) (noun)», which now matches the unit. The chapter 9 row of "How the tools line up per chapter" lists the Kata-Kata scenes "Rumah terbuka Hari Raya, Simpulan bahasa harian"; it should say "Rumah terbuka" once the Kata-Kata scene is renamed.
8. **Pilot.** Please teach unit 8 (the «se-» drills and the «gerai» listening) and unit 9, and say whether the «di-» rule (any known verb root, not only the 18) is the right reach for A1, and whether the festival notes in Block E feel right.
9. **Next.** The stage review and the A1 test wait for your go-ahead.
