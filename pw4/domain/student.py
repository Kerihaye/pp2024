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
