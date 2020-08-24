class A:
	def __init__(self):
		print("in A init")	
	def feature1(self):
		print("feature1 working")
	def feature2(self):
		print("feature2 working")
		
class B:					
	def __init__(self):
		print("in B init")
	def feature3(self):
		print("feature3 working")
	def feature4(self):
		print("feature4 working")
class C(A,B):					
	def __init__(self):
		super().__init__()		#calling init from upper class. (left to right rule)
		print("in C init")
	def feature5(self):
		print("feature5 working")	
		
c1=C()
c1.feature5()

