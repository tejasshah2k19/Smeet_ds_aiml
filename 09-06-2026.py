import numpy as np 


# print(np)

# python 09-06-2026.py

#  how to create array using numpy 

arr = np.array([]) # create empty array 
print(arr)

arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr)

#matrix -> row * col 

arr = np.array([  [1,2,3],[4,5,6],[7,8,9]   ])
print(arr)
#1 2 3 
#4 5 6
#7 8 9 

#Array properties :- 

arr1D = np.array([1,2,3,4,5])
arr2D = np.array([ [1,2,3],[4,5,6],[7,8,9]])

print(arr1D.ndim) # 1 
print(arr2D.ndim) # 2 


print(arr1D.shape) # (5,) 
print(arr2D.shape) # (3,3) 

print(arr1D.size) # 5
print(arr2D.size) # 9 

print(arr1D.dtype) # int 
print(arr2D.dtype) # int 



#fill 2D array with zeros 
zeroArray = np.zeros( (3,4) )
print(zeroArray)


#fill 2D array with ones 
onesArray = np.ones( (3,4) )
print(onesArray)


arr = np.eye(3)
print(arr)

arr = np.eye(4)
print(arr)


arr = np.arange(1,11)  # 1 to 10 1D
print(arr)


arr = np.random.rand(5) # 5 size of random 1D array    0 > value < 1 
print(arr)

arr = np.random.randint(1,100,5) # 5 size of random 1D array  between 1 to 100
print(arr)


# create random 1D array of size 9
arr = np.random.randint(1,100,9)
print(arr)

arr = arr.reshape(3,3)
print(arr)


# arr = np.random.randint(1,100,9)
# arr = arr.reshape(4,2)
# print(arr)



arr = np.array( [1,2,3,4,5 ] )
print(arr)
#sum 
sum = np.sum(arr) 
print(sum)
#min 
print(np.min(arr))
#max 
print(np.max(arr))
#mean 
print(np.mean(arr))
#median 
print(np.median(arr))


#indexing , slicing  



