import sqlite3

def init_db():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Anime (
                i_anime INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                description TEXT NOT NULL                  
            );
        ''')

def create_anime(title, author, description) -> int | None:
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Anime (title, author, description) VALUES (?, ?, ?)',
            (title, author, description)
        )
        connection.commit()
        return cursor.lastrowid

def get_list_of_anime():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Anime')
        return cursor.fetchall()

def get_anime_info(anime_id: int):
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Anime WHERE i_anime = ?', (anime_id,))
        return cursor.fetchone()
