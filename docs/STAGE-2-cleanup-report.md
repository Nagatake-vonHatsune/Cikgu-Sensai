# Stage 2 clean-up: refresh from Kata-Kata, rules fixes, chapter 17 fixes, the approved words back in, PDF text

**14 November 2026 · Claude.** Authorised by Sam (the Stage 2 clean-up instruction, 14 Nov 2026): refresh from Kata-Kata, rules fixes, chapter 17 fixes, and the newly approved words back into the units; follow `AGENTS.md` for checks, commits and the push to main; **stop at the end for Claude's review before chapter 18.** Started at `5d131e1` (Claude's PDF font fix). Kata-Kata (read only) is at `907946f`. Kata-Kata, Hanashishou and the ledger sheet were not edited. I did not re-open the charter Google Doc; nothing in the work depends on a charter change.

## Summary

| Part | Commit | What |
| --- | --- | --- |
| 1 Refresh | `b70d783` | c10 to c18 and both ledger copies from Kata-Kata `907946f`; 1,309 rows; **Stage 2 core 271**; the six practice-pool rows are not core |
| 2 Rules | `f0cdb97` | «tanda tangan» is a disallowed form (two words); the `lah-in-answer-key-fails` fixture uses «Takpelah, saya tunggu.»; 81 shared cases agree |
| 3 and 4 | `aecdc24` | «tandatangan» check (the two lines changed in Part 1, forced by the new ledger row); Sam's chapter 17 fixes (14 Nov) |
| 5 Words | `2529085` and `9747fc8` | The 31 approved core words are in the units, the lines are back to the natural wording, the HANDOFF backlog is empty |
| 6 PDF text | `7ccbdd1` | Cause found and fixed in `build.py` (three lines): the `liga` and `locl` features; rebuilt `dist/`; four pages looked at |

The checks: `python3 -m unittest discover -s tests` passes (**309** tests, 298 after Part 1, 306 after Part 5) and `python3 build.py` passes (542 packs, **3,346 pages** (3,335 before; the units grew by the new words and the fi and ff ligatures are two letters wide now), all fit-checked). The language checks are the same 20 violations (all in the frozen baseline of 30, none in a re-authored unit) and **188 ledger gaps** (199 before: the 31 new rows close 11 gaps in older content). Every re-authored unit still has zero violations and zero gaps.

## Part 1: refresh

