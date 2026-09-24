#iloc 
#loc 
#row selection 

import pandas as pd 

data = {
    "Name":["Amit","Saj","Sahdev","Priya","Karan","Neha"],
    "Age":[25,28,24,30,27,22],
    "City":["LA","NY","LS","LA","SA","DA"],
    "Salary":[35000,25000,39000,27000,55000,25000]
}

df = pd.DataFrame(data)
print(df)

#position based selection -> iloc()
#integer location 
#it will select data according to the position 
#it starts with 0 

#select first row from data frame 

print(df.iloc(0)) #address 
print(df.iloc[0]) #data 

#third record 
print(df.iloc[2]) 


#select multiple rows 
#1st 3rd and 5th 
print("1st 3rd and 5th")
print(df.iloc[ [0,2,4] ])

#select multiple rows - consecutives 
# 2nd 3rd and 4th 
#slicing 

print("2nd  3rd and 4th")
print(df.iloc[ 2:5 ]) #2 3 and 4 

#negative slicing  
print("Last Record ")
print(df[-1:])
print("Last 2 Record ")
print(df[-2:])


#alternate row 
print("Alternate Row")
# print(df[::]) # all records 
print(df[::2]) # alternate 


#can we access column data ? 
#can we have row column logic? 

#df.iloc[row,col] 


print(df.iloc[0]) #1st row all col data 
print(df.iloc[0,0])
print(df.iloc[0,3])

#multiple columns selection 
print(df.iloc[0,0:3])

#multiple rows and multiple col 
print(df.iloc[0:2,0:2])

#sepecfic row - col 
print(df.iloc[ [0,2,4] ,[0,3]])





print("***********************************************")
data = {
    "Name":["Amit","Saj","Sahdev","Priya","Karan","Neha"],
    "Age":[25,28,24,30,27,22],
    "City":["LA","NY","LS","LA","SA","DA"],
    "Salary":[35000,25000,39000,27000,55000,25000]
}

df = pd.DataFrame(data,index=["s1","s2","s3","s4","s5","s6"])
print(df)

print(df.iloc[0]) #index  ? yes 

#loc[] -> we can access via custom index 

print("0th row")
print(df.iloc[0]) #index [always starts with 0 ]
print(df.loc["s1"]) #custom index [own]


#selecting multiple row using loc 
print(df.loc[ ["s1","s3","s5"] ])

#loc works with columns also like iloc 
print(df.loc["s1","Name"])

#multiple row and multiple col
print(df.loc[ ["s1","s3","s5"] , ["Name","Salary"] ])

#slicing
print(df.loc["s1":"s3"]) #s1 s2 s3 
print(df.iloc[0:2])# 0 1  


#data Frame Filtering 
print("Salary > 40000 ")
print(df[ df ["Salary"] > 40000   ])


print("**************")
print(df["Salary"] > 40000)
sal = df["Salary"] > 40000
print(df[sal])

print("Age > 25")
print( df[df["Age"] > 25] )

#combine both condition 

print("salary > 25000 and age > 25")
print(    df[(df["Age"] > 25) & (df["Salary"] > 25000)]     )


print( df[ df["City"] == "LA" ] )