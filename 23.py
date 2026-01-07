# PANDA SERIES
import pandas as pd
a = [1,7,2]
print(pd.Series(a))

# LABEL
print(pd.Series(a[0]))

# Create label
x = [9,5,3]
data = (pd.Series(x, index = ["x","y","z"]))
print(data["x"])

# example 2
x = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
data = pd.Series(x, index=["a","b"])
print(data)

# Data frames
data = {
    "number":[79,80,81],
    "result":["pass","pass","pass"]
}

x = pd.DataFrame(data)
y = x,index=["key",""]
print(y)

# locate row
x = pd.DataFrame(data)
print(x.loc[[0]])
