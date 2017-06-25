from nltk import *
from nltk.corpus import inaugural

cfd = ConditionalFreqDist(
			(fileid,len(w))
			for fileid in inaugural.fileids()
			for w in inaugural.words(fileid)
			if fileid > '1980' and fileid < '2010')

print(cfd.items())
cfd.plot()
