import sqlite3
from tkinter.constants import INSERT


def show_menu(menu: dict[str:str], sep: str = '-') -> str:
    while True:
        for key, value in menu.items():
            print(f'{key} {sep} {value}')
        choice = input('Make your choice:\t')
        if choice not in my_menu.keys():
            print('\nInput is incorrect, repeat..\n')
        else:
            return choice

with sqlite3.connect('words.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    word TEXT NOT NULL
    );
    ''')

my_menu = {
    "1": "Display a list of words",
    "2": "Add a word",
    "0": "Exit the program"
}

while True:
    menu_item = show_menu(my_menu)

    if menu_item == '0':
        break

    elif menu_item == '1':
        # Показать список слов
        with sqlite3.connect('words.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT word FROM Words;
            ''')
            results = cursor.fetchall()
            if results:
                print()
                for word in results:
                    print(word[0])
                print()
            else:
                print('\nDatabase is empty!\n')

    elif menu_item == '2':
        # Добавление слова в таблицу
        user_word = input(f'Input a word:')
        with sqlite3.connect('words.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT word FROM Words;
            ''')
            results = cursor.fetchall()
            word_list = [word[0] for word in results]
            if user_word in word_list:
                print('\nThis word is already in database!\n')
            else:
                cursor.execute('''
                INSERT INTO Words (word)
                VALUES (?)''', (user_word,))


