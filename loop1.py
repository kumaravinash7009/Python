x=1
while x<=100:
	r=x%3
	s=x%5
	if(r==0)|(s==0):
		print(" ",end="")
	else:	
		print(x,"" ,end="")
	x+=1

	
