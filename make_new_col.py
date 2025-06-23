import sqlite3
from openai import OpenAI

# 🔐 Set your OpenAI API key
client = OpenAI(api_key="KEY")  # Replace this with your actual key

# 📂 Connect to the arvo.db
conn = sqlite3.connect("arvo.db")
cursor = conn.cursor()

# ➕ Create the column if it doesn't exist
try:
    cursor.execute("ALTER TABLE arvo ADD COLUMN crash_analysis TEXT")
except sqlite3.OperationalError:
    pass  # Column already exists

# 🔍 Fetch ALL libxml2 rows with crash info (no filtering on crash_analysis)
cursor.execute("""
    SELECT localId, crash_type, crash_output
    FROM arvo
    WHERE project = 'libxml2'
      AND crash_type IS NOT NULL
      AND crash_output IS NOT NULL
    LIMIT 10
""")
rows = cursor.fetchall()

# 🤖 GPT call using full crash output (no truncation)
def analyze_crash(crash_type, crash_output):
    prompt = f"""
Crash Type: {crash_type}

Crash Output: {crash_output}

Please:
1. Explain what this crash suggests about the vulnerability.
2. Infer which code behavior or function might be responsible.
3. Suggest a likely fix or defensive coding technique.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a C/C++ security expert analyzing crash logs."},
                {"role": "user", "content": prompt.strip()}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# 💾 Loop and overwrite crash_analysis
for row_id, crash_type, crash_output in rows:
    print(f"Re-analyzing crash ID {row_id}...")
    analysis = analyze_crash(crash_type, crash_output)
    print(f"→ GPT Response (first 200 chars):\n{analysis[:200]}...\n")
    cursor.execute("""
        UPDATE arvo
        SET crash_analysis = ?
        WHERE localId = ?
    """, (analysis, row_id))

# ✅ Save and close
conn.commit()
conn.close()
print("✅ All selected rows have been overwritten with new GPT analysis.")
