#coding=gbk
import requests

url = 'https://api.douban.com/v2/book/26319730'
r = requests.get(url)
print(r.text)

url = 'https://api.douban.com/v2/movie/subject/:1291546'
r = requests.get(url)
print(r.text)
