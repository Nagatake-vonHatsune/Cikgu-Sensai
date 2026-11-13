# STAGE 2 AUDIT REPORT: Batch 1b

**Scope:** Sam decided that Claude builds Stage 2 and asked Claude to audit ChatGPT's draft `docs/stage-2-plan.md` (commits d6ec42b to a82dcd0), fix it in place and replace its questions with a one-sitting decision brief. Planning only: no ledger writes (other than regenerating the copies), no chapter suites. Publication to main was pre-approved when the checks pass.

**Status:** audited plan and decision brief published; waiting for Sam's answers in [`docs/stage-2-decisions.md`](stage-2-decisions.md). `python3 build.py` and all 155 unit tests pass at each commit.

| Commit | Content |
| --- | --- |
| `29f0217` | Ledger copies and hash regenerated from the sheet: only the "Action (open)" column changed (119 rows, Journal row 129) |
| `3f3c367` | Stage 1 tidy-up: unit 5 pattern 4 tagged ms-c05-f04 and ms-c05-f06 («Kenapa / Mengapa»); unit 6 pattern 4 tagged ms-c06-f05 and ms-c06-f07 («Saya pilih»); both chapter fast packs and the two pattern tests updated |
| next commit | Audited plan, decision brief, this report, `HANDOFF.md` |

## Sources read

The live charter (Google Doc revision `AHj4eMSXOEF1…`, sections 3 to 6, 8 and 14 and the Stage 1 plan), `AGENTS.md`, `HANDOFF.md`, `docs/STEP-5h-report.md`, `docs/STEP-5i-report.md`, the plan in full, the ledger (sheet Ledger!A1:T1089 and Journal rows 120 to 129), `language_checks.py`, `curriculum/malay-roots.json`, `curriculum/foundation.txt`, and the Hanashishou repository at `55fd4ed` (read only; added to this session for the scene check).

## What the audit found

1. **Ledger reconciliation [VERIFIED against the sheet copy].** All 53 existing IDs the draft cites exist with the stated headword, meaning and band, and none is placed yet. No draft "new" form duplicates any of the 1,088 rows exactly, including L-1084 to L-1088 and the rows the Kata-Kata clean-up touched. Near-duplicates: «sehingga» beside L-1086 «hingga» (dropped); «berpindah» and «menukar» are the standard forms already named in L-0667 «pindah» and L-0604 «tukar» (now linked). Six roots of chapter 11 verbs have no row («terima», «lihat», «pinjam», «pesan», «ajar», «lancong»), so those verbs are taught as whole forms with the root shown.
2. **Malay forms [my judgement; no native review].** No Indonesian form was found. 211 of 235 forms are kept as they were; 5 changed in place, 2 replaced, 1 moved, 16 dropped (duplicate, B1 level, low need, or already covered by the chapter's own pattern); 16 added. Result: 233 core words, 57 existing rows and 176 new, every unit 19 to 24. Four forms are **Sam to confirm**: «mengecas», «jemputan», «cuti sakit» with spoken «MC», and «nombor penjejakan».
3. **Gaps the draft missed.** The ledger has no «lelaki», «perempuan» or «kunci», yet chapter 15 describes people and chapter 16 has a key left inside a flat; the linked Hanashishou clinic scene uses «MC» seven times and «klinik panel» three times, and chapter 13 had neither. All are now in the lists.
4. **Affix morphology.** Every ber-, meN- (nasal changes), -kan, -i and ter- form is spelt and formed correctly and arrives no earlier than its gate. One explanation was wrong: «bekerja» is not an exception but follows the be- rule (first syllable ending in -er); «belajar» is the only true exception [INFERRED from secondary grammar sources found by web search; not checked in Tatabahasa Dewan]. Proposal for Sam: the charter's ber- note should say "no nasal sound changes".
5. **Structure [VERIFIED arithmetic].** 67 blocks = 50.25 hours is correct; the review, writing and test pattern matches Stage 1. Cumulative class plus self-study is about 183 hours by the end of Stage 2, inside the charter's quoted A2 guideline (180 to 200). The unit split, chapter 18, the fast course and the pass rule are consistent with the Stage 1 decisions and were left unchanged.
6. **Scenes [VERIFIED file and blob level].** All nine linked scenes and five vocabulary files exist at the recorded blob SHAs, and the draft's content claims are correct. One link was mis-described: the chapter 10 driver scene is background small talk, not "the working day"; it now serves 10B, with the new-neighbour scene added. The plan asserts no real-world fact that needs a source.
7. **Simplified.** The derived-form storage question is answered with the ledger's existing practice (one row per taught form, root in "Root (KD4)"), and the eight-point checker design with a new schema is cut to seven ledger-driven items. The two real code defects the draft found are kept (fixed c01–c09 loader and minimum-chapter reading in `language_checks.py`; Kata-Kata's global exemption set).

Every change to the plan is itemised in its [Audit log](stage-2-plan.md#audit-log).

## Verification status

- **[VERIFIED]** ledger rows, IDs, duplicates and counts (scripted against the regenerated copy); block and hour arithmetic; Hanashishou file paths, blob SHAs and quoted lines; `language_checks.py` behaviour.
- **[INFERRED]** the ber- spelling rule (secondary sources, below).
- **[UNVERIFIED]** my judgements of Malaysian usage and need for every form have had no native-speaker read; the four "Sam to confirm" items in particular. «mengecas» was not found in PRPM by web search. All Japanese is a draft (two glosses were sharpened: «menyewa» and «meminjam» were both 借りる).

Web sources consulted for item 4: secondary descriptions of ber- allomorphs at [kumparan.com](https://kumparan.com/berita-terkini/memahami-makna-dari-imbuhan-ber-dalam-sebuah-kalimat-21RS8lxf9mm), [Scribd document 581257442](https://www.scribd.com/document/581257442/52945-147088-1-PB) and [MLCS Singapore](https://mlcs.moe.edu.sg/files/Kertas2_Dian2.pdf) (search excerpts only; none is Tatabahasa Dewan). The ledger and the draft's own DBP excerpts remain the main sources.

## Sam's decisions and next step

Sam answered the brief in chat on 13 November 2026: every recommendation accepted; W6, W7, W8 yes; W9 yes («bertolak» added, 234 core words); R1 (a); G3 no (build every chapter, no chapter 10 pilot); and Claude edited the charter for R7 (section 5, ber- has no nasal sound changes; the snapshot matches). The answers are in [`docs/stage-2-decisions.md`](stage-2-decisions.md) and at the end of the plan. Next is build step 1, the ledger session, which records the answers in the Journal before writing any row.
