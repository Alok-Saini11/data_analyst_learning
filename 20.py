# Mathmetical and Statical Operation
# Axis = 0 - column
# Axis = 1 - row

# To find minimum as columns
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(np.min(arr,axis = 0 ))

# To find minimum as rows
print(np.min(arr,axis = 1))

# To find maximum as columns
print(np.max(arr,axis = 0))

# To find maximum as rows
print(np.max(arr,axis = 1))

# To find mean/average as columns
print(np.mean(arr,axis = 0))

# To find mean/average as rows
print(np.mean(arr,axis = 1))

# Question
# Find the some of array as per rows ans columns
# Sum as per columns
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(x,axis = 0))

# Sum as per rows
print(np.sum(x,axis = 1))

# Cumulative Function
# Cumsum()
arr = ([1,2,3,4,5,6])
print(np.cumsum(arr))

# Cumproad()
print(np.cumprod(arr))

# Other function
# Round()
x = np.array([1.2437,5.673256,6.75355])
print(np.round(x))

# Floor()
print(np.floor(x))

# Ceil()
print(np.ceil(x))

# Concatenate Function
x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.concatenate((x,y)))

# concatenate as per column
x_1 = np.array([[1,2],[3,4]])
x_2 = np.array([[5,6],[7,8]])
print(np.concatenate((x_1,x_2),axis = 0))

# concatenate as per rows
print(np.concatenate((x_1,x_2),axis = 1))

# Normalization
x = np.array([10,20,30,40,50,60,70])
print((x - np.min(x)) / (np.max(x)-np.min(x)))

# Question
'''   M   E  H
   S1[45,78,56]
   S2[67,82,90]
   S3[85,65,70]
   S4[34,55,60]
   S5[76,88,97]'''

# 01.find maths average number
# 02.find S1 max number
# 03.find S4 min number
# 04.find average number per student
# 05.find average number per subject

# 01.
y = np.array([[45,78,56],[67,82,90],[85,65,70],[34,55,60],[76,88,97]])
x=(np.mean(y,axis=0))
print(x[0])

# 02.
x_1 = (np.max(y,axis=1))
print(x_1[0])

# 03.
x_2 = (np.min(y,axis=1))
print(x_2[3])

# 04.
x_3 = (np.mean(y,axis=1))
print(x_3)

# 05.
x_4 = (np.mean(y,axis=0))
print(x_4)