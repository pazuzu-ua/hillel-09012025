import sqlite3

with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('DROP TABLE IF EXISTS Cars')

cursor.execute('''
    CREATE TABLE Cars(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER CHECK (year > 0),
        exhaust_system TEXT NOT NULL
    )
''')

cars = [
    ('Toyota', 'supra', 'Armytrix', '2018'),
    ('BMW', 'm4 competition', 'Acrapovich', '2020'),
    ('Mercedes', 'G class', 'Capristo', '2023'),
    ('Dodge', 'Challenger Demon', 'Dawnpipe', '2019')
]
cursor.executemany('INSERT INTO Cars (brand, model, year, exhaust_system) VALUES (?, ?, ?, ?)', cars)

cursor.execute(' SELECT * FROM Cars;')
result = cursor.fetchall()
print(result)