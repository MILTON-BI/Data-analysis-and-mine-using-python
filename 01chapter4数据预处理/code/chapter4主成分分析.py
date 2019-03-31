import pandas as pd
from sklearn.decomposition import PCA

data = pd.read_excel('../../data1/principal_component.xls')
pca = PCA(n_components=3)
pca.fit(data)
low_d = pca.transform(data)   # 用它来降低维度
pd.DataFrame(low_d).to_excel('../outputfile/dimention_redocts.xls')
print(pca.components_)    # 返回模型的各个特征向量
print(pca.explained_variance_ratio_)   # 返回各个成分各自的方差百分比（贡献率）