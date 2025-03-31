import sqlite3

with sqlite3.connect("word.db") as connection:
    cursor = connection.cursor()

    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS Words(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL) """)

    while True:
        something = input("Введіть одну з трьох команд \nlist, add, exit: ")

        if something == 'list':
            cursor.execute("SELECT word FROM Words")
            words = cursor.fetchall()
            if words:
                print("Список усіх слів: ")
                for w in words:
                    print(w[0])
            else:
                print("Список слів порожній.")

        elif something == "add":
            add_word = input("Введіть слово яке хочете додати: ")
            cursor.execute("SELECT word FROM Words")
            words = [row[0] for row in cursor.fetchall()]

            if add_word in words:
                print("Це слово вже є у списку. ")
            else:
                cursor.execute('INSERT INTO Words (word) Values (?)', (add_word,))
                connection.commit()
                print("Слово було успішно додано.")

        elif something == "exit":
            print("Завершення роботи.")
            break

        else:
            print("Команда невідома. Введіть одну із запропонованих команд (list, add, exit).")



