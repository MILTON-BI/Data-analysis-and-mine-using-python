"""
0. 数据获取：问卷调查
1. 数据集构成：选取6种证型得分，TNM（肿瘤分期系统）分期属性值构成
2. 数据变换
    （1）属性构造：将证型得分换算成整形系数=该证型得分/该证型总分（例如肝气郁结证型总分41）
    （2）数据离散化：见本代码
        因为Apriori关联规则算法无法处理连续型变量，为将原始数据格式转换成合适的建模格式，需要对其进行离散化处理
"""
import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_excel('../../data2/C8_data.xls')
typeLabel = {u'肝气郁结证型系数': 'A',
             u'热毒蕴结证型系数': 'B',
             u'冲任失调证型系数': 'C',
             u'气血两虚证型系数': 'D',
             u'脾胃虚弱证型系数': 'E',
             u'肝肾阴虚证型系数': 'F'}
k = 4    # 需要进行的聚类类别数

keys = list(typeLabel.keys())
result = pd.DataFrame()


"""下面语句用来判断是否主窗口运行
__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
"""
if __name__ == '__main__':
    for i in range(len(keys)):
        # 调用Kmeans算法，进行聚类离散化
        print('正在进行“%s”的聚类......' % keys[i])
        kmodel = KMeans(n_clusters=k, n_jobs=4)  # 一般并行数等于cpu核数
        kmodel.fit(data[[keys[i]]].values)    # 模型训练

        r1 = pd.DataFrame(kmodel.cluster_centers_, columns=[typeLabel[keys[i]]]) # 聚类中心
        r2 = pd.Series(kmodel.labels_).value_counts()   # 统计各类包含的样本数
        r2 = pd.DataFrame(r2, columns=[typeLabel[keys[i]]+'n'])  # 转为dataframe,记录各类别数目
        r = pd.concat([r1, r2], axis=1).sort_values(typeLabel[keys[i]])  # 匹配聚类中心和类别数
        r.index = [1, 2, 3, 4]

        # r[typeLabel[keys[i]]] = pd.rolling_mean(r[typeLabel[keys[i]]], 2)
        r[typeLabel[keys[i]]] = r[typeLabel[keys[i]]].rolling(2).mean()
        # rolling_mean计算相邻两列的均值，以此作为边界点
        # rolling_mean()已经弃用了，转成新的用法df.rolling(参数).mean()
        r[typeLabel[keys[i]]][1] = 0.0
        result = result.append(r.T)  # 这两句代码将原来的聚类中心改为边界点

    result = result.sort_index()  # 按index排序，即按A-F顺序排序
    result.to_excel('../outputfiles/数据聚类离散化结果.xls')



