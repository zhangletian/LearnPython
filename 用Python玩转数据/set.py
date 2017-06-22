#coding=gbk

aSet = set('sunrise')
bSet = set('sunset')

print(aSet & bSet)
print(aSet | bSet)
print(aSet - bSet) #属于aSet，但不属于bSet
print(aSet ^ bSet) #不同时存在两者的元素

#$、|、-、^运算符可以与 = 直接复合使用：&=、|=、-=、^=
aSet-=set('sun')
print(aSet)
