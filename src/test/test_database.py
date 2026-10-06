import unittest

from database import *


class TestDatabase(unittest.TestCase):

    def test_get_connection(self):
        db = Database(":memory:")
        conn = db.get_connection()
        assert isinstance(conn, sqlite3.Connection)

if __name__ == '__main__':
    unittest.main()
