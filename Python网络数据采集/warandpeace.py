from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#url = 'http://www.pythonscraping.com/pages/warandpeace.html'
#html = urlopen(url)
#bsObj = BeautifulSoup(html,'lxml')
#nameList = bsObj.findAll('span',{'class':'green'})
#for name in nameList:
	#print(name.get_text())	

url = 'http://www.pythonscraping.com/pages/page3.html'
html = urlopen(url)
bsObj = BeautifulSoup(html,'lxml')
#for child in bsObj.find('table',{'id':'giftList'}).children:
	#print(child)

for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
	print(sibling)

images = bsObj.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
	print(image)
	print(image['src'])
