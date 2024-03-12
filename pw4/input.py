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
