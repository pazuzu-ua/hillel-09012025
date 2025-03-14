
import sqlite3

def create_scooter_table():
    conn = sqlite3.connect('scooters.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Scooters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        color TEXT NOT NULL,
        wheel_size INTEGER NOT NULL
    );
    ''')


create_scooter_table()