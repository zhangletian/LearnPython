from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://open.163.com/special/opencourse/bianchengdaolun.html?referered=http%3A%2F%2Fopen.163.com%2Fspecial%2Fopencourse%2Fbianchengdaolun.html'
html = urlopen(url)
bsObj = BeautifulSoup(html)

titleset = bsObj.find('h2')
title = titleset.string

chapterlist = []
chapterset = bsObj.findAll('td',{'class':'u-ctitle'})
for chapter in chapterset:
    clear = chapter.get_text().strip().replace(' ','').replace('\n','')
    chapterlist.append(clear)
chapterlist = chapterlist[10:]
print(chapterlist)

purechapterlist = []
numlist = []
titlelist = []
for chapter in chapterlist[:9]:
    num = chapter[:5]
    title = chapter[5:]
    numlist.append(num)
    titlelist.append(title)
for chapter in chapterlist[9:]:
    num = chapter[:6]
    title = chapter[6:]
    numlist.append(num)
    titlelist.append(title)
print(numlist)
print(titlelist)

filename = 'mit.csv'
with open (filename,'w') as file_object:
    for (num,title) in zip(numlist,titlelist):
        file_object.write(num + ',' + title + '\n')