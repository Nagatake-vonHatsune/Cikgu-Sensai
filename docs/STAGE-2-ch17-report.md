# Stage 2 build step 4, chapter 17: unit 17 (standard and spoken Malay, particles, invitations)

**13 November 2026 · Claude.** Authorised by Sam (build step 4, chapter 17 instruction, 13 Nov 2026): the chapter 16 fixes in their own commit, then the chapter 17 suite; push to main when the checks pass; **stop after chapter 17 for Claude's review** before the clean-up pass and chapter 18. Started at `680d4bd`. Kata-Kata (read only) is the pinned copy at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited. I did not re-open the charter Google Doc (the brief listed the files to read); nothing in the work depends on a charter change.

## Summary

- **Chapter 16 fixes (own commit, `d5e3958`, on main).** «terjatuh» takes «ke» («Cawan itu terjatuh ke lantai.», «Telefon saya terjatuh ke lantai.»; «Air kopi tertumpah di meja.» kept). The aspect drill has no «sudah» or «sedang» before an accident ter- verb («Kunci saya masih di dalam rumah.», «Mei Ling masih tersangkut di jalan yang sesak.», teacher note: «masih» and «baru» are fine). Mei Ling is Block C, unit 5-2 (her chapter 12 form) in the writing model and in the changed-facts variant (which said Block A, unit 8-5); I checked every chapter 10 to 16 line: Tanaka is Block B, unit 12-3, Siti is Block A, unit 8-1, and there is no other mix-up. Superlatives after a noun take «yang». **The model conversation ends at the office scene (s11); the clinic scene s12 to s17 is its own dialogue in the Block E part of the teaching plan** (a small optional `scene_e` key in the shared helper; the fast pack's model ends at s11 too). Sam's answers are in `docs/stage-2-decisions.md` section 13; «tidak apa-apa» and «masalah» are marked "recommended". 278 tests and the build passed.
- **Chapter 17 (`5e62076`).** One full A2 unit (five 45-minute blocks) and the chapter 17 fast pack, registered in `curriculum/reauthored-units.json` (zero gaps, zero violations). The plan gives chapter 17 **no review block and no writing block**, so none was built. `python3 build.py` passes (**542 packs, 3,335 pages**, all fit-checked; **20 violations and 199 gaps, all from older content**, none in chapter 17; unchanged). **295 tests** pass (278 before, plus 17 in `tests/test_stage2_ch17.py`).

## Blocks and timings

| Block | Unit 17: the dinner invitation, the café and the mamak | Minutes |
| --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns 20, first substitutions 5 | 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | 45 |
| C | Listening (Rahman invites Mei Ling and Tanaka to the mamak) 15, reading (a written invitation and a reply) and writing 10, task (an invitation, a refusal and a new day) 15, recall 5 | 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview 10 | 45 |
| E | Scene transfer: Kata-Kata s01 to s20 as listening 10, role-play 15, a changed fact 10, culture note 5, recall 5 | 45 |
| Fast | Chapter 17 fast pack, one 45-minute session | 45 |

Full course: **5 blocks = 3.75 class hours** for chapter 17 (no extra block), plus 1 fast block. Self-study planning figure: 3 hours for the unit.

## What the unit contains

| | Unit 17 |
| --- | --- |
| Core / recognition / revision | 24 / 0 / 47 |
| Core groups | invitations 8, accepting and declining 6, standard and spoken pairs 8, two particles 2 |
| Patterns (Kata-Kata frames) | five: f01 «Sudikah encik ___?»; f02 «Sayangnya saya tidak ___. Lain kali, ya?»; f03 «Bagaimana kalau ___?»; f04 and f05 together (saying yes, taking a no kindly); f06 «Jom makan kat ___ ni!» (spoken) |
| Drills | 8 + 8 + 10 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks |
| Model conversation | 16 turns (Kata-Kata s01 to s16 word for word, none joined), gapped, a 10-turn variant (Mei Ling is invited and suggests Thursday); the mamak scene s17 to s20 is the Block E dialogue |
| Listening | 123 Malay words, 8 questions (a lunch invitation that is moved; «takpe», «kat», «tu», «tak tahan», «macam tu», «Set!», «lah», «kan») |
| Reading and writing | a written invitation and a written reply in standard Malay, 7 questions; write three or four sentences to reply, no spoken forms |
| Task | An invitation, a refusal and a new day (Puan Aini and a colleague); change: the boss is not free on Friday; then replay the last turns as friends in spoken Malay |
| Culture and usage note | 4 paragraphs, 238 words: two registers; ちょっと… against «Sayangnya …» and «Lain kali, ya?»; «lah» and «kan»; general knowledge (labelled) and «belanja» |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) |

