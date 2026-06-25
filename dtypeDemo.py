
import numpy as np 

#dtype -> 1) attribute 2) parameter 

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1.2,2.3,3.4,4.5,5.1])

print(arr1) 
print(arr2)

print(arr1.dtype)  # attribute -> data type   #int64 
print(arr2.dtype)  # attribute -> data type   #float64 



arr1 = np.array([1,2,3,4,5],dtype=np.int8)
arr2 = np.array([1.2,2.3,3.4,4.5,5.1],dtype=np.float16)


print(arr1.dtype)   #int64->int8 
print(arr2.dtype)   #float64->float8 





print("###############################")
###############################
arr1 = np.array([1,2,3,4,5])
arr2  = arr1.view(dtype=np.int8)
arr3 = arr1.copy()

print(arr1.dtype)#64bit 
print(arr2.dtype)#8bit 
print(arr3.dtype)#64bit 


print(arr1.itemsize) #8byte
print(arr2.itemsize) #1byte 
print(arr3.itemsize) #8byte 


print("arr1 ",arr1) # 1 2 3 4 5 
arr2[0] = 10; 
print(arr1) #  
print(arr2) #
print(arr3) #


print("arr1 ",arr1) # 1 2 3 4 5 
arr3[0] = 10; 
print(arr1) #  
print(arr2) #
print(arr3) #


###############################











