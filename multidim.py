from numpy import *

arr1 = array([[1,2,3],[7,8,9],[4,5,6]])
arr2 = array([[3,2,4],[5,8,6],[2,5,1]]) 

arr3=arr1.flatten()
arr4=arr3.reshape(3,3)

m=matrix(arr1)
m1=matrix('1 2 3;4 3 2;5 6 7')

m3=m1+m
m4=m1*m

print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr3)
print(arr4)
print(m)
print(m1)
print(m3)
print(m4)
print(diagonal(m))
print(m.min())
print(m.max())
print(m[2,2])


