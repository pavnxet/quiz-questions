# 📚 Quiz Questions Bank

A bilingual (English + Hindi) question bank for Rajasthan state exam preparation. Questions are organized by subject and topic in JSON format, ready to be used with [Master Quiz Maker](https://github.com/pavnxet/Master-Quiz-maker).

---

## 📊 Analytics Dashboard

| Metric | Value |
|--------|-------|
| **Total Questions** | **391** |
| **Total Topics** | **121** |
| **Subjects** | **11** |
| **Languages** | English + Hindi (द्विभाषी) |

### Subject-wise Breakdown

| # | विषय (Subject) | Questions | Topics | Coverage |
|---|---------------|-----------|--------|----------|
| 1 | **राजनीति विज्ञान एवं शासन** | 96 | 31 | ████████████████████░░░░░ 24.6% |
| 2 | **इतिहास** | 79 | 13 | ████████████████░░░░░░░░░ 20.2% |
| 3 | **भूगोल** | 66 | 21 | █████████████░░░░░░░░░░░░ 16.9% |
| 4 | **शिक्षा मनोविज्ञान एवं शिक्षण विधियाँ** | 60 | 12 | ████████████░░░░░░░░░░░░░ 15.3% |
| 5 | **अर्थशास्त्र** | 40 | 8 | ████████░░░░░░░░░░░░░░░░░ 10.2% |
| 6 | **सामान्य विज्ञान** | 19 | 15 | ████░░░░░░░░░░░░░░░░░░░░░ 4.9% |
| 7 | **गणित** | 12 | 8 | ██░░░░░░░░░░░░░░░░░░░░░░░ 3.1% |
| 8 | **कृषि एवं पशुपालन** | 8 | 5 | █░░░░░░░░░░░░░░░░░░░░░░░░ 2.0% |
| 9 | **कंप्यूटर और सूचना प्रौद्योगिकी** | 6 | 5 | █░░░░░░░░░░░░░░░░░░░░░░░░ 1.5% |
| 10 | **तार्किक ज्ञान, मानसिक योग्यता** | 4 | 2 | █░░░░░░░░░░░░░░░░░░░░░░░░ 1.0% |
| 11 | **भाषा ज्ञान** | 1 | 1 | ░░░░░░░░░░░░░░░░░░░░░░░░░ 0.3% |

---

## 📁 Repository Structure

```
quiz-questions/
├── questions/                    # 📂 All question files
│   ├── अर्थशास्त्र/              # Economics (8 topics)
│   ├── इतिहास/                   # History (13 topics)
│   ├── कंप्यूटर और सूचना प्रौद्योगिकी/  # Computer & IT (5 topics)
│   ├── कृषि एवं पशुपालन/        # Agriculture & Animal Husbandry (5 topics)
│   ├── गणित/                     # Mathematics (8 topics)
│   ├── तार्किक ज्ञान.../         # Logical Reasoning (2 topics)
│   ├── भाषा ज्ञान/               # Language (1 topic)
│   ├── भूगोल/                    # Geography (21 topics)
│   ├── राजनीति विज्ञान एवं शासन/  # Political Science (31 topics)
│   ├── शिक्षा मनोविज्ञान.../     # Education Psychology (12 topics)
│   └── सामान्य विज्ञान/           # General Science (15 topics)
├── questions-archive/            # 🗄️ Archived questions (pre-cleanup)
├── AGENTS.md                     # 🤖 Agent processing instructions
├── learning.md                   # 📝 Session learnings & conventions
├── summary.md                    # 📋 Session log
└── README.md                     # 📖 This file
```

---

## 📝 Question Format

Each question follows this bilingual JSON structure:

```json
{
  "qEnglish": "What is the capital of Rajasthan?",
  "qHindi": "राजस्थान की राजधानी क्या है?",
  "optionsEnglish": ["Jaipur", "Jodhpur", "Udaipur", "Ajmer"],
  "optionsHindi": ["जयपुर", "जोधपुर", "उदयपुर", "अजमेर"],
  "correct": 0,
  "explanationEnglish": "Jaipur is the capital and largest city of Rajasthan.",
  "explanationHindi": "जयपुर राजस्थान की राजधानी और सबसे बड़ा शहर है।",
  "subject": "भूगोल",
  "topic": "राजस्थान का भूगोल"
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `qEnglish` | At least one | Question text in English |
| `qHindi` | At least one | Question text in Hindi (Devanagari) |
| `optionsEnglish` | Yes | 2-6 answer choices in English |
| `optionsHindi` | Yes | 2-6 answer choices in Hindi |
| `correct` | Yes | Zero-based index of correct answer |
| `subject` | No | Subject name (e.g., "भूगोल") |
| `topic` | No | Topic name (e.g., "राजस्थान का भूगोल") |
| `explanationEnglish` | No | Explanation shown after answer |
| `explanationHindi` | No | Explanation in Hindi |

---

## 🚀 Usage

### With Master Quiz Maker

1. Clone this repo or use the GitHub API
2. Set `GITHUB_REPO=pavnxet/quiz-questions` in your quiz maker config
3. Upload questions via web UI or Telegram bot
4. Questions are automatically organized by subject/topic

### Direct API Access

```bash
# Browse all topics
curl https://api.github.com/repos/pavnxet/quiz-questions/git/trees/main?recursive=1

# Download specific topic
curl https://raw.githubusercontent.com/pavnxet/quiz-questions/main/questions/भूगोल/राजस्थान का भूगोल.json
```

---

## 📈 Question Distribution by Subject

```
राजनीति विज्ञान एवं शासन  ████████████████████████████████████████  96 (24.6%)
इतिहास                    ██████████████████████████████████░░░░░░  79 (20.2%)
भूगोल                     ████████████████████████████░░░░░░░░░░░░  66 (16.9%)
शिक्षा मनोविज्ञान...      █████████████████████████░░░░░░░░░░░░░░  60 (15.3%)
अर्थशास्त्र               ████████████████░░░░░░░░░░░░░░░░░░░░░░  40 (10.2%)
सामान्य विज्ञान            ███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  19 ( 4.9%)
गणित                      █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  12 ( 3.1%)
कृषि एवं पशुपालन         ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   8 ( 2.0%)
कंप्यूटर...               ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   6 ( 1.5%)
तार्किक ज्ञान...          █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   4 ( 1.0%)
भाषा ज्ञान                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   1 ( 0.3%)
```

---

## 🏷️ Tags

`rajasthan` `rpsc` `rsmssb` `ldc` `grade-2` `preliminary` `general-knowledge` `bilingual` `hindi` `english` `quiz` `exam-preparation`

---

## 📜 License

This question bank is open for educational use. Questions are sourced from various Rajasthan state exam papers.

---

## 🤝 Contributing

1. Fork the repository
2. Add questions in the specified JSON format
3. Place files in `questions/{subject}/{topic}.json`
4. Submit a pull request

### Guidelines

- Maintain bilingual format (English + Hindi)
- Use consistent subject/topic naming
- Include explanations when possible
- Follow the existing JSON structure

---

## 📊 Last Updated

**391 questions** across **121 topics** in **11 subjects**

*Data as of July 2026*
