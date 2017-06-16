from random import randint

x = randint(0,300)
digit = int(input('Please input a number between 0-300:'))

if digit == x:
	print('Bingo!')
elif digit > x:
	print('Too large!')
else:
	print('Too small')
