# -*- coding: utf-8 -*-
# coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

titleList = []
ratingList = []
peonumList = []
for page in range(0,250,25):
    url = 'https://book.douban.com/top250?start={start}'.format(start=page)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)

    for title in bsObj.findAll('a'):
        if 'title' in title.attrs:
            # print(title.attrs['title'])
            titleList.append(title.attrs['title'])

    ratingSet = bsObj.findAll('span',{'class':'rating_nums'})
    for rating in ratingSet:
        ratingList.append(rating.string)

    peopleSet = bsObj.findAll('span',{'class':'pl'})
    for peonum in peopleSet:
        peonumList.append(peonum)
    # peopleSet = bsObj.find('span', attrs={"class": "pl"}).string.strip('\r\n ()人评价')


# print(titleList)
# print(ratingList)
# print(peonumList)

filename = 'DoubanBooksTop250.csv'
top_num = 1
with open (filename,'w') as file_object:
    for (name,rating_num) in zip(titleList,ratingList):
        file_object.write('Top'+ str(top_num) + ',' + name + ',' + str(rating_num) + '\n')
        top_num += 1