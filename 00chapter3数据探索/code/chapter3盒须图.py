import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('../data1/catering_sale.xls', index_col=u'日期')
# print(data1.describe())
# print(data1)
# print(data1.isnull().any())    # true
# print(data1.isnull().sum())    # 1,表示缺失一个

# 用来正常显示中文标签的预处理代码
plt.rcParams['font.sans-serif'] = ['simHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig = plt.figure()
p = data.boxplot(return_type='dict')  # 画箱线图，直接使用dataframe的方法
x = p['fliers'][0].get_xdata()  # flies即为异常值的标签
y = p['fliers'][0].get_ydata()
y.sort()   # 从小到大排序，该方法直接改变原对象

# 用annotate添加注释
# 其中有些相近的点，注解会出现重叠，需要一些技巧来控制
# 以下参数是经过调试的，需要具体问题具体调整
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],
                     xy=(x[i], y[i]),
                     xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.08, y[i]))
plt.show()
# plt.savefig('../chart/箱盒图.png')