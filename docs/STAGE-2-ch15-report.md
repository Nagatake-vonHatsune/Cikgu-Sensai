# Stage 2 build step 4, chapter 15: unit 15 (describing things and people with «yang»)

**13 November 2026 · Claude.** Authorised by Sam (build step 4, chapter 15 instruction, 13 Nov 2026): the chapter 14 fixes in their own commit, then the chapter 15 suite; push to main when the checks pass; **stop after chapter 15 for Claude's review** before chapter 16. Started at `ea61fef`. Kata-Kata (read only) is the pinned copy at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited. I did not re-open the charter Google Doc in this session (the brief listed the files to read); nothing in the work depends on a charter change.

## Summary

- **Fixes (own commit, `40b3c59`).**
  - **Noun object.** «tangguhkan» and «batalkan» now take a noun object, not a verb: «tangguhkan rancangan mendaki», «batalkan rancangan mendaki», «Rancangan mendaki batal (kerana hujan).», «Rancangan mendaki pada hari Sabtu batal …». Done in every pattern, drill, key, reading, listening, writing model, the task and its change, the fast pack and the teacher notes (for example «Mei Ling tangguhkan rancangan mendaki kerana dia bekerja.», «Jadi, kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.»). Written notices give the object («Oleh itu, kita tangguhkan rancangan itu ke hari Ahad.», «Jika hujan, kita batalkan rancangan itu.»); short spoken replies drop it («Jika hujan, kita tangguhkan.», «Kita tangguhkan ke hari Ahad.»). New teacher note.
  - **«kami» against «kita».** The reading message, the notice, both writing models, the writing-block model and the vocabulary examples are inclusive «kita» («Kita tangguhkan makan malam ke hari Jumaat … Kalau hujan, kita makan di rumah.»). I left «Hujung minggu ini kami mahu mendaki. Puan Aini mahu datang?» in the listening on purpose (the invitation leaves Puan Aini out until she says yes) and changed Tanaka's later «Jadi, kita tangguhkan ke hari Ahad.» to «kita» (she has said «Mahu!»). The markers drill keeps «Kami …» (a drill sentence, no message). New teacher note on «kami» (leaves the listener out) against «kita» (includes the listener), using exactly that pair.
  - **Provenance and backlog.** `docs/stage-2-decisions.md` section 11 now says "Sam's answers, given directly in the chapter 14 session" and records the two fixes as Claude's later review; «menangguhkan» and «membatalkan» are on the backlog as recommended. New test `test_noun_object_and_kita`. 240 tests, build and tests passed on that commit.
