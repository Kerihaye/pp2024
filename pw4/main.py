from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import input as input_module
import output

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def add_student(self):
        student = input_module.input_student_info()
        self.students.append(student)

    def add_course(self):
        course = input_module.input_course_info()
        self.courses.append(course)

    def enter_marks(self):
        student_id = input("Enter student ID for mark entry: ")
        course_id = input("Enter course ID for mark entry: ")
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if student and course:
            mark = input_module.input_marks(student, course)
            self.marks.append(mark)
        else:
            print("Invalid student or course ID.")

    def list_students(self):
        for student in self.students:
            output.print_student(student)

    def list_courses(self):
        for course in self.courses:
            output.print_course(course)

    def list_marks(self):
        for mark in self.marks:
            output.print_mark(mark)

    def run(self):
        while True:
            print("\n1. Add Student\n2. Add Course\n3. Enter Marks\n4. List Students\n5. List Courses\n6. List Marks\n7. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_course()
            elif choice == '3':
                self.enter_marks()
            elif choice == '4':
                self.list_students()
            elif choice == '5':
                self.list_courses()
            elif choice == '6':
                self.list_marks()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()
