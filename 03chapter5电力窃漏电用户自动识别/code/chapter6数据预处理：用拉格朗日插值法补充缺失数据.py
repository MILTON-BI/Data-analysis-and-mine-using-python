import pandas as pd
from scipy.interpolate import lagrange   # 导入拉格朗日插值函数

inputfile = '../../data2/C6_missing_data.xls'
outputfile = '../outputfiles/missing_data_processed.xls'

data = pd.read_excel(inputfile, header=None)
# print(len(data))    # 每列数据为21
# print(data)

# 定义列向量插值函数
def ployinterp_columns(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]   # 取数据
    print(y)
    y = y[y.notnull()]   # 剔除空值
    return lagrange(y.index, list(y))(n)    # 插值并返回插值结果
#
# # 逐个判断每个元素是否需要插值
for idx in data.columns:
    for j in range(len(data)):
        if (data[idx].isnull())[j]:  # 如果为空则插值
            data[idx][j] = ployinterp_columns(data[idx], j)

data.to_excel(outputfile, header=None, index=False)  # 输出结果
