import numpy as np
import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic[["Sex","Age"]].groupby("Sex").mean())