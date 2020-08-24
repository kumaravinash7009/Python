from numpy import *

arr1=array([1,2,94,4,5])
max=arr1[0]
for i in range(1,5):
	if max<=arr1[i]:
		max=arr1[i]
	else:
		continue
print(max)	
			
