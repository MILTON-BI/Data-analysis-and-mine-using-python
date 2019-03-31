import pandas as pd
import numpy as np

data = pd.read_csv('../../data2/C13_data1.csv')
# print(data)     # [20 rows x 14 columns]

# 对数据进行初步分析
r = [data.min(), data.max(), data.mean(), data.std()]
r = pd.DataFrame(r, index=['Min', 'Max', 'Mean', 'STD']).T
r = np.round(r, 2)
# print(r)
# r.to_excel('../outputfiles/原始数据概括性度量.xls')

# 相关性分析：计算pearson相关系数矩阵
corr = np.round(data.corr(method='pearson'), 2)   # 保留两位小数
# 其中，居民消费价格指数(x11)与财政收入线性关系不显著，而且呈负相关
# 其余变量均与财政收入呈现明显的正相关关系
# print(corr)
# corr.to_excel('../outputfiles/原始数据的相关系数矩阵.xls')
#