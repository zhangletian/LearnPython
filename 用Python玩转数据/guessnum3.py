from random import randint

x = randint(0,300)
go = 'y'
while(go == 'y'):
	message = 'Please input a number between 0-300:'
	digit = int(input(message))
	if digit == x:
		print('Bingo!')
		break
	elif digit > x:
		message_large = "Too large,please try again."
		print(message_large)
	elif digit < x:
		message_small = "Too small,please try again."
		print(message_small)
	print("Input 'y' if you want to continue")
	go = input()
print('Goodbye!')
