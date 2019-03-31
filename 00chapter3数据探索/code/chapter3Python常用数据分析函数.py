import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 线形图
# x = np.linspace(0, 4*np.pi, 100)
# y = np.sin(x)
# plt.plot(x, y, 'rp--')

# 饼图
# labels = ['frog', 'hogs', 'dogs', 'logs']
# sizes = [15, 30, 45, 10]
# colors = ['red', 'yellow', 'gold', 'green']
# explode = (0, 0.1, 0, 0) # 突出显示参数，这里突出显示第二块
# plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
# # autopct参数：显示数据百分比形式，保留一位小数
# # startangle参数：第一块的起始角度，正东为0度，正北为90度
# # shadow参数: 是否显示阴影

# hist直方图，可以显示数据分布
# x = np.random.randn(1000)  # 1000个服从正态分布的随机数
# n, bins, patches = plt.hist(x, 12)  # 分成12组生成直方图
# print(n)    # 显示每个面元包含的数据数量
# print('------------------------------------------')
# print(bins)  # 显示每个面元划分的边界值
# print('------------------------------------------')
# print(patches)   # 显示数据类型为list
# print('------------------------------------------')

# 绘制盒须图
# x = np.random.randn(100)
# df = pd.DataFrame([x, x+1]).T   # 生成两列的dataframe
# print(df)
# # df.plot(kind='box')
# df.boxplot()


# 对数数据图
# x = pd.Series(np.exp(np.arange(0,5,0.2)))
# x.plot(label=u'原始数据图', legend=True)
# plt.show()
# x.plot(logy=True, label=u'对数数据图', legend=True)

# 误差图
error = np.random.randn(10)
y = pd.Series(np.sin(np.arange(10)))
y.plot(yerr=error)
plt.show()
y.plot(xerr=error)

plt.show()