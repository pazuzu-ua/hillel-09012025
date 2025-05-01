import sqlite3



def init_db():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cats (
            i_cat INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_year INTEGER,
            years INTEGER,
            owner TEXT
            );
        ''')