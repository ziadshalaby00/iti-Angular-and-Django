from students_module import *
from courses_module import *
from students_courses_module import *

print("Welcome, please choose from the list what you want")

while True :
    
    print("""
[1]  adding new student 
[2]  show all students 
[3]  adding new course        
[4]  show all courses 
[5]  adding course to student
""")

    choise = input(": ")
    while True :
        if choise.isdigit() and int(choise) > 0 and int(choise) < 6 :
            break
        else :
            choise = input("pls enter number from 1 , 2 , 3 , 4 or 5 : ")

    choise = int(choise)

    if choise == 1 :
        name = input("pls enter your name : ")
        age = input("pls enter your age : ")
        email = input("pls enter your email : ")
        returendID = addStudent(name, age, email)
        print("=============================================")
        print(f"id is {returendID}")
        print("=============================================")
        
    elif choise == 2 :
        print("=============================================")
        showStudents()
        print("=============================================")
        
    elif choise == 3 :
        name = input("pls enter name course : ")
        max_grade = input("pls enter max_grade : ")
        returendID = addCourses(name, max_grade)
        print("=============================================")
        print(f"id is {returendID}")
        print("=============================================")
        
    elif choise == 4 :
        print("=============================================")
        showCourses()
        print("=============================================")
        
    elif choise == 5 :
        course_id = input("pls enter course_id : ")
        student_id = input("pls enter student_id : ")
        grade = input("pls enter grade : ")
        returendDec = addNewCourse(course_id, student_id, grade)
        print("=============================================")
        showSpeceficCourse(int(returendDec["course_id"]))
        showSpeceficStudent(int(returendDec["student_id"]))
        print(returendDec["grade"])
        print("=============================================")