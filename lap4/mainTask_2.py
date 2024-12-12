################### TASK (2) ###################

from Task_2 import *

Employee1 = Employee("ziad",2000,Car("Fiat 128",100),"shalabyziad94@gmail.com",3000,20)
Employee2 = Employee("ahmed",2000,Car("Fiat 128",100),"shalabyziad94@gmail.com",3000,20)
Employee3 = Employee("mohamed",2000,Car("Fiat 128",100),"shalabyziad94@gmail.com",3000,20)
Employee4 = Employee("ali",2000,Car("Fiat 128",100),"shalabyziad94@gmail.com",3000,20)
Employee5 = Employee("sameer",2000,Car("Fiat 128",100),"shalabyziad94@gmail.com",3000,20)

Office.name = "iti_office"
Office.employees = [Employee1, Employee2, Employee3]
Office.setEmployeesInJsonFile()


# Office.fire(Employee2.id)


# Office.hire(Employee4)
# Office.hire(Employee5)


# print(Office.employeesNum)


# Office.deduct(Employee2.id, 500)
# print(Employee2.salary)


# Office.reward(Employee3.id, 700)
# print(Employee3.salary)



# for item in  Office.get_all_employees() :
#     print("============================")
#     for itemInner in item :
#         print(f"{itemInner} is: {item[itemInner]}")


# print("============================")
# print(Office.get_employee("456fb154-b055-4b80-8f68-1d87a47dd423"))


# Employee1.send_mail(
# "ziad1@gmail.com",
# "mohamed",
#     """
#     Lorem Ipsum is simply dummy text of the 
#     printing and typesetting industry. Lorem 
#     Ipsum has been the industry's standard 
#     dummy text ever since the 1500s, when 
#     an unknown printer took a galley of 
#     type and scrambled it to make a type 
#     specimen book. It has survived not only 
#     five centuries, but also the leap into 
#     electronic typesetting, remaining essentially 
#     unchanged. It was popularised in the 1960s with 
#     the release of Letraset sheets containing Lorem 
#     Ipsum passages, and more recently with desktop 
#     publishing software like Aldus PageMaker including 
#     versions of Lorem Ipsum. 
#     """,
# "ziad")

#* Module Finished
#* Developed by: Ziad Ahmed Shalaby