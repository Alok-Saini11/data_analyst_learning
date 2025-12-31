import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("cleaned_Heart_Disease_dataset.csv")
#print(df.to_string) 

# EXAMPLE
# 01.
x = np.array([0,6])
y = np.array([0,25])
plt.plot(x,y)
plt.show()

# 02.Ploting without line
d1 = np.array([1,8])
d2 = np.array([3,10])
plt.plot(d1,d2,'o')
plt.show()

# 03.
x = np.array([1,2,6,8])
y = np.array([3,8,9,10])
plt.plot(x,y,'o')
plt.show()

# 04.
x = np.array([3,5,7,9])
plt.plot(x)
plt.show()

# QUESTIONS
# 01.
a = df['Age']
b = df['Sex']
a1 = np.array(a)
b1 = np.array(b)
plt.plot(a1,b1,'o')
plt.show()

# 02.
a2 = df['Chest pain type']
b2 = df['BP']
a3 = np.array(a)
b3 = np.array(b)
plt.plot(a3,b3,'o')
plt.show()

# 03.
a4 = df['Cholesterol']
b4 = df['FBS over 120']
a5 = np.array(a)
b5 = np.array(b)
plt.plot(a5,b5,'o')
plt.show()

# 04.
a6 = df['EKG results']
b6 = df['Max HR']
a7 = np.array(a)
b7 = np.array(b)
plt.plot(a7,b7,'o')
plt.show()

# 05.
a8 = df['Exercise angina']
b8 = df['ST depression']
a9 = np.array(a)
b9 = np.array(b)
plt.plot(a9,b9,'o')
plt.show()


