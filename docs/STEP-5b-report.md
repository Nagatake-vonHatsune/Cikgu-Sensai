# STEP 5b REPORT: Chapter 4, Batch 2

**Scope:** Malay A1 chapter 4 (time and tense markers): units **4A** and **4B** and the chapter 4 fast pack. Sam authorised chapter 4 on 12 Nov 2026 without waiting for chapter 3 pilot feedback, and pre-approved publication to main when the checks pass.

**Sources read:** the live Unified Curriculum Charter (Google Doc, read in full on 12 Nov 2026), `AGENTS.md`, `HANDOFF.md`, the Kata-Kata chapter 4 file (`curriculum/reference/katakata/c04.json`), the ledger snapshot, and the live ledger Journal and Rules tabs (read-only).

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests` (48 tests) pass on a full Git checkout at every commit below.

| Commit | Content |
| --- | --- |
| `453e68d` | Unit 4A, chapter 4 helper, tests, retirement of Clock time and Dates and days |
| `9f33cae` | Unit 4B with the timeline drill and the chapters 1 to 4 review block; retirement of Frequency and routines |
| `8fee84c` | Chapter 4 fast-course pack |
| this commit | This report and `HANDOFF.md` |

## Word accounting

All counts are unique ledger entries. A slash variant («sudah» / «dah», «balik» / «pulang») counts once.

| Unit | Theme | New core | Dunia recognition (by scene) | Revision (not counted, not tested as new) |
| --- | --- | ---: | --- | --- |
| 4A | Telling the time, days and dates, months, frequency, «bila» | **40** (27 + «tarikh» and 12 months, added 12 Nov) | **25**: "Hujan petang" 12, "Cuti ke pantai" 13 | 10 from chapters 1 to 3 |
| 4B | Tense and aspect markers, daily routine, the working day | **31** (27 + «sarapan», «sekejap», «hujung minggu», «lewat», added 12 Nov) | **30**: "Satu hari Encik Tanaka" 17, "Bangun pagi" 13 | 8 from chapters 1 to 3, 5 from unit 4A |
| **Total** | | **71** | **55** | |

**Ledger check.** The ledger places 54 core entries in chapter 4: the 48 rows placed "Ch4", plus «sekali» and «baru» ("Ch4; Ch6"), «bangun» (Dunia and Ch4, card ms-c04-046), «tunggu» (Dunia and Ch4, card ms-c04-051), and the pending rows «datang» (L-1006) and «bila» (L-1007). The 55 recognition entries are the four Dunia scenes that prime chapter 4, less «bangun». `tests/test_step5b_suite.py` recomputes both sets from the ledger and checks that 4A and 4B cover them exactly once.

**Words reused, not new.** «pagi», «tengah hari», «petang», «malam» (now chapter 1) and «selepas», «sebelum» (chapter 3) are listed under **Revision · 復習**, never as core. The test checks this.

### Why the split differs slightly from the brief

Sam's suggested themes give 31 words to 4A and 23 to 4B. To reach 27 / 27 I moved four words whose use is about the working day and tense, not about reading the clock:

- «masa» (time, as in «Encik ada masa petang ini?») and «waktu» («waktu pejabat», office hours) frame the working day in 4B;
- «depan» and «lepas» («minggu depan», «minggu lepas») are the time cues that drive «akan» and the past in the 4B timeline and transformation drills.

«tidak pernah» stays in 4A so the frequency scale (always … never) is taught whole; 4B then contrasts it with «pernah» and «belum pernah».

## Evidence for charter section 6 and section 14

| Minimum | 4A | 4B | Where it is tested |
| --- | --- | --- | --- |
| Eleven components | All eleven | All eleven | `test_components_and_vocabulary` |
| Vocabulary: every ledger word, JA and EN meaning, one example each, spoken forms marked | 62 entries, each with an example | 70 entries, each with an example; «dah» and «tengah» shown as spoken | entry count = example count = ID count |
| 3 to 5 patterns, 4 to 6 Q&A each, EN and JA explanation, Japanese note | 4 patterns × 5 Q&A (frames f01, f02) | 5 patterns × 4 Q&A (frames f03 to f07) | `test_patterns` |
| Drill types 1 to 5, at least 6 items each (30+) | 8 items each (40) | 8 items each (40) | `test_drills_keys_and_question_words` |
| Type 6 short dialogues (3+) | 4 | 4 | same |
| Cumulative question words | apa … berapa + «bila», «pukul berapa», «hari apa»; 9 tasks | same | same |
| Tense timeline drill (section 14) | (no markers yet) | Timeline on the board, 8 items on one 2 p.m. snapshot, Japanese bridge | `test_timeline_drill` |
| Real answer keys | Every drill item has its own answer | Every drill item, timeline item and self-check item | key regex per item |
| Model conversation 10 to 16 turns, gapped, changed facts | 12 + gapped (5 gaps, answers in key) + 12-turn variant | same | `test_conversation_…` |
| Listening 120 to 250 Malay words, before/during/after, 6+ items | 136 words, 8 items | 144 words, 8 items | same |
| Reading text with 5+ questions; guided writing with model | Class timetable, 6 questions, a weekly-schedule note | WhatsApp message about a moved meeting, 6 questions, a reply | same |
| Task: role cards, change of plan, success criteria | Weekly badminton slot; Saturday becomes unavailable | Busy-day catch-up; meeting moves to 1.30 | same |
| Culture note 150 to 300 words, full JA translation | 233 words | 189 words | word count; no leftover English in the JA |
| Test 15 to 20 items + speaking, every item tagged | 17 scored + 1 speaking; each item lists its own ledger words | same | `test_tests_and_plans` |
| Teaching plan: timings, prompts, Kata-Kata before and after | Five blocks, Sedia Kelas c04, Dunia scenes | Five blocks plus review block | same |
| Review block after 4B (Stage 1 plan) | | `ms-c04b-review-block`, registered in the catalogue | same |
| Fast pack: 2 to 4 pages, 15 to 20 words, patterns with 2 examples | 3 content pages, 20 words, 8 patterns, 10-turn conversation, task, 5-item self-check, self-study guide | | `test_fast_pack` |

**Chapter 4 Malay rules, tested:** no «kurang suku» anywhere (`test_chapter4_malay_rules`); every «dah» or «tengah» (other than «tengah hari») sits on a line that labels it spoken; clock time uses «pukul» with «pagi», «tengah hari», «petang» or «malam»; :15 is «suku», :30 «setengah», :45 is said in minutes. Only root verbs are used. The build's ledger, register, affix and Malaysian-form checks pass with no exceptions for 4A, 4B or the fast pack.

**Legacy packs.** Clock time, Dates and days, and Frequency and routines (learner pack and teaching plan each) are removed from the active catalogue; their source text stays in `curriculum/malay-course.txt`. Their three legacy exceptions (atau, saja, tak) are removed: **44 → 41**. The chapter 4 page status now reads "Step 5b chapter 4 suite · draft for pilot".

## Files changed

- **New:** `suite/chapter4_common.py`, `suite/ms_c04a.py`, `suite/ms_c04b.py`, `tests/test_step5b_suite.py`, this report.
- **Changed:** `suite/__init__.py` (chapter 4 grammar points ms-c04-g02 to g08, Dunia scene titles, unit loading, glosses for «sudah» / «dah» and «balik» / «pulang»), `suite/fast.py` (chapter 4 pack), `course.py` (retired packs, chapter 4 status), `catalogue.py` (review block after 4B), `curriculum/reauthored-units.json` (+ms-c04a, ms-c04b, ms-c04-fast), `curriculum/legacy-exceptions.json` (three removed), `curriculum/malay-mentions.json` (‹biasa›, ‹kurang suku›, ‹ke›, each with its source), `tests/test_catalogue.py` (retired titles), `tests/test_language_checks.py` (its example of a still-legacy unit moved from ms-c04a to ms-c05), and the generated `dist/` files.
- **Not changed:** the ledger, the Kata-Kata reference files, and the legacy lesson sources.

## Proposed ledger rows (approved by Sam on 12 Nov and added; see the last section)

| Word | Meaning | Proposed chapter | Why |
| --- | --- | --- | --- |
| tarikh | date | 4 | Forms and notices; the date is taught only as «berapa hari bulan?» for now |
| Januari to Disember | the twelve months | 4 | Dates are in the 4A brief, but no month names are in the ledger |
| hujung minggu | weekend | 4 | The natural word for the working-week topic; the units say «hari Sabtu dan Ahad» instead |
| sarapan | breakfast | 4 | L-0614 exists but is unplaced (Jambatan only); the routine has to avoid "breakfast" |
| sekejap | a moment («Tunggu sekejap») | 4 | Very common with «tunggu»; the units use «Tunggu lima minit» |
| lewat | late | 4 (spoken note) | Everyday alternative to «lambat» for "late"; recognise only |

Each needs the Kamus Dewan check before approval.

## Real-world facts used, and their sources

| Fact (unit 4A culture note) | Source checked | Rank | Status |
| --- | --- | --- | --- |
| All of Malaysia uses Malaysian Standard Time, UTC+8 | Malay Mail, 5 Mar 2024: MITI says MST is GMT+8 under the National Measurement System Act 2007 | 3 (reporting a Rank 2 statement) | [VERIFIED] via the report; the Act's text not opened |
| Until the end of 1981 Peninsular Malaysia was 30 minutes behind Sabah and Sarawak; it moved forward 30 minutes on 1 January 1982 (Malaysian Standard Time Act 1981) | The Star "QuickCheck", 16 Oct 2026; Wikipedia "Time in Malaysia" | 3 | [VERIFIED] date and offset; sources disagree only on the exact minute of the switch, which the note does not state |
| Malaysia is one hour behind Japan | UTC+8 vs UTC+9 | durable | [VERIFIED] |
| In Peninsular Malaysia the Employment Act 1955 limits normal hours to 45 a week, down from 48 from 1 January 2023 | Department of Labour Peninsular Malaysia (JTKSM) briefing on the Employment (Amendment) Act 2022; law-firm summaries (Rödl & Partner, ASEAN Briefing) | 2 / 3 | [VERIFIED] by summary; the Act's own wording not read |

Search links: The Star QuickCheck <https://www.thestar.com.my/news/true-or-not/2026/10/16/quickcheck-did-peninsular-malaysia-lose-30-minutes-on-new-year039s-eve-in-1981>; Malay Mail <https://www.malaymail.com/news/malaysia/2024/03/05/putrajaya-has-no-plans-to-adjust-malaysian-standard-time-to-gmt7-dewan-rakyat-told/121552>; JTKSM <https://jtksm.mohr.gov.my/sites/default/files/2023-02/Employment%20Act%20%28Amendment%29%202022%20.pdf>.

Unit 4B's culture note has no dated or legal facts. Its word notes come from Kata-Kata cards ms-c04-019, ms-c04-020, ms-c04-030, ms-c04-034 and ms-c04-041 and the chapter 4 scenario "Sudah makan?". No etymology was written beyond those card notes.

## Unverified and provisional

- **Dates:** «berapa hari bulan?» and «dua belas hari bulan» are taught as the spoken way to give the day of the month. Not checked against Kamus Dewan, including the spelling «hari bulan» against «haribulan». [UNVERIFIED]
- **Usage statements in the culture notes, not checked against a source:** «petang» lasts until about sunset; Malaysians mostly use the 12-hour clock in speech; «jam» is also heard for clock time in casual talk; «Sudah makan?» works as a friendly check-in; «balik» is more common than «pulang» in everyday speech. [UNVERIFIED]
- **Without «ke»:** «pergi kerja», «balik rumah» and «balik Jepun» are everyday Malaysian speech and are used because «ke» is a chapter 7 word. Standard written Malay would use «ke». Sam to confirm. Root verbs in «sedang baca e-mel» follow the Stage 1 affix rule, where the standard written form would be affixed.
- **Kamus Dewan check** still pending for «datang» (L-1006) and «bila» (L-1007), as for all of L-0983 to L-1031.
- **Japanese:** all of it is a draft for native review, including the full culture-note translations.
- **In class:** timings, drill load and the 4B review block have not been taught.
- All times, schedules, dates and names in the units are fictional and labelled so.

## Findings for Kata-Kata (not changed here)

The Kata-Kata chapter 4 file uses words placed after chapter 4: frame ms-c04-f02 «kopi» (Ch5); frame f04 «ke» (Ch7); frame f06 «durian» (not in the ledger); the scenario has «kedai mamak», «nasi kandar» and «di sana» (Ch5 and Ch7). Cikgu Sensai keeps the frame IDs but uses chapter 1 to 4 examples. The scenario's «Sekarang pukul satu suku» already follows Sam's correction (Journal, 6 Nov).

## Questions for Sam

1. **Dates:** is «berapa hari bulan?» / «dua belas hari bulan» right for chapter 4? «hari bulan» or «haribulan»? Shall month names and «tarikh» be added at chapter 4?
2. **Working week:** I left out the state differences in the weekend and anything about Friday prayers, as you asked. Would you like a neutral line such as "Most offices in the Klang Valley work Monday to Friday"?
3. **Split:** are you happy with «masa», «waktu», «depan» and «lepas» moving to 4B (reasons above)?
4. **«jam» for clock time:** the 4A note says you may hear it in casual speech but the course uses «pukul». Keep that or remove it?
5. **Without «ke»:** is «pergi kerja» / «balik rumah» acceptable until chapter 7?
6. **Proposed rows:** tarikh, months, hujung minggu, sarapan, sekejap, lewat.
7. **Chapter 5:** waits for your go-ahead.

## Sam's answers (12 Nov 2026) and the follow-up

| # | Sam's answer | What changed |
| --- | --- | --- |
| 1 | «tarikh» and «hari bulan» are separate. «Apa tarikh hari ini?» asks the full date; «Hari ini hari bulan berapa?» asks the day of the month (answer: the 11th). | 4A pattern 2, short dialogue 4 and the teacher notes now use «Hari ini hari bulan berapa?» → «Sebelas hari bulan.» The spelling is «hari bulan» (two words). «tarikh» waits for its ledger row (see below). |
| 1 (open) | Sam also wrote «Hari ini hari bulan apa?» with the answer "Thursday". | **Not taught yet.** Sam's legacy pack Dates and days ("Hari apa? untuk hari. Berapa hari bulan? untuk tarikh.") and charter section 14 ("Chapter 4: bila, pukul berapa, hari apa") both use «hari apa» for the weekday. 4A keeps «Hari ini hari apa?» until Sam confirms. |
| 2 | Yes to a neutral working-week line. | 4A culture note: "In Kuala Lumpur and Selangor most offices work Monday to Friday, and Saturday and Sunday are the weekend." Source: The Star, 9 Dec 2013 (the Sultan of Selangor keeps Saturday and Sunday as rest days) and Wikipedia "Public holidays in Malaysia" (Rank 3). Other states are not mentioned. |
| 3 | Split approved. | No change. |
| 4 | «pukul» and «jam» for clock time are both fine if explained. | 4A pattern 4 now says that «jam tiga» is common in casual speech and that the course practises «pukul tiga» (EN and JA). |
| 5 | Introduce ‹ke› / «di» gradually in explainers, not in the main line. | 4B pattern-focus explainer (EN and JA) and the vocabulary examples for «pergi» and «balik» show «pergi» ‹ke› «pejabat» and «balik» ‹ke› «rumah» as a "looking ahead, not tested" note. ‹ke› is a mention only, never drilled or tested; a test checks this. «di» is already a chapter 2 word. |
| 6 | Proposed ledger rows approved: tarikh, Januari to Disember, hujung minggu, sarapan, sekejap, lewat. | **Not yet in the ledger** (see below). |

### Second round (12 Nov 2026): Sam's further answers and the ledger update

| Sam | What changed |
| --- | --- |
| The day of the month is «Hari bulan sebelas», not «sebelas hari bulan». | Every date in 4A and the fast pack now puts «hari bulan» first: pattern 2, the listening (line 16: «Bulan ini, hari bulan dua puluh empat.»), short dialogue 4, the drill keys and the teacher notes. A test rejects the old order. |
| Share that some states have a Friday–Saturday weekend (Terengganu and Kelantan?), after checking. | **Checked:** Kedah, Kelantan and Terengganu have a Friday and Saturday weekend; Johor moved back from Friday–Saturday to Saturday–Sunday on 1 January 2025. Sources: Bernama, "Johor to revert weekend to Saturday and Sunday in 2025" (Oct 2024); The Star, "Johor's weekend to be Saturday-Sunday from Jan 1, 2025" (7 Oct 2024); Malay Mail, 18 Jan 2025 (the change in effect). All Rank 3 news reports of state decisions; no state gazette was read. The note gives the days only, not the reasons. **Correction to Sam's note: Kedah also has a Friday–Saturday weekend.** |
| Sheet writes allowed; add tarikh and the months to 4A (40) and hujung minggu, sarapan, sekejap and lewat to 4B (31); breaking 27/27 parity is fine. | Done (below). |
| «Hari ini hari apa?» works; «Hari ini hari bulan apa?» can be taken either way, depending on the listener. Verify. | **Could not verify:** a web search found no Malaysian source on «hari bulan apa» either way (the results were Indonesian calendar pages). 4A teaches the two clear questions («hari apa» for the weekday, «hari bulan berapa» for the date), and the teacher notes record Sam's point that «hari bulan apa» is heard both ways, so either answer is accepted. [UNVERIFIED beyond Sam's native judgement] |

**Ledger update (done):**
- The sheet was written first and logged in the Journal (rows 50 to 56).
- New rows L-1032 to L-1047: «tarikh», «Januari» to «Disember» (Malaysian spellings: Mac, Jun, Julai, Ogos, Disember), «sekejap» and «lewat». All are marked "Not yet checked" for Kamus Dewan.
- **A mistake of mine, corrected:** «hujung minggu» already existed as L-0702 (a Jambatan row with no chapter). L-1045 duplicated it, so L-1045 is now **Retired**, with its place cleared (IDs are never deleted), and L-0702 is placed in Ch4 instead. «sarapan» (L-0614) is placed in Ch4 the same way.
- The repo copies were regenerated from `Ledger!A1:T1048`. Before the change, regenerating them from the sheet reproduced the files byte for byte. The new hash is in `docs/step4-sources.json`.
- `suite.Ledger` no longer traces retired rows as taught words.
- Where the words are used:
  - 4A: a "Months" core group; «Apa tarikh hari ini?» → «Sebelas November.» in pattern 2, drill 4 (items 9 and 10), the reading notice (start date) and the test (V5 «tarikh», V6 «Ogos»).
  - 4B: «sarapan» in the listening, «sekejap» in a short dialogue, «hujung minggu» in the listening, and «lewat» beside «lambat» in the vocabulary.
- April, September and November are added to the English homograph list, because English text uses the same spellings.
- Core is now **71** (4A 40, 4B 31). Recognition stays 55. The build and all 49 tests pass.
