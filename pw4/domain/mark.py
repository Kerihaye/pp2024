class Mark:
    def __init__(self, student, course, mark=None):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"Student ID: {self.student.student_id}, Course ID: {self.course.course_id}, Mark: {self.mark:.1f}"
