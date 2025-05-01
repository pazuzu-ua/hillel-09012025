import sqlite3
from datetime import date
from schema import BookUpdate


def init_db():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    isbn TEXT NOT NULL UNIQUE,            
                    year INTEGER NOT NULL
                )
                """)


def create_book(title: str, author: str, isbn: int, year: date) -> int | None:
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Books (title, author,isbn, year) VALUES (?,?,?,?)',
            (title, author, isbn, year)
        )
        connection.commit() #треба зокомітити для того щоб id оновилася
        # поверне id останнього запису в БД
        return cursor.lastrowid # якщо не вийде - то ми отримаемо - None


def get_list_of_books():
    with sqlite3.connect('base.db') as connaction:
        cursor = connaction.cursor()
        cursor.execute('SELECT * FROM Books')
        authors_list = cursor.fetchall()
        return authors_list


def get_book_info(book_id: int):
    with sqlite3.connect('base.db') as connaction:
        cursor = connaction.cursor()
        cursor.execute('SELECT * FROM Books WHERE id = ?', (book_id,))
        book_info = cursor.fetchone()
        return book_info


def remove_book(book_id: int):
    with sqlite3.connect('base.db') as connaction:
        cursor = connaction.cursor()
        cursor.execute('DELETE FROM Books WHERE id = ?', (book_id,))
        return True


def update_book_info(book_id: int, book_info: BookUpdate):
    with sqlite3.connect('base.db') as connaction:
        cursor = connaction.cursor()
        cursor.execute(
            '''
            UPDATE Books 
            SET title = ?, author = ?, isbn = ?, year = ? 
            WHERE id = ?
            ''',
            (book_info.title, book_info.author, book_info.isbn, book_info.year, book_id)
            )
        return True










