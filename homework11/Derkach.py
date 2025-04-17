import sqlite3

with sqlite3.connect('Keyboard.db') as connection:
    connection.execute('PRAGMA foreign_keys = 1')

    cursor = connection.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS  Keyboard( 
            keyboards INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            model TEXT NOT NULL,
        );
     """)

    cursor.execute("""
        INSERT INTO Keyboard(name, color, model)
        VALUES
           ('AULA','white','F75'),
           ('FREEWOLF','orange','M96');
    """)