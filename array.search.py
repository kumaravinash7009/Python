from array import *

n= int(input("Enter the length of array:"))
arr=array('i',[])

for i in range(n):
	arr.append(int(input("Enter the no")))
print arr	
	
k=0
val=int(input("Enter the you want to check: "))

for e in arr:
	if e==val:
		
		print(k)		
		break	
	k+=1	
	
print(arr.index(val))	