**Standard first, spoken labelled.** Every pair is taught standard first, then the spoken form with the label "spoken": «tidak mengapa» → «takpe» / «tak apa»; «tidak boleh tahan» → «tak tahan» (with «Saya tak nak pedas.» and «Saya tak suka pedas.»; «boleh tahan», chapter 5, means "not bad"); «setuju» → «set»; «seperti itu» → «macam tu»; «di» → «kat»; «ini» → «ni»; «itu» → «tu»; «jom» against «mari». A test checks the order in the vocabulary list and the labels; the build's register check passes. The Opener and the goals never use a spoken form in «…», because the register check reads the order of the components.

**Particles.** «lah» (joined in writing: «Takpelah.», «Bolehlah.») and «kan» are heard in the model and the listening, taught as recognition only, and are in **no** key, task card, test answer or speaking key (`test_particles_are_recognition_only`; the one place a key must name them is quoted as a ‹…› mention, as the step 2 rule says; ‹lah› and ‹kan› are in `curriculum/malay-mentions.json`).

**Teacher notes the brief asked for** (all tested): when to use the spoken forms (friends, colleagues, the mamak) and when not (emails, forms, notices, meetings with clients); Japanese learners over-using «lah» (and that it is not a copy of よ or ね); polite refusal (soften, give a reason, offer another time) against Japanese ちょっと…, labelled a teaching hypothesis; «belanja» means "treat", not "spend" («berbelanja», chapter 10). The notes also cover «sudi» (for the other person only), «jom», «mari», «ajak» and «jemput» as different tones, «kami» against «kita» in an invitation, and «dari» (places) against «daripada» (people, offices): «jemputan daripada Puan Aini».

**Kata-Kata alignment.** The same frames f01 to f06; all six frame examples and all **20** scenario lines appear word for word; the model is s01 to s16 (s07 and s08 are both Puan Aini, who asks the boss between them, and are not joined); s17 to s20 are the Block E dialogue. Kata-Kata writes the quoted words in s13 and s15 with inner «…»; the unit shows them as ‘…’ because «…» marks Malay spans (a test compares the lines after that one change). Card IDs are cited in the vocabulary, the teacher notes and the culture sources (ms-c17-002, -003, -014 to -017, -022 to -024).

**Rules applied.** No «Assalamualaikum», «Waalaikumsalam» or other faith-specific expression; the Kata-Kata Sedia Kelas list also names a Dunia card about a festival open house (ms-d-perayaan-raya-05), which the unit does not use (a teacher note says so; see question 4). No medical reason for refusing food is taught or asked (a test checks it). «dari» only before a place; no «tangguhkan» or «batalkan»; the bare root only in Kata-Kata's own lines («Saya tanya bos dulu.») and requests; all names, places and times fictional.

## Core-word coverage

