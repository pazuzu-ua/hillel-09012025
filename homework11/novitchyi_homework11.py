import sqlite3

conn = sqlite3.connect("pc_cases.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    form_factor TEXT NOT NULL,
    color TEXT NOT NULL
);
""")

conn.commit()
conn.close()