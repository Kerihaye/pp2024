class Student:
    #Initialize the Student class
    def __init__(self, student_id, name, date_of_birth):
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.marks = {}
    
    #Method to add mark for a course
    def add_mark(self, course, mark):
        self.marks[course] = mark

    #Method to get mark for a course
    def get_mark(self, course):
        return self.marks.get(course, 0)


class Course:
    #Initialize the Course class
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class School:
    #Initialize the School class
    def __init__(self):
        self.students = []
        self.courses = []

    #Method to add student from the user
    def add_student(self, student):
        self.students.append(student)

    #Method to add course from the user
    def add_course(self, course):
        self.courses.append(course)

    #Method to get student by their id
    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    #Method to get course by course id
    def get_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    #Method to list student
    def list_students(self):
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}")

    #Method to list course
    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    #Method to list mark
    def list_marks(self):
        for student in self.students:
            for course, mark in student.marks.items():
                print(f"Student ID: {student.student_id}, Course ID: {course.course_id}, Mark: {mark}")


def main():
    school = School()
    #Menu for user to select their option 
    while True:
        print("1. Input student info")
        print("2. Input course info")
        print("3. Input mark")
        print("4. List students")
        print("5. List courses")
        print("6. List marks")
        print("7. Exit")
        option = int(input("Select an option: "))
        #Option1
        if option == 1:
            student_id = input("Student ID: ")
            name = input("Name: ")
            date_of_birth = input("Date of birth (example: dd/mm/yyyy): ")
            student = Student(student_id, name, date_of_birth)
            school.add_student(student)
        #Option2
        elif option == 2:
            course_id = input("Course ID: ")
            name = input("Name of the course: ")
            course = Course(course_id, name)
            school.add_course(course)
        #Option3
        elif option == 3:
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            mark = float(input("Mark: "))
            student = school.get_student(student_id)
            course = school.get_course(course_id)
            if student and course:
                student.add_mark(course, mark)
        #Option4
        elif option == 4:
            school.list_students()
        #Option5
        elif option == 5:
            school.list_courses()
        #Option6
        elif option == 6:
            school.list_marks()
        #Option7
        elif option == 7:
            break
        else:
            print("No option valid. Try again")

#Entry point of the program
if __name__ == "__main__":
    main()
