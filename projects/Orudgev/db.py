import sqlite3

from schema import ParrotUpdate

DB_NAME = "data.db"

def init_db():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Parrots (
            i_parrot INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            age INTEGER
        );
        """)

def create_parrot(name, color, age):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Parrots (name, color, age) VALUES (?, ?, ?)', (name, color, age)
        )
        connection.commit()
        return cursor.lastrowid

def get_list_of_parrots():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM Parrots
        """)
        parrots_list = cursor.fetchall()
        return parrots_list

def get_parrot_info(parrot_id: int):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM Parrots WHERE i_parrot = ?, (parrot_id,)
        """)
        parrot_info = cursor.fetchone()
        return parrot_info

def delete_parrot(parrot_id: int):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Parrots WHERE i_parrot = ? ", (parrot_id,))
        return True

def update_parrot_info(parrot_id: int, parrot_info: ParrotUpdate):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Parrots SET name = ?, color = ?, age = ? WHERE i_parrot = ?",
            (parrot_info.name, parrot_info.color, parrot_info.age, parrot_id)
        )
        return True