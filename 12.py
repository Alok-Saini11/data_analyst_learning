# CLASS/OBJECT

# EXAMPLE.1
class car:
    car = " "
obj1 = car()
obj1.car = "audi"
print(obj1.car)    

obj2 = car()
obj2.car = "BMW"
print(obj2.car)

# EXAMPLE.2
class person:
  def __init__(self,name,age):
     self.name = name
     self.age = age

  def printd(self):
   print(self.name, self.age)
   print("detail")

user1 = person("alok",25)
user2 = person("ravi",23)

user1.printd()
user2.printd()

# EXAMPLE.3
class Car:
   def __init__(self,brand,year,race):
      self.brand = brand
      self.year = year
      self.race = race

   def printD(self):
      print(self.brand)
      print(self.year)
      print(self.race)

car1 = Car("mustang",1969,150)
car2 = Car("audi",1970,250)
car3 = Car("bmw",1999,300)

car3.printD()

# EXAMPLE.4
class Person:
   def __init__(self,firstname,lastname,age,gender):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.gender = gender
   def details(self):
      print(self.firstname)
      print(self.age)

person1 = Person("ravi","sharma",15,"male")
person2 = Person("ram","kumar",12,"male")       

person2.details()

# EXAMPLE.5
class Person1:
   def __init__(self,age):
      self.age = age
      
   def check(self):
     if self.age % 2 == 0:
        print("even")
     else:
        print("odd") 

age = int(input("enter your age"))
x = Person1(age)
x.check()

# EXAMPLE.6
class Calculator:
   def __init__(self,a,b):
      self.a = a
      self.b = b

   def sum(self):
      print(self.a + self.b)   
   def sub(self):
      print(self.a - self.b)
   def divide(self):
      print(self.a / self.b)      
   def modulus(self):
      print(self.a % self.b)   

x = int(input("enter your number"))
y = int(input("enter your number"))      

obj = Calculator(x,y)
obj.sum()
obj.sub()
obj.divide()
obj.modulus()