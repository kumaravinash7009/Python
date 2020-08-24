
# def fib(n):
# 	lst=[]
# 	lst.append(0)
# 	lst.append(1)
# 	for i in range(n):
# 		x=lst[i]+lst[i+1]
# 		lst.append(x)
# 	return lst
def fib(n):
    if n < 2:  # base case
        return n
    return fib(n-1) + fib(n-2)

n=int(input())
lst=[]
for i in range(0,n):
	x=fib(i)
	lst.append(x)
print(lst)

SquareSum=0

for i in range(0,n+1):
	Square=lst[i]*lst[i]
	SquareSum+=Square
	

lastdigit=SquareSum%10

print(lastdigit)
