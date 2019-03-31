#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR


# 参数初始化
data = pd.read_excel('../../data1/bankloan.xls')
# print(data1)
# print(data1.iloc[0])
x = data.iloc[:, :8]
x_data = x.values
y = data.iloc[:, 8]
y_data = y.values
# print(x)
# print(y)


# 建立特征筛选模型
rlr = RLR()  # 建立随机逻辑回归模型，筛选变量
rlr.fit(x, y)  # 训练模型
result = rlr._get_support_mask()

print(result)  # 获取特征筛选结果
# print(rlr.scores_())  # 也可以通过.scores_方法获取各个特征的分数
result = list(result)
# print(result)
print('通过随机逻辑回归模型筛选特征结束。')
print('有效特征为： %s' % ','.join(x.columns[result]))
x_data = x[x.columns[result]].values
print(x_data)

# 建立逻辑回归模型
lr = LR()
lr.fit(x_data, y_data)  # 用筛选后的特征训练模型
print('逻辑回归模型结束。')
print('逻辑回归模型的正确率为： %s' % lr.score(x_data, y_data))  # 0.8142857142857143

