##########################################
########### (1) Keep Hydrated! ###########
##########################################
def litres(time):
    return int(time/2)
    # return time // 2
    # return time/2 - time/2 % 1

print(litres(4.5))

#########################################
########### (2) Invert values ###########
#########################################
def invert(lst):
    # for i in range(0,len(lst)) :
    #     lst[i] = -lst[i]
    # return lst # تقوم بتغيير الدالة الاصلية

    return [-item for item in lst] # هنا نقوم بتعديل قيمة منسوخة ولكن نقوم بارجاعها
   
    # for item in lst :
    #   item = -item
    # return lst هذة الطريقة خاظئة لانها تقوم بتعديل القيمة المنسوخة فقط والاراى الاساسية لا تعدل

print(invert([1,2,3,4,5]))

#############################################
########### (3) Century From Year ###########
#############################################
def century(year):
    return ((year-1) // 100) + 1

print(century(1705))

#####################################################
########### (4) Third Angle of a Triangle ###########
#####################################################
def other_angle(a, b):
    return 180 - a - b

print(other_angle(30,60))

#########################################################
########### (5) Convert a String to a Number! ###########
#########################################################
def string_to_number(s):
    result = 0
    p = len(s) - 1
    
    for item in s :
        if(item == '-') : 
            p -= 1
            continue
        result += (ord(item) - 48) * (10**p)
        p -= 1
    if(s[0] == '-') : result = -result
    return result

print(string_to_number("-123"))

#########################################
########### (6) L1: Set Alarm ###########
#########################################
def set_alarm(employed, vacation):
    if(employed == vacation) : return False
    else : return employed
    
print(set_alarm(False, True))

#######################################
########### (7) Even or Odd ###########
#######################################
def even_or_odd(number):
    if(number % 2 == 0) : return "Even"
    else : return "Odd"
    
print(even_or_odd(10))

#########################################
########### (8) Square(n) Sum ###########
#########################################
def square_sum(numbers):
    return sum(item**2 for item in numbers)
    # result = 0
    # for item in numbers :
    #     result += item**2
    # return result

print(square_sum([1,2,3]))

#######################################################
########### (9) Will there be enough space? ###########
#######################################################
def enough(cap, on, wait):
    if cap - on >= wait : return 0
    else : return wait - cap + on
    
print(enough(100,60,50))

################################################
########### (10) Get Nth Even Number ###########
################################################
def nth_even(n):
    return n*2 - 2

print(nth_even(100))

#########################################
########### (11) Twice as old ###########
#########################################
def twice_as_old(dad_years_old, son_years_old):
    return  abs(dad_years_old - son_years_old*2)

print(twice_as_old(42,21))

##############################################
########### (12) Can we divide it? ###########
##############################################
def is_divide_by(number, a, b):
    return (number%a == number%b == 0)

print(is_divide_by(-12,2,-6))

##########################################################
########### (13) Calculate Price Excluding VAT ###########
##########################################################
def excluding_vat_price(price):
    return (100 * price / 115) if price != None else -1

print(excluding_vat_price(230.00))

############################################
########### (14) Fuel Calculator ###########
############################################
def fuel_price(litres, price_per_litre):
    dis =  25 * litres if litres > 10 else int(litres * 5 /2) * litres
    return litres*price_per_litre - dis/100

print(fuel_price(7, 8.5))

####################################
########### (15) pillars ###########
####################################
def pillars(num_pill, dist, width):
    return 0 if num_pill < 2 else ((num_pill-1) * dist*100) + ((num_pill-2) * width)

print(pillars(2,10,10))

### Programed By Ziad Ahmed Shalaby ###