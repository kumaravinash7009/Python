pos=-1

def search(list, n):
	
	for i in range(len(list)):
		if list[i]==n:
			globals()['pos']=i
			return True
			
lst= [4,5,6,1,2,8]
n=1
if search(lst,n):
	print("Found at position of", pos+1)
else:
	print("Not found")	
