import sqlite3

conn = sqlite3.connect("arvo.db")
cursor = conn.cursor()

cursor.execute("""SELECT localId, crash_output, patch_url, crash_analysis FROM arvo WHERE project = 'libxml2'
      AND crash_type IS NOT NULL
      AND crash_output IS NOT NULL
    LIMIT 10""")
rows = cursor.fetchall()
conn.close()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Crash Table</title>
    <style>
        table { border-collapse: collapse; width: 100%; margin: 20px auto; table-layout: fixed; }
        th { border: 1px solid #ccc; padding: 8px; text-align: center; background-color: #f2f2f2; }
        td { border: 1px solid #ccc; padding: 8px; text-align: left; vertical-align: top;  word-wrap: break-word; white-space: pre-wrap;}
        h1 { text-align: center; }
    </style>
</head>
<body>
<h1>Crash Analysis Results</h1>
<table>
<tr>
  <th style="width:5%;">Local ID</th>
  <th style="width:40%;">Crash Output</th>
  <th style="width:20%;">Patch URL</th>
  <th style="width:35%;">API Result</th>
</tr>

"""

for localId, crash_output, patch_url, crash_analysis in rows:
    html += f"<tr><td>{localId}</td><td>{crash_output}</td><td>{patch_url}</td><td>{crash_analysis}</td></tr>"

html += """
</table>
</body>
</html>
"""

with open("result.html", "w") as f:
    f.write(html)
