pos=-1
def search(list,n):
	lb=0
	ub=len(list)-1
	
	for i in range(len(list)):
		temp=(lb+ub)//2
		#print(temp,type(temp))
		if n>list[temp]:
			lb=temp+1
		elif n<list[temp]:
			ub=temp-1
		elif n==list[temp]:
			globals()['pos']=temp
			return True
		else:	
			return False


lst= [1,5,6,11,12,18]

n=6
#print(type(n))
#print(type(lst[1]))
if search(lst,n):
	print("Found at position of", pos+1)
else:
	print("Not found")
