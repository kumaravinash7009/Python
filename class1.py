class computer:
	def config(self):				#creating a class or blueprint or model
		print("i5 500gb 4gb ram")
	
x=9
print(type(x))

a='8'
print(type(a))

com1=computer()			# 1st object made by class computer
com2=computer()			# 2nd object made by class computer

computer.config(com1)
computer.config(com2)
print("")
com1.config()
com1.config()
		
