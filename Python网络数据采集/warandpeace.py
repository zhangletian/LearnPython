from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
html = urlopen(url)
bsObj = BeautifulSoup(html,'lxml')
nameList = bsObj.findAll('span',{'class':'green'})
for name in nameList:
	print(name.get_text())	

