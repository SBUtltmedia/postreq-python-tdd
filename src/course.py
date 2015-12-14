from src.utils import trim, trim_leading_zeroes


class Course:
    def __init__(self, course_id, subject, catalog, rq_group):
        self.course_id = trim(course_id)
        self.subject = trim(subject)
        self.catalog = trim(catalog)
        self.rq_group = trim_leading_zeroes(trim(rq_group))

    def __repr__(self):
        return self.subject + " " + self.catalog
