# Stage 2 build step 4, chapter 16: unit 16 (accidents with ter-)

**13 November 2026 · Claude.** Authorised by Sam (build step 4, chapter 16 instruction, 13 Nov 2026): one chapter 15 fix and Sam's answers in their own commit, then the chapter 16 suite; push to main when the checks pass; **stop after chapter 16 for Claude's review** before chapter 17. Started at `e83eaca`. Kata-Kata (read only) is the pinned copy at `7fbe173`. Kata-Kata, Hanashishou and the ledger sheet were not edited. I did not re-open the charter Google Doc in this session (the brief listed the files to read); nothing in the work depends on a charter change.

## Summary

- **Fix and answers (own commit, `7389195`).** The review block line is now «Walaupun saya sibuk, saya akan menunggu doktor di sini.» Sam's six chapter 15 answers are recorded in `docs/stage-2-decisions.md` section 12 (the s11 and s12 join and the f01 and f03 merge are fine; fast packs hold all core words from now on; «ciri» is the common form and «ciri-ciri» stays a mention only, the form keeps «Ciri:»; the review setting and menu names are fine; «kakitangan» and «bola» approved). The backlog marks «kakitangan» and «bola» "approved by Sam". 258 tests and the build passed on that commit.
- **Chapter 16 (`f73c68b`).** One full A2 unit (five 45-minute blocks), the **writing block after chapter 16** (a brief factual incident message) and the chapter 16 fast pack, registered as re-authored in `curriculum/reauthored-units.json` (zero gaps, zero violations). The plan gives chapter 16 no review block, so none was built. `python3 build.py` passes (**523 packs, 3,219 pages**, all fit-checked; **20 violations and 199 gaps, all from older content**, none in chapter 16; unchanged from chapter 15). **277 tests** pass (258 before, plus 19 in `tests/test_stage2_ch16.py`).

## Blocks and timings

| Block | Unit 16: the locked door, the spilt coffee and the slip | Minutes |
| --- | --- | ---: |
| A | Words and patterns: recall 5, Tanya Cikgu 5, vocabulary 10, patterns 20, first substitutions 5 | 45 |
| B | Drills and conversation: recall 5, the drill ladder (6 types + markers) 20, model and gapped conversation 15, rehearsal 5 | 45 |
| C | Listening (Aini explains to Rahman why she is late) 15, reading (a clinic reception form) and writing 10, task (locked out at the guardhouse) 15, recall 5 | 45 |
| D | Mixed review 15, unit test 10, self-check 10, preview 10 | 45 |
| E | Scene transfer: Kata-Kata s01 to s17 as listening 10, role-play 15, a changed fact 10, culture note 5, recall 5 | 45 |
| Writing | A brief factual incident message: recall 5, model 10, guided draft 15, feedback 10, rewrite 5 | 45 |
| Fast | Chapter 16 fast pack, one 45-minute session | 45 |

Full course: **6 blocks = 4.5 class hours** for chapter 16 (5 blocks = 3.75 h plus the writing block 0.75 h). Self-study planning figure: 3 hours for the unit. Fast course: 1 block and 9 to 10 hours of self-study.

## What the unit contains

| | Unit 16 |
| --- | --- |
| Core / recognition / revision | 23 / 0 / 43 |
| Core groups | ter- accidents 9, ter- states and results 5, by accident, an accident, the key and the spill 4, what you see 5 |
| Patterns (Kata-Kata frames) | five: f01 «Saya tertinggal ___ di ___»; f02 «Maaf, saya ___»; f04 «Saya tidak sengaja ___ ___»; f03 and f06 together (a thing as the subject: «tertumpah», «Pintu terkunci. Boleh tolong ___?»); f05 the two ter- in one sentence |
| Drills | 8 + 8 + 10 + 8 + 8 items, 4 short dialogues, 8 marker items, 18 question-word tasks |
| Model conversation | 16 turns (Kata-Kata s01 to s17 word for word; turn 11 joins s11 and s12), gapped, a 10-turn variant (Mei Ling locked out, the management office not open) |
| Listening | 120 Malay words, 7 questions (Aini is late: slept in, missed the bus, taxi stuck, phone left at home, line cut off) |
| Reading and writing | a clinic reception form in written Malay and the counter's note, 7 questions; write four or five sentences about a small accident |
| Task | Locked out at the guardhouse; change: the management office is not open yet |
| Culture and usage note | 4 paragraphs, 246 words: one marker for a slip in Malay against two in Japanese; apology depends on responsibility; general knowledge (labelled, no figure); the Japanese slips |
| Test | 6 listening, 6 words, 4 grammar, 4 reading items, plus speaking (20 + 1) |
| Writing block | two factual messages (a key left inside, a spill): who and where, what happened with a ter- verb, «tidak sengaja», one request, no blame, no advice |

