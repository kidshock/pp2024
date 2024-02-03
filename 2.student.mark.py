class Person:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def __str__(self):
        return f"{self.name}, ID: {self.id}, DoB: {self.dob}"

class Student(Person):
    def __init__(self, name, id, dob):
        super().__init__(name, id, dob)

class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.marks = {}

    def add_mark(self, student, mark):
        self.marks[student.name] = mark

    def __str__(self):
        return f"{self.name}, ID: {self.id}"

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

if __name__ == "__main__":
    school = School()

    for _ in range(input_positive_number("Enter the number of students: ")):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        dob = input("Enter student DoB: ")
        school.add_student(Student(name, id, dob))

    for _ in range(input_positive_number("Enter the number of courses: ")):
        name = input("Enter course name: ")
        id = input("Enter course ID: ")
        school.add_course(Course(name, id))

    course_name = input("\nEnter the course to give marks: ")
    course = school.get_course(course_name)
    if course:
        for student in school.students:
            mark = float(input(f"Enter {course_name} mark for {student.name}: "))
            course.add_mark(student, mark)

    school.show_courses()
    school.show_students()
    course_to_show = input("\nEnter the course to show marks: ")
    school.show_marks(course_to_show)
