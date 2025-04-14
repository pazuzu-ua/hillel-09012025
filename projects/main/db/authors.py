import sqlite3


def add_author( name: str, birth_year: int ):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Authors (name, birth_year)
              VALUES (?, ?);
        ''', (name, birth_year))
