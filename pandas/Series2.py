import pandas as pd 

s1 = pd.Series([11,22,33,44,55])

print(s1[0])# 0th index 

#iloc 
print(s1.iloc(0))
print(s1.iloc[0])



s6 = pd.Series([11,22,33],index=[7,8,9])
print(s6) 


print(s6[7])  #s6[7] => label 
print(s6[8]) 

print(s6.iloc[1]) #iloc -> index 