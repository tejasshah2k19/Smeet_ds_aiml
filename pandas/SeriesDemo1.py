import pandas as pd 
import numpy as np 

s1 = pd.Series([10,20,30,40,50])
print(s1)

list = [10,"ram",False,25.52] #0 1 2 3 4 
s2 = pd.Series(list)
print(s2)


t = ("jack","rock","sakira")#0 1 2 3 4 
s3 = pd.Series(t)
print(s3)

d = { "name":"ram","salary":15000,"city":"Ayodhya"}#name salary city 
s4 = pd.Series(d)
print(s4)


n1 = np.array([11,22,33,44,55])#0 1 2 3 4 
s5 = pd.Series(n1)
print(s5)


print(s1.dtype)
print(s2.dtype)
print(s3.dtype)
print(s4.dtype)
print(s5.dtype)
 
 
s6 = pd.Series([11,22,33],index=[7,8,9])
print(s6) 


print(s6[1])
print(s6[0]) 