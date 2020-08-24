



def fib(n):
	lst=[]
	lst.append(0)
	lst.append(1)
	for i in range(n):
		x=lst[i]+lst[i+1]
		lst.append(x)
	return lst

n , a =input().split()
lst=fib(int(n))

print(lst[int(a)-1])



