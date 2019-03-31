import pandas as pd
from random import shuffle
from sklearn import svm
import pickle
from sklearn import metrics

data = pd.read_csv('../../data2/C9_moment.csv', encoding='GBK')
# print(data)

"""数据抽取"""
# 随机打乱数据
data = data.values
# print(data)
shuffle(data)

# 划分训练集和测试集
data_train = data[:int(len(data)*0.8), :]   # 前80%为训练集
data_test = data[int(len(data)*0.8):, :]    # 后20%为测试集

"""构建支持向量机SVM模型"""
x_train = data_train[:, 2:] * 30   # 乘以30放大特征
# 第一列为分类的类别，第二列为序号（无意义，舍弃），以后列为特征值。
y_train = data_train[:, 0].astype(int)
x_test = data_test[:, 2:] * 30
y_test = data_test[:, 0].astype(int)

# 建立和训练模型
svm_model = svm.SVC(gamma=0.01, C=100)
svm_model.fit(x_train, y_train)
# 用pickle保存模型
pickle.dump(svm_model, open('../outputfiles/svm.model', 'wb'))
# 以后可以用下面代码加载模型
# model = pickle.load(open('../outputfiles/svm.model', 'rb'))

# 使用metrics函数，生成混淆矩阵
# 训练样本的混淆矩阵
cm_train = metrics.confusion_matrix(y_train, svm_model.predict(x_train))
print(cm_train)  # 下面是训练集混淆矩阵输出，准确率162/162=100%
# [[110   0   0]
#  [  0  37   0]
#  [  0   0  15]]
# 测试样本的混淆矩阵
cm_test = metrics.confusion_matrix(y_test, svm_model.predict(x_test))
print(cm_test)   # 下面是测试集混淆矩阵输出，准确率40/41=97.56%
# [[13  0  0  0]
#  [ 0 15  0  0]
#  [ 0  0 12  0]
#  [ 0  0  1  0]]

# 保存结果
outputfile1 = '../outputfiles/训练数据的混淆矩阵.xls'
outputfile2 = '../outputfiles/测试数据的混淆矩阵.xls'
pd.DataFrame(cm_train, index=range(1, 4), columns=range(1, 4)).to_excel(outputfile1)
pd.DataFrame(cm_test, index=range(1, 5), columns=range(1, 5)).to_excel(outputfile2)



