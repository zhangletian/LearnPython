aStr = 'Hello,World!'
bStr = aStr[:7] + 'Python!'
count = 0
for ch in bStr[:]:
	if ch in ',.:!?':
		count += 1
print(count)
print('Punctuation marks = ',count)
if count >= 2:
	print('There are ' + str(count) + ' punctuation marks')
elif count < 2:
	print('There is ' + str(count) + 'punctuation mark')
