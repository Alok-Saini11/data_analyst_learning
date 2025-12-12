# NUMPY
import numpy as np
x = np.array([1,2,3,4,5])
print(x*2)

# example
import time
lst = list(range(1_000_000))
start = time.time()
[x*2 for x in lst]
print(time.time()-start)

# example
import time
import numpy as np
arr = np.arange(1_000_000)
start = time.time()
arr*2
print(time.time()-start)

# NUMPY ARRAY
# creating an array
import numpy as np
x = np.array([1,2,3,4,5,6])
print(x)

# multi_dimensional array
y = np.array([[1,2,3],[4,5,6]])
print(y)

# zero matrix
print(np.zeros((2,3)))

# ones matrix
print(np.ones((2,3)))

# full matrix
print(np.full((2,2),7))

# identity matrix
print(np.eye((3)))

# arange
print(np.arange(1,10,2))

# linespace
print(np.linspace(0,1,5))

# random number
print(np.random.randint(1,10))

# array functions
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

# shape of array
print(arr.shape)

# size of array
print(arr.size)

# dimension of array
print(arr.ndim)

# type of array
print(arr.dtype)

# TYPE COVERSION
arr = np.array([1,2,3],dtype=float)
print(arr)
print(arr.dtype)

# AIRTHMETIC OPERATION
arr_2 = np.array([1,2,3,4,5])

print(arr_2 + 5)
print(arr_2 - 5)
print(arr_2 * 2)
print(arr / 2)
print(arr ** 2)

# COMPARISION OR LOGICAL OPERATOR
arr_3 = np.array([10,20,30,40,50])
print(arr_3 > 25)
print(arr_3 == 30)

# question
# 01. create an array of number 1 to 20 using np.arange() and find its shape,size or datatype
arr_4 = np.arange(1,21,1)
print(arr_4)

print(arr_4.shape)
print(arr_4.size)
print(arr.dtype)

# 02. create a matrix of 3 by 3 and take random number between 10 to 50 and find its maximum,minimum,mean
x = np.random.randint(10,50,(3,3))
print(x)

#maximum
print(np.max(x))

#minimum
print(np.min(x))

# average
print(x.mean())

