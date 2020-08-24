a=10

def something():
	a=16
	print("inside fucntion", a)
something()
print("outside function", a)

def something1():
	print("inside fucntion", a)
something1()
print("outside function", a)

def something2():
	global a
	a=16
	print("inside fucntion", a)
something2()
print("outside function", a)


def something3():
	global a
	a=16
	print("inside fucntion", a)
something3()
print("outside function", a)

a=10
print(id(a))
def something4():
	a=9
	x=globals()['a']			#using x as a global variable
	print(id(x))
	print("inside fucntion", a,x)
	globals()['a']=16		#changing global variable a
something4()
print("outside function", a)
