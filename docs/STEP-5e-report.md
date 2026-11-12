# STEP 5e REPORT: Chapter 7, Batch 5

**Scope:** (1) the unit 6 follow-ups from Sam's answers to the step 5d questions and the review block after unit 6; (2) Malay A1 chapter 7 (places and directions): **unit 7** and the chapter 7 fast pack. Sam authorised the batch on 12 Nov 2026 and pre-approved publication to main when the checks pass. Nothing from chapter 8 was started.

**Sources read:** `AGENTS.md`, `HANDOFF.md` (in full, including "Quality rules for chapter 4 onward"), the charter (`docs/handoff/charter-snapshot.md`, refreshed from the live Google Doc on 12 Nov 2026; the live Doc was not opened in this session, so any change after that refresh is not reflected), the Kata-Kata chapter 7 file (`curriculum/reference/katakata/c07.json`), the ledger (read from the Google Sheet, Ledger!A1:T1054 at the start and A1055:T1059 after my additions), and chapters 6, 5 and 4 (source, helper, tests, report) as models.

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests` (91 tests) pass on a full Git checkout at every commit below (after `pip install pymupdf fonttools`, `apt-get update` and `apt-get install fonts-noto-cjk` and `git fetch --unshallow`; the `apt-get update` step is new: without it the font package is not found).

| Commit | Content |
| --- | --- |
| `c43f7e2` | Unit 6 follow-ups: ledger copies refreshed (L-1051 to L-1053, note on L-0285), unit 6 with «sewa», «bilik», «luas», «senang» marked spoken, chapter 6 fast pack, tests |
| `b628ff3` | Review block after unit 6 (chapters 1 to 6), registered as `ms-stage1-review-6` |
| `4d4a4d6` | Unit 7, chapter 7 helper, tests, registration, five new ledger rows in the copies, retirement of the legacy chapter 7 packs |
| `6d49e03` | Chapter 7 fast-course pack |
| next commit | This report and `HANDOFF.md` |

## Part 1: unit 6 follow-ups and the review block

| Sam's answer (step 5d report) | What I did |
| --- | --- |
| Q1: «sewa», «bilik», «luas» added to the ledger (L-1051 to L-1053, Journal rows 64 and 65, written by the other Claude) | Both repo copies regenerated from the sheet (Ledger!A1:T1054), `docs/step4-sources.json` hash updated. The only differences from the old copies were the three new rows and the L-0285 note. Unit 6 now has **35 core words** (was 32): «sewa» and «bilik» join «kondo» and «stesen» in "Places" (4), «luas» joins "Describing places and things" (14). Used naturally: «Berapa sewa kondo A?» «Sewa kondo A tiga ribu dua ratus ringgit setiap bulan.» «Kondo A ada tiga bilik.» «Kondo B ada dua bilik, tetapi kurang luas.» «Kondo D baru, luas dan sangat selesa.» Rent and rooms are in the model conversation, its variant, the listening (a new question: how many bedrooms), the condo listing (every condo has a rent and a room count), the task (A asks the rent and the number of rooms), the test and the chapter 6 fast pack (which swaps «susah», «cantik» and «stesen» out and «sewa», «bilik», «luas» in; still 20 words). Revision gained five words that return in those scenes («setiap», «bulan», «tidur», «bilik air», «ada»): 30 revision entries |
| Q4: «senang» is spoken, «mudah» standard | Already shown as «mudah» / «senang» (spoken); now also said in the pattern 1 explanation and the teacher note, which no longer says "[UNVERIFIED]" about Sam's decision (it still says Kamus Dewan was not opened). A test requires a "spoken" label on every line with «senang» |
| Q5: only the six whole ter- and se- words until chapter 16 | Unchanged; the existing test still fails if a new ter- or se- word is built |
| Q8: keep the Strata Management Act and rail-network note | Kept unchanged |
| Q3: «sekali» meaning | No change; Claude updates the ledger if Sam confirms |
| Q2 («tengok») and Q7 (pilot: is 32 too many?) | Not answered in the brief. «tengok» is still L-0577 in chapter 7 and is a Dunia recognition word in unit 7. The chapter 6 count is now 35 |

**One wording choice to check.** The ledger gloss of «sewa» says "sewa sebulan = rent per month", but «sebulan» is not a ledger word, so every rent line says «setiap bulan» (as in step 5d). Add «sebulan» if you want the shorter form.

**Review block after unit 6** (`ms-c06-review-block`, 45 minutes, "Skills" block, sub-type composition): modelled on the 4B review block and covering chapters 1 to 6.
- A six-turn model exchange with one line from each chapter: greeting (1), where you live (2), the rent (3 and 6), the time and the busiest hour (4 and 6), «Kenapa …?» with «Sebab …» (5), «Encik pilih yang mana?» (6).
- Task in three parts (10 + 20 + 15 minutes): one question per chapter without notes; six written sentences about a home or place (where, rent, rooms, a comparison, «sangat» or «terlalu», which is best); read the partner's sentences aloud and ask «Yang mana …?» and «Kenapa …?».
- Five-item peer check, one per chapter (no «kurang suku»); a model paragraph in the key.
- Registered: `catalogue.py` now maps `review-6` to `ms-c06-review-block` (`status: pilot draft`). Test: `test_review_block_after_unit_6`.

## Word accounting

All counts are unique ledger entries. A slash variant counts once.

| Unit | Theme | New core | Dunia recognition (by scene) | Revision (not counted, not tested as new) |
| --- | --- | ---: | --- | --- |
| 6 (after the follow-ups) | Comparing, the most, very and too, choosing, describing places and things, kondo, stesen, bilik, sewa | **35** | **14**: "Main badminton" 14 | 30 |
| 7 | Places and directions | **56** | **33**: "Di ruang tamu" 13, "Telefon baru" 12, "Lintas jalan" 8 | 43 |

**Ledger check for chapter 7.** The ledger copy places 53 rows in chapter 7 (47 "Ch7" and 6 "Ch7 (pending)") and 33 Dunia recognition entries, as the brief said. `tests/test_step5e_suite.py` recomputes both sets from the ledger. With the five rows Sam approved in the session (below), **58 rows** are placed in chapter 7. Two are not new core:

| Row | Why it is not counted as new core |
| --- | --- |
| **L-0592 «pintu masuk»** (Entrance, chunk, card ms-c07-036) | **Duplicate** of **L-0330 «pintu masuk / pintu keluar»** (same card ms-c07-036). Reported, not counted twice, not edited. The test asserts L-0330's Malay contains «pintu masuk» |
| **L-0304 «depan / hadapan»** (front, card ms-c07-009) | «depan» is L-0173 (Ch4, "next (time); front"), already taught in 4B. L-0304 adds «hadapan» (formal, from the card note). Revision, with «hadapan» said in the entry |

**58 − 2 = 56 core.** **Core load: 56 in one unit** (charter: 20 to 40 "typically"; the 13-unit plan has one unit for chapter 7; Sam has said more words are fine). It is the heaviest unit so far, and 21 of the 56 are in one group, so I give the A/B cut in the teacher notes (position, distance, direction and turning words first; landmarks, transport and compass points second).

| Group | Words |
| --- | ---: |
| Position words (kiri, kanan, belakang, atas, bawah, dalam, luar, sebelah, antara, seberang, sini, situ, sana) | 13 |
| Distance and direction (ke, ke mana, dari mana, dekat, jauh, berapa jauh, berapa lama, lebih kurang, lurus) | 9 |
| Turning and moving (belok, kemudian, jalan, jalan kaki, naik, turun, masuk, keluar, kalau) | 9 |
| Landmarks and transport (simpang, lampu isyarat, bulatan, lintasan, pintu masuk / pintu keluar, tingkat, lif, tandas, tempat, kedai, bank, **masjid, gereja, kuil, tokong, gurdwara, surau**, kereta, bas / teksi, kereta api, jam) | 21 |
| Compass points (utara, selatan, timur, barat) | 4 |

**Words reused, not new (revision, 43).** «depan» (ch 4), «bilik» (ch 6), «hospital» (L-0336, placed Ch5 in the "Di klinik" scene as well as Ch7), «kapal terbang» (L-0449, placed Ch4 in "Cuti ke pantai" as well as Ch7), «lama» (L-0284, Ch6; Ch7: the new meaning "a long time" is in the entry), and others from chapters 1 to 6 («maaf», «terima kasih», «sama-sama», «hati-hati», «jumpa», «pejabat», «rumah», «sekolah», «pasar», «pejabat pos», «meter», «pergi», «balik», «datang», «sampai», «minit», «jam» (hour), «tunggu», «mahu», «tetapi», «sebab», «stesen», «kondo», «cepat», «lebih», «paling», «yang mana» and more). The test checks every revision ID is placed in chapters 1 to 6 and is neither core nor recognition. «hospital» and «kapal terbang» are not among the 53 rows (their placement starts with "Dunia"), so counting them as revision keeps the brief's 53. «tengok» (L-0577) is one of the 13 "Di ruang tamu" recognition words, marked "everyday speech".

**Ledger rows added in this session (Sam approved in the session).** The brief said not to edit the ledger and to ask Sam first. I asked, and Sam answered in the session: «masjid» (L-0337, existing) plus «gereja», «kuil», «tokong», **«gurdwara» and «surau»** as one even-handed set of landmarks, and asked me to write the rows. I wrote to the sheet:

| Row | Word | Meaning (EN) | Meaning (JA) | Placement |
| --- | --- | --- | --- | --- |
| L-1054 | gereja | church | 教会 | Ch7 (pending) |
| L-1055 | kuil | Hindu temple | ヒンドゥー教寺院 | Ch7 (pending) |
| L-1056 | tokong | Chinese temple | 中国寺院（廟） | Ch7 (pending) |
| L-1057 | gurdwara | Sikh temple | シク教寺院（グルドワラ） | Ch7 (pending) |
| L-1058 | surau | small prayer hall | 礼拝所（スラウ） | Ch7 (pending) |

Journal row 66 records the five rows and row 67 records Sam's decision for L-0337 «masjid». «vihara» was offered and not selected. KD4 check is "Not yet checked" for all five; **the spelling and Kamus Dewan headword status of «gurdwara» are not confirmed** (noted in the row's Action cell). Both repo copies and `docs/step4-sources.json` (hash, 1,058 rows) were refreshed from the sheet (rows 1055 to 1059 re-read from the sheet before appending).

## Evidence for charter section 6 and section 14 (unit 7)

| Minimum | Unit 7 | Where it is tested |
| --- | --- | --- |
| Eleven components | All eleven, plus the markers drill. No writing block (see question 6) | `test_components_and_vocabulary` |
| Vocabulary: every ledger word, JA and EN meaning, one example each, spoken forms marked | 132 entries (56 + 33 + 43), each with an example; «jam» (traffic) marked spoken; «tengok» and «pergi kerja» / «balik rumah» marked everyday speech; «nak», «tapi», «saja» marked spoken | entry count = example count = ID count |
| 3 to 5 patterns, 4 to 6 Q&A each, EN and JA explanation, Japanese note | 5 patterns × 6 Q&A, one per Kata-Kata frame: f01 «ke» / «dari»; f02 «di» + position word (and compass points); f03 «Jalan lurus, kemudian belok»; f04 «Berapa jauh» / «lebih kurang»; f05 «Berapa lama» / «naik» | `test_patterns` |
| Drill types 1 to 5, at least 6 items each (30+) | 8 items each (40) | `test_drills_keys_and_question_words` |
| Type 6 short dialogues (3+) | 4 | same |
| Cumulative question words | all earlier ones + **«ke mana», «dari mana», «berapa jauh», «berapa lama»**; 16 tasks with model questions, each checked; the choice drill uses all four new ones | same |
| Tense and aspect markers return (section 14) | "Markers with places and routes": «sudah», «belum», «masih», «akan», «baru» with «pergi ke», «balik ke», «sampai», «tunggu», «turun»; 8 items, Japanese bridge, key | `test_markers_return` |
| Real answer keys | Every drill item, markers item, reading item and test item has its own answer | key regex per item |
| Model conversation 10 to 16 turns, gapped, changed facts | 13 turns (asking the way to a bank and a bus), gapped (5 gaps, answers in key), 13-turn variant with a different place, route, landmark and vehicle | `test_conversation_…` |
| Listening 120 to 250 Malay words, before/during/after, 6+ items | 136 words, 9 items | same |
| Reading text with 5+ questions; guided writing with model | A building directory board (fictional), 7 questions; a three- or four-sentence message giving the way from the station, with a model | same |
| Task: role cards, change of plan, success criteria | Asking the way to the hospital; halfway «Hari ini jam. Bas lambat.» and A asks «Kalau jalan kaki, berapa lama?» | same |
| Culture note 150 to 300 words, full JA translation | 210 words, four paragraphs; no leftover English in the Japanese | word count and a Japanese-cell check |
| Test 15 to 20 items + speaking, every item tagged | 19 scored (6 listening, 6 words, 3 grammar, 4 reading) + 1 speaking; word items use core words only | `test_tests_and_plans` |
| Teaching plan: timings, prompts, Kata-Kata before and after | Five blocks, Sedia Kelas c07 (27 cards, frames f01 and f02), the three Dunia scenes | same |
| Fast pack: 2 to 4 pages, 15 to 20 words, patterns with 2 examples | 3 content pages, 20 words, 5 patterns × 2 examples, 10-turn conversation, task with change of plan, 5-item self-check, self-study guide | `test_fast_pack` |

**Chapter 7 Malay rules, tested:**
- **«ke» is taught.** «pergi ke pejabat» and «balik ke rumah» are the standard written form; «pergi kerja» and «balik rumah» are marked "everyday speech" on every line where they appear (tested). The culture note, pattern 1, the vocabulary entries for «ke», «kerja» and «balik» and the teacher notes say the same.
- **Even-handed places of worship.** «masjid», «gereja», «kuil», «tokong», «gurdwara» and «surau» are one group of core words and are used as plain landmarks (position and route sentences only). A test counts their uses in marked spans: each appears at least 4 times (actual counts 9, 13, 11, 14, 11, 11) and none appears more than three times as often as the least used. No worship, dress, etiquette, greeting or prayer content: a regex test bans the Malay words for these and the earlier banned expressions («assalam», «insya», «halal», «puasa» and so on). Teacher notes say "Show no bias".
- **Standard first, spoken marked.** «jam» (traffic) and «tengok» are marked; «nak», «tapi», «saja» appear only on labelled lines.
- **Malaysian, never Indonesian:** «belok», «lampu isyarat», «bulatan», «tandas», «simpang», «lif», «kereta», «kedai», «bas» (the Indonesian look-alikes «toko», «bis», «mobil» and «toilet» are banned by test and by the build).
- **No ber- or me- verbs** (the build's affix check passes with no exceptions); the affixed words are the ledger's own («bulatan» with ‹bulat› from a Kata-Kata note, «lintasan»).
- **Nothing placed after chapter 7 and nothing missing from the ledger** (the build fails on either in a re-authored unit). Words that were out of reach and that I worked around are in "Proposed ledger rows".

**Natural Malay.** Where the in-scope words could not make a natural sentence I changed the scene, not the Malay:
- The Kata-Kata scenario uses «Maaf, tumpang tanya», LRT, Grab, Pavilion, KLCC and «terus»; none is in the ledger or none is verifiable, so the scenes use a bank, a station, a building directory and an office. The polite opener is «Maaf, …» (L-0018).
- Distances are in «meter» (the only ledger unit); there is no «kilometer», so the longest distance is «seribu meter» («Lebih kurang seribu meter.»).
- «Saya naik bas di mana?» / «Encik turun di bulatan.» uses only taught words; the bus stop itself has no ledger word, so the answer names a landmark («di seberang jalan, di depan stesen»).
- The traffic-delay sense of «jam» is spoken; it is used in the pairs «kalau tidak jam» / «kalau jam» only, labelled in the vocabulary and the pattern 5 explanation.

**Legacy packs.** "Asking where" and "Directions and orientation" (learner packs and teaching plans) are removed from the active catalogue; the source text stays in `curriculum/malay-course.txt`. **I also retired the legacy grammar pack "Di, ke and dari"**: it contained «kampus» and «tren» (not in the ledger), the build blocks ledger gaps inside a re-authored unit, and unit 7 patterns 1 and 2 now teach di, ke and dari; its source text stays in `build.py`. Two legacy exceptions for ms-c07 («nak», «tak») are removed: **32 → 30**. The chapter 7 page status now reads "Step 5e chapter 7 suite · draft for pilot".

## Files changed

- **New:** `suite/chapter7_common.py` (copy of the chapter 6 helper: ms-c07 ids, `GRAMMAR7`, the four new question words, "Markers with places and routes", the three Dunia scenes), `suite/ms_c07.py`, `tests/test_step5e_suite.py` (15 tests), this report.
- **Changed:** `suite/ms_c06.py` and `suite/fast.py` (follow-ups, review block, chapter 7 fast pack), `suite/chapter6_common.py` (review-block label), `suite/__init__.py` (grammar points ms-c07-g02 to g06, scene titles, glosses for «sewa» and «bilik», «internet» as an English homograph, unit loading), `catalogue.py` (`review-6`), `course.py` (chapter 7 status; three legacy packs retired), `curriculum/reauthored-units.json` (+ms-c07, ms-c07-fast), `curriculum/legacy-exceptions.json` (two removed), `curriculum/malay-mentions.json` (+‹menyewa›, ‹bulat›), both ledger copies and `docs/step4-sources.json` (hash), `tests/test_step5d_suite.py`, `tests/test_catalogue.py` (retired titles), `tests/test_language_checks.py` (its "not yet re-authored" fixture moves from ms-c07 to ms-c08), `HANDOFF.md`, and the generated files in `dist/` and `docs/step4-authored-scope.json`.
- **Not changed:** the charter snapshot, the Kata-Kata reference files, the legacy lesson sources. **The ledger sheet was changed by me** (five rows and two Journal entries, with Sam's approval in the session, as above).

## Proposed ledger rows

Words the chapter 7 scenes could not use. None is used. Each would be "Not yet checked" for Kamus Dewan; I added none.

| Word | Meaning | Why |
| --- | --- | --- |
| kilometer | kilometre | Real distances between towns and on road signs are in kilometres; today only «meter» is available |
| sebulan | per month, one month | The ledger gloss of «sewa» says "sewa sebulan"; the scenes say «setiap bulan» |
| tumpang tanya | excuse me, may I ask | The usual polite opener in the Kata-Kata scenario («Maaf, tumpang tanya.»); today only «Maaf» is available |
| terus | straight on, directly | A natural partner of «lurus» in directions; the scenes use «jalan lurus» only |
| jangan | do not | Directions and road signs often say «Jangan belok kanan»; no negative command is available |
| tangga | stairs | Building directories and «naik» / «turun»; today only «lif» is available |

## Real-world facts used, and their sources

| Fact (unit 7 culture note) | Source checked | Rank | Status |
| --- | --- | --- | --- |
| Traffic in Malaysia keeps to the left, a legacy of British rule | SAYS Malaysia, "Why Do M'sians Drive On The Left Side Of The Road While Most Countries Drive On The Right?"; Malay Mail, 29 June 2015, a primer on driving in Malaysia; WorldAtlas, "Countries That Drive on the Left" (search summaries; the pages were not opened) | 3 | Left-hand traffic [VERIFIED] across several secondary sources; the British origin is from one source's summary and general knowledge. The Road Transport Act 1987 and the Road Transport Department site were not opened |
| Reports of the 2020 census name Muslim, Buddhist, Christian and Hindu communities among the largest groups | Sinar Daily, "Malaysia's population now stands at 32.4 mil, 63.5 per cent Muslims", reporting the Department of Statistics Malaysia key findings; Statista (search summaries) | 3 (reporting a Rank 2 source) | The DOSM religion table was not retrieved, so **no percentage is given** in the note. [UNVERIFIED against DOSM] |
| «pergi kerja» and «balik rumah» are everyday speech; «pergi ke pejabat» and «balik ke rumah» are the standard written form | Sam's brief of 12 Nov 2026 | Sam's reference | Taken from the brief; Kamus Dewan not opened |
| Six places of worship are used as ordinary landmarks | Sam's decision of 12 Nov 2026 (Journal rows 66 and 67) | Sam's reference | Recorded in the ledger Journal |
| «lebih kurang» (more-less), «kereta api» (fire carriage), «bulatan» from ‹bulat› (round), «belok» a root word not a ber- form, «hadapan» more formal than «depan», «jam» with a third meaning (traffic) | Kata-Kata cards ms-c07-023, -046, -035, -025, -009, -049 | Sam's reference | [VERIFIED] against the card notes |

The note makes no claim about any real route, distance, road, station or building. All practice places, routes, distances, times and names are fictional and labelled so. The unit names no real-world road sign: «lintasan pejalan kaki» is from the ledger gloss only, and a search did not find the wording on a Malaysian sign, so it is not claimed to be one.

## Unverified and provisional

- **All Malay example sentences are mine.** They pass the ledger, register, affix and Malaysian-form checks, but none has had a native read. Please look especially at: «Jalan lurus, ya.», «Tandas di luar, bukan di dalam.», «Pagi Isnin selalu jam.» (traffic «jam» in speech), «Kalau tidak jam» / «Kalau jam, lebih lama.», «Hari ini jam. Bas lambat.», «Pejabat saya yang pertama.» (the first office on the right), «Pejabat saya di atas, di tingkat tiga.», «Bank di sebelah kanan, di antara kedai dan tokong.», «Kereta api tidak lambat.», «Lebih kurang seribu meter.», «Bateri telefon saya habis.», «Hari ini panas. Buka kipas.», «Tengok, telefon saya di bawah kerusi!», «Jam di dinding.», «Lintas jalan di lintasan pejalan kaki.», «Jalan ini bahaya.» and «Kondo saya dekat dengan surau.» [UNVERIFIED]
- **«gurdwara»**: spelling and Kamus Dewan headword status not confirmed (also «surau», «kuil», «tokong» and «gereja»: the KD4 check for L-1054 to L-1058 has not been run).
- **«jam» (traffic) as a spoken word** is from the ledger row L-0342 and card ms-c07-049 (Kata-Kata's "third meaning"); no usage source.
- **«tengok» as everyday speech.** The ledger gives no register. It is common colloquial Malay for "look"; the standard word is not in the ledger. [UNVERIFIED against Kamus Dewan]
- **The Japanese bridges.** へ / に / から ≈ «ke» / «di» / «dari» (all before the noun in Malay); 駅の前に versus «di depan stesen»; て-form versus «kemudian»; 乗る ≈ «naik»: general knowledge, not sourced. All Japanese is a draft for native review, including the full culture-note translation and the Japanese names of the five new religious-site words. I used コンド for "condo" and ロータリー for "roundabout".
- **In class:** timings, drill load and the 56-word unit have not been taught.
- **Kamus Dewan check** is still pending for L-0983 to L-1058.
- The page layout: the pattern pages are dense; the final PDF render overflowed once before I shortened four explanations, so the pack-fit check and the final render can disagree on dense pages (see `HANDOFF.md`).

## Findings for Kata-Kata (not changed here)

- **Scenario "Finding the LRT, then a Grab ride" (ms-c07-s01 to s13)** uses «tumpang tanya», LRT, Grab, Pavilion and «kalau tak jam» (spoken «tak» before «tidak» is taught). Only «kalau» and «jam» are ledger words.
- **Frame f01** («mahu pergi ke ___») uses «mahu» + «ke»; the example is «stesen LRT».
- **Cards ms-c07-036** («pintu masuk / pintu keluar») is shared by L-0330 and the duplicate L-0592.
- **Card ms-c07-009** («depan / hadapan») duplicates ms-c04-019 («depan», Ch4) with a second ledger row (L-0304 and L-0173).
- **Cards ms-c07-042 («hospital») and ms-c07-047 («kapal terbang»)** are chapter 7 cards but the words were placed in chapters 5 and 4.
- **No cards** exist yet for L-1051 to L-1058 («sewa», «bilik», «luas», «gereja», «kuil», «tokong», «gurdwara», «surau»), for L-1032 to L-1050 or for the Dunia scenes' new unit 6 and 7 usage. The "Di ruang tamu", "Telefon baru" and "Lintas jalan" cards (ms-d-rumah-ruang-tamu-*, ms-d-telefon-baru-*, ms-d-jalan-lintas-*) work as recognition cards as they are.
- **Sedia Kelas c07** (27 cards, frames f01 and f02, scene "rumah-ruang-tamu") works as the pre-class set.
- **Card ms-c07-016** («antara», note «di antara A dan B»): the unit teaches «di antara» as the use.

## Questions for Sam

1. **Places of worship:** the five new rows (gereja, kuil, tokong, gurdwara, surau) are in the ledger as Draft with your approval in the Journal. Please confirm the spelling of «gurdwara» for Malaysian use, and whether a Buddhist temple should be named apart from «tokong» (you did not select «vihara»). The Kamus Dewan check should run for all five.
2. **Duplicates:** retire L-0592 «pintu masuk» in the sheet (as L-1045 was retired)? And merge or retire L-0304 «depan / hadapan» into L-0173 «depan» (keeping «hadapan» as the formal form in L-0173)? I did not edit either.
3. **Retirement of "Di, ke and dari":** I retired this legacy grammar pack together with "Asking where" and "Directions and orientation" because it contained «kampus» and «tren» (not in the ledger) and unit 7 teaches di, ke and dari. Agreed, or should it be rewritten and kept?
4. **Proposed words:** add «kilometer», «sebulan», «tumpang tanya», «terus», «jangan» and «tangga»? Without them unit 7 cannot use real distances in kilometres, the short rent form, the usual polite opener or a negative command.
5. **«hospital» and «kapal terbang»** carry chapter 7 cards but were placed in chapters 5 and 4. I treated them as revision. Move them to core, or fix the cards?
6. **Writing block after unit 7** (Stage 1 plan: "directions by message"): not written in this batch, because the brief named unit 7 and the fast pack only. Write it now, or with chapter 8?
7. **Culture note:** it states left-hand traffic and its British-era origin (secondary sources only) and the 2020 census groups (secondary report of DOSM). Keep, or leave out until you have read the primary sources?
8. **Pilot:** did 35 core words in unit 6 and 56 in unit 7 feel like too many? The A/B cut I would make is in the teacher notes. Still open from step 5d: «tengok» (L-0577) is a chapter 7 recognition word as placed; is that fine now that the condo scenes do not need it?
9. **Review block after unit 6:** please teach it and say whether the three-part task fits 45 minutes.
10. **Chapter 8 waits for your go-ahead.**
