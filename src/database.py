import sqlite3

from student import Student
from subject import Subject


class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def search_username(self, student: Student) -> bool:
        query = "SELECT * FROM students WHERE studentName = ?"
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (student.username,))
            rows = cursor.fetchall()
                            
            return True if rows else False

    def save_credentials(self):
        pass

    def retrieve_hash(self):
        pass

    def search_subjects(self, student: Student, subject: Subject) -> list[dict]:
        query = "SELECT * FROM subjects WHERE studentID = ? AND subjectName = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (student.studentID, subject.name))
            rows = cursor.fetchall()
                    
            return [dict(row) for row in rows]

    def delete_subjects(self):
        pass

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
