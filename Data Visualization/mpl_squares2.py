import matplotlib.pyplot as plt

input_values = list(i for i in range(1,6))
squares = list(i**2 for i in input_values)

plt.plot(input_values,squares,linewidth=5)

plt.title('Squares Numbers',fontsize=24)
plt.xlabel('Values',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

plt.tick_params(axis='both',labelsize=14)
plt.show()

# print(input_values)
# print(squares)