# -*- coding: utf-8 -*-
# coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

titleList = []
for page in range(0,250,25):
    url = 'https://book.douban.com/top250?start={start}'.format(start=page)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)

    for title in bsObj.findAll('a'):
        if 'title' in title.attrs:
            # print(title.attrs['title'])
            titleList.append(title.attrs['title'])

print(titleList)
# urlList = []
# onlyname = []
# ratingList = []
# peopleList = []
# for i in range(0,250,25):
#     url = 'https://movie.douban.com/top250?start={start}&filter='.format(start=i)
#     urlList.append(url)
#     html = urlopen(url)
#     bsObj = BeautifulSoup(html)
#
#     spanSet = bsObj.findAll('span',attrs = {'class':'title'})
#     for span in spanSet:
#         imageName = span.string
#         if imageName.find(' / ') == -1:
#             onlyname.append(imageName)
#
#     ratingSet = bsObj.findAll('span',attrs={'class':'rating_num'})
#     for rating_num in ratingSet:
#         ratingList.append(rating_num.string)
