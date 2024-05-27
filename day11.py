import pandas as pd
data = [1,3,5,7,9]
a = pd.Series(data, index=['인천','경기','서울','경남','대전'])

print(a)
print(a.values)
print(a.index)