"""数据预处理：
   1. 离差标准化
"""
import pandas as pd

data = pd.read_excel('../../data2/C14_business_circle.xls', index_col='基站编号')
# print(data)   # [431 rows x 5 columns]
#    基站编号  工作日上班时间人均停留时间  凌晨人均停留时间  周末人均停留时间  日均人流量
#     36902            78                   521              602            2863
#     36903            144                  600              521            2245
#     36904             95                  457              468            1283
#     36905             69                  596              695            1054

# 数据标准化（离差标准化）
data = (data - data.min()) / (data.max() - data.min())
# data = data.reset_index()
data.to_excel('../outputfiles/standardized_data.xls')
