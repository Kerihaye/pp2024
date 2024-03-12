student = []
courses = []
marks = []

#input student in4
def input_student_in4():
    student_name = input("Name: ")
    student_id = input("Student ID: ")    
    student_date_of_birth = input("Date of birth (example: dd/mm/yyyy) : ")
    student.append((student_id,student_name,student_date_of_birth))
    num_courses = int(input("Number of courses: "))
    for _ in range(num_courses):
        input_course_in4(student_id)
        input_marks(student_id)

#input course in4
def input_course_in4(student_id):
    course_name = input("Name of the course: ")
    course_id = input("course ID: ")
    courses.append((course_id, course_name))
    marks.append((student_id, course_id, None))

#input marks of student
def input_marks(student_id):
    course_id = input("course ID: ") 
    mark = float(input("Mark: "))
    for i in range(len(marks)):
        if marks[i][0] == student_id and marks[i][1] == course_id:
            marks[i] = (student_id, course_id, mark)
            break

#list course
def list_course():
    for course in courses:
        print(f"ID:{course[0]}, Name:{course[1]}")
        
#list marks
def list_mark():
    for mark in marks:
        print(f"student ID:{mark[0]}, course ID:{mark[1]}, mark: {mark[2]}")

#main funct to drive prog
def main():
    while True:
        print("1.input student info")
        print("2.list students")
        print("3.list courses")
        print("4.list marks")
        print("5.exit")
        option = int(input("Select an option: "))
        if option == 1:
            input_student_in4()
        elif option == 2:
            list_students()
        elif option == 3:
            list_courses()
        elif option == 4:
            list_marks()
        elif option == 5:
            break
        else:
            print("No option valid. Try again")

#run main funct
if __name__ == "__main__":
    main()
