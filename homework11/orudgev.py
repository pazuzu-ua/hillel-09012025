import sqlite3

with sqlite3.connect('cat.db') as connection:
    connection.execute('PRAGMA foreign_keys = 1')

    cursor = connection.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Cats( 
            i_cat INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            breed TEXT NOT NULL, 
            age INTEGER NOT NULL CHECK (age > 0)

        );
     """)

    cursor.execute("""
        INSERT INTO Cats(name, color, breed, age)
        VALUES
           ('Shilka','grey','беспородная', 4),
           ('Dymka', 'black', 'Норвежская лесная', 5);
    """)


