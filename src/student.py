from subject import Subject


class Student:
    def __init__(self,
                 studentID: int | None,
                 username: str,
                 password: str,
                 db_hash: str | None,
                 subjects: list[Subject] | None,
                 time_available: int | None #int is the number of minutes
    ):
        self.studentID = studentID
        self.username = username
        self.password = password
        self.db_hash = db_hash
        self.subjects = subjects
        self.time_available = time_available


    def sanitise_credentials(self):
        pass

    def hash_pass(self):
        pass

    def compare_hash(self):
        pass
    
    def set_subjects(self):
        pass

    def set_available_time(self):
        pass
 