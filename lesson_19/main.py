import sqlite3

with sqlite3.connect('data.db') as connection:
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON;')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            salary INTEGER,
            department_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES Departments(id)
        );
    ''')

    # placeholder "?"
    # escape SQL injection
    cursor.executemany(
        'INSERT OR IGNORE INTO Departments (id, name, location) VALUES (?, ?, ?);',
        (
            (1, 'HR', 'New York'),
            (2, 'Engineering', 'San Francisco'),
            (3, 'Marketing', 'Chicago'),
            (4, 'Sales', 'Los Angeles'),
            (5, 'Finance', 'Boston'),
        )
    )

    cursor.executemany(
        'INSERT OR IGNORE INTO Employees (id, first_name, last_name, salary, department_id) VALUES (?, ?, ?, ?, ?);',
        (
            (1, 'John', 'Doe', 60000, 1),
            (2, 'Jane', 'Smith', 65000, 1),
            (3, 'Alice', 'Johnson', 120000, 2),
            (4, 'Bob', 'Lee', 110000, 2),
            (5, 'Charlie', 'Kim', 100000, 2),
            (6, 'Dana', 'White', 70000, 3),
            (7, 'Eric', 'Brown', 75000, 3),
            (8, 'Fiona', 'Davis', 80000, 4),
            (9, 'George', 'Miller', 82000, 4),
            (10, 'Helen', 'Wilson', 78000, 4),
            (11, 'Ivan', 'Thomas', 90000, 5),
        )
    )
