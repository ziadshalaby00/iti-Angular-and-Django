def VowelsRemoval(content) :
    content = content.lower()
    list = ['a','e','o','u','i']
    newContent = ""
    isNotVowel = True
    for item in content :
        for Vowel in list :
            if(item == Vowel) :
                isNotVowel = False
                break
            
        if  isNotVowel : 
            newContent += item  
            
        isNotVowel = True
    return newContent

print(VowelsRemoval("iiaaoouuee z z z z"))

########################

def findChar(content, char) :
    list = []
    for index, item in enumerate(content) :
        if item == char :
            list.append(index)
    return list

print(findChar("This is javaScript", 'i'))

########################

def MultiplicationTable(num) :
    mainList = []
    
    for i in range(1, num+1, 1) :
        smallList = []
        for k in range(1, i+1, 1) :
            smallList.append(k*i)
        mainList.append(smallList)
    
    return mainList

print(MultiplicationTable(3))

########################

def CalculateArea(char, num1, num2=1) :
    if char == 't' : 
        return 0.5 * num1 * num2 
    if char == 'r' and num2 != 1 :
        return num1 * num2 
    if char == 'r' and num2 == 1 :
        return num1 * num1
    if char == 'c' and num2 == 1 :
        return 22/7 * num1 * num1
    
print(CalculateArea("r", 10))

########################

def  convertToDirctory(list) :
    list = sorted(list)
    dec = {}
    for item in list :
        dec[item[0]] = item
    
    return dec

print(convertToDirctory(["ziad", "ahmed", "shalaby"]))

########################

def Pyramid(num) :
    for i in range(1, num+1) :
        line = ""
        for k in range(i,num+1) :
            line += " "
        for k in range(1,i+1) :
            line += "*"  
            
        print(line)

Pyramid(4)

########################