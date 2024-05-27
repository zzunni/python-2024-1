import numpy as np
import pandas as pd

titanic = pd.read_csv("titanic.csv")

df1 = titanic["Pclass"] == 1
df2 = titanic["Age"] >= 60
print(titanic.loc[df1&df2])

df3 = titanic.loc[df1&df2].sort_values(by='Age')
df4 = titanic.loc[df1|df2]

df3.to_csv('result1.csv',encoding='cp949')
df4.to_csv('result2.csv',encoding='cp949')