import sqlite3

with sqlite3.connect('words.db') as connection:
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL UNIQUE
        )
    ''')

    words_cache = set(word[0] for word in cursor.execute('SELECT word FROM Words'))

    while True:
        command = input("Введіть команду (list, add, exit): ").strip().lower()

        if command == "list":
            for word in words_cache:
                print(word)

        elif command == "add":
            new_word = input("Введіть слово: ").strip()
            if new_word not in words_cache:
                cursor.execute('INSERT INTO Words (word) VALUES (?)', (new_word,))
                connection.commit()
                words_cache.add(new_word)
                print(f"Слово '{new_word}' додано!")
            else:
                print("Це слово вже є в списку!")

        elif command == "exit":
            print("Вихід з програми.")
            break

        else:
            print("Невідома команда! Спробуйте ще раз.")
