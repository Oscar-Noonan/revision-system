import sqlite3

def create_database():
    connection = sqlite3.connect("data/app.db")

    with open("data/schema/database.sql") as file:
        schema = file.read()

    connection.executescript(schema)
    connection.close()


create_database()