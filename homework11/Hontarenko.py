import sqlite3

with sqlite3.connect('database.db') as connection:
    connection.execute('PRAGMA foreign_keys=1')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cars(
    i_car INTEGER PRIMARY KEY AUTOINCREMENT,
    colour TEXT NOT NULL,
    make TEXT NOT NULL,
    price INTEGER NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Car_owners(
    i_owner INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER NOT NULL CHECK( age>17),
    i_car INTEGER,
    FOREIGN KEY (i_car) REFERENCES Cars(i_car)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Car_additional_details(
    i_detail INTEGER PRIMARY KEY AUTOINCREMENT,
    condition TEXT NOT NULL,
    registration_date INTEGER NOT NULL,
    features TEXT NOT NULL,
    i_car INTEGER,
    FOREIGN KEY (i_car) REFERENCES Cars(i_car)
    );
    """)
