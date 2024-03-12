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
