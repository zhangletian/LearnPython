aInfo = {'Wangdachui':3000,'Niuyun':2000,'Linling':4500,'Tianqi':8000}

info = [('Wangdachui',3000),('Niuyun',2000),('Linling',4500),('Tianqi',8000)]
bInfo = dict(info)

cInfo = dict([['Wangdachui',3000],['Niuyun',2000],['Linling',4500],['Tianqi',8000]])

dInfo = dict(Wangdachui=3000,Niuyun=2000,Linling=4500,Tianqi=8000)

aDict = {}.fromkeys(('Wangdachui','Niuyun','Linling','Tianqi'),3000)

eDict = dict(zip(names,slaries))

pList = []
aList = []
bList = []
for i in range(len(pList)):
	aStr = pList[i][0]
	bStr = pList[i][2]
	aList.append(aStr)
	bList.append(bStr)
aDict = dict(zip(aList,bList))
print(sDict)
