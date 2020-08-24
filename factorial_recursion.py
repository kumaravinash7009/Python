c=1
def fac(n):
	global c
	c=c*n
	n=n-1
	if n>1:
		fac(n)
	return c
result=fac(5)		
print(result)


def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)

result2=fact(6)		
print(result2)			
