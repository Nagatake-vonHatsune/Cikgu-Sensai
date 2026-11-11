# Instructions for any AI builder working on Cikgu Sensai

This repository may be worked on by ChatGPT or Claude, one at a time. These rules apply to both. `CLAUDE.md` points here.

## Start of every session

1. Read the governing charter, the [Unified Curriculum Charter](https://docs.google.com/document/d/1d-uiYfQixReMUlPAcUEJ6R4onWOh-4Aa9urr14DL2lw). It is a living Google Doc; read the current version, not a copy. It is read-only to builders: propose changes to Sam in your report.
2. Read `HANDOFF.md` in this repository. It says which step is in progress, what is done, what is next and what is still open.
3. Read the latest `docs/STEP-*-REPORT.md`.
4. Run `git pull` and confirm you are at the commit `HANDOFF.md` names. If not, read the commits in between before doing anything.

## Sources of truth

| What | Where |
| --- | --- |
| Curriculum, rules, work order | The charter (Google Doc above), especially sections 6, 8, 12, 13 and 14 |
| Malay vocabulary and chapter placement | The Malay ledger Google Sheet in the Language Teaching System Drive folder (Ledger and Journal tabs) |
| Agreed Malay words and sentence patterns per chapter | `curriculum/reference/katakata/` (a snapshot of the Kata-Kata repository) |
| Current state of the work | `HANDOFF.md` and `docs/STEP-*-REPORT.md` |

If you cannot open Google Drive, use the dated copies in `docs/handoff/`: `charter-snapshot.md` and `ledger-snapshot.csv`. The Google versions win whenever you can read them. Whoever has Drive access refreshes the copies at a handover.

A decision made only in a chat does not count. If Sam decides something, it goes into the charter, the ledger or `HANDOFF.md` before the session ends.

## Rules

- Work only on the step `HANDOFF.md` names, and stop at the charter's stop points for Sam's approval.
- All Malay is Malaysian standard as in Kamus Dewan, never Indonesian. Standard forms first; spoken forms marked.
- Never add a word to the ledger or the reference snapshot without Sam's approval recorded in the ledger Journal.
- `curriculum/legacy-exceptions.json` may only shrink. Never regenerate it from current content.
- Free, offline, no accounts, no analytics, no learner records, no runtime services.
- All Japanese is a draft until a native speaker reviews it. Mark it so.
- Meet the content minimums in charter section 6. A component below its minimum is not done.

## Before every push

1. `python build.py` passes (it runs the language checks and the PDF overflow checks).
2. `python -m unittest discover -s tests -v` passes.
3. Use a full Git checkout (not shallow) when the build checks run, because the exception check reads Git history.
4. `git fetch origin main` and rebase if `main` has moved. Push to `main` (Cloudflare deploys it).

## End of every session

Update `HANDOFF.md` before your last push, even if the step is unfinished: what you did, the last commit, what is half-done and where, the next action, and open questions for Sam. The next builder may be a different AI with no access to your conversation.
