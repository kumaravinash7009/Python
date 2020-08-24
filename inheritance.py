class A:
	def feature1(self):
		print("feature1 working")
	def feature2(self):
		print("feature2 working")
		
class B(A):					#multilayer inheritance
	def feature3(self):
		print("feature3 working")
	def feature4(self):
		print("feature4 working")
class C(B):					#or class C(A,B) for multiple inheritance
	def feature5(self):
		print("feature5 working")	
		
c1=C()
c1.feature5()	
		
		
