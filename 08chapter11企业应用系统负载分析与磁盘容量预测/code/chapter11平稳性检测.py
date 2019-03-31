import pandas as pd

data = pd.read_excel('../outputfiles/data_processed.xls')
data = data.iloc[: len(data)-5]   # 不使用最后5个数据


# 平稳性检测
from statsmodels.tsa.stattools import adfuller as ADF
diff = 0
adf = ADF(data['CWXT_DB:184:D\\'])
while adf[1] >= 0.05:   # adf[1]为p值，p<0.05认为是平稳的
    diff = diff + 1
    adf = ADF(data['CWXT_DB:184:D\\'].diff(diff).dropna())

print('原始数据经过%s阶差分后归于平稳，p值为%s' % (diff, adf[1]))
