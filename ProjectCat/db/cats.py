import sqlite3
from sqlite3.dbapi2 import paramstyle


def add_cat(name: str, birth_year: int, years: int, owner: str):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Cats (name, birth_year, years, owner)
                VALUES (?, ?, ?,?);
        ''',(name, birth_year, years, owner))
