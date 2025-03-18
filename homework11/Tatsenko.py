import sqlite3

conn = sqlite3.connect("Matvii.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Staff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    salary INTEGER
)
''')

conn.commit()
conn.close()
