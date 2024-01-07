class Student:
    def __init__(self):
        self.name = None
        self.id = None
        self.dob = None

    def input_student_info(self, number):
        print(f"\nEnter information for student {number}:")
        self.name = input("Enter student name: ")
        self.id = input("Enter student ID: ")
        self.dob = input("Enter student DoB: ")

    def __str__(self):
        return f"Student {self.name}, ID: {self.id}, DoB: {self.dob}"


class Course:
    def __init__(self):
        self.name = None
        self.id = None

    def input_course_info(self, number):
        print(f"\nEnter information for course {number}:")
        self.name = input("Enter course name: ")
        self.id = input("Enter course ID: ")

    def __str__(self):
        return f"Course {self.name}, ID: {self.id}"


class MarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def add_students(self, count):
        for i in range(count):
            student = Student()
            student.input_student_info(i + 1)
            self.students.append(student)

    def add_courses(self, count):
        for i in range(count):
            course = Course()
            course.input_course_info(i + 1)
            self.courses.append(course)

    def input_marks_for_course(self):
        course_name = input("\nEnter the course to give marks: ")
        course = next((c for c in self.courses if c.name == course_name), None)
        if course is None:
            print("Course not found.")
            return

        course_marks = {}
        for student in self.students:
            mark = float(input(f"Enter {course_name} mark for {student.name}: "))
            course_marks[student.name] = mark
        self.marks[course_name] = course_marks

    def show_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def show_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def show_marks(self, course_name):
        if course_name in self.marks:
            print(f"\nMarks for {course_name}:")
            for student, mark in self.marks[course_name].items():
                print(f"{student}: {mark}")
        else:
            print("No marks recorded for this course.")

def input_positive_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    management = MarkManagement()

    student_count = input_positive_number("Enter the number of students: ")
    management.add_students(student_count)

    course_count = input_positive_number("Enter the number of courses: ")
    management.add_courses(course_count)

    management.input_marks_for_course()

    management.show_courses()
    management.show_students()
    course_to_show = input("\nEnter the course to show marks: ")
    management.show_marks(course_to_show)
