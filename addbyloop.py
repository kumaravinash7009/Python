from numpy import *

arr1=array([1,2,3,4,5])
arr2=array([5,4,3,2,1])
arr3=zeros(5)

for i in range(5):
	arr3[i]=arr1[i]+arr2[i]
print(arr3)

