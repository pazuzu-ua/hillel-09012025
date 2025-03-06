import sqlite3

with sqlite3.connect('data.db') as connection:
    # зайшли в блок: під'єдналися
    # Це має включити підтримку зовнішніх ключів:
    connection.execute('PRAGMA foreign_keys = 1')

    # КУРСОР
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Authors (
            i_author INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            i_book INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            pages INTEGER NOT NULL CHECK ( pages > 0 ),
            i_author INTEGER NOT NULL,
            FOREIGN KEY (i_author) REFERENCES Authors(i_author)
        );
    """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Reviews (
                i_review INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                stars INTEGER NOT NULL CHECK (stars > 0 AND stars < 6 ),
                i_book INTEGER NOT NULL,
                FOREIGN KEY (i_book) REFERENCES Books(i_book)
            );
        """)

    # cursor.execute("""
    #     INSERT INTO Authors ( name, surname )
    #     VALUES
    #         ( 'Stephen', 'King' ),
    #         ( 'Joan', 'Roaling' );
    # """)

    # шаблон!
    # binding
    # SQL injection
    cursor.executemany(
    """
        INSERT INTO Books ( title, pages, i_author )
         VALUES ( ?, ?, ? )
    """,
    [
        ( 'IT', 800, 1 ),
        ( 'Harry Potter 1', 500, 2 )
    ]
    )

    # email = input()
    # f"INSERT INTO Users (email) VALUES ('{email}')"
    # ""DROP DATABASE;"

# вийшли з блоку: від'єдналися