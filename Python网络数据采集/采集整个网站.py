#coding=gbk

#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#import re

#pages = set()
#def getLinks(pageUrl):
	#global pages
	##url = 'http://en.wikipedia/org' + pageUrl
	#html = urlopen('http://en.wikipedia/org' + pageUrl)
	#bsObj = BeautifulSoup(html)
	#for link in bsObj.findAll('a',href = re.compile('^(/wiki/)')):
		#if 'href' in link.attrs:
			#if link.attrs['href'] not in pages:
				#newPage = link.attrs['href']
				#print(newPage)
				#pages.add(newPage)
				#getLinks(newPage)

#getLinks('')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen('http://en.wikipedia.org' + pageUrl)
	bsObj = BeautifulSoup(html)
	try:
		print(bsObj.h1.get_text())
		print(bsObj.find(id = 'mw_content-text').findAll('p')[0])
		#print(bsObj.find(id = 'mw_content-text').find('p'))
		print(bsObj.find(id = 'ca-edit').find('span').find('a').attrs['href'])
	except AttributeError:
		print('页面缺少一些属性！')

	for link in bsObj.findAll('a',href = re.compile('^(/wiki/)')):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print('-----------------\n'+newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks('')
