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
- Every error encountered must be recorded in summary.md with the fix applied.

## Mistakes made & fixes (so they aren't repeated)
- **autocrlf hides real file changes**: `git diff` shows nothing even after `write`/`edit` changed content, because CRLF↔LF normalization makes blobs identical. Fix: delete file + recreate with `cat > file << 'EOF'` heredoc, or use Python file writes.
- **`write` tool on Windows**: path resolution can silently fail — file appears updated in `read` but `bash cat` shows old content. Fix: always verify with `python3 -c` read after writing.
- **`read` tool caches differently from shell**: `read` may show newer content while `bash grep/cat` shows stale. Fix: use `python3 -c` for ground truth.
- **Unicode filenames break `read`**: files with Hindi/Unicode chars in names (e.g., RSSB / वनपाल) fail `read` tool. Fix: `glob` to find file, then `cp` to a clean filename.
- **GitHub API needs explicit token**: scripts can't auto-use Windows Credential Manager tokens. Fix: use local git commands (`git add/commit/push`) instead of API calls.
- **Python triple-quoted strings + `\u`**: `\uXXXX` in Python strings triggers Unicode escape. Fix: use raw strings `r'...'` or `cat > file << 'EOF'` heredoc.
- **`sed` regex fails on Windows bash**: special chars in regex patterns break sed. Fix: use Python `str.replace()` or `re.sub()` instead.
- **Python f-strings with backslash**: `f-string.split('Html Questions\')` causes SyntaxError — backslash not allowed in f-string expressions. Fix: use string concatenation or `str.split()` with a variable.
- **Temp files get committed if not excluded**: `git add -A` stages everything including temp files. Fix: always `git rm` temp files before committing, or add to `.gitignore`.
- **`fixed_placeholder.json` files**: empty files created by broken `mkdir` + `write` operations can accumulate in repo. Fix: periodically scan for and remove orphan files.

## Domain knowledge picked up on the job
- Rajasthan exam question JSONs typically have `subject` and `topic` fields with `->` separators (e.g., "राजस्थान की अर्थव्यवस्था -> लघु, कुटीर एवं ग्रामोद्योग").
- Each question has qEnglish, qHindi, optionsEnglish, optionsHindi, correct (0-based index), and optional explanations.
- **For README updates:** gather stats programmatically by scanning `questions/` dir with Python, don't hardcode numbers.
- **ASCII bar charts** work well for GitHub READMEs — use `█` and `░` blocks with percentages.
- **Exam field convention (planned):** add `exam` field to every question, format: `{exam_name} {date}` extracted from filename. Enables source tracing and filtering.
- **Duplicate topic patterns found and merged:**
  - `राजस्थान का इतिहास - X` merged into standalone `X` (keep shorter name)
  - `भारतीय संविधान एवं राजनीतिक व्यवस्था - X` merged into standalone `X`
  - `राजस्थान की राजनीतिक एवं प्रशासनिक व्यवस्था - X` merged into standalone `X`
  - `and` vs `और` vs `und` normalized to `और`
  - Spelling variants (पर्यावरणाय/पर्यावरणीय → पर्यावरण) merged
  - `उच्च न्यायालय` merged into `उच्चतम न्यायालय` (correct term)
- **Future rule: When processing new JSON files, BEFORE saving:**
  1. List all subject/topic combos from the JSON
  2. Compare against existing topics in repo (use `ghListTopics` or scan `questions/` dir)
  3. If a topic name is similar but not identical to an existing one → ASK USER which name to use
  4. Never auto-merge without confirming — the user knows the canonical topic names
