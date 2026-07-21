# Plan: Embed Exam Name in Question JSON

## Goal
Add an `exam` field to every question in the repo so each question can be traced back to its source exam paper.

## Current State
- Questions have: qEnglish, qHindi, optionsEnglish, optionsHindi, correct, explanation*, subject, topic
- **No exam/source tracking** — questions from different exams look identical
- When processing, exam name is visible in the filename but lost after saving

## What Changes

### 1. Add `exam` field to question JSON format
```json
{
  "qEnglish": "...",
  "qHindi": "...",
  "exam": "RSSB वनपाल Preliminary 2026-06-28",
  ...existing fields...
}
```

### 2. Processing workflow update (in AGENTS.md)
When processing a JSON file:
1. Extract exam name from filename (e.g., `2026-06-28 RSSB वनपाल Preliminary.json` → `RSSB वनपाल Preliminary 2026-06-28`)
2. Add `exam` field to every question before saving
3. Commit with exam name in message

### 3. Filename → Exam Name mapping
| Filename pattern | Exam name |
|-----------------|-----------|
| `2026-06-28 RSSB वनपाल Preliminary` | `RSSB वनपाल Preliminary 2026-06-28` |
| `2026-07-13 RPSC 2nd Grade Paper-I (GK)` | `RPSC 2nd Grade Paper-I (GK) 2026-07-13` |

Formula: `{exam_name} {date}` — clean, sortable, searchable.

### 4. Retroactive update (optional)
- Scan all existing questions in repo
- Questions without `exam` field → leave as-is or mark as `"exam": "unknown"`
- Only new uploads get the exam field

## Files to Modify
- `AGENTS.md` — add exam extraction step to processing workflow
- `learning.md` — add exam field convention
- Processing script (inline Python) — add exam field injection

## Verification
1. Process a test file → verify `exam` field appears in saved JSON
2. Check repo via GitHub API → confirm exam field in question objects
3. Run `grep` for `exam` field across repo → count questions with/without
