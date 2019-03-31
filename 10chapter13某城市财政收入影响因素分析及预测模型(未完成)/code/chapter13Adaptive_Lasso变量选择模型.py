"""模型参数
x1:社会从业人数; x2: 在岗职工工资总额；x3: 社会消费品零售总额; x4: 城镇居民人均可支配收入
x5: 城镇居民人均消费性支出；x6: 年末总人口；x7: 全社会固定资产投资额; x8: 地区生产总值
x9: 第一产业产值; x10: 税收; x11: 居民消费价格指数；x12: 第三产业与第二产业产值比
x13:居民消费水平；y: 财政收入
"""

import pandas as pd
from sklearn.linear_model import Lasso
import numpy as np

data = pd.read_csv('../../data2/C13_data1.csv')
# print(data)
model = Lasso(alpha=10, max_iter=10000)
model.fit(data.iloc[:, :13], data['y'])
print(model.coef_)
# [-1.85085555e-04 -3.15519378e-01  4.32896206e-01 -3.15753523e-02
#   7.58007814e-02  4.03145358e-04  2.41255896e-01 -3.70482514e-02
#  -2.55448330e+00  4.41363280e-01  5.69277642e+00 -0.00000000e+00
#  -3.98946837e-02]
result = pd.DataFrame({'特征': data.columns[:13], '系数': model.coef_})
result = result.set_index('特征')
result = result.T
print(result)
# result.to_excel('../outputfiles/Apaptive_lasso变量选择模型系数表.xls')
