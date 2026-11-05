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

        student = Student("Oscar", None, None, None, None)
        self.assertTrue(db.search_username(student.username))

        os.remove("test.db")


    def test_retrieve_hash(self):
        db = Database("test.db")
        
        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    username TEXT,
                    "password" TEXT
                )
            """)

            first_username = "Oscar"
            first_password = hashlib.sha256("password123".encode()).hexdigest()
            second_username = "Other"
            second_password = hashlib.sha256("SecurePassword123".encode()).hexdigest()

            conn.executemany(
                "INSERT INTO students VALUES (?, ?)",
                [
                    (first_username, first_password),
                    (second_username, second_password)
                ]
            )

        self.assertEqual(db.retrieve_hash(first_username), first_password)
        self.assertEqual(db.retrieve_hash(second_username), second_password)

        os.remove("test.db")


    def test_save_credentials(self):
        db = Database("test.db")
                
        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    time_available INTEGER NOT NULL
                )
            """)

        username = "student1"
        password = "password123"
        time_available = 90

        db.save_credentials(username, password, time_available)

        with db.get_connection() as conn:
            cursor = conn.execute("SELECT username, password, time_available FROM students WHERE username = ?",  (username,))
            result = cursor.fetchone()

        self.assertEqual(result[0], username)
        self.assertEqual(result[1], password)
        self.assertEqual(result[2], time_available)

        os.remove("test.db")


    def test_update_password(self):
        db = Database("test.db")
                        
        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    time_available INTEGER NOT NULL
                )
            """)

        username = "student1"
        password = "password123"
        time_available = 90

        db.save_credentials(username, password, time_available)

        password = "newpassword123"
        
        db.update_password(username, password)

        with db.get_connection() as conn:
            cursor = conn.execute("SELECT username, password, time_available FROM students WHERE username = ?",  (username,))
            result = cursor.fetchone()

        self.assertEqual(result[0], username)
        self.assertEqual(result[1], password)
        self.assertEqual(result[2], time_available)

        os.remove("test.db")


    def test_update_time_available(self):
        db = Database("test.db")
                        
        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    time_available INTEGER NOT NULL
                )
            """)

        username = "student1"
        password = "password123"
        time_available = 90

        db.save_credentials(username, password, time_available)

        time_available = 120

        db.update_time_available(username, time_available)

        with db.get_connection() as conn:
            cursor = conn.execute("SELECT username, password, time_available FROM students WHERE username = ?",  (username,))
            result = cursor.fetchone()

        self.assertEqual(result[0], username)
        self.assertEqual(result[1], password)
        self.assertEqual(result[2], time_available)

        os.remove("test.db")


    def test_search_enrollment_single(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS enrolments (
                    username TEXT,
                    subject_name TEXT
                )
            """)
            conn.execute(
                "INSERT INTO enrolments VALUES (?, ?)",
                ("Oscar", "Computer Science")
            )

        student = Student("Oscar", None, None, None, None)

        self.assertEqual(
            db.search_subjects(student.username),
            ["Computer Science"]
        )

        os.remove("test.db")


    def test_search_enrollment_multiple(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS enrolments (
                    username TEXT,
                    subject_name TEXT
                )
            """)
            conn.executemany(
                "INSERT INTO enrolments VALUES (?, ?)",
                [
                    ("Oscar", "Computer Science"),
                    ("Other", "Computer Science"),
                    ("Oscar", "Geography")
                ]
            )

        self.assertEqual(
            db.search_subjects("Oscar"),
            [
                "Computer Science",
                "Geography"
            ]
        )

        os.remove("test.db")


    def test_delete_subjects(self):
        db = Database("test.db")

        with db.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS enrolments (
                    username TEXT,
                    subject_name TEXT
                )
            """)
            conn.executemany(
                "INSERT INTO enrolments VALUES (?, ?)",
                [
                    ("Oscar", "Computer Science"),
                    ("Other", "Computer Science"),
                    ("Oscar", "Geography")
                ]
            )

        db.delete_subjects("Oscar")

        self.assertEqual(
            db.search_subjects("Oscar"),
            []
        )

        self.assertEqual(
            db.search_subjects("Other"),
            [
                "Computer Science"
            ]
        )

        os.remove("test.db")

if __name__ == "__main__":
    unittest.main()