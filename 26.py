import matplotlib.pyplot as plt
import numpy as np

# Markers
x = np.array([1,3,5,7])
y = np.array([10,20,30,40])
plt.plot(x,y,'o')
plt.show()

# "*"
plt.plot(x,y,'*')
plt.show()

# "."
plt.plot(x,y,'.')
plt.show()

# "H"
plt.plot(x,y,'H')
plt.show()

# "D"
plt.plot(x,y,'D')
plt.show()

# "P"
plt.plot(x,y,'P')
plt.show()

# "^"
plt.plot(x,y,'^')
plt.show()

# ">"
plt.plot(x,y,'>')
plt.show()

# "2"
plt.plot(x,y,'2')
plt.show()

# "4"
plt.plot(x,y,'4')
plt.show()

# "-"
plt.plot(x,y,'-')
plt.show()

# "X"
plt.plot(x,y,'X')
plt.show()

# "+"
plt.plot(x,y,'+')
plt.show()

# "s"
plt.plot(x,y,'s')
plt.show()

# "d"
plt.plot(x,y,'d')
plt.show()

# "v"
plt.plot(x,y,'v')
plt.show()

# "<"
plt.plot(x,y,'<')
plt.show()

# "1"
plt.plot(x,y,'1')
plt.show()

# "3"
plt.plot(x,y,'3')
plt.show()

# "|"
plt.plot(x,y,'|')
plt.show()
'''
'''# format strings
plt.plot(x,y,'o:r')
plt.show()

# '_ ,g'
plt.plot(x,y,'o-g')
plt.show()

# '--,b'
plt.plot(x,y,'o--b')
plt.show()

# '-.,c'
plt.plot(x,y,'o-.c')
plt.show()

# size of marker
plt.plot(x,y,'o',ms = 20)
plt.show()

# border colour of marker
plt.plot(x,y,'o',mec = 'r')
plt.show()

# inner colour of marker
plt.plot(x,y,'o',mfc = 'r')
plt.show()

# to change full colour of marker
plt.plot(x,y,'o',mec = 'r',mfc = 'r')
plt.show()

# Line Style
plt.plot(x,y,ls = 'dotted')
plt.show()

# dashed line
plt.plot(x,y,ls = 'dashed')
plt.show()

# or(remove a line)
plt.plot(x,y,ls = 'None')
plt.show()

# colour of line
plt.plot(x,y,c = 'r')
plt.show()

# width of line
plt.plot(x,y,lw = '20.5')
plt.show()

# colour & width & Type
plt.plot(x,y,ls = 'dashed',c = 'b',lw = '10')
plt.show()

# TO use multiple lines
x1 = np.array([2,4,6,8])
y1 = np.array([11,22,33,44])
plt.plot(x,y,x1,y1)
plt.show()