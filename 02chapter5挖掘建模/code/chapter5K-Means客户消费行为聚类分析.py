import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


data = pd.read_excel('../../data1/consumption_data.xls', index_col='Id')
# print(data1)

k = 3  # 聚类类别
epochs = 500  # 参数：聚类的最大循环次数

norm_data = (data - data.mean()) / data.std()   # 数据归一化

# 建立模型和训练
model = KMeans(n_clusters=k, n_jobs=4, max_iter=epochs)  # 分为k类，并发数为4，训练轮次为500
model.fit(norm_data)    # 模型训练

# print(model.labels_)    # 输出各条记录（行）对应的类别标签（0\1\2）
# print(model.cluster_centers_)   # 输出聚类中心，形状为一个3*3矩阵（3维数据空间，分3类）

# 显示结果
r1 = pd.Series(model.labels_).value_counts()   # 统计各个类别的数目。value_counts用来统计同类标签的个数
# print(r1)
r2 = pd.DataFrame(model.cluster_centers_)   # 显示各聚类中心，转换成dataframe数据格式
# print(r2)
r = pd.concat([r2, r1], axis=1)     # 横向连接(axis=0为纵向)，得到各聚类中心下聚类的个数
r.columns = list(data.columns) + [u'类别数目']      # 重命名表头，追加添加‘类别数目’一列
# print(r)

# 详细输出原始数据及其类别
rr = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)  # 输出每个样本对应的类别
rr.columns = list(data.columns) + [u'聚类类别']  # 重命名表头
# rr.to_excel('../outputfiles/K-means聚类结果.xls')

# 可视化：聚类后的概率密度函数
# def density_plot(data1):#
#     p = data1.plot(kind='kde', linewidth=2, color='red', subplots=True, sharex=False)
#     [p[i].set_ylabel(u'密度') for i in range(k)]
#     plt.legend()
#     return plt
# pic_output = '../outputfiles/pd_'   # 概率密度图文件名的前缀
# for i in range(k):
#     density_plot(data1[rr[u'聚类类别']==i]).savefig(u'%s%s.png' % (pic_output, i))

# # 用TSNE可视化工具进行数据降维，并显示结果
# from sklearn.manifold import TSNE
#
# tsne = TSNE()
# tsne.fit_transform(norm_data)   # 进行数据降维
# tsne_trans = pd.DataFrame(tsne.embedding_, index=rr.index) # 转换数据格式
# # print(tsne_trans)
#
# # 不同聚类类别用不同颜色和样式绘图
# d1 = tsne_trans[rr[u'聚类类别']==0]
# plt.plot(d1[0], d1[1], 'r.')
# d2 = tsne_trans[rr[u'聚类类别']==1]
# plt.plot(d2[0], d2[1], 'go')
# d3 = tsne_trans[rr[u'聚类类别']==2]
# plt.plot(d3[0], d3[1], 'b*')
# # plt.show()
# plt.savefig('../outputfiles/kmeans聚类结果tsne图像.jpg')




