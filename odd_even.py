x=int(input("please Enter 1st your no.: "))
y=int(input("please Enter 2st your no.: "))
z=int(input("please Enter 3st your no.: "))
if (x>=y)&(x>=z):
	print(x)
elif (y>=x) & (y>=z):
	print(y)
else:
	print(z)