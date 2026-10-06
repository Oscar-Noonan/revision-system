class Question:
    def __init__(self,
                 questionID: int,
                 question_text: str,
                 total_marks: int,
                 mark_scheme: int,
                 user_answer: str | None,
                 response: dict | None
    ):
        self.questionID = questionID
        self.question_text = question_text
        self.total_marks = total_marks
        self.mark_scheme = mark_scheme
        self.user_answer = user_answer
        self.response = response
        
    
    def retirve_questions():
        pass
    
    def mark_questions():
        pass
