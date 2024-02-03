def input_positive_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_student_info():
    name = input("Enter student name: ")
    id = input("Enter student ID: ")
    dob = input("Enter student DoB: ")
    return {"name": name, "id": id, "dob": dob}

def input_course_info():
    name = input("Enter course name: ")
    id = input("Enter course ID: ")
    return {"name": name, "id": id}

def input_marks_for_course(students, course_name):
    marks = {}
    for student in students:
        mark = float(input(f"Enter {course_name} mark for {student['name']}: "))
        marks[student['name']] = mark
    return marks

def show_courses(courses):
    for course in courses:
        print(f"Course {course['name']}, ID: {course['id']}")

def show_students(students):
    for student in students:
        print(f"Student {student['name']}, ID: {student['id']}, DoB: {student['dob']}")

def show_marks(marks, course_name):
    if course_name in marks:
        print(f"\nMarks for {course_name}:")
        for student, mark in marks[course_name].items():
            print(f"{student}: {mark}")
    else:
        print("No marks recorded for this course.")

if __name__ == "__main__":
    students = [input_student_info() for _ in range(input_positive_number("Enter the number of students: "))]
    courses = [input_course_info() for _ in range(input_positive_number("Enter the number of courses: "))]

    marks = {}
    for course in courses:
        marks[course['name']] = input_marks_for_course(students, course['name'])

    show_courses(courses)
    show_students(students)
    course_to_show = input("\nEnter the course to show marks: ")
    show_marks(marks, course_to_show)
