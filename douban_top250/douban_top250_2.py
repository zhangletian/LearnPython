
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
html = urlopen(url)
bsObj = BeautifulSoup(html)
# print(bsObj)

spanSet = bsObj.findAll('span',attrs = {'class':'title'})
# print(spanSet)
onlyname = []
for span in spanSet:
	imageName = span.string
	if imageName.find(' / ') == -1:
		onlyname.append(imageName)
		# print(imageName)
# print(onlyname)

filename = 'DoubanMoviesTop250.txt'
top_num = 1
with open (filename,'w') as file_object:
    for name in onlyname:
        file_object.write('Top'+ str(top_num) + ' ' + name+'\n')
        top_num += 1

