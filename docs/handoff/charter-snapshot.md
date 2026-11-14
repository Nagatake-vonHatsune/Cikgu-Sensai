<!-- Snapshot of the Google Doc charter (master: https://docs.google.com/document/d/1d-uiYfQixReMUlPAcUEJ6R4onWOh-4Aa9urr14DL2lw), exported 2026-11-11, refreshed 2026-11-12 (the faith-expression sentence in section 8, Malay form rules, added) and 2026-11-13 (section 5, ber- has no nasal sound changes; Claude at Sam's request, Stage 2 decision R7). For builders without Drive access. If you can open the Google Doc, it wins. -->

# **Unified Curriculum Charter: Cikgu Sensai, Kata-Kata, Hanashishou (v0.1)**

Nov 11, 2026 · @Samuel Mancyni John Vianney Nagatake von Hatsune-Loh Yung Jian

## **Context: read this first**

This document is being handed to ChatGPT so it can continue building Cikgu Sensai as one part of a three-tool language-learning system. This section explains the situation. Section 12 says exactly what to build and in what order.

**Who it is for.** Sam teaches language classes in Malaysia. His students are mostly Japanese working adults living in Malaysia, at mixed levels. He currently teaches Malay in a nine-chapter order of his own design, and wants English and Japanese materials on the same footing.

**The three tools.**

| Tool | What it is | Used | Built with | Where |
| :---- | :---- | :---- | :---- | :---- |
| Cikgu Sensai | Printable worksheet library, becoming the full classroom textbook | In class | ChatGPT | [Live site](https://cikgu-sensai.vonhatsune.workers.dev), [repository](https://github.com/Nagatake-vonHatsune/Cikgu-Sensai) |
| Kata-Kata | Malay word and sentence-frame trainer for zero beginners | At home | Claude Code | [Repository](https://github.com/Nagatake-vonHatsune/katakata) |
| Hanashishou 話匠 | Speaking-practice game with a level evaluator | At home | Claude Code | [Live site](https://hanashishou.vonhatsune.workers.dev/), [repository](https://github.com/Nagatake-vonHatsune/Hanashishou) |

**The problem.** The three were built separately. Kata-Kata and Hanashishou already share a vocabulary ledger, a card format and a review scheduler. Cikgu Sensai was built later and shares none of them: its Malay units run in a different order from Sam's classes, use different words, and skip several of his grammar points. A student would meet three slightly different courses.

**The goal.** One syllabus, three tools. A student learns a chapter's words at home in Kata-Kata, is taught the chapter in class from Cikgu Sensai, and later practises speaking it in Hanashishou. The same chapters, words, patterns and level labels appear in all three.

**How this charter was produced.** On 11 Nov 2026 Claude read all three repositories and the live Cikgu Sensai site, compared them against Sam's nine-chapter order, and drafted this charter with Sam. Section 9 records what was found. Sam's decisions are listed in section 1\. Parts marked as proposals or drafts are not yet agreed.

**What this means for the builder of Cikgu Sensai.**

* Cikgu Sensai changes the most. It is restructured around Sam's chapters and grows from two components per unit to a full textbook suite.

* Kata-Kata is the reference for Malay content. Its chapter files already hold the agreed words and sentence patterns, and Cikgu Sensai should reuse them, not write new ones.

* The other two tools are not yours to change. If Cikgu Sensai needs something from them, raise it with Sam.

* Malay comes first. English and Japanese follow only after the Malay pilot is approved.

## **1\. Purpose**

This charter is the single reference for what is taught, in what order and how, across Cikgu Sensai, Kata-Kata and Hanashishou. Each tool keeps its own code and design. All three take chapters, word lists, sentence patterns and level labels from here.

It is written so the same text can be given to ChatGPT (which builds Cikgu Sensai) and Claude Code (which builds Kata-Kata and Hanashishou). When a tool's own spec disagrees with this charter on curriculum, the charter wins. On anything else (interface, hosting, game design) the tool's own spec wins.

Decisions already made by Sam (11 Nov 2026):

* Malay is unified first. English and Japanese follow the same design afterwards.

* Sam's nine-chapter Malay order is the spine. Cikgu Sensai is restructured to fit it.

* CEFR (A1 to C1) is the common level scale.

* Content is consistent across the tools. Learner progress is not shared between them, beyond the existing Kata-Kata to Hanashishou word file.

* Malay teaches standard forms first and marks colloquial forms as spoken. This rule is Malay-only.

* A class portion is a 45-minute core.

* Cikgu Sensai becomes a full textbook: tests, drills, grammar focus, vocabulary focus and listening focus, alongside its current activities.

Status: v0.1 is a draft for Sam's review. Sections 5 to 7 and 10 are proposals. Section 11 lists what still needs a decision.

## **2\. The three tools and the weekly loop**

Each tool has one job, and a learner meets every chapter in all three, in a fixed order.

| Tool | Where it is used | Job | Covers |
| :---- | :---- | :---- | :---- |
| Kata-Kata | Home, before and after class | Words and sentence frames, with spaced review | Malay, zero to A2 |
| Cikgu Sensai | Classroom | The textbook: teach, drill, practise, test | Malay, English and Japanese, A1 to C1 |
| Hanashishou | Home, after class | Speaking in realistic scenes, with a level evaluator | From A2 upward (band 1 is roughly A2) |

The loop for one chapter:

1. **Prime (home, Kata-Kata).** The learner does the chapter's Sedia Kelas set and arrives knowing the words. Questions go into Tanya Cikgu.

2. **Teach (class, Cikgu Sensai).** The 45-minute blocks run recall, pattern focus, drills, model conversation, listening and an independent task. Tanya Cikgu questions open the first block.

3. **Consolidate (home, Kata-Kata).** The chapter's Dunia scenes and spaced review recycle the same words in new settings.

4. **Check (class, Cikgu Sensai).** A short chapter test and a can-do self-check close the chapter. Weak items feed the next chapter's recall.

5. **Speak (home, Hanashishou).** From Stage 2 onward, the learner plays the scenes linked to that chapter. Before Stage 2, the Jambatan bridge scenes in Kata-Kata prepare the words.

The rule that makes this work: a word, pattern or grammar point appears in Cikgu Sensai only if it is in the shared ledger for that chapter or an earlier one. Kata-Kata already works this way.

## **3\. Teaching approach**

The approach combines three traditions into ten working rules that every chapter, in every tool, must follow.

| Tradition | What we take from it |
| :---- | :---- |
| Japanese language teaching | Sentence patterns built up one at a time (the Minna no Nihongo method). A fixed drill ladder from controlled to free. Can-do goals tied to real tasks (the Irodori and JF Standard method). Regular review lessons. Reading aloud and shadowing. |
| International practice | CEFR can-do descriptors as the level scale. A balance of input, output, language study and fluency work (Nation's four strands). Tasks with a real outcome, not only exercises. |
| Educational psychology | Retrieval practice. Spaced review. Worked examples that fade into independent work. Low-stakes testing. Mixing old and new material. A calm error climate for adult learners. |

The ten rules:

1. **One can-do goal per lesson block.** Written as "I can ...", tied to life in Malaysia, and checked at the end of the block.

2. **Patterns before rules.** Each grammar point enters as a sentence pattern with a slot to fill. The explanation comes after the learner has used it.

3. **Words first, at home.** Vocabulary is learnt in Kata-Kata before class, so class time goes to using it.

4. **Every block opens with recall.** Two to five minutes retrieving the previous block's language without notes.

5. **The drill ladder.** Repeat, substitute, transform, question and answer, then a free exchange. No step is skipped.

6. **Fade the support.** Model first, then a gapped version, then roles with no script, then a change of plan.

7. **Spaced return.** Each pattern is scheduled to reappear in the next chapter, three chapters later, and in the stage review.

8. **Build on Japanese.** Each chapter names where Japanese helps (counters, titles, location and direction particles) and where it interferes (adjective order, no verb conjugation, sounds).

9. **No red crosses.** Errors return later as practice. Tests are low-stakes and feed the next lesson.

10. **Controlled affixes and register.** New word forms enter only when the syllabus says so (section 8).

References the Cikgu Sensai site already cites: [KSBM framework](https://pppm.moe.gov.my/dokumen/39-lt2021-bm/file), [CEFR descriptors](https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors), [English Profile](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/418955FC7ED2455E98A499BC40C2C816/S2041536212000013a.pdf), [Minna no Nihongo](https://www.3anet.co.jp/en/minnaqa.html), [Irodori](https://www.irodori.jpf.go.jp/en/starter/pdf.html), [IES practice guide](https://ies.ed.gov/ncee/WWC/PracticeGuide/1).

Note on sourcing: this section summarises well-established methods from general knowledge. The linked sources were not re-read for this draft. Hanashishou's docs/LEARNING-SCIENCE.md holds a referenced version for that app and should be reconciled with this list.

### **Benchmarking against established textbooks (first pass done 11 Nov 2026\)**

Cikgu Sensai is meant to be an authoritative all-in-one resource: syllabus, curriculum, lesson plans and learner content. Its schedule and chapter contents must therefore be checked against established authorities before v1.0, not only named.

| Benchmark | What to take from it |
| :---- | :---- |
| Minna no Nihongo | Lesson anatomy, the order in which patterns accumulate, drill types, vocabulary load per lesson |
| Irodori and Marugoto (Japan Foundation) | Can-do goals per lesson, topic sequence for daily life, self-check format |
| KSBM and published Malay courses for foreign learners | Malay grammar sequence, standard topic order, level descriptors |
| CEFR Companion Volume and English Profile | Level descriptors and English grading |

Output of the benchmark: a comparison table per chapter (our content against each source), a pacing guide in class hours per level, and a list of gaps or reorderings to put to Sam. The first pass below covers lesson anatomy, pacing and assessment. The Malay grammar sequence has not yet been checked against KSBM or published Malay courses.

### **Benchmark findings: first pass**

The chapter suite matches the anatomy of Minna no Nihongo closely, the assessment plan matches Irodori, and the main gap is hours: both courses on their own cover less than half the study time the benchmarks give for A1.

| Source | Structure | Time |
| :---- | :---- | :---- |
| [Minna no Nihongo Shokyu I](https://plus.3anet.co.jp/?p=3955) | 25 lessons. Each: sentence patterns, example sentences, conversation, Exercises A, B and C, practice questions (listening, grammar, reading). A review every few lessons. Books I and II total [50 lessons](https://www.3anet.co.jp/en/minnaqa.html). | 4 to 6 hours a lesson; about 150 hours for Book I |
| [Irodori](https://www.irodori.jpf.go.jp/en/faq.html) Starter, Elementary 1 and 2 | 18 lessons per book, built on Can-do goals; listening and speaking activities carry the vocabulary and grammar | 2.5 to 3 hours of activities a lesson, 4 to 5 with language practice; 80 to 100 hours a book |
| [Cambridge guided learning hours](https://support.cambridgeenglish.org/hc/en-gb/articles/202838506-Guided-learning-hours) | Cumulative from zero, a guideline only | A1 90 to 100; A2 180 to 200; B1 350 to 400; B2 500 to 600; C1 700 to 800 |
| This charter, Malay Stage 1 | 9 chapters taught as 13 units, eleven components each | Full course 57 class hours; fast course about 7 |

What this changes:

1. **Lesson anatomy holds, with one addition.** Minna places short question-and-answer example sentences between the patterns and the conversation. Component 3 now includes them. The drill ladder corresponds to Exercises A, B and C.

2. **Chapter tests cover three skills.** Following Minna's practice questions, each test has listening, grammar and reading items, plus one speaking item.

3. **Self-study hours must be stated.** Against a benchmark of 90 to 100 hours for A1, the full course at 56 class hours needs roughly 3 hours of Kata-Kata study per unit, and the fast course roughly 9 to 10 per chapter. These are planning figures. The benchmarks are for Japanese and English, and Malay has no new script to learn, so the real figure may be lower. Each chapter pack should print its expected self-study time.

4. **Assessment rhythm is in line.** A Japan Foundation [curriculum example for Irodori](https://jfmo.org.ph/wp-content/uploads/2025/04/A1-Curriculum-.pdf) uses a Can-do check and mini test every lesson and a summative test every six lessons. This charter has a self-check and test every chapter and a review after chapters 3, 6 and 9\.

5. **Two courses has a precedent.** Marugoto separates communicative activities (Katsudoo) from language study (Rikai), which parallels the fast and full courses. This comes from a search summary; the Marugoto site itself was not opened.

Still to do:

* KSBM: a 2018 [Bernama report](https://www.malaymail.com/news/malaysia/2018/10/23/education-ministry-wants-educational-institutions-to-adopt-kbsm-next-year-s/1685910) describes six levels equivalent to the CEFR. The framework document itself has not been read, so the A1 and A2 labels on the Malay chapters are not yet checked against it.

* Published Malay courses for foreign learners: none reviewed yet. Sam to name the ones he trusts or already uses.

* English Profile and the Japanese sequences for section 7\.

## **4\. Malay Stage 1 (A1): chapters 1 to 9**

Stage 1 is Sam's nine chapters, unchanged in order and scope. Kata-Kata already follows them exactly (427 chapter cards). The can-do goals below are drafts for Sam to edit.

**Chapter order confirmed (11 Nov 2026).** Sam confirmed that Kata-Kata's order governs: adjectives (5), comparatives and superlatives (6), then directions and locations (7). Cikgu Sensai's units, which currently place location and directions before adjectives, are reordered to match.

| Ch | Topic and grammar (Sam's order) | Can-do goals (draft) | Core patterns | Where Japanese helps or interferes |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Greetings, with etymology | Greet by time of day, use titles, ask after someone, take leave | Selamat \_\_\_, (title) \_\_\_. / Apa khabar? Khabar baik. | Titles work like さん, but come before the name |
| 2 | Pronouns, pe- and \-an, self-introduction, Siapa / Apa / Di mana, \-kah | Introduce yourself (name, origin, work, home, hobby) and ask the same of others | Nama saya \_\_\_. / Saya orang \_\_\_. Asal saya dari \_\_\_. / Siapa nama (title)? | No は or です: two nouns side by side make a sentence |
| 3 | Numbers to 1 juta, money, ke- ordinals, fractions, decimals, percent, Berapa, umur, ke-an | Ask and pay a price, check change, give age and phone number, say which one in a sequence | Berapa harga \_\_\_? / Harganya \_\_\_ ringgit. / Umur saya \_\_\_ tahun. | Number system is regular and base-ten, as in Japanese |
| 4 | Time, frequency, tense markers | Tell the time and day, describe a routine, say what is done, not yet done or under way | Sekarang pukul \_\_\_. / Saya \_\_\_ setiap \_\_\_. / Saya sedang, sudah, belum, akan \_\_\_. | Verbs do not conjugate: a separate word carries the tense |
| 5 | Adjectives, Bagaimana / Macam mana | Describe food, objects and feelings, and choose between items | (noun) ini (adjective). / Bagaimana rasa \_\_\_? / Saya mahu \_\_\_ yang \_\_\_. | Adjective follows the noun, the reverse of Japanese |
| 6 | Comparatives and superlatives (lebih, sangat, paling, ter-) | Compare two options, say two things are equal, pick the best of three | A lebih \_\_\_ daripada B. / A sama \_\_\_ dengan B. / paling ***, ter-*** | より and 一番 map cleanly to daripada and paling |
| 7 | Directions and locations | Ask where something is, follow and give a route, name transport | \_\_\_ di (position) \_\_\_. / Saya mahu pergi ke \_\_\_. / Jalan terus, kemudian belok \_\_\_. | di, ke, dari map to で・に, へ, から, but come before the noun |
| 8 | Penjodoh bilangan | Order and count things with the right classifier | Saya mahu (number) (counter) (noun). / se-(counter) (noun) / Berapa (counter) \_\_\_? | Same idea as Japanese counters (匹, 個, 枚), in a different word order |
| 9 | Passive di- | Read signs and notices, say what was done and by whom | \_\_\_ dibuat oleh \_\_\_. / \_\_\_ sudah, belum di-(verb). / Dilarang \_\_\_. | Malay passive is neutral and very common, unlike 受身 |

### **How the tools line up per chapter**

| Ch | Kata-Kata cards | Kata-Kata scenes | Cikgu Sensai units today | To write for Cikgu Sensai |
| :---- | :---- | :---- | :---- | :---- |
| 1 | 38 | None | Greetings | Titles, leave-taking, etymology notes |
| 2 | 63 | Pagi di pejabat, Sembang di pantri | Introductions | Full pronoun set, pe- and \-an, \-kah questions |
| 3 | 56 | Pasar pagi, Ke bank dan pejabat pos | Counting and quantities, Order and floors, Ringgit and sen, plus the Beli buah di pasar pack | Large numbers, fractions and percent, age, ke-an |
| 4 | 56 | Bangun pagi, Satu hari Encik Tanaka, Hujan petang, Cuti ke pantai | Clock time, Dates and days, Frequency and routines | Tense and aspect markers |
| 5 | 58 | Di klinik, Gambar bayi, Masak nasi goreng, Lepak di kedai mamak | Taste and colour, Size and shape | Feelings, Bagaimana, yang |
| 6 | 34 | Main badminton | Comparisons and superlatives | sama and se-, sangat, terlalu, ter- |
| 7 | 49 | Lintas jalan, Di ruang tamu, Telefon baru | Asking where, Directions and orientation | Transport, distance and duration |
| 8 | 43 | Beli baju | None | The whole chapter |
| 9 | 30 | Rumah terbuka (general open house), Simpulan bahasa harian | None | The whole chapter |

Cikgu Sensai currently runs these units in a different order (location and directions before adjectives) and labels units 10 to 13 as A2 by position alone. Under this charter all nine chapters are A1, in Sam's order.

## **5\. Malay roadmap beyond chapter 9**

Stage 2 is nine chapters (10 to 18\) that take learners to A2 and into Hanashishou; Sam agreed the content and order on 11 Nov 2026\. Stage 3 is outlined at B1.

The logic of Stage 2: Stage 1 deliberately holds back ber- and me-. Learners finish it able to handle transactions with root words, fixed phrases and the di- passive. Stage 2 opens the verb system in a controlled order, then adds the connecting words needed to explain, give reasons and handle problems. Those are the skills Hanashishou's band 1 scenes assume.

### **Stage 2 (A2): chapters 10 to 18**

| Ch | Grammar focus | Can-do goals (draft) | Example forms | Linked Hanashishou pack |
| :---- | :---- | :---- | :---- | :---- |
| 10 | ber- verbs (states, habits, having) | Retell your day and your background in full sentences | bekerja, berjalan, bercakap, berumur, berkahwin | Daily life |
| 11 | me- verbs I: the active form and its sound changes | Say who does what; switch between active and the di- passive from chapter 9 | membeli and dibeli, membaca, menulis, memasak, mengambil | Office |
| 12 | me- verbs II: \-kan and \-i; requests with tolong | Ask someone to do something for you; report a repair or delivery | Tolong tutupkan pintu. menghantar, membaiki | Home and condo |
| 13 | Negation and modals as a system | Give and understand rules, permission, need and advice | tidak, bukan, belum, jangan; boleh, mesti, perlu, patut | Health |
| 14 | Linking words: reason, condition, purpose, contrast, time | Explain why, set a condition, tell a short sequence of events | kerana, jadi, kalau, supaya, walaupun, sebelum, selepas | Social |
| 15 | yang clauses and the full question-word set | Describe a person or lost item precisely; ask why and when | orang yang \_\_\_, kenapa, bila, yang mana | Daily life |
| 16 | ter- for accidents and unplanned states | Report a mishap, apologise, make a complaint politely | terjatuh, tertinggal, terlupa, tertidur | Home and condo, Health |
| 17 | Register and particles: spoken short forms, lah, kan, pun; inviting and declining | Follow natural spoken Malay; invite, accept and refuse without offence | tak, nak, dah, kat; Jom\! Jemput datang. | Social, Office |
| 18 | Stage review and A2 check | Pass the A2 exit tasks (the A2 stage test: pass 48 of 80, with at least 10 of 20 in each section; Sam's decision, 13 Nov 2026, carried over from the A1 test; a course rule, not a validated CEFR cut score); set up Hanashishou at band 1 | Review of chapters 10 to 17 | All five |

Notes on the order:

* ber- comes before me- because it has no nasal sound changes and covers the routine verbs learners already half-know. Its only spelling variants are be- before a root starting with r or whose first syllable ends in -er (berehat, bekerja) and bel- in belajar, the one exception (Sam, 13 Nov 2026).

* Chapter 11 pairs each me- verb with the di- form learnt in chapter 9, so the new prefix attaches to known words.

* Chapter 16 reuses ter-, first met as a superlative in chapter 6, and contrasts the two meanings.

* Chapter 17 collects the spoken forms that have been flagged since chapter 1 and teaches them as a system.

What changes in each tool for Stage 2:

* **Kata-Kata** gains chapter packs c10 to c18. Its affix guard becomes stage-aware: ber- is allowed from chapter 10, me- from chapter 11\.

* **Cikgu Sensai** gains nine chapter suites at A2. Its existing A2 pack (Ambil bungkusan di lobi) moves into chapter 12\.

* **Hanashishou** tags each Malay scene with the earliest chapter it suits. The current Jambatan bridge is then rebuilt from those tags.

### **Stage 3 (B1): outline only**

Stage 3 inherits the B1 to B2 scene library from the English course (section 7\) and adds the Malay grammar layer: abstract nouns (pe-...-an, per-...-an, ke-...-an), memper-, reduplication, the passive with saya and awak as agent, reported speech with bahawa, formal and informal writing (email against WhatsApp), longer listening, and common peribahasa. It pairs with Hanashishou band 2\. It should be detailed only after Stage 2 has been piloted.

## **6\. Cikgu Sensai as a textbook: the chapter suite**

Every chapter in Cikgu Sensai ships the same eleven components, taught in four 45-minute blocks. Today each unit has two of them: a learner pack and a teaching plan.

| \# | Component | What it contains | Block | Exists today |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Chapter opener | Can-do goals, the scene, a recall task from the previous chapter | A | Partly (recall line in the plan) |
| 2 | Vocabulary focus | The chapter's ledger words by group, with Japanese and English meanings; matches the Kata-Kata set | A | Five words per unit |
| 3 | Pattern and grammar focus | Each pattern in a box with a slot, short question-and-answer example sentences, then a short explanation in the explainer language | A | Notes only |
| 4 | Drills | The ladder: repeat, substitute, transform, question and answer | B | No |
| 5 | Model conversation | A dialogue using only taught language, then a gapped version | B | Yes |
| 6 | Listening focus | An Encik Tanaka script at chapter level, with a task before, during and after listening | C | No |
| 7 | Reading and writing | A short real-world text (sign, message, form) and a guided writing task | C | Higher-level packs only |
| 8 | Task | An independent exchange with an outcome to check, then a change of plan | C | Yes |
| 9 | Culture and word-origin note | Sam's etymology and usage notes for the chapter | Any | No |
| 10 | Chapter test and self-check | Ten minutes, low-stakes: listening, grammar and reading items, plus one speaking item; "I can" checklist | D | No |
| 11 | Teaching plan and answer key | Timings per block, what to listen for, answers, homework in Kata-Kata and Hanashishou | All | Yes |

### **The four blocks**

1. **Block A, Words and patterns.** Recall (5 min), Tanya Cikgu questions (5), vocabulary check (10), pattern focus (20), first substitutions (5).

2. **Block B, Drills and conversation.** Recall (5), drill ladder (20), model conversation and gapped version (15), pair rehearsal (5).

3. **Block C, Listening and task.** Recall (5), listening focus (15), reading or writing (10), independent task with change of plan (15).

4. **Block D, Review and test.** Mixed review with earlier chapters (15), chapter test (10), self-check and feedback (10), preview of the next Kata-Kata set (10).

5. **Block E, Scene.** Recall (5), a Kata-Kata Dunia scene as listening (10), role-play of the scene (15), free variation with a change of plan (10), link to the matching Hanashishou scene where one exists (5).

### **Stage 1 plan (agreed 11 Nov 2026\)**

Stage 1 is taught as 13 units from the 9 chapters, five blocks per unit, plus review and skills blocks: 76 blocks, or 57 class hours. Nothing new is added to the syllabus; the heavy chapters are split and each unit gets more time in use. With the self-study hours below, a learner reaches the 90 to 100 hour A1 benchmark.

**Unit count confirmed (11 Nov 2026).** Sam chose 13 units. Chapter 5 is not split.

| Unit | Chapter and content | Blocks | Notes |
| :---- | :---- | :---- | :---- |
| 1 | Ch 1 Greetings, titles, leave-taking | 5 | Plus a pronunciation and spelling block (Malay orthography is regular; one block suffices) |
| 2A | Ch 2 Pronouns, name, origin, Siapa / Apa / Di mana | 5 |  |
| 2B | Ch 2 Work, home, family, hobby; pe- and \-an; \-kah | 5 | Writing block: a self-introduction form |
| 3A | Ch 3 Numbers to 1 juta, Berapa, age, phone number | 5 | Review block after this unit |
| 3B | Ch 3 Money, prices, paying, change | 5 |  |
| 3C | Ch 3 ke- ordinals, fractions, decimals, percent, ke-an measures | 5 | Writing block: a price list or order |
| 4A | Ch 4 Clock time, days, dates, frequency | 5 |  |
| 4B | Ch 4 Tense and aspect markers, daily routine | 5 | Review block after this unit |
| 5 | Ch 5 Adjectives, Bagaimana, yang | 5 | Writing block: a short description |
| 6 | Ch 6 Comparatives and superlatives | 5 | Review block after this unit |
| 7 | Ch 7 Locations and directions | 5 | Writing block: directions by message |
| 8 | Ch 8 Penjodoh bilangan | 5 |  |
| 9 | Ch 9 Passive di-, signs and notices | 5 | Stage review and A1 test after this unit |

| Block type | Count | Hours |
| :---- | :---- | :---- |
| Unit blocks A to E | 65 | 48.75 |
| Review blocks (after units 3A, 4B, 6\) and the stage review; the A1 stage test adds 2 blocks (1.5 hours: written papers, then speaking) | 4 | 3 |
| Skills blocks (pronunciation; writing in units 2B, 3C, 5, 7\) | 5 | 3.75 |
| Total | 76 | 57 (76 blocks of 45 minutes, with the A1 test) |

The five strands each block type serves: new language in use (A, B), listening and reading input (C, E), fluency and recycling (E, review), explicit language focus (A, skills), and spaced retrieval (every block's recall, D, review).

Block E and the extensive strand draw on content that already exists in Kata-Kata: its 19 Dunia scenes map to chapters 2 to 9, and the Encik Tanaka listening materials supply graded input. Chapter 1 has no Dunia scene yet; one is needed.

The full course is therefore a two-term programme at two blocks a week. The fast course is unchanged: one session per chapter, nine sessions, with the rest in self-study.

Each chapter pack states the self-study time expected in Kata-Kata: roughly 3 hours a unit on the full course (about 40 hours across Stage 1\) and 9 to 10 hours a chapter on the fast course, as planning figures.

Listening needs a decision on audio, since Cikgu Sensai has none today: teacher-read scripts, device text-to-speech, or recordings (section 11).

Print and download options stay as they are (merged PDF, ZIP, editable Word; explainer in Japanese, Malay or English; teacher key included, separate or omitted). Each component becomes a selectable exercise type in the library.

### **Chapter menu and flexible delivery**

The teacher opens a chapter and sees everything available for it, then chooses what to use. This is a requirement, not an option.

* **Chapter page.** Lists every component for the chapter with its time estimate, level and type, plus the linked Kata-Kata set and Hanashishou scenes. Each item can be ticked into a print pack. A chapter that is split into units shows its units in order, each with its own five blocks.

* **Stand-alone components.** Every component works on its own. None assumes that another was taught in the same sitting.

* **Two delivery paths.** The fast course teaches a chapter in one 45-minute session from a single summary chapter pack: can-do goals, core words, key patterns with examples, one model conversation, one task and a self-check. The student then self-studies the rest in Kata-Kata and Hanashishou, and the pack ends with a guide naming the exact sets and scenes to do. The full course teaches the expanded lessons and drills, all eleven components over four or six blocks, with the same two apps used alongside for self-study. Both courses draw on the same chapter content, so a class can switch between them chapter by chapter.

* **Topic-to-topic movement.** Previous and next chapter buttons follow the teaching order. A chapter also lists which earlier chapters it depends on, so a teacher can skip or revisit.

### **Component tagging and extraction (requirement, 11 Nov 2026\)**

Every component is an independent, tagged item that a teacher can pull out on its own, without the rest of its chapter. A teacher following a different syllabus can take only the listening task or only the composition drill from a chapter and use it alongside their own course.

Each component carries these tags:

| Tag | Values | Example |
| :---- | :---- | :---- |
| Language | Malay, English, Japanese | Malay |
| Level | A1, A2, B1, B2, C1 | A1 |
| Chapter and unit | From section 4 or 5; blank for stand-alone packs | ms-c03b |
| Component type | Opener, vocabulary, pattern and grammar, drill, model conversation, listening, reading and writing, task, culture note, test, teaching plan | Listening |
| Sub-type | For drills: repeat, substitute, transform, question and answer, free. For writing: form, message, note, composition. For tests: words, grammar, listening, reading, speaking | Substitute |
| Skill | Listening, speaking, reading, writing, vocabulary, grammar | Listening |
| Genre | From the genre table in section 7 | Shopping and money |
| Grammar points | From the language layer | ke- ordinals |
| Time | Minutes in class | 15 |
| Prerequisites | Chapters or grammar points assumed; blank if none | ms-c03a |
| Course path | Full, fast, both | Both |
| External textbook link | For Japanese and other supplementary use: the lesson it fits | Minna no Nihongo I, Lesson 5 |
| Review status | Draft, reviewed, approved | Draft |

What the library must let a teacher do:

* Filter by any tag or combination, for example every Malay listening task at A1, or every substitution drill on comparatives.

* Select single components across chapters and print them as one pack, with or without the teacher key.

* See each component's prerequisites, so a drill pulled out of chapter 6 states that it assumes chapters 3 and 5\.

* Export a component as a stand-alone sheet with its own header (language, level, chapter, type, time), so it makes sense away from its chapter.

* Add a prerequisite check. Selecting the prerequisites tag on any component offers to add a short revision pack in front of it: the chapter test or self-check for each prerequisite chapter, cut down to the grammar points and words that component actually assumes. For example, a comparatives drill from chapter 6 generates a ten-minute check on numbers (chapter 3\) and adjectives (chapter 5), so students revise before the teacher starts the main content. The check prints as the first sheet of the pack, with its own key, and can be given as homework before class or run in the first ten minutes.

The chapter page (above) and this component view are two routes to the same items: by chapter when teaching the course, by tag when supplementing another one.

For the prerequisite check to work, every test item must itself be tagged with the grammar points and word IDs it tests, so a reduced check can be assembled automatically from the prerequisite chapters' tests.

### **Topic genres**

Every chapter, scene and pack carries one genre tag, so content can be browsed by topic as well as by chapter. The three tools use different labels today. Proposed common set:

| Genre | Covers | Existing labels it absorbs |
| :---- | :---- | :---- |
| Social life | Greetings, introductions, invitations, festivals | Social encounters; Social; perayaan |
| Shopping and money | Prices, markets, banks, ordering food | Transactions; Dining; pasar, bank-pos, makan-luar, pakaian |
| Getting around | Location, directions, transport | Wayfinding; jalan |
| Time and routines | Clock, dates, frequency, daily habits | Schedules; Daily routines; kata-kerja, cuaca, cuti |
| Describing and choosing | Adjectives, comparing, opinions | Description; Choices and opinions |
| Home | Housing, condo life, cooking | Housing; Home and condo; rumah, dapur, telefon |
| Health | Body, clinic, pharmacy | Health; badan |
| Work and study | Office, meetings, campus | Work; Study; Office; pejabat |

### **Content minimums (11 Nov 2026\)**

Each full-course unit must reach these amounts. The figures are working targets set for the step 4 pilot and will be adjusted after Sam has taught it. A component below its minimum is not done, and the builder's report says so.

* **Vocabulary focus:** every ledger word placed in the unit (typically 20 to 40), grouped by theme, each with its Japanese and English meaning and one example sentence; spoken forms marked.  
* **Pattern and grammar focus:** 3 to 5 patterns; each with a pattern box, 4 to 6 question-and-answer example sentences, a short explanation in Japanese and English, and a note on where Japanese helps or misleads.  
* **Drills:** all six section 14 types; at least 6 items each for types 1 to 5 (30 or more items in all) and at least 3 short dialogues for type 6, plus the cumulative question-word drill.  
* **Model conversation:** 10 to 16 turns, a gapped version, and a variant with changed facts.  
* **Listening:** an Encik Tanaka script of 120 to 250 words, with a before, during and after task and at least 6 comprehension items.  
* **Reading and writing:** one real-world text (sign, menu, message or form) with at least 5 questions, and one guided writing task with a model answer.  
* **Task:** role cards A and B, a change of plan, and the success criteria the teacher checks.  
* **Culture and word-origin note:** 150 to 300 words, drawing on Sam's etymology notes.  
* **Chapter test:** 15 to 20 items across listening, vocabulary and grammar, and reading, plus one speaking task; every item tagged; separate answer key.  
* **Teaching plan:** timings per block, teacher prompts, expected learner answers, and the Kata-Kata set to assign before and after class.  
* **Fast-course summary pack:** 2 to 4 pages per chapter: can-do goals, 15 to 20 core words, key patterns with 2 examples each, one model conversation, one task, a self-check and the self-study guide.

## **7\. English and Japanese**

English and Japanese copy the Malay design, not the Malay grammar: the same chapter suite, the same four blocks, the same ten rules and the same ladder of everyday functions, with each language's own grammar sequence underneath.

### **Priority and purpose per language (Sam, 11 Nov 2026\)**

| Priority | Language | Learners | Purpose of Cikgu Sensai | Course form |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Malay | Japanese adults from zero | The complete course: syllabus, textbook, lesson plans | Full and fast courses, Stage 1 then Stage 2 |
| 2 | English | Lower-intermediate to upper-intermediate adults (B1 to B2), aiming at business English at intermediate range | The complete course for that band; no A1 or A2 English course | Themed chapters at B1 and B2, built on Hanashishou's bands 2 and 3 |
| 3 | Japanese | Learners taught by other teachers, from whatever textbook those teachers use | Complementary and supplementary material only: stand-alone packs a teacher can drop into an existing course | No chapter sequence of its own; packs tagged by CEFR level and the Minna no Nihongo or Irodori lesson they fit |

What this changes in the rest of this section: the A1 function ladder below is the A1 scene library under the two-layer model. Its English and Japanese grammar columns are first proposals to be set from each language's own authorities. The English course proper starts at B1; English A1 packs are localisations of the Malay scenes. Japanese packs are tagged to external textbooks, not to chapters of this charter.

### **The two-layer model (agreed 11 Nov 2026\)**

Content is written once per CEFR level as a language-neutral scene, then localised into each language with that language's own grammar. Sam wants a holistic system: whichever language is being worked on, the other two gain matching materials.

| Layer | Holds | Shared across languages | Owner |
| :---- | :---- | :---- | :---- |
| Scene library (per CEFR level) | Scene, can-do goal, task and change of plan, listening script outline, reading text type, test item shapes, genre tag | Yes, written once | This charter |
| Language layer (per language) | Grammar sequence, word list from that language's ledger, pattern cards, first-language notes, which scenes attach to which chapter, hour budget | No | Each language's syllabus |

Rules:

* A scene is pinned to a situation and a can-do goal, never to a grammar point. The same mamak-order scene is taught with di- in Malay and with ます and てください in Japanese.

* A language's grammar order is set by that language's own authorities (section 4 for Malay; Minna no Nihongo and Irodori for Japanese; English Profile for English), not by another language's chapters.

* Localising is cheaper than authoring but not free: every localised pack carries its own word list, pattern cards and native-speaker review, and Japanese A1 adds kana and a larger hour budget.

* Priority order stays Malay, English, Japanese. The model makes the second and third cheaper; it does not reorder them.

How the layers run in both directions:

* **A1 scene library** \= the Malay Stage 1 functions (nine chapters, 13 units). Localised into English A1 and Japanese A1 packs. For Japanese these are supplementary packs tagged to Minna no Nihongo and Irodori lessons, not a sequenced course.

* **A2 scene library** \= Malay Stage 2 (section 5), localised the same way.

* **B1 to B2 scene library** \= the English business course. When Malay reaches Stage 3 it inherits this library rather than starting from scratch.

### **B1 to B2 scene library: organisation**

Organised by business function, mixed with everyday and social use so the course is not office-only. Each function gets scenes at B1 and at B2. Proposed set, for Sam to edit:

| Strand | Business functions | Everyday and social scenes mixed in |
| :---- | :---- | :---- |
| Talking with people | Small talk at work, introductions at events, networking | Neighbours, condo committee, parents at school, weekend plans |
| Meetings | Agenda, giving an update, disagreeing politely, summarising decisions | Family or group planning, a committee meeting at a club |
| Written messages | Email requests, follow-ups, declining, apologising, WhatsApp at work | Messages to a landlord, a clinic, a school, a contractor |
| Presenting and explaining | Short presentation, explaining a process, handling questions | Explaining Malaysian or Japanese customs to a visitor, giving a toast |
| Negotiating and solving problems | Deadlines, prices with a supplier, scope, complaints to a vendor | Rental repairs, a wrong bill, a return at a shop, a travel change |
| Telephone and online | Calls, video meetings, voicemail | Booking, hotlines, deliveries, service centres |
| Numbers and reports | Figures, trends, comparisons, a one-page summary | Household budget, a quote from a contractor, a medical bill |

The English course at B1 to B2 and Malay Stage 3 both draw from this table. Hanashishou's Office, Social, Health and Home and condo packs supply the first scenes.

### **What carries over and what does not**

| Carries over unchanged | Set separately for each language |
| :---- | :---- |
| The eleven-component chapter suite and the 45-minute blocks | The grammar sequence |
| The ten teaching rules | The word list and its level grading |
| CEFR as the level scale | Register order (the standard-first rule is Malay-only) |
| Scenes set in Malaysia | Notes on what the learner's first language helps or hinders |
| ID scheme and review status flags | Controlled-form rules (the affix rule is Malay-only) |

### **The shared function ladder at A1**

This table is the A1 scene library. The function column is shared; each grammar column belongs to that language's own layer and is a first proposal.

| Ch | Function | Malay grammar | English grammar (proposed) | Japanese grammar (proposed) |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Greeting and leave-taking | Selamat, titles | Greetings, be | あいさつ, です |
| 2 | Introducing yourself | Pronouns, pe-, \-an | Pronouns, possessives, Wh- questions | は, の, か |
| 3 | Numbers and money | Numbers, ke-, Berapa | Numbers, How much / many | 数字, いくら |
| 4 | Time and routine | Tense markers | Present simple, adverbs of frequency | 時間, ます form |
| 5 | Describing | Adjectives, yang | Adjectives, a / an / the | い and な adjectives |
| 6 | Comparing | lebih, paling, ter- | Comparatives and superlatives | より, 一番 |
| 7 | Places and directions | di, ke, dari | Prepositions of place, imperatives | に, で, へ, あります / います |
| 8 | Counting and ordering things | Penjodoh bilangan | Countable and uncountable, some / any | 助数詞 |
| 9 | Saying what was done; notices | Passive di- | Past simple, signs and notices | ました, てください |

The English and Japanese columns are first proposals. They need checking against English Profile and against the Minna no Nihongo and Irodori sequences before any content is written.

### **Higher-level English (B1 to C1)**

English is the second priority and is taught from B1 to B2 only, for working adults who need business English at intermediate range. It uses the same eleven-component suite, with three components changing character. Hanashishou's bands 2 and 3 and its Office, Social and Health packs supply the content, and its existing B1 to C1 Cikgu Sensai scenario families are the starting point.

* **Pattern focus becomes the level ladder.** One intent is shown at four levels (basic request, softer modal, indirect request with reason, conditional softener), as in Hanashishou's Level Ladder cards. Learners practise moving a sentence up one step.

* **Vocabulary focus becomes collocation and nuance.** Synonyms, opposites and common word partners, drawn from Hanashishou's vocabulary files.

* **The task becomes a negotiated role-play.** Private role cards, then a change of plan. Cikgu Sensai's B1 to C1 packs already do this.

| CEFR | Hanashishou band | Cikgu Sensai chapters | Themes |
| :---- | :---- | :---- | :---- |
| A2 | 1 Foundation | Transactional exchanges with one complication | Daily life, Home and condo |
| B1 | 2 Developing | Explaining, arranging, softening requests | Health, Office |
| B2 | 3 Confident | Negotiating, giving reasons, handling disagreement | Office, Social |
| C1 | 4 Advanced | Weighing evidence, hedging, formal register | Office, Social |

Hanashishou's spec calls its CEFR labels approximate. Under this charter the mapping above becomes the working rule, and the Evaluator shows the CEFR label beside the band name.

## **8\. Shared standards**

Four layers govern content, each overriding the one below it: this charter, the syllabus spine, the vocabulary ledger, then each tool's content files.

### **Source of truth**

* **Charter (this document).** Approach, roles, stages and rules. Changed only by Sam.

* **Syllabus spine.** One record per chapter: can-do goals, pattern IDs, grammar points, word IDs, items to recycle, linked scenes. Proposed home: a Syllabus tab in the existing Malay ledger sheet, exported as a JSON file committed to all three repositories.

* **Vocabulary ledger.** The Google Sheet Sam named on 6 Nov 2026 as the reference for Kata-Kata and Hanashishou (982 terms, IDs L-0001 onward, with a Journal tab). Cikgu Sensai joins it.

* **Change order.** A change is made in the spine or ledger first, logged in the Journal, then pushed to each tool. No tool introduces a word or pattern on its own.

### **IDs**

Keep the IDs Kata-Kata already uses, and extend them.

| Thing | Format | Example |
| :---- | :---- | :---- |
| Chapter | language-chapter | ms-c03 |
| Lesson block | chapter-block | ms-c03-b2 |
| Word card | chapter-number (existing) | ms-c03-001 |
| Sentence pattern | chapter-f-number (existing) | ms-c03-f01 |
| Ledger term | L-number (existing) | L-0001 |
| Textbook component | chapter-component | ms-c03-listening |

### **Levels**

* CEFR labels are assigned by the can-do goals a chapter meets, not by its position in a list.

* Malay: chapters 1 to 9 are A1, 10 to 18 are A2, Stage 3 is B1.

* Hanashishou bands map to CEFR as in section 7\.

### **Malay form rules**

* **Affixes.** Stage 1 uses root words, fixed chunks and the affixes Sam teaches in chapters 2, 3, 6 and 9 (pe-, \-an, \-kah, ke-, ke-an, se-, ter-, di-). ber- and me- are not used productively before chapters 10 and 11\. Fixed expressions tagged as chunks (for example Selamat berkenalan) and look-alike roots on the allow-list (for example besar, merah) are permitted. Kata-Kata's affix guard enforces this at build time. Cikgu Sensai and Hanashishou's Malay content adopt the same check.

* **Register.** Standard forms are taught first (mahu, tidak, sudah). Colloquial forms (nak, tak, dah) are shown beside them from chapter 1, marked "spoken". A dialogue may use a spoken form only after its standard form has been taught. Chapter 17 teaches the spoken system as a whole.

* **Malaysian standard, never Indonesian.** All Malay follows Malaysian usage as recorded by Dewan Bahasa dan Pustaka in Kamus Dewan. Indonesian forms are errors even where they look close: nombor not nomor, bas not bis, epal not apel, selepas not setelah, beza not beda, kereta not mobil, tandas not toilet or WC, tiket not karcis, kedai not toko, wang or duit not uang. When a word's Malaysian status is unsure, flag it for Sam and the Kamus Dewan check; do not guess. Greetings used within one religion (Assalamualaikum, Waalaikumsalam) are not taught anywhere: not as vocabulary, in culture notes, drills or pronunciation lists (Sam, 11 Nov 2026). Ask Sam before adding any other faith-specific expression.

### **Quality and constraints**

* Every item carries a review status. All Japanese text in all three tools is an AI draft awaiting a native check. All ledger rows are currently Draft.

* Malay terms are checked against Kamus Dewan Edisi Keempat, as the ledger already does.

* All three tools stay free, offline-capable and account-free, and store no learner records on a server.

* Explainer text is available in Japanese, English and Malay.

## **9\. Audit: where the three repositories stand**

Kata-Kata and Hanashishou already share a scheduler, a card format and a vocabulary ledger. Cikgu Sensai shares none of these yet. Read from the three GitHub repositories on 11 Nov 2026\.

|  | Kata-Kata | Cikgu Sensai | Hanashishou |
| :---- | :---- | :---- | :---- |
| Built with | Claude Code | ChatGPT | Claude Code |
| Version | 0.10.0, release candidate | No version number | Has its own 1.0 checklist |
| Malay structure | 9 chapters matching Sam's order, 19 Dunia scenes, 5 Jambatan bridge scenes | 13 course units, plus 5 scenario families (A1 to C1) | 5 themed packs plus a tutorial, 4 bands |
| Malay size | 805 cards (427 chapter, 249 scene, 129 bridge) | 5 words per course unit | 381 vocabulary entries |
| Other languages | Interface only (Japanese, English, Malay) | English and Japanese scenario families, A1 to C1 | English is the main target; Japanese and Malay targets drafted |
| Level scale | Chapters | CEFR labels, assigned by position | 4 bands, CEFR approximate |
| In the shared ledger | Yes (784 terms) | No | Yes (381 terms; 183 shared with Kata-Kata) |
| Affix check | Automatic, at build | None | None |
| Lesson design | Daily session: reviews, new words, a frame drill, a game | Learner pack and 45-minute teaching plan per unit; conversation, grammar and writing packs | Branching scenes, minigames, notepad, Evaluator |
| Class link | Sedia Kelas prep, Tanya Cikgu export, Teacher Desk agenda | Print packs | Results screen designed for later classroom export |

Findings that drive the plan:

* Cikgu Sensai has no units for chapters 8 and 9, and lacks pe- and \-an, \-kah, tense markers, ke-an, fractions and percent, and ter-.

* Cikgu Sensai's dialogues use spoken forms (nak, tak) from the first units, which conflicts with the Malay register rule.

* Hanashishou starts at about A2, so there is no speaking practice tool for A1. The Jambatan bridge and Stage 2 close that gap.

* Every ledger row is still marked Draft, and no Japanese text in any tool has had a native check.

* Cikgu Sensai already has a sound lesson shape (recall, model, guided practice, independent task, change of plan). The suite in section 6 extends it; it does not replace it.

## **10\. Build roadmap**

The work runs in six phases, each ending in something Sam can test in class before the next begins.

| Phase | Outcome | Cikgu Sensai | Kata-Kata | Hanashishou |
| :---- | :---- | :---- | :---- | :---- |
| 0\. Sign-off | Charter v1.0 agreed | None | None | None |
| 1\. Spine | Syllabus spine for chapters 1 to 9 exists and all three read it | Words added to the ledger | Spine file added; no content change | Spine file added |
| 2\. Restructure and pilot | 13 units regrouped into 9 chapters; full suite built for chapters 1 and 2 | Regroup, add form checks to the build, write the two pilot suites | Sedia Kelas sets matched to lesson blocks | None |
| 3\. Stage 1 complete | Suites for chapters 3 to 9, three review lessons, the A1 stage test | Write, including new chapters 8 and 9 | Teacher Desk agenda cites lesson block IDs | CEFR label shown in the Evaluator |
| 4\. Stage 2 | Chapters 10 to 18 in all three tools | Nine A2 suites | Packs c10 to c18; stage-aware affix guard | Malay scenes tagged by chapter; bridge rebuilt |
| 5\. English and Japanese | A1 function ladder for both; upper English B1 to C1 on the same suite | Write | None | English packs linked to Cikgu Sensai chapters |
| 6\. Review and Stage 3 | Native-speaker checks done; Stage 3 detailed from pilot results | Fixes | Fixes | Fixes |

The pilot in phase 2 matters most. Chapters 1 and 2 are built in full, taught once, and the suite template is frozen only after Sam has used it with students. Everything in phases 3 to 5 then copies that template.

Hand-off: the whole charter goes to ChatGPT, which follows the brief in section 12\. Claude Code receives sections 1 to 8 and its own columns of the table above.

## **11\. Open decisions for Sam**

All seven points are decided. Two details remain open under the Japanese item, and the draft can-do goals and scene tables still need Sam's edit

* ☐ **Home of the spine.** Decided 11 Nov 2026: for now, chapter data is read from the Kata-Kata chapter files and the ledger snapshot.

* ☐ **Stage 2 order.** Agreed 11 Nov 2026: chapters 10 to 18 as in section 5, ber- before me-.

* ☐ **Blocks per chapter.** Decided 11 Nov 2026: 13 units of five blocks, with review and skills blocks, per the Stage 1 plan in section 6; plus the one-session fast course.

* ☐ **Who the Japanese materials are for.** Decided 11 Nov 2026: supplementary packs for learners taught by other teachers from their own textbooks (section 7). Still open: which textbooks those teachers use, and what the explainer language should be.

* ☐ **Listening audio.** Decided 11 Nov 2026: teacher-read scripts, no audio files.

* ☐ **Tests.** Decided 11 Nov 2026: low-stakes only.

* ☐ **Who builds Cikgu Sensai.** Decided 11 Nov 2026: ChatGPT continues, guided by this charter and the brief in section 12\.

Also to confirm: the draft can-do goals in sections 4 and 5, and the English and Japanese grammar columns in section 7\.

## **12\. Brief for ChatGPT: building Cikgu Sensai**

Your job is to turn Cikgu Sensai from a worksheet library into the classroom textbook for this syllabus, Malay first, in the seven steps below. Stop for Sam's approval where marked.

### **Your scope**

* You build Cikgu Sensai only. Do not edit Kata-Kata or Hanashishou.

* Sections 1 to 8 are the rules. Section 9 is the starting point. Sections 4 to 7 hold the content plan.

* Where a section is marked as a proposal or draft, follow it as the working default and label your output provisional.

* If this charter is unclear or contradicts itself, ask Sam. Do not guess.

### **Files to read before changing anything**

| Repository | File | Why |
| :---- | :---- | :---- |
| Cikgu-Sensai | course.py, curriculum.py, build.py | How chapters, packs and PDFs are generated today |
| Cikgu-Sensai | curriculum/malay-course.txt | The 13 Malay units to regroup |
| Cikgu-Sensai | curriculum/foundation.txt, advanced.txt, guided.txt, foundation-guided.txt | The scenario families for all three languages |
| katakata | content/ms/kelas/c01.json to c09.json | The agreed words, sentence patterns, scenario and class-prep set for each chapter |
| katakata | content/ledger/malay-ledger.csv | Snapshot of the shared vocabulary ledger |
| katakata | tools/affix-guard.mjs | The affix check to reproduce |
| Hanashishou | SPEC.md sections 6 and 8, docs/LEARNING-SCIENCE.md | Bands, Level Ladder, vocabulary format |

### **Rules you must not break**

1. **Chapter order.** Malay chapters 1 to 9 follow section 4 exactly. All nine are A1.

2. **Ledger-only vocabulary.** A Malay word appears in a chapter only if the ledger places it in that chapter or an earlier one. Need a new word? List it for Sam; do not add it silently.

3. **Reuse, do not rewrite.** Take each chapter's words and patterns from the Kata-Kata chapter file and keep their IDs.

4. **Affix rule and register rule** as written in section 8\. No productive ber- or me- before chapters 10 and 11\. Standard forms first; spoken forms marked. All Malay is Malaysian standard as in Kamus Dewan, never Indonesian (section 8).

5. **Levels by can-do**, never by position in a list.

6. **Accuracy.** Do not invent Malay, Japanese or English usage. Mark anything you have not checked as unverified. All Japanese stays flagged as a draft until a native speaker reviews it.

7. **Product constraints.** Free, works offline, no accounts, no analytics, no learner records, no runtime services. Keep the current print and download options.

### **Work order**

1. **Restructure.** Regroup the 13 Malay units into the 9 chapters using the table in section 4\. Reorder them to the chapter order in section 4, relabel all as A1, and move the existing Malay scenario packs into their chapters. No new content yet. *Sam reviews.*

2. **Data model.** Give each chapter a record holding its ID, can-do goals, pattern IDs, word IDs, grammar points, recycled items and block plan. Make each of the eleven components in section 6 a selectable exercise type. Use the IDs in section 8\.

3. Each component is also an independently tagged item that a teacher can extract and print on its own, under the tagging scheme in section 6\. Build the tag fields into the data model from the start, and tag every test item with the grammar points and word IDs it tests, so the prerequisite check in section 6 can be assembled automatically. Retrofitting either later is costly.

4. **Build checks.** Add three checks to build.py that fail the build: the affix check, the register check, and the ledger check.

5. **Pilot: chapters 1 and 2\.** Write the full eleven-component suite for both, as units 1, 2A and 2B (five blocks each, plus the pronunciation and writing blocks), the section 14 drill sets, and the fast-course summary pack for each chapter. *Stop. Sam teaches them and gives feedback. The template is frozen only after this.*

6. **Chapters 3 to 9\.** Write the remaining ten units, including chapters 8 and 9 from scratch, the three review blocks, the writing blocks, the stage review and the A1 test.

7. **Stage 2\.** Chapters 10 to 18 at A2, once Sam has confirmed section 5\.

8. **English and Japanese.** English B1 to B2 chapters from the scene library in section 7; English A1 and Japanese A1 packs localised from the Malay scenes; Japanese packs tagged to the textbooks Sam names.

### **Defaults until Sam decides (section 11\)**

* Spine: read chapter data from the Kata-Kata chapter files and the ledger snapshot.

* Blocks: five per unit, 13 units, as in the Stage 1 plan in section 6\.

* Listening: teacher-read scripts printed in the teaching plan. No audio files.

* Tests: low-stakes only.

### **A chapter is done when**

* ☐ All eleven components exist and print without overflow

* ☐ Every word and pattern traces to a ledger or Kata-Kata ID

* ☐ The three build checks pass

* ☐ Each block has one can-do goal, opens with recall and follows the drill ladder

* ☐ The teaching plan names the Kata-Kata set to assign before and after class

* ☐ Japanese text is flagged as awaiting native review

* ☐ Every component carries the full tag set in section 6 and prints as a stand-alone sheet

### **Report back to Sam after each step**

* What changed, by file

* New words or patterns you propose for the ledger

* Anything unverified or provisional

* Questions that block the next step

## **13\. Ledger additions for Stage 1 (approved 11 Nov 2026\)**

Thirty words (counting sahaja / saja as one) should be added to the ledger before the step 4 pilot. They are the gaps the step 1 audit found in learner-facing Stage 1 text, checked against the 982-row ledger snapshot on 11 Nov 2026\. Most are basic function words that every chapter needs and that Kata-Kata does not yet teach as cards either.

Only words from model conversations, vocabulary lists, drills and tasks are included. Words appearing only in Malay instructions are excluded, because Stage 1 instructions move to Japanese or English. English meanings are drafts; Japanese meanings are added in the ledger workflow.

### **A. Add as new cards**

| Malay | Meaning | Proposed chapter | Why there |
| :---- | :---- | :---- | :---- |
| pun | also, too (after the word) | 1 | Saya pun baik is the natural reply to Apa khabar? |
| oh | oh (interjection) | 1 | Reactions, beside ya and tidak |
| ini | this | 2 | Ini kawan saya; Minna also teaches demonstratives in lesson 2 |
| itu | that | 2 | Paired with ini |
| kelas | class | 2 | Learners' own context: school, work, class |
| belas | \-teen (11 to 19\) | 3 | Ledger has only dua belas; the building block is needed |
| puluh | tens | 3 | Ledger has only dua puluh |
| ratus | hundred | 3 | Ledger has only seratus; needed for dua ratus |
| ribu | thousand | 3 | Ledger has only seribu |
| juta | million | 3 | Ledger has only sejuta; chapter goal is numbers to 1 juta |
| nombor | number | 3 | Ledger has only nombor telefon |
| jumlah | total | 3 | Checking a bill |
| cukup | enough | 3 | Paying and change |
| betul | correct | 3 | Confirming a price; ledger has only betul ke? |
| untuk | for | 3 | Beli untuk kawan |
| ialah | is (introduces a definition) | 3 | Standard form; adalah can wait for Stage 2 |
| sahaja / saja | only | 3 | Standard sahaja first, saja marked spoken |
| selepas | after | 3 | Used with ordinals in unit 3C; reused for time in chapter 4 |
| sebelum | before | 3 | Pairs with selepas |
| datang | come | 4 | Routine verbs beside pergi and balik |
| kelakar | funny | 5 | In Sam's own chapter 5 adjective list |
| epal, pisang, mangga | apple, banana, mango | 3 | Market scenes; as nouns only, counted with buah until chapter 8 |
| tempat | place | 7 | Ledger has it only in phrases |
| utara, selatan, timur, barat | north, south, east, west | 7 | Sam teaches compass directions in chapter 7 |
| lintasan | crossing | 7 | Lintasan pejalan kaki; lintas is in the ledger unassigned |

**Malaysian, not Indonesian.** Every word in list A was checked against its Indonesian counterpart on 11 Nov 2026, and the Malaysian form is the one listed: nombor (not nomor), epal (not apel), selepas (not setelah or sesudah), sahaja (not saja as the standard form), kelakar (not lucu), betul (not benar). Lintasan pejalan kaki was confirmed in Malaysian official use by [JPJ reporting](https://paultan.org/2026/04/14/pemandu-yang-abaikan-isyarat-trafik-dan-lintasan-pejalan-kaki-boleh-digantung-lesen-memandu-jpj/) and [PLANMalaysia guidance](https://www.planmalaysia.gov.my/portalassets/main_files/PANDUAN_PELAKSANAAN_PTK_FEB_2025.pdf). The other words were checked from knowledge, not a dictionary: each still goes through the ledger's Kamus Dewan Edisi Keempat check before approval.

### **B. Do not add: derived by a rule the chapter teaches**

keempat (ke- ordinal, chapter 3), seminggu (se- with minggu, chapter 4), ceritanya (-nya, chapter 2). The audit should accept regular derivations from rules already taught, rather than listing every form in the ledger.

### **C. Do not add: rewrite the sentence instead**

These appear once, are above A1, or have a simpler taught alternative. Rewrite when the unit is re-authored.

| Word | Where | Suggested fix |
| :---- | :---- | :---- |
| setandan | Unit 3B | Counters belong in chapter 8; use buah or a price per kilo |
| begitu | Unit 5 (Kalau begitu) | Kalau is chapter 7; rephrase or treat Kalau begitu as a fixed chunk |
| memang, lucu, cerita | Unit 6 | Use kelakar and words already taught |
| sos, rak, tali | Unit 5 | Swap for nouns already in the ledger |
| beritahu | Unit 7 | Stage 2; use tolong with a taught verb |
| campur, bajet | Unit 3B | Rephrase with taught words |
| bual, semak, rakan, lanjut, selama, cara | Task instructions in units 3B and 4B | Instruction text: moves to Japanese or English |

Sam approved list A on 11 Nov 2026, with selepas and sebelum placed at chapter 3\. The 30 terms are now ledger rows, together with three question words Sam asked for (L-0983 to L-1015 in all): adakah (chapter 2), bila (chapter 4\) and kenapa (chapter 5, answered with sebab). Placement changes made at the same time: saya, pagi, tengah hari, petang and malam move to chapter 1; bolehkah is placed at chapter 2; awak stays at chapter 2\. Each row is logged in the Journal and marked pending: Kata-Kata (Claude Code) and the Cikgu Sensai reference snapshot (ChatGPT) still need updating, and the Kamus Dewan check still needs to run.

## **14\. Drill bank**

Every chapter's Drills component (component 4 in section 6\) uses the six drill types below, in this order, following the drill ladder in section 3\. Types 1 to 3 correspond to Minna no Nihongo's Exercise A and B, and type 6 to Exercise C. Each drill is tagged with its sub-type, grammar points and word IDs, so it can be extracted on its own and used in the prerequisite check.

### **Drill types**

* **Pattern table.** One frame with its fillers in columns; learners read every combination aloud. Saya \[sudah / belum / sedang / akan\] \[makan / minum / tidur\].  
* **Substitution.** A cue replaces one slot. Saya sudah makan. (minum) → Saya sudah minum.  
* **Transformation.** A cue changes the form: statement to question (Encik Tanaka orang Jepun. → Adakah Encik Tanaka orang Jepun?), positive to negative (Saya lapar. → Saya tidak lapar. Ini kopi. → Ini bukan kopi.), or tense by a time cue (semalam → sudah, sekarang → sedang, esok → akan).  
* **Question and answer.** Answer the question, then reverse it: hear the answer and ask the question that fits. Pukul tiga petang. → Pukul berapa? Di stesen. → Di mana?  
* **Question-word choice.** Choose the question word for a gap from every one taught so far, so earlier words keep returning.  
* **Short dialogue.** A two-turn exchange with picture or word cues, then one more turn added by the learners (Minna's Exercise C).

### **Tense and aspect markers (chapter 4, then every later chapter)**

* **Timeline drill.** Place sudah, sedang / tengah, belum, akan, masih, baru and pernah on a drawn timeline, then say a sentence for each point.  
* **Time-cue transformation.** Semalam saya beli tiket. Sekarang saya sedang makan. Esok saya akan pergi ke Melaka. The teacher calls a time word and learners change the marker.  
* **Sudah or belum.** The everyday exchange Sudah makan? Sudah. / Belum. in pairs, then with other verbs (sudah sampai, belum bayar).  
* **Japanese bridge.** sudah ≈ もう, belum ≈ まだ〜ていない, sedang ≈ 〜ている, pernah ≈ 〜たことがある. Malay verbs do not change form, so the marker carries the time.  
* **Register.** sudah first; dah taught as its spoken form, marked spoken.

### **Question words: a cumulative drill set**

Each chapter adds its question words to one running set, and the question-word choice drill always uses the whole set to date. All entries below are now in the ledger.

* **Chapter 1:** apa (Apa khabar?)  
* **Chapter 2:** siapa, apa, di mana, the \-kah forms (Siapakah, Apakah, di manakah), adakah, bolehkah  
* **Chapter 3:** berapa (price, age, quantity)  
* **Chapter 4:** bila, pukul berapa, hari apa  
* **Chapter 5:** bagaimana (spoken: macam mana), kenapa with the answer sebab  
* **Chapter 6:** yang mana  
* **Chapter 7:** ke mana, dari mana, berapa jauh, berapa lama  
* **Chapter 8:** berapa with a counter (Berapa biji?)

### **Where the drills run**

* **Cikgu Sensai:** Block B, 20 minutes, types 1 to 6 in order; the question-word and tense sets also appear in the Block D review.  
* **Kata-Kata:** the same frames as homework, through its frame drill and Susun Ayat game.  
* **Hanashishou:** the speaking scenes from Stage 2 reuse the same patterns in context.

The drill types were already planned as component 4; this section fixes their content so all three tools use the same set.