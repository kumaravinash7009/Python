class computer:
	def __init__(self):
		self.name="avinash"
		self.age=25
		
	def compare(self, other):
		if self.age==other.age:
			print("they are same.")
		else:
			print("they are different.")

c1=computer()
c2=computer()

c1.name="bhargavi"
c1.age=26

c1.compare(c2)

print(c1.name,c1.age)
print(c2.name,c2.age)
		
