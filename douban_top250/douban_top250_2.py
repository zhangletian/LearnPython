
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = 'https://movie.douban.com/top250'
urlList = []
onlyname = []
ratingList = []
peopleList = []
for i in range(0,250,25):
    url = 'https://movie.douban.com/top250?start={start}&filter='.format(start=i)
    urlList.append(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)

    spanSet = bsObj.findAll('span',attrs = {'class':'title'})
    for span in spanSet:
        imageName = span.string
        if imageName.find(' / ') == -1:
            onlyname.append(imageName)

    ratingSet = bsObj.findAll('span',attrs={'class':'rating_num'})
    for rating_num in ratingSet:
        ratingList.append(rating_num.string)

    peopleSet = bsObj.findAll('div',attrs={'class':'star'})#用兄弟标签

		# print(imageName)
# print(onlyname)

# print(spanSet)
# print(ratingSet)
# print(ratingList)
print(peopleSet)


# filename = 'DoubanMoviesTop250.txt'
# top_num = 1
# with open (filename,'w') as file_object:
#     for name in onlyname:
#         file_object.write('Top'+ str(top_num) + ' ' + name+'\n')
#         top_num += 1