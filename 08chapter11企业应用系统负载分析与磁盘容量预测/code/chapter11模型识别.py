"""模型识别，确定最佳的p、d、q值"""
import pandas as pd

data = pd.read_excel('../outputfiles/data_processed.xls', index_col='COLLECTTIME')
data = data.iloc[: len(data)-5]   # 不使用最后5个数据
x_data = data['CWXT_DB:184:D\\']
# print(x_data)


from statsmodels.tsa.arima_model import ARIMA
# 定阶
pmax = int(len(x_data)/10)   # 一般阶数不超过len/10
qmax = int(len(x_data)/10)   # 一般阶数不超过len/10
print('pmax=', pmax)
bic_matrix = []    # bic矩阵
for p in range(pmax):
    temp = []
    for q in range(qmax):
        try:  # 存在部分报错，所以用try来跳过报错
            temp.append(ARIMA(x_data, (p, 1, q)).fit().bic)
        except:
            temp.append(None)
    bic_matrix.append(temp)
# print(bic_matrix)
bic_matrix = pd.DataFrame(bic_matrix)   # 从中可以找出最小值
# print(bic_matrix)
# bic_matrix = bic_matrix.fillna('')
# print(bic_matrix)

p, q = bic_matrix.stack().idxmin()  # 先用stack展平，然后用idxmin找出最小值位置
print('BIC的最小p值和q值分别为：%s、%s' % (p, q))
# 数据序列   D盘使用空间
# 模型类型   ARIMA(1,1,1)
# 最小BIC值  1271.89