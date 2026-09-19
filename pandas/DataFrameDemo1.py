import pandas as pd 


#DataFrame
#two dimensional label data structure 
#data base -- table 
#excel -- sheet 
#dataframe is a collection of series -- multiple series 

#series name 
#series maths 
#series sci 
#series eng 

#dataframe => name maths sci eng 


students= {
    "Name":["Ram","Shyam","Ravan","Sita","Nakshi","Anurag"],
    "Maths":[95,85,65,85,90,55],
    "Sci":[90,80,60,80,70,45],
    "Eng":[85,75,65,90,80,55]
}

df = pd.DataFrame(students)

print(df)
print(df["Name"])
 
print(df.shape)
print(df.columns) 
print(df.dtypes) 

print("**********************")
print(df.head()) #top row ->default size is 5  
print(df.tail()) #bottom row -> defualt size is 5 

print("**********************")
print(df.head(1)) # 
print(df.tail(1)) # 

print("##############################")
print(df.info())

print("##############################")
print(df.describe())



#print name and maths marks of students 
print(df["Name"]) #sinle name column 
print(df["Maths"]) #sinle maths column 
print("****************************")
print(df[ ["Name","Maths"] ])


########################################################################################

#add custom label / index to data frame 

df = pd.DataFrame(students,index=["s1","s2","s3","s4","s5","s6"])

print("**************************")
print(df)


#list of data 

data = [ 
            ["Ram",85,90,60],
            ["Shyam",90,85,90],
            ["Sita",80,90,60]
        ]

df = pd.DataFrame(data,columns=["Name","Maths","Sci","Eng"])

print("*********************")
print(df)


#list of dictionary

data= [
    {"Name":"ram","Maths":90,"Eng":85},
    {"name":"Shyam","Maths":100,"Eng":60}
]

df = pd.DataFrame(data)

print("*********************")
print(df)


data= [
    {"Name":"ram","Maths":90,"Eng":85},
    {"Name":"Shyam","Maths":100,"Eng":60}
]

df = pd.DataFrame(data)

print("*********************")
print(df)


#####################################################################################

"""  


| Operation              | Pandas                  |
| ---------------------- | ----------------------- |
| Create DataFrame       | `pd.DataFrame()`        |
| Number of rows/columns | `df.shape`              |
| Column names           | `df.columns`            |
| Row index              | `df.index`              |
| Data types             | `df.dtypes`             |
| First rows             | `df.head()`             |
| Last rows              | `df.tail()`             |
| Information            | `df.info()`             |
| Statistics             | `df.describe()`         |
| One column             | `df["Name"]`            |
| Multiple columns       | `df[["Name", "Marks"]]` |


"""