- **Chapter 15.** One full A2 unit (five 45-minute blocks), the **review block after chapter 15** (the plan's Review 3: chapters 13 to 15 plus earlier verb contrasts) and the chapter 15 fast pack, registered as re-authored in `curriculum/reauthored-units.json` (zero gaps, zero violations). `python3 build.py` passes (**503 packs, 3,100 pages**, all fit-checked; **20 violations and 199 gaps, all from older content**, none in chapter 15; unchanged from chapter 14). **258 tests** pass (240 before, plus 18 in `tests/test_stage2_ch15.py`).

## Blocks and timings

| Block | Unit 15: the lost wallet and the visitors | Minutes |
| --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns 20, first substitutions 5 | 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | 45 |
| C | Listening (Rahman and Tanaka on the phone) 15, reading (a lost-property form) and writing 10, task (at the counter) 15, recall 5 | 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview 10 | 45 |
| E | Scene transfer: Kata-Kata s01 to s17 as listening 10, role-play 15, a changed item 10, culture note 5, recall 5 | 45 |
| Review 3 | Chapters 13 to 15: recall 5, mixed input 10, alternating role task 15, changed situation 10, self-check 5 | 45 |
| Fast | Chapter 15 fast pack, one 45-minute session | 45 |

Full course: **6 blocks = 4.5 class hours** for chapter 15 (5 blocks = 3.75 h plus the review block 0.75 h). Self-study planning figure: 3 hours for the unit. Fast course: 1 block and 9 to 10 hours of self-study.

## What the unit contains

All 11 components plus the review block; every section 6 and section 14 minimum is met and tested.

| | Unit 15 |
| --- | --- |
| Core / recognition / revision | 21 / 0 / 37 |
| Core groups | lost things 6, parts and materials 5, colour, shape and likeness 6, people and what they wear 4 |
| Patterns (Kata-Kata frames) | five, 6 Q&A each: f02 «___ saya hilang»; f01 and f03 together («yang ada», «yang memakai»); f04 colour and features («berwarna», «dan ada»); f06 shape and likeness («Bentuknya …, seperti …», «seperti itu / seperti ini»); f05 «Yang mana satu? Yang … atau yang …?» |
| Drills | 8 + 8 + 10 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks |
| Model conversation | 16 turns (Kata-Kata s01 to s17 word for word; turn 11 joins s11 and s12), gapped, a 10-turn variant (Mei Ling's handbag, two red bags) |
| Listening | 138 Malay words, 9 questions (Rahman asks Tanaka on the phone which visitors to look for) |
| Reading and writing | a lost-property form and the counter's reply in written Malay, 8 questions; write four or five sentences about a lost item |
| Task | At the lost-property counter; change: two bags look the same, «Yang mana satu?» |
| Culture and usage note | 4 paragraphs, 249 words: description before the noun against «yang»; what to say at a counter; general knowledge (labelled, no figure); the Japanese slips |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) |
| Review block | a lost bag at the clinic reception: «belum», «perlu», «supaya», «walaupun», «yang», plus ber-, meN-, ‹-kan› and ‹-i› verbs; no new word |

**The four notes the brief asked for** are in the teacher notes and tested (`test_teacher_notes_yang_memakai_hilang`): «yang» as the connector Japanese does not need (黒い財布 against «dompet yang hitam» and «dompet hitam»); when «yang» can be dropped (one adjective after the noun) and when it cannot («beg ada zip» is a whole sentence); «memakai» for glasses, clothes, a hat and shoes against かける / 着る / かぶる / はく (the unit uses all four things in sentences); «hilang» against the chapter 16 ‹tertinggal›, which appears only as a ‹…› mention (new entry in `curriculum/malay-mentions.json`; a test checks that no pupil line uses it).

**«seperti» and «macam».** «seperti» is standard and «macam» (chapter 5) is its spoken partner, shown in the vocabulary entry. «seperti itu» is named as the standard partner of the chapter 17 spoken ‹macam tu›, which is a mention only (source: card ms-c15-014); a test checks that ‹macam tu› never appears in a «…» line.

**Kata-Kata alignment:** the same frames f01 to f06; all six frame examples and all **17** scenario lines appear word for word, as rebuilt at `7fbe173` («Seperti ini?» / «Ya, seperti itu, tetapi ada zip.», «Yang ada zip. Yang itu!», «yang memakai» twice, «membawa»); card IDs are cited in the opener (ms-c15-001 to -021), the vocabulary entries, the teacher notes and the culture sources.

**Rules applied.** «kami» only where the listener is left out (the staff in the review block); no «tangguhkan» or «batalkan» in the unit at all (no noun-object risk); bare root «jumpa» only as the dialogue's «Saya sudah jumpa dia.» (Kata-Kata) and in the markers key («Belum. Saya belum jumpa beg saya.»), with the meN- form («mencari», «membawa», «memakai») in the patterns, drills and keys; «dari Jepun», «dari mana» for places, no «dari» before a person; no «lah» or «kan» in any key; no Assalamualaikum or Waalaikumsalam and nothing faith-specific; all items, places and times fictional.

## Core-word coverage

All 21 core words appear in the unit outside the vocabulary list (the test checks this and that every revision word is really used). "Practised only" means the word is drilled and used in scenes but is not a scored test item. **16 of the 21 words are tested**; all 21 are in the fast pack (as in chapter 14, Sam's ruling; the plan's 15 to 20 would have dropped one).

| Tested | Practised only |
| --- | --- |
| hilang, dompet, beg tangan, nombor plat, kulit, poket, zip, tali, berwarna, berjalur, bulat, segi empat, seperti, lelaki, cermin mata, memakai | barang, jenama, ciri, bentuk, perempuan |

Thin spots: «nombor plat», «jenama» and «kulit» appear about six times outside the vocabulary list; «ciri» and «bentuk» about eleven. A pilot teacher may want one more drill item for each.

## Code and data changed

- `suite/ms_c15.py` (the unit and the review block `EXTRA`) and the chapter 15 fast pack in `suite/fast.py` (`C15_WORDS`, `chapter15`, `STAGE2_PACKS`). The unit imports `chapter10_common.unit_dict` unchanged.
- `suite/__init__.py`: grammar points ms-c15-g02 to g09; the unit is loaded; GLOSS entries for L-1229, L-1271 and L-1272 (their ledger meanings contain Malay); «zip» added to `ENGLISH_HOMOGRAPHS` (English prose, and ledger row L-1228).
- `course.py`: chapter 15 «Describing things and people» (unit 15), genre Lost property, and its status line. `catalogue.py`: fifteen chapters, chapter 15 goal and focus; the `review-15` extra block and the `ms-stage2-review-15` additional block.
- `curriculum/reauthored-units.json`: ms-c15 and ms-c15-fast added. `curriculum/malay-mentions.json`: four entries added (‹tertinggal›, ‹macam tu›, ‹ciri-ciri›, ‹jalur›), each with its Kata-Kata card as the source. `curriculum/legacy-exceptions.json` unchanged (20).
- Tests: `tests/test_stage2_ch15.py` is new (18 tests: ledger partition, core-word use, roots and mentions, the four teacher notes, «seperti» and «macam», «yang» kept and dropped, casual turns, the -kan rule and «dari» / «daripada», Kata-Kata alignment with all 17 lines, register, minimums, the review block, openers, culture note, Japanese, fast pack, registration). `tests/test_stage2_ch14.py` gains `test_noun_object_and_kita`; `test_catalogue` expects 15 chapters, 22 units, 110 blocks and 242 slots, levels A1 × 9 + A2 × 6.
- `tools/check_spans.py` was run on the unit file at chapter 15 before building: 0 problems (379 spans).

## Lines a native speaker should read first

These are my judgement calls; everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. Pattern 4: «Bagaimana bentuk meja di kafe itu?» «Bulat. Seperti pinggan besar.» and «Bentuknya bulat, seperti jam.» (round glasses)
2. Pattern 1: «Maaf, apa yang hilang?» and «Barang apa yang hilang, encik?»
3. Pattern 3: «Beg itu kecil dan berwarna biru.» and «Baju itu putih dan berjalur.»
4. Teacher note: «dompet yang hitam» stresses "the black one" against another; «dompet hitam» is the plain form.
5. Listening: «Bukan. Dia tidak memakai cermin mata. Dia memakai topi.» and «Rambut perempuan itu pendek.»
6. Listening: «Saya tidak ingat nombor plat kereta itu, tetapi nombor plat ada dalam mesej saya.»
7. Variant: «Ya, seperti itu, tetapi tidak ada zip.» and «Betul. Ini beg tangan puan.»
8. Reading: the form («Nama: Encik Tanaka. Barang: dompet. Ciri: dompet kulit, berwarna hitam, …») and the reply «Dompet yang ada zip sudah ada di kaunter. Sila ambil dompet itu pada hari Selasa.»
9. Drill key: «Lelaki yang tinggi memakai cermin mata.» (or «Lelaki yang memakai cermin mata itu tinggi.»)
10. Question keys: «Bolehkah saya melihat dompet itu?» and «Ada berapa keping kad di dalam?»
11. Review block: «Baik. Kalau doktor sudah ada, kami panggil encik.» and «Tolong hubungi pejabat saya, ya?»
12. The culture note's counter sentence (general knowledge, labelled) and the speaker label «Staff» in place of «Kakitangan stesen».

All Japanese is a draft for the native review. The bridges (modifier before the noun against «yang»; 〜のような against «seperti»; 黒いの against «yang hitam»; なくした against «hilang») are teaching hypotheses.

## Word proposals for Sam (not in the ledger; I rewrote the lines instead and added no rows)

| Proposed form | Why it came up | What the unit says instead |
| --- | --- | --- |
| «kakitangan» (staff) | the Kata-Kata speaker label for the counter clerk (s02 to s10) | the English label «Staff» |
| «bola» (ball) | the natural thing a round bag or hat is "like" (`bulat, seperti bola`) | «Bentuknya bulat, seperti jam.» |

Both are on the HANDOFF "Word proposals backlog" with the earlier ones.

## Questions for Sam

1. **Turn 11.** Kata-Kata gives 17 lines and the charter allows 16 turns, so turn 11 joins s11 «Terima kasih banyak!» and s12 «Encik Rahman, tetamu dari Jepun …» (Tanaka thanks the clerk, then rings Rahman). The alternative is a model of s01 to s11 only and the visitors scene in Block E. Is the join acceptable?
2. **Five patterns.** f01 and f03 share pattern 2 («yang ada», «yang memakai»); the order is f02, f01 and f03, f04, f06, f05. Is that the pair you want merged?
3. **Fast pack.** It holds all 21 core words, as chapter 14 did at your request, although the plan says 15 to 20. OK to keep that for the rest of the chapters?
4. **«ciri-ciri».** The form says «Ciri:»; the doubled ‹ciri-ciri› is a mention only (the checker treats reduplication as a Stage 3 form). Is that the right way to "recognise both"?
5. **The review block.** A lost bag at the clinic reception covers chapters 13 to 15 and the verb contrasts. Do you want a different setting?
6. **Menu names.** Title «Describing things and people», genre «Lost property». OK?

## Not verified

- **Kamus Dewan:** none of the chapter 15 forms was checked (end of the project, ledger Journal row 128). The cards' notes are the source for the roots and traps.
- **Facts:** the culture note states no figure, rule or date about Malaysia; the counter sentence is general knowledge, labelled and not source-checked. The items, names, places and times are fictional.
- **PDF:** the build's fit check passed for every page. I did not review the pages by eye.
- **Environment:** the build needed `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (after `apt-get update`); I installed them in the session. The checkout was shallow and was unshallowed first.
