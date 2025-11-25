# SORT
data = [100,500,90,1,29]
data.sort()
print(data)

# REVERSE PRINT
data.sort(reverse=True)
print(data)

# SORTING A LIST
data = ["ram","shyam","hari"]
data.sort()
print(data)

# ADDING TWO LIST USING DIFFERENT METHODS
list_1 =[1,2,3,4,5,6]
list_2 =[7,8,9,10,11]

# method.1
list_1.extend(list_2)
print(list_1)

# method.2
list_1 =[1,2,3,4,5,6]
list_3 = list_1 + list_2
print(list_3)

# method.3
for x in list_2:
    list_1.append(x)
print(list_1)

# GLOBAL VARIABLE
x = 10
def func():
    global x
    x = 11
    print(x)

func()
print(x)

# LOCAL VARIABLE
y = 10
def funct():
    y = 11
    print(y)

funct()
print(y)    

# TUPLE
# 01
x = ("ram","shyam",5,4)
y = list(x)
y.append("ravi")
x = tuple(y)
print(x)

# 02
for i in x:
 if i == "shyam":
    print("yes")

# UNPACKING

# method 1
x = ("ravi","ram","shyam")
(a,b,c) = x

print(a)
print(b)
print(c)

# method 2
y = x[0]
z = x[1]
z1 = x[2]

print(y)
print(z)
print(z1)
