from math import sqrt
j = 2
while j <= 100:
	i = 2
	k = sqrt(j)
	while i <= k:
		if j%i ==0:
			break
		i = i + 1
	if i > k:
		print(j,end=' ')
	j += 1
	
print('\n')

from math import sqrt
for i in range(2,101):
	flag = 1
	k = int(sqrt(i))
	for j in range(2,k+1):
		if i % j == 0:
			flag = 0
			break
	if (flag):
			print(i,end=' ')
