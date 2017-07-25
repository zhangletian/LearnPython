from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.bilibili.com/ranking'
html = urlopen(url)
bsObj = BeautifulSoup(html)

titlelist = []

titleset = bsObj.findAll('div',{'class':'title'})
rankset = bsObj.findAll('i',{'class':'b-icon b-icon-v-play'})

print(titleset)
print(rankset)