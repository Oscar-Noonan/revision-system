import sqlite3


class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def search_username(self, username: str | None) -> bool:
        query = "SELECT 1 FROM students WHERE studentName = ?"
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            return cursor.fetchone() is not None

    def save_credentials(self):
        pass

    def retrieve_hash(self):
        pass

    def search_subjects(self, studentID: int | None) -> list[dict]:
        query = "SELECT * FROM enrolments WHERE studentID = ?"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (studentID,))
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
