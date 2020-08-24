
def fib(n):
	lst=[]
	lst.append(0)
	lst.append(1)
	for i in range(n):
		x=lst[i]+lst[i+1]
		lst.append(x)
	return lst
n=int(input())
lst=fib(n)


Sum=0

for i in range(n):
	Sum+=lst[i]
	
lastdigit=Sum%10

print(lastdigit)
