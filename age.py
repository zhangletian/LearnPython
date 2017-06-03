age = input('Your age:')
age = int(age)
if age<=4:
	price = 0
elif age <18:
	price = 5
elif age>=18:
	price = 10
print('Your price is ' + str(price) + '!')
