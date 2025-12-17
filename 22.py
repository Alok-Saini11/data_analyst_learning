# Stacking array
# vstack()
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a, b)))

# hstack()
print(np.hstack((a, b)))

# Stack()
print(np.stack((a, b), axis = 0))

# Spliting array
arr = np.array([1,2,3,4,5,6])
print(np.split(arr,2))

# array_split
print(np.array_split(arr,4))

# append
a = np.array([1,2,3])
print(np.append(a,4))
print(np.append(a,[5,6]))

# insert
x = np.array([10,20,30,40])
print(np.insert(x,2,25))

# delete
y = np.delete(x,2)
print(y)

# Broad_casting and advance topic
a = np.array([1,2,3])
b = 5
print( a+b )

# addition in 2d array
x = np.array([[1,2,3],[4,5,6]])
y = [10,20,30]
print( x+y ) 

# Any()
arr = np.array([10,20,0,70])
print(np.any(arr))

# All()
print(np.all(arr))

# Clip()
arr_1 = np.array([10,20,30,40,50,60])
print(np.clip(arr_1,20,50))

# Sort()
arr_2 = np.array([4,2,1,3,5])
print(np.sort(arr_2))

# Sorting in 2d array
arr_3 = np.array([[3,1,2],[6,4,5]])
print(np.sort(arr_3))