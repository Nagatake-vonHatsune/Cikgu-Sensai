# Handoff

Update this file at the end of every session. The next builder (ChatGPT or Claude) starts here, after the charter and `AGENTS.md`.

## Current state

- **Last updated:** 11 Nov 2026, by Claude
- **Last commit before this file:** `0ee337f` (step 4 pilot). This file is updated in the commit after it.
- **Step in progress:** step 4 is **built and stopped for Sam's review**. Sam teaches units 1, 2A and 2B (and the fast packs, if used), then gives feedback. The suite template is frozen only after that (charter section 10). Do not start step 5 (chapters 3 to 9) until Sam approves.
- **Snapshots:** `docs/handoff/charter-snapshot.md` and `docs/handoff/ledger-snapshot.csv`, exported 11 Nov 2026. At step 4 start both matched the live Google versions (charter: formatting differences only; ledger: identical, L-0001 to L-1015).

## Done

| Step | What | Report |
| --- | --- | --- |
| 1 | Malay units regrouped into 9 A1 chapters and 13 unit slots; wording preserved; issues logged | `docs/STEP-1-REPORT.md` |
| 2 | Catalogue: chapter records, 11 component types, tags, test-item contract | `docs/STEP-2-REPORT.md` |
| 3 | Build checks (ledger, register, affix, Malaysian form) with a frozen, shrink-only exception baseline of 86 keys | `docs/STEP-3-REPORT.md` |
| 4 | Pilot: full 11-component suites for units 1, 2A, 2B (plus pronunciation and writing blocks) and fast packs for chapters 1 and 2; all section 6 minimums and section 14 drills met and tested; baseline 86 → 79 | `docs/STEP-4-REPORT.md` |

## How step 4 works (for the next builder)

- Pilot content is in `suite/` (`ms_c01.py`, `ms_c02a.py`, `ms_c02b.py`, `fast.py`). Malay target text is marked `«…»`. Roots and standard forms quoted from Kata-Kata notes are marked `‹…›` and listed with their source in `curriculum/malay-mentions.json`. Names go in `curriculum/malay-proper-nouns.json`.
- Unmarked ledger Malay fails the build, and so does any ledger gap in a unit listed in `curriculum/reauthored-units.json`.
- `tests/test_step4_suite.py` encodes the charter section 6 minimums. Reuse it for chapters 3 to 9.
- Builds are not byte-reproducible: the PDF inside `bank.js` changes IDs on every build. Commit the build you tested, and compare the lesson JSON, not the bytes.
- Preview PDFs with poppler (`pdftoppm`). PyMuPDF's rasteriser garbles this font subset on screen; the PDF itself is fine.

## Next: Sam's review of the pilot

Feedback to collect: timings per block, vocabulary load (core words: unit 1 44, 2A 35, 2B 37; recognition and hobby words listed separately), drill difficulty, and whether the fast packs fit one 45-minute session. After that, freeze the template and start step 5 (chapters 3 to 9).

## Decided after step 4 (11 Nov 2026)

- **No faith-specific greetings.** Sam: Assalamualaikum and Waalaikumsalam are not taught anywhere (charter section 8; ledger Rules tab). Ledger L-0009 is Retired. Both were removed from unit 1 (vocabulary, culture note, pronunciation list, teaching plan, culture-note key) and from `curriculum/malay-mentions.json`; Waalaikumsalam is not added to the ledger. Rebuilt; 31 tests pass. Ask Sam before adding any other faith-specific expression.
- **Languages in chapter 2.** Sam agreed that learners say «Saya boleh cakap bahasa Melayu sedikit.» in chapter 2. Ledger: new rows L-1016 «bahasa», L-1017 «Melayu», L-1018 «Inggeris»; L-0216 «sedikit» moved from Ch5 to Ch2 (reused in Ch5); L-0473 «cakap» placed in Ch2. The spoken «sikit je» (L-0948) is now allowed and is taught in unit 2A as a chat word. «Melayu» and «Inggeris» are listed as proper nouns, so the affix check does not read «Melayu» as me- + ‹layu›.
- **Hobby word bank (chapter 2).** Sam's list: karaoke, golf, cafe hopping, travelling, hiking, oshikatsu, plus muzik, filem, sukan, lagu, masak and badminton. Ledger L-1019 to L-1031, and L-0968 «badminton» placed in Ch2. Malaysian forms («muzik», «filem», «sukan», «kafe», not the Indonesian ‹musik›, ‹film›, ‹olahraga›). «travelling» and «hiking» use «jalan-jalan» and the spoken loans «travel» and «hiking»: ‹melancong› and ‹mendaki› are me- verbs and wait for chapter 11. In unit 2B the bank is a separate vocabulary group: each learner keeps the words that are true for them, and only those are tested.
- **Vocabulary parity (Sam: "ease some of the excess 52 words … and have parity").** Unit 1 already carries 44 words, so nothing more moves into chapter 1; the balance is between 2A and 2B. «dengan» moved from 2B to 2A (example «Saya cakap bahasa Melayu dengan kawan saya.»). Each unit now separates core words from recognition words:
  - unit 1: 44 core;
  - unit 2A: 35 core, plus 12 chat words from "Sembang di pantri" to recognise;
  - unit 2B: 37 core, plus 14 office words from "Pagi di pejabat" to recognise and the 14-word hobby bank.
  Unit 2A also gained drill items (substitution 9 and 10, question and answer 9 and 10) and two model-conversation turns (now 16) for the language sentence; unit 2B gained a hobby example in pattern 3 and substitution items 11 and 12. The chapter 2 fast pack shows both sentences.
- **Etymology notes come from Kata-Kata only for now** (Sam). Do not write new etymology into Cikgu Sensai; quote Kata-Kata card notes and mark roots with ‹…›.
- **Ledger copies refreshed** (both `curriculum/reference/katakata/malay-ledger.csv` and `docs/handoff/ledger-snapshot.csv`, now L-0001 to L-1031); new hash pinned in `docs/step4-sources.json`. Journal rows 43 to 49.

## Open questions for Sam

- **Unverified items to confirm:** the pronunciation notes (unit 1), the name-customs paragraph (unit 2A culture note), and every "Japanese helps or misleads" note.
- **Still open from before:** which textbooks the other Japanese teachers use, and the explainer language for Japanese packs. The Kamus Dewan check for L-0983 to L-1031 has still not been run (L-1031 «oshikatsu» will not be in Kamus Dewan; it is kept as a fans' loanword).

## Other repositories

Kata-Kata (Claude Code) still needs the same ledger changes: new cards for L-0983 to L-1031, saya and the time words moved to chapter 1, Ch2 cards for «sedikit», «cakap» and «badminton», and card ms-c01-009 (Assalamualaikum, L-0009) removed. Tracked in the ledger Journal as pending.

Step 4 findings for Kata-Kata:
- The chapter 2 scenario uses «dari mana» (ledger chapter 7) and «badminton» (chapter 6) at chapter 2.
- Chapter 1 still has no Dunia scene; Block E of unit 1 uses the chapter 1 scenario instead.
