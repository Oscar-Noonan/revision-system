import unittest
import os

from database_setup import create_database


class TestDatabaseSetup(unittest.TestCase):

    def test_create_database(self):
        create_database()
        assert os.path.exists("data/app.db")

    def test_create_database_with_parameter(self):
        test_db = "test_app.db"
        create_database(test_db)
        assert os.path.exists(test_db)

if __name__ == '__main__':
    unittest.main()
