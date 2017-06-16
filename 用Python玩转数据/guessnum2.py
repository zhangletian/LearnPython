from random import randint

x = randint(0,300)

for count in range(5):
	print('Please input a number between 0-300:')
	digit = int(input())
	if digit == x:
		print('Bingo!')
		break
	elif digit > x:
		print('Too large,please try again!')
	elif digit < x:
		print('Too small,please try agagin!')
