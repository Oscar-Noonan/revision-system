class Subject:
    def __init__(
            self,
            subject_name: str | None,
            topics: 'list[Topic]'
    ):
        self.subject_name = subject_name
        self.topics = topics


class Topic:
    def __init__(
            self,
            topic_name: str | None
            ):
        self.topic_name = topic_name