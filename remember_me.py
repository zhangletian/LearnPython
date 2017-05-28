##number_writer
#import json

#numbers = [2,3,5,7,11,13]
#filename = 'numbers.json'
#with open(filename,'w') as file_object:
	#json.dump(numbers,file_object)

#with open(filename) as file_object:
	#numbers2 = json.load(file_object)
#print(numbers2)

##remember_me.py
#import json
#username = input('What is your name? ')
#filename = 'username.json'
#with open(filename,'w') as file_object:
	#json.dump(username,file_object)
	#message = "We'll remember you when you come back, " + username + "!"
	#print(message)

##greet_user.py
#import json
#filename = 'username.json'
#with open(filename) as file_object:
	#username = json.load(file_object)
	#print('Welcome back, ' + username + '!')

#import json
#filename = 'username.json'
#try:
	#with open(filename) as file_object:
		#username = json.load(file_object)
#except FileNotFoundError:
	#print('The file ' + filename + ' does not exit.')
	#username = input('What is your name ? ')
	#with open(filename,'w') as file_object:
		#json.dump(username,file_object)
		#message = 'We will remember you when you come back,' + username.title() + '!'
		#print(message)
#else:		
	#print('Welcome back, ' + username.title() + '!')

#import json

#def get_stored_username():
	#filename = 'username.json'
	#try:
		#with open(filename) as file_object:
			#username = json.load(file_object)
	#except FileNotFoundError:
		#return None
	#else:
		#return username

#def greet_user():
	#username = get_stored_username()
	#if username:
		#print('Welcome back,' + username + '!')
	#else:
		#username = input('What is your name? ')
		#with open(filename,'w') as file_object:
			#json.dump(username,file_object)
			#print('We will remember you when you come back,' + username +'.')
 
#greet_user()
 
import json

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_user():
	username = input('What is your name?')
	filename = 'username.json'
	with open(filename,'w') as file_object:
		json.dump(username,file_object)
		
	return username

def greet_user():
	username = get_stored_username()
	if username:
		print('Welcome back,' + username + '!')
	else:
		username = get_new_user()
		print('We will remember you when you come back,' + username +'.')
 
greet_user()
