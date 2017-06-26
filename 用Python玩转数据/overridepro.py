from doginsta import Dog

class BarkingDog(Dog):
	def greet(self):
		print('Wood!I am %s,my number is %d'%(self.name,Dog.counter))

if __name__ == '__main__':
	dog = BarkingDog('Zoe')
	dog.greet()
