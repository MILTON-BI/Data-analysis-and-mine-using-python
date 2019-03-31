import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../outputfiles/data_processed.xls')

# 时序图检测
plt.plot(data['COLLECTTIME'], data['CWXT_DB:184:C\\'])
plt.xlabel(u'数据采集时间')
plt.xticks(rotation=45)
plt.ylabel(u'磁盘已用容量')
# plt.show()
plt.savefig('../outputfiles/C盘存储使用时序图.jpg')