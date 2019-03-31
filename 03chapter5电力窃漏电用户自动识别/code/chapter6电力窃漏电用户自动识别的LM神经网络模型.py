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
print(train_data)
print(test_data)

"""-----------------------LM神经网络模型构建---------------------------"""
from keras.models import Sequential   # 导入神经网络初始化函数
from keras.layers.core import Dense, Activation   # 导入神经网络层函数、激活函数

net = Sequential()   # 建立神经网络
net.add(Dense(10, input_dim=3))   # 添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation('relu'))   # 隐藏层使用relu激活函数
net.add(Dense(1, input_dim=10))   # 添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid'))   # 输出层使用sigmoid激活函数

# 编译模型，使用adam优化器和binary_crossentropy损失函数
net.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 模型训练1000轮，并保存参数
net.fit(x=train_data[:, :3], y=train_data[:, 3], epochs=1000, batch_size=1)
output_file = '../outputfiles/电力窃漏电用户自动识别的LM神经网络模型.model'
net.save_weights(output_file)   # 保存为HDF5文件类型
# 再次使用需要导入from keras.models import load_model
# 并用model.load_model(filepath)载入模型


# 用模型进行预测
predict_result = net.predict_classes(train_data[:, :3]).reshape(len(train_data))  # 预测结果变形
# keras的predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n*1维数组，而不是通常的1*n维

# 用cm_plot模块可视化混淆矩阵
from cm_plot import *
cm_plot(train_data[:, 3], predict_result)
plt.show()
# plt.savefig('../outputfiles/窃漏电用户自动识别LM神经网络预测结果的混淆矩阵.jpg')

"""-----------------------用ROC曲线评价模型，使用测试集数据---------------------------"""
from sklearn.metrics import roc_curve   # 导入roc曲线绘制的函数

test_predict_result = net.predict_classes(test_data[:, :3]).reshape(len(test_data)) # 预测结果变形
fpr, tpr, thresholds = roc_curve(test_data[:, 3], test_predict_result, pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of LM')  # 绘制roc曲线
plt.ylabel('True Positive Rate')    # 设置y坐标轴标签
plt.xlabel('False Positive Rate')   # 设置x坐标轴标签
plt.ylim(0, 1.05)    # 设置y轴方向的边界范围
plt.xlim(0, 1.05)    # 设置x轴方向的边界范围
plt.legend(loc=4)    # 设置图例
plt.show()
# plt.savefig('../outputfiles/窃漏电用户自动识别的LM神经网络模型评价的ROC曲线.jpg')