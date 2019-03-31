import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 参数初始化
inputfile = '../../data1/consumption_data.xls'
k = 3    # 聚类的类别数目
threadhold = 2  # 指定离散点阈值
epochs = 500  # 聚类的最大训练次数

# 读取数据，并用均值-方差进行归一化
data = pd.read_excel(inputfile, index_col='Id')
norm_data = (data - data.mean()) / data.std()

# 聚类
from sklearn.cluster import KMeans
model = KMeans(n_clusters=k, n_jobs=4, max_iter=epochs)  # 分为k类，并发数为4，最大训练次数500
model.fit(norm_data)

# 标准化数据及其类别
result = pd.concat([norm_data, pd.Series(model.labels_, index=data.index)], axis=1)
# 每个样本对应的类别
result.columns = list(data.columns) + [u'聚类类别']   # 重命名表头

# 将数据按相对距离进行变换
norm = []
for i in range(k):  # 逐一处理
    norm_tmp = result[['R', 'F', 'M']][result[u'聚类类别'] == i] - model.cluster_centers_[i]
    norm_tmp = norm_tmp.apply(np.linalg.norm, axis=1)   # 求出绝对距离
    norm.append(norm_tmp / norm_tmp.median())    # 求相对距离，并加入到norm列表。median()作用求中位数
norm = pd.concat(norm)  # 合并

# 可视化
normal_points = norm[norm <= threadhold]   # 正常点
normal_points.plot(style='go')
discrete_points = norm[norm > threadhold]  # 离群点
discrete_points.plot(style='ro')

for i in range(len(discrete_points)):   # 给离群点做标记
    id = discrete_points.index[i]
    n = discrete_points.iloc[i]
    plt.annotate('(%s, %0.2f)' % (id, n), xy=(id, n), xytext=(id, n))

plt.xlabel(u'编号')
plt.ylabel(u'相对距离')
# plt.show()
plt.savefig('../outputfiles/基于聚类的集群点检测结果图.jpg')



