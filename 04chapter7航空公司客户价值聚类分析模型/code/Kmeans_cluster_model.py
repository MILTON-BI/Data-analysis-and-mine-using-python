import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


model_data = pd.read_excel('../outputfiles/经过清洗和预处理的数据.xls')
# print(model_data)

# 参数设置
k = 5  # 聚类的类别数
epochs = 1000

# 调用kmeans算法
k_model = KMeans(n_clusters=k, n_jobs=4, max_iter=epochs)
# n_jobs是并行数，一般等于cup核数量较好
k_model.fit(model_data)
# print(k_model.cluster_centers_)
# print(k_model.labels_)

# 显示聚类结果
r1 = pd.Series(k_model.labels_).value_counts()  # 统计各类别数目
r2 = pd.DataFrame(k_model.cluster_centers_)   # 聚类中心
r3 = pd.Series(['客户群1', '客户群2', '客户群4', '客户群4', '客户群5'])
r = pd.concat([r2, r1], axis=1)
r = pd.concat([r3, r], axis=1)
r.columns = [u'客户分类'] + list(model_data.columns) + [u'类别数目']
# print(r)
r.to_excel('../outputfiles/KmeansCluster_centers+classCounts.xls', index=False)


# 输出详细数据及聚类类别
result = pd.concat([model_data, pd.Series(k_model.labels_, index=model_data.index)], axis=1)
# 每个样本对应的类别
result.columns = list(model_data.columns) + [u'聚类类别']   # 重命名表头
# print(result)
result.to_excel('../outputfiles/Kmeans_cluster_result.xls')


# 结果可视化
# # 用TSNE可视化工具进行数据降维，并显示结果
from sklearn.manifold import TSNE

tsne = TSNE(n_components=3, init='pca', random_state=0)
tsne.fit_transform(model_data)   # 进行数据降维
tsne_trans = pd.DataFrame(tsne.embedding_, index=result.index) # 转换数据格式
# print(tsne_trans)

# 不同聚类类别用不同颜色和样式绘图
d1 = tsne_trans[result[u'聚类类别'] == 0]
plt.plot(d1[0], d1[1], 'r.')
d2 = tsne_trans[result[u'聚类类别'] == 1]
plt.plot(d2[0], d2[1], 'go')
d3 = tsne_trans[result[u'聚类类别'] == 2]
plt.plot(d3[0], d3[1], 'b*')
d4 = tsne_trans[result[u'聚类类别'] == 3]
plt.plot(d4[0], d4[1], 'yx')
d5 = tsne_trans[result[u'聚类类别'] == 4]
plt.plot(d5[0], d5[1], 'cs')

# plt.show()
plt.savefig('../outputfiles/kmeans_cluster_tsnePic.jpg')