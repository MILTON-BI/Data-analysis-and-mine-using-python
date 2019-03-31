from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel('../data1/catering_sale.xls', index_col=u'日期')

# 过滤异常数据
data = data[(data[u'销量'] > 400) & (data[u'销量'] < 5000)]
# print(data1)
statistics = data.describe()

statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']   # 极差
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']    # 变异系数
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']     # 四分位数间距
print(statistics)