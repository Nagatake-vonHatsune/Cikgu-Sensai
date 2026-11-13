# Stage 2 build step 4, chapter 13: unit 13 (health: belum, permission, need and advice)

**13 November 2026 · Claude.** Authorised by Sam (build step 4, chapter 13 instruction, 13 Nov 2026): the chapter 12 fixes in their own commit, then the chapter 13 suite; push to main when the checks pass; **stop after chapter 13 for Claude's review** before chapter 14. Started at `b54fde6`. Kata-Kata (read only) is the pinned copy at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited.

## Summary

- **Chapter 12 fixes (own commit, `732e336`).** The ‹-kan› rule is applied to every 12A and 12B line, drill and key: the bare ‹-kan› verb stays in requests and first-person offers or replies; with a third-person doer or «sudah», «sedang», «belum», «akan», «baru», «masih» the units use the meN- verb the ledger has («Pengawal menyimpan bungkusan itu.», «Saya sedang membawa bungkusan itu ke lif.»); where there is none («letakkan», «bukakan», «matikan», «bersihkan») the line is rephrased. I applied the same rule to the ‹-i› verbs («Kami akan menghubungi juruteknik.», «Juruteknik belum membaiki paip itu.»). The 12A and 12B markers drills now show the change to the meN- verb. Teacher notes say that «menyimpankan» and «menghantarkan» are not taught. Also: «… akan menukar paip itu»; 12B «Tolong kosongkan lantai itu juga.» deleted (the reply is «Boleh, encik. Terima kasih.»); «Penerima Puan Siti, ya?» (and «ialah» out of the other conversational 12A lines); «Ada berapa kotak di lobi?» (and «Ada berapa lampu yang rosak?»); the guardhouse and management-office notes are two lines each; the old «Ambil bungkusan di lobi» placeholder is retired from the course menu with its six legacy lessons and its ten legacy exceptions (30 → 20; the list only shrank). Sam's answers are in `docs/stage-2-decisions.md` section 9, and «sejak», «melaporkan» and «salinan» are on the backlog marked "recommended".
- **Chapter 13.** One full A2 unit (five 45-minute blocks) and the chapter 13 fast pack, registered as re-authored in `curriculum/reauthored-units.json` (zero gaps, zero violations). `python3 build.py` passes (463 packs, 2,862 pages, all fit-checked; **20 violations and 199 gaps, all from older content**, none in chapter 13; before this session 22 and 203, and the placeholder's entries went with its retirement). All **223** tests pass (207 before, plus 1 for the -kan rule, plus 15 in `tests/test_stage2_ch13.py`).
- **No extra block.** The plan gives chapter 13 neither a writing nor a review block (writing blocks follow 10B, 12A, 14 and 16; reviews follow 11B, 12B and 15), so none was built.

## Blocks and timings

| Block | Unit 13: the panel clinic and the pharmacy | Minutes |
| --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns 20, first substitutions 5 | 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | 45 |
| C | Listening (Mei Ling's call to the clinic, then the pharmacy) 15, reading (a clinic notice and a message about sick leave) and writing 10, task (register, ask permission, ask a pharmacist to repeat) 15, recall 5 | 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview of unit 14 10 | 45 |
| E | Scene transfer: Kata-Kata s01 to s18 as listening 10, role-play 15, a changed time 10, culture note 5, recall 5 | 45 |
| Fast | Chapter 13 fast pack, one 45-minute session | 45 |

Full course: **5 blocks = 3.75 class hours** for chapter 13. Self-study planning figure: 3 hours for the unit. Fast course: 1 block and 9 to 10 hours of self-study (the figure the other fast packs state).

## What the unit contains

All 11 components; every section 6 and section 14 minimum is met and tested.

| | Unit 13 |
| --- | --- |
| Core / recognition / revision | 25 / 0 / 53 («MC» is the spoken form inside L-1200 and is labelled spoken wherever it appears) |
| Patterns (Kata-Kata frames) | five, 6 Q&A each: f01 «belum»; f02 «Bolehkah saya …?» (and «Boleh saya …?»); f03 «perlu»; f04 «patut» with «mesti»; f05 and f06 together for signs and forms («tidak dibenarkan», «dilarang», «wajib diisi») |
| Drills | 8 + 8 + 8 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks |
| Model conversation | 14 turns (Kata-Kata s01 to s14 word for word), gapped, a 10-turn variant (Mei Ling, with an appointment); s15 to s18 (the pharmacy) are in the task key and the E-block listening |
| Listening | 137 Malay words, 9 questions (Mei Ling's call, then the pharmacist) |
| Reading and writing | A clinic notice, a message about sick leave and a corridor sign, 8 questions; write a short message to a boss |
| Task | Register at the clinic and ask the pharmacist to repeat; change: the doctor is not in, B chooses a time and asks permission to leave a bag |
| Culture and usage note | 4 paragraphs, 248 words: need, advice and must; signs against speech and how to ask permission; panel clinics and sick leave (general knowledge, labelled, two lines, no figure); the Japanese slip |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) |

**Kata-Kata alignment:** the same frames f01 to f06; all six frame examples and all **18** scenario lines appear word for word (s01 to s14 in the model conversation, s15 to s18 in the task key); card IDs are cited in the opener (ms-c13-001 to -025), the vocabulary entries (the root notes), the teacher notes (cards -004, -005, -012, -021) and the culture sources.

**Safety.** No diagnosis, no treatment advice, no medicine name with a dose and no dosing instruction anywhere, and a test checks it: the doctor says only «patut berehat» and gives sick leave, the pharmacist only points to the label and says «tanya saya lagi», «dos» appears only in the label context, and none of ubat, pil, sehari, selesema or any figure with mg or ml appears in a Malay line. The teacher notes (read first) and the culture note tell learners to follow their own doctor and pharmacist. Sick leave is taught as «cuti sakit»; «MC» is recognition only and never in a key. The emergency word is taught on a door sign («Pintu kecemasan ada di sebelah kiri.»), not as advice.

**Rules applied:** «mesti» is shown as a root (not ‹me-› + ‹sti›, card ms-c13-021); «kebenaran» means permission only (every use is «minta kebenaran»); «wajib» is secular (forms and notices); «dibenarkan» is ‹di-› + ‹benar› + ‹-kan›, the opposite of «dilarang»; «mendaftar» is the standard form and «daftar» the everyday one (Kata-Kata s03 keeps «daftar»). Standard first, spoken forms marked. No «lah», «kan» (the particle), «tak», «dah», «takpe» or «nak»; no «ialah», no di- … oleh in conversation, no «keputusan»; no faith-specific expression. The ‹-kan› rule of chapter 12 holds («Tolong elakkan …» is a request). Teacher notes: «belum» against «tidak»; «perlu» against «patut» against «mesti» / «wajib»; where Japanese learners slip (入ってもいいですか against «Boleh saya masuk?»; «tidak boleh» for 〜なくてもいい); panel clinics and «cuti sakit» / «MC» (general knowledge, labelled, two lines, no figure).

## Core-word coverage

All 25 core words appear in the unit outside the vocabulary list (the test file checks this and that every revision word is really used). "Practised only" means the word is drilled and used in scenes but is not a scored test item. **13 of the 25 words are tested**; 20 are in the fast pack.

| Tested | Practised only |
| --- | --- |
| perlu, patut, mesti, wajib, dibenarkan, kebenaran, bila perlu, penyambut tetamu, daftar, mendaftar, kesihatan, farmasi, arahan | nasihat, elakkan, sesuai, klinik panel, temu janji, cuti sakit, simptom, sakit tekak, alahan, rawatan, dos, kecemasan |

Thin spots: «simptom», «rawatan» and «kecemasan» each appear outside the vocabulary list only once or twice, and «sakit tekak» three times. They pass the check, but a pilot teacher may want one more drill item for each.

## Code and data changed

- `suite/ms_c13.py` (the unit, no extra block) and the chapter 13 fast pack in `suite/fast.py` (`C13_WORDS`, `chapter13`, `STAGE2_PACKS`). The unit imports `chapter10_common.unit_dict` unchanged.
- `suite/__init__.py`: grammar points ms-c13-g02 to g08; the unit is loaded; GLOSS entries for L-1189, L-1200 and L-1268 (their ledger meanings contain Malay). Speaker labels are English («Receptionist», «Doctor», «Pharmacist»): «penyambut tetamu» and the Kata-Kata label «Ahli farmasi» would be unmarked Malay.
- `course.py`: chapter 13 «Health: may, need, should» (unit 13), genre Health, and its status line; the retired placeholder (chapter 12 fixes). `catalogue.py`: thirteen chapters, chapter 13 goal and focus; `future_chapters` is now empty.
- `curriculum/reauthored-units.json`: ms-c13 and ms-c13-fast added. `curriculum/malay-mentions.json`: nine entries added (the roots ‹benar›, ‹sihat›, ‹cemas›, ‹arah›, ‹rawat›, ‹alah›, ‹elak›, ‹suai› and the wrong split ‹sti›), each with its Kata-Kata card as the source. `curriculum/legacy-exceptions.json`: ten entries removed (shrink only).
- Tests: `tests/test_stage2_ch13.py` is new (15 tests, copied from chapter 12 and adapted: ledger partition, core-word use, the traps, the -kan rule, Kata-Kata alignment with all 18 lines, the safety rule, «MC» as recognition, minimums, openers, the fast pack, registration). `tests/test_stage2_ch12.py` gains the -kan rule test; the chapter 10, 11, 12 and step 5e to 5g tests now expect 20 legacy exceptions; `test_catalogue` expects the six retired titles and, for the structure, 13 chapters, 20 units, 100 blocks and 220 slots, levels A1 × 9 + A2 × 4. No Stage 1 content changed.
- `tools/check_spans.py` was run on the unit file at chapter 13 before building: 0 problems.

## Lines a native speaker should read first

These are my judgement calls, so please read them first. Everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. Pattern 1: «Apa simptom awak?» → «Saya demam. Saya tidak batuk.»
2. Pattern 3: «Apa saya perlu buat?» → «Awak perlu mendaftar dulu.» and «Saya perlu tunggu lama?» → «Tidak perlu. Nombor giliran awak sudah dekat.»
3. Pattern 3: «Saya perlu isi semua borang ini?» → «Tidak perlu. Borang kesihatan sahaja wajib diisi.»
4. Pattern 4: «Saya mahu cuti esok. Apa saya patut buat?» → «Awak patut tanya bos dulu.», and pattern 2: «Boleh saya cuti esok?» → «Awak mesti minta kebenaran bos dulu.»
5. Pattern 5: «Maaf, dilarang masuk. Sila tunggu di bilik menunggu.» and «Pelawat dibenarkan masuk pukul dua.»
6. Variant: «Ada. Saya cakap dengan doktor nanti.» and «Boleh. Doktor akan panggil cik.» (the bare «panggil» after «akan», where the course teaches «memanggil»)
7. Listening: «Saya belum minta kebenaran bos. Saya mesti menelefon bos dulu.», «Cik tidak perlu bawa duit sekarang.» and «Cik boleh tunggu di luar.»
8. Reading notice: «Untuk rawatan, tunjukkan kad syarikat.» and the corridor sign «Pintu kecemasan ada di sebelah kiri. Sila elakkan bising.»
9. Reading message: «Cuti sakit satu hari dari doktor. Awak tidak perlu datang ke pejabat esok. Awak patut berehat di rumah.» (written without «Doktor berikan …», because «berikan» has no meN- form in the ledger)
10. Vocabulary examples: «Pukul empat petang sesuai?», «Kad ini untuk rawatan di klinik panel.», «Tolong elakkan bising di bilik menunggu.»
11. Task change: «Maaf, doktor belum ada. Encik boleh tunggu, atau datang pukul empat. Sesuai?» → «Pukul empat sesuai. Boleh saya letak beg di sini?»
12. The culture note's panel-clinic paragraph (general knowledge, two lines, labelled) and the teacher note that repeats it.

All Japanese is a draft for the native review. The bridges (まだ〜ていません against «belum»; 〜てもいいですか against «Boleh saya …?»; 〜たほうがいい, 〜なければならない and 必要がある against «patut», «mesti» / «wajib» and «perlu») are teaching hypotheses.

## Word proposals for Sam (not in the ledger; I rewrote the lines instead and added no rows)

| Proposed form | Why it came up | What the unit says instead |
| --- | --- | --- |
| «sihat» (healthy) | the root of the ledger word «kesihatan»; «Saya sihat.» / «Saya tidak sihat.» (**recommended**) | «Saya demam dan sakit tekak.» |
| «ahli farmasi» (pharmacist) | the Kata-Kata speaker label for s16 and s18 | the English label «Pharmacist» |
| «beritahu» (to tell) | "tell the doctor" about an allergy | «Saya cakap dengan doktor nanti.» |
| «tinggalkan» (to leave something) | leaving a bag at the counter | «Boleh saya letak beg di sini?» |

All four are on the HANDOFF "Word proposals backlog" list with the earlier ones. The ‹meN-› + ‹-kan› forms are not proposed: Sam said they are not natural.

## Questions for Sam

1. **Five patterns.** Kata-Kata gives six frames and the charter allows five patterns per unit, so pattern 5 shows f05 and f06 together (signs and forms). Is that grouping right, or should f06 «wajib diisi» stand alone and f03 and f04 merge?
2. **«mendaftar» first.** Kata-Kata s03 says «Encik perlu daftar dulu.» and the ledger row L-1268 is «mendaftar». I teach «mendaftar» as the standard form and «daftar» as the everyday one, and never mark «daftar» wrong. Is that the order you want?
3. **«MC» as recognition.** «cuti sakit» is the form in every key; «MC» is labelled spoken and appears only in the vocabulary entry, the notes and one culture sentence. Keep it that way?
4. **Fictional rules.** The notices (visitors in at two, no photographs, health form compulsory) are invented and labelled fictional. Do you want them kept, or would you rather the unit used only the rules in the Kata-Kata scenario?

## Not verified

- **Kamus Dewan:** none of the chapter 13 forms was checked (end of the project, ledger Journal row 128). The cards' notes are the source for the roots and traps; they were not re-checked against Tatabahasa Dewan.
- **Facts:** the culture note states no figure, rule or date about Malaysia. The panel-clinic and sick-leave paragraph is general knowledge, labelled and not source-checked. The clinic, its notices and every time in the unit are fictional; the unit gives no medical advice.
- **PDF:** the build's fit check passed for every page. I did not review the pages by eye.
- **Environment:** the build needed `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (after `apt-get update`); I installed them in the session. The checkout was shallow and was unshallowed first.
