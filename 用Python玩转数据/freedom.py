#coding=gbk

from nltk import *
from nltk.corpus import inaugural

#ע�⣬Ҫ��ȥnltk.download()����inaugural

fd3 = FreqDist([s.lower() for s in inaugural.words()])
print(fd3.freq('freedom'))
