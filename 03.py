# DATA TYPES

#NUMBER
x=5
print(x)

y=22.5
print(y)

z=(1+3j)
print (z)

#TYPE CASTING
x= "10"
y=int(x)
print(y+5)

#STRING
x= 'Hello'
print(x)

x= "Hello"
print(x)

x= '''Hello 
      world'''
print(x)

#STRING SLICE
x="Hello"
print(x[1:5])

#MODIFY STRING
x="hello"
y=x.upper()
print(y)

#SPLIT
x="Hello"
y=x.split('e')
print(y)

#QUESTIONS
#01.sum of two numbers
x=int(input(" "))
y=int(input(" "))
print(x+y)

#02.convert hello to Hello
x="hello"
y=x[0]
z=y.upper()
y1= x[1:5]
z1=z+y1
print(z1)

#03.convert helloworld to helloWorld
x="helloworld"
y=x[5]
z=y.upper()
y1=x[0:5]
z1=x[6:10]
z2=y1+z+z1
print(z2)

#04.convert"hello world into uppercase
x="hello world"
y=x.upper()
print(y)

#05."PYTHON PROGRAMMING" convert into lower case
x="PYTHON PROGRAMMING"
y=x.lower()
print(y)

#06." apple,banana,grapes "strip spaces and then split using comma
x=" apple,banana,grapes "
y= x.strip()
x1=y.split(',')
print(x1)

#07."PythonIsAwesome"print only Python using slicing
x="PythonIsAwesome"
y=x[0:6]
print(y)

#08."banana" count how many times 'a' appears
x="banana"
print(x.count('a'))

#09."I love Python Programming" print python from here
x="I love Python Programming"
y=x[7:13]
print(y)

#10."HELLO"convert string into lower
x="HELLO"
y=x.lower()
print(y)

#11." welcome to python " remove leading and trailing spaces
x=" welcome to python "
y= x.strip()
print(y)

#12."apple orange mango" split the string by spaces into the list
x="apple orange mango"
y=x.split(' ')
print(y)

#13."DataScience"print characters from index 4 to 9 using slicing
x="DataScience"
y=x[4:10]
print(y)