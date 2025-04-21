import sqlite3


def init_db():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cats (
                i_cat INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                breed TEXT NOT NULL,
                birth_date TEXT NOT NULL                  
            );
        ''')

def create_cat( name, breed, birth_date ) -> int | None:
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Cats ( name, breed, birth_date ) VALUES (?, ?, ?)',
            ( name, breed, birth_date )
        )
        connection.commit() # закомітити треба, щоби айдішка оновилася
        # поверне айдішку останнього запису в БД
        return cursor.lastrowid # якщо не вийде - то ми отримаємо None

def get_list_of_cats():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Cats')
        cats_list = cursor.fetchall()
        return cats_list

def get_cat_info( cat_id: int ):
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Cats WHERE i_cat = ?', (cat_id,))
        cat_info = cursor.fetchone()
        return cat_info
