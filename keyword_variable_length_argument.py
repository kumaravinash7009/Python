def person(name,**data):
	print(name)
	print(data)
	
person('avinash',age=25, place='Muzaffarpur', mobile=7002916241)


def person(name,**data):
	print(name)
	for i,j in data.items():
		print(i,j)
	
person('avinash',age=25, place='Muzaffarpur', mobile=7002916241)	
