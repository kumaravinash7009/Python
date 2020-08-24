class car:
	wheels=4		#class variables
			
	def __init__(self):		#instance variables
		self.min=10
		self.name="BMW"

car1=car()
car2=car()

car2.min=8

print(car1.min,car1.name,car1.wheels)
print(car2.min,car2.name,car2.wheels)		

