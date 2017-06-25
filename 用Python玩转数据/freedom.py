#coding=gbk

from nltk import *
from nltk.corpus import inaugural

#注意，要先去nltk.download()下载inaugural

fd3 = FreqDist([s.lower() for s in inaugural.words()])
print(fd3.freq('freedom'))
