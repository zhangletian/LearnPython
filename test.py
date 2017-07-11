# -*- coding: utf-8 -*-
# coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

for page in range(0,250,25):
    url = 'https://book.douban.com/top250?start=£ûstart£ý'.format(start=page)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)

    for title in bsObj.findAll('a'):
        if 'title' in title.attrs:
            print(title.attrs['title'])

