import matplotlib.pyplot as plt
import numpy as np

# Label
x = np.array([10,20,30,40])
y = np.array([1,2,3,4])
plt.plot(x,y,'o')
plt.xlabel("Age")
plt.ylabel("BP")
plt.show()

# Label Style
plt.plot(x,y)
font_1 = {'family':'Serif','color':'blue','size':20}
plt.xlabel("Age",fontdict=font_1)
plt.ylabel("BP",fontdict=font_1)
plt.show()

# Title
# super title
plt.plot(x,y)
plt.suptitle("Analysis")
plt.show()

# Title style
plt.plot(x,y)
font_2 = {'family':'Serif','color':'blue','size':20}
plt.title("Analysis",fontdict=font_2)
plt.show()

# Grid
plt.plot(x,y)
plt.grid()
plt.show()

# Grid line using axis of x & y
plt.plot(x,y)
plt.grid(axis='x')
plt.show()

# Grid Style
plt.plot(x,y)
plt.grid(color = "green",linestyle = '--',linewidth = 0.5)
plt.show()

# Subplot
# example.1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.xlabel("A")
plt.ylabel("B")
plt.suptitle("Analysis")
plt.title("Age")

x1 = np.array([2,3,4,5])
y1 = np.array([5,6,7,8])
plt.subplot(1,2,2)
plt.xlabel("C")
plt.ylabel("D")
plt.plot(x,y)
plt.title("BP")

plt.show()

# example.2
a = np.array([2,4,6,8])
b = np.array([10,20,30,40])
plt.subplot(2,1,1)
plt.plot(a,b)
plt.suptitle("Analysis_2")
plt.title("Min")

c = np.array([0,1,2,3])
d = np.array([2,3,4,5])
plt.subplot(2,1,2)
plt.plot(c,d)
plt.title("Max")

plt.show()

# example.3
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
plt.subplot(3,3,1)
plt.suptitle("Analysis_3")
plt.title("A")
plt.plot(x,y)

x1 = np.array([10,20,30,40])
y1 = np.array([50,60,70,80])
plt.subplot(3,3,2)
plt.title("B")
plt.plot(x1,y1)

x2 = np.array([1,2,3,4])
y2 = np.array([5,6,7,8])
plt.subplot(3,3,3)
plt.title("C")
plt.plot(x2,y2)

x3 = np.array([1,2,3,4])
y3 = np.array([5,6,7,8])
plt.subplot(3,3,4)
plt.title("D")
plt.plot(x3,y3)

x4 = np.array([1,2,3,4])
y4 = np.array([5,6,7,8])
plt.subplot(3,3,5)
plt.title("E")
plt.plot(x4,y4)

x5 = np.array([1,2,3,4])
y5 = np.array([5,6,7,8])
plt.subplot(3,3,6)
plt.title("F")
plt.plot(x5,y5)

x6 = np.array([1,2,3,4])
y6 = np.array([5,6,7,8])
plt.subplot(3,3,7)
plt.title("G")
plt.plot(x6,y6)

x7 = np.array([1,2,3,4])
y7 = np.array([5,6,7,8])
plt.subplot(3,3,8)
plt.title("H")
plt.plot(x7,y7)

x8 = np.array([1,2,3,4])
y8 = np.array([5,6,7,8])
plt.subplot(3,3,9)
plt.title("I")
plt.plot(x8,y8)

plt.show()
