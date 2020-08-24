a=6
b=0
try:
	print("Resource opened")
	k=int(input("Enter your no.: "))
	print(a/b)
except ZeroDivisionError as e:
	print("Hey, you cannot divide no. by zero",e)
except ValueError as f:
	print("Invalid Output",f)
except Exception as g:
	print("Something went wrong..")

finally:
	print("Resource closed")
