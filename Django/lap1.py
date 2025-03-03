
num = input("Enter number : ")
while(True) : 
    if num.isdigit() :
        num = float(num)
        break
    else : num = input("Pls enter number : ")
start = 15
end = 35

print(num >= start and num <= end)

########################

age = input("Enter age : ")
copon = input("Enter the coupon if you have it If you don't have it enter 0 : ")
age = int(age)
print(age < 18 or age > 65 or copon != '0')

#########################

name = input("Enter your name : ")
print(f"Hello, {name}")

######################

fullName = input("Enter your first and last name with a space between them : ")

fullName = fullName.split()
name = ""
for item in fullName :
    name += item[0]

print(name)

#################################

name = input("Enter your name : ")  
age = input("Enter you age : ")

print(f"{name} is {age} years old")
print("{name} is {age} years old".format(name=name, age=age))