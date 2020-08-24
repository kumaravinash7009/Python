#f= lambda n: n%2==0
from functools import reduce    #cimporting reduce function
nums=[5,6,2,8,9,7,8,3,6]

evens=list(filter(lambda n:n%2==0,nums))		#or  you can call the function.(filter(f,nums))

double=list(map(lambda a:a*2,evens))			#map function
sums=reduce(lambda a,b:a+b,double)			#reduce function
print(evens)
print(double)
print(sums)
