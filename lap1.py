
num = input("Enter number : ")
while(True) : 
    if num.isdigit() :
        num = float(num)
        break
    else : num = input("pls enter number : ")
start = 15
end = 35

print(num >= start and num <= end)

########################

age = input("Enter age : ")
copon = input("Enter copon if you have if you dont enter 0 : ")

print(int(age) < 18) or (int(age) > 65) or (copon != '0')

#########################

name = input("enter your name : ")
print(f"Hello, {name}")

######################

fullName = input("enter first and last name with space between them : ")

fullName = fullName.split()
name = ""
for item in fullName :
    name += item[0]

print(name)

#################################

name = input("enter your name : ")
age = input("enter you age : ")

print(f"{name} is {age} years old")
print("{name} is {age} years old".format(name=name, age=age))