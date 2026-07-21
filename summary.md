# Session Summaries

Append one entry per session, newest at the bottom. Keep each entry short — 5–10 lines.
Do not edit past entries. This is a log, not a knowledge base (see learning.md for that).

Template:

```
## YYYY-MM-DD HH:MM — <one-line task title>
- Task: what was asked
- Did: what was actually done (files touched, decisions made)
- Result: outcome — done / partially done / blocked, and why
- Open: anything left unfinished or worth picking up next session
```

---

## 2026-07-14 10:05 — Example entry (delete once real entries exist)
- Task: Set up the agent memory system itself
- Did: Created AGENTS.md, summary.md, learning.md and a Stop hook to enforce updates
- Result: Done. Hook tested and blocks correctly if summary.md isn't touched.
- Open: None

## 2026-07-21 23:30 — Process RSSB Vanpal Preliminary 2026-06-28 questions
- Task: Process JSON file with 100 questions, push to quiz-questions repo
- Did: Read temp_input.json, grouped 100 questions into 72 topics across 10 subjects. Used local git operations (no GitHub API) since Windows Credential Manager handles auth. safeName strips `->` from topic names. 35 topics updated, 54 skipped (already existed), 0 failed. Committed and pushed to main.
- Errors encountered & fixes:
  1. `read` tool failed on JSON file with Unicode chars in filename (RSSB / वनपाल / etc.) → used `glob` to find file, then `cp` via Python to a clean filename
  2. GitHub API approach failed — no token available directly → discovered git uses Windows Credential Manager (`credential.helper=manager`), switched to local file writes + `git push`
  3. `write` tool on Windows didn't persist utils.js changes (safeName fix) → confirmed via `read` that write DID work, but `bash grep` showed stale cache; used heredoc to rewrite files cleanly
  4. `edit` tool reported file had correct content while `bash` showed old content → read tool cached differently than shell; verified with `python3 -c` reads
  5. Python heredoc had Unicode escape errors (`\u` in triple-quoted strings) → rewrote files with `cat > file << 'EOF'` heredoc instead
  6. `sed` commands failed due to regex escaping on Windows bash → used Python for string replacements instead
  7. `git add` didn't track utils.js/github.js due to autocrlf line-ending normalization → used `rm` + `cat >` to force-create fresh files, then `git add -A`
- Result: Done. 39 files changed, 3501 insertions. Push successful. Post-processing files updated.
- Open: None

## 2026-07-21 23:45 — Update AGENTS.md with processing workflow
- Task: Update AGENTS.md with JSON processing workflow, working directory, and error logging rules
- Did: Added "Processing workflow" section with step-by-step instructions, key rules (local git, safeName, never stop on error). Added "Record every error encountered" to post-processing rules.
- Result: Done. Pushed to main.
- Open: None

## 2026-07-22 00:30 — Merge duplicate topics across repo
- Task: Find and merge duplicate/similar topic names in the question bank
- Did: Scanned all 155 topic files across 10 subjects. Found 36 duplicate pairs caused by: prefix variations (राजस्थान का इतिहास - X vs X), spelling variants (and/और/und), spelling errors (पर्यावरणाय/पर्यावरणीय), and subtopic vs standalone naming. Merged 50 questions into canonical topics, deleted 36 duplicate files. Updated learning.md with merge patterns and future duplicate detection rules.
- Errors encountered & fixes:
  1. Python heredoc truncated due to Unicode in f-strings → rewrote as single-line `-c` script
- Result: Done. 62 files changed. Push successful. Repo now has 119 topic files (down from 155).
- Open: None

## 2026-07-22 00:15 — Process 3 RPSC 2nd Grade Paper-I (GK) files
- Task: Process 3 JSON files (2026-07-13, 07-14, 07-16) with 100 questions each, push to quiz-questions repo
- Did: Used `glob` to find files (Unicode filenames), `cp` to copy with clean names, Python to analyze and process. Merged 300 questions into 88 topics. Used local git for push.
- Errors encountered & fixes:
  1. `glob` pattern with backslash in Python string caused SyntaxWarning → used raw strings `r'...'`
  2. Python `f-string` with backslash in split caused SyntaxError → used string concatenation instead
  3. Temp files got committed to git before cleanup → added `git rm --cached` + `git rm` for temp files in same commit
  4. `fixed_placeholder.json` files appeared in repo (likely from earlier broken writes) → found and removed with `find ... -exec git rm`
- Result: Done. 91 files changed, 14211 insertions. Push successful. Post-processing files updated.
- Open: None
