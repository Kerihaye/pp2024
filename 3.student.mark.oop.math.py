import math
import numpy as np
import curses

class Person:
    def __init__(self, id, name, date_of_birth):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth

    def display(self):
        raise NotImplementedError("Subclass must implement this method")

class Student(Person):
    def __init__(self, student_id, name, date_of_birth):
        super().__init__(student_id, name, date_of_birth)
        self.marks = {}
        self.credits = {}

    def add_mark(self, course, mark, credit):
        self.marks[course] = math.floor(mark)
        self.credits[course] = credit

    def calculate_gpa(self):
        marks = np.array(list(self.marks.values()))
        credits = np.array(list(self.credits.values()))
        return np.average(marks, weights=credits)

    def display(self):
        return f"ID: {self.id}, Name: {self.name}, GPA: {self.calculate_gpa()}"

class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Invalid student")
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def list_students(self):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True)
        for student in self.students:
            print(student.display())

    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_marks(self):
        for student in self.students:
            for course, mark in student.marks.items():
                print(f"Student ID: {student.id}, Course ID: {course.course_id}, Mark: {mark}")

def main():
    stdscr = curses.initscr()
    school = School()
    while True:
        stdscr.addstr("1. Input student info\n")
        stdscr.addstr("2. Input course info\n")
        stdscr.addstr("3. Input mark\n")
        stdscr.addstr("4. List students\n")
        stdscr.addstr("5. List courses\n")
        stdscr.addstr("6. List marks\n")
        stdscr.addstr("7. Exit\n")
        stdscr.refresh()
        option = int(stdscr.getstr().decode())
        if option == 1:
            student_id = input("Student ID: ")
            name = input("Name: ")
            date_of_birth = input("Date of birth (example: dd/mm/yyyy): ")
            student = Student(student_id, name, date_of_birth)
            school.add_student(student)
        elif option == 2:
            course_id = input("Course ID: ")
            name = input("Name of the course: ")
            credit = int(input("Credit of the course: "))
            course = Course(course_id, name, credit)
            school.add_course(course)
        elif option == 3:
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            mark = float(input("Mark: "))
            student = school.get_student(student_id)
            course = school.get_course(course_id)
            if student and course:
                student.add_mark(course, mark, course.credit)
        elif option == 4:
            school.list_students()
        elif option == 5:
            school.list_courses()
        elif option == 6:
            school.list_marks()
        elif option == 7:
            break
        else:
            print("No option valid. Try again")
    curses.endwin()

if __name__ == "__main__":
    main()
