import math
import curses
from .input import input_positive_number
from .output import output_with_curses
from .domains.person import Person
from .domains.student import Student
from .domains.course import Course
from .domains.school import School

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