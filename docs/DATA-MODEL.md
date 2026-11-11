# Step 2 model contract

`catalogue.py` generates `dist/catalogue.js`. Its data is metadata around the
existing bank; source page text is never rewritten. `chapter_id` and `unit_id`
are null for unplaced supplementary material. Future chapter 12 is inactive.
Source titles remain the legacy identity; component IDs combine placement, type
and a stable title hash. Renaming a source therefore requires an explicit ID
migration. Duplicate placements of the same source are separate extracts.

## Two layers

`scenes` contains neutral situation titles and draft can-do goals drawn from the
pinned Kata-Kata scenarios and charter. Task/change/listening/reading/test shapes
are explicit nulls or empty arrays until authored. No cross-language scene
alignment is inferred. `language_layers` owns grammar sequence, word IDs,
pattern IDs, first-language notes, scene/chapter mappings and hour budget.
English and Japanese legacy packs remain supplementary. No new language course
or external textbook alignment is asserted.

## Chapters and components

Nine Stage 1 records hold IDs, draft charter can-do goals, all original Kata-Kata
word and frame IDs, grammar points, recycle scheduling, units and block plans.
There are 65 unit blocks plus nine review/skills blocks. Per-block goals and
actual recycled word selections await pilot authoring; proposed pattern-return
destinations follow next chapter, three chapters later, stage review.

143 component slots represent 13 units × 11 types, separately from the 216
extractable placements. A populated slot is partial, not a complete suite.
Every component has language, level, chapter/unit, component type, subtype,
skills, genre, grammar points, time_minutes, prerequisites (chapters, grammar
points, word IDs), course_path, external_textbook_links and review_status.
`null` means unverified, not zero time. An empty prerequisite list is currently
unmapped, not a claim of no prerequisites. Existing material is assigned to
`full`; fast summary packs have not been authored. All review statuses are draft.
Grammar mappings are provisional family-level labels, not validated coverage.
Word links use exact surface matching against chapter cards; ambiguity and
unmatched text remain in the audit. These links are not a ledger compliance check.

Extracted components carry their source explainers and original source key;
keys can include answers to other source sections and are labelled accordingly
in the picker. New component-specific keys belong with later content work.
PDF and Word exports add a language/level/chapter-or-unit/type/time header.
Original full packs remain selectable. Combined tag filters and selections
across chapters use the same component records.

## Test items

`curriculum/test-items.json` is deliberately empty: there are no existing chapter
tests. Guided practice has not been relabelled as testing. When authored, each
item must provide:

- `id`, `chapter_id`, `component_id` referencing its Test component;
- `sub_type`: words, grammar, listening, reading or speaking;
- `grammar_points` and `word_ids`: arrays of IDs actually tested, not incidental
  prompt vocabulary; at least one array must be non-empty;
- `prompt`, `answer_key`, `review_status`.

`validate_test_item` rejects missing fields, unknown grammar/word IDs, invalid
subtypes/status and mismatched chapter/component references. This is structural
validation, not step 3 language enforcement. `prerequisite_items` intersects
requested IDs with test-item tags inside the required chapters. Fixture tests
verify matching and exclusion. There are no real items to assemble today; the
interface explains this when prerequisites are requested. Future authoring must
supply real prerequisite mappings, tests and their independent keys.

## Reference integrity and roots

The nine JSON files and ledger CSV are byte-identical upstream snapshots at the
revision in `docs/restructure-sources.json`. No reference repository is edited.
`curriculum/malay-roots.json` records Sam's five root classifications. The audit
uses these classifications without adding terms to the ledger or enabling the
step 3 affix guard.
