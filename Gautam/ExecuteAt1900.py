import schedule 
import time

c=1  
def fac(n):
	global c
	c=c*n
	n=n-1
	if n>1:
		fac(n)
	return c
def value():
	x=fac(5)
	print("Value : ", x)


	# now calling factorial function everyday at 07:00PM 
schedule.every().day.at("19:00").do(value)

while True: 
    schedule.run_pending() 
    time.sleep(1)