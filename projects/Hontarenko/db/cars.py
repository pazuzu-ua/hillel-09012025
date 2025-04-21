import sqlite3


def init_db():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cars(
                i_car INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                colour TEXT NOT NULL,
                production_date TEXT NOT NULL
            );

        ''')


def create_car(brand, model, colour, production_date) -> int | None:
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Cars(brand,model,colour,production_date) VALUES (?,?,?,?)',
            (brand, model, colour, production_date)
        )
        connection.commit()
        return cursor.lastrowid


def get_list_of_cars():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Cars')
        cars_list = cursor.fetchall()
        return cars_list


def get_car_info(car_id: int):
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Cars WHERE i_car=?', (car_id,))
        car_info = cursor.fetchone()
        return car_info