- **Copied** Kata-Kata `content/ms/kelas/c10.json` to `c18.json` into `curriculum/reference/katakata/` (c10 to c17 differ from the old copies only by the appended class cards for the new core rows: every old card, frame, scenario line and Sedia Kelas list is unchanged; c18 and c01 to c09 are byte for byte the same). Both ledger copies come from `content/ledger/malay-ledger.csv`: `docs/handoff/ledger-snapshot.csv` is the Kata-Kata file byte for byte (CRLF), the reference copy is the same file with LF. Hashes and the commit are in `docs/step4-sources.json`; the pinned-source tests and the `catalogue.py` link moved to `907946f`.
- **The ledger:** 1,309 rows. The diff to the previous copy is exactly what Kata-Kata's report lists: L-0530 «tandatangan» (was «tanda tangan»), 17 existing rows with a card ID and place change (the chapter 10 Dunia picture scene's twins) and 37 new rows. **31 are Stage 2 core** (L-1273 to L-1303, placed Ch10 to Ch17, Draft, Action «KD4 check») and **6 are practice pool** (L-1304 to L-1309: «menyapu», «disemak», «disimpan», «bersukan», «hidup», «giliran»), place «Kata-Kata practice pool (not core); Dunia · Kata biasa (primes Ch18)».
- **Stage 2 core is now 271** (56 existing + 215 new). By chapter: 10 = 44, 11 = 45, 12 = 48, 13 = 29, 14 = 29, 15 = 23, 16 = 27, 17 = 26. Updated in `docs/stage-2-plan.md` (the unit table, the totals paragraph and a new section) and `HANDOFF.md`.
- **The six practice-pool rows stay out of the core counts, the coverage tests and any chapter 18 key.** The checker reads the place column only, and "primes Ch18" reads as chapter 18, so they are not forward references in a chapter 18 unit but they *are* gaps in chapters 10 to 17 (as they were before). `tests/test_stage2_cleanup.py` checks that none is in a unit's core list or a fast pack, that every one has "practice pool" in its place and that the Stage 2 core count is 271.
- **Things the new ledger forced (all in the Part 1 commit, so that the checks pass):**
  - The two «tanda tangan» lines (Part 3).
  - «bersukan» is now a ledger word, so the two 10A teacher notes that said "*bersukan is not in the ledger" quote it as a ‹bersukan› mention with a source (`curriculum/malay-mentions.json`).
  - **«minggu depan» (L-1303, Ch17) is already taught at chapter 4** (Kata-Kata card ms-c04-019; used in 4B, in a 7 note and in 10B). Placed as a phrase row at chapter 17 it makes those early uses forward references. I added `curriculum/phrases-taught-earlier.json` (a Cikgu Sensai file, not a shared rules file), which lets the phrase through from chapter 4, and one condition in `language_checks.py`. **This is question 1 for Sam.**
  - The catalogue's word registry lists the six practice-pool Dunia cards (a unit may use «disemak»), never as core.
  - Tests: the interim set `PENDING_NEW_CORE` kept the unit tests green until Part 5 (it is deleted now); the core selectors accept the new place texts ("Ch10 (unit 10A); Dunia · …"); the class card is the first ID when a row lists a Dunia twin too; L-0530's stale action cell «KD4 check; refresh Kata-Kata Dunia card» is allowed in one test (Kata-Kata did that card in step 3e and I may not edit the sheet).
- Build before and after Part 1: 20 violations (unchanged), 188 gaps (was 199).

## Part 2: rules (own commit `f0cdb97`)

