import unittest
import os
import sqlite3
import hashlib

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
                    username TEXT
                )
            """)

            conn.execute(
                "INSERT INTO students VALUES (?)",
                ("Oscar",)
            )

        student = Student("Oscar", None, 1, None, None, None)
        self.assertTrue(db.search_username(student.username))

        os.remove("test.db")


    def test_retrieve_hash(self):
        db = Database("test.db")
        
        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE students (
                    student_id INTEGER,
                    password TEXT
                )
            """)

            first_student_id = 1
            first_password = hashlib.sha256("password123".encode()).hexdigest()
            second_student_id = 2
            second_password = hashlib.sha256("SecurePassword123".encode()).hexdigest()

            conn.executemany(
                "INSERT INTO students VALUES (?, ?)",
                [
                    (first_student_id, first_password),
                    (second_student_id, second_password)
                ]
            )

        self.assertEqual(db.retrieve_hash(first_student_id), first_password)
        self.assertEqual(db.retrieve_hash(second_student_id), second_password)

        os.remove("test.db")


    def test_search_enrollment_single(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS enrolments (
                    student_id INTEGER,
                    subject_name TEXT
                )
            """)
            conn.execute(
                "INSERT INTO enrolments VALUES (?, ?)",
                (1, "Computer Science")
            )

        student = Student("Oscar", None, 1, None, None, None)

        self.assertEqual(
            db.search_subjects(student.student_id),
            [{"student_id": 1, "subject_name": "Computer Science"}]
        )

        os.remove("test.db")


    def test_search_enrollment_multiple(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS enrolments (
                    student_id INTEGER,
                    subject_name TEXT
                )
            """)
            conn.executemany(
                "INSERT INTO enrolments VALUES (?, ?)",
                [
                    (1, "Computer Science"),
                    (2, "Computer Science"),
                    (1, "Geography")
                ]
            )

        self.assertEqual(
            db.search_subjects(1),
            [
                {"student_id": 1, "subject_name": "Computer Science"},
                {"student_id": 1, "subject_name": "Geography"}
            ]
        )

        os.remove("test.db")


    def test_delete_subjects(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS enrolments (
                    student_id INTEGER,
                    subject_name TEXT
                )
            """)
            conn.executemany(
                "INSERT INTO enrolments VALUES (?, ?)",
                [
                    (1, "Computer Science"),
                    (2, "Computer Science"),
                    (1, "Geography")
                ]
            )

        db.delete_subjects(1)

        self.assertEqual(
            db.search_subjects(1),
            []
        )

        self.assertEqual(
            db.search_subjects(2),
            [
                {"student_id": 2, "subject_name": "Computer Science"}
            ]
        )

        os.remove("test.db")

if __name__ == "__main__":
    unittest.main()