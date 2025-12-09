# INHERITANCE
# EXAMPLE.1
class Car():
    def __init__(self,colour,year,brand):
        self.colour = colour
        self.year = year
        self.brand = brand

class Audi(Car):
    def __init__(self, colour, year, brand,race):
        super().__init__(colour, year, brand)
        self.race = race
    def printd(self):
        print(self.colour,self.year,self.brand,self.race)    

obj1 = Audi("red",1970,"BMW",120)    
obj1.printd()

# EXAMPLE.2
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, graduation_year):
        super().__init__(name, age)
        self.graduation_year = graduation_year
    def printd(self):
        print(self.name,self.age,self.graduation_year)

obj1 = Student("alok",21,2025)
obj1.printd()

# POLYMORPHISM
class Bike():
    def __init__(self,brand):
        self.brand = brand
    def move(self):
        print(self.brand)

class Boat():
    def __init__(self,model):
        self.model = model   
    def move(self):
        print(self.model)

class Plane():
    def __init__(self,name):
        self.name = name 
    def move(self):
        print(self.name)

Bike1 = Bike("Honda")
Boat1 = Boat("Speed_boat")
Plane1 = Plane("Air_india")   

for x in(Bike1,Boat1,Plane1):
    x.move()


    



        
       
        