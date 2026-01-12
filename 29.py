import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("anagrams")
print(data.head())

# Line plot
sns.lineplot(x = 'num1',y = 'num2', data = data)
plt.show()

# title
sns.lineplot(x = 'num1',y = 'num2', data = data)
plt.title("Analysis")
plt.show()

# Hue
sns.lineplot(x = 'num1',y = 'num2', data = data,hue='attnr')
plt.show()

# size
sns.lineplot(x = 'num1',y = 'num2', data = data,sizes=(0.1,0.9))
plt.show()

# line style
sns.lineplot(x = 'num1',y = 'num2', data = data,hue='attnr',style='attnr')
plt.show()

# color palette
sns.lineplot(x = 'num1',y = 'num2', data = data,hue='attnr',style='attnr',palette='Accent')
plt.show()

# markers
sns.lineplot(x = 'num1',y = 'num2', data = data,hue='attnr',style='attnr',palette='Accent',markers=['o','>'])
plt.show()

# dashes
sns.lineplot(x = 'num1',y = 'num2', data = data,hue='attnr',style='attnr',palette='Accent',markers=['o','>'],dashes=False)
plt.show()

# legend
sns.lineplot(x = 'num1',y = 'num2', data = data,hue='attnr',style='attnr',palette='Accent',markers=['o','>'],dashes=False,legend=False)
plt.show()

# grid
sns.lineplot(x = 'num1',y = 'num2', data = data,hue='attnr',style='attnr',palette='Accent',markers=['o','>'],dashes=False,legend=False)
plt.grid()
plt.show()

