################### TASK (2) ###################
import json
import uuid

class Person() :
    def __init__(self,name,money) :
        self.name = name
        self.money = money
        self.mood = None
        self.healthRate = None
        
    def sleep(self,hours) :
        if(hours == 7) :
            self.mood = "happy"
        elif (hours < 7) :
            self.mood = "tired"
        elif (hours > 7) :
            self.mood = "Lazy"
        return self.mood

    def eat(self,meals) :
        if (meals == 3) :
            self.healthRate = "100% hth"
        elif (meals == 2) :
            self.healthRate = "75% hth"
        elif (meals == 1) :
            self.healthRate = "50% hth"
        return self.healthRate

    def buy(self,items) :
        self.money -= items * 10
        return self.money
    
    
class Employee(Person) :
        def __init__(self, name, money, car, email, salary, distanceToWork) :
            super().__init__(name,money)

            self.id = str(uuid.uuid4())
            print(self.id )
            
            self.salary = salary
            self.car = car
            self.email = email
            self.distanceToWork = distanceToWork
        
        def work(self,hours) :
            if(hours == 8) :
                self.mood = "happy"
            elif (hours < 8) :
                self.mood = "lazy"
            elif (hours > 8) :
                self.mood = "tired"
            return self.mood
        
        def drive(self,velocity) :
            self.car.run(velocity, self.distanceToWork)
            
        def refuel(self, gasAmount = 100): 
            self.car.fuelRate += gasAmount
            
        def send_mail(self,to, subject, msg, receiver_name) :
            file = open("EmailFile.md", 'w')
            file.write(
f"""From: {self.email}
To: {to}

    Hi, {subject}
    {msg}
{receiver_name}""")
            

class Car() :
    def __init__(self,name, fuelRate) :
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = None
        
    def run(self, velocity, distance) :
        if(velocity > 200 or velocity < 0) :
            print("velocity must be between 0 and 200")
            return
        
        self.velocity = velocity
        self.fuelRate -= 10 * (distance/10)
        
        if(self.fuelRate <= 0) :
            distanceRem = -self.fuelRate
            Car.stop(distanceRem)
        elif self.fuelRate >= 0:
            Car.stop(0)
            
    def stop(self,distanceRem) :
        self.velocity = 0
        if(distanceRem == 0) :
            print("The car stopped because you arrived to the work.")
        else :
            print("The car stopped because the fuelRate was finished.")
            print(f"The distance before the workplace is: {distanceRem} km")

class Office() :
    employeesNum = None
    name = None
    employees = []
    
    @classmethod
    def setEmployeesInJsonFile(cls) :
        cls.employeesNum = len(cls.employees)
        
        listEmployees = [] # list of dec (json)
        for item in cls.employees :
            decModal = {
                            "ID" : item.id,
                            "name" : item.name,
                            "money" : item.money,
                            "mood" : item.mood,
                            "healthRate" : item.healthRate,
                            "email" : item.email,
                            "salary" : item.salary,
                            "distanceToWork" :item.distanceToWork,
                            "car" : {
                                "name" : item.car.name,
                                "fuelRate" : item.car.fuelRate,
                                "velocity" : item.car.velocity
                            }
                        }
            listEmployees.append(decModal)
    
            file = open("lap4/office.Json", "w")
            json.dump({cls.name : listEmployees}, file, indent=4)
            
    @classmethod
    def get_all_employees(cls) :
        file = open("lap4/office.Json", "r")
        file = json.load(file)
        key = list(file.keys())[0]
        return file[key]
    
    @classmethod
    def get_employee(cls,id) :
        file = open("lap4/office.Json", "r")
        file = json.load(file)
        key = list(file.keys())[0]
        employeesList = file[key]
        for item in employeesList :
            if item["ID"] == id :
                return item
            
    @classmethod        
    def hire(cls,employee) :
        cls.employees.append(employee)
        Office.setEmployeesInJsonFile()
    
    @classmethod 
    def fire(cls,id) :
        for index, item in enumerate(cls.employees) :
            if item.id == id : 
                cls.employees.pop(index)
                Office.setEmployeesInJsonFile()
                break
            
    @classmethod
    def deduct(cls, id, deduction) :
        for index, item in enumerate(cls.employees) :
            if item.id == id : 
                cls.employees[index].salary -= deduction
                Office.setEmployeesInJsonFile()
                break   
            
    @classmethod
    def reward(cls, id, deduction) :
        for index, item in enumerate(cls.employees) :
            if item.id == id : 
                cls.employees[index].salary += deduction
                Office.setEmployeesInJsonFile()
                break
            
#* Module Finished
#* Developed by: Ziad Ahmed Shalaby