# init_database.py

import pathlib
import sqlite3

if __name__ == '__main__':
    if pathlib.Path('people.db').exists():
        pathlib.Path('people.db').unlink()

    conn = sqlite3.connect('people.db')

    columns = [
        "id INTEGER PRIMARY KEY",
        "lname VARCHAR UNIQUE",
        "fname VARCHAR",
        "timestamp DATETIME",
    ]
    create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
    conn.execute(create_table_cmd)
