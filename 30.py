import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("anscombe")
print(data.head())

# Histogram
sns.displot(data['x'])
plt.show()

# bins
sns.displot(data['x'],bins=10)
plt.show()

sns.displot(data['x'],bins=[10,12,14,16,18,20])
plt.show()

# Kde
sns.displot(data['x'],kde=True)
plt.show()

# rug
sns.displot(data['x'],kde=True,rug=True)
plt.show()

# color
sns.displot(data['x'],kde=True,color='g')
plt.show()

# log_scale value
sns.displot(data['x'],kde=True,log_scale=True)
plt.show()


# Bar plot
data_1 = sns.load_dataset("attention")
print(data_1.head())

sns.barplot(x='subject',y='score',data=data_1)
plt.show()

# hue
sns.barplot(x='subject',y='score',data=data_1,hue='attention')
plt.show()

# order
sns.barplot(x='subject',y='score',data=data_1,order=['5','6','1'])
plt.show()

# orient
sns.barplot(x='subject',y='score',data=data_1,hue='attention',orient='h')
plt.show()

# color
sns.barplot(x='subject',y='score',data=data_1,hue='attention',color='g')
plt.show()

# saturation
sns.barplot(x='subject',y='score',data=data_1,hue='attention',saturation=0.5)
plt.show()

# errcolor
sns.barplot(x='subject',y='score',data=data_1,hue='attention',errcolor='r')
plt.show()

# capsize
sns.barplot(x='subject',y='score',data=data_1,hue='attention',capsize=5)
plt.show()

# dodge
sns.barplot(x='subject',y='score',data=data_1,hue='attention',dodge=True)
plt.show()


# Scatter plot
data_2 = sns.load_dataset("car_crashes")
print(data_2.head())

sns.scatterplot(x='speeding',y='alcohol',data=data_2)
plt.show()

# hue
sns.scatterplot(x='speeding',y='alcohol',data=data_2,hue='abbrev')
plt.show()

# style
sns.scatterplot(x='speeding',y='alcohol',data=data_2,hue='abbrev',style='abbrev')
plt.show()

# size
sns.scatterplot(x='speeding',y='alcohol',data=data_2,hue='abbrev',size='abbrev')
plt.show()

# sizes
sns.scatterplot(x='speeding',y='alcohol',data=data_2,hue='abbrev',sizes=(1,2,3,4,5,6,7,8,9,10))
plt.show()

# palette
sns.scatterplot(x='speeding',y='alcohol',data=data_2,hue='abbrev',palette='ocean')
plt.show()

# alpha
sns.scatterplot(x='speeding',y='alcohol',data=data_2,hue='abbrev',alpha=0.8)
plt.show()

# markers
sns.scatterplot(x='speeding',y='alcohol',data=data_2,hue='abbrev',markers=['<','>'])
plt.show()
