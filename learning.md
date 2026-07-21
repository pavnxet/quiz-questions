# Learnings

Curated knowledge, not a log. Read fully at the start of every session.
Rules for editing this file:
- One fact per line, under the right category.
- If a new fact updates or contradicts an old line, EDIT the old line — never leave two conflicting entries.
- Keep entries short and generalizable ("prefer X over Y because Z"), not session-specific narration.
- Prune anything that stops being useful (project finished, preference changed, etc).
- If this file exceeds ~150 lines, consolidate before adding more.

---

## Environment / Setup
- Git auth uses Windows Credential Manager (`credential.helper=manager`) — no token needed in scripts, just use `git push` directly.
- Repo at `E:\study\Quiz-questions` is the working copy for processing.

## Codebase conventions
- Questions live in `questions/{subject}/{topic}.json` — each file is a JSON array of question objects.
- `safeName()` strips `/\:*?"<>|#%` and normalizes `->` to space — topic names must be filesystem-safe.
- Dedup key = normalized qEnglish + qHindi (lowercased, whitespace-collapsed).

## User preferences
- User prefers local git operations over GitHub API calls — simpler, no token management.
- Post-processing (summary.md + learning.md) is mandatory after every session.

## Mistakes made & fixes (so they aren't repeated)
- GitHub API calls failed silently due to autocrlf line-ending normalization — git saw files as unchanged even when content differed. Fix: use local file writes + `git add/commit/push` instead of GitHub Contents API.
- `write` tool on Windows sometimes doesn't persist due to path resolution issues — use heredoc or Python file writes for reliability.

## Domain knowledge picked up on the job
- Rajasthan exam question JSONs typically have `subject` and `topic` fields with `->` separators (e.g., "राजस्थान की अर्थव्यवस्था -> लघु, कुटीर एवं ग्रामोद्योग").
- Each question has qEnglish, qHindi, optionsEnglish, optionsHindi, correct (0-based index), and optional explanations.
