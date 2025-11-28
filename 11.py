# SET
# ACCESS ITEMS
x = { 1,2,3 }
if 1 in x:
    print(x)

# ADD ITEMS
x . add(4)    
print(x)

# REMOVE ITEM
x . remove(2)
print(x)

# ACCESS ITEM USING LOOP
for y in x:
    print(y)

# DICTIONARY 
x = { "brand":"volvo",
     "year": 1990, }
   
# ACCESS VALUES   
print(x['brand'])

# ACCESS KEYS
print(x.keys())
   
# ACCESS VALUES
print(x.values())

# UPDATE VALUES
x['year'] = 2000
print(x)

# CREATING A DICTIONARY USING CONSTRUCTOR
x = dict(name= "ravi",age = 17)
print(x)

# REMOVING A KEY
x . pop('age')
print(x) 

# DELETING A KEY
del x['name']
print(x)

# DELETE A DICTIONARY
del x

# ACCESS KEYS USING LOOP
x = { "brand":"volvo",
     "year": 1990, }

for i in x.keys():
    print(i)  

# ACCESS VALUES USING LOOP
for i in x.values():
    print(i)  

# ACESS ITEMS
data = { "brand":"volvo",
     "year": 1990, }
for x,y in data.items():
    print(x,y)   

# COPY DATA
data_1 = data.copy()
print(data_1)    

# SECOND METHOD TO COPY DATA
data_1 = dict(data)
print(data_1)

# NESTED DICTIONARY
data = {
    "user1":{
        "fname":"ravi",
        "lname":"singh" },
        
    "user2":{
         "fname":"ram",
         "lname":"saini"
        }
}

#  ACCESS VALUES USING LOOP
for i in data.values():
    for i1 in i.values():
        print(i1)

# QUESTIONS
''' Q1.get a number from user and a random number between 1 to 10 if both the numbers are equal print winner otherwise print looser'''
import random
x = int(input("enter a number between 0 to 10"))
y = random.randrange(0,10)
if x == y:
    print("winner")
else:
    print("looser")


'''
Q2. Unique Cities Finder
-------------------------------------------
cities = ["Delhi", "Mumbai", "Pune", "Delhi", "Pune", "Jaipur", "Mumbai"]

# Task:
# 1. List se unique cities ka set banao
# 2. Total unique cities count print karo

'''
cities = ["Delhi", "Mumbai", "Pune", "Delhi", "Pune", "Jaipur", "Mumbai"]
# TASK 1
x = set(cities)
print(x)
print(type(x))

# TASK 2
print(len(x))

'''
 Q3. Remove Duplicates from List Using Set
-------------------------------------------
nums = [1, 2, 3, 2, 4, 1, 5, 3, 6, 5]

# Task:
# 1. Set use karke duplicates remove karo
# 2. Result ko wapas list me convert karke print karo
'''
# TASK 1
nums = [1, 2, 3, 2, 4, 1, 5, 3, 6, 5]
x = set(nums)
print(x)
print(type(x))

# TASK 2
y = list(x)
print(y)
print(type(y))

'''
Q4. Count Word Frequency (Dictionary)
-------------------------------------------
text = "apple mango apple orange mango apple"

# Task:
# 1. Ek dictionary banao jisme:
#    key = word, value = word count
# 2. Output: {'apple': 3, 'mango': 2, 'orange': 1}

'''
# TASK 
text = "apple mango apple orange mango apple"
x = text.split(" ")
this_dict = {}
for i in x:
    if i in this_dict:
        this_dict[i] += 1
    else:
        this_dict[i] = 1
print(this_dict) 
print(type(this_dict))     

'''
Q5. Student Marks Dictionary
-------------------------------------------
marks = {
    "Ajay": 85,
    "Rohit": 92,
    "Simran": 78,
    "Neha": 90
}

# Task:
# 1. Sab students ke names print karo
# 2. Average marks print karo
# 3. Highest marks laane wale student ka naam print karo
'''
# Task 1
marks = {

    "Ajay": 85,
    "Rohit": 92,
    "Simran": 78,
    "Neha": 90
}

sum = 0
for i in marks.keys():
    print(i)

# TASK 2    
    sum += marks[i]
avg = sum/len(marks)
print(avg)    

# TASK 3
highest_marks = 0
highest_name = ""
for i in marks.keys():

    if marks[i] > highest_marks:
        highest_marks = marks[i]
        highest_name = i

print(highest_name,highest_marks)

'''
Q6. Price Updater
-------------------------------------------
prices = {
    "pen": 10,
    "pencil": 5,
    "notebook": 50
}

# Task:
# 1. Sab items ki price 10% badhao
# 2. Nayi dictionary print karo (Example: pen -> 11, pencil -> 5.5)
'''
# TASK 
prices = {
    "pen": 10,
    "pencil": 5,
    "notebook": 50
}
this_dict = {}
for i,j in prices.items():
    x = j + (j * 0.10)
    this_dict[i] = x
print(this_dict)    


