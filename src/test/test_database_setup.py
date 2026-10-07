import unittest
import os
import sqlite3

from database_setup import create_database


class TestDatabaseSetup(unittest.TestCase):

    def test_create_database(self):
        create_database()

        self.assertTrue(os.path.exists("data/app.db"))

    def test_create_database_with_parameter(self):
        test_db = "test_app.db"

        create_database(test_db)

        self.assertTrue(os.path.exists(test_db))

        if os.path.exists(test_db):
            os.remove(test_db)

    def test_database_contains_schema(self):
        test_db = "test_schema.db"

        create_database(test_db)

        with sqlite3.connect(test_db) as connection:
            cursor = connection.cursor()

            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )

            tables = cursor.fetchall()

        self.assertGreater(len(tables), 0)

        if os.path.exists(test_db):
            os.remove(test_db)


if __name__ == "__main__":
    unittest.main()