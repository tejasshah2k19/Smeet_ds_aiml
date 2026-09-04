import numpy as np 

#  arange(start,stop,step,dtype) 

a1 = np.arange(7)#0 1 2 3 4 5 6 
print(a1)

a1 = np.arange(1,5)
print(a1)  # 1 2 3 4 

a1 = np.arange(1,9,3)
print(a1)# 1 4 7 

a1 = np.arange(10,1,-1) # 10 9 8 7 6 5 4 3 2 
print(a1)

print(a1.dtype)

a1 = np.arange(1,5,dtype=np.int16)
print(a1)  # 1 2 3 4 
print(a1.dtype)


a1 = np.arange(0,1,0.2)
print(a1)  #[0.  0.2 0.4 0.6 0.8]

#reshape 
#reshape(2,3)

a1 = np.arange(1,10).reshape(3,3)
print(a1)


#linspace()
#is used to create an array of evenly space numbers between a start value and end value. 

#linspace(start,stop,num=50,endPoint=true,retStep=False,dtype,axis=0)


a1 = np.linspace(1,10)
print(a1)

a1 = np.linspace(1,10,num=4)
print(a1)


#endPoint = True
#step (stop-start)/(num-1)


#endPoint = False
#step (stop-start)/(num)

a1 = np.linspace(1,10,num=4,endpoint=False)
print(a1)


a1 , step  = np.linspace(1,10,num=4,endpoint=False,retstep=True)
print(a1)
print(step)


a1 = np.linspace(1,10,5,dtype=int)
print(a1)

a1 = np.linspace(-10,10,5,dtype=int)
print(a1)

a1 = np.linspace(1,12,12,dtype=int).reshape(4,3)
print(a1)


#meshgrid() 
#is used to create coordinate matrices from two or more coordinate vectors. 

x = np.array([1,2,3])
y = np.array([10,20])

a,b = np.meshgrid(x,y)
print(a)
print(b)

