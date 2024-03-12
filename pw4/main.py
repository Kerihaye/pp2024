from input import get_student_info, get_course_info, get_mark_info
from output import init_screen, print_menu, end_screen
from domains.student import Student
from domains.course import Course
from domains.school import School

def main():
    stdscr = init_screen()
    school = School()
    while True:
        print_menu(stdscr)
        option = int(stdscr.getstr().decode())
        if option == 1:
            student_id, name, date_of_birth = get_student_info()
            student = Student(student_id, name, date_of_birth)
            school.add_student(student)
        elif option == 2:
            course_id, name, credit = get_course_info()
            course = Course(course_id, name, credit)
            school.add_course(course)
        elif option == 3:
            student_id, course_id, mark = get_mark_info()
            student = school.get_student(student_id)
            course = school.get_course(course_id)
            if student and course:
                student.add_mark(course, mark, course.credit)
        elif option == 4:
            school.list_students()
        elif option == 5:
            school.list_courses()
        elif option == 6:
            school.list_marks()
        elif option == 7:
            break
        else:
            print("No option valid. Try again")
    end_screen()

if __name__ == "__main__":
    main()
