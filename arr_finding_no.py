from array import *

arr= array('i', [])
n= int(input("Enter the no of array: "))

for i in range(n):
	x=int(input("Enter the next value: "))
	arr.append(x)
print(arr)	

num=int(input("enter the number you are searching for: "))
k=0
for e in arr:
	if e==num:
		print(k)
		break
	k+=1	
		