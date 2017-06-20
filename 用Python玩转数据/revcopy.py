filename = 'companies.txt'
with open(filename,'w') as file_object:
	#file_object.write('GOOGLE Inc.')
	#file_object.write('\nMicrosoft Corporation')
	#file_object.write('\nApple Inc.')
	#file_object.write('\nFacebook Inc.')
	file_object.write('GOOGLE Inc.\nMicrosoft Corporation\nApple Inc.\nFacebook Inc.')

f1 = open(r'companies.txt')
cNames = f1.readlines()
for i in range(0,len(cNames)):
	cNames[i] = str(i+1) + ' ' + cNames[i]
f1.close()

with open()

f2 = open(r'scompanies.txt','w')
f2.writelines(cNames)
f2.close
