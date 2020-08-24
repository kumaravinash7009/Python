x=int(input("enter your number: "))
if x>1:
	for i in range(2,x):
		if x%i==0:
			print("not a prime no.")
			break
	else :
		print("no is prime")
	
	
