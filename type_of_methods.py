class student:
	school='JNV'
	def __init__(self,m1,m2,m3):		
		self.m1=m1
		self.m2=m2
		self.m3=m3
		
	def avg(self):				#instance methods
		return (self.m1+self.m2+self.m3)/3
		
	@classmethod				#class methods
	def getschool(cls):
		return cls.school
		
	@staticmethod				#static methods
	def info():
		print("today is a great day!")
		

s1=student(34,47,32)
s2=student(89,32,12)

print(s1.avg())
print(student.getschool())

student.info()		 
