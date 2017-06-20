filename_c = 'companies_own.txt'
filename_sc = 'scompanies_own.txt'
with open(filename_c,'w+') as file_object:
	#file_object.write('GOOGLE Inc.')
	#file_object.write('\nMicrosoft Corporation')
	#file_object.write('\nApple Inc.')
	#file_object.write('\nFacebook Inc.')
	file_object.write('GOOGLE Inc.\nMicrosoft Corporation\nApple Inc.\nFacebook Inc.')
	cNames = file_object.readlines()

with open(filename_sc,'w+') as file_object_sc:
	for i in range(0,len(cNames)):
		cNames[i] = str(i+1) + ' ' + cNames[i]
		file_object_sc.write(cNames)
