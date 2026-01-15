import matplotlib.pyplot as plt
import seaborn as sns

# count plot
data = sns.load_dataset("dots")
print(data.head())

sns.countplot(x = 'coherence',data=data)
plt.show()

# hue
sns.countplot(x = 'coherence',data=data,hue='firing_rate')
plt.show()

# color
sns.countplot(x = 'coherence',data=data,color='r')
plt.show()

# palette
sns.countplot(x = 'coherence',data=data,palette='dark')
plt.show()


# Pair plot
data_1 = sns.load_dataset('exercise')
print(data_1.head())

sns.pairplot(data=data_1)
plt.show()

# hue
sns.pairplot(data=data_1,hue='diet')
plt.show()

# palette
sns.pairplot(data=data_1,hue='diet',palette='dark')
plt.show()

# vars
sns.pairplot(data=data_1,hue='diet',palette='dark',vars=['pulse','id'])
plt.show()


# cat plot
data_2 = sns.load_dataset('flights')
print(data_2.head())

sns.catplot(x='passengers',data=data_2)
plt.show()

# kind(bar,count,scatter)
sns.catplot(x='passengers',data=data_2,kind='bar')
plt.show()