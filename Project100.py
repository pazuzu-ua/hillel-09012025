import sqlite3

def create_table():
    with sqlite3.connect("words.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Words (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()

def add_word(word):
    try:
        with sqlite3.connect("words.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Words (word) VALUES (?)", (word,))
            conn.commit()
            print(f"Слово '{word}' додано!")
    except sqlite3.IntegrityError:
        print("Це слово вже є у списку!")

def list_words():
    with sqlite3.connect("words.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM Words")
        words = cursor.fetchall()
        if words:
            print("Ваші улюблені слова:")
            for word in words:
                print(f"- {word[0]}")
        else:
            print("Список слів порожній!")

def main():
    create_table()
    while True:
        command = input("Введіть команду (list, add, exit): ").strip().lower()
        if command == "list":
            list_words()
        elif command == "add":
            word = input("Введіть слово: ").strip()
            if word:
                add_word(word)
        elif command == "exit":
            print("До побачення!")
            break
        else:
            print("Невідома команда!")

if __name__ == "__main__":
    main()