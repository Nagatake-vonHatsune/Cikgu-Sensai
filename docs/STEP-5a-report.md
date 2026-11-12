# STEP 5a REPORT: Chapter 3, Batch 1 (redo)

**Scope:** Malay A1 chapter 3 only, units **3A**, **3B**, **3C**, and the chapter 3 fast pack. Chapter 4 is not authorised. Working source of truth: charter v0.1, AGENTS.md, HANDOFF.md, Kata-Kata chapter 3 reference and pinned ledger. Sam authorised publication in advance.

**Review status:** draft for Sam's pilot and native Japanese review. Actual build/test results and deployment must be verified from GitHub Actions and main; this report does not substitute for that evidence.

## Word accounting

All counts below are unique *ledger entries*, not alternative spellings. A slash-marked variant counts as one entry. Core and recognition ID lists do not overlap.

| Unit | Scope | New core | Dunia to recognise | Revision (not new) | Extra block |
| --- | --- | ---: | ---: | ---: | --- |
| 3A | Numbers up to one million, age, fictional telephone digits | **25** | **5** | **6** | Cumulative review |
| 3B | Prices, payments and change | **24** | **11** | **8** | None |
| 3C | Ordinals, fractions, decimals, percentages, measures | **24** | **8** | **9** | Written order/measurements |
| **Total** | | **73 unique** | **24 unique** | **23 instances** | |

The 56 original Kata-Kata chapter 3 cards, plus the 17 chapter 3 ledger additions L-0989 to L-1005, appear as new core exactly once. The 24 Dunia entries are the bank/post-office entries L-0418 to L-0430 (split 5 and 8) and the market entries L-0512 to L-0522 (11). They are displayed separately under **Dunia · To recognise** and not tested as new core. Earlier words are listed separately under **Revision · 復習** and do not increase the core count. No ledger or Kata-Kata reference source was edited.

## Evidence for charter section 6 and drill-bank section 14

| Minimum | Source and mechanism |
| --- | --- |
| Eleven components per unit | suite/chapter3_common.py generates opener, vocabulary, pattern-grammar, drills, model conversation, listening, reading-writing, task, culture, test, and teaching plan. tests/test_step5a_suite.py checks component presence. |
| 3–5 patterns and 4–6 Q&A each | Four patterns with four A/B examples apiece per unit; original Kata-Kata frame IDs ms-c03-f01 to ms-c03-f07 are retained. |
| 30+ drills and three dialogues | Five drill types with eight numbered prompts each (40), four additional short dialogues with a self-generated third turn, and a separate cumulative question-word drill. |
| Cumulative question words | The drill covers apa, siapa, di mana, -kah formal forms, adakah, bolehkah and berapa. |
| 10–16 turn conversation plus gaps and changed facts | Each unit contains a 12-turn dialogue, a gapped version and a separate 12-turn changed-facts variant. |
| 120–250 Malay-word listening and at least six items | Teacher-read Encik Tanaka scene scripts, eight listening comprehension items, before/while/after tasks and shadowing. The new test enforces the required Malay-word range. No audio files. |
| Reading and writing, at least five questions | Fictional class forms, price lists or order/dimension sheets with six questions each, guided writing and teacher answer keys. |
| Independent task plus change of plan | Separate role cards for A and B, a numerical or payment change, and success criteria. |
| Culture/usage note of 150–300 English words | Unique English notes for 3A (quantity and privacy), 3B (cash, card, register), and 3C (ordinals, proportion, measurements), plus Japanese draft summaries. Length is tested. Word-building claims come only from Kata-Kata notes. |
| Test of 15–20 items plus speaking | Per unit: five listening, six vocabulary, two grammar and four reading questions (**17 scored**) plus one speaking item and can-do self-check. Item tags resolve against the ledger and grammar registry. |
| 45-minute blocks and independent components | Each unit has five timed A–E 45-minute blocks with retrieval first, including a Dunia scene block. Extra review follows 3A and extra writing follows 3C. Components are tagged for independent printing. |
| Fast pack 2–4 pages and one 45-minute lesson | suite/fast.py has 20 priority words, seven brief patterns, a ten-turn dialogue, a fictional buying task, a five-item self-check and a guide to full Kata-Kata c03 cards, frames, two Dunia scenes and about 9–10 hours self-study. tests/test_step5a_suite.py checks actual page count. |
| Legacy pack retirement | Counting and quantities, Ringgit and sen, Order and floors, Beli buah di pasar, Jumlah buah and Pesanan buah are removed from the active catalogue. Source files remain in curriculum. |

## Files changed

* **Content:** suite/chapter3_common.py, suite/ms_c03a.py, suite/ms_c03b.py, suite/ms_c03c.py, suite/fast.py.
* **Registration:** suite/__init__.py, course.py, catalogue.py and curriculum/reauthored-units.json. All chapter 3 parts have ledger-gap checks.
* **Checks:** tests/test_step5a_suite.py, tests/test_catalogue.py and .github/workflows/step5a-verify.yml. The recovery-branch workflow runs python3 build.py and python3 -m unittest discover -s tests -v on full Git history, then commits the generated print assets if successful.
* **Handoff and reporting:** HANDOFF.md and this file.
* **Generated deliverables:** dist/bank.js and its PDF, dist/chapters.js, dist/catalogue.js, offline ZIP and docs/step4-authored-scope.json generated by build.py rather than manually edited.

## Proposed ledger rows

**None added or edited.** The number-building terms and new chapter 3 terms already exist in the pinned ledger, including L-0989 to L-1005. Any genuine missing learner word should be proposed to Sam first and entered through the shared ledger and Journal, not invented locally. No exception may be added to bypass a ledger gap.

## Unverified and provisional

1. All Japanese glosses, grammar comparison notes and summaries await native-speaker review.
2. Earlier pending Kamus Dewan checks on newer ledger rows L-0983 to L-1031 remain upstream. No approval is claimed here.
3. Naturalness of a few simplified, ledger-restricted market and measurement exchanges needs Sam's pilot feedback. Chapter 8 classifiers are deliberately not introduced.
4. Every phone number, price, discount, weight and dimension is fictional teaching data, not a real value. No learner's identifying telephone number should be collected.
5. Kata-Kata and Hanashishou content is not edited; Kata-Kata cards for pending ledger-only additions remain an upstream follow-up.
6. PDF fit, the strict register and affix checks, and complete test success must be verified by the passing workflow run. Do not publish if any fail.

## Questions for Sam at pilot feedback (not decisions to reopen)

* Which of the three unit drill ladders runs too quickly or slowly in class?
* Should the 3C fractions and measurement practice receive additional time before chapter 8 classifiers?
* Is the fast pack realistically teachable within one 45-minute session?

**Stop:** Chapter 4 and later materials wait for Sam's pilot feedback and explicit instruction.
