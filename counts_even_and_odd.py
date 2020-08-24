lst=[12,15,76,46,42,41,43,97,95,89,16,43,76]

def counts(lst):
	even=0
	odd=0
	for i in range(len(lst)):
		if i%2==0:
			even+=1
		else:
			odd+=1
	return even,odd

even,odd=counts(lst)	
print("Total even no. are: {}, Total odd no. are:{}".format(even,odd))		
	
