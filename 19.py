#indexing
import numpy as np
x = np.array([1,2,3,4,5])
print(x[0])
print(x[1])

#indexing in 2d array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[0,0])
print(arr[1,2])
print(arr[0])
print(arr[:,1])

#Slicing array
y = [1,3,8,6,9,6,7]
print(y)
print(y[1:4])
print(y[ :4])
print(y[::2])

#2D_Slicing
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[:2,:])
print(a[:,:2])
print(a[0:2,1:3])

#Advance Selection
b =np.array([2,4,6,8,10,12,14])
indices = [0,2,3,5]
print(b[indices])

#Advance Selection on 2D array
ar = np.array([[11,12,13],[14,15,16],[17,18,19]])
print(ar)
ind = ar[[0,2],[1,2]]
print(ind)

#Boolean indexing
x1 = np.array([10,20,30,40,50])
print(x1>30)
print(x1[x1>30])

ar1 = np.array([5,10,15,20,25,30])
print(ar1 % 2 == 0)
print(ar1[ar1 % 2 == 0])

ar1[(ar1<25) & (ar1>10)]
print(ar1)

#replace value with condition
arr1 =np.array([10,40,20,50,60])
arr1[arr1>20] = 0
print(arr1)

#not operator
arr2 = np.array([1,2,3,4,5,6,7,8,])
print(arr2[~((arr2<7) & (arr2>3))])

#Conditional replacement
data = np.array([35,45,47,33,96,12,97])
print(np.where(data < 36, "fail","pass"))

Pass = data[data>36]
print(Pass)

#Q.1 Create an array 10-50, print even number only, print number>30, replace number<20 to 0
t = np.arange(10,51)
print(t)

#even number only
print(t[t%2 == 0])

#number>30
print(t[t>30])

#replacing numbers
t[t>20]=0
print(t)


#Q.2 create 2d array of 1-12 by 3*4 matrix, print 2nd row, print 3rd row, print first 2 row and 3 col, extract value < 6
val = np.arange(1,13)
array =val.reshape(3,4)
print(array)

#print 2nd row only
print(array[1,:])

#print 3rd row
print(array[2,:])

#print first two row and three col
print(array[:2,:3])

#extract value < 6
print(array[array<6])


#Q.3 [25,60,45,80,35,90,55] print student who passed(mark>40), replace fail mark with 40, find average of new array
marks = np.array([25,60,45,80,35,90,55])
print(marks)

#students who passed in exam
print(marks[marks>40])

#replace fail marks with 40
marks[marks<40]=40
print(marks)

#find avg of new array
s = np.sum(marks)
print(s / len(marks))


#Q.4 create a 2d array 5*5 than extract only even number, extract all numbers from 2nd and 4th row, replace <50 to 0
b1 = np.arange(1,101)
arr_2 = b1.reshape(10,10)
print((arr_2))

#extract even numbers
print(arr_2[arr_2%2==0])

#extract all number from 2nd and 4th row
print(arr_2[[1,3]])

#replace <50 to 0
arr_2[arr_2<50]=0
print(arr_2)