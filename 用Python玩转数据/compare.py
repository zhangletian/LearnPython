#sStr = 'acdhdca'
#if(sStr==''.join(reversed(sStr))):
	#print('Yes')
#else:
	#print('No')

import operator
sStr = 'acdhdca'
if operator.eq(sStr,''.join(reversed(sStr))) == 0:
	print('Yes')
else:
	print('No')