**The four teacher notes the brief asked for** are in the teacher notes and tested (`test_two_ter_side_by_side`, `test_tertinggal_against_hilang`, `test_apology_and_state_notes`): ter- accident against ter- superlative (the Kata-Kata first card says it; «Yang ini termurah, tetapi dompet saya tertinggal di rumah.» shows both in one sentence; the root decides: an adjective gives "the most", a verb gives "by accident"; learn each ter- word as a word); «tertinggal» (left behind) against chapter 15 «hilang» (lost): "do I know where it is?"; apologising in Malay («Maaf, saya terlupa.» is the whole apology, answer «Jangan risau.») against Japanese うっかり〜てしまいました, which marks the slip twice; «terkunci» as a state («Pintu terkunci.»), not an action, with «masih» for a state and «baru» or «sudah» for an accident.

**Every ter- word shows its root and the root's chapter**, and says "by accident, without meaning to": «tinggal» (chapter 2), «lupa», «tidur», «lepas» (chapter 4), «tumpah» and «kunci» (this chapter); ‹jatuh›, ‹silap›, ‹langgar›, ‹gelincir›, ‹cedera›, ‹bakar›, ‹putus›, ‹sangkut› and ‹malang› are ‹…› mentions with their Kata-Kata cards as sources (eight new root entries and an extended ‹putus› in `curriculum/malay-mentions.json`, plus ‹ter-› and ‹tak sengaja›). The three chapter 6 superlatives «termurah», «terbesar», «terbaik» are a revision group beside them, marked "the most (not an accident)".

**Clinic safety.** The injury is described only as «Tangan saya bengkak dan ada luka kecil. Lutut saya pun lebam.» The receptionist's three lines are Kata-Kata's («Encik tercedera? Di mana yang sakit?», «Encik perlu daftar dulu. Ini borang.», «Boleh. Sila tunggu sekejap.»). There is no diagnosis, treatment advice or medicine anywhere; the role-play stops at «Sila tunggu sekejap.»; the reading is a registration form; the writing block says "only what is visible". `test_clinic_safety` checks the Malay spans for banned words and the receptionist's lines.

