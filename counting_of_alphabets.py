lst=[]
n=int(input('Enter the number of name:'))

for i in range(n):
	
	lst.append(input('enter the next name: '))
print(lst)

def counts(lst):
	more=0
	less=0
	for a in range(len(lst)):
		if len(lst[a])>5:
			more+=1
		else:
			less+=1
	return more,less	
		

more,less =counts(lst)
print("No. of students less than 5 alphabets are: {} and more than 5 are: {}".format(less,more))				
