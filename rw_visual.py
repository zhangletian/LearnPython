#coding=gbk

import matplotlib.pyplot as plt
from random_walk import RandomWalk

#ֻҪ�����ڻ״̬���Ͳ��ϵ�ģ���������
while True:
	#����һ��RandomWalkʵ��������������ĵ㶼���Ƴ���
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_values,rw.y_values,s=15)
	plt.show()

	keep_running = input('make another walk?(y/n):')
	if keep_running == 'n':
		break
