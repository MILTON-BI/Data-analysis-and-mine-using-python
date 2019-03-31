import pandas as pd

data = pd.read_excel('../outputfiles/data_processed.xls')
data = data.iloc[: len(data)-5]   # 不使用最后5个数据

# D盘白噪声检测
from statsmodels.stats.diagnostic import acorr_ljungbox as AL
[[lb], [p]] = AL(data['CWXT_DB:184:D\\'], lags=1)
if p < 0.05:
    print('D盘原始序列为非白噪声序列，对应的p值为%s' % p)
else:
    print('D盘原始序列为白噪声序列，对应的p值为%s' % p)

# D盘的一阶差分的白噪声检测
[[lb1], [p1]] = AL(data['CWXT_DB:184:D\\'].diff().dropna(), lags=1)
if p1 < 0.05:
    print('D盘原始序列的一阶差分为非白噪声序列，对应的p值为%s' % p1)
else:
    print('D盘原始序列的一阶差分为白噪声序列，对应的p值为%s' % p1)

# C盘白噪声检测
from statsmodels.stats.diagnostic import acorr_ljungbox as AL
[[lb2], [p2]] = AL(data['CWXT_DB:184:C\\'], lags=1)
if p2 < 0.05:
    print('C盘原始序列为非白噪声序列，对应的p值为%s' % p2)
else:
    print('C盘原始序列为白噪声序列，对应的p值为%s' % p2)

# C盘的一阶差分的白噪声检测
[[lb3], [p3]] = AL(data['CWXT_DB:184:C\\'].diff().dropna(), lags=1)
if p3 < 0.05:
    print('C盘原始序列的一阶差分为非白噪声序列，对应的p值为%s' % p3)
else:
    print('C盘原始序列的一阶差分为白噪声序列，对应的p值为%s' % p3)