- **`lah-in-answer-key-fails`** now uses «Takpelah, saya tunggu.» (chapter 17). «baiklah» (L-1289) is a word in its own right, so «Baiklah, saya tunggu.» no longer tests R4. «Takpelah» is «takpe» (L-1266) plus the joined «lah», so it still fails in an answer key. **Both checkers agree on all cases again** (81 of 81 here). Ledger Journal row 198 is answered.
- **«tanda tangan» is a disallowed form** (Malaysian «tandatangan»), allowed only inside a ‹…› mention whose source says "do not use". It is the first disallowed form of two words, so the rule's `format` text now says a two-word form is matched as the two words in that order; `language_checks.py` does it with one regular expression. Four new fixtures: `indonesian-tanda-tangan-fails`, `tandatangan-joined-passes`, `tanda-tangan-in-do-not-use-note-passes`, `tanda-tangan-mention-without-do-not-use-fails` (**81 cases**, was 77).
- `docs/STAGE-2-step2-report.md` has the rules section updated and a new "Stage 2 clean-up amendments" section.
- **For Kata-Kata:** copy `curriculum/stage-rules.json` and `curriculum/stage-rules-fixtures.json` from commit **`f0cdb97397c17af15f4daaabb34a7a6b836dcc97`** at its next rules sync (update `SOURCE.json`'s pins and the case count, 77 to 81, and make its checker match a two-word disallowed form). Noted in `HANDOFF.md`.

## Part 3: «tandatangan»

11B pattern 1 is «Tolong tandatangan di sini.» and the Stage 1 2B example is «Ini tandatangan saya.» (both changed in the Part 1 commit, because the new ledger row made the spaced form a ledger gap and the build stopped). A search of every unit and the legacy text finds no other spaced form, and `tests/test_stage_rules.py` now fails if one comes back. The Stage 1 vocabulary entry for L-0530 shows the ledger headword, «tandatangan», without an edit.

## Part 4: chapter 17 fixes (Sam, 14 Nov)

All six are in `suite/ms_c17.py` and recorded in `docs/stage-2-decisions.md` section 14, with the chapter 17 questions 1 to 8 marked "Claude's recommendations, not contested by Sam" (all as built).

| Sam's fix | Now |
| --- | --- |
| «Lain kali, ya?» is a soft no, like また今度 | dropped from the reading reply and the test reading wherever the writer offers a new day («Bagaimana kalau hari Khamis?»); the answer to "What does he suggest?" is "Thursday"; a teacher note says so. The writing model did not use it. The Kata-Kata frame f02 and every refusal that offers no day keep it. |
| «Saya ajak Encik Tanaka makan malam. Sudikah encik datang?» | «Saya mahu ajak encik makan malam. Sudikah encik datang?» |
| «Sudikah cik singgah di pejabat dulu?» | «Boleh cik singgah di pejabat dulu?» and a teacher note: «sudi» is very polite, for invitations; «boleh» is the casual, common choice |
| «Kafe itu pedas.» | «Makanan di kafe itu pedas.» (I also changed the same slip in a short dialogue: «Terima kasih. Tetapi kafe itu pedas.») |
| «Terima kasih. Saya ada hari lain.» | «Terima kasih. Kita cari hari lain.» |
| «Terima kasih atas jemputan puan. Saya datang.» | «… Saya akan datang.» |

## Part 5: the new words, line by line

Every approved core row is in its unit's core list and vocabulary (an example line, and an entry whose meaning is written without unmarked Malay), in at least one pattern, dialogue, listening or task line, and in its chapter's fast pack (`C##_WORDS`, with the "N core words" counts). The Kata-Kata scenario lines are word for word, and every changed line passes `tools/check_spans.py` at its chapter. Counts per unit: 10A 24 (was 20), 11A 21, 11B 24, 12B 25, 13 29, 14 29, 15 23, 16 27 (a fifth group «What happened, and what to say»), 17 26.

| Ch | Word → line (where) |
| --- | --- |
| 10 (10A) | «tiga kali seminggu»: «Saya bersenam tiga kali seminggu.» (frame f03; was «… setiap hari Isnin, Rabu dan Jumaat.»). «kolam renang» and «taman»: «Pada hari Sabtu saya berlari di taman. Pada hari Ahad saya berenang di kolam renang.» (variant). «penuh»: «Kereta api selalu penuh.» (listening; was «… selalu sesak.») |
| 11 | «kepada» (11A): «Awak menghantar apa kepada pengurus?» «Saya menghantar emel kepada pengurus.» (frame f01). «sehari», «menempah», «bukit» (11B): «Seratus ringgit sehari.», «Kami menempah kereta di sana.» (listening; the item now tests «menempah»), «Saya mahu mendaki bukit dengan kawan saya.» and «Kami menempah kereta, seratus ringgit sehari.» (frame f06) |
| 12 (12B) | «melaporkan kebocoran»: «Encik sudah melaporkan kebocoran itu?» «Saya melaporkan kebocoran itu kepada pengurus.» (frame f06). «Tolong simpankan salinan borang itu di pejabat.» (review block; was «… simpankan borang itu …»). «Juruteknik sudah dihubungi.» (frame f05). «Paip itu sudah dibaiki oleh juruteknik.» (frame f04) |
| 13 | «Saya tidak sihat. Saya demam, tetapi saya tidak batuk.» (frame f01). «Saya akan beritahu doktor.» (variant; was «Saya cakap dengan doktor nanti.») and «Awak patut beritahu bos dulu.» (frame f04). «Awak perlu tanya ahli farmasi.» (frame f03; the speaker label stays «Pharmacist»). «Boleh saya tinggalkan beg di sini?» (frame f02, the variant, the changed-fact line and the task key; was «letak beg»; «Letak beg di sebelah kaunter.» keeps the revision word «letak» in use) |
| 14 | «Baiklah, kita buat begini.» (the casual listening turn). «Puan Aini mahu ikut?» (listening; was «mahu datang?»). «Apa kata Puan Aini?» (frame f01). «PENGUMUMAN» as the notice heading (the notice model and the writing key). **Third person (frames f02 and f03, f04):** «Mei Ling menangguhkan rancangan mendaki kerana dia bekerja.» and «Cik Mei Ling membatalkan rancangan mendaki kerana hujan.»; the bare «tangguhkan» and «batalkan» stay for requests, offers and «kita» plans («Boleh kita tangguhkan ke hari Ahad?», «Kita batalkan rancangan mendaki.»). The decisions note that allowed the interim bare form is updated (sections 11 and 15). |
| 15 | «Kakitangan stesen ada di kaunter.» (frame f02; the label stays «Staff»). «Bulat, seperti bola.» (frame f06, the drill, the key and the reading form; was «… seperti jam»). |
| 16 | «Encik tidak apa-apa?» «Saya tidak apa-apa, terima kasih.» (frames f03 and f06). «Ada masalah?» (listening; was «Kenapa?»). «Apa yang berlaku?» (frames f03 and f06). «Boleh saya pinjam telefon encik?» (frames f03 and f06) |
| 17 | «Sila balas sebelum hari Rabu.» (frame f01 and the written invitation; «Sila hubungi Puan Aini.» stays beside it, because «hubungi» is a revision word the unit must still use). «Saya belanja minggu depan.» (frame f06, the listening and the teacher note; was «Lain kali saya belanja.») |

Left as they were, on purpose: the 12A and 12B Kata-Kata lines («Saya simpankan bungkusan itu …»), «Tolong baiki paip ini.» requests, and the Kata-Kata s05 line «Kita tangguhkan ke hari Ahad …».

**The HANDOFF backlog is empty.** `docs/stage-2-decisions.md` section 15 records the rulings; `tests/test_stage2_cleanup.py` (8 tests) checks the 31 words (core list, vocabulary example, fast pack, use in a pattern or task line), the restored lines, that the old lines are gone, that the practice pool is not core, the third-person rule, the chapter 17 fixes and the empty backlog.

## Part 6: PDF text check

**Finding (about 25 minutes).** The ToUnicode map the PDF carries had no entry for **two kinds of glyph the pages actually draw**. The subset font keeps the OpenType features `liga` and `locl`, so the shaper draws the digits 0 to 9 as alternate glyphs (`locl`, lookup 6) and «ff», «fi», «fl», «ffi» as ligature glyphs (`liga`). Those glyphs look the same as the normal ones but have **no Unicode value of their own** (no `cmap` entry), so MuPDF's ToUnicode map cannot name them and a viewer copies the raw number instead. In the old bank, page 1's header text «B1» is written as the glyphs for "B" and the alternate "1" (glyph 2285, no entry); copying gives «B» plus a stray character, and «A1» comes out as «A=» in Sam's viewer. The same break hits every word with «fi», «fl», «ff» or «ffi» («file» copies as «6le», «office» as «o8ce» in my test). The missing entries were exactly glyphs 2284 to 2293 (the ten digits) and 2124 to 2127 (the ligatures); every other glyph the pages draw had a correct entry. So the earlier font fix is not the cause: the glyphs draw correctly, only the copy map is incomplete.

**Fix (small, safe, in `build.py`).** The subset keeps only the `ccmp`, `vert` and `vrt2` features (`subset.Options().layout_features`), so the shaper has nothing to substitute: the digits and «fi» now use the normal glyphs, which do have entries. Visually the only change is that «fi», «fl», «ff» and «ffi» are drawn as two or three separate letters instead of one ligature glyph (the page images in my test are otherwise identical). I reproduced the bug in a small script that copies the build's font and `insert_htmlbox` steps: before, «A1 B1 file fish office different» extracts as «AE BE 6le 6sh o8ce di5erent»; after, it extracts as written, with PyMuPDF and with `pdftotext`. `tests/test_pdf_fonts.py` has three new tests: the build keeps no substituting feature, every glyph drawn on a sample of pages has a ToUnicode entry, and digits and «fi» words extract as written.

**Pages looked at by eye** (rendered with PyMuPDF `get_pixmap` from the built `dist/bank.js`): four pages, as the instruction asks, plus the extracted text of the same pages (`get_pixmap` at 100 dpi, then looked at by eye; `pdftotext` and PyMuPDF for the text): **Stage 1** page 631 (Unit 1 vocabulary, the greetings: blue Malay, Japanese, English and the «A1» in the header all correct); **chapter 11** page 2416 (Unit 11B core words: «menyemak», the root and nasal-change notes, Japanese); **chapter 14** page 2858 (Unit 14 pattern 1: the new «Apa kata Puan Aini?» example, the explanation and the Japanese bridge); **chapter 17** page 3251 (Unit 17 listening focus: the spoken forms «takpe», «tak tahan», «set», «kat», «tu»). All four render as written. Text copy: a sample of 305 pages (every 11th) gives «A1», «A2», «B1», «first», «office», «different» and «file» as written and none of «AE», «A=», «6le», «o8ce», «di5erent»; `pdftotext` on pages 631 and 2416 gives the header «A1» and «A2» and the Malay text correctly. The new `tests/test_pdf_fonts.py` tests also run over every 25th page of the bank.

## Questions for Sam

1. **«minggu depan» (L-1303)** is placed at Ch17, but chapter 4 already teaches and uses it (card ms-c04-019, 4B, 10B). The checker would call those early uses forward references, so I added `curriculum/phrases-taught-earlier.json` (a Cikgu Sensai file, one entry) and one condition in the checker. Do you want the ledger row's place changed to Ch4 (then it is not a Stage 2 core word and the count is 270), or keep the exception? The unit 17 line «Saya belanja minggu depan.» is fine either way.
2. **Fast packs.** The chapter 10 to 13 fast packs hold the 20 words they had plus the new ones (24 each; the chapters have 44, 45, 48 and 29 core words); from chapter 14 on they hold all core words (your ruling of 13 Nov). Do you want the chapter 10 to 13 packs widened to all core words?
3. **The ledger sheet** (not mine to edit): L-0530's «Action (open)» still says "refresh Kata-Kata Dunia card", which Kata-Kata finished in step 3e; the practice-pool rows' place text makes the shared checker read chapter 18, which is fine only while nobody uses them before chapter 18. Is the place text «Kata-Kata practice pool (not core); Dunia · Kata biasa (primes Ch18)» the one you want?
4. **Two-word disallowed form.** Kata-Kata's checker reads disallowed forms as single tokens; it needs the same two-word match when it copies the rules.
5. **Native reader, new lines** (my judgement calls; the checks cannot judge naturalness): «Kami menempah kereta, seratus ringgit sehari.», «Paip itu sudah dibaiki oleh juruteknik.», «Puan Aini kata, kalau hujan, kita tangguhkan. Bila cuaca cerah, kita mendaki.», «Saya tidak sihat. Saya demam, tetapi saya tidak batuk.», «Bulat, seperti bola.» (a round bag), «Boleh. Letak beg di sebelah kaunter.», «Encik tidak apa-apa?» «Saya tidak apa-apa, terima kasih. Cawan saya pecah.», «Boleh saya pinjam telefon encik?», «Sila balas sebelum hari Rabu.», «Saya belanja minggu depan.», «Baiklah, kita buat begini. Di stesen, pukul tujuh.»

## Not verified

- Kamus Dewan: none of the new lines was checked (end of the project, ledger Journal row 128). The card notes are the source for the forms.
- Naturalness of the new lines (question 5) and of the Japanese, which stays a draft.
- The build's fit check passed for every page; the pages I looked at are listed above, not all 3,000 or more.
