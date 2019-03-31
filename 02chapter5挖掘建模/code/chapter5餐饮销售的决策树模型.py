import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC

data = pd.read_excel('../../data1/sales_data.xls', index_col='序号')

# print(data1)

# 数据是类别标签，需要转化为数值标签
# 用1来表示“好”“高”“是”，-1表示“坏”“低”“否”
data[data.values == '好'] = 1
data[data.values == '高'] = 1
data[data.values == '是'] = 1
data[data.values != 1] = -1

x = data.iloc[:, :3]
x_data = x.values.astype(int)
y = data.iloc[:, 3]
y_data = y.values.astype(int)
# print(x, y, x.shape, y.shape)

# 建立模型和训练
dtc = DTC(criterion='entropy')  # 基于信息熵建立决策树模型
dtc.fit(x_data, y_data)   # 训练模型

# 导入相关函数，可视化决策树
# 导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

with open('tree.dot', 'w') as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=f)