All 24 core words appear in the unit outside the vocabulary list (the test checks this and that every revision word is really used). **12 of the 24 are tested** (a word counts once it is a listening, word, grammar or reading item); all 24 are in the fast pack (Sam's ruling of 13 Nov: fast packs hold all core words). "Practised only" means the word is drilled and used in scenes but is not a scored test item.

| Tested | Practised only |
| --- | --- |
| jemputan, sudi, lapang, belanja, singgah, cadangan, lain kali, setuju, menolak, sayangnya, tidak boleh tahan, set | ajak, segan, malangnya, tidak mengapa, tak tahan, kat, ni, tu, macam tu, takpe, lah, kan |

The spoken forms (kat, ni, tu, macam tu, takpe, tak tahan) and the two particles are mostly practised, not scored: the test items are listening, words, grammar and reading, and the spoken forms are marked wrong or right by context in conversation, never by a fixed key (the step 2 rule allows the standard form in every key). «lah» and «kan» are practised by hearing only, by design. Thin spots: «ajak» appears in one pattern line, the vocabulary example and a teacher note; «segan» and «malangnya» appear in the model, the variant, pattern 2 and the reading. A pilot teacher may want one more scored item for «tidak mengapa» and for «segan».

## Code and data changed

- `suite/ms_c17.py` (the unit) and the chapter 17 fast pack in `suite/fast.py` (`C17_WORDS`, `chapter17`, `STAGE2_PACKS`). The unit imports `chapter10_common.unit_dict`; the helper gained the optional `scene_e` key (chapter 16 fix).
- `suite/__init__.py`: grammar points ms-c17-g02 to g09; the unit is loaded; GLOSS entries for the fast-pack word list (L-0931, L-1252, L-1261, L-1262, L-1263, L-1264, L-1266, L-1267); **«mamak» added to `ENGLISH_HOMOGRAPHS`** (English prose says "the mamak stall"; question 3).
- `course.py` chapter 17 «Spoken Malay and invitations» (unit 17), genre Invitations, status line. `catalogue.py`: seventeen chapters, chapter 17 goal and focus. No extra block.
- `curriculum/reauthored-units.json`: ms-c17 and ms-c17-fast. `curriculum/malay-mentions.json`: ‹cadang›, ‹sayang›, ‹lah›, ‹kan› with sources. `curriculum/legacy-exceptions.json` unchanged (20).
- **`build.py` (memory fix, same output):** the build needs `insert_htmlbox`, which keeps memory until its document is closed; the fit check and the PDF loop used one document each, so the build grew to about 14 GB and was killed (exit 137) once the page count passed about 3,300. The fit-check scratch document is now replaced every 100 checks and the PDF document is reopened every 300 pages. The build now peaks near 0.6 GB for the fit check. The packs, pages and checks are unchanged.
- Tests: `tests/test_stage2_ch17.py` is new (17 tests: ledger partition, core-word use, standard before spoken and the labels, the four teacher notes, particles never required, «tidak boleh tahan» / «belanja» / «sudi», «dari» / «daripada» and «kami» / «kita», Kata-Kata alignment with all 20 lines and no join, register and scope, no extra block, minimums, openers, culture note, Japanese, fast pack, registration). `tests/test_stage2_ch16.py` has one new test and the model change. `test_catalogue` expects 17 chapters, 24 units, 120 blocks and 264 slots, levels A1 × 9 + A2 × 8.
- `tools/check_spans.py` was run on the unit file at chapter 17 before building: 0 problems (354 spans).
- Docs: `docs/stage-2-decisions.md` section 13; `docs/stage-2-plan.md` (a chapter 17 note); `HANDOFF.md`.

## Lines a native speaker should read first

These are my judgement calls; everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. Pattern 1: «Sudikah puan makan dengan kami hari Jumaat?» and «Terima kasih atas jemputan puan. Saya datang.»
2. Pattern 2: «Saya segan untuk menolak jemputan encik, tetapi saya tidak lapang.» and «Sayangnya saya tidak lapang hari Sabtu dan hari Ahad.»
3. Pattern 2: «Malangnya saya ada mesyuarat. Lain kali, ya?»
4. Pattern 3: «Tempat itu jauh.» «Bagaimana kalau kita naik teksi?»
5. Pattern 4: «Hari Jumaat, pukul tujuh. Setuju?» «Set!» and «Maaf, saya tidak lapang.» «Takpe. Kita cari hari lain.»
6. Pattern 5: «Jom minum kat kafe ni! Saya belanja!» «Terima kasih! Saya minum teh. Lain kali saya belanja.»
7. Pattern 5: «Makanan kat sini pedas.» «Saya tak tahan pedas. Saya tak nak pedas.»
8. Listening: «Terima kasih, Encik Rahman. Tetapi makanan kat situ pedas, kan? Saya tak tahan pedas.»
9. Listening: «Kalau macam tu, saya setuju. Esok saya lapang.» and «Ya, esok saya belanja. Lain kali, Mei Ling belanja pula, ya?» «Bolehlah. Lain kali saya belanja.»
10. Variant: «Terima kasih, puan. Saya tunggu.» and «Setuju. Terima kasih, Puan Aini.»
11. Reading: «Terima kasih, Puan Aini. Saya segan untuk menolak jemputan puan, tetapi hari Jumaat saya tidak lapang. Bagaimana kalau hari Khamis? Lain kali, ya?» and «Encik Tanaka, ini jemputan makan malam pejabat. Hari: Jumaat. Pukul: tujuh malam. Tempat: kedai makan dekat pejabat.»
12. Model: Kata-Kata s13 and s15 with the inner words in ‘…’ («Tadi cik cakap ‘takpe’. Itu sama dengan ‘tidak mengapa’, ya?»), and the writing model «Terima kasih, Puan Aini. Saya setuju. Hari Jumaat saya lapang. Saya singgah di pejabat pukul enam.»

All Japanese is a draft for the native review. The bridges (ちょっと… against «Sayangnya …»; 「ですます」と「くだけた形」 against the standard and spoken forms; よ・ね against «lah» and «kan» (a "not a copy" statement)) are teaching hypotheses.

## Questions for Sam

1. **The model is s01 to s16, one line to a turn.** Your rule (no join across a scene change) leaves the model at 16 turns: s01 to s09 (the office), s10 to s16 (the café and the talk about «takpe», «lah» and «kan»); s07 and s08 are both Puan Aini and stay separate. The mamak scene (s17 to s20) is the Block E dialogue. Is it acceptable that the model crosses from the office to the café (no join) and ends before the mamak, or would you rather the model stop at s09 (nine turns, below the charter's ten)?
2. **Spoken forms in the Opener.** The goals and the recall key use no spoken form in «…», because the register check requires the standard form to be taught first (vocabulary or model). The goals say "the spoken forms" in English. OK?
3. **«mamak» in English prose.** I added «mamak» to `ENGLISH_HOMOGRAPHS` so that "the mamak stall" in English text is not flagged; the Malay uses are all marked. The alternative is «mamak» in every English line (about twelve places). Which do you prefer?
4. **The Sedia Kelas festival card.** Kata-Kata's Sedia Kelas list for chapter 17 includes ms-d-perayaan-raya-05 (a festival open house). The unit teaches no festival and no faith-specific expression, and the only invitations are to an office dinner, a café and the mamak. Do you want the festival card kept out of Cikgu Sensai for good?
5. **Five patterns.** f04 and f05 share pattern 4 (saying yes, taking a no kindly); the order is f01, f02, f03, f04 and f05, f06. Is that the pair you want merged?
6. **Spoken forms with a senior colleague.** The task asks learners to replay the last turns as friends in spoken Malay and the main exchange with Puan Aini in standard Malay. Is that the right line (spoken with friends and colleagues you know, standard with someone senior)?
7. **Menu names.** Title «Spoken Malay and invitations», genre «Invitations». OK?
8. **Build change.** The memory fix in `build.py` (same output) is needed to build more than about 3,300 pages in this environment. OK to keep?

## Not verified

- **Kamus Dewan:** none of the chapter 17 forms was checked (end of the project, ledger Journal row 128). The cards' notes are the source for «tidak boleh tahan», «tak tahan», «takpe», «belanja», «lah» and «kan»; «sudi», «menolak» and «segan» are as the cards give them.
- **Facts:** the culture note states no figure, rule or date about Malaysia; the sentence about colleagues eating together is general knowledge, labelled and not source-checked. The refusal norms (soften, give a reason, offer another time) and the ちょっと… comparison are teaching hypotheses. The names, places, times and prices are fictional.
- **PDF:** the build's fit check passed for every page. I did not review the pages by eye.
- **Environment:** the build needed `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (after `apt-get update`); I installed them in the session. The checkout was shallow and was unshallowed first.

## Word proposals backlog (not in the ledger; one table for Sam to approve in one go)

Builders rewrote the lines instead and added no rows. "Sam" means Sam has already recommended or approved the word; "Claude" is my recommendation. Chapter 17 added three words; the rest are carried from the HANDOFF backlog.

| Word | Chapter | Why it came up | Recommendation |
| --- | --- | --- | --- |
| «kepada» (to, for a person) | 11 | «menghantar emel kepada pengurus»; the unit says «Saya menghantar fail itu ke Osaka.» | Claude: add |
| «sehari» (a day, per day) | 11 | the price of a rented car; the unit says «untuk satu hari» | Claude: add |
| «bukit» (hill) | 11 | «mendaki bukit»; the unit says «mendaki dengan kawan saya» | Claude: add (low priority) |
| «menempah» (to book) | 11 | booking a car for the trip («tempah» is chapter 4) | Claude: add |
| «disemak», «disimpan», «dipesan», «dipilih», «dipinjam», «dikira», «diisi» | 11 | di- partners of the 11B verbs; the ledger has di- rows only for the chapter 9 list | Claude: add only the ones a unit really uses |
| «menyapu» (to sweep) | 11 | the s → ny trap; quoted only as a ‹menyapu› mention | Claude: drop (mention is enough) |
| «kolam renang» (swimming pool) | 10 | recorded in `docs/STAGE-2-ch10-report.md` | Claude: add |
| «taman» (park) | 10 | same | Claude: add |
| «seminggu» (a week) | 10 | same | Claude: add |
| «penuh» (full) | 10 | same | Claude: add |
| «bersukan» (to do sport) | 10 | same | Claude: defer |
| «hidup» (alive, to live) | 10 | same; «hidupkan» is chapter 12 | Claude: defer |
| «salinan» (copy) | 12 | «simpankan salinan di pejabat» (rewritten) | Sam: recommended |
| «sejak» (since) | 12 | now chapter 14 core (L-1212), already taught | Sam: recommended; closed |
| «melapor» / «melaporkan» (to report) | 12 | Hanashishou band 2 uses «melaporkan kebocoran» | Sam: recommended |
| «dihubungi», «dibaiki» | 12 | di- partners of «menghubungi» and «membaiki» | Claude: add |
| «sihat» (healthy) | 13 | root of «kesihatan»; «Saya sihat.» | Sam: recommended |
| «ahli farmasi» (pharmacist) | 13 | Kata-Kata speaker label for s16 and s18 | Claude: add |
| «beritahu» (to tell) | 13 | "tell the doctor" | Sam: recommended |
| «tinggalkan» (to leave behind) | 13 | leaving a bag at the counter | Claude: add |
| «baiklah» and «begini» | 14 | «Baiklah, kita buat begini» for stating a plan | Sam: his natural casual phrase; Claude: add «baiklah», «begini» optional |
| «ikut» (to come along) | 14 | «Puan Aini mahu ikut?»; came up again in chapter 17 invitations | Claude: add (strongly; two chapters ask for it) |
| «kata» (to say) | 14 | "what does the message say?" | Claude: add |
| «pengumuman» (announcement) | 14 | the heading of a written notice | Claude: add |
| «menangguhkan» and «membatalkan» | 14 | meN- forms of «tangguhkan» and «batalkan» for a third person | Claude: recommended (a later chapter must introduce them) |
| «kakitangan» (staff) | 15 | Kata-Kata speaker label for the counter clerk | Sam: approved |
| «bola» (ball) | 15 | «bulat, seperti bola» | Sam: approved |
| «tidak apa-apa» (never mind) | 16 | the everyday answer to «Maaf» | Sam: recommended |
| «berlaku» (to happen) | 16 | "what happened" in a report or a clinic form | Claude: add |
| «masalah» (problem) | 16 | «Ada masalah?» | Sam: recommended |
| «pinjam» (to borrow) | 16 | «Pemandu teksi pinjamkan telefon …» | Claude: add |
| «balas» (to reply) | 17 | «Sila balas sebelum hari Rabu.» on a written invitation; the unit says «Sila hubungi Puan Aini.» | Claude: add |
| «minggu depan» (next week) | 17 | «Saya belanja minggu depan.»; the unit says «Lain kali saya belanja.» | Claude: add |
| «giliran» (turn) | 17 | «Lain kali, giliran Mei Ling belanja.»; the unit says «Lain kali, Mei Ling belanja pula, ya?» | Claude: optional |
