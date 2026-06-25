import numpy as np 
import time     

marks = np.random.randint(0,101,1000)
list = marks.tolist() 


marks.size # total number of items 
marks.nbytes # total bytes occupied by array 
marks.dtype  # data type of array 
marks.itemsize # single data item size in byte 




start = time.time()
sum = 0 
for data in list:
    sum = sum + data 
end = time.time()

print(end-start)
a = end -start 


start = time.time()
np.sum(marks)
end = time.time()
print(end-start)
b = end -start 

print(a/b) # 2.21 
print(b/a)