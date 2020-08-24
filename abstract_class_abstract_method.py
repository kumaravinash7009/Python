from abc import ABC, abstractmethod

class Computer(ABC):
	@abstractmethod
	def process(self):
		pass
		
class laptop(Computer):
	def process(self):
		print("its running")
		
#com=Computer()
com1=laptop()
com1.process()		
