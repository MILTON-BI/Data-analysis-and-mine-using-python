"""模型参数
x1:社会从业人数; x2: 在岗职工工资总额；x3: 社会消费品零售总额; x4: 城镇居民人均可支配收入
x5: 城镇居民人均消费性支出；x6: 年末总人口；x7: 全社会固定资产投资额; x8: 地区生产总值
x9: 第一产业产值; x10: 税收; x11: 居民消费价格指数；x12: 第三产业与第二产业产值比
x13:居民消费水平；y: 财政收入
"""
import pandas as pd
import numpy as np
from GM11 import GM11

data = pd.read_csv('../../data2/C13_data1.csv')
data.index = range(1994, 2014)
data.loc[2014] = None
data.loc[2015] = None
l = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']
# print(data['x1'])
# print(data['x1'].iloc[0:20])
for i in l:
    f = GM11(data[i].iloc[:20])[0]
    data[i][2014] = f(len(data))   # 2014年预测结果
    data[i][2015] = f(len(data)+1)    # 2015年预测结果
    data[i] = data[i].round(2)  # 保留2位小数

data[1+['y']].to_excel('../outputfiles/data1_GM11.xls')