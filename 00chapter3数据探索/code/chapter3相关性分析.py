import pandas as pd

data = pd.read_excel('../data1/catering_sale_all.xls', index_col=u'日期')
# print(data1.corr())  # 显示相关系数矩阵
# print(data1.corr()[u'百合酱蒸凤爪'])  # 百合酱蒸凤爪与所有菜品的相关系数
print(data[u'金银蒜汁蒸排骨'].corr(data[u'原汁原味菜心']))   # 只显示两种菜品的相关系数