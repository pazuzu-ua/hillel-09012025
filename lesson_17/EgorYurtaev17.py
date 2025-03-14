import sqlite3

with sqlite3.connect('guitars.db') as connection:

    connection.execute('PRAGMA foreign_keys = 1')

    cursor = connection.cursor()

    # Створення таблиці Guitars
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Guitars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            string_count INTEGER NOT NULL CHECK (string_count > 0)
        );
    """)