import numpy as np 

arr1 = np.array([1,2,3,4,5])
arr2 = arr1.view()
arr2[0] = 10
arr1[1] = 20 
print(arr1)
print(arr2)



arr1 = np.array([1,2,3,4,5])
arr2 = arr1.copy()
arr2[0] = 10
arr1[1] = 20
print(arr1)
print(arr2)
