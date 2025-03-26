import sqlite3

conn = sqlite3.connect("words.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT UNIQUE NOT NULL
)
''')

conn.commit()
conn.close()

def list_words():
    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM Words")
    words = cursor.fetchall()
    conn.close()
    print("Список слів:")
    for word in words:
        print(word[0])

def add_word(word):
    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Words (word) VALUES (?)", (word,))
        conn.commit()
        print("Слово додано.")
    except sqlite3.IntegrityError:
        print("Це слово вже є в базі.")
    finally:
        conn.close()

def main():
    while True:
        command = input("Введіть команду (list, add, exit): ").strip().lower()
        if command == "list":
            list_words()
        elif command == "add":
            word = input("Введіть слово: ").strip()
            add_word(word)
        elif command == "exit":
            print("До побачення!")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
