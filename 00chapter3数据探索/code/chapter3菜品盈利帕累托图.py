import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_excel('../data1/catering_dish_profit.xls')
# print(data1)
data_profit = data[u'盈利'].copy()
data_dish = data[u'菜品名'].copy()
# print(data_profit)
# print(data_dish)
x = np.array(data_dish)
y = np.array(data_profit/10000)
print(x, y)

data_profit.sort_values(ascending=False)
print(data_profit)

# 用来正常显示中文标签的预处理代码
plt.rcParams['font.sans-serif'] = ['simHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.bar(x, y, color='orange')
p = y.cumsum() / y.sum()
print(p)
plt.ylabel(u'盈利(万元)')
plt.plot(p, 'r-o', linewidth=2)

plt.annotate(format(p[6], '.4%'),
             xy=(6, p[6]),
             xytext=(6*0.9, p[6]*0.9),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# plt.show()
plt.savefig('../chart/菜品盈利的帕累托图.jpg')