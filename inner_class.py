class student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
		self.lap=self.laptop()
		
	def show(self):
		print(self.name,self.rollno)
		self.lap.show()
		
	class laptop:
		def __init__(self):
			self.ram='4GB'
			self.model='i5'
			
		def show(self):
			print(self.ram,self.model)
			
s1=student('Avinash',424)
S2=student('Abhay',426)

s1.show()				
