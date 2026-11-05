import sqlite3

import student


class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def search_username(self, username: str | None) -> bool:
        query = "SELECT 1 FROM students WHERE username = ?"
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            return cursor.fetchone() is not None

    def save_credentials(self, username: str, password: str, time_available: int) -> int:
        query = "INSERT INTO students (username, password, time_available) VALUES (?, ?, ?)"
                
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (username, password, time_available))
            return 0

    def update_password(self, username: str, password: str) -> int:
        query = "UPDATE students SET password = ? WHERE username = ?"
                        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (password, username))
            return 0

    def update_time_available(self, username: str, time_available: int) -> int:
        query = "UPDATE students SET time_available = ? WHERE username = ?"
                                
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (time_available, username))
            return 0

    def retrieve_hash(self, username: str | None) -> str:
        query = "SELECT password FROM students WHERE username = ?"
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            row = cursor.fetchone()
            return row[0] if row else ""

    def search_subjects(self, username: str | None) -> list[str]:
        query = "SELECT subject_name FROM enrolments WHERE username = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            rows = cursor.fetchall()
                    
            return [row[0] for row in rows]

    def delete_subjects(self, username: str | None) -> int:
        query = "DELETE FROM enrolments WHERE username = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            return 0

    def save_subjects(self):
        pass
    
    def get_scores(self):
        pass

    def store_plan(self):
        pass

    def get_questions(self):
        pass

    def save_scores(self):
        pass
