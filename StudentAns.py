import numpy as np 

#read all data from csv 
data = np.genfromtxt("students.csv",delimiter=",",dtype=str)

# print(data)


# 1)Display first 5 students.
print("First Five : " ,data[0:5])
# 2)Display last 3 students.
print("Last Three : ",data[-3:])
# 3)Display only names.
print("Names : ",data[::,1])
# 4)Display only marks.
print("Marks : ",data[::,4:])

# 5)Display students whose age >21.
allAge = data[::,3].astype(int)
print("Age > 21 : \n",data[allAge>21])