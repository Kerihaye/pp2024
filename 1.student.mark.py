def input_student_info():
    student_id = input("Student ID: ")
    student_name = input("Name: ")
    student_dob = input("Date of birth (example: dd/mm/yyyy): ")
    return student_id, student_name, student_dob

def input_course_info():
    course_id = input("Course ID: ")
    course_name = input("Name of the course: ")
    return course_id, course_name

def input_marks(student_id, course_id):
    mark = float(input(f"Enter the mark for student {student_id} in course {course_id}: "))
    return mark

def list_students(students):
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def list_courses(courses):
    for course in courses:
        print(f"Course ID: {course[0]}, Name: {course[1]}")

def list_marks(marks):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    for mark in marks:
        if mark[0] == student_id and mark[1] == course_id:
            print(f"Student ID: {mark[0]}, Course ID: {mark[1]}, Mark: {mark[2]}")
            break
    else:
        print("No marks found for the specified student and course.")

def main():
    students = []
    courses = []
    marks = []

    while True:
        print("1. Input student info")
        print("2. List students")
        print("3. List courses")
        print("4. List marks")
        print("5. Exit")
        option = int(input("Select an option: "))

        if option == 1:
            student_id, student_name, student_dob = input_student_info()
            students.append((student_id, student_name, student_dob))
            num_courses = int(input("Number of courses: "))
            for _ in range(num_courses):
                course_id, course_name = input_course_info()
                courses.append((course_id, course_name))
                marks.append((student_id, course_id, None))
                mark = input_marks(student_id, course_id)
                for i in range(len(marks)):
                    if marks[i][0] == student_id and marks[i][1] == course_id:
                        marks[i] = (student_id, course_id, mark)
                        break
        elif option == 2:
            list_students(students)
        elif option == 3:
            list_courses(courses)
        elif option == 4:
            list_marks(marks)
        elif option == 5:
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
