from nltk.corpus import gutenberg

allwords = gutenberg.words('shakespeare-hamlet.txt')
print(len(allwords))
print(len(set(allwords)))
print(allwords.count('Hamlet'))

A = set(allwords)
longwords = [w for w in A if len(w)>12]
print(sorted(longwords))
