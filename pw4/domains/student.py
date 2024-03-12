from .person import Person
import math
import numpy as np

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
