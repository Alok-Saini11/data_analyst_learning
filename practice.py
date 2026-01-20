import numpy as np
import pandas as pd

df = pd.read_csv("Exam_Score_Prediction.csv")
print(df.head())
print(df.tail())
print(df.sample())
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
