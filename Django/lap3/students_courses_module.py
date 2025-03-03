# This module will contain one main function,
# for adding course to specefic student,

import os
# هستخدمها عشان اجيب مسار الملف بس عشان يقدر يشتغل على اى جهاز
file_path = os.path.join(os.path.dirname(__file__), "Student_Course.csv")

# adding new course to specefic student
def addNewCourse(course_id, student_id, grade) :
    file = open(file_path, "a")
    file.write(f"{course_id},{student_id},{grade}\n")
    return {
        "course_id": course_id,
        "student_id": student_id,
        "grade": grade
    }

# this module is finished
# programed by ziad ahmed shalaby