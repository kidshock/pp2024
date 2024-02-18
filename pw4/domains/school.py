class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def get_course(self, name):
        for course in self.courses:
            if course.name == name:
                return course
        return None

    def show_courses(self):
        for course in self.courses:
            print(course)

    def show_students(self):
        for student in self.students:
            print(student)

    def show_marks(self, course_name):
        course = self.get_course(course_name)
        if course:
            print(f"\nMarks for {course_name}:")
            for student, mark in course.marks.items():
                print(f"{student}: {mark}")
        else:
            print("No marks recorded for this course.")
        
    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True)