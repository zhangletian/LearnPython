filename = 'programming.txt'
with open(filename,'w') as file_object:
	file_object.write('I love programming.\n')
	file_object.write('I love creating games.\n')

with open(filename,'a') as file_object:
	file_object.write('I also love finding meaning in large datasets.\n')
	file_object.write('I love creating apps that can run in a browser.\n')

with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

name = ''
reason = ''
guest_filename = 'guest.txt'
guest_book_filename = 'guest_book.txt'
guest_reason_filename = 'reason.txt'
active = True
while active:
	name = input('Enter your name :')
	if name == 'quit':
		active = False
	if name != 'quit':
		with open(guest_filename,'a') as file_object:
			file_object.write(name.lower() + '\n')
		print('Hello,' + name.title())
		with open(guest_book_filename,'a') as file_object:
			file_object.write(name.lower() + ' visits.\n')
		reason = input('Why do you love programming :')
		if reason == 'quit':
			with open(guest_reason_filename,'a') as file_object:
				file_object.write(name.lower() + ':no reason\n')
			active = False
		if reason != 'quit':
			with open(guest_reason_filename,'a') as file_object:
				file_object.write(name.lower() + ':' + reason.lower() + '\n')
	
with open(guest_filename) as file_object:
	contents = file_object.read()
	print(contents.title())

with open(guest_reason_filename) as file_object:
	contents = file_object.read()
	print(contents.title())
