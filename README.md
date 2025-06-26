
# Crash Analysis Automation with GPT

This project analyzes crash logs from a SQLite database using OpenAI's GPT model and generates an HTML report summarizing the results. It is intended for use on crash data (e.g., from the `libxml2` project) to assist in security analysis and triage.

## 📁 Files

### `make_new_col.py`
- Connects to `arvo.db` SQLite database.
- Adds a new column `crash_analysis` to the `arvo` table if it does not exist.
- Fetches up to 10 crash records for the `libxml2` project with non-null `crash_type` and `crash_output`.
- Sends crash data to GPT-4 (`gpt-4-1106-preview`) for analysis.
- Updates the `crash_analysis` column with the AI-generated response.

### `generate_results.py`
- Reads the same 10 records from the `arvo` table.
- Generates a styled HTML file `result.html` that displays:
  - Crash ID
  - Crash output
  - Patch URL (if available)
  - GPT-generated crash analysis

## 🧰 Requirements

- Python 3.7+
- `openai` Python package
- SQLite3

Install dependencies with:

```bash
pip install openai
```

## 🔑 Setup

Replace the placeholder API key in `make_new_col.py`:

```python
client = OpenAI(api_key="YOUR_API_KEY")
```

## 🚀 Usage

1. Run the crash analysis script:
   ```bash
   python make_new_col.py
   ```

2. Generate the HTML report:
   ```bash
   python generate_results.py
   ```

3. Open `result.html` in a browser to view the results.

## ⚠️ Notes

- Be sure to replace the API key and validate that `arvo.db` exists in your working directory.
- The `LIMIT 10` clause can be adjusted for batch sizes or removed for full analysis (not recommended for large datasets without batching).

## 📄 License

MIT License (or specify your license)
