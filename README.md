# 🧠 Crash Analysis Pipeline for `libxml2` (SQLite + GPT + HTML)

This project analyzes crash data from the `libxml2` fuzzing reports stored in a SQLite database (`arvo.db`), uses GPT to explain each crash, and generates an HTML report summarizing the results.

---

## 📁 Files Overview

| File              | Purpose                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `make_new_col.py` | Adds a `crash_analysis` column to `arvo` table and populates it via GPT |
| `generate_results.py` | Generates `result.html` to summarize crashes and AI explanations |
| `result.html`     | Final visual report of analyzed crash entries                          |

---

## 🛠️ Requirements

- Python 3.7+
- `openai` package
- `arvo.db` SQLite database with `libxml2` crash records

Install dependencies:
```bash
pip install openai
```

---

## 🔑 Setup

1. **API Key**:  
   Replace the placeholder in `make_new_col.py` with your actual OpenAI key:
   ```python
   client = OpenAI(api_key="your_openai_api_key_here")
   ```

2. **Database File**:  
   Ensure `arvo.db` is in the same directory as the scripts and contains a table `arvo` with columns:
   - `localId`
   - `project`
   - `crash_type`
   - `crash_output`
   - `patch_url` (optional)

---

## 🚀 Usage

### 1. Analyze Crashes
Run GPT to generate explanations for `libxml2` crashes:
```bash
python make_new_col.py
```

This will:
- Create a `crash_analysis` column if it doesn't exist
- Analyze up to 10 crash logs using GPT
- Save explanations into the database

### 2. Generate Report
Create a styled HTML summary:
```bash
python generate_results.py
```

This produces `result.html`, a formatted table with:
- Local ID
- Crash output (truncated for readability)
- Patch URL
- GPT-generated analysis

---

## 📄 Example Output

Open `result.html` in your browser to view a full summary table like this:

| Local ID | Crash Output | Patch URL | GPT Crash Analysis |
|----------|--------------|-----------|---------------------|
| 42470114 | ...          | https://... | 1. Explanation...   |

---

## ⚠️ Notes

- Crash data is filtered to only include rows where:
  - `project = 'libxml2'`
  - `crash_type` and `crash_output` are **not NULL**

- You can adjust the `LIMIT 10` clause in both scripts to process more rows.

---

## 📬 Contact

For questions, reach out to the project author or file an issue.
