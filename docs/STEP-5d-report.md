# STEP 5d REPORT: Chapter 6, Batch 4

**Scope:** Malay A1 chapter 6 (comparing, choosing, describing places): **unit 6** and the chapter 6 fast pack. Sam authorised chapter 6 on 12 Nov 2026 and pre-approved publication to main when the checks pass. Nothing else was touched: no ledger edit, no review block, no chapter 7.

**Sources read:** `AGENTS.md`, `HANDOFF.md` (in full, including "Quality rules for chapter 4 onward"), the charter (`docs/handoff/charter-snapshot.md`, refreshed from the live Google Doc on 12 Nov 2026; the live Doc was not opened in this session, so any change after that refresh is not reflected), the Kata-Kata chapter 6 file (`curriculum/reference/katakata/c06.json`), the ledger snapshot (1,050 rows), and chapters 5 and 4 (source, helper, tests, report) as models.

**Status:** draft for Sam's pilot and native Japanese review. `python3 build.py` and `python3 -m unittest discover -s tests` (75 tests) pass on a full Git checkout at every commit below.

| Commit | Content |
| --- | --- |
| `79e76af` | Unit 6, chapter 6 helper, tests, registration, retirement of the legacy "Comparisons and superlatives" pack |
| `bd2420e` | Chapter 6 fast-course pack |
| next commit | Culture-note correction (the Strata Management Act's scope), this report and `HANDOFF.md` |

## Word accounting

All counts are unique ledger entries. A slash variant («mudah» / «senang») counts once.

| Unit | Theme | New core | Dunia recognition (by scene) | Revision (not counted, not tested as new) |
| --- | --- | ---: | --- | --- |
| 6 | Comparing, the most, very and too, choosing, describing places and things, kondo and stesen | **32** | **14**: "Main badminton" 14 | 25: 2 from chapter 4 (a new meaning), 14 from chapter 5, 9 from chapters 1 to 3 |

**Ledger check: 34 rows are placed in chapter 6, 32 are core, as the brief said.** `tests/test_step5d_suite.py` recomputes the sets from the ledger: a row whose placement has a "Ch6" part and no earlier "ChN" part is core (32); a Dunia row "primes Ch6" that is not core is recognition (14). The two rows placed in both chapter 4 and chapter 6 are **«sekali» (L-0188)** and **«baru» (L-0195)**; they are revision, and the test checks that neither is counted as core. **Core load: 32 in one unit** (charter: 20 to 40; the 13-unit plan has one unit for chapter 6).

| Group | Words |
| --- | ---: |
| Comparing and equal (lebih, kurang, daripada, sama, setinggi, semahal) | 6 |
| The most (paling, termurah, terbesar, terbaik, tercantik) | 5 |
| Very and too (sangat, amat, terlalu) | 3 |
| Choosing (yang mana, pilih, lain) | 3 |
| Describing places and things (cantik, bagus, lama, mudah / senang, susah, cepat, perlahan, selesa, ramai, sunyi, bising, bersih, kotor) | 13 |
| Places (kondo, stesen) | 2 |

**Words reused, not new.**
- **«baru»** and **«sekali»** are listed under "Chapter 4 · a new meaning in chapter 6", and the vocabulary entry says so: «baru» = new (chapter 4: just, «baru sampai»); «sekali» = very, after an adjective («cantik sekali», Kata-Kata card ms-c06-008); chapter 4: once («seminggu sekali»). The ledger Meaning (EN) of L-0188 still reads only "once" (see "Proposed ledger rows").
- **Chapter 5 adjectives and linking words that return** (14): besar, kecil, panas, sejuk, manis, pahit, pedas, sedap, penat, tetapi / tapi, yang, atau, sebab, kenapa.
- **Chapters 1 to 3** (9): mahal, murah, tinggi, panjang, berat, harga, tinggal, pejabat, badminton.
- «cepat» (L-0497) is placed "Dunia · Lintas jalan (primes Ch7); Ch6" and is core here; «lama» (L-0284) is placed "Ch6; Ch7" and is core here, with a note that chapter 7 uses it for time.

## Evidence for charter section 6 and section 14

| Minimum | Unit 6 | Where it is tested |
| --- | --- | --- |
| Eleven components | All eleven, plus the markers drill (no writing block: the Stage 1 plan puts a review block after unit 6, not a writing block) | `test_components_and_vocabulary` |
| Vocabulary: every ledger word, JA and EN meaning, one example each, spoken forms marked | 71 entries (32 + 14 + 25), each with an example; «senang» shown as spoken beside «mudah», «tapi» as spoken beside «tetapi» | entry count = example count = ID count |
| 3 to 5 patterns, 4 to 6 Q&A each, EN and JA explanation, Japanese note | 5 patterns × 6 Q&A. Six Kata-Kata frames: f01 and f02 share pattern 1 (lebih / kurang … daripada); f03 = pattern 2 (sama … dengan; setinggi, semahal); f04 = pattern 3 (paling; termurah …); f05 = pattern 4 (yang mana, pilih); f06 = pattern 5 (sangat, amat, terlalu, sekali) | `test_patterns` |
| Drill types 1 to 5, at least 6 items each (30+) | 8 items each (40) | `test_drills_keys_and_question_words` |
| Type 6 short dialogues (3+) | 4 | same |
| Cumulative question words | apa … hari apa, bagaimana (spoken macam mana), kenapa = mengapa = apa sebab (answered with sebab or kerana), **+ yang mana**; 12 tasks with model questions; the choice drill uses yang mana, berapa, di mana, bila, bagaimana, kenapa, siapa and apa | same |
| Tense and aspect markers return (section 14) | "Markers with comparisons": «masih», «sudah», «akan», «belum» with «lebih» and the new adjectives, 8 items, Japanese bridge, key | `test_markers_return` |
| Real answer keys | Every drill item, markers item, reading item and test item has its own answer | key regex per item |
| Model conversation 10 to 16 turns, gapped, changed facts | 13 turns choosing a condo, gapped (5 gaps, answers in key), 13-turn variant with different facts | `test_conversation_…` |
| Listening 120 to 250 Malay words, before/during/after, 6+ items | 125 words, 9 items | same |
| Reading text with 5+ questions; guided writing with model | A condo listing message (fictional prices), 7 questions, a three-sentence reply with a model | same |
| Task: role cards, change of plan, success criteria | Choosing a condo; the condo A chose is taken («Orang lain sudah ambil kondo B.») and A chooses again with «Yang mana …?» and «pilih» | same |
| Culture note 150 to 300 words, full JA translation | 242 words, four paragraphs; no leftover English in the Japanese | word count and a Japanese-cell check |
| Test 15 to 20 items + speaking, every item tagged | 19 scored (6 listening, 6 words, 3 grammar, 4 reading) + 1 speaking; every item lists the ledger words it tests; word items use core words only | `test_tests_and_plans` |
| Teaching plan: timings, prompts, Kata-Kata before and after | Five blocks, Sedia Kelas c06 (16 cards, frames f01 and f02), the Dunia scene "Main badminton" | same |
| Fast pack: 2 to 4 pages, 15 to 20 words, patterns with 2 examples | 3 content pages, 20 words, 5 patterns × 2 examples, 10-turn conversation, task with change of plan, 5-item self-check, self-study guide | `test_fast_pack` |

**Chapter 6 Malay rules, tested:**
- **Whole words only.** «termurah», «terbesar», «terbaik», «tercantik», «setinggi» and «semahal» are taught as whole ledger words. No drill builds a new ter- or se- word: the test fails if any marked span contains ter- or se- plus one of 32 listed adjectives that is not one of the six. «paling» + adjective and «sama … dengan» are the productive forms; the explanations and teacher notes say building new words waits for a later chapter (productive ter- is chapter 16, as in the brief). The build's affix check passes with no exceptions.
- **Standard first, spoken marked:** «mudah» first, «senang» marked spoken; «tetapi» before «tapi». No «nak», «tak», «dah» or «sikit» in unit 6. Every line with a spoken form carries a "spoken" label (tested).
- **No word placed after chapter 6, and no word missing from the ledger, is used** (the ledger check in `build.py` fails on either in a re-authored unit). Out of reach were «dekat», «jauh», «ke», «kedai», «sini», «sana», «tingkat», «lif», «bas», «kereta», «jalan», «tengok», «sewa», «bilik» and «luas». The unit works around them rather than bending the Malay.
- No faith-specific greetings or expressions, no medicine or doses (the body words in "Main badminton" are labels only).
- Root verbs only; no ber- or me- forms. Mentions are ‹…›-marked with a Kata-Kata or ledger source (see "Files changed").

**Natural Malay.** The scenes are choosing a condo with an agent, a Monday talk about the new condo and the way to work, a condo listing, comparing two players. Where the in-scope words could not make a natural sentence I changed the scene:
- The Kata-Kata scenario compares condos by distance to the LRT («dekat», «jauh», «stesen LRT»); none of those is available, so the comparisons are size, price, noise, age, comfort and cleanliness, and «stesen» appears in the listening and the culture note («Stesen sangat ramai pukul lapan.»).
- Rent: «sewa» is not in the ledger, so the listing says «RM 3,200 setiap bulan» beside each condo and the practice questions use «harga». I think a Malaysian reading «setiap bulan» next to a price in a listing understands a monthly rent, but I flagged it (see "Unverified").
- Viewing a condo needs «tengok» or «lihat» (not available before chapter 7), so no line asks to see a condo.

**Legacy packs.** "Comparisons and superlatives" (learner pack and teaching plan) is removed from the active catalogue; its source text stays in `curriculum/malay-course.txt`. Two legacy exceptions for ms-c06 (antara, tapi) are removed: **34 → 32**. The chapter 6 page status now reads "Step 5d chapter 6 suite · draft for pilot".

## Files changed

- **New:** `suite/chapter6_common.py` (copy of the chapter 5 helper: ms-c06 ids, `GRAMMAR6`, «yang mana» in the question-word set, the markers drill renamed "Markers with comparisons", no extra block used), `suite/ms_c06.py`, `tests/test_step5d_suite.py` (13 tests), this report.
- **Changed:** `suite/__init__.py` (grammar points ms-c06-g02 to g06, scene title "Main badminton", unit loading), `suite/fast.py` (chapter 6 pack), `course.py` (chapter 6 has no legacy items, "Comparisons and superlatives" retired, chapter 6 status), `curriculum/reauthored-units.json` (+ms-c06, ms-c06-fast), `curriculum/legacy-exceptions.json` (two removed), `curriculum/malay-mentions.json` (+‹ter›, ‹dekat›, ‹jauh›; ‹se› gains the chapter 6 cards as a second source), `curriculum/malay-proper-nouns.json` (E, F, G as condo labels), `tests/test_catalogue.py` (retired titles), `tests/test_language_checks.py` (its "not yet re-authored" fixture moves from ms-c06 to ms-c07), `HANDOFF.md`, and the generated files in `dist/` and `docs/step4-authored-scope.json`.
- **Not changed:** the ledger (both copies and the hash), the charter snapshot, the Kata-Kata reference files and the legacy lesson sources.

## Proposed ledger rows

I did not add anything. These are the words the condo scenes needed and could not use; none is used in unit 6. Each would be "Not yet checked" for Kamus Dewan.

| Word | Meaning | Why |
| --- | --- | --- |
| sewa | rent; to rent | A condo listing gives a monthly rent; now «setiap bulan» stands beside the price |
| bilik | room | Comparing condos by rooms; today only «bilik air» (L-0555) is placed |
| luas | spacious, wide | A natural partner of «besar» for homes; Kata-Kata does not list it |

Also for Sam's decision (no new rows):
- **L-0188 «sekali»**: Meaning (EN) is "once" and Meaning (JA) "一回"; the chapter 6 card says "very (after adjective)". Proposed: "once; very (after an adjective, Ch6)" and "一回；とても（形容詞のあと）".
- **L-0577 «tengok»** is placed in chapter 7 ("Dunia · Di ruang tamu"). Viewing a condo («Boleh tengok kondo itu?») is the most natural chapter 6 request after "which one". Move it earlier, or leave it for chapter 7?

## Real-world facts used, and their sources

| Fact (unit 6 culture note) | Source checked | Rank | Status |
| --- | --- | --- | --- |
| «kondo» is the everyday Malaysian word for a condominium: a block of homes with shared areas; it is a headword in Kamus Dewan | Ledger L-0294 (KD4 check "Headword", p.2172; Kata-Kata card ms-c06-033 "condominium") | Sam's reference | Taken from the ledger as written; Kamus Dewan itself not opened |
| Under the Strata Management Act 2013 (Act 757), in Peninsular Malaysia and Labuan, shared areas of a strata development such as a condominium are looked after first by a joint management body of the owners and, once strata titles are issued, by a management corporation | Wikipedia, "Strata Management Act 2013"; PropertyGuru Malaysia, "The Strata Management Act (SMA) 2013 In Malaysia, And How It Affects You"; Low Partners, "Strata Management Act 2013" parts 1 and 2; Shah Alam city council (MBSA) page "Joint Management Body (JMB) / Management Corporation (MC)" (search summaries; the pages and the Act were not opened) | 3, plus one 2 (local government) | [VERIFIED] across several secondary sources; **the statute text was not read**. A first search did not confirm that condominiums fall under the Act, so I searched again; the guides name "apartments, condominiums, flats, townhouses" as covered. The scope line (Peninsular Malaysia and Labuan) is also from those guides |
| The Klang Valley has a rail network that includes LRT, MRT, monorail and KTM Komuter lines | Wikipedia, "Klang Valley Integrated Transit System" and "RapidKL"; Prasarana and KTMB operators (search summary) | 3 | [VERIFIED] in general. The sources disagree on line names and opening dates, so the note names no line and no date |
| ‹se-› + «tinggi», ‹se-› + «mahal»; «terbaik» from «baik» with ‹ter-›; «sekali» after an adjective = very, same word as "once"; «baru» = new, also "just"; «bersih» is a root that only looks like a ber- word; the agent's «Kondo B kurang besar» | Kata-Kata cards ms-c06-005, -006, -014, -008, -021, -031 and scenario ms-c06-s03 | Sam's reference | [VERIFIED] against the card notes |
| «kurang» + an adjective means "less" or "not so" | Ledger L-0266 ("less") and the scenario line above | Sam's reference | Meaning from the ledger; the note does not say it is polite or a softener |

The note makes no claim about rents, prices, neighbourhoods or how many people live in condominiums. All practice prices, condo labels (A to G) and names are fictional and labelled.

## Unverified and provisional

- **All Malay example sentences are mine.** They pass the ledger, register, affix and Malaysian-form checks, but none has had a native read. Please look especially at: «Pisang hari ini semahal mangga!», «Anak saya sudah setinggi saya.», «Harga kondo A dan kondo D sama?», «Kondo B kurang besar daripada kondo A.» and «kurang susah», «Kondo D bising?», «RM 3,200 setiap bulan» beside a condo (rent without «sewa»), «Orang lain sudah ambil kondo B.», «Kenapa encik tidak pergi lebih awal?», «Pukul lapan stesen paling ramai.», «Kondo kawan encik cantik?», «Dapur kondo baru bersih sekali!», «Bilik air kondo itu kotor.», «Saya amat gembira hari ini.» (formal), «Terlalu pedas untuk saya.», «Dia juara badminton.», «Skor kita sama!» and «Siku saya tidak sakit hari ini.» [UNVERIFIED]
- **«senang» as the spoken form of «mudah».** The brief's example and the Kata-Kata slash entry ("mudah / senang") give no register. My search found «senang» mostly defined as "happy, at ease" (Indonesian KBBI) and a Wiktionary label "dated, dialect" for the "easy" sense (the language of that entry was not confirmed); I found no Kamus Dewan entry. The unit shows «mudah» first, «senang» as spoken, and the teacher notes say «senang» is also heard with another meaning. [UNVERIFIED against Kamus Dewan]
- **«amat» as formal «very» and «sangat» as the everyday word:** from the ledger ("very (formal)"); no usage source.
- **The Japanese bridges.** 一番 ≈ «paling» (same order), ～すぎる ≈ «terlalu», どれ / どちら ≈ «yang mana», B より before the standard in Japanese and after in Malay: general knowledge, not sourced. All Japanese is a draft for native review, including the full culture-note translation. I used コンド for "condo" in the Japanese lines (the Kata-Kata gloss is マンション).
- **«kondo» "headword in Kamus Dewan"** and the Strata Act line: see the table above; neither primary source was opened.
- **In class:** timings, drill load and the 32-word unit have not been taught.
- **Kamus Dewan check** is still pending for L-0983 to L-1050 (including «kelakar», «kuah», «mengapa», «kerana»). Chapter 6 words L-0265 to L-0295 and the Dunia words L-0969 to L-0982 carry a KD4 check in the ledger, taken as given.
- All prices, condo labels, names and situations are fictional and labelled so.

## Findings for Kata-Kata (not changed here)

- **Scenario "Choosing a condo" (ms-c06-s01 to s08)** uses «dekat» (L-0313, chapter 7), «jauh» (L-0314, chapter 7) and «stesen LRT» (LRT is not in the ledger), all before their chapter. «paling baru» (s07) is fine.
- **Frames f03 and f04** show open slots: «A sama ___ dengan B. / A se-___ B.» and «___ paling ___. / ___ ter-___.» A learner can read these as productive se- and ter-. Cikgu Sensai teaches only the six whole words until chapter 16; the frames could name the whole words (setinggi, semahal; termurah, terbesar, terbaik, tercantik) instead of the slot.
- **Card ms-c06-002 «kurang»** carries the note "Also 'minus' in telling time (Ch4)", but Sam's Journal entry of 6 Nov says «kurang suku» is not used. The note could go.
- **Card ms-c06-008 «sekali»** teaches "very (after adjective)", while ledger L-0188 says "once" (see the proposed edit).
- **Card ms-c06-023 «mudah / senang»** has no register note.
- **Card ms-c06-025 «cepat»**: the ledger lists it as "Dunia · Lintas jalan (primes Ch7); Ch6" with cards ms-d-jalan-lintas-09 and ms-c06-025; the card is a chapter 6 card.
- **Sedia Kelas c06** (16 cards, frames f01 and f02, scene "sukan-badminton") works as the pre-class set; no change needed.
- **Dunia "Main badminton"** is recognition only here; the ledger moved «badminton» (L-0968) to chapter 2 but its Dunia card ms-d-sukan-badminton-01 stays in the scene.
- **No Kata-Kata card or frame** exists for the "which one … choose" exchange beyond f05 («Yang mana lebih ___?»); «Saya pilih ___» has no frame.

## Questions for Sam

1. **Ledger rows:** may I add «sewa», «bilik» and «luas» (Ch6)? Without them the condo scenes say «setiap bulan» beside a price and never count rooms.
2. **«tengok» (L-0577, chapter 7):** bring it forward to chapter 6 so learners can ask to see a condo?
3. **L-0188 «sekali»:** change Meaning (EN) to "once; very (after an adjective, Ch6)" and Meaning (JA) to "一回；とても（形容詞のあと）"? (I did not edit the ledger.)
4. **«senang» as the spoken form of «mudah»:** is that right, and should it be marked "spoken" or "everyday"? The Kamus Dewan check should confirm.
5. **Se- and ter- words:** confirm that only the six whole words are taught until chapter 16, and that Kata-Kata frames f03 and f04 should name them instead of showing a slot.
6. **Review block after unit 6** (Stage 1 plan: review blocks after 3A, 4B and 6): not written in this batch because the brief named unit 6 and the fast pack only. Write it now, or with chapter 7?
7. **Pilot:** did 32 core words feel like too many? If so, the cut I would make is A/B: comparing, equal and most first; very, too, choosing and the describing words second.
8. **Culture note:** it names the Strata Management Act 2013 and the Klang Valley rail network (sources above, secondary, statute not read). Keep, or leave out until you have read them?
9. **Chapter 7 waits for your go-ahead.**
