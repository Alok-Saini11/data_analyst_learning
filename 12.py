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

