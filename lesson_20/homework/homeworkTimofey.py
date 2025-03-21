import sqlite3

conn = sqlite3.connect('favorites.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT UNIQUE
                  )''')
conn.commit()


def list_words():
    cursor.execute('SELECT word FROM Words')
    words = cursor.fetchall()

    if words:
        print("Ваші улюблені слова:")
        for word in words:
            print(word[0])
    else:
        print("Список слів порожній.")


def add_word(word):
    try:
        cursor.execute('INSERT INTO Words (word) VALUES (?)', (word,))
        conn.commit()
        print(f"Слово '{word}' додано до списку.")
    except sqlite3.IntegrityError:
        print(f"Слово '{word}' вже існує в списку.")


def main():
    while True:
        command = input("Введіть команду (list, add, exit): ").strip().lower()

        if command == 'list':
            list_words()
        elif command == 'add':
            word = input("Введіть слово для додавання: ").strip()
            add_word(word)
        elif command == 'exit':
            print("До побачення!")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

main()
conn.close()
