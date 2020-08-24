import math as m
from array import *

a=int(input('Enter from:'))
b=int(input('Enter upto:'))
num=range(a,b)
prime=array('i',[])
for i in num:
	if i==1:
		continue
	elif i==2:
		continue
	j=int(m.ceil(m.sqrt(i)))
	k=2
	for k in range(2,j+1):
		if i%k==0:
			break
	else:
		prime.append(i)
print(prime)		
	


			
		



