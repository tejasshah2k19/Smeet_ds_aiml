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
"""
--------------------------------------------
| Requirement        | Pandas              |
| ------------------ | ------------------- |
| Greater            | `>`                 |
| Greater/equal      | `>=`                |
| Less               | `<`                 |
| Less/equal         | `<=`                |
| Equal              | `==`                |
| Not equal          | `!=`                |
| AND                | `&`                 |
| OR                 | `\|`                |
| NOT                | `~`                 |
| Multiple values    | `isin()`            |
| Range              | `between()`         |
| Contains text      | `.str.contains()`   |
| Starts with        | `.str.startswith()` |
| Ends with          | `.str.endswith()`   |
| SQL-like filtering | `query()`           |
--------------------------------------------
""" 


""" TASK 

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Karan",
             "Mehul", "Riya", "Jay"],
    "Age": [25, 28, 24, 30, 27, 32, 23, 29],
    "City": ["Ahmedabad", "Mumbai", "Pune", "Delhi",
             "Surat", "Mumbai", "Ahmedabad", "Delhi"],
    "Salary": [35000, 45000, 38000, 55000,
               42000, 60000, 32000, 48000]
})


Find employees with salary greater than 40000.
Find employees with salary less than 40000.
Find employees age >= 28.
Find employees from "Mumbai".
Find employees NOT from "Mumbai".
Find employees with salary between 40000 and 50000.
Find employees from Mumbai or Delhi.

Find employees whose salary is greater than 40000 and age is greater than 25.
Find employees from Ahmedabad or Delhi with salary above 30000.
Find employees whose name contains "a", ignoring case.
Find employees whose age is between 25 and 30.
Find employees whose city is one of: Ahmednad , Mumbai , Delhi 


Difficult: 
Find employees who earns more than 45000 in the age of 25-30 and does not lives in Ahmedabad 
    Return only Name, City, and Salary.



"""