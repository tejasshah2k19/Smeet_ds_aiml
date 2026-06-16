import numpy as np 

a = np.array([10,20,30,40,50,60,70,80,90,100])

print(a)

print(a[0]) # index starts with zero

print(a[0:5]) # 0 to 4 index 

print(a[-1]) # last 

print(a[-2]) # second last 

print(a[::]) # all elements start from 0th index to end 

print(a[2::]) # start from 2nd index to end  

print(a[::2]) # start with 0th index and then increment by 2 till end [0 2 4 6 8 ] 

print(a[::1]) 

print(a[::-1]) 


print("====Loop====")
for i in range(0,len(a)):
    print(a[i])
    
    
print("====Loop====")
for i in range(len(a)-1,0,-1):
    print(a[i])