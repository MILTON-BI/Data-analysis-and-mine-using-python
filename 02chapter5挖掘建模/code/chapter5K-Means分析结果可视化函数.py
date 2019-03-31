import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def density_plot(data, title):
    plt.figure()
    for i in range(len(data.iloc[0])):  # 逐列作图
        (data.iloc[:, i]).plot(kind='kde', color='red', label=data.colomns[i], linewidth=2)
    plt.ylabel(u'密度')
    plt.xlabel(u'人数')
    plt.title(u'聚类类别%s各属性的概率密度曲线' % title)
    plt.legend()
    plt.savefig('../outputfiles/K-Means分析结果的概率密度曲线.jpg')
    return plt
