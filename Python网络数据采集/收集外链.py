#coding=gbk

from urllib.request import urlopen
from bs4 import BeautifulSoup

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl)
	bsObj = BeautifulSoup(html)
	internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
	externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.all(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			print('������ȡ���ӵ�URL�ǣ�' + link)
			allIntLinks.add(link)
			getAllExternalLinks(link)

getAllExternalLinks('http://oreilly.com')
