import requests
from bs4 import BeautifulSoup
import re

markup = '<p class="title"><b>The Little Prince</b></p>'
soup = BeautifulSoup(markup,'lxml')
print(soup.b)
print(soup.p)
print(type(soup.b))
print(type(soup.p))
print(soup.find_all('b'))

url = 'https://book.douban.com/subject/1084336/'
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
	print(item.string)

sum = 0
pattern_s = re.compile('<span class="user-stars allstar(.*) rating"')
p = re.findall(pattern_s,r.text)
for star in p:
	sum += int(star)
print(sum)
