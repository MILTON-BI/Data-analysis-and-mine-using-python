import pandas as pd
import numpy as np


# unique：去重
# D = pd.Series([1,2,3,4,5,6,3,1])
# print(D.unique())
# print(np.unique(D))

# random函数
# print(np.random.rand(2,3,4))  # 生成2*3*4的随机矩阵，元素分布在0-1
# print(np.random.randn(3,3,3))   # 生成一个元素服从标准正态分布的随机矩阵，无参数则默认输出一个值
# print(np.random.randint(1,300,[4,4]))   # 生成1-300的16个随机整数，按4*4矩阵形式
# print(np.random.randint(1,300,16))   # 生成1-300的16个随机整数，默认排列为一维数组

# PCA:主成分分析（降维）
from sklearn.decomposition import PCA
D = np.random.rand(10, 4)
pca = PCA()
pca.fit(D)
# print(pca.fit(D))   # PCA(copy=True, iterated_power='auto', n_components=None, random_state=None,
#   svd_solver='auto', tol=0.0, whiten=False)
print(pca.components_)
print(pca.explained_variance_ratio_)
# print(sum([0.68030002,0.15683715,0.09124387,0.07161896]))
