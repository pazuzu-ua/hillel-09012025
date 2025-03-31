import sqlite3

with sqlite3.connect('data.db') as connection:
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON;')

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Words (
    i_word INTEGER PRIMARY KEY AUTOINCREMENT,
    user_words TEXT NOT NULL
    );
    """)

    user_word = []

    while True:
        command = input('Please enter one of the commands: list / add / exit: ')

        if command == 'add':
            added_word = input('Please enter your favourite word: ')
            cursor.execute("SELECT * FROM Words WHERE user_words = ?", (added_word,))
            if cursor.fetchone() is not None:
                print('Sorry, the word is already added...')
            else:
                user_word.append(added_word)
                cursor.execute("""
                        INSERT INTO Words(user_words)
                        VALUES(?)
                        """, (added_word,))
                connection.commit()
                print('The word is successfully added to the list!')

        elif command == 'list':
            cursor.execute("""
                SELECT user_words FROM Words
                """)
            selected_words = cursor.fetchall()
            if len(selected_words) == 0:
                print('Sorry, there are no added words to list...')
            else:
                print("List of favourite words:")
                for word in selected_words:
                    print(f"- {word[0]}")

        elif command == 'exit':
            print('Exiting the program...')
            break

        else:
            print('Invalid command. Please try again.')