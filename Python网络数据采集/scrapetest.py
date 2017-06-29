from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except (HTTPError,URLError) as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

def getNameList(url):
	try:
		html = urlopen(url)
	except (HTTPError,URLError) as e:
		return None
	bsObj = BeautifulSoup(html,'lxml')
	nameList = bsObj.findAll('span',{'class':'green'})
	nameOnlyList = sorted(set(nameList),key=nameList.index)
	for name in nameOnlyList:
		print(name.get_text())	

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
nameList = getNameList(url)



#title = getTitle(url)	
#if title == None:
	#print('Title cound not be found.')
#else:
	#print(title)

#http://www.pythonscraping.com/pages/page1.html
#http://www.pythonscraping.com/pages/warandpeace.html
#http://www.pythonscraping.com/pages/page3.html
