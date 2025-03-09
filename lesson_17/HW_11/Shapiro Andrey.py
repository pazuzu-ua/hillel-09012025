import sqlite3

with sqlite3.connect('cars.db') as connection:
    cur = connection.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS cars (
    vin TEXT NOT NULL UNIQUE PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    type TEXT NOT NULL,
    color TEXT NOT NULL,
    year INTEGER NOT NULL CHECK (year >= 1980),
    price REAL NOT NULL CHECK (price >= 0 AND price <= 100000)
    );
    ''')
