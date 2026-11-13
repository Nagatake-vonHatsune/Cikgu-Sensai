# Stage 2 build step 4, chapter 14: unit 14 (reasons, conditions, purpose, contrast and sequence)

**13 November 2026 · Claude.** Authorised by Sam (build step 4, chapter 14 instruction, 13 Nov 2026): the chapter 12 and 13 fixes in their own commit, then the chapter 14 suite; push to main when the checks pass; **stop after chapter 14 for Claude's review** before chapter 15. Started at `1fd7862`. Kata-Kata (read only) is the pinned copy at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited. I did not re-open the charter Google Doc in this session (the brief listed the files to read); nothing in the work depends on a charter change.

## Summary

- **Fixes (own commit, `11db7f0`).** «dari» / «daripada»: 13 «Cuti sakit satu hari daripada doktor.» (listening, task key, reading message, writing model) and «Berapa hari cuti sakit daripada doktor?»; 12A «mesej daripada kedai itu» (both lines). The search of chapters 10 to 13 found one more person or organisation after «dari»: **11A «surat daripada bank itu»**, fixed the same way. The other hits are places or times and stay («berasal dari Osaka», «dari pukul sembilan», «dari atas meja», «dari pondok pengawal», «kawan dari pejabat», «Fail dari Osaka», «stesen dari pejabat»). 13: «Sila jangan bising.» and «Tolong jangan bising di bilik menunggu.»; the reading message says «terima kasih atas mesej itu»; both visiting-hours lines and the question «Pelawat boleh masuk pukul berapa?» are gone («pelawat» left the revision list; pattern 5 now has «Apa yang tidak dibenarkan di sini?»); the health-form and no-photography rules stay, labelled fictional. Because removing «elakkan bising» left the core word «elakkan» unused, the vocabulary example is now «Tolong elakkan lif itu. Lif itu rosak.» (a request, so the bare ‹-kan› verb is right). The HANDOFF template carries the «dari» / «daripada» rule and the bare-root rule; Sam's four answers and the other rulings are in `docs/stage-2-decisions.md` section 10; «sihat» and «beritahu» are marked "recommended" on the backlog. 223 tests passed on that commit.
- **Chapter 14.** One full A2 unit (five 45-minute blocks), the **writing block after unit 14** (the plan's "explain and rearrange a plan") and the chapter 14 fast pack, registered as re-authored in `curriculum/reauthored-units.json` (zero gaps, zero violations). `python3 build.py` passes (483 packs, 2,981 pages, all fit-checked; **20 violations and 199 gaps, all from older content**, none in chapter 14; unchanged from the end of chapter 13). **239 tests** pass (223 before, plus 16 in `tests/test_stage2_ch14.py`).

## Blocks and timings

| Block | Unit 14: the weekend hike | Minutes |
| --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns 20, first substitutions 5 | 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | 45 |
| C | Listening (Tanaka's call to Puan Aini) 15, reading (Mei Ling's message in written Malay) and writing 10, task (a changed outing) 15, recall 5 | 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview 10 | 45 |
| E | Scene transfer: Kata-Kata s01 to s15 as listening 10, role-play 15, a changed day 10, culture note 5, recall 5 | 45 |
| Writing | Explain and rearrange a plan: recall 5, model and notice comparison 10, guided draft 15, feedback 10, rewrite 5 | 45 |
| Fast | Chapter 14 fast pack, one 45-minute session | 45 |

Full course: **6 blocks = 4.5 class hours** for chapter 14 (5 blocks = 3.75 h plus the writing block 0.75 h). Self-study planning figure: 3 hours for the unit. Fast course: 1 block and 9 to 10 hours of self-study.

## What the unit contains

All 11 components plus the writing block; every section 6 and section 14 minimum is met and tested.

| | Unit 14 |
| --- | --- |
| Core / recognition / revision | 22 / 0 / 42 |
| Core groups | joining ideas 10 (the connectors, with «semasa» and «sejak»), the order of a plan 3, plans and changes 9 |
| Patterns (Kata-Kata frames) | five, 6 Q&A each: f01 «kalau» (with «jika», «bila», «apabila»); f02 and f03 together, reason and purpose («kerana», «sebab», «supaya», «tujuan»); f04 «walaupun» (with «namun»); f05 «sambil» (with «semasa», «sejak»); f06 «mula-mula», «kemudian», «akhirnya» (with «seterusnya») |
| Drills | 8 + 8 + 10 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks |
| Model conversation | 15 turns (Kata-Kata s01 to s15 word for word), gapped, a 10-turn variant (a second change: Sunday is out, next Saturday is in) |
| Listening | 134 Malay words, 9 questions (Tanaka's call to Puan Aini) |
| Reading and writing | Mei Ling's message to the hiking group in written Malay (jika, apabila, namun, oleh itu, seterusnya, keputusan), 8 questions; write a message that changes a plan |
| Task | A changed outing; change: it rains on Sunday too, A cancels the hike and keeps the cafe, B asks the time |
| Culture and usage note | 4 paragraphs, 235 words: everyday against written words; putting off against cancelling; group-chat custom (general knowledge, labelled, no figure); the Japanese slip |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) |
| Writing block | a group-chat message and the same news as a notice (six to eight sentences), with a peer check |

**The formal connectors beside the everyday partners.** Every vocabulary entry for «jika», «apabila», «namun», «oleh itu» and «seterusnya» names its partner and the register: «jika» / «kalau», «apabila» / «bila» («bila» for "when" is everyday, «apabila» is standard), «namun» / «tetapi» (spoken «tapi»), «oleh itu» / «jadi», «seterusnya» / «kemudian» (spoken ‹lepas tu›, recognition only, a mention sourced to card ms-c14-010). The transformation drill goes written to everyday first; the listening and the conversation use the everyday words; the reading uses the written ones; the writing block asks for both registers. A test checks all of this.

**Kata-Kata alignment:** the same frames f01 to f06; all six frame examples and all **15** scenario lines appear word for word (the whole scene is the model conversation, including s12 «Kita batalkan rancangan mendaki, tetapi kita masih makan di kafe.» with no «Itu keputusan kita»; s13 and s14 show the message language against speech); card IDs are cited in the opener (ms-c14-001 to -022), the vocabulary entries, the teacher notes (cards -018 to -022) and the culture sources.

**Rules applied.**
- **-kan rule (chapter 12).** «tangguhkan» and «batalkan» appear only in «kita» sentences and requests; never after «sudah», «sedang», «belum», «akan», «baru», «masih» and never with a third-person doer (the ledger has no meN- form). Where a third person is the subject the unit says «Mendaki batal.» or «Mendaki batal kerana hujan.»; a test holds the regex. No meN-…-kan form; the roots «tangguh» and «batal» are shown beside their -kan words in the vocabulary.
- **Bare root in dialogue (Sam, today).** Kata-Kata s13 «Saya sudah tulis mesej …» stays in the conversation as the everyday bare root; the pattern models, keys, readings and the markers drill use «menulis». The teacher notes say so.
- **Casual turns.** No «keputusan», «ialah» or di- … oleh in any conversation line; «keputusan» is taught as a word for a written notice or a result («Keputusan: hari Ahad.»). «baiklah» and «begini» are not in any line (see the backlog).
- **«dari» / «daripada».** No «dari» before a person or organisation in the unit (tested).
- Standard first, spoken marked: «tapi» appears only as the labelled spoken partner of «tetapi» in vocabulary entries and notes; no «lah», «kan», «tak», «dah», «nak», «ni», «tu» in a pupil line.

## Core-word coverage

All 22 core words appear in the unit outside the vocabulary list (the test checks this and that every revision word is really used). "Practised only" means the word is drilled and used in scenes but is not a scored test item. **13 of the 22 words are tested**; 20 are in the fast pack («semasa» and «sejak» are not).

| Tested | Practised only |
| --- | --- |
| supaya, walaupun, jika, apabila, sambil, namun, jadi, mula-mula, akhirnya, tujuan, tangguhkan, batal, batalkan | oleh itu, seterusnya, semasa, sejak, pilihan, keputusan, perubahan, janji, tangguh |

Thin spots: «tangguh» (the root) appears outside the vocabulary list only twice (the variant conversation and the root explanation); «keputusan» and «perubahan» about six times each («keputusan» only in written notices by design); «batal» about six times. A pilot teacher may want one more drill item for each.

## Code and data changed

- `suite/ms_c14.py` (the unit and the writing block `EXTRA`) and the chapter 14 fast pack in `suite/fast.py` (`C14_WORDS`, `chapter14`, `STAGE2_PACKS`). The unit imports `chapter10_common.unit_dict` unchanged.
- `suite/__init__.py`: grammar points ms-c14-g02 to g09; the unit is loaded; GLOSS entries for L-1203, L-1204, L-1206, L-1207 and L-1210 (their ledger meanings contain Malay). Speaker labels are «Tanaka» and «Mei Ling» (no unmarked «Cik»).
- `course.py`: chapter 14 «Reasons, conditions and plans» (unit 14), genre Plans, and its status line. `catalogue.py`: fourteen chapters, chapter 14 goal and focus; the `writing-14` extra block and the `ms-stage2-writing-14` additional block.
- `curriculum/reauthored-units.json`: ms-c14 and ms-c14-fast added. `curriculum/malay-mentions.json`: eight entries added (‹walau›, ‹akhir›, ‹tuju›, ‹putus›, ‹ubah›, ‹lepas tu›, ‹-nya›, ‹per-an›), each with its Kata-Kata card as the source. `curriculum/legacy-exceptions.json` unchanged (20).
- Tests: `tests/test_stage2_ch14.py` is new (16 tests: ledger partition, core-word use, roots, written against everyday words, no ruling-style turns, the -kan rule and «dari» / «daripada», Kata-Kata alignment with all 15 lines, register, minimums, the writing block, openers, culture note, Japanese, fast pack, registration). `tests/test_stage2_ch13.py` gains the checks for Sam's fixes; `test_catalogue` expects 14 chapters, 21 units, 105 blocks and 231 slots, levels A1 × 9 + A2 × 5.
- `tools/check_spans.py` was run on the unit file at chapter 14 before building: 0 problems.

## Lines a native speaker should read first

These are my judgement calls; everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. Variant: «Tangguh dulu, ya? Kita tunggu cuaca hari Jumaat.» (the bare root «tangguh» as a short reply; Kata-Kata gives no sentence for the root alone)
2. Pattern 1: A: «Bila kita makan di kafe?» B: «Kalau hujan.» and A: «Bila awak mendaki?» B: «Bila cuaca cerah.»
3. Pattern 2: A: «Apa tujuan mesej ini?» B: «Supaya kawan kita tahu rancangan itu.»; A: «Kenapa cik tidak boleh datang pada hari Sabtu?» B: «Sebab saya bekerja.»
4. Pattern 3: A: «Walaupun hujan, kita mendaki?» B: «Tidak. Kalau hujan, kita makan di kafe.»; variant «Boleh. Walaupun lama, Sabtu depan lebih baik. Awak janji datang awal?»
5. Pattern 4: A: «Sejak bila awak suka mendaki?» B: «Sejak bulan lepas.»; B: «Semasa mendaki, saya minum air dan berehat.»
6. Pattern 5: A: «Akhirnya awak sampai!» B: «Ya, akhirnya saya sampai. Maaf, saya lambat.»; B: «Mula-mula kita tangguhkan, kemudian kita tulis mesej untuk kawan kita.»
7. Reading message: «Oleh itu, kami tangguhkan ke hari Ahad.», «Namun kita masih makan di kafe.» and «Keputusan: hari Ahad. Janji!»
8. Listening: «Kalau hujan, mendaki batal. Tetapi kita masih berjumpa dan makan di kafe.» and «Bawa air dan payung. Semasa mendaki, kita minum air.»
9. Task change: «Maaf, hari Ahad pun hujan. Jadi, kita batalkan mendaki, tetapi kita masih makan di kafe.»
10. Variant: «Kita makan di kafe sahaja.» and the question-word key «Adakah kita masih mahu mendaki?» («Adakah» is formal; it is the model for the formal-question task)
11. Vocabulary: «Mendaki batal kerana hujan.» and «Keputusan: kita mendaki pada hari Ahad.» (a written notice)
12. The culture note's group-chat sentence (general knowledge, labelled) and the teacher note that repeats the register rule.

All Japanese is a draft for the native review. The bridges (〜たら / 〜ば / 〜なら / 〜と against «kalau»; ので・から against «kerana», ように against «supaya», のに against «walaupun»; 〜ながら against «sambil») are teaching hypotheses.

## Word proposals for Sam (not in the ledger; I rewrote the lines instead and added no rows)

| Proposed form | Why it came up | What the unit says instead |
| --- | --- | --- |
| «baiklah» and «begini» | Sam's natural casual opening «Baiklah, kita buat begini» for stating a plan; **no line in the unit needs them**, so nothing was rewritten, but both go on the backlog as you asked | «Baik. Ini rancangan kita.» (Kata-Kata s08) |
| «ikut» (to come along) | inviting Puan Aini in the listening: «Puan Aini mahu ikut?» | «Puan Aini mahu datang?» |
| «kata» (to say) | "what does the message say?" | «Apa dalam mesej itu?» |
| «pengumuman» (announcement) | the heading of the written notice in the writing block | the notice starts «Ada perubahan rancangan.» |

All four are on the HANDOFF "Word proposals backlog" with the earlier ones. «sejak» (a chapter 12 proposal) is now a **chapter 14 core word** (L-1212); the chapter 12 rewrite stays and the backlog row says so.

## Questions for Sam

1. **Five patterns.** Kata-Kata gives six frames and the charter allows five patterns, so pattern 2 shows f02 «kerana» and f03 «supaya» together (reason and purpose), as pattern 5 did in chapter 13. Is that the pair you want merged, or would you rather merge f04 and f05?
2. **«keputusan».** It appears only in written notices (the reading message, the writing block) and one vocabulary example, never in a conversation line. Is that the right home, or do you want a casual use found?
3. **The bare root «tangguh».** I used it once as a short reply («Tangguh dulu, ya?») and show it as the root of «tangguhkan». Is the short reply natural, or should «tangguh» appear only as a root in the vocabulary (and the thin-spot be accepted)?
4. **No way to say a third person postponed.** Because the ledger has no meN- form of «tangguhkan» or «batalkan», the unit cannot say "Mei Ling postponed the hike"; it says «Mendaki batal.» instead. Is that acceptable until a later chapter?
5. **Fast pack.** It drops «semasa» and «sejak» to keep 20 core words. OK?
6. **Menu names.** Title «Reasons, conditions and plans», genre «Plans». OK?

## Not verified

- **Kamus Dewan:** none of the chapter 14 forms was checked (end of the project, ledger Journal row 128). The cards' notes are the source for the roots and traps.
- **Facts:** the culture note states no figure, rule or date about Malaysia; the group-chat sentence is general knowledge, labelled and not source-checked. The plans, names and times are fictional.
- **Legacy text:** «mesej dari kedai» and «mesej dari awak» still stand in the retired placeholder's legacy text (`curriculum/foundation.txt`, `foundation-guided.txt`) and its generated scope files; the placeholder is no longer in the course menu. I did not edit them.
- **PDF:** the build's fit check passed for every page. I did not review the pages by eye.
- **Environment:** the build needed `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (after `apt-get update`); I installed them in the session. The checkout was shallow and was unshallowed first.
