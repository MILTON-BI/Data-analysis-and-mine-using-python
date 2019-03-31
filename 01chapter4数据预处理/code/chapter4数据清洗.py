import pandas as pd
import numpy as np
from scipy.interpolate import lagrange  # 需要导入拉格朗日插值函数

data = pd.read_excel('../../data1/catering_sale.xls')
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None  # 过滤数据，将不符合要求的转化为空值
# 定义列向量插值函数
# s为列向量，n为差值位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] # 取数
    y = y[y.notnull()] # 剔除空值
    return lagrange(y.index, list(y))(n)  # 调用拉格朗日插值函数并返回差值结果


# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]: # 如果为空，则需要插值
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel('../outputfile/sales.xls')