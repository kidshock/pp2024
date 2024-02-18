class Course:
    def __init__(self, name, id, credit):
        self.name = name
        self.id = id
        self.credit = credit
        self.marks = {}

    def add_mark(self, student, mark):
        self.marks[student.name] = mark
        student.add_mark(self, mark, self.credit)

    def __str__(self):
        return f"{self.name}, ID: {self.id}"