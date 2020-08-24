def person(name,age):		#position Argument
	print(name)
	print(age)
	
person('Avinash',25)			


def person(name,age):		#keyword Argument
	print(name)
	print(age)
	
person(age=25, name='Avinash')	

def person(name,age=25):		#default Argument
	print(name)
	print(age)
	
person('Avinash')			

def sum(*b):			#variable argument
	c=0
	for i in b:
		c+=i
	print(c)

sum(4,5,6,8,9)
