import numpy as np
import pandas as pd

df = pd.read_csv('new_data.csv')
print(df.to_string())

# dropna
data = df.dropna()
print(data)

# fillna
x = df.fillna(130)
print(x)

# replace null value with specific column
x_1 = df.fillna({"Duration":"30"})
print(x_1)

# head()
x_2 = df.head()
print(x_2)

# tail()
x_3 = df.tail()
print(x_3)

# duplicated
print(df.duplicated())

# drop_dupllicates()
print(df.drop_duplicates())

