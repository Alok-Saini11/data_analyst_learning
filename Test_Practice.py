
# Pandas – Data Understanding & Cleaning

# 1. Load the CSV file using pandas and display the first 5 rows.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Customers.csv")
print(df.head())

# 2. How many rows and columns are present in the dataset?
print(df.shape)

# 3. Check if there are any missing values in the dataset.
print(df.isnull().sum())

# 4. Replace missing values in Work Experience with the column mean.
mean_value = df['Profession'].mean
df['Profession']= df['Profession'].fillna(mean_value)
print(df.isnull().sum())

# 5. Convert Gender and Profession into categorical data.
df['Gender'] = df['Gender'].astype('category')
df['Profession'] = df['Profession'].astype('category')

# 6. Rename column Annual Income ($) to Annual_Income.
rename =df.rename(columns={"Annual Income ($)":"Annual_Income"})
print(rename.columns)

# 7. Find duplicate records (if any) and remove them.
df.drop_duplicates()

# 8. Change all column names to lowercase with underscores.
df.columns = df.columns.str.lower().str.replace(' ', '_')


# 🔹 Pandas – Data Analysis & Aggregation

# 9. What is the average annual income of customers?
avg = df['annual_income_($)'].mean()
print("Average",avg)

# Find the average spending score by gender.
gender_avg = df.groupby('gender')['spending_score_(1-100)'].mean()
print("gender average:",gender_avg)

# Which profession has the highest average income?
#max_income = df['annual_income_($)'].max()
highest_income = df.groupby('profession')['annual_income_($)'].mean().max()
print(highest_income)

# Find the top 5 customers with the highest spending score.
x = df['spending_score_(1-100)'].head(5)
print(x)

# Calculate the median age of customers.
y = df['age'].median()
print("median age",y)

# Find the count of customers in each profession.
count_profession = df['profession'].value_counts()
print(count_profession)

# What is the average family size by profession?


# Find customers whose income is above average but spending score is below average.

# Create a new column income_group:

# Low: < 40,000

# Medium: 40,000–80,000

# High: > 80,000

# Find the number of customers in each income group.

# 🔹 NumPy – Numerical Operations

# Convert Age and Spending Score columns into NumPy arrays.

# Calculate mean, median, and standard deviation of Annual Income using NumPy.

# Find the maximum and minimum spending score using NumPy.

# Normalize the Spending Score column using NumPy.

# Identify customers whose age is greater than 1 standard deviation above the mean.

# Use NumPy to calculate correlation between income and spending score.

# 🔹 Pandas + NumPy – Logical Filtering

# Find all female customers with:

# Income > 60,000

# Spending Score > 70

# Find customers with more than 5 family members.

# Filter customers with work experience greater than 10 years.

# Find engineers whose spending score is less than 20.

# Count customers aged between 25 and 40.

# 🔹 Matplotlib – Data Visualization

# Plot a histogram of Age distribution.

# Create a bar chart showing number of customers per profession.

# Plot a scatter plot between Annual Income and Spending Score.

# Create separate spending score distributions for males and females.

# Plot a boxplot of Annual Income by Gender.

# Create a line plot showing average spending score by age.

# Plot a bar chart for income groups vs customer count.

# Visualize family size distribution using a bar chart.

# Create a scatter plot of Age vs Spending Score with different colors for gender.

# 🔹 Real Interview Case-Based Questions

# Based on spending score and income, how would you identify premium customers?

# Which profession should a company target for high-value marketing, and why?

# Do older customers spend more than younger customers? Justify using plots.

# Is there a relationship between family size and spending score?

# How would you segment customers using only pandas and matplotlib?

# 🔹 Bonus (Common Interview Traps)

# Difference between loc and iloc with an example from this dataset.

# Why is vectorized computation in NumPy faster than loops?

# When would you prefer groupby() over pivot tables?

# Explain how you would optimize this dataset if it had 1 million rows.
