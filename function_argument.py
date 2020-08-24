def update(x):
	print(id(x))
	x=8
	print(id(x))
	print("x", x)
	
a=10
print(id(a))
update(a)
print('a',a)

print('')


def update(lst):
	print(id(lst))
	lst[1]=8
	print(id(lst))
	print("lst", lst)
	
lst=[10,3,4]
print(id(lst))
print('lst',lst)
update(lst)
print('lst',lst)


