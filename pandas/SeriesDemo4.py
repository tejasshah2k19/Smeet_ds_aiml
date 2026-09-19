import pandas as pd 



marks = pd.Series([12,34,56,78,98,78,56,32,34,56,78])

print(marks.value_counts())

print(marks.nunique())

print(marks.unique())