#coding=gbk

import matplotlib.pyplot as plt
from random_walk import RandomWalk

#只要程序处于活动状态，就不断地模拟随机漫步
while True:
	#创见一个RandomWalk实例，并将其包含的点都绘制出来
	rw = RandomWalk()
	rw.fill_walk()

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
		edgecolor='none',s=15)
	
	#突出起点与终点
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
		s=100)
		
	plt.show()

	keep_running = input('make another walk?(y/n):')
	if keep_running == 'n':
		break
