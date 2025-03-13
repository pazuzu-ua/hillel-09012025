import sqlite3


with sqlite3.connect('data.db') as connection:
    cursor = connection.cursor()

    # cursor.execute('PRAGMA foreign_keys = ON;')

    # виконуємо запит SELECT
    # FETCHALL
    # cursor.execute(' SELECT * FROM Departments; ')
    # result = cursor.fetchall()
    # print(result)
    # departments = [
    #     dict( id=department[0], name=department[1], location=department[2] ) for department in result
    # ]
    # for department in departments:
    #     print( f"{department['name']} Department is in {department['location']}" )

    # FETCH ONE
    # ПОВЕРНЕ None, якщо більше нічого нема
    # if result is None: ...
    # 1. перевірити чи є хоч одне значення
    # 2. оптимізація використання пам'яті
    # cursor.execute(' SELECT * FROM Departments; ')
    #
    # while True:
    #     result = cursor.fetchone()
    #     if result is None:
    #         break
    #     print(result)

    # walrus operator     ( := )
    # cursor.execute(' SELECT * FROM Departments; ')
    # # 1. result = cursor.fetchone()
    # # 2. while result
    # # 3. на 6-тій ітерації в нас буде: while None:
    # while result := cursor.fetchone():
    #     print(result)

    # data = { 'name': 'Sara' }
    # # якщо ключ існує - отримаємо його значення, якщо ключ не існує - отримаємо None
    # if name := data.get('name'):
    #     print( name )

    # FETCH MANY
    # пагінація
    # cursor.execute(' SELECT * FROM Departments; ')
    # result = cursor.fetchmany(3)
    # print(result)
    #
    # result = cursor.fetchmany(3)
    # print(result)
    # if not result or len(result) < 3:
    #     print('Це остання...')

    # cursor.execute('''
    #     SELECT E.first_name, E.last_name, D.name, E.salary
    #       FROM Employees E
    #       JOIN Departments D ON E.department_id = D.id
    # ''')
    # result = cursor.fetchall()
    # print(result)

    # cursor.execute('SELECT first_name, last_name, MAX(salary) FROM Employees')
    # result = cursor.fetchone()
    # print(result)

    # UPDATE
    # cursor.execute(' SELECT * FROM Departments; ')
    # result = cursor.fetchall()
    # print(result)
    #
    # cursor.execute(  " UPDATE Departments SET location = 'Kyiv', name = 'Super HR' WHERE id = 1 " )
    #
    # cursor.execute(' SELECT * FROM Departments; ')
    # result = cursor.fetchall()
    # print(result)

    # DELETE
    # cursor.execute(' SELECT * FROM Departments; ')
    # result = cursor.fetchall()
    # print(result)
    #
    # cursor.execute(' DELETE FROM Departments WHERE id = 3 ')
    #
    # cursor.execute(' SELECT * FROM Departments; ')
    # result = cursor.fetchall()
    # print(result)

    # cursor.execute(' SELECT * FROM Employees; ')
    # result = cursor.fetchall()
    # print(result)
