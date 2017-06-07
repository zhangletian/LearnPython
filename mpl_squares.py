#coding=gbk
import matplotlib.pyplot as plt

#input_values = [1,2,3,4,5]
#squares = [1,4,9,16,25]
#plt.plot(input_values,squares,linewidth=5)

#plt.scatter(2,4,s=200)

x_values=list(range(1,1001))
y_values=[i**2 for i in x_values]
#plt.scatter(x_values,y_values,c='red',edgecolor='none',s=10)
#plt.scatter(x_values,y_values,c=(0,0,0.5),edgecolor='none',s=40)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
	edgecolor='none',s=40)

#设置图表标题，并给坐标轴加上标签
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of value',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')
