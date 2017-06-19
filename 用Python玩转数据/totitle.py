aStr = 'What do you think of this saying "No pain,No gain"?'
#lindex = aStr.index('\"',0,len(aStr))
#rindex = aStr.rindex('\"',0,len(aStr))
#tempStr = aStr[lindex+1:rindex]
tempStr = aStr.split("\"")[1]
if tempStr.istitle():
	print('It is title format.')
else:
	print('It is not title format.')
print(tempStr.title())
