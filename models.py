class StudyRecord:
    def __init__(self, date, subject, study_time):
        self.date = date
        self.subject = subject
        self.study_time = study_time

    def to_dict(self):
        return {
            "date": self.date,
            "subject": self.subject,
            "study_time": self.study_time
        }