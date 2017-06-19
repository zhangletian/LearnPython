week = ['Monday','Tuseday','Wednesday','Thursday','Friday']
weekend = ['Satuday','Sunday']
week.extend(weekend)
for i,j in enumerate(week):
	print(i+1,j)

week.append(weekend)
print(week)
