import unittest
import os
import sqlite3

from database import Database
from student import Student
from subject import Subject


class TestDatabase(unittest.TestCase):

    def test_get_connection(self):
        db = Database(":memory:")
        self.assertIsInstance(db.get_connection(), sqlite3.Connection)


    def test_search_username(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE students (
                    studentName TEXT
                )
            """)

            conn.execute(
                "INSERT INTO students VALUES (?)",
                ("Oscar",)
            )

        student = Student("Oscar", None, 1, None, None, None)
        self.assertTrue(db.search_username(student.username))

        os.remove("test.db")


    def test_search_subjects_single(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE subjects (
                    studentID INTEGER,
                    subjectName TEXT
                )
            """)
            conn.execute(
                "INSERT INTO subjects VALUES (?, ?)",
                (1, "Computer Science")
            )

        student = Student("Oscar", None, 1, None, None, None)

        self.assertEqual(
            db.search_subjects(student.studentID),
            [{"studentID": 1, "subjectName": "Computer Science"}]
        )

        os.remove("test.db")


    def test_search_subjects_multiple(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE subjects (
                    studentID INTEGER,
                    subjectName TEXT
                )
            """)
            conn.executemany(
                "INSERT INTO subjects VALUES (?, ?)",
                [
                    (1, "Computer Science"),
                    (2, "Computer Science"),
                    (1, "Geography")
                ]
            )

        student = Student("Oscar", None, 1, None, None, None)

        self.assertEqual(
            db.search_subjects(student.studentID),
            [
                {"studentID": 1, "subjectName": "Computer Science"},
                {"studentID": 1, "subjectName": "Geography"}
            ]
        )

        os.remove("test.db")

if __name__ == "__main__":
    unittest.main()