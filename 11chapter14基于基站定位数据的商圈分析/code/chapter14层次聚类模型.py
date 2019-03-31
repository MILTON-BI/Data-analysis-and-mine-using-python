import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
# 导入scipy的层次聚类函数，用来做谱系聚类图
from sklearn.cluster import AgglomerativeClustering
# 导入sklearn的层次聚类函数
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../outputfiles/standardized_data.xls', index_col='基站编号')
# print(data)

# 画谱系聚类图
Z = linkage(data, method='ward', metric='euclidean')  # 普洗聚类图
P = dendrogram(Z, 0) # 画谱系聚类图
# plt.show()
# plt.savefig('../outputfiles/谱系聚类图.jpg')
# 根据谱系聚类图可以看出，聚类类别数可以取3(k=3)

# 层次聚类算法
k = 3
model = AgglomerativeClustering(n_clusters=k, linkage='ward')
model.fit(data)

# 详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
r.to_excel('../outputfiles/层次聚类结果.xls')


# 结果可视化
style = ['ro-', 'go-', 'bo-']
xlabels = ['工作日人均停留时间', '凌晨人均停留时间', '周末人均停留时间', '日均人流量']
pic_output = '../outputfiles/type_'   # 图片存储文件的前缀

for i in range(k): # 按不同样式逐一作图
    plt.figure()
    tmp = r[r['聚类类别'] == i].iloc[:, :4]  # 提取每一类
    # print(tmp)
    # [146 rows x 4 columns]
    # [148 rows x 4 columns]
    # [137 rows x 4 columns]
    for j in range(len(tmp)):
        plt.plot(range(1, 5), tmp.iloc[j], style[i])
    plt.xticks(range(1, 5), xlabels, rotation=20)   # 坐标轴标签
    plt.subplots_adjust(bottom=0.15)  # 调整底部
    plt.savefig(pic_output + str(i) + '.png')

