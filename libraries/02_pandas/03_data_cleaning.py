import pandas as pd

df = pd.read_csv("diabetes.csv")

df.isnull().sum()

df2 = df.copy()
df2 = df2.dropna()
df2.shape