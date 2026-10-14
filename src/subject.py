class Subject:
    def __init__(
            self,
            subject_name: str | None,
            subjectID: int | None,
            topics: 'list[Topic]'
    ):
        self.subject_name = subject_name
        self.subject_id = subjectID
        self.topics = topics


class Topic:
    def __init__(
            self,
            topic_id: int | None,
            topic_name: str | None
            ):
        self.topic_id = topic_id
        self.topic_name = topic_name