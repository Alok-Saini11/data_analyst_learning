import matplotlib.pyplot as plt
import numpy as np

# Scatter
x = np.array([1,2,3,4])
y = np.array([10,20,30,40])
plt.scatter(x,y)
plt.show()

# Compare plot
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.scatter(x,y,color = "red")

x1 = np.array([10,30,60,90])
y1 = np.array([2,4,6,8])
plt.scatter(x1,y1,color = "blue")

plt.show()

# To use specific color on each marker
c = np.array(["red","blue","green","orange"])
plt.scatter(x,y,color = c)
plt.show()

# To use specific size on each marker
s = np.array([2,3,4,5])
plt.scatter(x,y,s=s)
plt.show()

# Alpha
plt.scatter(x,y,alpha=0.6)
plt.show()

# Bars
x = np.array(["A","B","C","D"])
y = np.array([70,80,90,80])
plt.bar(x,y,width=0.5,color = "red")
plt.show()

# Horizontal bar
plt.barh(x,y,height=0.6,color = "blue")
plt.show()

# Histogram
x = np.random.normal(100,10,10)
plt.hist(x)
plt.show()

# Pie
x = np.array([35,25,25,15])
plt.pie(x)
plt.show()

# style of pie chart
x =np.array([20,25,30,40])
my_lab = np.array(['A','B','C','D'])
Explode = np.array([0.3,0.4,0.5,0.6])
colour = np.array(['red','blue','pink','green'])
plt.pie(x,labels=my_lab,startangle=90,explode=Explode,shadow=True,colors=colour)
plt.legend(my_lab,title = "categories")
plt.show()