#print('Give me two numbers,and I will divide them.')
#print("Enter 'q' to quit")

#while True:
	#first_number = input('First number:')
	#if first_number == 'q':
		#break
	#second_number = input('Second_number:')
	#if second_number == 'q':
		#break
	#try:
		#result = int(first_number) / int(second_number)
	#except ZeroDivisionError:
		#print('You can not divide by 0!')
	#else:
		#print(result)

def count_words(filename):
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		msg = 'Sorry,the file ' + filename + ' does not exit.'
		print(msg)
	else:
		words = contents.split()
		num_words = len(contents)
		message = 'The file ' + filename + ' has about ' + str(num_words) + ' words.'
		print(message)

filename = 'wonderland.txt'
count_words(filename)
