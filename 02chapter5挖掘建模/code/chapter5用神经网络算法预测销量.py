"""用单层神经网络进行销量预测"""
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation


data = pd.read_excel('../../data1/sales_data.xls', index_col='序号')

# 数据是类别标签，需要转化为数值标签
# 用1来表示“好”“高”“是”，0表示“坏”“低”“否”
data[data.values == '好'] = 1
data[data.values == '高'] = 1
data[data.values == '是'] = 1
data[data.values != 1] = 0

x = data.iloc[:, :3]
x_data = x.values.astype(int)
y = data.iloc[:, 3]
y_data = y.values.astype(int)
print(x_data, y_data)

# 建立和训练模型
model = Sequential()
model.add(Dense(3, input_shape=(3, )))
model.add(Activation('relu'))   # 用relu函数做激活函数，能大幅度提高准确度
model.add(Dense(1))
model.add(Activation('sigmoid'))  # 由于是0-1输出，所以用sigmoid函数做激活函数

"""
编译模型：
1.由于使用的是二元分类，所以指定损失函数为binary_crossentropy，以及模型为binary
2.其他常见的损失函数还有mean_squared_error\categroical_crossentropy等
3.求解方法(优化器)用adam，此外常用的还有sgd、rmsprop等可选
"""
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

result = model.fit(x=x_data, y=y_data, epochs=1000, batch_size=10) # 训练模型1000次
yp = model.predict_classes(x_data).reshape(len(y_data)) # 分类预测
print(yp)    # [1 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 1 1 0 0 0 0 1 0 0]

from cm_plot import *
cm_plot(y_data, yp).show()