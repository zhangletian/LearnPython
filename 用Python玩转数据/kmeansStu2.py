import numpy as np
from sklearn.cluster import KMeans

list1 = [88,74,96,85]
list2 = [92,99,95,94]
list3 = [91,87,99,95]
list4 = [78,99,97,81]
list5 = [88,78,98,84]
list6 = [100,95,100,92]

X = np.array([list1,list2,list3,list4,list5,list6])
kmeans = KMeans(n_clusters=2).fit(X)
pred = kmeans.predict(X)
print(pred)
