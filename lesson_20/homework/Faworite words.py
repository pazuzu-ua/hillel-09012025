import sqlite3


def create_table():
    with sqlite3.connect("words.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Words (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT UNIQUE NOT NULL
            )
        """
        )
        conn.commit()

def add_word(word, words_cache):
    if word in words_cache:
        print("Таке слово вже є")
        return
    with sqlite3.connect("words.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Words (word) VALUES (?)", (word,))
            conn.commit()
            words_cache.add(word)
            print("Слово успішно додано")
        except sqlite3.IntegrityError:
            print("Таке слово вже є")

def list_words():
    with sqlite3.connect("words.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM Words")
        words = [row[0] for row in cursor.fetchall()]
    return words

def main():
    create_table()
    words_cache = set(list_words())

    while True:
        command = input("Введіть команду list, add, exit: ").strip().lower()

        if command == "list":
            words = list_words()
            print("Ваші улюблені слова:", ", ".join(words) if words else "(немає)")
        elif command == "add":
            word = input("Введіть слово: ").strip()
            if word:
                add_word(word, words_cache)
        elif command == "exit":
            print("Вихід...")
            break
        else:
            print("Неіснуюча команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()