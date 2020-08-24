lst = [6,7,4,3,2,1,4,5]

def peakfinder(lst):
	pos=[]
	n=len(lst)
	for i in range(len(lst)):
		if i==n-1:
			if lst[i]>=lst[i-1]:
				pos.append(i)
		elif i==0:
			if lst[i]>=lst[i+1]:
				pos.append(i)
		else:
			if lst[i]>=lst[i-1] and lst[i]>=lst[i+1]:
				pos.append(i)
	print(pos)

a=peakfinder(lst)
print(a)			 		