#filtering - conditions 


import pandas as pd 


students= {
    "Name":["Ram","Shyam","Ravan","Sita","Nakshi","Anurag"],
    "Maths":[95,85,65,85,90,55],
    "Sci":[90,80,60,80,70,45],
    "Eng":[85,75,65,90,80,55],
    "City":["LA","NY","LA","SD","LA","NY"]
}

df = pd.DataFrame(students)

print("DF => ")
print(df)


#filter -> select only the rows that satisfy a conidtion 

#give all students who got 85+ in maths
#select * from students where maths >= 85 


maths85 = df[ df["Maths"] >= 85 ]
print("Maths 85+")
print(maths85)



# df["Maths"] >= 85 => this will not return all the rows immediately , it returns boolean Series 
"""  
0   True 
1   True 
2   False
3   True 
4   True 
5   False 
"""
"""
    we can use > >= < <= == != 
    
"""

#now what if we don't want entire row , we only wants to print name of students who got 85+ in Maths 

#we need to use loc[] 

maths85 = df.loc[ df["Maths"] >= 85 , "Name" ] 
print("----------------------")
print(maths85)


#add multiple condition 
# we can not use AND like in python 
#here we have to & 

mathsSci85 = df.loc[  (df["Maths"] >= 85) & (df["Sci"] >= 85) , "Name" ] 
print("----------------------")
print(mathsSci85)

mathsSci85 = df.loc[  (df["Maths"] >= 85) & (df["Sci"] >= 85)  ] 
print("----------------------")
print(mathsSci85)


#display all students who lives in LA or NY 
#OR 
print("===================")
print(df[  (df["City"] == "LA") | ( df["City"] == "NY") ])

#we can have multiple or and , mixture of it 

#if we want to add multiple or condtion than isin() is good 


print("===================")
print(df[  df["City"].isin(["LA","NY"]) ])


#we can also have not isin() for this we have to used ~
print("===================")
print(df[  ~df["City"].isin(["LA","NY"]) ])
 
#for numertic value we have between()

#maths marks 70 to 90 

print("==========70 ---- 90==========")
print(df[  (df["Maths"] >= 70) & (df["Maths"] <= 90) ])

print("==========70 ---- 90==========")
print(df[ df["Maths"].between(70,90) ])


#name contains 'a' 
#name contains 'i' 

print("===================")
print(df[   df["Name"].str.contains("i")  ])


#name starts with 'S' 
print("===================")
print(df[   df["Name"].str.startswith("S")  ])

print("===================")
print(df[   df["Name"].str.startswith("s")  ])


#endsWith
print("===================")
print(df[   df["Name"].str.endswith("a")  ])



#query()

print("===Query====")
print(df.query("Maths >= 85 and Maths <= 95 "))

#quer() can used to make complex condition/filters  easier 
