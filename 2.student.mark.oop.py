class Person:
    # Initialize the Person class
    def __init__(self, id, name, date_of_birth):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth

    # Method to display person's information
    def display(self):
        raise NotImplementedError("Subclass must implement this method")


class Student(Person):
    # Initialize the Student class
    def __init__(self, student_id, name, date_of_birth):
        super().__init__(student_id, name, date_of_birth)
        self.marks = {}

    # Method to add a mark for a course
    def add_mark(self, course, mark):
        self.marks[course] = mark

    # Method to get the mark of a course
    def get_mark(self, course):
        return self.marks.get(course, 0)

    # Override the display method of Person
    def display(self):
        return f"ID: {self.id}, Name: {self.name}"


class Course:
    # Initialize the Course class
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class School:
    # Initialize the School class
    def __init__(self):
        self.students = []
        self.courses = []

    # Method to add a student
    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Invalid student")
        self.students.append(student)

    # Method to add a course
    def add_course(self, course):
        self.courses.append(course)

    # Method to get a student by their ID
    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    # Method to get a course by ID
    def get_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    # Method to list all students
    def list_students(self):
        for student in self.students:
            print(student.display())

    # Method to list all courses
    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    # Method to list marks
    def list_marks(self):
        for student in self.students:
            for course, mark in student.marks.items():
                print(f"Student ID: {student.id}, Course ID: {course.course_id}, Mark: {mark}")


def main():
    school = School()
    # Menu option 
    while True:
        print("1. Input student info")
        print("2. Input course info")
        print("3. Input mark")
        print("4. List students")
        print("5. List courses")
        print("6. List marks")
        print("7. Exit")
        option = int(input("Select an option: "))
        # Option 1
        if option == 1:
            student_id = input("Student ID: ")
            name = input("Name: ")
            date_of_birth = input("Date of birth (example: dd/mm/yyyy): ")
            student = Student(student_id, name, date_of_birth)
            school.add_student(student)
        # Option 2
        elif option == 2:
            course_id = input("Course ID: ")
            name = input("Name of the course: ")
            course = Course(course_id, name)
            school.add_course(course)
        # Option 3
        elif option == 3:
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            mark = float(input("Mark: "))
            student = school.get_student(student_id)
            course = school.get_course(course_id)
            if student and course:
                student.add_mark(course, mark)
        # Option 4
        elif option == 4:
            school.list_students()
        # Option 5
        elif option == 5:
            school.list_courses()
        # Option 6
        elif option == 6:
            school.list_marks()
        # Option 7
        elif option == 7:
            break
        # If user input another thing not 1 of 7 options
        else:
            print("No option valid. Try again")

# Entry point of the program
if __name__ == "__main__":
    main()
