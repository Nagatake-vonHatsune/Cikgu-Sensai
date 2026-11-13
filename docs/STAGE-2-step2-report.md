# Stage 2 build step 2: stage-aware Malay checks

**13 November 2026 · Claude.** Authorised by Sam (build step 2 instruction, 13 Nov 2026; publication to main pre-approved when the checks pass). No chapter content, ledger row or reference file was changed.

## Result

- `python3 build.py` passes: 335 packs, 2,140 pages. The checks find the same 22 violations as before (all in the frozen baseline of 30) and the same 203 ledger gaps.
- All **165** tests pass (155 before, plus 10 new in `tests/test_stage_rules.py`).
- **Stage 1 unchanged:** before committing I ran the old and the new checker on every segment the build checks (13,586 segments, chapters 1 to 9, the legacy chapter 12 pack and the unplaced packs). Violations, their reasons, ledger gaps and derivations are identical.

## What the checks now enforce

All rules live in `curriculum/stage-rules.json`; `language_checks.py` reads its numbers and lists from there.

1. **Affix gates.** ber- from chapter 10; meN- (with nasal changes) from 11; -kan and -i from 12 (meN-…-kan and meN-…-i need both); ter- for an accident or unplanned state from 16. A ber-, meN-, -kan, -i or accident ter- form passes only if every gate is open **and** its own ledger row is placed at or before the unit's chapter (for a Stage 1 derivation such as «dibaiki» or «simpankannya», the base's row). An affixed form with no placed row fails, even after its gate. A ‹…› mention with a source in `curriculum/malay-mentions.json` is still not checked.
2. **Family detection.** If the ledger's "Affix tag" names a family or a non-root type (for example «masakan» is tagged -an), the tag decides. Otherwise the spelling decides. This matters for L-0619 «tertinggal», L-0621 «terlepas» and L-0644 «terlupa», which the ledger tags "root": they are still gated at 16. «termurah», «terbesar», «terbaik» and «tercantik» stay chapter 6 superlatives and never open the accident ter- family. A final i is not -i («membeli», «mengisi»), and «makan», «ikan», «bukan» and «akan» are roots.
3. **Whole words at their own chapter:** Selamat berkenalan (1), belajar (2, the only bel- spelling), berapa (3), mengapa (5), the four superlatives, bersih and menang (6), Dilarang merokok (9), bekerja and berehat (10, the be- spelling of ber-), mesej (11), mesti (13), belanja and setuju (17); plus every ledger row tagged chunk, chunk* or lex, at its own chapter (so «rumah terbuka» stays a chapter 9 phrase), and the look-alike roots (the Kata-Kata allow-list plus Sam's list in `curriculum/malay-roots.json`). The Stage 1 di- rule (9), se- + classifier (8), ke- ordinals (3), -nya, -kah and -an (2) are unchanged; their chapter numbers now come from the file.
4. **Placement read strictly.** The chapter is the lowest "ChN" in the ledger's place column after removing notes ("moved from", "reviewed in", "reused", "was", "waits for"); card IDs no longer count, and a retired row is never placed. For today's ledger this gives the same chapter for all 1,265 rows. Every pinned Kata-Kata chapter file is loaded, not a fixed c01 to c09 range.
5. **Register (R3).** New pairs: tidak mengapa / tak apa (from chapter 10) and tidak mengapa / takpe, tidak tahan / tak tahan, setuju / set, di / kat (in every chapter); seperti itu / macam tu, ini / ni and itu / tu were already checked. «tidak mengapa» is taught as «tidak mengapa» (spoken: «takpe» / «tak apa»), per Sam's answer below. As before, a spoken form fails unless its standard form was taught earlier and the spoken form was taught with a "spoken" label.
6. **Particles (R4).** «lah» and «kan» may appear in prompts and listening once placed (chapter 17), but a test answer key that contains them fails («lah» on its own or as an ending, «kan» on its own; «adalah» and «masalah» are whole words). If a key has to name the particle, quote it as a ‹…› mention.
7. **Malaysian forms.** Disallowed teaching forms, matched as whole words and inside hyphenated words: the Stage 1 list plus berbicara, perbaiki, musik, film, olahraga, apotek, kantor, and four the plan names as Indonesian: bersepeda, antre, berwisata, kecelakaan. They are allowed only inside a ‹…› mention whose source in `curriculum/malay-mentions.json` says "do not use"; any other use fails, including other mentions.

## The shared files

- **`curriculum/stage-rules.json`** (version 1). Its `format` key documents every field for Kata-Kata: `affix_gates` (family, chapter, ledger tags, detection, which rule set enforces it), `stage_aware_rule`, `family_resolution`, `shape_tests`, `whole_words` (form, chapter, ledger ID, reason), `ter_superlatives`, `lookalike_roots`, `register_pairs` (spoken, standard, from_chapter, decision), `particles` and `disallowed_forms`. Readers ignore keys they do not know, and nobody edits the file to make content pass.
- **`curriculum/stage-rules-fixtures.json`**: 72 shared cases (each a short list of segments with an expected pass or fail and the check that must fail). `tests/test_stage_rules.py` runs them all; Kata-Kata's guard should run the same file.

## Left for Kata-Kata (build step 3)

1. Read `curriculum/stage-rules.json` (copy it into Kata-Kata or read it from a pinned Cikgu Sensai commit) instead of hard-coded gates and `ALLOW_LIST`.
2. Pass the chapter to the affix guard and scope chunk exemptions by chapter, so a chapter 12 chunk cannot become legal in Stage 1 (plan section 3, item 4; re-read the guard at the current Kata-Kata head first).
3. Run `curriculum/stage-rules-fixtures.json` and agree with Python on every case.
4. When c10 to c18 exist, refresh the Cikgu Sensai snapshot: the checker already loads every pinned chapter file.

## Sam's answers (13 Nov 2026, in chat)

1. **«tidak mengapa» with both spoken forms.** Sam first said «tidak mengapa» is not used in speech (Malaysians say «tak apa», or the slang short form «takpe»), then decided: **teach «tidak mengapa» (spoken: «takpe» / «tak apa») so learners meet all three.** So `curriculum/stage-rules.json` pairs both spoken forms with «tidak mengapa» (see `register_notes`). The «tak apa» pair applies from chapter 10, because Stage 1 unit 5 already shows «tak apa» as Dunia recognition (L-0940, primes chapter 5) and must stay unchanged; «takpe», tak tahan, set and kat apply in every chapter.
2. **Indonesian forms: confirmed** as added (bersepeda, antre, berwisata, kecelakaan) and as left out (saku, darurat, berdagang, berteman, menikah).
3. **Stative ter- words: confirmed.** «terbuka» and the like on their own stay gated at chapter 16 unless Sam approves a whole-word entry.

## Still to do in the ledger (not done here: this step may not edit the ledger)

- **Journal row** for Sam's answer 1.
- **L-1261 «tidak mengapa»** stays the chapter 17 core row; update its meaning cells to name both spoken forms («takpe» / «tak apa»).
- **«takpe»** has no ledger row. Sam's decision makes it a marked spoken form of «tidak mengapa» (chapter 17, unit 17); the ledger session writes the row (or adds it to L-0940) before any content uses it. Until then the checker reports «takpe» as a ledger gap, which blocks a re-authored unit.
