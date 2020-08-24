def topten():
	n=1
	while n<=10:
		sq=n*n
		yield sq
		n+=1
		
values=topten()

for i in values:
	print(i)
	
	
	
def top():
	yield 1	
	yield 2	
	yield 3	
	yield 4	
	yield 5	

values1=top()
print(values1.__next__())	
print(values1.__next__())

for j in values1:
	print(j)
