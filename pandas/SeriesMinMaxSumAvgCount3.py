import pandas as pd 



marks  = pd.Series([85,95,80,75,60],index=["Maths","Sci","Eng","Comp","Hindi"])

print("min = ",marks.min())
print("max = ",marks.max())
print("sum = ",marks.sum())
print("mean = ",marks.mean())#avg 
print("median = ",marks.median())
print("count = ",marks.count())
print("std dev = ",marks.std())
print("variance = ",marks.var())
print("Product = ",marks.prod())

#print subject name - in which student got min marks 
#index 
print(marks.idxmin())
print(marks.idxmax())


#combine all functions 
print("********DESCRICE***********")
print(marks.describe())
