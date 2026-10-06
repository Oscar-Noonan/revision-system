import sqlite3

def create_database(database: str = "data/app.db"):
    connection = sqlite3.connect(database)

    with open("data/schema/database.sql") as file:
        schema = file.read()

    connection.executescript(schema)
    connection.close()


create_database()