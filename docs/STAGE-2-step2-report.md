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
5. **Register (R3).** New pairs: tidak mengapa / tak apa, tidak tahan / tak tahan, setuju / set, di / kat (seperti itu / macam tu, ini / ni and itu / tu were already checked). As before, a spoken form fails unless its standard form was taught earlier and the spoken form was taught with a "spoken" label.
6. **Particles (R4).** «lah» and «kan» may appear in prompts and listening once placed (chapter 17), but a test answer key that contains them fails («lah» on its own or as an ending, «kan» on its own; «adalah» and «masalah» are whole words). If a key has to name the particle, quote it as a ‹…› mention.
7. **Malaysian forms.** Disallowed teaching forms, matched as whole words and inside hyphenated words: the Stage 1 list plus berbicara, perbaiki, musik, film, olahraga, apotek, kantor, and four the plan names as Indonesian: bersepeda, antre, berwisata, kecelakaan. They are allowed only inside a ‹…› mention whose source in `curriculum/malay-mentions.json` says "do not use"; any other use fails, including other mentions.

## The shared files

- **`curriculum/stage-rules.json`** (version 1). Its `format` key documents every field for Kata-Kata: `affix_gates` (family, chapter, ledger tags, detection, which rule set enforces it), `stage_aware_rule`, `family_resolution`, `shape_tests`, `whole_words` (form, chapter, ledger ID, reason), `ter_superlatives`, `lookalike_roots`, `register_pairs` (spoken, standard, from_chapter, decision), `particles` and `disallowed_forms`. Readers ignore keys they do not know, and nobody edits the file to make content pass.
- **`curriculum/stage-rules-fixtures.json`**: 69 shared cases (each a short list of segments with an expected pass or fail and the check that must fail). `tests/test_stage_rules.py` runs them all; Kata-Kata's guard should run the same file.

## Left for Kata-Kata (build step 3)

1. Read `curriculum/stage-rules.json` (copy it into Kata-Kata or read it from a pinned Cikgu Sensai commit) instead of hard-coded gates and `ALLOW_LIST`.
2. Pass the chapter to the affix guard and scope chunk exemptions by chapter, so a chapter 12 chunk cannot become legal in Stage 1 (plan section 3, item 4; re-read the guard at the current Kata-Kata head first).
3. Run `curriculum/stage-rules-fixtures.json` and agree with Python on every case.
4. When c10 to c18 exist, refresh the Cikgu Sensai snapshot: the checker already loads every pinned chapter file.

## For Sam to confirm

1. **«tak apa» in Stage 1.** Unit 5 already shows «tak apa» (L-0940, a Dunia recognition word, primes chapter 5), long before «tidak mengapa» (L-1261, chapter 17). To keep Stage 1 passing unchanged, the four new R3 pairs apply from chapter 10. In Stage 2 «tak apa» therefore needs «tidak mengapa» first (chapter 17). Is that what you want, or should unit 5 change?
2. **Indonesian forms.** I added bersepeda, antre, berwisata and kecelakaan from the plan's word tables. I did **not** add saku, darurat, berdagang, berteman or menikah, which the plan also calls Indonesian but which are also used in Malaysian Malay (for example «wang saku»). [UNVERIFIED against Kamus Dewan; part of the end-of-project check.]
3. **Stative ter- words.** The checker treats every ter- word except the four superlatives as the chapter 16 accident family. «terbuka», «tertutup» or «termasuk» on their own would need a whole-word entry (your approval) before chapter 16. «rumah terbuka» is unaffected.
