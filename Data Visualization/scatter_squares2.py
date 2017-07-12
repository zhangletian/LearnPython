import matplotlib.pyplot as plt

x_values = list(x for x in range(1,1001))
y_values = list(x**2 for x in x_values)

# plt.scatter(x_values,y_values,edgecolor='none',c=(0,0,0),s=10)
# plt.scatter(x_values,y_values,edgecolor='none',c=(0,0,0),s=10)
plt.scatter(x_values,y_values,edgecolor='none',c=y_values,cmap=plt.cm.YlGn,s=10)

#http://matplotlib.org/examples/color/colormaps_reference.html

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])

plt.savefig('squares_plot2.png',bbox_inches='tight')

plt.show()