import numpy as np
# ARRAY ATTRIBUTES & SHAPE
data = np.array([1,2,3,4,5,6])
print(data)

# item size
print(data.itemsize)

# number of bytes
print(data.nbytes)

# reshape
data = np.arange(1,13)
print(np.reshape(data, (3,4)))

# auto dimension detection
print(np.reshape(data, (2,-1)))

# METHOD
# flatten()
data = np.array([[1,2,3],[4,5,6]])
x = (data.flatten())
x[0] = 7
print(x)
print(data)

# ravel()
data_2 = np.array([[1,2,3],[4,5,6]])
x_1 = (data_2.ravel())
x_1[0] = 7
print(x_1)
print(data_2)

# copy()
x = np.array([1,2,3,4,5,6])
x_2 = (x.copy())
x_2[0]=10
print(x)
print(x_2)

# view()
y = np.array([1,2,3,4,5,7])
y_2 = (y.view())
y_2[0]=10
print(y)
print(y_2)

# AIRTHMETIC OPERATIONS
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a+5)
print(a-5)

# MATHMATICAL OPERATION
x = np.array([1,4,5,9,16,25])
print(x)
print(np.sqrt(x))
print(np.exp(x))
print(np.log(x))
print(np.sin(x))
print(np.cos(x))
print(np.min(x))
print(np.max(x))
print(np.mean(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))

# QUESTIONS
# 01. create an array of 4 by 4 matrix between number 1 to 16 and change it in 1d array after use all the methods
arr = np.arange(1,17)
arr = np.reshape(arr,(4,4))
print(arr)
y = arr.flatten()
print(y.shape)
print(y.size)
print(y.ndim)
print(y.dtype)
print(y.itemsize)
print(y.nbytes)
print(np.sqrt(y))
print(np.exp(y))
print(np.log(y))
print(np.sin(y))
print(np.cos(y))
print(np.min(y))
print(np.max(y))
print(np.mean(y))
print(np.median(y))
print(np.var(y))
print(np.std(y))

# 02. create an 2d array & square of each element and subtract by 10 and find its mean,median,max,min
z = np.array([[10,20,30],[40,50,60]])
y =  np.square(z)
z_1 = (y - 10)
print(np.min(z_1))
print(np.max(z_1))
print(np.mean(z_1))
print(np.median(z_1))

# 03. create an array of number 1 to 500 and find its min,max,mean,median,var,std values
arr = np.linspace(1,501,100)
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.var(arr))
print(np.std(arr))