**Kata-Kata alignment:** the same frames f01 to f06; all six frame examples and all **17** scenario lines appear word for word, and the three scenes of the brief are the model (locked out with the key inside; Mei Ling late with «terlepas bas», «tersangkut», the spilt coffee and the broken cup; Tanaka's slip and the clinic); card IDs are cited in the opener (ms-c16-001 to -023), the vocabulary entries, the teacher notes and the culture sources.

**Rules applied.** No Assalamualaikum or Waalaikumsalam and nothing faith-specific; no «lah» or «kan» in any key; «dari» only before a place; «kita» and «kami» as in chapter 15 (no group message here, so no teacher-note change); the bare root only in Kata-Kata's own dialogue lines («Saya hubungi pejabat pengurusan.», «Encik perlu daftar dulu.») and first-person replies, with «menunggu», «mendaftar», «menghubungi» in the readings and keys; no «tangguhkan» or «batalkan»; Malaysian «kemalangan» (not the Indonesian word); all names, units and times fictional.

## Core-word coverage

All 23 core words appear in the unit outside the vocabulary list (the test checks this and that every revision word is really used). "Practised only" means the word is drilled and used in scenes but is not a scored test item. **16 of the 23 words are tested** (a word counts once it is a listening, word, grammar or reading item); all 23 are in the fast pack (Sam's ruling of 13 Nov: fast packs hold all core words).

| Tested | Practised only |
| --- | --- |
| tertinggal, terlupa, terlepas, tertumpah, terkunci, tersilap, tertidur, tergelincir, tersangkut, terputus, tidak sengaja, terlanggar, kemalangan, luka, bengkak, licin | terjatuh, tercedera, terbakar, kunci, tumpah, lebam, pecah |

The brief named eleven ter- words; the ledger places 23 core words at chapter 16, so «terjatuh», «tertidur» and «terbakar» are in the unit too (the plan's own table). «terbakar» appears only as «Roti itu terbakar.» (burnt bread), with no fire or emergency scene. Thin spots: «terjatuh» appears three times and «terbakar» three times outside the vocabulary list, and the bare root «tumpah» once (the vocabulary example is «Air tumpah di lantai.»). A pilot teacher may want one more drill item for each.

## Code and data changed

- `suite/ms_c16.py` (the unit and the writing block `EXTRA`) and the chapter 16 fast pack in `suite/fast.py` (`C16_WORDS`, `chapter16`, `STAGE2_PACKS`). The unit imports `chapter10_common.unit_dict` unchanged.
- `suite/__init__.py`: grammar points ms-c16-g02 to g09; the unit is loaded. No GLOSS entry was needed (no ledger meaning contains Malay).
- `course.py`: chapter 16 «Accidents with ter-» (unit 16), genre Accidents, and its status line. `catalogue.py`: sixteen chapters, chapter 16 goal and focus; the `writing-16` extra block and the `ms-stage2-writing-16` additional block.
- `curriculum/reauthored-units.json`: ms-c16 and ms-c16-fast added. `curriculum/malay-mentions.json`: eleven entries added or extended (‹jatuh›, ‹silap›, ‹langgar›, ‹gelincir›, ‹cedera›, ‹bakar›, ‹sangkut›, ‹malang›, ‹ter-›, ‹tak sengaja›, and the existing ‹putus› now also cites card ms-c16-013), each with its Kata-Kata card as the source. `curriculum/legacy-exceptions.json` unchanged (20).
- Tests: `tests/test_stage2_ch16.py` is new (19 tests: ledger partition, core-word use, roots and mentions, the two ter-, «tertinggal» against «hilang», the apology and state notes, clinic safety, casual turns, the -kan rule and «dari» / «daripada», Kata-Kata alignment with all 17 lines, register, minimums, the writing block, openers, culture note, Japanese, fast pack, registration). `test_catalogue` expects 16 chapters, 23 units, 115 blocks and 253 slots, levels A1 × 9 + A2 × 7.
- `tools/check_spans.py` was run on the unit file at chapter 16 before building: 0 problems (354 spans).
- Docs: `docs/stage-2-decisions.md` section 12; `HANDOFF.md` (latest session, template note, four backlog rows); a chapter 16 note in `docs/stage-2-plan.md`.

## Lines a native speaker should read first

These are my judgement calls; everything passes the checks, but the checks cannot judge whether a line sounds natural.

1. Pattern 2: «Maaf, saya tersilap nombor.» and «Nombor ini bukan nombor Encik Tanaka.»
2. Pattern 4: «Kenapa awak di tangga?» «Lif itu rosak. Saya tergelincir di tangga.»
3. Pattern 4: «Maaf, talian terputus.» and the vocabulary example «Roti itu terbakar.»
4. Pattern 3: «Maaf, saya tidak sengaja tertidur.» and «Ya, saya tidak sengaja. Cawan itu terjatuh di lantai.»
5. Pattern 1: «Kunci awak tertinggal di dalam?» «Betul, kunci saya tertinggal di dalam bilik.»
6. Pattern 5: «Saya mahu cawan yang termurah.» «Yang ini termurah. Yang itu pecah.»
7. Listening: «Pemandu teksi menelefon pejabat untuk saya, tetapi talian terputus.»
8. Listening: «Maaf, saya juga tersilap hari. Saya ingat mesyuarat hari Khamis.»
9. Listening: «Awak tertinggal fail itu semalam.» and «Hari ini saya tidak mahu terlupa lagi.»
10. Variant: «Maaf, pejabat pengurusan belum buka. Cik tunggu sekejap.» and «Boleh. Sila duduk.»
11. Reading: «Sebab: tergelincir di tangga. Bila: pagi tadi. Tangan: bengkak dan ada luka kecil. Lutut: lebam.» and the note «Encik sudah mendaftar. Sila tunggu sekejap.»
12. Writing block: «Boleh tolong hubungi pengawal? Saya menunggu di lobi.» and the culture note's guardhouse sentence (general knowledge, labelled).

All Japanese is a draft for the native review. The bridges (うっかり〜てしまった against «ter-»; 〜ている against «terkunci»; 一番〜 against «termurah») are teaching hypotheses.

## Word proposals for Sam (not in the ledger; I rewrote the lines instead and added no rows)

| Proposed form | Why it came up | What the unit says instead |
| --- | --- | --- |
| «tidak apa-apa» (never mind) | the everyday answer to «Maaf» | «Jangan risau.» (Kata-Kata s07) |
| «berlaku» (to happen) | "what happened" in a report or a clinic form | «Sebab: tergelincir di tangga.» |
| «masalah» (problem) | «Ada masalah?» to a late colleague | «Kenapa?» |
| «pinjam» (to borrow) | the taxi driver lends his phone | «Pemandu teksi menelefon pejabat untuk saya» |

All four are on the HANDOFF "Word proposals backlog" with the earlier ones.

## Questions for Sam

1. **Turn 11 crosses a scene.** Kata-Kata gives 17 lines and the charter allows 16 turns. The only two consecutive lines of one speaker are s11 and s12, so turn 11 is «Terima kasih. Hati-hati, lantai licin. Selamat pagi. Saya tergelincir di tangga tadi.»: Tanaka warns about the floor in the evening scene, then greets the clinic the next morning. A teacher note says so. The alternative is a model of s01 to s11 with the clinic scene (s12 to s17) in Block E only. Is the join acceptable here, where it crosses a scene change?
2. **Eleven words in the brief, 23 in the unit.** The unit also teaches «terjatuh», «tertidur» and «terbakar» because the ledger and Kata-Kata place them at chapter 16. «terbakar» is only burnt bread. OK?
3. **Five patterns.** f03 and f06 share pattern 4 (a thing is the subject; a state; a request). The order is f01, f02, f04, f03 and f06, f05. Is that the pair you want merged?
4. **Speaker labels.** «Guard» and «Receptionist» are English because «pengawal» and «penyambut tetamu» are ledger words (the chapter 15 rule). Would you rather the labels be Malay now that the words are taught?
5. **The apology answer.** The unit says «Jangan risau.» only. «tidak apa-apa» (the everyday answer) is on the backlog. Keep it there for the batch after chapter 17?
6. **Menu names.** Title «Accidents with ter-», genre «Accidents». OK?

## Not verified

- **Kamus Dewan:** none of the chapter 16 forms was checked (end of the project, ledger Journal row 128). The cards' notes are the source for the roots and traps; the card notes for «terjatuh», «tersilap» say the root is not a class card, and the other roots are mentions only.
- **Facts:** the culture note states no figure, rule or date about Malaysia; the guardhouse sentence is general knowledge, labelled and not source-checked. The apology norms are teaching hypotheses. The items, names, units, places and times are fictional.
- **PDF:** the build's fit check passed for every page. I did not review the pages by eye.
- **Environment:** the build needed `pymupdf`, `fonttools`, `brotli` and `fonts-noto-cjk` (after `apt-get update`); I installed them in the session. The checkout was shallow and was unshallowed first.
