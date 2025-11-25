# APPEND
x=["ram","shyam"]
x.append("ravi")
print(x)

# INSERT
x=["ram","shyam"]
x.insert(1,"ravi")
print(x)

# UPDATE
x=["ram","shyam"]
x[0]="ravi"
print(x)

# EXTEND
x=["ram","shyam"]
y=["ravi","hari"]
x.extend(y)
print(x)

# POP
x=["ram","shyam"]
x.pop()
print(x)

# REMOVE
x=["ram","shyam"]
x.remove("shyam")
print(x)

# CLEAR
x=["ram","shyam"]
x.clear()
print(x)

# DELETE
x=["ram","shyam"]
del x[1]
print(x)

# QUESTIONS
# 01.print list
mylist = ["mango","banana","apple","orange"]
for i in mylist:
    print(i)

# 02.print list by taking user input
list = []
while True:
    if len(list)==5:
        break
    else:
        x=int(input("enter your number"))
        list.append(x)
print(list)       

# 03.print list by adding 10
x=[5,10,15,20,25,30]
for i in range(0,len(x)):
    x[i] = x[i] + 10
print(x)    

# 04.print list by adding 5 in even number and 10 in odd numbers
x=[5,10,15,20,25,30]
for i in range(0,len(x)):
    if x[i]%2==0:
        x[i]=x[i]+5
    else:
        x[i]=x[i]+10
print(x)            

# 05.print even number between 1 to 50
list=[]
for i in range(1,51):
    if i%2==0:
        list.append(i)
print(list)        


