# This file will contain 3 main functions,
# one for displaying students,
# one for adding a student.
# and one for show specefic student.

import os
# هستخدمها عشان اجيب مسار الملف بس عشان يقدر يشتغل على اى جهاز
file_path = os.path.join(os.path.dirname(__file__), "Students.csv")


# displaying students from students.csv
def showStudents() :
    file = open(file_path, "r")
    for item in file.readlines() :
        item = item.replace("\n","").replace(","," ")
        print(item)

# adding new student with uniqe ID 
def addStudent(name, age, email) :
    file = open(file_path, "r")
    file = file.readlines()
    newId = int(file[len(file)-1].split(",")[0]) + 1 # ال اى دى الجديد هو اخر اى دى زائد واحد
    
    file = open(file_path, "a")
    file.write(f"{newId},{name},{age},{email}\n")
    return newId

# show specefic student
def showSpeceficStudent(id) :
    file = open(file_path, "r")
    file = file.readlines()
    for item in file :
        if not item[0].isdigit() : continue
        if(int(item[0]) == id) :
            print(item)
            break

# this file is finished 
# programed by ziad ahmed shalaby