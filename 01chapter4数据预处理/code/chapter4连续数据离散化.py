import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('../../data1/discretization_data.xls')

data = data[u'肝气郁结证型系数'].copy()
# print(data1)
# print(data1.describe())

k = 10
# 等宽离散化，各类别名依次命名为0，1，2...
D1 = pd.cut(data, k, labels=range(k))
# print(D1)

# 等频离散化
w = [i/k for i in range(k+1)]    # 划分k个区间
# print(w)
W = data.describe(percentiles=w)[4:4+k+1]   # 用describe函数自动计算分位数
# print(W)
W[0] = W[0] * 0.99999
# print(W[0])
D2 = pd.cut(data, W, labels=range(k))
# print(D2)

# 聚类离散化
from sklearn.cluster import KMeans
kmodel = KMeans(n_clusters=k, n_jobs=4)  # 建立模型；n_jobs是并行数，一般用于cup较好的机器
kmodel.fit(np.array(data).reshape(-1,1))  # 训练模型
c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)  # 输出聚类中心，并排序（默认是随机排序）
w = c.rolling(2).iloc[1:]  # 相邻两项求中点，作为边界点
w = [0] + list(w[0]) + [data.max()] # 加上首、末边界点
D3 = pd.cut(data, w, labels=range(k))

# 定义可视化函数，显示聚类结果
def cluster_plot(d, k):
    plt.rcParams['font.sans-serif'] = ['simHei']  # 用来正常显示中文标签
    plt.reParams['axes.unicode_minus'] = False   # 用来正常显示负号

    plt.figure(figsize=(8, 3))
    for j in range(k):
        plt.plot(data[d==j], [j for i in d[d==j]], 'ro')

    plt.ylim(-0.5, k-0.5)
    return plt

cluster_plot(D1, k).show()
cluster_plot(D2, k).show()
cluster_plot(D3, k).show()
