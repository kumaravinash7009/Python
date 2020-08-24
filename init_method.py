class computer:
	def __init__(self,cpu,ram):
		self.cpu=cpu
		self.ram=ram
		
	def config(self):
		print("computer configuration is: ", self.cpu, self.ram)
	
com1=computer('intel', '4gb')
com2=computer('IOS','8gb')		

com1.config()
com2.config()
