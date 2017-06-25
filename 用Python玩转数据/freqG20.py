from nltk.corpus import gutenberg
from nltk.probability import *

allwords = gutenberg.words('shakespeare-hamlet.txt')
fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])
print(fd2.B())
print(fd2.N())
fd2.tabulate(20)
fd2.plot(20)
fd2.plot(20,cumulative = True)
