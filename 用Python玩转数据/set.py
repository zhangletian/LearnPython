#coding=gbk

aSet = set('sunrise')
bSet = set('sunset')

print(aSet & bSet)
print(aSet | bSet)
print(aSet - bSet) #����aSet����������bSet
print(aSet ^ bSet) #��ͬʱ�������ߵ�Ԫ��

#$��|��-��^����������� = ֱ�Ӹ���ʹ�ã�&=��|=��-=��^=
aSet-=set('sun')
print(aSet)
