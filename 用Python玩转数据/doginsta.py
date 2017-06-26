class Dog(object):
	counter = 0
	#def setName(self,name):
	def __init__(self,name):
		self.name = name
		Dog.counter += 1
	def greet(self):
		print('Hi,I am called %s.'%self.name,Dog.counter)

if __name__ =='__main__':
	dog = Dog('XiaoQiang')
	dog.greet()
