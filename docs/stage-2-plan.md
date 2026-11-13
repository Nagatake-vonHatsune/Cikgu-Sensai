# Malay Stage 2 (A2): plan and proposed word lists

**12 November 2026 · Stage 2 · PLANNING ONLY · drafted by ChatGPT (Batch 1), audited and corrected by Claude (Batch 1b).**
Status: **audited; Sam's decisions recorded on 13 Nov 2026** (every recommendation accepted, «bertolak» added to 10A, no chapter 10 pilot gate, charter edited for R7; see the answers in the brief and [Sam's decisions](#sams-decisions-13-nov-2026) at the end). Sam's questions are now in [`docs/stage-2-decisions.md`](stage-2-decisions.md) (one line each); the audit is summarised in [`docs/STAGE-2-audit-report.md`](STAGE-2-audit-report.md), and every change Claude made to this file is listed in the [Audit log](#audit-log) at the end. Nothing here approves vocabulary, ledger rows, chapter suites or changes to the other tools. All Japanese is a draft for native review.
**Review gate (Sam, ledger Journal row 128, 12 Nov 2026):** the Kamus Dewan check and the native Japanese review happen once, at the end of the whole project. They do not block the Stage 2 ledger writes; rows are written as Draft with "KD4 check" in their Action cell. Sam has now answered the brief, so the ledger writes (build step 1) can go ahead; the four forms once marked "Sam to confirm" are confirmed.

## Source record and findings

Read the current Google Doc charter on 12 November 2026 (revision `AHj4eMSDx09t9TRA4282cxmjAp5E4tDGXr_w7rSQvjQjjhE-WWoP-YSf7ufoflnf3l9D5p4PVaQonBwPNGDwA8IBIQqNjD-bxDNH-6FGcCw`), especially sections 5, 6, 8 and 14; the repository snapshot agrees on the Stage 2 sequence. Read `AGENTS.md`, all of `HANDOFF.md`, `docs/STEP-5h-report.md`, `suite/ms_c07.py`, and the ledger copy `curriculum/reference/katakata/malay-ledger.csv` (L-0001 to L-1083). Starting main: `bb72bc5`; its only change after the handoff commit `228d961` is the Stage 1 test-time amendment to the charter snapshot.

- The ledger contains **no Kata-Kata place with Ch10 to Ch18, including no “primes Ch10 or later” rows**. The requested first-priority pool is empty. Use the unplaced Jambatan/Hanashishou rows and deferred forms instead; do not invent chapter placements or IDs.
- Existing Stage 1 recognition words remain revision when activated for speaking in Stage 2. They are not counted as new core words. Unplaced Hanashishou words can become proposed new core, even though they already have ledger IDs.
- Chapter 18 is review and assessment, with **zero new words**. A 20-word minimum there would contradict the charter's review-only scope.
- Five blocks per teaching unit follows the explicit Stage 1 decision and implemented suites. The older “four blocks” / “four or six blocks” prose in section 6 is inconsistent with that decision. No charter edit is made here.
- The starting charter said 57.5 hours for 76 Stage 1 blocks. **Resolved during this session by Claude in `a4099cf`: the live charter and snapshot now say 57 hours.** The table still folds the two test blocks into a note rather than a separate row. Stage 2 accounting below separates them.

Primary curriculum source: [Unified Curriculum Charter v0.1](https://docs.google.com/document/d/1d-uiYfQixReMUlPAcUEJ6R4onWOh-4Aa9urr14DL2lw). Repository evidence is pinned to the starting commit above. Counts, pacing, tasks and assessments below are proposals, not external CEFR certification claims.

**Concurrent source update:** main advanced to `a52c6a0` during section 2: Claude added approved Stage 1 rows L-1084–L-1088 (pesta, perhatian, hingga, tolak, tarik). Reconciled against the refreshed copy: none of the 235 proposed core forms duplicates these five rows; hingga is now Stage 1 revision beside proposed sehingga, and tolak is the existing root for chapter 17 menolak. No Stage 2 ledger permission is implied. The section 2 checkpoint followed that upstream commit. Later concurrent commits `55db51d` and `9d719e8` completed the Stage 1 test follow-ups and updated `HANDOFF.md` / `docs/STEP-5i-report.md`; both were read and preserved before final validation. The final source ledger is L-0001–L-1088. The newer Stage 1 decisions are recorded in the handoff/report and Journal, not inferred as A2 approval. A final docs-only upstream commit, `a4099cf`, corrected the Stage 1 hours; preserved it and re-read the live charter at revision `AHj4eMSXOEF1Yjacpzxp7Au6A3kRKnlzjTOSEy31iMqHUOUKNiMcUpcvMNyRSpIHApOj8eke2Mmwmpysd4SfMTg-g5NdQ1FXl-RyGwy426U`, confirming 57 hours. No course code changed in that last upstream commit.

**Audit sources (Claude, Batch 1b, 12 Nov 2026):** the live charter (same revision as above), `AGENTS.md`, `HANDOFF.md`, `docs/STEP-5h-report.md` and `docs/STEP-5i-report.md`; the ledger regenerated from the sheet at `29f0217` (Ledger!A1:T1089, L-0001 to L-1088) and Journal rows 120 to 129; `language_checks.py` and `curriculum/malay-roots.json`; `curriculum/foundation.txt`; and the Hanashishou repository at `55fd4ed` (all nine scene files and five vocabulary files cited below exist at exactly the blob SHAs this plan records; the claims about their content were spot-checked). Every one of the 235 draft forms was checked against every ledger row (exact form, each slash variant, multi-word rows and English meaning).

## 1. Unit plan, blocks and hours

Propose **11 teaching units across chapters 10 to 17**, plus chapter 18 as a five-block stage close. Split the three morphology-heavy chapters; keep later functional chapters intact. This preserves the agreed chapter order without carrying Stage 1's 13-unit count into a different syllabus.

| Unit | Scope | Blocks | Additional block after unit |
| --- | --- | ---: | --- |
| 10A | ber- routines, work and movement; retrieve known roots | 5 | None |
| 10B | ber- background, states and activities; exception review | 5 | Writing: a short personal background and weekly routine |
| 11A | meN- active verbs and familiar transitive di- pairs | 5 | None |
| 11B | nasal spelling changes; office actions and deferred hobbies | 5 | Review 1: chapters 10–11 with Stage 1 passive and aspect |
| 12A | -kan requests, actions for another person, delivery | 5 | Writing: parcel collection instructions |
| 12B | -i and selected whole verb families; repair/contact requests | 5 | Review 2: chapters 10–12, request and response |
| 13 | negation, permission, obligation and advice in health situations | 5 | None |
| 14 | reasons, conditions, purpose, contrast and sequence | 5 | Writing: explain and rearrange a plan |
| 15 | yang descriptions and cumulative question words | 5 | Review 3: chapters 13–15 plus earlier verb contrasts |
| 16 | accidental ter- and resulting states, apology and complaint | 5 | Writing: a brief factual incident message |
| 17 | standard/spoken choices, particles, invitations and refusals | 5 | None |
| 18 | integrated review, rehearsal, A2 tasks and next-step planning | 5 | Included below, not another five-block teaching suite |

### Five-block teaching-unit template

Each block is 45 minutes and has one observable can-do goal adapted to its unit. A: words and patterns (5 recall, 5 learner questions, 10 vocabulary check, 20 pattern work, 5 substitutions). B: drills and conversation (5 recall, 20 all six section 14 drill types in order, 15 model/gapped dialogue, 5 rehearsal). C: listening and task (5 recall, 15 teacher-read listening, 10 reading/writing, 15 independent exchange including a change of plan). D: review and check (15 mixed retrieval, 10 low-stakes check, 10 self-check/feedback, 10 homework preview). E: scene transfer (5 recall, 10 graded scene listening, 15 role-play, 10 changed situation, 5 home-practice briefing).

Every teaching unit ultimately needs all eleven section 6 components and its minimums: 3–5 patterns with 4–6 exchanges each; at least six items for each of drill types 1–5 and three short dialogues; 10–16-turn model plus gap and variant; 120–250-word listening with six questions; a reading with five questions and writing model; role cards and change of plan; 150–300-word sourced culture note; 15–20 scored test items plus speaking; real item-by-item keys. These are authoring requirements, not material created in this batch. The ten-minute D check may need sampling across two sittings if the pilot shows the full item set cannot fit.

All units continue the cumulative question-word set and aspect-marker drills. Roots already taught are retrieved before affixed forms. Each new pattern returns in chapter n+1, n+3, and chapter 18. For late chapters, returns that fall beyond 18 are brought into separate chapter 18 tasks and retained as Stage 3 handover obligations, rather than claimed completed three chapters later.

### Review, writing and assessment

Each intermediate review: recall 5, mixed input 10, alternating role task 15, changed situation 10, self-check 5. Each extra writing block: recall 5, model/notice comparison 10, guided draft 15, peer or teacher feedback 10, rewrite 5. Use fictional names, addresses, procedures and numerical details; do not present invented clinic or condo rules as Malaysian law.

Chapter 18:

| Block | Outcome | Minutes |
| --- | --- | ---: |
| 18A | Integrated review across all five pack themes, including every chapter's patterns | 45 |
| 18B | Rehearsal and targeted repair: a new colleague's day, parcel problem and changed invitation | 45 |
| 18C | A2 check: listening 12, reading 15, writing 18 | 45 |
| 18D | Speaking: about 7 minutes per learner; one examiner can assess six learners | 45 |
| 18E | Feedback, can-do review, demonstration of appropriate Hanashishou band 1 scenes and personal practice plan | 45 |

Propose parallel A/B test versions, four sections of 20 marks, 48/80 overall and at least 10/20 per section, **subject to Sam's approval**. This proposes carrying over the Stage 1 scoring structure, now approved in Sam's step 5i decisions; it is not a validated CEFR cut score and still needs an explicit A2 decision. Map every item to words, patterns, chapter and can-do; require coverage of chapters 10–17 in both versions and compulsory task evidence for the key contrasts. Writing and speaking assess successful communication, comprehensibility and appropriate language; listening/reading have fact-specific keys. Use a local course-completion label; do not promise official A2 certification or equivalence from hours alone. More than six learners requires another speaking slot per six learners (or concurrent examiners), outside the base total.

| Block category | Count | Hours |
| --- | ---: | ---: |
| 11 teaching units × A–E | 55 | 41.25 |
| Intermediate reviews | 3 | 2.25 |
| Extra writing blocks | 4 | 3.00 |
| Chapter 18 review, rehearsal, assessment and feedback | 5 | 3.75 |
| **Full-course total** | **67** | **50.25** |

**Audit check:** 55 × 45 min = 41.25 h, 3 → 2.25 h, 4 → 3.00 h, 5 → 3.75 h; 67 blocks = 50.25 h. Correct. The pattern matches Stage 1 (three review blocks, four writing blocks, a stage close whose written papers are 12 + 15 + 18 = 45 minutes and whose speaking test is a separate block). Cumulative check against the charter's benchmark: Stage 1 is 57 class hours plus about 40 hours of self-study (charter section 6), Stage 2 is 50.25 plus 36, so a full-course learner reaches about 183 hours, inside the Cambridge A2 guideline of 180 to 200 cumulative hours quoted in charter section 3 (a planning figure, not a Malay attainment claim). At two blocks a week this is 33.5 teaching weeks, before holidays or extra assessment slots. Provisional home practice: 3 hours per teaching unit (33 hours) plus 3 hours for chapter 18, **36 hours**, total classroom plus home **86.25 hours**. Pilot these estimates; they are a workload budget, not a researched Malay A2 attainment threshold.

**Fast course:** exactly one 2–4-page, 45-minute summary pack for each chapter c10–c18, even where the full chapter has two units: **9 blocks / 6.75 hours**. Chapters 10–17 select 15–20 words from that chapter's approved core, key patterns with two examples each, one conversation, task, self-check and exact home sets. Chapter 18 instead recycles 15–20 previously taught words, gives a review task and directs the learner to the separate full assessment. A 45-minute review pack is not the complete four-skill test. Provisional home budget: 9–10 hours per chapter, 81–90 hours total. The fast course does not confer completion by attendance alone.


## 2. Proposed core word lists and ledger reconciliation

**Counting rule:** one ledger row is one core word. A taught surface form or fixed chunk is one row (as the ledger already does for «dibaca» L-0385, «menyimpan» L-0792 and «mengapa» L-1049); its family is recorded in the existing "Root (KD4)" and "Affix tag" columns. A root already taught is revision, not new.

**In the ledger after build step 1: 233 core forms, 56 existing ledger rows and 177 new rows (L-1089 to L-1265)** (draft: 235 = 53 + 182; the audit gave 233; Sam added «bertolak»; build step 1 left L-0657 «tempat kerja» as revision, see the note under unit 10A). Every unit is between 19 and 24 new core words, inside the "typically 20 to 40" of charter section 6 (unit 15 is one under 20; see the decision brief). Each table row carries an Audit column: kept, changed (with why), added or moved; dropped forms are listed under each table. The four forms whose Malaysian usage I was not sure of were put to Sam and are marked "confirmed by Sam".

| Unit | Draft core | Audited core | Existing rows | New rows |
| --- | ---: | ---: | ---: | ---: |
| [10A](#unit-10a) | 20 | 20 | 2 | 18 |
| [10B](#unit-10b) | 20 | 20 | 4 | 16 |
| [11A](#unit-11a) | 20 | 20 | 0 | 20 |
| [11B](#unit-11b) | 22 | 21 | 7 | 14 |
| [12A](#unit-12a) | 22 | 23 | 7 | 16 |
| [12B](#unit-12b) | 20 | 21 | 9 | 12 |
| [13](#unit-13) | 23 | 24 | 8 | 16 |
| [14](#unit-14) | 21 | 20 | 2 | 18 |
| [15](#unit-15) | 21 | 19 | 3 | 16 |
| [16](#unit-16) | 24 | 23 | 6 | 17 |
| [17](#unit-17) | 22 | 22 | 8 | 14 |
| **Total** | **235** | **233** | **56** | **177** |

**What the audit checked for every form:** Malaysian standard as in Kamus Dewan, never Indonesian (no Indonesian form was found; the Malaysian choices are noted where an Indonesian one exists); the everyday Malaysian sense; the register (formal or written forms are paired with their everyday partner); real need for a Japanese working adult in Malaysia at A2; spelling of every ber-, meN-, -kan, -i and ter- form (all correct; nasal changes listed in the notes); the chapter gate (no form arrives before its affix opens); and duplicates against all 1,088 ledger rows, including L-1084 to L-1088 and the rows the Kata-Kata clean-up touched (no exact duplicate; one near-duplicate, «sehingga» beside L-1086 «hingga», dropped; two "new" forms, «berpindah» and «menukar», are the standard forms the ledger already names in L-0667 and L-0604, so they are linked to them). All 53 existing IDs the draft cited exist with the stated headword, meaning and band, and none is placed in a chapter yet.

### Unit 10A

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| bekerja | to work | 働く | NEW | kept: lexicalised: ber- becomes be- before a first syllable ending in -er (kerja); teach as a whole word |
| berjalan | to walk | 歩く | NEW | kept |
| bercakap | to speak | 話す | NEW | kept |
| bermain | to play | 遊ぶ・スポーツをする | NEW | kept |
| berehat | to rest | 休む | NEW | kept: ber- becomes be- before r (rehat) |
| bersenam | to exercise | 運動する | NEW | kept |
| berenang | to swim | 泳ぐ | NEW | kept: ber- becomes be- before r (renang) |
| berlari | to run | 走る | NEW | kept |
| berbasikal | to cycle | 自転車に乗る | NEW | kept: Malaysian (not Indonesian bersepeda) |
| berjumpa | to meet | 会う | NEW | kept |
| berbual | to chat | おしゃべりする | NEW | kept |
| beratur | to queue | 列に並ぶ | NEW | kept: Malaysian (not Indonesian antre) |
| bersarapan | to have breakfast | 朝食をとる | NEW | kept: standard; everyday speech often just says «sarapan» (L-0614, Ch4) |
| bermula | to begin | 始まる | NEW | kept |
| berhenti | to stop | 止まる・やめる | NEW | kept |
| bersiap | To get ready | 準備する、したくする | L-0807 (existing) | kept |
| bersedia | To be ready or prepared (standard form of "sedia") | 準備ができている（「sedia」の標準形） | L-0916 (existing) | kept |
| ~~tempat kerja~~ | Workplace | 職場 | L-0657 (existing) | **revision, not core** (build step 1): the A1 test (version A) already uses the form label «Tempat kerja», built from Stage 1 words, so placing L-0657 in Ch10 would make Stage 1 content a forward reference; left unplaced (Journal row 144) |
| berlatih | to practise | 練習する | NEW | kept |
| rutin | routine | 日課 | NEW | kept |
| bertolak | to set off; to depart | 出発する | NEW | added by Sam (W9, 13 Nov): root «tolak» (push, L-1087, Ch9) changes meaning with ber-; «Pukul berapa kita bertolak?» |

**Unit 10A: 20 core forms (2 existing rows, 18 new).**

### Unit 10B

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| berumur | to be aged | 〜歳である | NEW | kept: standard; everyday speech says «Umur saya …» (Ch3) |
| berkahwin | to be married / get married | 結婚している・結婚する | NEW | kept: Malaysian (not Indonesian menikah); optional persona |
| berkeluarga | to have a family | 家庭を持つ | NEW | kept |
| berasal | to originate / come from | 〜の出身である | NEW | kept |
| bernama | to be named | 〜という名前である | NEW | kept: written or formal; everyday «Nama saya …» (Ch2) |
| bersekolah | to attend school | 学校に通う | NEW | kept |
| berkawan | to be friends | 友達になる・付き合う | NEW | kept: Malaysian (not Indonesian berteman) |
| berjiran | To live as neighbours (hidup berjiran = neighbourly living) | 隣同士で暮らす（hidup berjiran＝近所付き合い） | L-0779 (existing) | kept |
| berpindah | to move home | 引っ越す | NEW | changed: new row linked to existing root L-0667 «pindah», whose note already names berpindah as the standard form; L-0667 becomes chapter 10 recognition (spoken) |
| bercuti | to be on leave / holiday | 休暇をとる | NEW | kept |
| berniaga | to trade / run a business | 商売をする | NEW | kept: Malaysian (not Indonesian berdagang) |
| berbelanja | to spend money / shop | お金を使う・買い物をする | NEW | kept: spend money; contrast with L-0717 «belanja» (treat someone) in chapter 17 |
| berkumpul | to gather | 集まる | NEW | kept |
| berkenalan | To get to know someone; to be introduced | 知り合いになる、自己紹介し合う | L-0781 (existing) | kept |
| berminat | to be interested | 興味がある | NEW | kept |
| berpakaian | to wear clothes / be dressed | 服を着ている | NEW | kept: mostly in «berpakaian kemas» (dress code) |
| jiran | Neighbour | 隣人、近所の人 | L-0660 (existing) | kept |
| sepupu | Cousin | いとこ | L-0714 (existing) | kept |
| pengalaman | experience | 経験 | NEW | kept: whole word only: peN-…-an is a Stage 3 family |
| berdua | the two together | 二人で | NEW | kept |

**Unit 10B: 20 core forms (4 existing rows, 16 new).**

### Unit 11A

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| membeli | to buy | 買う | NEW | kept |
| membaca | to read | 読む | NEW | kept |
| menulis | to write | 書く | NEW | kept: t → n |
| memasak | to cook | 料理する | NEW | kept: m-initial root, no change |
| mengambil | to take / collect | 取る・受け取る | NEW | kept: meng- before a vowel |
| membuat | to make / do | 作る・する | NEW | kept |
| membuka | to open | 開ける | NEW | kept |
| menutup | to close | 閉める | NEW | kept: t → n |
| membawa | to bring / carry | 持ってくる・運ぶ | NEW | kept |
| membayar | to pay | 支払う | NEW | kept |
| mencari | to look for | 探す | NEW | kept |
| mencuci | to wash | 洗う | NEW | kept |
| memanggil | to call someone | 人を呼ぶ | NEW | kept: p → m |
| menghantar | to send / deliver | 送る・届ける | NEW | kept: meng- before h; Malaysian sense also "drop someone off" |
| menerima | to receive | 受け取る | NEW | kept: t → n; root ‹terima› has no ledger row (only «terima kasih»), so teach the whole form |
| menjawab | to answer | 答える | NEW | kept |
| melihat | to see | 見る | NEW | kept: root ‹lihat› has no ledger row; everyday speech says «tengok» (L-0577) |
| mendengar | to hear / listen | 聞く | NEW | kept |
| menunggu | to wait | 待つ | NEW | kept: t → n |
| menjual | to sell | 売る | NEW | kept |

**Unit 11A: 20 core forms (0 existing rows, 20 new).**

### Unit 11B

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| menyewa | to rent as tenant | （家・部屋を）借りる（賃借する） | NEW | changed: Japanese draft made specific: （家・部屋を）借りる（賃借する）, so it is not the same as meminjam |
| melancong | to travel for leisure | 旅行する | NEW | kept: Malaysian (not Indonesian berwisata) |
| mendaki | To hike; to climb (a hill) | （山を）登る、ハイキングする | L-0865 (existing) | kept |
| menyimpan | To keep, to store (standard form of "simpan") | 保管する、取っておく（「simpan」の標準形） | L-0792 (existing) | kept |
| menyemak | To check; to review | 確認する、目を通す | L-0819 (existing) | kept |
| menukar | to change / exchange | 替える・交換する | NEW | changed: new row linked to existing root L-0604 «tukar», whose note names menukar as the standard form; L-0604 becomes chapter 11 recognition (spoken) |
| mengira | to count / calculate | 数える・計算する | NEW | kept: k → ng |
| mengisi | to fill | 記入する・入れる | NEW | kept: meng- before a vowel |
| memilih | to choose | 選ぶ | NEW | kept: p → m; root «pilih» is Ch6 |
| meminjam | to borrow | （一時的に）借りる | NEW | changed: Japanese draft made specific: （一時的に）借りる |
| memesan | to order goods / food | 注文する | NEW | kept: p → m |
| menolong | to help | 手伝う・助ける | NEW | kept: t → n; contrast with «tolong» (please, Ch8) |
| mengajar | to teach | 教える | NEW | kept |
| draf | A draft | 下書き | L-0680 (existing) | kept |
| slaid | Slide (in a presentation) | スライド | L-0696 (existing) | kept |
| tarikh akhir | Deadline (formal, written) | 締め切り（あらたまった書き言葉） | L-0849 (existing) | kept: formal; L-0678 «deadline» (everyday, Sam: keep) becomes chapter 11 recognition (spoken) |
| rancangan | A plan | 計画、予定 | L-0684 (existing) | kept |
| semak | check / review (request) | 確認してください | NEW | kept: root used as a request: «Tolong semak draf ini.» |
| mesej | message | メッセージ | NEW | kept |
| menelefon | to phone | 電話をかける | NEW | added: replaces menyapu; t → n; root «telefon» L-0573 (Dunia); Hanashishou already uses it (L-0658 example) |
| mengecas | to charge (a phone, a battery) | 充電する | NEW | added · confirmed by Sam (13 Nov): replaces mengecat |

**Unit 11B: 21 core forms (7 existing rows, 14 new).**
Not core after the audit: ~~menyapu~~ (dropped: low need for this learner; s → ny is already shown by menyewa, menyimpan and menyemak. Replaced by menelefon); ~~mengecat~~ (replaced by «mengecas» (to charge a phone): same menge- spelling, far higher need; root «cas» is L-0583 (Dunia, primes Ch7)); ~~mengepos~~ (dropped: the usual transitive is ‹mengeposkan› (a -kan form, chapter 12); «menghantar» covers the need).

### Unit 12A

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| hantarkan | send / deliver for someone (request) | 送ってあげる・届けてください | NEW | kept |
| simpankan | keep for someone (request) | 預かってください | NEW | kept |
| ambilkan | get for someone (request) | 取ってきてください | NEW | kept |
| belikan | buy for someone (request) | 買ってきてください | NEW | kept |
| bawakan | bring for someone (request) | 持ってきてください | NEW | kept |
| tutupkan | close for someone (request) | 閉めてください | NEW | kept: charter example «Tolong tutupkan pintu.» |
| bukakan | open for someone (request) | 開けてください | NEW | kept |
| letakkan | put / place (request) | 置いてください | NEW | kept: double k |
| pulangkan | return something (request) | 返してください | NEW | kept |
| berikan | give (request) | 渡してください | NEW | kept: «beri» is on the root allow-list; everyday «bagi» (L-0482) |
| tunjukkan | show (request) | 見せてください | NEW | kept: double k |
| pastikan | To make sure | 確かめる、必ず〜するようにする | L-0743 (existing) | kept |
| pengawal | Security guard | 警備員 | L-0595 (existing) | kept |
| unit | Unit; flat (in a condo) | 部屋、住戸 | L-0654 (existing) | kept |
| pejabat pengurusan | The (condo) management office | 管理事務所 | L-0650 (existing) | kept |
| pondok pengawal | Guardhouse | 守衛所、警備員室 | L-0658 (existing) | kept |
| pemilik | Owner | 所有者、オーナー | L-0662 (existing) | kept |
| label | label | ラベル | NEW | kept |
| penerima | recipient | 受取人 | NEW | kept: written label on parcels; whole word |
| nombor penjejakan | tracking number | 追跡番号 | NEW | kept · confirmed by Sam (13 Nov): the ledger itself names it as the formal form of L-0608 «nombor tracking»; standard first, L-0608 as spoken recognition. Whether couriers really print this term is unconfirmed |
| lobi | lobby | ロビー | NEW | kept: L-0666 «lobi lif» is then compositional, not a new core word |
| koyak | torn | 破れた | NEW | kept |
| blok | Block (of a building) | 棟（ブロック） | L-0653 (existing) | added: needed for the wrong-unit parcel scene («Blok B, unit 12-3») |

**Unit 12A: 23 core forms (7 existing rows, 16 new).**

### Unit 12B

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| baiki | repair (request) | 修理してください | NEW | kept: Malaysian (never Indonesian ‹perbaiki›) |
| membaiki | to repair | 修理する | NEW | kept |
| hubungi | contact (request) | 連絡してください | NEW | kept: common on notices: «Sila hubungi …» |
| menghubungi | To contact | 連絡する | L-0789 (existing) | kept |
| tempahan | booking / reservation | 予約 | NEW | kept: root «tempah» is L-0451 (Dunia) |
| isikan | fill in / put in (request) | 記入してください・入れてください | NEW | kept: everyday speech prefers «isi» («Sila isi borang ini»); teach both |
| kosongkan | empty / clear (request) | 空にしてください | NEW | kept |
| hidupkan | switch on (request) | つけてください | NEW | kept: standard; everyday «buka» (lights, aircon), noted |
| matikan | switch off (request) | 消してください | NEW | kept: standard; everyday «tutup», noted |
| bersihkan | clean (request) | きれいにしてください | NEW | kept: bersih + -kan, not ber- + sih |
| kebocoran | A leak | 水漏れ、漏れ | L-0651 (existing) | kept |
| juruteknik | Technician | 技術者、修理の人 | L-0652 (existing) | kept |
| paip | Pipe | 配管、パイプ | L-0661 (existing) | kept |
| siling | Ceiling | 天井 | L-0649 (existing) | kept |
| kontraktor | Contractor | 工事業者、請負業者 | L-0665 (existing) | kept |
| slot | Time slot (a booked period of time) | 時間帯、枠 | L-0655 (existing) | kept |
| kerosakan | damage / fault | 故障・破損 | NEW | kept |
| aduan | complaint / problem report | 苦情・問題の報告 | NEW | kept |
| gantikan | replace (request) | 交換してください | NEW | kept |
| perlahankan | To lower (the voice); to slow down | （声を）小さくする、ゆっくりにする | L-0871 (existing) | kept: whole word (per- is Stage 3); fits a noise request |
| ganti | To replace; to stand in for someone | 代わりをする、代わる | L-0698 (existing) | moved: moved from unit 16, beside «gantikan» |

**Unit 12B: 21 core forms (9 existing rows, 12 new).**

### Unit 13

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| perlu | need / necessary | 必要である | NEW | kept |
| patut | should / advisable | 〜したほうがよい | NEW | kept |
| wajib | compulsory | 義務である・必須の | NEW | kept: secular use only («wajib isi borang») |
| dibenarkan | allowed | 許可されている | NEW | kept: di-…-kan: needs chapters 9 and 12 |
| kebenaran | permission | 許可 | NEW | kept: sense note: also means "truth"; taught only as "permission" («minta kebenaran») |
| nasihat | advice | 助言 | NEW | kept |
| alahan | Allergy | アレルギー | L-0633 (existing) | kept |
| simptom | Symptom | 症状 | L-0634 (existing) | kept |
| sakit tekak | Sore throat | のどの痛み | L-0631 (existing) | kept |
| temu janji | Appointment | 予約、約束 | L-0638 (existing) | kept |
| farmasi | pharmacy | 薬局 | NEW | kept: Malaysian (not Indonesian apotek) |
| dos | dose | 用量 | NEW | kept: reading a label only; no dosage advice is authored |
| arahan | instruction | 指示 | NEW | kept |
| kesihatan | health | 健康 | NEW | kept |
| rawatan | treatment | 治療 | NEW | kept |
| elakkan | avoid (request) | 避けてください | NEW | kept: existing L-0788 «mengelak» stays unplaced |
| sesuai | suitable | 適している | NEW | kept |
| kecemasan | emergency | 緊急事態 | NEW | kept: Malaysian (not Indonesian darurat) |
| penyambut tetamu | Receptionist | 受付係 | L-0627 (existing) | kept |
| bila perlu | When needed | 必要なときに | L-0636 (existing) | kept |
| mesti | must | 〜しなければならない | NEW | kept |
| klinik panel | Panel clinic (one your company has an agreement with) | パネルクリニック（会社が契約しているクリニック） | L-0630 (existing) | added: used three times in the linked Hanashishou scene clinic_visit |
| daftar | To register | 登録する、受付をする | L-0648 (existing) | added: registering at the clinic counter (clinic_registration scene) |
| cuti sakit | sick leave | 病気休暇 | NEW | added · confirmed by Sam (13 Nov): spoken «MC» is used seven times in clinic_visit; propose «MC» as its marked spoken form |

**Unit 13: 24 core forms (8 existing rows, 16 new).**
Not core after the audit: ~~larangan~~ (dropped: «dilarang» (Ch9) already covers notices; the noun adds little at A2); ~~risiko~~ (dropped: abstract, low need for the permission and advice functions).

### Unit 14

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| supaya | so that | 〜するために・〜するように | NEW | kept |
| walaupun | although / even though | 〜だけれども | NEW | kept |
| jika | if | もし〜なら | NEW | kept: formal or written; everyday «kalau» (Ch7) |
| apabila | when | 〜するとき | NEW | kept: formal or written; everyday «bila» (Ch4) |
| sambil | while doing | 〜しながら | NEW | kept |
| namun | however (written) | しかし（書き言葉） | NEW | kept: written only; everyday «tapi» |
| oleh itu | therefore | そのため | NEW | kept: formal; everyday «jadi» |
| akhirnya | finally | 最後に・ついに | NEW | kept |
| mula-mula | first / at first | 最初に | NEW | kept: whole word (reduplication is Stage 3) |
| seterusnya | next | 次に | NEW | kept: formal; everyday «lepas tu» from known words |
| semasa | during / when | 〜の間に | NEW | kept |
| sejak | since | 〜以来 | NEW | kept |
| tujuan | purpose | 目的 | NEW | kept |
| pilihan | choice | 選択肢 | NEW | kept |
| keputusan | decision / result | 決定・結果 | NEW | kept |
| perubahan | change | 変更・変化 | NEW | kept: whole word (per-…-an is Stage 3); needed for "change of plan" |
| jadi | so / therefore | だから・そのため | NEW | kept |
| tangguh | To put off; to pause for a while | 延期する、一時休む | L-0641 (existing) | added: postponing is the core "change of plan" move |
| janji | A promise; to promise | 約束（する） | L-0710 (existing) | added |
| batal | to cancel; cancelled | 取り消す・中止になる | NEW | added: «dibatalkan» on notices; spoken loan «cancel» noted |

**Unit 14: 20 core forms (2 existing rows, 18 new).**
Not core after the audit: ~~sehingga~~ (dropped: duplicates L-1086 «hingga» (until, Ch9); shown as a ‹sehingga› mention beside it); ~~selagi~~ (dropped: B1 level; «kalau» covers the A2 need); ~~sebaliknya~~ (dropped: B1 level; not needed for the five A2 functions); ~~alasan~~ (dropped: reads as "excuse" and can sound accusatory («Apa alasan awak?»); «sebab» (L-0688) already means "reason").

### Unit 15

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| hilang | lost / missing | なくなった | NEW | kept |
| ciri | feature | 特徴 | NEW | kept: usually reduplicated «ciri-ciri» on forms; recognise both |
| berjalur | striped | しま模様の | NEW | kept |
| tali | strap / cord | ひも・ストラップ | NEW | kept |
| poket | pocket | ポケット | NEW | kept: Malaysian (not Indonesian saku) |
| dompet | wallet | 財布 | NEW | kept |
| beg tangan | Handbag (narrowed from "hand luggage; handbag") | ハンドバッグ | L-0623 (existing) | kept: sense narrowed to "handbag" (L-0623 also says hand luggage) |
| kulit | Leather; also skin | 革；皮膚 | L-0618 (existing) | kept |
| nombor plat | Car number plate | 車のナンバー（ナンバープレート） | L-0591 (existing) | kept: useful for identifying an e-hailing car |
| bentuk | shape | 形 | NEW | kept |
| bulat | round | 丸い | NEW | kept |
| segi empat | square or rectangular (four-sided) | 四角形 | NEW | changed: English gloss changed to "square or rectangular (four-sided)", the everyday sense |
| zip | zip / zipper | ファスナー | NEW | kept |
| seperti | like / such as | 〜のような | NEW | kept: standard; spoken «macam» (L-0930) |
| lelaki | man; male | 男性・男の | NEW | added: no ledger row exists; needed to describe a person |
| perempuan | woman; female | 女性・女の | NEW | added: no ledger row exists; needed to describe a person |
| cermin mata | glasses | めがね | NEW | added: compound; «cermin» L-0556 (mirror) is Stage 1 recognition |
| barang | thing(s); belongings | 物・持ち物 | NEW | added: «barang hilang» (lost property) |
| jenama | brand | ブランド・銘柄 | NEW | added |

**Unit 15: 19 core forms (3 existing rows, 16 new).**
Not core after the audit: ~~berbintik~~ (dropped: low need; natural form is reduplicated ‹berbintik-bintik› (Stage 3)); ~~berzip~~ (dropped: the chapter target «beg yang ada zip» says the same thing with yang); ~~berlengan~~ (dropped: everyday «baju lengan panjang» uses «lengan» (L-0977, Dunia) without ber-); ~~pemegang~~ (dropped: low need for lost-item and person descriptions); ~~tanda harga~~ (dropped: no use in the chapter 15 scenes; stays unplaced); ~~segi tiga~~ (dropped: low need; «bulat» and «segi empat» cover bags and boxes); ~~jalur~~ (dropped: «berjalur» covers it).

### Unit 16

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| terjatuh | to fall accidentally | うっかり落ちる・転ぶ | NEW | kept |
| tertinggal | To be left behind by accident | （うっかり）置き忘れる | L-0619 (existing) | kept |
| terlupa | To forget (by accident) | うっかり忘れる | L-0644 (existing) | kept |
| tertidur | to fall asleep unintentionally | うっかり寝てしまう | NEW | kept |
| terlepas | To miss (a bus, a chance) | （バスやチャンスを）逃す、乗り遅れる | L-0621 (existing) | kept |
| tersilap | To be mistaken; to get something wrong (by accident) | 間違える、間違いが起きる（うっかり） | L-0752 (existing) | kept |
| tertumpah | to spill accidentally | こぼれてしまう | NEW | kept |
| terlanggar | to bump into accidentally | うっかりぶつかる | NEW | kept |
| terkunci | locked / accidentally locked | 鍵がかかっている・かかってしまう | NEW | kept |
| tercedera | injured | けがをする | NEW | kept |
| tergelincir | to slip | 滑る | NEW | kept |
| terbakar | burnt / on fire | 燃える・焼ける | NEW | kept |
| terputus | cut off / disconnected | 切れてしまう・途切れる | NEW | kept: e.g. water supply or a call cut off |
| tersangkut | Stuck (in traffic or somewhere) | （渋滞などで）身動きがとれない | L-0875 (existing) | kept |
| tidak sengaja | By accident; not on purpose | うっかり、わざとではなく | L-0758 (existing) | kept: spoken «tak sengaja» |
| kemalangan | accident | 事故 | NEW | kept: Malaysian (not Indonesian kecelakaan) |
| luka | wound | 傷 | NEW | kept |
| lebam | bruise | あざ | NEW | kept |
| bengkak | swollen | 腫れた | NEW | kept |
| licin | slippery | 滑りやすい | NEW | kept |
| pecah | broken / shattered | 割れた | NEW | kept |
| tumpah | spill / spilled | こぼれる | NEW | kept: root beside «tertumpah»; everyday «Air tumpah!» |
| kunci | key | 鍵 | NEW | added: the chapter 16 scene is a key left inside the flat; «terkunci» needs the noun |

**Unit 16: 23 core forms (6 existing rows, 17 new).**
Not core after the audit: ~~kecederaan~~ (dropped: formal noun; «tercedera» and «luka» cover the need); ~~ganti~~ (moved: to unit 12B, beside «gantikan»; a root should not arrive four chapters after its -kan form).

### Unit 17

| Malay | English meaning | 日本語（草稿・母語話者の確認待ち） | Ledger | Audit |
| --- | --- | --- | --- | --- |
| kat | at / in (spoken, standard di) | 〜で・〜に（話し言葉） | NEW; spoken | kept: spoken; standard «di» |
| kan | confirmation-seeking particle (spoken) | 〜でしょう・〜よね（話し言葉） | NEW; spoken | kept: spoken; recognition first (see the decision brief) |
| lah | discourse particle (spoken, tone-dependent) | 語調を調整する助詞（話し言葉・文脈による） | NEW; spoken | kept: spoken; recognition first (see the decision brief) |
| ajak | To invite along; to ask someone to come (informal) | （気軽に）誘う | L-0689 (existing) | kept |
| sudi | To be willing; glad to (polite) | 喜んで〜する（ていねい） | L-0828 (existing) | kept |
| lapang | Free (not busy) | 手が空いている、暇な | L-0656 (existing) | kept |
| setuju | agree | 賛成する | NEW | kept: standard before «Set!» (L-0703) |
| menolak | decline / reject | 断る | NEW | kept: root «tolak» (push, Ch9); new sense "decline" |
| cadangan | suggestion | 提案 | NEW | kept |
| segan | hesitant / shy | 遠慮する・気が引ける | NEW | kept |
| sayangnya | what a pity | 残念なことに | NEW | kept |
| malangnya | Unfortunately | 残念ながら、あいにく | L-0787 (existing) | kept |
| lain kali | another time | また今度 | NEW | kept |
| tidak mengapa | it is all right / never mind | 大丈夫・かまわない | NEW | kept: standard; spoken partner is existing L-0940 «tak apa» (Stage 1 recognition) |
| macam tu | like that (spoken, standard seperti itu) | そんなふうに（話し言葉） | NEW; spoken | kept: spoken; standard «seperti itu» (chapter 15) |
| tak tahan | Can't handle; can't stand (informal) | 耐えられない、苦手だ（くだけた言い方） | L-0690 (existing); spoken | kept: spoken; show «tidak tahan» first |
| set | "Deal!" / "Agreed!" (everyday speech) | 「決まり！」（日常の話し言葉） | L-0703 (existing); spoken | kept: spoken; «setuju» first |
| belanja | To treat someone (pay for them) | おごる、ごちそうする | L-0717 (existing) | kept |
| singgah | To drop in; to stop by | 立ち寄る | L-0748 (existing) | kept |
| ni | this (spoken, standard ini) | これ・この（話し言葉） | NEW; spoken | kept: spoken; standard «ini» |
| tu | that (spoken, standard itu) | それ・その（話し言葉） | NEW; spoken | kept: spoken; standard «itu» |
| jemputan | invitation | 招待・招待状 | NEW | added · confirmed by Sam (13 Nov): replaces pelawaan |

**Unit 17: 22 core forms (8 existing rows, 14 new).**
Not core after the audit: ~~pelawaan~~ (replaced by «jemputan» (invitation; «kad jemputan»), the everyday noun; root «jemput» L-0541 is Stage 1 recognition).

### Chapter 18: no new core list

Reuse the approved chapters 10–17 inventory and Stage 1 dependencies. Its fast pack selects 15–20 revision forms across the five themes; the full test does not introduce unknown words. Core 0, recognition 0, revision selected by the assessment item map.

### Revision · 復習, recognition and deferred candidates

These are deliberately outside the new-core totals. A teacher may activate recognition vocabulary for production without pretending it is a new lexical introduction. The final suites must list only revision items actually used in their scenes, following the unit 7/8 standard.

| Chapter | Minimum revision anchor set (existing ledger rows) | Recognition / scope decision |
| --- | --- | --- |
| 10 | kerja L-0065; jalan L-0321; cakap L-0473; main L-0074; belajar L-0069; hujung minggu L-0702; sarapan L-0614; umur (Ch3) | belajar is an existing whole-word exception, not NEW. L-1045 duplicates hujung minggu and must not supply another core item. Recognition: L-0667 «pindah» (spoken partner of «berpindah»). |
| 11 | baca L-0474; tulis L-0475; ambil L-0481; buat L-1076; masak L-1023; sewa L-1051; cuci L-1078; panggil L-1077; pilih L-0280; tolong L-0375; telefon L-0573; cas L-0583; tengok L-0577 | Deferred forms: memasak/membuat in 11A; menyewa/melancong/mendaki in 11B. «terima» and «lihat» have no root rows, so «menerima» and «melihat» are taught as whole forms. Recognition: L-0604 «tukar» and L-0678 «deadline» (spoken partners). |
| 12 | tolong L-0375; bungkusan L-0430; kotak L-0359; pintu L-0565; simpan L-0529; isi L-0420; buka L-0484; tutup L-0485; tempah L-0451; chapter 11 menghantar, menyimpan, menyemak, mesej | L-0608 nombor tracking: optional spoken recognition only, after new standard nombor penjejakan; existing row, not core. L-0666 lobi lif can be understood compositionally after lobi; no duplicate core count. |
| 13 | tidak/tak L-0030; bukan L-0130; belum L-0194; jangan L-1062; boleh L-0076; rehat L-0417; dilarang L-0397; doktor L-0407; ubat L-0408; demam L-0409; batuk L-0410 | mesti is on the root allow-list but has no exact ledger row: genuinely NEW, not permission supplied by that allow-list. No diagnosis or dosage advice is authored. |
| 14 | kerana L-1050; sebab L-0688; kalau L-0341; sebelum L-1002; selepas L-1001; tetapi/tapi L-0215; kemudian L-0320; bila L-1007; hingga L-1086; sampai L-0203; cuaca L-0431; hujan L-0434 | These are already taught, so the new work is connecting clauses. jadi has no exact row and is proposed here, not silently assumed earlier. ‹sehingga› is shown only as a mention beside «hingga». |
| 15 | yang L-0212; kenapa L-1009; bila L-1007; yang mana L-0279; corak L-0511; warna L-0225; beg L-0504; baju L-0500; seluar L-0501; topi L-0503; rambut L-0927; lengan L-0977; kad L-0124; pasport L-0421; kaunter L-0423; chapter 12 pemilik | pemiliknya is revision via -nya, not a new word. All earlier question words return. No accidental ter- introduced a chapter early. |
| 16 | termurah L-0275; terbaik L-0277; maaf L-0018; rosak L-0588; lantai L-0571; pintu L-0565; chapter 12 aduan/kerosakan/ganti; chapter 13 symptom terms | Contrast superlatives with event/state ter-. Other ter- meanings and idioms wait; do not infer meaning merely from a prefix. |
| 17 | tidak/tak L-0030; mahu/nak L-0213; sudah/dah L-0193; sedikit/sikit L-0216; sahaja/saja L-1000; tetapi/tapi L-0215; macam mana L-0211; pun L-0983; jom L-0075; jemput L-0541; betul ke? L-0944; tak apa L-0940; macam L-0930 | These spoken forms and chunks are systematised, not counted new. ni/tu are NEW rows even though the register checker already names them. Other regional forms are excluded. |
| 18 | All earlier chapters as required by the item map | No vocabulary inflation to meet a teaching-unit minimum. |

**Core totals by chapter in the ledger (build step 1):** 10 = 40; 11 = 41; 12 = 44; 13 = 24; 14 = 20; 15 = 19; 16 = 23; 17 = 22; 18 = 0. Total 233 (draft 235). New-to-course recognition (existing rows, never tested as new core): L-0667 «pindah» (10), L-0604 «tukar» and L-0678 «deadline» (11), L-0608 «nombor tracking» (12). Revision counts will follow actual scene usage, not an invented total before authoring.

### Existing parcel pack: move and re-author, not relabel

Read `curriculum/foundation.txt` and `curriculum/foundation-guided.txt`, “Ambil bungkusan di lobi”. Its existing dialogue leads with nak/dah and includes tak/ni, unplaced vocabulary, and jadi/perlu before their proposed chapters. Plan a chapter 12 adaptation whose standard model begins “Saya mahu ambil bungkusan. Sudah sampai?” and uses the learned request forms. Use “Boleh tunjukkan mesej?” rather than the later modal perlu; omit jadi until chapter 14; use ini rather than ni; use baik instead of adding elok solely for one line. semak and mesej enter 11B; lobi, unit, blok, pengawal, label and koyak enter 12A. Keep the wrong-unit/torn-label change of plan and a clear successful collection outcome. Fictional condo procedures only.

The exact legacy script is not approved for chapter 12 just because its title is linked. Remove or revise every out-of-scope line in both ordinary and guided versions, then retire the superseded listing while preserving provenance. No migration happens in this planning batch.

**Selection exclusions:** no religious expressions or ceremonies, no blanket import of higher-band Hanashishou vocabulary, no Indonesian substitutions, no new etymologies. Existing rows such as L-0853 akad nikah and L-0643 puasa are not proposed; any religious scene requires Sam's separate decision. Medical vocabulary is for reporting and understanding professional instructions, not treatment guidance.


## 3. Affix progression, register and stage-aware checks

### Teaching rules by chapter

| Chapter | Open for productive teaching | Boundaries and examples |
| --- | --- | --- |
| 10 | Selected ber- verbs: action, state, possession/background | “Saya bekerja di Kuala Lumpur.” / “Saya bercakap bahasa Melayu dengan jiran saya.” Teach the chosen lexical families, not ber- attached to any word. belajar is revision. **Corrected in the audit:** ber- has no nasal changes, but it has two spelling variants: be- before a root starting with r (berehat, berenang) or whose first syllable ends in -er (bekerja), and bel- in belajar only. So bekerja follows a rule and belajar is the one true exception. The charter's "no sound changes" should read "no nasal sound changes" (a proposal for Sam; the charter is not edited here). |
| 11 | meN- active forms: me-, mem-, men-, meng-, meny-, menge- | Start with familiar transitive pairs: “Aini membaca buku itu.” / “Buku itu dibaca oleh Aini.” Teach lexical mappings such as tulis → menulis, telefon → menelefon, sewa → menyewa, kira → mengira and cas → mengecas. Do not make a di- passive from every verb: melancong is not a transitive object-taking model. memasak, membuat, menyewa, melancong and mendaki enter here. |
| 12 | Selected -kan and -i families, including meN-...-kan/-i and corresponding passive/request forms | “Tolong simpankan bungkusan ini.” / “Boleh hubungi juruteknik?” / “Juruteknik sedang membaiki paip.” Teach each verb with its object and meaning. -kan is not a universal politeness ending; -i does not have one English or Japanese equivalent. baiki and membaiki are preferred repair forms. bersihkan is bersih + -kan, not ber- + sih. membeli is meN- + beli, not productive -i. |
| 13 | No new affix family; negation/modal combinations and controlled revision | “Saya belum makan.” / “Bolehkah saya masuk?” / “Saya perlu berjumpa doktor.” Contrast belum with tidak, bukan with noun predicates, and jangan with prohibitions. mesti/perlu/patut differ in force. wajib is secular obligation here. Medical scripts ask for clarification, not give treatment recommendations. |
| 14 | No new affix family; selected connectors and two-clause messages | “Kalau hujan, kita makan di kafe.” / “Saya tidak datang kerana saya bekerja.” Keep walaupun/namun manageable and marked by register; do not turn every everyday exchange into formal prose. Nominals such as keputusan are whole words, not an opening of productive ke-...-an. |
| 15 | No new affix family; noun + yang + short clause and precise questions | “Saya mencari beg yang ada zip.” uses a short clause to identify the item. Reuse earlier question words in genuine information gaps, not as a new-word list. |
| 16 | Selected accidental/unplanned/result-state ter- families | “Saya tertinggal telefon di pejabat.” / “Maaf, saya terlupa.” Contrast with chapter 6 termurah/terbaik. terkunci and terputus can describe resulting states; not every ter- form means an accident. Ability/success readings and idioms are outside this batch. |
| 17 | No new productive affix; systematic register and discourse work | Standard first: tidak/tak, mahu/nak, sudah/dah, ini/ni, itu/tu, di/kat, sedikit/sikit, sahaja/saja, tetapi/tapi, bagaimana/macam mana, seperti itu/macam tu, tidak mengapa/tak apa, tidak tahan/tak tahan, setuju/set. Every second form marked **spoken**. kan (confirmation) is distinct from suffix -kan; lah needs contextual tone examples, not a one-word translation; pun is an existing standard particle, not inherently slang. jom and jemput are invitations with different tone, not interchangeable contractions. |
| 18 | No new affix or register form | Assessment language stays within approved chapters 1–17. Standard production is always accepted; recognition of spoken forms does not require forced particle use. |

All examples in this section are planning illustrations, subject to Sam's Malaysian usage review and the eventual approved ledger check. No suite is authorised by showing them here.

### What the current code actually does

`language_checks.py` already blocks ber-/be-shaped words before 10 and me-shaped words before 11, but **only loads c01–c09 cards** (`range(1,10)`). Its derivation routine handles selected Stage 1 constructions, not the full Stage 2 families. There is no suffix -kan/-i gate or semantic accidental-ter gate. Chapter assignment currently takes the minimum number found in both card IDs and free-text place fields. That is unsuitable for approval decisions: a “waits for” note or historical placement can become permission accidentally.

The repo's affix root allow-list is `curriculum/malay-roots.json`, added to `ROOTS` in `language_checks.py`; it contains beri, mesej, memang, mesti, beritahu and mengapa. It classifies look-alike roots only. It neither creates ledger rows nor approves their chapter placement. Keep this file root-only. Do not add every Stage 2 affixed verb to it or enlarge `curriculum/legacy-exceptions.json`.

Read Kata-Kata `tools/affix-guard.mjs` and `tools/check-content.mjs` at `0f78179034552f85d4c0d7ac4cb9e185f8b8ac8a`. Its current guard receives packs but no chapter policy; `ALLOW_LIST` contains roots. It builds one global `exemptWords` set from all chunks/recognition cards, then permits those words anywhere. New later-chapter exemptions could therefore leak backwards into Stage 1. Fix that before loading c10–c18.

### Required implementation, after approval (simplified in the audit)

The draft listed eight requirements and a new policy schema with family mappings. The ledger already holds what the checks need, so the audit recommends this smaller design (decision S4 in the brief):

1. **The ledger drives the gate.** Each Stage 2 form gets its own row, like «dibaca» L-0385, «menyimpan» L-0792 and «mengapa» L-1049 today, with its chapter in "Kata-Kata place", its family in "Affix tag" and its root in "Root (KD4)". No separate policy file and no family-mapping schema. A form is allowed from its row's chapter; a row with no chapter, or a retired row, is never allowed in authored content.
2. **One table of affix openings, identical in both repositories:** ber- 10; meN- 11; -kan and -i 12 (a meN-…-kan or meN-…-i form needs both 11 and 12); ter- in the accident or unplanned-state sense 16 (superlative ter- and its Stage 1 whole words stay at 6). Whole words with Stage 3 affixes («pengalaman», «perubahan», «penerima», «kerosakan» and so on) pass only as their own ledger rows, never by rule.
3. **Read placement strictly.** Load every placed chapter instead of the fixed c01–c09 range (`range(1,10)` in `language_checks.py`), and take the chapter from the place field only, ignoring notes such as "waits for" or "was Ch…" (today `_chapter` is the minimum of every chapter number found). Register each Stage 2 unit in `curriculum/reauthored-units.json` when it is built. Keep `curriculum/malay-roots.json` for roots only.
4. **Kata-Kata: scope exemptions by chapter.** The draft found (at Kata-Kata 0f78179) that the affix guard builds one global exemption set from all chunks, so a chapter 12 chunk would become legal in Stage 1 once c10–c18 exist. Pass the chapter to the guard and allow a chunk only from its own chapter. Re-read the guard at the current Kata-Kata head before changing it.
5. **Register pairs:** add «kat», «ni», «tu», «macam tu», «tak apa», «tak tahan» and «set» with their standard partners; treat «lah» and «kan» as particles, not contractions of anything.
6. **Malaysian-form rules:** add ‹berbicara›, ‹perbaiki›, ‹musik›, ‹film› and ‹olahraga› as disallowed teaching forms, matched as whole words.
7. **Shared fixtures (Python and JavaScript must agree):** «bercakap» 9 fail / 10 pass; «menyewa» 10 fail / 11 pass; «membaiki» 11 fail / 12 pass; «tertinggal» 15 fail / 16 pass; «termurah» 6 pass without unlocking «terjatuh»; «membeli» and «mengisi» 11 pass (a final i is not -i); «makan» and «ikan» stay roots; «bersihkan» 11 fail / 12 pass; a chapter 12 chunk fails at chapter 9; an unlabelled spoken form fails; an unplaced or retired row fails. All Stage 1 checks and the shrink-only exception baseline stay as they are.

### Linguistic source checks and limits (12 November 2026)

- [DBP PRPM: bekerja](https://prpm.dbp.gov.my/Cari1?d=175768&keyword=bekerja) and [DBP morphology reference](https://jendeladbp.my/app/uploads/woocommerce_uploads/2025/04/eDigital_Morfologi-qnsczr.pdf): indexed DBP text identifies bekerja and belajar as exceptions. This supports correcting “no sound changes”, not changing chapter order.
- [DBP PRPM: akhiran](https://prpm.dbp.gov.my/Cari1?d=175768&keyword=akhiran) and [DBP advice on -kan/-i](https://prpm.dbp.gov.my/Cari1?d=175768&keyword=lihat+kan): indexed explanations distinguish meanings and include membaiki. Do not teach a single mechanical translation of either suffix.
- [DBP PRPM: bercakap](https://prpm.dbp.gov.my/Cari1?d=10456&keyword=bercakap): indexed Kamus Dewan Edisi Keempat senses support speak/use a language/chat. This course selects those senses.
- [DBP PRPM: terjatuh](https://prpm.dbp.gov.my/Cari1?d=72508&keyword=terjatuh): indexed Kamus Dewan definition supports the accidental-fall sense.

- **Audit, ber- spelling (12 Nov 2026):** secondary grammar sources found by web search (not Tatabahasa Dewan itself) agree that ber- becomes be- before r-initial roots and roots whose first syllable ends in -er (bekerja), and bel- only in belajar. Treated as [INFERRED] until the end-of-project Kamus Dewan check. «mengecas» could not be found in PRPM by search, so it is marked Sam to confirm.

These were retrieved through web-search excerpts; direct PRPM page opens timed out or returned errors. **Do not mark a full KD4 review complete or invent page references.** A row-by-row check, spelling/valency review and Japanese native review remain before approved publication of teaching material. No legal, clinic, transport, price or institutional fact is asserted by the fictional scenes in this plan.


## 4. Charter can-do goals and proposed refinements

These preserve the charter's sequence and functions. The measurable task limits are teaching proposals for pilot review, not externally validated CEFR thresholds. Japanese translations are complete drafts for native review. Use an optional fictional persona for personal background and health tasks.

| Ch | Charter draft goal | Proposed learner-facing goal | 日本語（母語話者の確認待ち） | Reason for refinement / evidence to collect |
| --- | --- | --- | --- | --- |
| 10 | Retell your day and your background in full sentences | I can describe my usual day and background in four to six connected sentences and answer two follow-up questions. | 普段の一日と自分の背景について、つながりのある4〜6文で話し、追加の質問二つに答えられます。 | Makes “full sentences” observable without requiring advanced narrative. Routines in 10A, background in 10B; marital/family details can be fictional or omitted. |
| 11 | Say who does what; switch between active and the di- passive from chapter 9 | I can explain who does an office task and what happens to the object, using an appropriate active or passive sentence. | 職場の作業を誰がするか、その対象がどうなるかを、適切な能動文または受動文で説明できます。 | Tests meaning and roles, not prefix substitution alone. Only transitive verbs take the paired transformation. The hobby extension uses active verbs without artificial passive counterparts. |
| 12 | Ask someone to do something for you; report a repair or delivery | I can make a clear request about a parcel or repair, give the place and time, and confirm the agreed next step. | 荷物や修理について、場所と時間を伝えて明確に頼み、合意した次の対応を確認できます。 | Gives the exchange a checkable outcome. Parcel work in 12A, repair/contact in 12B; selected -kan/-i families serve that outcome. |
| 13 | Give and understand rules, permission, need and advice | I can ask permission, explain a need, and distinguish a prohibition from advice or something not yet done in a simple health-related exchange. | 健康に関する簡単なやり取りで、許可を求め、必要なことを説明し、禁止・助言・まだ終わっていないことを区別できます。 | Avoids conflating “not allowed”, “should not” and “not yet”. Assess language comprehension using fictional instructions, not medical knowledge. |
| 14 | Explain why, set a condition, tell a short sequence of events | I can give a reason, set one condition, and describe three steps in a plan; I can explain a simple purpose or contrast when needed. | 理由を述べ、条件を一つ示し、計画の三つの手順を説明できます。必要に応じて、簡単な目的や対比も説明できます。 | Preserves all five connector functions but does not force five connectors into every utterance. Separate short tasks provide the evidence. |
| 15 | Describe a person or lost item precisely; ask why and when | I can identify a person or missing item with two useful details and a short yang clause, then ask questions that distinguish it from another possibility. | 役に立つ特徴二つと短い yang の節を使って人や紛失物を特定し、別の候補と区別するための質問ができます。 | Makes specificity the task. Why/when and the other question words are retrieval, not new grammar. Use fictional people and belongings. |
| 16 | Report a mishap, apologise, make a complaint politely | I can explain a small mishap, state what happened and where, apologise if appropriate, and ask for one practical next step. | 小さなトラブルについて、何がどこで起きたかを説明し、必要なら謝り、具体的な次の対応を一つ頼めます。 | Separates reporting from taking blame; avoids forcing an apology for someone else's fault. Contrast accidental events and resultant states with superlatives. |
| 17 | Follow natural spoken Malay; invite, accept and refuse without offence | I can recognise the taught spoken forms, choose a suitable standard or spoken response, and invite, accept or decline with a reason or alternative. | 学んだ話し言葉の形を聞き取り、場面に合う標準形または話し言葉で返答し、誘う・受ける・理由や代案を添えて断ることができます。 | “Without offence” cannot be guaranteed by a language test. Assess contextual appropriateness and successful communication. No requirement to imitate slang or add lah. |
| 18 | Pass the A2 exit tasks; set up Hanashishou at band 1 | I can complete the course's integrated daily-life, office, home, health and social tasks, identify what I need to practise, and start an appropriately tagged band 1 scene. | このコースの日常生活・職場・住まい・健康・交流を組み合わせた課題を終え、自分に必要な練習を確認し、適切な章タグのあるバンド1の場面を始められます。 | Replaces a circular “pass the test” goal with demonstrated tasks and next action. Hanashishou's recognition/self-rating result is not proof of spoken accuracy (SPEC.md §6.4). |

### One outcome per block, to carry into the eventual teaching plans

A = guided pattern use; B = controlled exchange; C = information/task outcome; D = check and repair; E = transfer to a changed scene. Each cell below is read as “I can …”. The section 1 timings apply.

| Unit | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| 10A | state a routine with a taught ber- verb | ask and answer about routines | extract a colleague's daily activities | correct a routine description | explain a changed workday |
| 10B | give two background details | exchange background questions | identify a neighbour from a short introduction | check my own introduction | introduce myself to a different neighbour |
| 11A | identify actor and object | change a suitable active sentence to passive | identify who completed an office task | correct reversed actor/object roles | report a different completed task |
| 11B | use the selected meN- spelling families | ask what a colleague is doing | confirm an action and its deadline | correct a chosen verb form | explain a new work or weekend activity |
| 12A | make a selected -kan request | request and confirm a parcel action | identify and collect the correct parcel | check the details of a collection message | resolve a wrong-label change of plan |
| 12B | use a selected -i/request family | request contact or a repair | agree a visit time and location | check a repair message for missing details | reschedule a repair visit |
| 13 | distinguish need, advice and prohibition | ask permission and clarify a rule | interpret a fictional clinic instruction | correct a negation/modal misunderstanding | ask for clarification in a changed situation |
| 14 | connect two ideas with a reason or condition | explain a purpose or contrast | sequence a simple plan | check connector meaning | rearrange the plan when a condition changes |
| 15 | attach a short description with yang | ask discriminating questions | identify the correct item | check description accuracy | identify an item after one detail changes |
| 16 | distinguish an accident/state from a superlative | report a mishap and respond | agree one practical next action | correct an unclear incident report | handle a different small mishap |
| 17 | match spoken forms to standard meanings | select a suitable invitation response | arrange or decline a social plan | explain a register choice | respond to a changed invitation with an alternative |

Assessment must accept more than one natural Malaysian answer when it achieves the task. Do not penalise an appropriate standard form because the model uses a spoken form. Every full Japanese explainer and answer-key note must translate its English counterpart fully; no shortened Japanese summaries or residual English prose.


## 5. Malaysian scenes, Hanashishou links and Japanese transfer

All classroom scenes below are fictional adaptations for Japanese working adults living in Malaysia. They make no claim about a real property's procedures, a clinic's requirements, fares, opening hours, medicine or current regulations. Japanese-transfer notes are teaching hypotheses for Sam and a native Japanese reviewer to test, not claims that all Japanese learners make the same errors.

The charter's pack labels map to the actual repository folders `daily-life`, `office`, `home-condo`, `health`, `social`. Malay story paths below are relative to `content/packs/<pack>/targets/ms/story/`. The corresponding Malay `vocab.json` files were read on 12 November 2026. A pack link is a **curriculum destination**, not approval to run every current scene at that chapter.

| Ch | One or two classroom scenes and outcome | Charter pack and inspected scene anchor | Japanese helps / potential interference |
| --- | --- | --- | --- |
| 10 | 10A: telling a colleague about your usual working day and weekend (classroom scene). 10B: meeting a neighbour and exchanging background details, using an optional persona; the e-hailing driver's "Where are you from?" small talk as the speaking link. Outcome: understand the person's routine and two background details. | Daily life: `daily-life/grab_ride_chat.ink` (**audit:** the scene is background small talk, «Awak dari mana?» with «berpindah» at band 3, plus steering the driver to the office; it suits 10B, not "the working day"). Also `home-condo/new_neighbour.ink`, whose bands 1–2 use root words only, for 10B. | Familiar self-introduction routines help; separate time markers can be compared with Japanese time expressions. Avoid treating ber- as a Malay equivalent of -ます or adding it to every verb. Japanese often leaves subjects implicit; use explicit actor cues when learners need them, without banning natural Malay ellipsis. |
| 11 | 11A: a colleague reads a document and sends it to another colleague; identify who did what. 11B: check a draft and confirm when it will be ready; optional short discussion of cooking/travel/hiking after work. | Office: `office/report_deadline.ink`; draf/menyemak/slaid from the office word pool, mendaki from Social. | Familiar transitive/intransitive distinctions can help discussion, but Malay meN- is not a tense or politeness ending. Do not transfer a negative/adversative interpretation to every di- passive. Nasal spelling changes need word-family retrieval, not Japanese conjugation rules. |
| 12 | 12A: collect two parcels at a condo guardhouse; the small box belongs to another unit (block and unit numbers). 12B: report water at the ceiling and agree a technician's visit. Outcome: correct item or a confirmed next action/time. | Home and condo: `home-condo/guardhouse_parcel.ink`, `home-condo/ceiling_leak.ink`; also `home-condo/aircon_repair.ink` for «hidupkan» / «matikan». Cikgu Sensai's “Ambil bungkusan di lobi” is adapted here. | Request frames such as 〜てください help establish intent. They do not predict whether Malay needs -kan, -i or neither. English/Japanese glosses must show the recipient, object and place separately; do not equate -kan mechanically with 〜てあげる. |
| 13 | Ask permission and clarify a simple fictional clinic notice; ask a pharmacist to repeat an instruction, without authoring a real dose or treatment recommendation. Outcome: distinguish must, should, may and must not. | Health: `health/clinic_visit.ink`, `health/pharmacy_advice.ink`; also `health/clinic_registration.ink` (a starter scene: first visit, registering). **Audit:** clinic_visit uses «MC» seven times and «klinik panel» three times, so chapter 13 now has «cuti sakit» (spoken «MC», Sam to confirm), «klinik panel» and «daftar». Their full scripts require adaptation and content review before assignment. | まだ and もう help with belum/sudah; 〜てもいい, 〜なければならない and 〜たほうがいい help frame permission/obligation/advice. They are approximate bridges. Jangan is a prohibition, not an interchangeable negative ending. |
| 14 | Rearrange a weekend activity because of rain or a work commitment; explain a three-step plan with one condition and one alternative. Outcome: both people agree when/where and what happens if the condition changes. | Social: `social/weekend_plans.ink`. Use fictional meeting places and timings rather than repeating unverified weather or safety advice. | Japanese reason/condition connectors give useful functional comparisons. Avoid word-for-word 〜から/〜ので/〜たら mapping; choose by the relationship between clauses. Keep Malay clause order and short messages natural. |
| 15 | Describe a missing wallet to station staff; identify a visitor or colleague from clothing and an agreed meeting location. Outcome: select the right item/person from plausible alternatives. | Daily life: `daily-life/lost_wallet.ink`. Chapter 15 version must say hilang rather than the original opening's tertinggal; return to the accident account in 16. | Japanese noun-modifying clauses provide the concept, but come before the noun. Malay noun + yang + clause reverses that order. Questions need useful distinguishing details, not just a memorised interrogative. |
| 16 | Explain a small spill or a key left inside a flat; report a minor fall at a clinic reception using fictional details. Outcome: state what happened and request a practical next step. | Home and condo + Health: reuse adapted `home-condo/guardhouse_parcel.ink` or `ceiling_leak.ink` problem/response structure; adapted `health/clinic_visit.ink` for the minor incident. Daily life's `lost_wallet.ink`, `missed_bus.ink` («terlepas») and `wrong_order.ink` (pointing out a problem without blame) are optional cross-pack recycling, not replacement charter links; `home-condo/noisy_renovation.ink` fits the polite complaint. | 〜てしまった can help introduce unintended events, but does not cover every ter- sense. A resulting state may resemble 〜ている, while chapter 6 superlatives require a separate reading. Apologies depend on responsibility and context. |
| 17 | Accept or decline a colleague's dinner invitation; rearrange a weekend outing and offer another time. Outcome: an explicit answer and, when appropriate, an alternative. | Social + Office: `social/weekend_plans.ink`, `office/team_dinner.ink`. | Japanese invitations, refusals and sentence-final particles offer a familiar pragmatic topic. lah and kan are not automatic replacements for よ and ね. Indirectness alone does not guarantee clarity: practise an understandable yes/no plus reason or alternative. |
| 18 | Integrated working-week scenario: introduction and office handover, parcel/repair problem, appointment clarification and changed invitation. Second parallel version uses different fictional details. Outcome: complete all four skill sections and choose targeted home practice. | All five packs, using only audited chapter-tagged versions of the anchors above. | Translate only when it supports comprehension; the task outcome is achieved in Malay. Japanese self-check wording must not hide a different standard from the English rubric. |

### What inspection of the linked sources changes

The five Malay vocabulary files were read at these blob SHAs (the files, not whole-repository commit IDs):

| Pack | `content/packs/<pack>/targets/ms/vocab.json` blob |
| --- | --- |
| daily-life | `6989f4d996209d1e3ef50804070fa2dd48f2d442` |
| health | `c5ef70d2565923b837c16bce52e138edd0226058` |
| home-condo | `bc305aac9792d62632f79344974af3feda0fa945` |
| office | `2f3df3b9f3c29eceb948efd1c552856acd866e02` |
| social | `d963367ed332e7d709bf4b36e4d44de8f5b66c59` |

Source browser: [Hanashishou content packs](https://github.com/Nagatake-vonHatsune/Hanashishou/tree/main/content/packs). Also read `SPEC.md` §§6 and 8 and the target-language framework examples in `content/targets/ms/ms.json` (blob `328682732f9fd5886420d25830fba677d8901d35`).

- `report_deadline.ink` (blob `d58342fd17065ccc60bfa6d6461138295fc5e46c`) already contains later words and suffixes, plus ni/kan in colleague lines. Chapter 11 must use a graded extract or adapted counterpart, not unlock the full story simply because its pack is Office.
- `guardhouse_parcel.ink` (`8f29f94b337bfd3d3a5d8e278943bc4a29ea8b20`) has a useful unit-number/two-box outcome but uses perlu in the guard's loop. The chapter 12 adaptation must rephrase that loop or wait until 13. Higher branches contain bahawa, which belongs to Stage 3.
- `ceiling_leak.ink` (`ef100f58f5fb26f50ab8161b364080e49e4c7316`) includes menitis, sejak, perlu and other later/unselected language. Keep the clear place/problem/time structure and graded request task; do not copy all words into chapter 12 to make it fit.
- `lost_wallet.ink` (`96ce795a81077268c70f9f85715c0fea2a5ba86d`) opens with tertinggal before even the band 1 choice. That is a concrete reason why filtering learner choices by band alone is insufficient for chapter 15.
- `weekend_plans.ink` (`56b28cb3f6dfa51be95302bb237151495dfd0658`) and `team_dinner.ink` (`73b0e40b229d93b893b34aaf93853a543057cc21`) include informal forms in narration/other-speaker lines. Tag and teach those forms, or grade the input; do not silently waive them.
- `clinic_visit.ink` (`68dbed5d5b68fba1f2d3ad7483bd322220dc2b70`) and `pharmacy_advice.ink` (`7ddac461dc23194e37ca6ef29229dd4fdabfd367`) contain claims/procedures and medicine instructions. These remain source material, not verified health guidance. Adapt to fictional language tasks and obtain appropriate source checks before any learner-facing factual guidance.
- daily-life's beg tangan entry mixes handbag and cabin-baggage usage and includes a numeric baggage allowance. For chapter 15 use **handbag** (Japanese ハンドバッグ) only, as a proposed sense narrowing of L-0623; keep its identity and record the reviewed sense change rather than making a duplicate. Do not reproduce a baggage allowance as a universal rule.
- Existing words selected from higher bands (mendaki, menyemak, menghubungi, tarikh akhir and others) need short approved A2 examples. A source deck's band label neither prohibits a useful familiar word nor certifies that its whole scene is ready.

**Source limitation:** the inspected story anchors and vocabulary are sufficient to identify adaptation work; a complete audit of every branch, ladder, minigame, explainer and distractor is still an implementation gate. Proposed scene chapter tags are not represented as already present upstream. No external repository was edited.


## 6. Build order, approval gates and handover

Sam has decided that Claude builds Stage 2 and answered [`docs/stage-2-decisions.md`](stage-2-decisions.md) on 13 Nov 2026, approving this build order and its models (B1). Step 1 starts by recording the answers in the ledger Journal.

### Build order after Sam approves (audit proposal)

| Step | Session and tool | What it delivers | Recommended model |
| --- | --- | --- | --- |
| 1 | Ledger session (sheet, then Cikgu Sensai copies) | Journal rows recording Sam's answers; the approved rows written to the Ledger tab (new rows as Draft with "KD4 check" in Action, existing rows placed, roots in "Root (KD4)"); both copies and the hash regenerated, diff checked row by row | Sonnet: a mechanical change set from the audited tables, with a scripted duplicate and diff check |
| 2 | Cikgu Sensai | Stage-aware language checks and the affix allow-list (section 3, items 1 to 3 and 5 to 7) with the shared fixtures; no content | Opus: the gate logic decides what every later chapter may say |
| 3 | Kata-Kata session | Packs c10 to c18 (cards, frames, Sedia Kelas, Dunia scenes; c18 review only) and the stage-aware affix guard with scoped exemptions (item 4); a pinned snapshot for Cikgu Sensai | Opus for the guard and c10, then Sonnet for c11 to c18 with an Opus check of each pack's frames |
| 4 | Cikgu Sensai, chapter by chapter | Chapter 10 (10A, 10B, writing block, fast pack) as the template; then chapters 11 to 17 with their review and writing blocks, each to the section 6 minimums | Opus for chapter 10; Sonnet for chapters 11 to 17, with an Opus review after each chapter before it is published (no pilot pause after chapter 10: Sam, G3) |
| 5 | Cikgu Sensai | Chapter 18: the A2 review and rehearsal blocks, the A2 test (versions A and B, keys, scripts, administration sheet), the catalogue's Stage 2 record | Opus |
| 6 | Hanashishou session | Chapter tags on every Malay scene (all reachable text: narration, other speakers, every branch), graded or deferred branches, the Jambatan bridge rebuilt from the tags, and the L-0592 → L-0330 «pintu masuk» mapping | Sonnet for tagging, with an Opus review of the bridge rebuild |

Steps 3 and 4 run chapter by chapter after chapter 10 (Kata-Kata pack first, then the Cikgu Sensai suite), so each chapter's home preparation exists before its class pack. Sam decided (G3, 13 Nov 2026) not to pilot chapter 10 first: all chapters are built in order, each with an Opus review before the next starts. Missing words found while authoring or tagging go back through Sam and the Journal; they never enter the ledger to fit an existing script.

### Cross-tool acceptance checklist for later builds

- Same stable word IDs, approved sense, chapter/unit assignment and pattern IDs in all three tools; compare snapshot hashes and record source commits.
- Core / recognition / revision remain distinct. The recognition rows (L-0667, L-0604, L-0678, L-0608) are not assessed as new core words. Chapter 18 adds no vocabulary.
- Same lexical/affix policy outcomes in Python and JavaScript; no global exemption leakage and no permission derived from deferred notes.
- Shared frames, with actor/object meaning preserved in active/passive work. Accept natural Malaysian alternatives in keys; no filler, no unidiomatic line to satisfy a count.
- Every full teaching unit meets section 6 minimums and all six section 14 drill types; cumulative question words and aspect markers continue throughout.
- Explicit spaced-return schedule: 10 → 11/13/18; 11 → 12/14/18; 12 → 13/15/18; 13 → 14/16/18; 14 → 15/17/18; 15 → 16/18; 16 → 17/18 plus a carried-forward Stage 3 return; 17 → 18 plus a carried-forward Stage 3 return. Chapter 18 separates review and rehearsal so late-stage material is recalled more than once.
- Standard forms taught first and each spoken form visibly labelled, including stand-alone print extracts. For L-0690 tak tahan, show «tidak tahan» first; for L-0703 set, show «setuju» first; for «tidak mengapa», L-0940 «tak apa» is the spoken partner. Neither change is made now.
- Full Japanese translations in eventual instructional prose and keys, marked draft until reviewed. No etymologies beyond approved Kata-Kata notes.
- Facts supported by checkable sources; fictional procedures clearly labelled. No imported medicine doses, baggage limits, legal duties or religion-specific expressions without the necessary review and Sam's scope decision.
- Tests and full-history build pass; PDF pages are visually reviewed when suites are authored. A successful build of this planning document validates the unchanged course build, not the linguistic quality of proposed words.

### Questions for Sam

The draft's seven long questions are replaced by the one-sitting brief [`docs/stage-2-decisions.md`](stage-2-decisions.md).

### Publication and validation record

Section checkpoints were published incrementally to main using the connected GitHub service because shell push authentication was unavailable. The local checkout is full-history; each numbered section was build-checked and run through the complete unittest suite, then main was fetched and reconciled. Concurrent upstream code changes landed between some checks and publication; the completed plan was therefore checked again against the fully updated main before the final commit. Builds generate nondeterministic PDF archive changes; those were discarded rather than published as unrelated site changes. Only this plan and the final handoff note belong to this planning session. Initial baseline: 149 tests; after the first concurrent ledger update: 150; final updated-main validation: 153 tests. Final build: 335 packs / 2,139 pages, all fit-checked. All 53 existing core IDs were checked against their ledger headwords; no duplicate core forms or Stage 1 placements were counted as new. Proposed totals were recalculated: 235 = 53 + 182. These checks do not substitute for dictionary/native review.

| Section | Main commit |
| --- | --- |
| 1: unit plan | `7ac9c4fe6c5a7ad4954a650ff950dd61fbc623b2` |
| 2: word lists | `d6ec42bbcec58b144afe9bf48ce1433ef4d4b2b3` |
| 3: affix policy | `26ee232e470b9f35dd6e6b62a91a708a98240545` |
| 4: can-do goals | `55175a68f4e00de5ce9443204c712f039c0ec90c` |
| 5: scenes and source audit | `3e2c1ac83fc9d1ceebb4c55627fe0e733182dc86` |
| 6: build order and final questions | The commit containing this completed section and the accompanying handoff update |

No chapter suites, ledger rows, language-check code or external repositories were changed by this session. Concurrent Stage 1 changes by Claude are described in the source record, not claimed as this batch's work.

**Batch 1b (Claude, audit):** this file was corrected in place in one commit after `3f3c367`; see the Audit log below and `docs/STAGE-2-audit-report.md`. `python3 build.py` and all unit tests passed before publication. **Stop here for Sam's decisions.**

## Audit log

Claude, Stage 2 Batch 1b, 12 November 2026. Every change made to this file, and why. The decision brief lists only the items that need Sam's judgement.

### Word lists (section 2)

1. **Totals: 235 → 233 core forms; 53 → 57 existing rows; 182 → 176 new rows.** Of the 235 draft forms, 211 are kept as they were, 5 are changed in place, 2 are replaced, 1 is moved and 16 are dropped; 16 forms are added (2 of them the replacements). Each unit's table shows the status of every form.
2. **Changed in place (5):** «berpindah» and «menukar» are linked to the existing roots L-0667 «pindah» and L-0604 «tukar», whose ledger notes already name them as the standard forms (the roots become spoken recognition); the Japanese of «menyewa» and «meminjam» now distinguishes renting from borrowing (both were 借りる); the English of «segi empat» is now the everyday "square or rectangular".
3. **Replaced (2):** «mengecat» → «mengecas» (same menge- spelling, much higher need, root «cas» already in the ledger; Sam to confirm); «pelawaan» → «jemputan» (the everyday noun for an invitation; Sam to confirm).
4. **Moved (1):** L-0698 «ganti» from unit 16 to unit 12B, beside «gantikan».
5. **Dropped (16):** «menyapu», «mengepos», «larangan», «risiko», «sehingga», «selagi», «sebaliknya», «alasan», «berbintik», «berzip», «berlengan», «pemegang», «tanda harga», «segi tiga», «jalur», «kecederaan». Reasons are in each unit's "Not core after the audit" line: a duplicate (sehingga beside L-1086 hingga), B1-level or low need for this learner, a form the chapter's own yang pattern already covers (berzip), a reduplicated natural form (berbintik-bintik), a ‹-kan› transitive that belongs to chapter 12 (mengepos), or a pragmatic risk (alasan reads as "excuse").
6. **Added (16):** existing rows L-0653 «blok», L-0630 «klinik panel», L-0648 «daftar», L-0641 «tangguh» and L-0710 «janji»; new rows «menelefon», «mengecas», «cuti sakit», «batal», «lelaki», «perempuan», «cermin mata», «barang», «jenama», «kunci» and «jemputan». Each is needed by the chapter's own scene: the ledger has no «lelaki», «perempuan» or «kunci» although chapter 15 describes people and chapter 16 has a key left inside a flat; the linked Hanashishou clinic scene uses «MC» and «klinik panel».
7. **Recognition rows named** (existing rows, never tested as core): L-0667, L-0604, L-0678 «deadline» and L-0608 «nombor tracking»; the draft named only L-0608.
8. **Revision anchors** extended in every chapter with the Stage 1 rows the scenes actually reuse (for example the clinic words of chapter 5's Dunia scene for chapter 13, the clothing words of chapter 8 for chapter 15, L-0940 «tak apa» for chapter 17).
9. **Counting rule simplified:** one ledger row is one core word, and the family is recorded in the existing "Root (KD4)" and "Affix tag" columns. This answers the draft's derived-form storage question (see section 3, item 1).
10. The parcel-pack paragraph adds «blok» to the forms that enter in 12A.

### Structure, affixes and checks (sections 1 and 3)

11. **Hours re-checked** (all arithmetic correct) and a cumulative check added: about 183 hours of class and self-study by the end of Stage 2, inside the charter's quoted A2 guideline of 180 to 200.
12. **ber- explanation corrected:** «bekerja» follows the be- rule (first syllable ending in -er); «belajar» is the only true exception. The charter's "no sound changes" should become "no nasal sound changes" (proposal for Sam; charter not edited). Source: secondary grammar sources by web search, marked [INFERRED] until the end-of-project Kamus Dewan check.
13. Chapter 11 spelling examples updated to the audited list (telefon → menelefon, cas → mengecas instead of sapu and cat). Chapter 17's standard and spoken pairs now include «tidak mengapa / tak apa», «tidak tahan / tak tahan» and «setuju / set».
14. **Checks simplified:** the draft's eight implementation requirements and its proposed policy schema with family mappings are replaced by seven shorter items driven by the ledger's existing columns. The two real defects the draft found are kept: the fixed c01–c09 loader and minimum-chapter reading in `language_checks.py` (verified in the code), and Kata-Kata's global exemption set.

### Scenes (section 5)

15. **All Hanashishou anchors verified** at Hanashishou `55fd4ed`: the nine scene files and five vocabulary files exist at exactly the blob SHAs recorded; the draft's content claims (tertinggal in lost_wallet's opening, perlu in the guard's loop, ni and kan in report_deadline, later words in ceiling_leak) are correct; no linked scene contains a faith-specific greeting or «jalan lurus».
16. **Chapter 10 link corrected:** grab_ride_chat is background small talk and steering the driver, not "the working day", so it serves 10B; home-condo/new_neighbour (root words only at bands 1–2) is added for 10B and 10A becomes a classroom scene about the working day.
17. Extra anchors named: aircon_repair (12B), clinic_registration (13), missed_bus, wrong_order and noisy_renovation (16), all optional and still to be graded before use.
18. Scene naturalness checked: every proposed scene (e-hailing small talk, condo guardhouse parcel, ceiling leak, panel clinic, pharmacy, rained-off weekend plan, lost wallet at a station counter, key locked inside, dinner invitation) is an everyday situation for a Japanese professional in Malaysia. The plan states no real-world fact (rule, fare, dose, date) that needs a source; scenes are fictional, as the draft says.

### Build order and questions (section 6)

19. The eight-row shared workflow is replaced by the six-step build order Sam asked for, with a recommended model for each step.
20. The seven long questions are replaced by `docs/stage-2-decisions.md`.
21. The cross-tool checklist now names all four recognition rows and the «tak apa» pairing.

### Checked and left unchanged

- The unit split (11 units, five blocks each), the review and writing block positions, chapter 18's five blocks and zero new words, the fast course (nine packs), the pass rule carried over from Stage 1, and the can-do goals of section 4. All are consistent with the Stage 1 decisions (48/80 with 10/20 per section; writing items allowed; 76 Stage 1 blocks = 57 hours; standard forms first; no faith-specific greetings; no festivals added; «terus», never «jalan lurus»; classifiers with se-).
- Affix spelling: all 235 draft forms are spelt and formed correctly and none arrives before its gate; whole words with Stage 3 affixes are listed as whole words.

## Sam's decisions (13 Nov 2026)

Sam answered `docs/stage-2-decisions.md` in chat on 13 Nov 2026: **every recommendation accepted**, with these specifics.

- **W6, W7, W8: yes.** «mengecas», «jemputan» and «cuti sakit» (with «MC» as its marked spoken form) are confirmed.
- **W9: yes.** «bertolak» added to unit 10A (now 21 core; Stage 2 total 234 = 57 existing + 177 new).
- **R1: (a).** «nombor penjejakan» is a new row (written label) and L-0608 «nombor tracking» its spoken partner.
- **R7: yes, and Claude edits the charter.** Done on 13 Nov 2026: section 5 of the live charter (revision after the edit `AHj4eMSiZ2Bi…`) and `docs/handoff/charter-snapshot.md` now say ber- has no nasal sound changes, with be- (berehat, bekerja) and bel- (belajar) as its only spelling variants.
- **G3: no.** No chapter 10 pilot before the rest: build all chapters, with an Opus review after each.
- **B1: yes.** The six-step build order and models in section 6 are approved.

These answers are recorded here, in the brief and in `HANDOFF.md`; build step 1 copies them into the ledger Journal before writing any row.

## Build step 1: the ledger (13 Nov 2026)

Claude wrote the approved rows to the ledger sheet and regenerated both Cikgu Sensai copies.

- **Journal rows 130 to 132:** Sam's answers. **Rows 133 to 145:** the changes below.
- **New rows L-1089 to L-1265 (177):** Ch10 L-1089 to L-1122, Ch11 L-1123 to L-1156, Ch12 L-1157 to L-1184, Ch13 L-1185 to L-1200, Ch14 L-1201 to L-1218, Ch15 L-1219 to L-1234, Ch16 L-1235 to L-1251, Ch17 L-1252 to L-1265. All Draft, KD4 check "Not yet checked", Action "KD4 check", place "ChN (unit X)", root in "Root (KD4)", affix family in "Affix tag".
- **Existing rows placed:** 56 as core (place "ChN (unit X); Jambatan · …"), and L-0604, L-0608, L-0667, L-0678 as recognition. L-0623 narrowed to "Handbag" (Hanashishou keeps hand luggage in its own column).
- **One exception, for Sam to confirm:** L-0657 «tempat kerja» was not placed (see unit 10A), so the ledger holds 233 Stage 2 core forms (56 + 177).
- **Knock-on fixes the build required:** six lines of the legacy chapter 12 pack "Ambil bungkusan di lobi" no longer use «ni», «jadi», «perlu» or «macam tu» before their chapters (the review record `curriculum/malay-text-scope.json` and the two legacy-content tests list exactly those edits); «Bernama» and English «label» were added to the English homographs, since both are now ledger forms.
- Each batch was read back from the sheet and compared cell by cell with the plan: no other cell changed.

## Build step 2: stage-aware checks (13 Nov 2026)

Section 3's "Required implementation" is built: gates, whole words, register pairs, particles and disallowed forms are in `curriculum/stage-rules.json`, shared with Kata-Kata, with 69 shared cases in `curriculum/stage-rules-fixtures.json`. Stage 1 results are unchanged. Sam's answers to its three points (13 Nov 2026): «tidak mengapa» is not used, so «tak apa» has no standard partner and L-1261 awaits a ledger session; the disallowed forms and the stative ter- rule are confirmed. Report: [`docs/STAGE-2-step2-report.md`](STAGE-2-step2-report.md).
