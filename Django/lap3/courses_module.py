# الموديل يشبه جدا الموديل الخاص الطلاب

# This module will contain 3 main functions,
# one for displaying courses,
# one for adding a course.
# and one for show specefic course.

import os
# هستخدمها عشان اجيب مسار الملف بس عشان يقدر يشتغل على اى جهاز
file_path = os.path.join(os.path.dirname(__file__), "Courses.csv")


# displaying Courses from Courses.csv
def showCourses() :
    file = open(file_path, "r")
    for item in file.readlines() :
        item = item.replace("\n","").replace(","," ")
        print(item)

# adding new Courses with uniqe ID 
def addCourses(name, max_grade) :
    file = open(file_path, "r")
    file = file.readlines()
    newId = int(file[len(file)-1].split(",")[0]) + 1 # ال اى دى الجديد هو اخر اى دى زائد واحد
    
    file = open(file_path, "a")
    file.write(f"{newId},{name},{max_grade}\n")
    return newId

# show specefic course
def showSpeceficCourse(id) :
    file = open(file_path, "r")
    file = file.readlines()
    for item in file :
        if not item[0].isdigit() : continue
        if(int(item[0]) == id) :
            print(item)
            break

# this module is finished 
# programed by ziad ahmed shalaby