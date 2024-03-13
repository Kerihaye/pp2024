import math
from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def input_student_info():
    student_id = input("Student ID: ")
    student_name = input("Name: ")
    student_dob = input("Date of birth (example: dd/mm/yyyy): ")
    return Student(student_id, student_name, student_dob)

def input_course_info():
    course_id = input("Course ID: ")
    course_name = input("Name of the course: ")
    credits = int(input("Credits for the course: "))
    return Course(course_id, course_name, credits)

def input_marks(student, course):
    mark = float(input(f"Enter the mark for student {student.student_id} in course {course.course_id}: "))
    return Mark(student, course, math.floor(mark * 10) / 10)
