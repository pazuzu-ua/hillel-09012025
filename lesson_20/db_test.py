import sqlite3

class Author:
    def __init__(self, i_author, name, birth_year):
        self.i_author = i_author
        self.name = name
        self.birth_year = birth_year
    def get_name(self):
        return self.name
    def age(self):
        return 2025 - self.birth_year

with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS Authors (
    #         i_author INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name TEXT NOT NULL,
    #         birth_year INTEGER CHECK (birth_year > 0)
    #     )
    # ''')
    #
    # authors = [
    #     ("J.K. Rowling", 1965),
    #     ("George Orwell", 1903),
    #     ("Jane Austen", 1775),
    #     ("Mark Twain", 1835),
    #     ("Agatha Christie", 1890),
    #     ("J.R.R. Tolkien", 1892),
    #     ("Stephen King", 1947),
    #     ("Ernest Hemingway", 1899),
    #     ("F. Scott Fitzgerald", 1896),
    #     ("Leo Tolstoy", 1828)
    # ]
    # cursor.executemany("INSERT INTO AUTHORS (name, birth_year) VALUES (?, ?)", authors)

    cursor.execute('SELECT * FROM Authors;')
    authors = cursor.fetchall()
    print(authors)
    # [ ( 1, 'name', 199 ) ]

    authors = [ Author( author[0], author[1], author[2] ) for author in authors ]
    for author in authors:
        print( author.get_name(), author.age() )
