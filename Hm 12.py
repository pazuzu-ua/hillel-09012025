import sqlite3

conn = sqlite3.connect('fvwords.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT UNIQUE
                  )''')
conn.commit()


def list_words():
    conn = sqlite3.connect("fvwords.db")
    cursor = conn.cursor()
    cursor.execute('SELECT word FROM Words')
    words = cursor.fetchall()
    if words:
        print("Список улюблених слів:")
        for word in words:
            print(word[0])
    else:
        print("Список слів порожній.")


def add_word(word):
    conn = sqlite3.connect("fvwords.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Words (word) VALUES (?)",(word,))
        conn.commit()
        print(f"Слово '{word}' додано.")
    except sqlite3.IntegrityError:
        print(f"Це слово '{word}' вже існує.")


def main():
    while True:
        command = input("Введіть команду (list,add,exit): ").strip().lower()

        if command == 'list':
            list_words()
        elif command == 'add':
            word = input("Введіть слово об додати в список: ").strip()
            add_word(word)
        elif command == 'exit':
            print("До побачення!")
            break
        else:
            print("Невідома команда.Спробуйте ще раз.")

if __name__ == "__main__":
    main()