import pandas as pd
from apriori import *

data = pd.read_excel('../../data1/menu_orders.xls', header=None)
# print(data1)

print(u'\n转换原始数据为0-1矩阵......')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])   # 转换0-1矩阵的过渡函数
b = map(ct, data.as_matrix())   # 用map函数进行转化
data = pd.DataFrame(list(b)).fillna(0)  # 进行转换，空值用0替换
print(u'\n转换完毕。')
del b  # 删除中间变量，节省内存

support = 0.2   # 设定最小支持度
confidence = 0.5    # 设定最小置信度
ms = '---'  # 连接符：默认‘--’，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符
find_rule(data, support, confidence, ms).to_excel('../outputfiles/apriori_rules.xls')