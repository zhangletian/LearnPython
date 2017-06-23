import pandas as pd
import numpy as np

data = {'name':['Wangdachui','Linling','Niuyun'],'pay':[4000,5000,6000]}
frame = pd.DataFrame(data)
print(frame)

data2 = np.array([('Wangdachui',4000),('Cuihua',5000),('Tiezhu',6000)])
frame2 = pd.DataFrame(data,index=range(1,4),columns=['name','pay'])
print(frame2)

#frame2.index = range(2,5)
#print(frame2)

print(frame2.name)
print('\n')
print(frame2.pay.min())
print(frame2[frame2.pay>=5000])
