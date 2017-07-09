#coding=gbk

from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

url = 'https://movie.douban.com/top250'
html = urlopen(url)
soup = BeautifulSoup(html.read())
#spanSet = soup.findAll('span',attrs = {'class':'title'})

#for child in soup.findAll('span',{'class':'title'},recursive=False).children:
	#print(child)
	
spanSet = soup.findAll('span',attrs = {'class':'title'})

print(spanSet)

for span in spanSet:
	print(span.get_text())


#for span in spanSet:
	#imageName = span.string
	#if imageName.find('&nbsp') == -1:
		#print(imageName)

#fileHandle = open('DoubanMoviesTop250.txt','w+')
#fileHandle.write(imageName)
#fileHandle.close()
