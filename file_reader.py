with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

print('\n')

file_path = r'E:\python_work\pi_digits.txt'
with open(file_path) as file_object2:
	contents2 = file_object2.read()
	print(contents2.rstrip())

print('\n')

filename = 'pi_digits.txt'
with open(filename) as file_object3:
	for line in file_object3:
		print(line.rstrip())

print('\n')

with open(filename) as file_object4:
	lines = file_object4.readlines()

for line in lines:
	print(line.rstrip())

print('\n')

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print('\n')

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + '...')
print(str(len(pi_string)) + '\n')

#birthday = input('Enter your birthday,in the form yymmdd: ')
#if birthday in pi_string:
	#print('Your birthday appears in the first million digits of pi!')
#else:
	#print('Your birthday does not appear in the first million digits of pi.')
