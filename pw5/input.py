def get_student_info():
    student_id = input("Student ID: ")
    name = input("Name: ")
    date_of_birth = input("Date of birth (example: dd/mm/yyyy): ")
    return student_id, name, date_of_birth

def get_course_info():
    course_id = input("Course ID: ")
    name = input("Name of the course: ")
    credit = int(input("Credit of the course: "))
    return course_id, name, credit

def get_mark_info():
    student_id = input("Student ID: ")
    course_id = input("Course ID: ")
    mark = float(input("Mark: "))
    return student_id, course_id, mark

def read_students(filename):
    students = {}
    with open(filename, 'r') as file:
        for line in file:
            student_id, name, date_of_birth = line.strip().split(',')
            students[student_id] = {'name': name, 'date_of_birth': date_of_birth}
    return students

def read_courses(filename):
    courses = {}
    with open(filename, 'r') as file:
        for line in file:
            course_id, name, credit = line.strip().split(',')
            courses[course_id] = {'name': name, 'credit': int(credit)}
    return courses

def read_marks(filename):
    marks = {}
    with open(filename, 'r') as file:
        for line in file:
            student_id, course_id, mark = line.strip().split(',')
            if student_id not in marks:
                marks[student_id] = {}
            marks[student_id][course_id] = float(mark)
    return marks

students_data = read_students('students.txt')
courses_data = read_courses('courses.txt')
marks_data = read_marks('marks.txt')
