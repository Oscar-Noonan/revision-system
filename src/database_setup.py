import sqlite3

def create_database(database: str = "data/app.db"):
    with sqlite3.connect(database) as connection:
        with open("data/schema/database.sql") as file:
            schema = file.read()

        connection.executescript(schema)


create_database()