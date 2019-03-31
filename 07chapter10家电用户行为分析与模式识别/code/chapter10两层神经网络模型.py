# -*- coding=utf-8 -*-
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Activation

# 读入数据并建立训练集和测试集的特征和标签
data_train = pd.read_excel('../../data2/C10_train_neural_network_data.xls')
data_test = pd.read_excel('../../data2/C10_test_neural_network_data.xls')

x_train = data_train.iloc[:, 5:17].values
y_train = data_train.iloc[:, 4].values
x_test = data_test.iloc[:, 5:17].values
y_test = data_test.iloc[:, 4].values

# 构建多层神经网络模型
neural_model = Sequential()
neural_model.add(Dense(17, input_dim=11, activation='relu'))   # 添加输入层、隐藏层1的连接
# model.add(Activation('relu'))
neural_model.add(Dense(10, input_dim=17, activation='relu'))   # 添加隐藏层1、隐藏层2的连接
# model.add(Activation('relu'))
neural_model.add(Dense(1, input_dim=10, activation='sigmoid'))   # 添加隐藏层2、输出层的连接
# model.add(Activation('sigmoid'))

neural_model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
neural_model.fit(x_train, y_train, epochs=200, batch_size=1)
neural_model.save_weights('../outputfiles/二层神经网络权重.model')

r = pd.DataFrame(neural_model.predict_classes(x_test), columns=['预测结果'])
pd.concat([data_test.iloc[:, :5], r], axis=1).to_excel('../outputfiles/测试集测试结果.xls')
print(neural_model.predict(x_test))   # 显示预测结果,0或1
