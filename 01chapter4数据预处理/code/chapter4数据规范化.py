import pandas as pd
import pandasql

data = pd.read_excel('../../data1/normalization_data.xls')
print(data)

# 最大最小规范化
norm_maxmin = (data - data.min()) / (data.max() - data.min())
print(norm_maxmin)

# 0-均值规范化
norm_zeroMean = (data - data.mean()) / data.std()
print(norm_zeroMean)

# 小数定标规范化
norm_decimal = data / 1000
print(norm_decimal)