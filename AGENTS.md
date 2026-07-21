# Agent Instructions

## Memory system (read this every session)

This project has a persistent memory system. Two files carry knowledge across sessions:

- **`learning.md`** — distilled lessons, gotchas, conventions, and preferences learned from past work.
  **Read this in full at the start of every session, before doing anything else.**
- **`summary.md`** — a running log of what happened in each session. Skim the last 3–5 entries for recent context; don't read the whole file unless you need history.

### At the START of a session
1. Read `learning.md` fully. Treat it as binding context — it encodes hard-won corrections, not suggestions.
2. Skim the last few entries of `summary.md` for recent momentum (what was in progress, what's still open).

### At the END of a session (non-negotiable — do this before stopping)
1. Append a new entry to `summary.md` using the template at the top of that file. One entry, dated, concise.
2. Review what happened this session. If anything is worth generalizing — a mistake you made and fixed, a pattern that worked, a user preference, a fact about this codebase/environment you didn't know before — merge it into `learning.md`:
   - **New fact** → add it under the right category.
   - **Fact that updates/contradicts an old one** → edit the old line in place, don't just append a contradiction. `learning.md` must never contain two conflicting entries on the same topic.
   - **Nothing new learned** → it's fine to skip a `learning.md` edit. Don't pad it with trivia to look productive.
3. If `learning.md` is getting long (>150 lines) or has near-duplicate entries, consolidate/prune before finishing.

Do not end a session without touching `summary.md`. This step is enforced by a Stop hook — if you skip it, the session will be blocked from ending and you'll be told to complete it.
