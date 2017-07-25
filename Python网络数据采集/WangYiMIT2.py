from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://open.163.com/special/opencourse/bianchengdaolun.html?referered=http%3A%2F%2Fopen.163.com%2Fspecial%2Fopencourse%2Fbianchengdaolun.html'
html = urlopen(url)
bsObj = BeautifulSoup(html)

titleset = bsObj.find('h2')
title = titleset.string

chapterlist = []
chapterset = bsObj.findAll('td',{'class':'u-ctitle'})
print(chapterset)

for link in bsObj.find('table').findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

filename = 'mit2.csv'
with open (filename,'w') as file_object:
    for chapter in chapterset:
        file_object.write(str(chapter) + '\n')