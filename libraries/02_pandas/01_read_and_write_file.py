import pandas as pd

# Read Data From Different Sources
df = pd.read_csv("diabetes.csv")
df = pd.read_csv("diabetes.txt", sep="\s")
df = pd.read_json("diabetes.json")

df = pd.read_excel('diabetes.xlsx')
# Extracting the second sheet since Python uses 0-indexing
df = pd.read_excel('diabetes_multi.xlsx', sheet_name=1)

# Write Data
df.to_csv("diabetes_out.csv", index=False)
df.to_json("diabetes_out.json")
df.to_csv('diabetes_out.txt', header=df.columns, index=None, sep=' ')
df.to_excel("diabetes_out.xlsx", index=False)

