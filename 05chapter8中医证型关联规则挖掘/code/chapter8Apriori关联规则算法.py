import pandas as pd
from apriori import *
import time

data = pd.read_csv('../../data2/C8_apriori.txt', header=None, dtype=object)

start = time.clock()   # 开始计时
print(u'\n转换原始数据为0-1矩阵')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)]) # 转换的过渡函数，即将标签数据转换成1
b = map(ct, data.values)   # 用map方式执行
data = pd.DataFrame(list(b)).fillna(0)   # 实现矩阵变换，除了1以外，其余为空，空值用0填充
end = time.clock()
print(u'\n转换完毕，用时：%0.2f秒' % (end-start))
del b   # 删除中间变量b,节省内存

support = 0.06    # 最小支持度
confidence = 0.75   # 最小置信度
ms = '---'   # 连接符，默认'--'，用来区分不同元素，如A---B。需要保证原始表格中不含有该字符

start = time.clock()
print(u'\n开始搜索关联规则.....')
result = find_rule(data, support, confidence, ms)
end = time.clock()
print(u'\n搜索完毕，用时：%0.2f秒' % (end-start))
# print(result)
result.to_excel('../outputfiles/关联规则.xls')