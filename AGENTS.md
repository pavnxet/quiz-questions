# Agent Instructions

> **FIRST RULE — READ THIS BEFORE DOING ANYTHING ELSE:**
> 1. Read `learning.md` in full — it contains hard-won corrections and conventions.
> 2. Skim last 3–5 entries of `summary.md` — recent context and open items.
> Do NOT process any files until both are read. This is non-negotiable.

## Memory system

Two files carry knowledge across sessions:

- **`learning.md`** — distilled lessons, gotchas, conventions, preferences. **Read fully at session start.**
- **`summary.md`** — running log of each session. Skim recent entries for context.

### At START of session
1. Read `learning.md` fully — treat as binding context, not suggestions.
2. Skim last few entries of `summary.md` — what was in progress, what's open.

### At END of session (non-negotiable)
1. Append entry to `summary.md` — dated, concise, **record every error + fix**.
2. Update `learning.md` — add new patterns, edit contradictions in-place.
3. If `learning.md` > 150 lines, consolidate/prune.

## Processing workflow

When asked to process a JSON quiz file:

1. **Read** the JSON file (use `glob` if filename has Unicode/special chars, then `cp` to clean name)
2. **Analyze** — count questions, list subject/topic combos
3. **Process** — for each subject/topic:
   - Read existing `questions/{subject}/{topic}.json` (if exists)
   - Dedup by normalized qEnglish + qHindi
   - Merge new questions, write back
4. **Push** — `git add -A && git commit && git push origin main`
5. **Post-process** (mandatory):
   - Append session entry to `summary.md` (include ALL errors + fixes)
   - Update `learning.md` with new patterns/learnings

### Working directory
`E:\study\Quiz-questions` — already cloned, has git credentials via Windows Credential Manager.

### Key rules
- Use **local git commands** for push (not GitHub API) — Windows Credential Manager handles auth
- Use `safeName()` logic: strip `/\:*?"<>|#%`, normalize `->` to space
- Never stop on error — log it and continue to next topic
- Always clean up temp files after processing
