import sys

sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

x=0
def rec():
	global x
	x+=1
	print("hello",x)
	rec()

rec()
	
	
