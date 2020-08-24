from numpy import *

arr1 = array([[1,2,3],[7,8,9],[4,5,6]])
arr2 = array([[3,2,4],[5,8,6],[2,5,1]]) 
arr3=zeros(9)
arr4=arr3.reshape(3,3)

arr2[2,2]=3
print(arr1)
print(arr2)

for i in range(len(arr1)):
	for j in range(len(arr2[0])):
		for k in range(len(arr2)):
			arr4[i,j]+=arr1[i,k]*arr2[k,j]

print(arr4)			
print(matrix(arr1)*matrix(arr2))
print(arr1*arr2)
