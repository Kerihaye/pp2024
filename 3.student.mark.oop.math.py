import curses
import math
import numpy as np

class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.student_name}, Date of Birth: {self.student_dob}"

class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Credits: {self.credits}"

class Mark:
    def __init__(self, student, course, mark=None):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"Student ID: {self.student.student_id}, Course ID: {self.course.course_id}, Mark: {self.mark:.1f}"

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_info(self):
        student_id = input("Student ID: ")
        student_name = input("Name: ")
        student_dob = input("Date of birth (example: dd/mm/yyyy): ")
        return Student(student_id, student_name, student_dob)

    def input_course_info(self):
        course_id = input("Course ID: ")
        course_name = input("Name of the course: ")
        credits = int(input("Credits for the course: "))
        return Course(course_id, course_name, credits)

    def input_marks(self, student, course):
        mark = float(input(f"Enter the mark for student {student.student_id} in course {course.course_id}: "))
        return Mark(student, course, math.floor(mark * 10) / 10)  # Round down to 1 decimal place

    def calculate_gpa(self, student):
        total_credits = 0
        weighted_sum = 0
        for mark in self.marks:
            if mark.student == student:
                total_credits += mark.course.credits
                weighted_sum += mark.course.credits * mark.mark
        return weighted_sum / total_credits if total_credits > 0 else 0

    def list_students(self):
        for student in self.students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)

    def list_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        for mark in self.marks:
            if mark.student.student_id == student_id and mark.course.course_id == course_id:
                print(mark)
                break
        else:
            print("No marks found for the specified student and course.")

    def list_students_by_gpa(self):
        sorted_students = sorted(self.students, key=self.calculate_gpa, reverse=True)
        for student in sorted_students:
            print(f"{student} - GPA: {self.calculate_gpa(student):.2f}")

    def main(self):
        while True:
            print("1. Input student info")
            print("2. List students")
            print("3. List courses")
            print("4. List marks")
            print("5. List students by GPA")
            print("6. Exit")
            option = int(input("Select an option: "))

            if option == 1:
                student = self.input_student_info()
                self.students.append(student)
                num_courses = int(input("Number of courses: "))
                for _ in range(num_courses):
                    course = self.input_course_info()
                    self.courses.append(course)
                    mark = self.input_marks(student, course)
                    self.marks.append(mark)
            elif option == 2:
                self.list_students()
            elif option == 3:
                self.list_courses()
            elif option == 4:
                self.list_marks()
            elif option == 5:
                self.list_students_by_gpa()
            elif option == 6:
                break
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    student_management = StudentManagement()
    student_management.main()
