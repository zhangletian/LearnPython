from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.smzdm.com/jingxuan/'
html = urlopen(url)
bsObj = BeautifulSoup(html)

