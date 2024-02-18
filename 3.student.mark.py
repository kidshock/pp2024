import math
import numpy as np
import curses

def input_positive_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
    
    def calculate_gpa(self):
        weighted_marks = np.array([mark * credit for (_, mark), credit in zip(self.marks, self.credits)])
        total_credits = np.sum(self.credits)
        return np.sum(weighted_marks) / total_credits if total_credits else 0


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


def main(stdscr):
    school = School()

    stdscr.addstr("Welcome to Student Mark Management System!\n")
    stdscr.refresh()

    num_students = input_positive_number("Enter the number of students: ")
    stdscr.addstr(f"\nNumber of students: {num_students}\n")
    stdscr.refresh()

    for _ in range(num_students):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        dob = input("Enter student DoB: ")
        school.add_student(Student(name, id, dob))

    num_courses = input_positive_number("Enter the number of courses: ")
    stdscr.addstr(f"\nNumber of courses: {num_courses}\n")
    stdscr.refresh()

    for _ in range(num_courses):
        name = input("Enter course name: ")
        id = input("Enter course ID: ")
        credit = input_positive_number("Enter course credit: ")
        school.add_course(Course(name, id, credit))

    course_name = input("\nEnter the course to give marks: ")
    course = school.get_course(course_name)
    if course:
        for student in school.students:
            mark = float(input(f"Enter {course_name} mark for {student.name}: "))
            mark = math.floor(mark * 10) / 10  # round down to 1 decimal place
            course.add_mark(student, mark)

    stdscr.addstr("\nCourses:\n")
    school.show_courses()
    stdscr.addstr("\nStudents:\n")
    school.show_students()

    course_to_show = input("\nEnter the course to show marks: ")
    stdscr.addstr(f"\nMarks for {course_to_show}:\n")
    school.show_marks(course_to_show)

    school.sort_students_by_gpa()
    stdscr.addstr("\nStudents sorted by GPA:\n")
    school.show_students()

    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
