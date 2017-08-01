import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import pygal

# df = ts.get_gdp_year()
# df.to_excel('gdp.xlsx')

# df.gdp.plot()
#
# ax = plt.gca()
# # ax.invert_xaxis()
# plt.show()

filename = 'gdp.xlsx'
df = pd.read_excel(filename)

# plt.plot(df['year'],df['gdp'],c='red')
# # plt.gca().invert_xaxis()
#
# plt.title('GDP 1952 - 2016')
# plt.xlabel('Year')
# plt.ylabel('Money')
#
# plt.show()

gdplist = list(df['gdp'])
gdplist.reverse()

hist = pygal.Bar()

hist.title = 'GDP 1952 - 2016'
# hist.x_labels = list(str(i) for i in range(1952,2017))
hist.x_labels = map(str, range(1952,2017))

hist.x_title = 'Year'
hist.y_title = 'Money'

hist.add('GDP',gdplist)
plt.gca().invert_xaxis()
hist.render_to_file('GDP.svg')