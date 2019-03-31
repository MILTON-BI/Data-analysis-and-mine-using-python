import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""---------------------输出处理----------------------"""
# 读取数据
data_file = '../../data2/C6_model.xls'
data = pd.read_excel(data_file)
# print(data)

# 将dataframe对象转换成矩阵，并随机打乱数据
data = data.values
random.shuffle(data)
# print(data)

# 划分训练集和数据集
p = 0.8
train_data = data[:int(len(data)*p), :]  # 前80%作为训练集数据
test_data = data[int(len(data)*p):, :]        # 后20%作为测试集数据
# print(train_data)
# print(test_data)

"""-----------------------CART决策树模型构建---------------------------"""
from sklearn.tree import DecisionTreeClassifier   # 导入决策树模型

# 建立模型并训练
tree = DecisionTreeClassifier()
tree.fit(train_data[:, :3], train_data[:, 3])

# 保存模型
from sklearn.externals import joblib
output_file = '../outputfiles/窃漏电用户自动识别CART决策树模型.pkl'
joblib.dump(tree, output_file)

# 用cm_plot模块可视化混淆矩阵
from cm_plot import *
cm_plot(train_data[:, 3], tree.predict(train_data[:, :3])) # sklearn使用predict方法直接给出预测结果
plt.show()
# plt.savefig('../outputfiles/窃漏电用户自动识别决策树预测结果的混淆矩阵.jpg')

"""-----------------------用ROC曲线评价模型，使用测试集数据---------------------------"""
from sklearn.metrics import roc_curve   # 导入roc曲线绘制的函数

fpr, tpr, thresholds = roc_curve(test_data[:, 3], tree.predict_proba(test_data[:, :3])[:, 1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of CART')  # 绘制roc曲线
plt.ylabel('True Positive Rate')    # 设置y坐标轴标签
plt.xlabel('False Positive Rate')   # 设置x坐标轴标签
plt.ylim(0, 1.05)    # 设置y轴方向的边界范围
plt.xlim(0, 1.05)    # 设置x轴方向的边界范围
plt.legend(loc=4)    # 设置图例
# plt.show()
plt.savefig('../outputfiles/窃漏电用户自动识别的CART决策树模型评价的ROC曲线.jpg')
